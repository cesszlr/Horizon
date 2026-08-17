import asyncio
from datetime import datetime, timezone
from types import SimpleNamespace

import pytest
from pydantic import ValidationError
from rich.console import Console

from src.models import (
    AIConfig,
    CategoryGroupConfig,
    Config,
    ContentItem,
    FilteringConfig,
    SourceType,
    SourcesConfig,
)
from src.orchestrator import HorizonOrchestrator


def make_item(item_id: str, score: float, category: str | None) -> ContentItem:
    metadata = {"category": category} if category is not None else {}
    return ContentItem(
        id=item_id,
        source_type=SourceType.RSS,
        title=item_id,
        url=f"https://example.com/{item_id}",
        published_at=datetime.now(timezone.utc),
        ai_score=score,
        metadata=metadata,
    )


def make_orchestrator(filtering: FilteringConfig) -> HorizonOrchestrator:
    orchestrator = HorizonOrchestrator.__new__(HorizonOrchestrator)
    orchestrator.config = SimpleNamespace(filtering=filtering)
    orchestrator.console = Console(record=True)
    return orchestrator


def test_unconfigured_balanced_digest_preserves_old_behavior() -> None:
    items = [make_item("lower", 7.0, "ai"), make_item("higher", 9.0, "finance")]
    result = make_orchestrator(FilteringConfig()).apply_balanced_digest(items)

    assert result.enabled is False
    assert result.items is items


def test_category_groups_apply_limits_and_default_group_limit() -> None:
    filtering = FilteringConfig(
        category_groups={
            "ai": CategoryGroupConfig(limit=2, categories=["ai", "ml"]),
            "finance": CategoryGroupConfig(limit=1, categories=["finance"]),
        },
        default_group_limit=1,
    )
    items = [
        make_item("ai-low", 7.0, "ai"),
        make_item("finance-low", 6.0, "finance"),
        make_item("other-high", 9.5, "world"),
        make_item("ai-high", 9.0, "ml"),
        make_item("finance-high", 8.5, "finance"),
        make_item("ai-mid", 8.0, "ai"),
        make_item("other-low", 5.0, None),
    ]

    result = make_orchestrator(filtering).apply_balanced_digest(items)

    assert [item.id for item in result.items] == [
        "other-high",
        "ai-high",
        "finance-high",
        "ai-mid",
    ]
    assert result.group_counts == {"other": 1, "ai": 2, "finance": 1}


def test_max_items_applies_after_group_limits() -> None:
    filtering = FilteringConfig(
        max_items=2,
        category_groups={
            "ai": CategoryGroupConfig(limit=2, categories=["ai"]),
            "finance": CategoryGroupConfig(limit=2, categories=["finance"]),
        },
    )
    items = [
        make_item("finance", 8.0, "finance"),
        make_item("ai-top", 10.0, "ai"),
        make_item("ai-second", 9.0, "ai"),
    ]

    result = make_orchestrator(filtering).apply_balanced_digest(items)

    assert [item.id for item in result.items] == ["ai-top", "ai-second"]
    assert result.group_counts == {"ai": 2}


def test_max_items_works_without_category_groups() -> None:
    filtering = FilteringConfig(max_items=1)
    items = [make_item("lower", 7.0, None), make_item("higher", 9.0, None)]

    result = make_orchestrator(filtering).apply_balanced_digest(items)

    assert [item.id for item in result.items] == ["higher"]


def test_duplicate_category_warns_and_first_group_wins() -> None:
    filtering = FilteringConfig(
        category_groups={
            "first": CategoryGroupConfig(limit=1, categories=["shared"]),
            "second": CategoryGroupConfig(limit=2, categories=["shared"]),
        }
    )
    orchestrator = make_orchestrator(filtering)

    result = orchestrator.apply_balanced_digest(
        [make_item("top", 9.0, "shared"), make_item("second", 8.0, "shared")]
    )

    assert [item.id for item in result.items] == ["top"]
    assert result.duplicate_categories == ["shared"]
    assert "using 'first'" in orchestrator.console.export_text()


@pytest.mark.parametrize(
    "kwargs",
    [
        {"max_items": 0},
        {"default_group_limit": 0},
        {"category_groups": {"ai": {"limit": 0, "categories": ["ai"]}}},
        {"category_groups": {"ai": {"limit": 1, "categories": []}}},
    ],
)
def test_balanced_digest_config_rejects_non_positive_or_empty_limits(kwargs) -> None:
    with pytest.raises(ValidationError):
        FilteringConfig(**kwargs)


