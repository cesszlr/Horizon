"""Daily summary generation — pure programmatic rendering."""

import re
from typing import List, Dict, Any

from ..models import ContentItem


_CJK = r"[\u4e00-\u9fff\u3400-\u4dbf]"
_ASCII = r"[A-Za-z0-9]"


def _pangu(text: str) -> str:
    """Insert a space between CJK and ASCII letters/digits (Pangu spacing)."""
    text = re.sub(rf"({_CJK})({_ASCII})", r"\1 \2", text)
    text = re.sub(rf"({_ASCII})({_CJK})", r"\1 \2", text)
    return text


LABELS = {
    "en": {
        "header": "Horizon Daily",
        "source": "Source",
        "background": "Background",
        "discussion": "Discussion",
        "references": "References",
        "tags": "Tags",
        "selected_items": "From {total} items, {selected} important content pieces were selected",
        "empty_analyzed": "Analyzed {total} items, but none met the importance threshold.",
        "empty_body": (
            "No significant developments today. This might indicate:\n"
            "- A quiet day in your tracked sources\n"
            "- The AI score threshold is too high\n"
            "- Your information sources need expansion\n\n"
            "Consider:\n"
            "1. Lowering the `ai_score_threshold` in config.json\n"
            "2. Adding more diverse information sources\n"
            "3. Checking if the AI model is working correctly\n"
        ),
        "category_sections": {
            "technology": "Technology",
            "politics": "Politics & Current Affairs",
            "social_hotspot": "Social & Social Media Hotspots",
            "trending": "Trending Hot Topics",
            "product_manager": "Product Management",
            "other": "Other",
        },
    },
    "zh": {
        "header": "Horizon 每日速递",
        "source": "来源",
        "background": "背景",
        "discussion": "社区讨论",
        "references": "参考链接",
        "tags": "标签",
        "selected_items": "从 {total} 条内容中筛选出 {selected} 条重要资讯。",
        "empty_analyzed": "已分析 {total} 条内容，但没有达到重要性阈值的条目。",
        "empty_body": (
            "今日暂无重要动态，可能原因：\n"
            "- 今天关注的信息源较平静\n"
            "- AI 评分阈值设置过高\n"
            "- 信息源种类有待扩充\n\n"
            "建议：\n"
            "1. 在 config.json 中降低 `ai_score_threshold`\n"
            "2. 添加更多多样化的信息源\n"
            "3. 检查 AI 模型是否正常工作\n"
        ),
        "category_sections": {
            "technology": "技术 (Technology)",
            "politics": "时政 (Politics)",
            "social_hotspot": "社会热点 (Social Hotspots)",
            "trending": "热搜 (Trending Hot Topics)",
            "product_manager": "产品经理 (Product Management)",
            "other": "其他 (Other)",
        },
    },
}


