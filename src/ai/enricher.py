"""Content enrichment using AI (second-pass analysis).

For items that pass the score threshold, this module:
1. Searches the web for relevant context (via DuckDuckGo)
2. Feeds search results + item content to AI to generate grounded background knowledge
3. Caches enrichment results across profiles to avoid duplicate AI calls and token usage
"""

import asyncio
import json
import re
import sys
import os
from typing import List, Optional, Dict, Any
from tenacity import retry, stop_after_attempt, wait_exponential
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, MofNCompleteColumn
from ddgs import DDGS
import httpx

from .client import AIClient
from .prompts import (
    CONCEPT_EXTRACTION_SYSTEM, CONCEPT_EXTRACTION_USER,
    CONTENT_ENRICHMENT_SYSTEM, CONTENT_ENRICHMENT_USER,
)
from .utils import parse_json_response
from ..models import ContentItem


class ContentEnricher:
    """Enriches high-scoring content items with background knowledge."""

    def __init__(self, ai_client: AIClient, cache: Optional[Dict[str, Dict[str, Any]]] = None):
        self.client = ai_client
        # Shared or instance-level cache mapping item.id -> enriched metadata dict
        self.cache: Dict[str, Dict[str, Any]] = cache if cache is not None else {}

    def _get_concurrency(self) -> int:
        """Return the configured enrichment concurrency, clamped to 1 or above."""
        config = getattr(self.client, "config", None)
        concurrency = getattr(config, "enrichment_concurrency", 1)
        return max(concurrency, 1)

    async def enrich_batch(self, items: List[ContentItem]) -> None:
        """Enrich items in-place with background knowledge.

        Args:
            items: Content items to enrich (modified in-place)
        """
        concurrency = self._get_concurrency()
        semaphore = asyncio.Semaphore(concurrency)

        async def _process(item: ContentItem, progress_task) -> None:
            async with semaphore:
                try:
                    await self._enrich_item(item)
                except Exception as e:
                    print(f"Error enriching item {item.id}: {e}, falling back to translation")
                    await self._translate_item(item)
            progress.advance(progress_task)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            MofNCompleteColumn(),
            transient=True,
        ) as progress:
            task = progress.add_task("Enriching", total=len(items))
            coros = [
                _process(item, task) for item in items
            ]
            await asyncio.gather(*coros)

    async def _web_search(self, query: str, max_results: int = 3) -> list:
        """Search the web for context via DuckDuckGo.

        Returns:
            List of dicts with keys: title, url, body
        """
        try:
            # Suppress primp "Impersonate ... does not exist" stderr warning
            stderr = sys.stderr
            sys.stderr = open(os.devnull, "w")
            try:
                ddgs = DDGS()
                results = await asyncio.to_thread(ddgs.text, query, max_results=max_results)
            finally:
                sys.stderr.close()
                sys.stderr = stderr
        except Exception:
            return []

        return [
            {"title": r.get("title", ""), "url": r.get("href", ""), "body": r.get("body", "")}
            for r in (results or [])
        ]

    @staticmethod
    def _parse_json_response(response: str) -> Optional[dict]:
        """Try multiple strategies to extract a JSON object from an AI response.

        Returns the parsed dict, or None if all strategies fail.
        """
        return parse_json_response(response)

    async def _extract_concepts(self, item: ContentItem, content_text: str) -> List[str]:
        """Ask AI to identify concepts that need explanation.

        Args:
            item: Content item
            content_text: Extracted content text

        Returns:
            List of search queries for concepts that need explanation
        """
        user_prompt = CONCEPT_EXTRACTION_USER.format(
            title=item.title,
            summary=item.ai_summary or item.title,
            tags=", ".join(item.ai_tags) if item.ai_tags else "",
            content=content_text[:1000],
        )

        try:
            response = await self.client.complete(
                system=CONCEPT_EXTRACTION_SYSTEM,
                user=user_prompt,
            )
            result = self._parse_json_response(response)
            if result is None:
                return []
            queries = result.get("queries", [])
            return queries[:3]
        except Exception:
            return []

    async def _fetch_full_text_fallback(self, url: str) -> str:
        """Fetch minimal clean webpage text if content is too short."""
        try:
            async with httpx.AsyncClient(timeout=8.0, follow_redirects=True) as client:
                headers = {"User-Agent": "Mozilla/5.0 (compatible; HorizonBot/2.0)"}
                resp = await client.get(url, headers=headers)
                if resp.status_code == 200:
                    text = resp.text
                    # Strip script, style, and html tags
                    text = re.sub(r"<(script|style).*?</\1>", " ", text, flags=re.DOTALL | re.IGNORECASE)
                    text = re.sub(r"<[^>]+>", " ", text)
                    text = re.sub(r"\s+", " ", text).strip()
                    return text[:3000]
        except Exception:
            pass
        return ""

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1.5, min=2, max=30)
    )
    async def _enrich_item(self, item: ContentItem) -> None:
        """Enrich a single item with background knowledge.

        Args:
            item: Content item to enrich (modified in-place via metadata)
        """
        # Check cache first (for cross-profile reuse)
        if item.id in self.cache:
            cached_meta = self.cache[item.id]
            for k, v in cached_meta.items():
                item.metadata[k] = v
            return

        # Extract content text and comments separately
        content_text = ""
        comments_text = ""
        if item.content:
            if "--- Top Comments ---" in item.content:
                main, comments_part = item.content.split("--- Top Comments ---", 1)
                content_text = main.strip()[:4000]
                comments_text = comments_part.strip()[:2000]
            else:
                content_text = item.content[:4000]

        # If content is too brief, attempt light web fetch
        if len(content_text.strip()) < 150:
            full_text = await self._fetch_full_text_fallback(str(item.url))
            if full_text:
                content_text = full_text

        # Step 1: AI identifies concepts to explain
        queries = await self._extract_concepts(item, content_text)

        # Step 2: Search web for each concept
        all_results = []
        web_sections = []
        for query in queries:
            results = await self._web_search(query)
            all_results.extend(results)
            if results:
                lines = [f"- [{r['title']}]({r['url']}): {r['body']}" for r in results]
                web_sections.append(f"**{query}:**\n" + "\n".join(lines))
        web_context = "\n\n".join(web_sections) if web_sections else ""

        # Index of available URLs for citation validation
        available_urls = {r["url"]: r["title"] for r in all_results if r.get("url")}

        # Step 3: AI generates background grounded in search results
        user_prompt = CONTENT_ENRICHMENT_USER.format(
            title=item.title,
            url=str(item.url),
            summary=item.ai_summary or item.title,
            score=item.ai_score or 0,
            reason=item.ai_reason or "",
            tags=", ".join(item.ai_tags) if item.ai_tags else "",
            content=content_text,
            comments_section=f"\n**Community Comments:**\n{comments_text}" if comments_text else "",
            web_context=web_context or "No web search results available.",
        )

        response = await self.client.complete(
            system=CONTENT_ENRICHMENT_SYSTEM,
            user=user_prompt,
        )

        # Parse JSON response with robust fallback
        result = self._parse_json_response(response)
        if result is None:
            print(f"Warning: could not parse enrichment response for {item.id}, falling back to translation")
            print("--- FAILED RESPONSE DATA START ---")
            print(response)
            print("--- FAILED RESPONSE DATA END ---")
            await self._translate_item(item)
            return

        def _get_str_val(val: Any) -> str:
            if val is None:
                return ""
            if isinstance(val, str):
                return val.strip()
            if isinstance(val, dict):
                return str(val.get("text") or val.get("content") or val.get("value") or "").strip()
            if isinstance(val, list):
                return " ".join(str(x) for x in val if x).strip()
            return str(val).strip()

        def _get_list_val(val: Any) -> List[str]:
            if val is None:
                return []
            if isinstance(val, list):
                return [str(x).strip() for x in val if str(x).strip()]
            if isinstance(val, str):
                lines = [re.sub(r"^[-*•\d.]+\s*", "", line).strip() for line in val.split("\n") if line.strip()]
                return [line for line in lines if line]
            return [str(val).strip()]

        # Combine structured sub-fields into per-language metadata
        for lang in ("en", "zh"):
            # Title
            t_val = _get_str_val(result.get(f"title_{lang}") or (result.get("title") if lang == "zh" else ""))
            if t_val:
                item.metadata[f"title_{lang}"] = t_val

            # Key Takeaways (3-5 bullet points)
            raw_takeaways = result.get(f"key_takeaways_{lang}") or result.get(f"takeaways_{lang}") or result.get("key_takeaways")
            takeaways = _get_list_val(raw_takeaways)
            if takeaways:
                item.metadata[f"key_takeaways_{lang}"] = takeaways

            # Deep Dive narrative (self-contained analysis)
            raw_deep_dive = result.get(f"deep_dive_{lang}") or result.get("deep_dive")
            deep_dive = _get_str_val(raw_deep_dive)
            if deep_dive:
                item.metadata[f"deep_dive_{lang}"] = deep_dive

            # Sub-components / summary
            parts = []
            for field in ("whats_new", "why_it_matters", "key_details"):
                text = _get_str_val(result.get(f"{field}_{lang}") or result.get(field))
                if text:
                    parts.append(text)
            if parts:
                item.metadata[f"detailed_summary_{lang}"] = " ".join(parts)
            elif result.get(f"detailed_summary_{lang}") or result.get("detailed_summary"):
                item.metadata[f"detailed_summary_{lang}"] = _get_str_val(result.get(f"detailed_summary_{lang}") or result.get("detailed_summary"))

            # Background
            bg = _get_str_val(result.get(f"background_{lang}") or result.get("background"))
            if bg:
                item.metadata[f"background_{lang}"] = bg

            # Community discussion
            cd = _get_str_val(result.get(f"community_discussion_{lang}") or result.get("community_discussion"))
            if cd:
                item.metadata[f"community_discussion_{lang}"] = cd

        # Store citation sources
        raw_sources = result.get("sources")
        if raw_sources and available_urls:
            sources_list = raw_sources if isinstance(raw_sources, list) else [raw_sources]
            valid = []
            for u in sources_list:
                url_str = str(u.get("url") if isinstance(u, dict) else u).strip()
                if url_str in available_urls:
                    valid.append({"url": url_str, "title": available_urls[url_str]})
            if valid:
                item.metadata["sources"] = valid

        # Backward-compatible fallback fields (English as default)
        item.metadata["detailed_summary"] = item.metadata.get("detailed_summary_en", "") or item.metadata.get("detailed_summary_zh", "")
        item.metadata["background"] = item.metadata.get("background_en", "") or item.metadata.get("background_zh", "")
        item.metadata["community_discussion"] = item.metadata.get("community_discussion_en", "") or item.metadata.get("community_discussion_zh", "")

        # Save to enrichment cache
        cache_entry = {}
        for k in (
            "title_en", "title_zh",
            "key_takeaways_en", "key_takeaways_zh",
            "deep_dive_en", "deep_dive_zh",
            "detailed_summary_en", "detailed_summary_zh",
            "background_en", "background_zh",
            "community_discussion_en", "community_discussion_zh",
            "sources", "detailed_summary", "background", "community_discussion",
        ):
            if k in item.metadata:
                cache_entry[k] = item.metadata[k]
        self.cache[item.id] = cache_entry

    async def _translate_item(self, item: ContentItem) -> None:
        """Lightweight translation fallback: when full enrichment fails, at least
        translate the title and summary to Chinese so the item is not dropped."""
        try:
            response = await self.client.complete(
                system="You are a translator. Translate to Simplified Chinese. Return only valid JSON, no other text.",
                user=(
                    f'Title: {item.title}\n'
                    f'Summary: {item.ai_summary or item.title}\n\n'
                    'Return JSON:\n'
                    '{"title_zh": "<中文标题>", "summary_zh": "<用中文写1-2句摘要>"}'
                ),
            )
            result = self._parse_json_response(response)
            if result:
                if result.get("title_zh"):
                    item.metadata["title_zh"] = result["title_zh"]
                if result.get("summary_zh"):
                    item.metadata["detailed_summary_zh"] = result["summary_zh"]
        except Exception:
            pass
