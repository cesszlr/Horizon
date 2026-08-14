"""Unit tests for custom category rules and dynamic prompt generation."""

import pytest
from unittest.mock import AsyncMock, MagicMock
import json

from src.ai.prompts import (
    build_content_analysis_system_prompt,
    build_content_analysis_user_prompt,
)
from src.ai.analyzer import ContentAnalyzer
from src.ai.summarizer import DailySummarizer
from src.models import CategoryRule, ContentItem, SourceType


def test_build_content_analysis_prompts_with_custom_categories():
    categories = {
        "gaming": CategoryRule(
            id="gaming",
            name="游戏资讯 (Gaming)",
            description="电子游戏与电竞赛事",
            scoring_rubric={"9-10": "TGA大作", "0-2": "抽卡广告"},
            focus_points=["机制创新", "玩家口碑"]
        ),
        "finance": CategoryRule(
            id="finance",
            name="金融与投资",
            description="宏观金融与股票市场",
            scoring_rubric={"9-10": "央行决议", "0-2": "垃圾广告"}
        )
    }

    system_prompt = build_content_analysis_system_prompt(categories)
    assert "游戏资讯 (Gaming) [gaming]" in system_prompt
    assert "TGA大作" in system_prompt
    assert "金融与投资 [finance]" in system_prompt
    assert "机制创新" in system_prompt

    user_prompt = build_content_analysis_user_prompt(categories)
    assert '"gaming" | "finance" | "other"' in user_prompt


def test_content_analyzer_classifies_with_custom_categories():
    async def _test():
        categories = {
            "gaming": CategoryRule(
                id="gaming",
                name="游戏资讯 (Gaming)",
                scoring_rubric={"9-10": "重磅首发"}
            )
        }

        mock_client = MagicMock()
        mock_client.config = MagicMock()
        mock_client.config.analysis_concurrency = 1
        mock_client.complete = AsyncMock(return_value=json.dumps({
            "category": "gaming",
            "score": 8.8,
            "reason": "知名大作发售实测",
            "summary": "新游戏发售并在Steam获得好评",
            "tags": ["游戏", "Steam"]
        }))

        analyzer = ContentAnalyzer(mock_client, categories=categories)
        item = ContentItem(
            id="rss:game-1",
            source_type=SourceType.RSS,
            title="Black Myth Wukong DLC Announced",
            url="https://example.com/game",
            published_at="2026-08-14T00:00:00Z"
        )

        await analyzer._analyze_item(item)
        assert item.ai_category == "gaming"
        assert item.ai_score == 8.8
        assert item.metadata.get("category") == "gaming"

    import asyncio
    asyncio.run(_test())


def test_daily_summarizer_custom_category_label():
    categories = {
        "gaming": CategoryRule(
            id="gaming",
            name="游戏 (Gaming)",
            name_en="Gaming"
        )
    }
    summarizer = DailySummarizer(categories=categories)
    item = ContentItem(
        id="rss:game-1",
        source_type=SourceType.RSS,
        title="Game Update",
        url="https://example.com/game",
        published_at="2026-08-14T00:00:00Z"
    )
    item.ai_category = "gaming"

    label_zh = summarizer._get_category_label(item, "zh")
    assert "游戏" in label_zh

    label_en = summarizer._get_category_label(item, "en")
    assert label_en == "Gaming"