class DailySummarizer:
    """Generates daily Markdown summaries from pre-analyzed content items."""

    def __init__(self):
        pass

    def _get_category_label(self, item: ContentItem, language: str) -> str:
        """Get a localized category label for the item."""
        cat = item.ai_category
        if not cat:
            cat = item.metadata.get("category")
            if not cat:
                return ""
            return str(cat)

        mapping = {
            "zh": {
                "technology": "技术",
                "politics": "时政",
                "social_hotspot": "社会热点",
                "trending": "热搜",
                "product_manager": "产品经理",
                "other": "其他",
            },
            "en": {
                "technology": "Tech",
                "politics": "Politics",
                "social_hotspot": "Social",
                "trending": "Trending",
                "product_manager": "PM",
                "other": "Other",
            }
        }
        lang_map = mapping.get(language, mapping["en"])
        return lang_map.get(cat.lower(), cat)

    def _normalize_category_key(self, item: ContentItem) -> str:
        """Normalize category value to one of: technology, politics, social_hotspot, trending, product_manager, other."""
        cat = item.ai_category
        if not cat:
            cat = item.metadata.get("category")
        if not cat:
            return "other"
        
        cat_lower = str(cat).lower()
        if cat_lower in ("technology", "tech", "ai", "programming languages", "cloud native", "open source"):
            return "technology"
        elif cat_lower in ("politics", "politics / current affairs"):
            return "politics"
        elif cat_lower in ("social_hotspot", "social hot topics", "social network hot topics"):
            return "social_hotspot"
        elif cat_lower in ("trending", "hot search", "热搜"):
            return "trending"
        elif cat_lower in ("product_manager", "pm", "产品经理"):
            return "product_manager"
        
        return "other"

    def _group_items_by_category(
        self,
        items: List[ContentItem],
        category_groups: Dict[str, Any],
        default_group: str,
    ) -> Dict[str, List[tuple[int, ContentItem]]]:
        """Group items according to the category_groups definition."""
        grouped = {group_key: [] for group_key in category_groups.keys()}
        grouped[default_group] = []

        cat_to_group = {}
        for group_key, group in category_groups.items():
            categories = getattr(group, "categories", None)
            if categories is None and isinstance(group, dict):
                categories = group.get("categories", [])
            for cat in (categories or []):
                cat_to_group[cat.lower()] = group_key

        for i, item in enumerate(items):
            cat = item.ai_category
            if not cat:
                cat = item.metadata.get("category")
            
            group_key = default_group
            if cat:
                cat_str = str(cat).lower()
                if cat_str in cat_to_group:
                    group_key = cat_to_group[cat_str]
                elif cat_str in category_groups:
                    group_key = cat_str
                else:
                    found = False
                    for group_k, group in category_groups.items():
                        categories = getattr(group, "categories", None)
                        if categories is None and isinstance(group, dict):
                            categories = group.get("categories", [])
                        if any(c.lower() in cat_str or cat_str in c.lower() for c in (categories or [])):
                            group_key = group_k
                            found = True
                            break
                    if not found:
                        group_key = default_group

            grouped[group_key].append((i + 1, item))
            
        return grouped

    def _get_group_display_name(
        self,
        group_key: str,
        category_groups: Dict[str, Any],
        default_group: str,
        section_labels: Dict[str, str],
    ) -> str:
        if group_key in category_groups:
            group = category_groups[group_key]
            name = getattr(group, "name", None)
            if name is None and isinstance(group, dict):
                name = group.get("name")
            if name:
                return name
        return section_labels.get(group_key, group_key.capitalize())

    async def generate_summary(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
        category_groups: Dict[str, Any] | None = None,
        default_group: str = "other",
    ) -> str:
        """Generate daily summary in Markdown format.

        Items are rendered in score-descending order (already sorted by orchestrator).

        Args:
            items: High-scoring content items (already enriched)
            date: Date string (YYYY-MM-DD)
            total_fetched: Total number of items fetched before filtering
            language: Output language, either "en" or "zh"
            category_groups: Optional configuration-driven category groups map
            default_group: Default group key for items not matching any category group

        Returns:
            str: Markdown formatted summary
        """
        labels = LABELS.get(language, LABELS["en"])

        if not items:
            return self._generate_empty_summary(date, total_fetched, labels)

        header = (
            f"# {labels['header']} - {date}\n\n"
            f"> {labels['selected_items'].format(total=total_fetched, selected=len(items))}\n\n"
            "---\n\n"
        )

        section_labels = labels.get("category_sections", {})
        if not category_groups:
            category_groups = {
                "technology": {
                    "name": section_labels.get("technology", "Technology"),
                    "categories": ["technology", "tech", "ai", "programming languages", "cloud native", "open source"]
                },
                "politics": {
                    "name": section_labels.get("politics", "Politics"),
                    "categories": ["politics", "politics / current affairs"]
                },
                "social_hotspot": {
                    "name": section_labels.get("social_hotspot", "Social"),
                    "categories": ["social_hotspot", "social hot topics", "social network hot topics"]
                },
                "trending": {
                    "name": section_labels.get("trending", "Trending"),
                    "categories": ["trending", "hot search", "热搜"]
                },
                "product_manager": {
                    "name": section_labels.get("product_manager", "Product Manager"),
                    "categories": ["product_manager", "pm", "产品经理"]
                }
            }

        grouped_items = self._group_items_by_category(items, category_groups, default_group)
        render_keys = list(category_groups.keys())
        if default_group not in render_keys:
            render_keys.append(default_group)

        # TOC grouped by category
        toc_parts = []
        for cat_key in render_keys:
            cat_items = grouped_items.get(cat_key, [])
            if not cat_items:
                continue
            cat_name = self._get_group_display_name(cat_key, category_groups, default_group, section_labels)
            toc_parts.append(f"#### {cat_name}")
            for idx, item in cat_items:
                _t = item.metadata.get(f"title_{language}") or item.title
                t = str(_t).replace("[", "(").replace("]", ")")
                if language == "zh":
                    t = _pangu(t)
                score = item.ai_score or "?"
                category = self._get_category_label(item, language)
                cat_suffix = f" [{category}]" if category else ""
                toc_parts.append(f"{idx}. [{t}](#item-{idx}) \u2b50\ufe0f {score}/10{cat_suffix}")
            toc_parts.append("")  # Empty line between sections

        toc = "\n".join(toc_parts).strip() + "\n\n---\n\n"

        # Content Details grouped by category
        detail_parts = []
        for cat_key in render_keys:
            cat_items = grouped_items.get(cat_key, [])
            if not cat_items:
                continue
            cat_name = self._get_group_display_name(cat_key, category_groups, default_group, section_labels)
            detail_parts.append(f"## {cat_name}\n\n")
            for idx, item in cat_items:
                detail_parts.append(self._format_item(item, labels, language, idx))

        return header + toc + "".join(detail_parts)

    def generate_webhook_overview(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
        category_groups: Dict[str, Any] | None = None,
        default_group: str = "other",
    ) -> str:
        """Generate a compact overview for multi-message webhook delivery."""
        labels = LABELS.get(language, LABELS["en"])
        if not items:
            return self._generate_empty_summary(date, total_fetched, labels)

        if language == "zh":
            header = (
                f"# {labels['header']} - {date}\n\n"
                f"> 从 {total_fetched} 条内容中筛选出 {len(items)} 条重要资讯。\n\n"
                "下面会按新闻逐条发送详情，你可以只看感兴趣的标题。\n\n"
            )
        else:
            header = (
                f"# {labels['header']} - {date}\n\n"
                f"> Selected {len(items)} important items from {total_fetched} fetched items.\n\n"
                "Details will be sent item by item so you can read only the topics you care about.\n\n"
            )

        section_labels = labels.get("category_sections", {})
        if not category_groups:
            category_groups = {
                "technology": {
                    "name": section_labels.get("technology", "Technology"),
                    "categories": ["technology", "tech", "ai", "programming languages", "cloud native", "open source"]
                },
                "politics": {
                    "name": section_labels.get("politics", "Politics"),
                    "categories": ["politics", "politics / current affairs"]
                },
                "social_hotspot": {
                    "name": section_labels.get("social_hotspot", "Social"),
                    "categories": ["social_hotspot", "social hot topics", "social network hot topics"]
                },
                "trending": {
                    "name": section_labels.get("trending", "Trending"),
                    "categories": ["trending", "hot search", "热搜"]
                },
                "product_manager": {
                    "name": section_labels.get("product_manager", "Product Manager"),
                    "categories": ["product_manager", "pm", "产品经理"]
                }
            }

        grouped_items = self._group_items_by_category(items, category_groups, default_group)
        render_keys = list(category_groups.keys())
        if default_group not in render_keys:
            render_keys.append(default_group)

        entries = []
        for cat_key in render_keys:
            cat_items = grouped_items.get(cat_key, [])
            if not cat_items:
                continue
            cat_name = self._get_group_display_name(cat_key, category_groups, default_group, section_labels)
            entries.append(f"\n*{cat_name}*")
            for idx, item in cat_items:
                title = str(item.metadata.get(f"title_{language}") or item.title).replace("[", "(").replace("]", ")")
                if language == "zh":
                    title = _pangu(title)
                score = item.ai_score or "?"
                category = self._get_category_label(item, language)
                cat_suffix = f" [{category}]" if category else ""
                entries.append(f"{idx}. [{title}]({item.url}) \u2b50\ufe0f {score}/10{cat_suffix}")

        return header + "\n".join(entries).strip()

    def generate_webhook_item(
        self,
        item: ContentItem,
        language: str,
        index: int,
        total: int,
    ) -> str:
        """Generate one item message for multi-message webhook delivery."""
        labels = LABELS.get(language, LABELS["en"])
        prefix = f"第 {index}/{total} 条\n\n" if language == "zh" else f"Item {index}/{total}\n\n"
        return prefix + self._format_item(item, labels, language, index).rstrip("-\n ")

    def _format_item(self, item: ContentItem, labels: dict, language: str, index: int) -> str:
        """Format a single ContentItem into Markdown."""
        _title = item.metadata.get(f"title_{language}") or item.title
        title = str(_title).replace("[", "(").replace("]", ")")
        url = str(item.url)
        score = item.ai_score or "?"
        category = self._get_category_label(item, language)
        cat_suffix = f" [{category}]" if category else ""
        meta = item.metadata

        summary = (
            meta.get(f"detailed_summary_{language}")
            or meta.get("detailed_summary")
            or item.ai_summary
            or ""
        )
        background = meta.get(f"background_{language}") or meta.get("background") or ""
        discussion = (
            meta.get(f"community_discussion_{language}")
            or meta.get("community_discussion")
            or ""
        )

        if language == "zh":
            title = _pangu(title)
            summary = _pangu(summary)
            background = _pangu(background)
            discussion = _pangu(discussion)

        # Source line with parts joined by " · ", link appended at end
        source_type = item.source_type.value
        source_parts = [source_type]
        if meta.get("subreddit"):
            source_parts.append(f"r/{meta['subreddit']}")
        if meta.get("feed_name"):
            source_parts.append(meta["feed_name"])
        else:
            source_parts.append(item.author or "unknown")
        if item.published_at:
            if language == "zh":
                source_parts.append(
                    f"{item.published_at.month}月{item.published_at.day}日 "
                    f"{item.published_at:%H:%M}"
                )
            else:
                day = item.published_at.strftime("%d").lstrip("0")
                source_parts.append(item.published_at.strftime(f"%b {day}, %H:%M"))
        source_line = " \u00b7 ".join(source_parts)  # ·

        discussion_url = meta.get("discussion_url")
        if discussion_url:
            discussion_url = str(discussion_url)
            if discussion_url != url:
                source_line += f' · [{labels["discussion"]}]({discussion_url})'

        lines = [
            f'<a id="item-{index}"></a>',
            f"### [{title}]({url}) \u2b50\ufe0f {score}/10{cat_suffix}",  # ⭐️
            "",
            summary,
            "",
            source_line,
        ]

        if background:
            lines.append("")
            lines.append(f"**{labels['background']}**: {background}")

        sources = meta.get("sources") or []
        if sources:
            items_html = "".join(f'<li><a href="{s["url"]}">{s["title"]}</a></li>\n' for s in sources)
            lines += [
                "",
                f'<details><summary>{labels["references"]}</summary>\n<ul>\n{items_html}\n</ul>\n</details>',
            ]

        if discussion:
            lines.append("")
            lines.append(f"**{labels['discussion']}**: {discussion}")

        if item.ai_tags:
            tags_str = ", ".join([f"`#{t}`" for t in item.ai_tags])
            lines.append("")
            lines.append(f"**{labels['tags']}**: {tags_str}")

        lines.append("")
        lines.append("---")

        return "\n".join(lines) + "\n\n"

    def _generate_empty_summary(self, date: str, total_fetched: int, labels: dict) -> str:
        """Generate summary when no high-scoring items were found."""
        return (
            f"# {labels['header']} - {date}\n\n"
            f"> {labels['empty_analyzed'].format(total=total_fetched)}\n\n"
            + labels["empty_body"]
        )