def test_run_applies_balanced_digest_before_enrichment(tmp_path, monkeypatch) -> None:
    config = Config(
        ai=AIConfig(
            provider="openai",
            model="test",
            api_key_env="TEST_API_KEY",
            languages=[],
        ),
        sources=SourcesConfig(),
        filtering=FilteringConfig(
            ai_score_threshold=7.0,
            max_items=1,
            category_groups={
                "ai": CategoryGroupConfig(limit=1, categories=["ai"]),
                "finance": CategoryGroupConfig(limit=1, categories=["finance"]),
            },
        ),
    )
    storage = SimpleNamespace()
    orchestrator = HorizonOrchestrator(config, storage)
    items = [
        make_item("ai", 9.0, "ai"),
        make_item("finance", 8.0, "finance"),
        make_item("below-threshold", 6.0, "ai"),
    ]
    enriched_ids: list[str] = []

    async def fetch_all_sources(since):  # type: ignore[no-untyped-def]
        return items

    async def analyze_content(input_items):  # type: ignore[no-untyped-def]
        return input_items

    async def merge_topic_duplicates(input_items):  # type: ignore[no-untyped-def]
        return input_items

    async def expand_twitter_discussion(input_items):  # type: ignore[no-untyped-def]
        return None

    async def enrich_important_items(input_items):  # type: ignore[no-untyped-def]
        enriched_ids.extend(item.id for item in input_items)

    monkeypatch.setattr(orchestrator, "fetch_all_sources", fetch_all_sources)
    monkeypatch.setattr(orchestrator, "_analyze_content", analyze_content)
    monkeypatch.setattr(orchestrator, "merge_topic_duplicates", merge_topic_duplicates)
    monkeypatch.setattr(orchestrator, "_expand_twitter_discussion", expand_twitter_discussion)
    monkeypatch.setattr(orchestrator, "_enrich_important_items", enrich_important_items)
    monkeypatch.chdir(tmp_path)

    asyncio.run(orchestrator.run())

    assert enriched_ids == ["ai"]


def test_merge_topic_duplicates_chunking(monkeypatch) -> None:
    # Setup orchestrator with dummy config
    config = Config(
        db_path=":memory:",
        profiles={},
        sources=SourcesConfig(),
        ai=AIConfig(provider="openai", model="gpt-4", api_key_env="TEST_API_KEY", languages=[]),
    )
    storage = SimpleNamespace()
    orchestrator = HorizonOrchestrator(config, storage)

    # Create test items with different categories and titles
    items = []
    # 35 items in category 'tech' (to trigger chunking of size 30)
    for i in range(35):
        item = make_item(f"tech-{i}", 9.0 - i * 0.1, "tech")
        item.title = f"Title-{35-i:02d}"
        item.ai_category = "tech"
        items.append(item)

    # 5 items in category 'politics'
    for i in range(5):
        item = make_item(f"pol-{i}", 8.0 - i * 0.1, "politics")
        item.title = f"PolTitle-{5-i:02d}"
        item.ai_category = "politics"
        items.append(item)

    # Mock _merge_topic_duplicates_batch
    batches_passed = []

    async def mock_batch_dedup(batch_items):  # type: ignore[no-untyped-def]
        batches_passed.append(batch_items)
        return batch_items

    monkeypatch.setattr(orchestrator, "_merge_topic_duplicates_batch", mock_batch_dedup)

    # Run deduplication
    result = asyncio.run(orchestrator.merge_topic_duplicates(items))

    # We expect 3 batches:
    # Batch 1: 'politics' category (5 items, sorted alphabetically by title)
    # Batch 2: 'tech' category chunk 1 (30 items, sorted alphabetically by title)
    # Batch 3: 'tech' category chunk 2 (5 items, sorted alphabetically by title)
    assert len(batches_passed) == 3

    # Check politics batch
    pol_batch = [b for b in batches_passed if b[0].ai_category == "politics"][0]
    assert len(pol_batch) == 5
    # Titles should be sorted: PolTitle-01, PolTitle-02, ... PolTitle-05
    assert [x.title for x in pol_batch] == [f"PolTitle-{i:02d}" for i in range(1, 6)]

    # Check tech batches
    tech_batches = [b for b in batches_passed if b[0].ai_category == "tech"]
    assert len(tech_batches) == 2
    # Chunk 1 should have 30 items
    assert len(tech_batches[0]) == 30
    # Chunk 2 should have 5 items
    assert len(tech_batches[1]) == 5

    # Check that they are sorted alphabetically by title
    all_tech_titles = [x.title for x in tech_batches[0]] + [x.title for x in tech_batches[1]]
    assert all_tech_titles == [f"Title-{i:02d}" for i in range(1, 36)]

    # Check that the final returned list is sorted by score descending (restored priority)
    # tech-0 has 9.0, tech-1 has 8.9... pol-0 has 8.0...
    assert [x.id for x in result[:3]] == ["tech-0", "tech-1", "tech-2"]

