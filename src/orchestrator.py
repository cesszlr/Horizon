"""Main orchestrator coordinating the entire workflow."""

import asyncio
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import List, Dict, Optional, Any
from urllib.parse import urlparse
import httpx
from rich.console import Console

from .models import (
    Config,
    ContentItem,
    FilteringConfig,
    ProfileConfig,
    SourcesConfig,
    TwitterConfig,
)
from .storage.manager import StorageManager
from .services.email import EmailManager
from .services.webhook import WebhookNotifier
from .scrapers.github import GitHubScraper
from .scrapers.hackernews import HackerNewsScraper
from .scrapers.rss import RSSScraper
from .scrapers.reddit import RedditScraper
from .scrapers.telegram import TelegramScraper
from .scrapers.twitter import TwitterScraper
from .scrapers.twitter_playwright import TwitterPlaywrightScraper
from .scrapers.openbb import OpenBBScraper
from .scrapers.ossinsight import OSSInsightScraper
from .ai.client import create_ai_client
from .ai.analyzer import ContentAnalyzer
from .ai.summarizer import DailySummarizer
from .ai.enricher import ContentEnricher
from .ai.tokens import get_usage_snapshot


@dataclass
class BalancedDigestResult:
    """Items and selection statistics from balanced digest filtering."""

    items: List[ContentItem]
    enabled: bool = False
    group_counts: Dict[str, int] = field(default_factory=dict)
    group_limits: Dict[str, Optional[int]] = field(default_factory=dict)
    duplicate_categories: List[str] = field(default_factory=list)


