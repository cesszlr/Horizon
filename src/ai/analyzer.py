"""Content analysis using AI."""

import asyncio
import json
import re
from typing import List, Optional
from tenacity import retry, stop_after_attempt, wait_exponential
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, MofNCompleteColumn

from .client import AIClient
from .prompts import (
    CONTENT_ANALYSIS_SYSTEM,
    CONTENT_ANALYSIS_USER,
    build_content_analysis_system_prompt,
    build_content_analysis_user_prompt,
)
from .utils import parse_json_response
from ..models import CategoryRule, ContentItem

DEFAULT_THROTTLE_SEC = 0.0


class ContentAnalyzer:
    """Analyzes content items using AI to determine importance."""

    def __init__(
        self,
        ai_client: AIClient,
        categories: Optional[dict[str, CategoryRule]] = None,
    ):
        self.client = ai_client
        self.categories = categories
        self.system_prompt = build_content_analysis_system_prompt(categories)
        self.user_prompt_template = build_content_analysis_user_prompt(categories)

    @staticmethod
    def _parse_json_response(response: str) -> Optional[dict]:
        """Try multiple strategies to extract a JSON object from an AI response.

        Returns the parsed dict, or None if all strategies fail.
        """
        return parse_json_response(response)

    def _get_throttle_sec(self) -> float:
        """Return the configured inter-item throttle, clamped to zero or above."""
        config = getattr(self.client, "config", None)
        throttle_sec = getattr(config, "throttle_sec", DEFAULT_THROTTLE_SEC)
        return max(throttle_sec, 0.0)

    def _get_concurrency(self) -> int:
        """Return the configured analysis concurrency, clamped to 1 or above."""
        config = getattr(self.client, "config", None)
        concurrency = getattr(config, "analysis_concurrency", 1)
        return max(concurrency, 1)

    async def analyze_batch(self, items: List[ContentItem]) -> List[ContentItem]:
        throttle_sec = self._get_throttle_sec()
        concurrency = self._get_concurrency()
        semaphore = asyncio.Semaphore(concurrency)

        async def _process(item: ContentItem, index: int, progress_task) -> ContentItem:
            async with semaphore:
                try:
                    await self._analyze_item(item)
                except Exception as e:
                    print(f"Error analyzing item {item.id}: {e}")
                    item.ai_category = None
                    item.ai_score = 0.0
                    item.ai_reason = "Analysis failed"
                    item.ai_summary = item.title
                if throttle_sec > 0 and index < len(items) - 1:
                    await asyncio.sleep(throttle_sec)
            progress.advance(progress_task)
            return item

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            MofNCompleteColumn(),
            transient=True,
        ) as progress:
            task = progress.add_task("Analyzing", total=len(items))
            coros = [
                _process(item, i, task) for i, item in enumerate(items)
            ]
            analyzed_items = await asyncio.gather(*coros)

        return analyzed_items

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1.5, min=2, max=30)
    )
    async def _analyze_item(self, item: ContentItem) -> None:
        """Analyze a single content item.

        Args:
            item: Content item to analyze (modified in-place)
        """
        # Prepare content section
        content_section = ""
        if item.content:
            # Split off comments if present
            content_text = item.content
            if "--- Top Comments ---" in content_text:
                main, comments_part = content_text.split("--- Top Comments ---", 1)
                content_section = f"Content: {main.strip()[:800]}"
            else:
                content_section = f"Content: {content_text[:1000]}"

        # Prepare discussion section (comments, engagement)
        discussion_parts = []
        if item.content and "--- Top Comments ---" in item.content:
            comments_part = item.content.split("--- Top Comments ---", 1)[1]
            discussion_parts.append(f"Community Comments:\n{comments_part[:1500]}")

        meta = item.metadata
        engagement_items = []
        if meta.get("score"):
            engagement_items.append(f"score: {meta['score']}")
        if meta.get("descendants"):
            engagement_items.append(f"{meta['descendants']} comments")
        if meta.get("favorite_count"):
            engagement_items.append(f"{meta['favorite_count']} likes")
        if meta.get("retweet_count"):
            engagement_items.append(f"{meta['retweet_count']} retweets")
        if meta.get("reply_count"):
            engagement_items.append(f"{meta['reply_count']} replies")
        if meta.get("views"):
            engagement_items.append(f"{meta['views']} views")
        if meta.get("bookmarks"):
            engagement_items.append(f"{meta['bookmarks']} bookmarks")
        if meta.get("upvote_ratio"):
            engagement_items.append(f"upvote ratio: {meta['upvote_ratio']:.0%}")
        if engagement_items:
            discussion_parts.append(f"Engagement: {', '.join(engagement_items)}")
        if meta.get("discussion_url"):
            discussion_parts.append(f"Discussion: {meta['discussion_url']}")
        if meta.get("community_note"):
            discussion_parts.append(f"Community Note: {meta['community_note']}")

        discussion_section = "\n".join(discussion_parts) if discussion_parts else ""

        # Generate user prompt
        category_hint = item.metadata.get("category") or ""
        user_prompt = self.user_prompt_template.format(
            category_hint=category_hint,
            title=item.title,
            source=f"{item.source_type.value}",
            author=item.author or "Unknown",
            url=str(item.url),
            content_section=content_section,
            discussion_section=discussion_section,
        )

        provider_name = getattr(getattr(self.client, "config", None), "provider", "unknown")
        provider_str = provider_name.value if hasattr(provider_name, "value") else str(provider_name)
        model_str = getattr(getattr(self.client, "config", None), "model", "unknown")

        # Get AI completion
        try:
            response = await self.client.complete(
                system=self.system_prompt,
                user=user_prompt,
            )
        except Exception as e:
            print(f"Error calling AI complete for {item.id} (provider: {provider_str}, model: {model_str}): {e}")
            raise

        # Parse JSON response with robust fallback
        result = self._parse_json_response(response)
        if result is None:
            debug_info = getattr(self.client, "last_debug_info", {})
            print(f"Warning: could not parse analysis response for {item.id}, using defaults")
            print(f"Request Info - Provider: {provider_str}, Model: {model_str}")
            if debug_info.get("status_code"):
                print(f"HTTP Info - Status: {debug_info.get('status_code')}, Request-ID: {debug_info.get('request_id') or 'N/A'}")
            if debug_info.get("finish_reason"):
                print(f"Model Info - Finish Reason: {debug_info.get('finish_reason')}, Tokens: prompt={debug_info.get('prompt_tokens')}, completion={debug_info.get('completion_tokens')}")
            if debug_info.get("has_reasoning_content"):
                print(f"Reasoning Info - Reasoning Content Len: {debug_info.get('reasoning_content_len')}")
            print(f"Prompt Info - System prompt len: {len(self.system_prompt)}, User prompt len: {len(user_prompt)}")
            print(f"Response Info - Type: {type(response)}, Len: {len(str(response)) if response else 0}")
            print("--- FAILED RESPONSE DATA START ---")
            print(response)
            print("--- FAILED RESPONSE DATA END ---")
            item.ai_category = None
            item.ai_score = 0.0
            item.ai_reason = "Analysis response parse failed"
            item.ai_summary = item.title
            item.ai_tags = []
            return

        # Update item with analysis results
        item.ai_category = result.get("category")
        item.ai_score = float(result.get("score", 0))
        item.ai_reason = result.get("reason", "")
        item.ai_summary = result.get("summary", item.title)
        item.ai_tags = result.get("tags", [])

        # If category is not pre-defined, populate it with AI category
        if item.ai_category and not item.metadata.get("category"):
            item.metadata["category"] = item.ai_category
