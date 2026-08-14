"""Unit tests for multi-profile configuration and execution."""

import json
import pytest
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

from src.models import (
    AIConfig,
    AIProvider,
    CategoryGroupConfig,
    Config,
    ContentItem,
    FilteringConfig,
    ProfileConfig,
    ProfileOutputConfig,
    RSSSourceConfig,
    SourcesConfig,
    SourceType,
)
from src.storage.manager import StorageManager
from src.orchestrator import HorizonOrchestrator


def test_storage_manager_loads_base_and_profiles(tmp_path):
    # Setup data directory
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    categories_dir = data_dir / "categories"
    categories_dir.mkdir()
    profiles_dir = data_dir / "profiles"
    profiles_dir.mkdir()

    # Base config with all sources
    base_config = {
        "version": "2.0",
        "ai": {
            "provider": "openai",
            "model": "gpt-4",
            "api_key_env": "TEST_KEY",
        },
        "sources": {
            "rss": [
                {"name": "Base RSS", "url": "https://base.example.com/feed.xml", "enabled": True}
            ]
        }
    }
    with open(data_dir / "config.base.json", "w") as f:
        json.dump(base_config, f)

    # Category rule
    cat_rule = {
        "id": "gaming",
        "name": "游戏资讯 (Gaming)",
        "scoring_rubric": {"9-10": "Epic release", "0-2": "Spam"}
    }
    with open(categories_dir / "gaming.json", "w") as f:
        json.dump(cat_rule, f)

    # Profile 1 (tech) - no sources needed
    prof_tech = {
        "id": "tech",
        "name": "Tech Profile",
        "filtering": {
            "ai_score_threshold": 7.0,
        },
        "output": {
            "docs_dir": str(tmp_path / "docs" / "tech")
        }
    }
    with open(profiles_dir / "tech.json", "w") as f:
        json.dump(prof_tech, f)

    # Profile 2 (pm) - no sources needed
    prof_pm = {
        "id": "pm",
        "name": "PM Profile",
        "filtering": {
            "ai_score_threshold": 6.0,
        },
        "output": {
            "docs_dir": str(tmp_path / "docs" / "pm")
        }
    }
    with open(profiles_dir / "pm.json", "w") as f:
        json.dump(prof_pm, f)

    # Load via StorageManager
    storage = StorageManager(data_dir=str(data_dir))
    config = storage.load_config()

    assert config.ai.model == "gpt-4"
    assert "gaming" in config.categories
    assert config.categories["gaming"].name == "游戏资讯 (Gaming)"
    assert len(config.profiles) == 2
    assert "tech" in config.profiles
    assert "pm" in config.profiles
    assert len(config.sources.rss) == 1


def test_profile_independent_filtering():
    storage = StorageManager()
    profile_tech = ProfileConfig(
        id="tech",
        name="Tech Profile",
        filtering=FilteringConfig(
            ai_score_threshold=8.0,
            category_groups={
                "tech": CategoryGroupConfig(limit=5, categories=["technology", "ai"])
            }
        )
    )
    profile_pm = ProfileConfig(
        id="pm",
        name="PM Profile",
        filtering=FilteringConfig(
            ai_score_threshold=6.0,
            category_groups={
                "pm": CategoryGroupConfig(limit=5, categories=["product_manager", "trending"])
            }
        )
    )

    base_config = Config(
        version="2.0",
        ai=AIConfig(provider=AIProvider.OPENAI, model="gpt-4", api_key_env="KEY"),
        profiles={"tech": profile_tech, "pm": profile_pm}
    )

    orchestrator = HorizonOrchestrator(base_config, storage)

    # Sample analyzed items
    item1 = ContentItem(
        id="rss:1",
        source_type=SourceType.RSS,
        title="High Tech Item",
        url="https://example.com/1",
        published_at="2026-08-14T00:00:00Z",
    )
    item1.ai_score = 8.5
    item1.ai_category = "technology"
    item1.metadata["category"] = "technology"

    item2 = ContentItem(
        id="rss:2",
        source_type=SourceType.RSS,
        title="Mid PM Item",
        url="https://example.com/2",
        published_at="2026-08-14T00:00:00Z",
    )
    item2.ai_score = 6.5
    item2.ai_category = "product_manager"
    item2.metadata["category"] = "product_manager"

    # Tech balanced digest
    res_tech = orchestrator.apply_balanced_digest([item1, item2], filtering=profile_tech.filtering, log=False)
    assert len(res_tech.items) == 2  # item1 and item2 grouped into tech/other
    assert res_tech.items[0].id == "rss:1"

    # PM balanced digest
    res_pm = orchestrator.apply_balanced_digest([item1, item2], filtering=profile_pm.filtering, log=False)
    assert len(res_pm.items) == 2


def test_enrichment_cache_avoids_duplicate_ai_calls():
    async def _test():
        from src.ai.enricher import ContentEnricher

        mock_client = MagicMock()
        mock_client.config = MagicMock()
        mock_client.config.enrichment_concurrency = 1
        mock_client.complete = AsyncMock(return_value=json.dumps({
            "title_zh": "测试标题",
            "key_takeaways_zh": ["要点1", "要点2"],
            "deep_dive_zh": "深度解析内容",
            "whats_new_zh": "更新说明",
            "why_it_matters_zh": "重要原因",
            "key_details_zh": "细节描述",
            "background_zh": "背景知识",
            "community_discussion_zh": "热评",
        }))

        shared_cache = {}
        enricher1 = ContentEnricher(mock_client, cache=shared_cache)
        enricher2 = ContentEnricher(mock_client, cache=shared_cache)

        item = ContentItem(
            id="rss:test-1",
            source_type=SourceType.RSS,
            title="Test Title",
            url="https://example.com/test",
            published_at="2026-08-14T00:00:00Z",
        )

        # First enrich call -> executes AI complete
        await enricher1._enrich_item(item)
        assert mock_client.complete.call_count > 0
        first_call_count = mock_client.complete.call_count
        assert "rss:test-1" in shared_cache
        assert item.metadata["title_zh"] == "测试标题"
        assert item.metadata["deep_dive_zh"] == "深度解析内容"

        # Second enrich call on another instance with same item -> cache hit!
        item2 = ContentItem(
            id="rss:test-1",
            source_type=SourceType.RSS,
            title="Test Title",
            url="https://example.com/test",
            published_at="2026-08-14T00:00:00Z",
        )
        await enricher2._enrich_item(item2)
        # Complete call count must NOT increase!
        assert mock_client.complete.call_count == first_call_count
        assert item2.metadata["title_zh"] == "测试标题"
        assert item2.metadata["deep_dive_zh"] == "深度解析内容"

    import asyncio
    asyncio.run(_test())