class HorizonOrchestrator:
    """Orchestrates the complete workflow for content aggregation and analysis."""

    def __init__(self, config: Config, storage: StorageManager):
        """Initialize orchestrator.

        Args:
            config: Application configuration
            storage: Storage manager
        """
        self.config = config
        self.storage = storage
        self.console = Console()
        self.enrichment_cache: Dict[str, Dict[str, Any]] = {}
        self.email_manager = EmailManager(config.email, console=self.console) if config.email else None
        self.webhook_notifier = (
            WebhookNotifier(config.webhook, console=self.console)
            if config.webhook and config.webhook.enabled
            else None
        )

    async def run(
        self,
        force_hours: int = None,
        target_profile_id: Optional[str] = None,
        no_notify: bool = False,
    ) -> None:
        """Execute the complete workflow.

        Args:
            force_hours: Optional override for time window in hours
            target_profile_id: Optional specific profile ID to run
            no_notify: If True, skips sending webhook/ntfy and email notifications
        """
        self.console.print("[bold cyan]🌅 Horizon - Starting aggregation...[/bold cyan]\n")

        if no_notify:
            self.console.print("[yellow]🔕 Notification mode disabled (--no-notify). Summaries will be generated and saved locally only.[/yellow]\n")

        # Check email subscriptions if configured
        if (
            not no_notify
            and self.email_manager
            and self.config.email
            and self.config.email.enabled
            and self.config.email.imap_enabled
        ):
            self.console.print("📧 Checking for new email subscriptions...")
            self.email_manager.check_subscriptions(self.storage)

        try:
            # 1. Determine time window
            since = self._determine_time_window(force_hours)
            self.console.print(f"📅 Fetching content since: {since.strftime('%Y-%m-%d %H:%M:%S')}\n")

            # Determine active profiles
            active_profiles: Dict[str, ProfileConfig] = {}
            if self.config.profiles:
                if target_profile_id:
                    if target_profile_id in self.config.profiles:
                        active_profiles[target_profile_id] = self.config.profiles[target_profile_id]
                    else:
                        self.console.print(f"[bold red]❌ Profile '{target_profile_id}' not found![/bold red]")
                        return
                else:
                    active_profiles = {
                        pid: p for pid, p in self.config.profiles.items() if p.enabled
                    }

            # 2. Fetch content from all sources (global pool)
            all_items = await self.fetch_all_sources(since)
            self.console.print(f"📥 Fetched {len(all_items)} items from all sources\n")

            if not all_items:
                self.console.print("[yellow]No new content found. Exiting.[/yellow]")
                return

            # 3. Merge cross-source duplicates (same URL from different sources)
            merged_items = self.merge_cross_source_duplicates(all_items)
            if len(merged_items) < len(all_items):
                self.console.print(
                    f"🔗 Merged {len(all_items) - len(merged_items)} cross-source duplicates "
                    f"→ {len(merged_items)} unique items\n"
                )

            # 4. Global 1st-Pass AI Analysis (Token shared across all profiles!)
            analyzed_items = await self._analyze_content(merged_items)
            self.console.print(f"🤖 Analyzed {len(analyzed_items)} items with AI\n")

            today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

            # 5. Process either multi-profile pipeline or classic single-profile pipeline
            if active_profiles:
                self.console.print(f"👥 Running pipeline for {len(active_profiles)} active profile(s)...\n")
                for prof_id, profile in active_profiles.items():
                    await self._process_profile(
                        profile=profile,
                        analyzed_items=analyzed_items,
                        all_items_count=len(all_items),
                        today=today,
                        no_notify=no_notify,
                    )
            else:
                # Legacy single-profile fallback
                await self._process_single_profile(
                    analyzed_items=analyzed_items,
                    all_items_count=len(all_items),
                    today=today,
                    no_notify=no_notify,
                )

            self.console.print("[bold green]✅ Horizon completed successfully![/bold green]")
            usage = get_usage_snapshot()
            if usage.total_tokens > 0:
                self.console.print(
                    f"\n🧮 Token usage this run: "
                    f"{usage.total_tokens} tokens "
                    f"(input: {usage.total_input_tokens}, output: {usage.total_output_tokens})"
                )
                for provider, u in sorted(usage.per_provider.items()):
                    if u.total <= 0:
                        continue
                    self.console.print(
                        f"   • {provider}: {u.total} tokens "
                        f"(in: {u.input_tokens}, out: {u.output_tokens})"
                    )

        except Exception as e:
            self.console.print(f"[bold red]❌ Error: {e}[/bold red]")
            if self.webhook_notifier:
                await self.webhook_notifier.send_failure(
                    date=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                    error_message=str(e),
                )
            raise

    async def _process_profile(
        self,
        profile: ProfileConfig,
        analyzed_items: List[ContentItem],
        all_items_count: int,
        today: str,
        no_notify: bool = False,
    ) -> None:
        """Process filtering, enrichment, report generation and notifications for a specific profile."""
        self.console.print(f"[bold magenta]👤 === Processing Profile: {profile.name} [{profile.id}] ===[/bold magenta]")

        # 1. Filter by score threshold
        threshold = profile.filtering.ai_score_threshold
        important_items = [
            item.model_copy(deep=True) for item in analyzed_items
            if item.ai_score and item.ai_score >= threshold
        ]
        important_items.sort(key=lambda x: x.ai_score or 0, reverse=True)

        self.console.print(f"⭐️ {len(important_items)} items scored ≥ {threshold} for {profile.name}")

        # 2. Semantic deduplication
        deduped_items = await self.merge_topic_duplicates(important_items)
        if len(deduped_items) < len(important_items):
            self.console.print(
                f"🧹 Removed {len(important_items) - len(deduped_items)} topic duplicates "
                f"→ {len(deduped_items)} unique items"
            )
        important_items = deduped_items

        # 3. Twitter reply expansion
        if self.config.sources.twitter:
            await self._expand_twitter_discussion(important_items, self.config.sources.twitter)

        # 4. Balanced digest filtering
        balanced_result = self.apply_balanced_digest(
            important_items,
            filtering=profile.filtering,
            log=True,
        )
        important_items = balanced_result.items

        # 5. Enrich important items (reusing shared cache)
        await self._enrich_important_items(important_items)

        # 6. Generate and save daily summaries
        profile_notifier = (
            WebhookNotifier(profile.webhook, console=self.console)
            if profile.webhook and profile.webhook.enabled
            else self.webhook_notifier
        )
        profile_email = (
            EmailManager(profile.email, console=self.console)
            if profile.email and profile.email.enabled
            else self.email_manager
        )

        for lang in self.config.ai.languages:
            summarizer = DailySummarizer(categories=self.config.categories)
            summary = await summarizer.generate_summary(
                important_items,
                today,
                all_items_count,
                language=lang,
                category_groups=profile.filtering.category_groups,
                default_group=profile.filtering.default_group,
            )

            # Save to data/summaries/{profile_id}/
            summary_path = self.storage.save_daily_summary(
                today, summary, language=lang, profile_id=profile.id
            )
            self.console.print(f"💾 Saved {lang.upper()} summary to: {summary_path}")

            # Save to docs for Jekyll / GitHub Pages / Cloudflare Pages
            try:
                base_docs = Path(profile.output.docs_dir) if profile.output.docs_dir else Path("docs")
                posts_dir = base_docs / "_posts"
                posts_dir.mkdir(parents=True, exist_ok=True)

                # Ensure Jekyll boilerplate exists if using dedicated docs directory
                if base_docs.resolve() != Path("docs").resolve():
                    import shutil
                    root_docs = Path("docs")
                    if (root_docs / "_config.yml").exists() and not (base_docs / "_config.yml").exists():
                        shutil.copy2(root_docs / "_config.yml", base_docs / "_config.yml")
                    if (root_docs / "assets").exists() and not (base_docs / "assets").exists():
                        shutil.copytree(root_docs / "assets", base_docs / "assets", dirs_exist_ok=True)
                    if (root_docs / "_includes").exists() and not (base_docs / "_includes").exists():
                        shutil.copytree(root_docs / "_includes", base_docs / "_includes", dirs_exist_ok=True)

                post_filename = f"{today}-summary-{lang}.md"
                dest_path = posts_dir / post_filename

                front_matter = (
                    "---\n"
                    "layout: default\n"
                    f"title: \"{profile.name} Summary: {today} ({lang.upper()})\"\n"
                    f"date: {today}\n"
                    f"lang: {lang}\n"
                    f"profile: {profile.id}\n"
                    "---\n\n"
                )

                summary_content = summary
                first_line = summary_content.strip().split("\n")[0]
                if first_line.startswith("# "):
                    parts = summary_content.split("\n", 1)
                    if len(parts) > 1:
                        summary_content = parts[1].strip()

                with open(dest_path, "w", encoding="utf-8") as f:
                    f.write(front_matter + summary_content)

                self.console.print(f"📄 Copied {lang.upper()} summary to docs: {dest_path}")
            except Exception as e:
                self.console.print(f"[yellow]⚠️ Failed to copy summary to docs: {e}[/yellow]")

            if no_notify:
                continue

            # Send Email
            if profile_email and profile.email and profile.email.enabled:
                self.console.print(f"📧 Sending {lang.upper()} email summary for {profile.name}...")
                subscribers = self.storage.load_subscribers()
                subject = f"{profile.name} Summary ({lang.upper()}) - {today}"
                profile_email.send_daily_summary(summary, subject, subscribers)

            # Send Webhook / ntfy
            if profile_notifier:
                await profile_notifier.send_daily_summary(
                    summary=summary,
                    important_items=important_items,
                    all_items_count=all_items_count,
                    date=today,
                    lang=lang,
                    summarizer=summarizer,
                )

        self.console.print(f"[magenta]✓ Finished profile {profile.name}[/magenta]\n")

    async def _process_single_profile(
        self,
        analyzed_items: List[ContentItem],
        all_items_count: int,
        today: str,
        no_notify: bool = False,
    ) -> None:
        """Process legacy single profile configuration."""
        threshold = self.config.filtering.ai_score_threshold
        important_items = [
            item for item in analyzed_items
            if item.ai_score and item.ai_score >= threshold
        ]
        important_items.sort(key=lambda x: x.ai_score or 0, reverse=True)

        self.console.print(f"⭐️ {len(important_items)} items scored ≥ {threshold}\n")

        deduped_items = await self.merge_topic_duplicates(important_items)
        if len(deduped_items) < len(important_items):
            self.console.print(
                f"🧹 Removed {len(important_items) - len(deduped_items)} topic duplicates "
                f"→ {len(deduped_items)} unique items\n"
            )
        important_items = deduped_items

        if self.config.sources.twitter:
            await self._expand_twitter_discussion(important_items, self.config.sources.twitter)

        balanced_result = self.apply_balanced_digest(important_items)
        important_items = balanced_result.items

        await self._enrich_important_items(important_items)

        for lang in self.config.ai.languages:
            summarizer = DailySummarizer(categories=self.config.categories)
            summary = await summarizer.generate_summary(
                important_items,
                today,
                all_items_count,
                language=lang,
                category_groups=self.config.filtering.category_groups,
                default_group=self.config.filtering.default_group,
            )

            summary_path = self.storage.save_daily_summary(today, summary, language=lang)
            self.console.print(f"💾 Saved {lang.upper()} summary to: {summary_path}\n")

            try:
                post_filename = f"{today}-summary-{lang}.md"
                posts_dir = Path("docs/_posts")
                posts_dir.mkdir(parents=True, exist_ok=True)
                dest_path = posts_dir / post_filename

                front_matter = (
                    "---\n"
                    "layout: default\n"
                    f"title: \"Horizon Summary: {today} ({lang.upper()})\"\n"
                    f"date: {today}\n"
                    f"lang: {lang}\n"
                    "---\n\n"
                )

                summary_content = summary
                first_line = summary_content.strip().split("\n")[0]
                if first_line.startswith("# "):
                    parts = summary_content.split("\n", 1)
                    if len(parts) > 1:
                        summary_content = parts[1].strip()

                with open(dest_path, "w", encoding="utf-8") as f:
                    f.write(front_matter + summary_content)

                self.console.print(f"📄 Copied {lang.upper()} summary to GitHub Pages: {dest_path}\n")
            except Exception as e:
                self.console.print(f"[yellow]⚠️ Failed to copy summary to docs: {e}[/yellow]\n")

            if no_notify:
                continue

            if self.email_manager and self.config.email and self.config.email.enabled:
                self.console.print(f"📧 Sending {lang.upper()} email summary...")
                subscribers = self.storage.load_subscribers()
                subject = f"Horizon Summary ({lang.upper()}) - {today}"
                self.email_manager.send_daily_summary(summary, subject, subscribers)

            if self.webhook_notifier:
                await self.webhook_notifier.send_daily_summary(
                    summary=summary,
                    important_items=important_items,
                    all_items_count=all_items_count,
                    date=today,
                    lang=lang,
                    summarizer=summarizer,
                )

    def _determine_time_window(self, force_hours: int = None) -> datetime:
        if force_hours:
            since = datetime.now(timezone.utc) - timedelta(hours=force_hours)
        else:
            hours = self.config.filtering.time_window_hours
            since = datetime.now(timezone.utc) - timedelta(hours=hours)
        return since

    async def fetch_all_sources(
        self,
        since: datetime,
        sources: Optional[SourcesConfig] = None,
    ) -> List[ContentItem]:
        """Fetch content from all configured sources."""
        src_cfg = sources or self.config.sources
        async with httpx.AsyncClient(timeout=30.0) as client:
            tasks = []

            # GitHub sources
            if src_cfg.github:
                github_scraper = GitHubScraper(src_cfg.github, client)
                tasks.append(self._fetch_with_progress("GitHub", github_scraper, since))

            # Hacker News
            if src_cfg.hackernews and src_cfg.hackernews.enabled:
                hn_scraper = HackerNewsScraper(src_cfg.hackernews, client)
                tasks.append(self._fetch_with_progress("Hacker News", hn_scraper, since))

            # RSS feeds
            if src_cfg.rss:
                rss_scraper = RSSScraper(src_cfg.rss, client)
                tasks.append(self._fetch_with_progress("RSS Feeds", rss_scraper, since))

            # Reddit
            if src_cfg.reddit and src_cfg.reddit.enabled:
                reddit_scraper = RedditScraper(src_cfg.reddit, client)
                tasks.append(self._fetch_with_progress("Reddit", reddit_scraper, since))

            # Telegram
            if src_cfg.telegram and src_cfg.telegram.enabled:
                telegram_scraper = TelegramScraper(src_cfg.telegram, client)
                tasks.append(self._fetch_with_progress("Telegram", telegram_scraper, since))

            # Twitter
            if src_cfg.twitter and src_cfg.twitter.enabled:
                tw_cfg = src_cfg.twitter
                if tw_cfg.mode == "playwright":
                    twitter_scraper = TwitterPlaywrightScraper(tw_cfg)
                else:
                    twitter_scraper = TwitterScraper(tw_cfg, client)
                tasks.append(self._fetch_with_progress("Twitter", twitter_scraper, since))

            # OpenBB
            if src_cfg.openbb and src_cfg.openbb.enabled:
                openbb_scraper = OpenBBScraper(src_cfg.openbb, client)
                tasks.append(self._fetch_with_progress("OpenBB", openbb_scraper, since))

            # OSS Insight
            if src_cfg.ossinsight and src_cfg.ossinsight.enabled:
                oss_scraper = OSSInsightScraper(src_cfg.ossinsight, client)
                tasks.append(self._fetch_with_progress("OSS Insight", oss_scraper, since))

            results = await asyncio.gather(*tasks, return_exceptions=True)

            all_items = []
            for result in results:
                if isinstance(result, Exception):
                    self.console.print(f"[red]Error fetching source: {result}[/red]")
                elif isinstance(result, list):
                    all_items.extend(result)

            return all_items

    async def _fetch_with_progress(self, name: str, scraper, since: datetime) -> List[ContentItem]:
        self.console.print(f"🔍 Fetching from {name}...")
        items = await scraper.fetch(since)
        self.console.print(f"   Found {len(items)} items from {name}")

        sub_counts: Dict[str, int] = defaultdict(int)
        for item in items:
            sub_counts[self._sub_source_label(item)] += 1
        if len(sub_counts) > 1:
            for sub, count in sorted(sub_counts.items()):
                self.console.print(f"      • {sub}: {count}")

        return items

    @staticmethod
    def _sub_source_label(item: ContentItem) -> str:
        meta = item.metadata
        if meta.get("subreddit"):
            return f"r/{meta['subreddit']}"
        if meta.get("feed_name"):
            return meta["feed_name"]
        if meta.get("channel"):
            return f"@{meta['channel']}"
        if meta.get("period") and meta.get("repo"):
            return f"ossinsight:{meta.get('primary_language', 'all')}"
        if meta.get("repo"):
            return meta["repo"]
        if meta.get("watchlist"):
            return meta["watchlist"]
        return item.author or "unknown"

    def merge_cross_source_duplicates(self, items: List[ContentItem]) -> List[ContentItem]:
        def normalize_url(url: str) -> str:
            parsed = urlparse(str(url))
            host = parsed.hostname or ""
            if host.startswith("www."):
                host = host[4:]
            path = parsed.path.rstrip("/")
            return f"{host}{path}"

        url_groups: Dict[str, List[ContentItem]] = {}
        for item in items:
            key = normalize_url(str(item.url))
            url_groups.setdefault(key, []).append(item)

        merged = []
        for key, group in url_groups.items():
            if len(group) == 1:
                merged.append(group[0])
                continue

            primary = max(group, key=lambda x: len(x.content or ""))
            all_sources = set()
            for item in group:
                all_sources.add(item.source_type.value)
                for mk, mv in item.metadata.items():
                    if mk not in primary.metadata or not primary.metadata[mk]:
                        primary.metadata[mk] = mv

                if item is not primary and item.content:
                    if primary.content and item.content not in primary.content:
                        primary.content = (primary.content or "") + f"\n\n--- From {item.source_type.value} ---\n" + item.content

            primary.metadata["merged_sources"] = list(all_sources)
            merged.append(primary)

        return merged

    async def merge_topic_duplicates(self, items: List[ContentItem]) -> List[ContentItem]:
        if len(items) <= 1:
            return items

        from .ai.prompts import TOPIC_DEDUP_SYSTEM, TOPIC_DEDUP_USER
        from .ai.utils import parse_json_response

        lines = []
        for i, item in enumerate(items):
            tags = ", ".join(item.ai_tags) if item.ai_tags else "—"
            summary = item.ai_summary or "—"
            lines.append(f"[{i}] {item.title}\n    Tags: {tags}\n    Summary: {summary}")
        items_text = "\n\n".join(lines)

        try:
            ai_client = create_ai_client(self.config.ai)
            response = await ai_client.complete(
                system=TOPIC_DEDUP_SYSTEM,
                user=TOPIC_DEDUP_USER.format(items=items_text),
            )
            result = parse_json_response(response)
            if result is None:
                self.console.print("[yellow]  dedup: could not parse AI response, skipping[/yellow]")
                return items

            duplicate_groups = result.get("duplicates", [])
        except Exception as e:
            self.console.print(f"[yellow]  dedup: AI call failed ({e}), skipping[/yellow]")
            return items

        if not duplicate_groups:
            return items

        drop_indices: set[int] = set()
        for group in duplicate_groups:
            if not isinstance(group, list) or len(group) < 2:
                continue
            primary_idx = group[0]
            if primary_idx < 0 or primary_idx >= len(items):
                continue
            primary = items[primary_idx]
            for dup_idx in group[1:]:
                if not isinstance(dup_idx, int) or dup_idx < 0 or dup_idx >= len(items):
                    continue
                if dup_idx == primary_idx:
                    continue
                dup = items[dup_idx]
                if dup.content:
                    if not primary.content or dup.content not in primary.content:
                        label = dup.source_type.value
                        primary.content = (primary.content or "") + f"\n\n--- From {label} ---\n{dup.content}"
                self.console.print(
                    f"   [dim]dedup: keep [{primary_idx}] {primary.title}[/dim]\n"
                    f"   [dim]       drop [{dup_idx}] {dup.title}[/dim]"
                )
                drop_indices.add(dup_idx)

        return [item for i, item in enumerate(items) if i not in drop_indices]

    def apply_balanced_digest(
        self,
        items: List[ContentItem],
        filtering: Optional[FilteringConfig] = None,
        *,
        log: bool = True,
    ) -> BalancedDigestResult:
        """Apply configured category quotas and the final item cap."""
        f_cfg = filtering or self.config.filtering
        groups = f_cfg.category_groups
        max_items = f_cfg.max_items

        if not groups and max_items is None:
            return BalancedDigestResult(items=items)

        sorted_items = sorted(
            items,
            key=lambda item: item.ai_score or 0,
            reverse=True,
        )

        category_to_group: Dict[str, str] = {}
        duplicate_categories: List[str] = []
        for group_key, group in groups.items():
            for category in group.categories:
                if category in category_to_group:
                    if category_to_group[category] != group_key:
                        duplicate_categories.append(category)
                    continue
                category_to_group[category] = group_key

        if log:
            for category in sorted(set(duplicate_categories)):
                first_group = category_to_group[category]
                self.console.print(
                    f"[yellow]Warning: category '{category}' is configured in multiple "
                    f"groups; using '{first_group}'.[/yellow]"
                )

        selected: List[tuple[ContentItem, str]] = []
        group_counts: Dict[str, int] = defaultdict(int)
        default_group = f_cfg.default_group

        for item in sorted_items:
            category = item.metadata.get("category")
            group_key = (
                category_to_group.get(category, default_group)
                if isinstance(category, str)
                else default_group
            )

            if group_key in groups:
                limit = groups[group_key].limit
            else:
                limit = f_cfg.default_group_limit

            if limit is not None and group_counts[group_key] >= limit:
                continue

            selected.append((item, group_key))
            group_counts[group_key] += 1

        if max_items is not None:
            selected = selected[:max_items]

        final_counts: Dict[str, int] = defaultdict(int)
        for _, group_key in selected:
            final_counts[group_key] += 1

        group_limits: Dict[str, Optional[int]] = {
            group_key: group.limit for group_key, group in groups.items()
        }
        group_limits.setdefault(default_group, f_cfg.default_group_limit)

        if log:
            self.console.print(
                f"⚖️ Balanced digest selected {len(selected)}/{len(items)} items"
            )
            for group_key, group in groups.items():
                label = group.name or group_key
                self.console.print(
                    f"      • {label}: {final_counts.get(group_key, 0)}/{group.limit}"
                )
            if (
                final_counts.get(default_group, 0)
                or f_cfg.default_group_limit is not None
            ):
                limit_label = (
                    str(f_cfg.default_group_limit)
                    if f_cfg.default_group_limit is not None
                    else "unlimited"
                )
                self.console.print(
                    f"      • {default_group}: "
                    f"{final_counts.get(default_group, 0)}/{limit_label}"
                )
            self.console.print("")

        return BalancedDigestResult(
            items=[item for item, _ in selected],
            enabled=True,
            group_counts=dict(final_counts),
            group_limits=group_limits,
            duplicate_categories=sorted(set(duplicate_categories)),
        )

    async def _expand_twitter_discussion(
        self,
        items: List[ContentItem],
        twitter_config: Optional[TwitterConfig] = None,
    ) -> None:
        """Second-stage: fetch reply text for important Twitter items and re-analyze."""
        tw_cfg = twitter_config or self.config.sources.twitter
        if not tw_cfg or not tw_cfg.enabled or not tw_cfg.fetch_reply_text:
            return

        from .models import SourceType

        twitter_items = [
            item for item in items
            if item.source_type == SourceType.TWITTER
        ][:tw_cfg.max_tweets_to_expand]

        if not twitter_items:
            return

        self.console.print(
            f"💬 Fetching reply text for {len(twitter_items)} Twitter items..."
        )

        async with httpx.AsyncClient(timeout=30.0) as client:
            if tw_cfg.mode == "playwright":
                self.console.print(
                    "   [yellow]Reply expansion not yet supported in Playwright mode.[/yellow]"
                )
                return
            scraper = TwitterScraper(tw_cfg, client)
            expanded = []
            for item in twitter_items:
                try:
                    reply_lines = await scraper.fetch_replies_for_item(item)
                    if TwitterScraper.append_discussion_content(item, reply_lines):
                        expanded.append(item)
                        self.console.print(
                            f"   💬 {len(reply_lines)} replies added to: {item.title[:60]}"
                        )
                except Exception as exc:
                    self.console.print(
                        f"   [yellow]⚠️ Reply fetch failed for {item.id}: {exc}[/yellow]"
                    )

        if not expanded:
            return

        self.console.print(
            f"   Re-analyzing {len(expanded)} Twitter items with reply context...\n"
        )
        ai_client = create_ai_client(self.config.ai)
        analyzer = ContentAnalyzer(ai_client, categories=self.config.categories)
        await analyzer.analyze_batch(expanded)

    async def _enrich_important_items(self, items: List[ContentItem]) -> None:
        """Enrich items with background knowledge and deep takeaways (reusing cache)."""
        if not items:
            return

        self.console.print("📚 Enriching with background knowledge & deep takeaways...")
        ai_client = create_ai_client(self.config.ai)
        enricher = ContentEnricher(ai_client, cache=self.enrichment_cache)
        await enricher.enrich_batch(items)
        self.console.print(f"   Enriched {len(items)} items\n")

    async def _analyze_content(self, items: List[ContentItem]) -> List[ContentItem]:
        """Analyze content items with AI using registered categories."""
        self.console.print("🤖 Analyzing content with AI...")

        ai_client = create_ai_client(self.config.ai)
        analyzer = ContentAnalyzer(ai_client, categories=self.config.categories)

        return await analyzer.analyze_batch(items)
