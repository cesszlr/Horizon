import asyncio
from datetime import datetime, timezone
from types import SimpleNamespace

import src.ai.analyzer as analyzer_module
from src.ai.analyzer import ContentAnalyzer
from src.models import ContentItem, SourceType


def _make_item(item_id: str) -> ContentItem:
    return ContentItem(
        id=item_id,
        source_type=SourceType.RSS,
        title=f"Item {item_id}",
        url="https://example.com/item",
        published_at=datetime(2026, 4, 26, tzinfo=timezone.utc),
    )


def test_analyze_batch_does_not_sleep_by_default(monkeypatch):
    analyzer = ContentAnalyzer(SimpleNamespace())
    items = [_make_item("rss:test:1"), _make_item("rss:test:2")]
    sleep_calls = []

    async def fake_analyze_item(item):
        item.ai_score = 8.0

    async def fake_sleep(seconds):
        sleep_calls.append(seconds)

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)
    monkeypatch.setattr(analyzer_module.asyncio, "sleep", fake_sleep)

    result = asyncio.run(analyzer.analyze_batch(items))

    assert len(result) == 2
    assert sleep_calls == []


def test_analyze_batch_sleeps_between_items_when_throttle_configured(monkeypatch):
    client = SimpleNamespace(config=SimpleNamespace(throttle_sec=1.5))
    analyzer = ContentAnalyzer(client)
    items = [_make_item("rss:test:1"), _make_item("rss:test:2"), _make_item("rss:test:3")]
    sleep_calls = []

    async def fake_analyze_item(item):
        item.ai_score = 8.0

    async def fake_sleep(seconds):
        sleep_calls.append(seconds)

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)
    monkeypatch.setattr(analyzer_module.asyncio, "sleep", fake_sleep)

    asyncio.run(analyzer.analyze_batch(items))

    assert sleep_calls == [1.5, 1.5]


def test_analyze_batch_concurrent_processing(monkeypatch):
    """Verify that higher concurrency allows overlapping item processing."""
    client = SimpleNamespace(config=SimpleNamespace(analysis_concurrency=3))
    analyzer = ContentAnalyzer(client)
    items = [_make_item(f"rss:test:{i}") for i in range(5)]
    active_count = 0
    max_active = 0

    async def fake_analyze_item(item):
        nonlocal active_count, max_active
        active_count += 1
        max_active = max(max_active, active_count)
        await asyncio.sleep(0.05)  # Small delay to allow overlap
        active_count -= 1

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)

    asyncio.run(analyzer.analyze_batch(items))

    assert max_active == 3
    assert all(item.ai_score is None for item in items)  # None because fake_analyze_item doesn't set it


def test_analyze_batch_concurrent_preserves_order(monkeypatch):
    """Verify that analyze_batch preserves input order in results."""
    client = SimpleNamespace(config=SimpleNamespace(analysis_concurrency=3))
    analyzer = ContentAnalyzer(client)
    items = [_make_item(f"rss:test:{i}") for i in range(5)]

    async def fake_analyze_item(item):
        item.ai_score = float(item.id.split(":")[-1]) * 10

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)

    result = asyncio.run(analyzer.analyze_batch(items))

    assert [item.id for item in result] == [item.id for item in items]


def test_analyze_item_extracts_category():
    class FakeClient:
        def __init__(self):
            self.last_user_prompt = None
            self.last_system_prompt = None

        async def complete(self, system, user):
            self.last_system_prompt = system
            self.last_user_prompt = user
            return '{"category": "politics", "score": 8.5, "reason": "important news", "summary": "brief summary", "tags": ["tag1", "tag2"]}'

    fake_client = FakeClient()
    analyzer = ContentAnalyzer(fake_client)

    item = _make_item("rss:test:1")
    item.metadata = {"category": "politics-test-hint"}
 
    asyncio.run(analyzer._analyze_item(item))
 
    assert item.ai_category == "politics"
    assert item.metadata["category"] == "politics-test-hint"  # preserve pre-defined hint
    assert item.ai_score == 8.5
    assert item.ai_reason == "important news"
    assert item.ai_summary == "brief summary"
    assert item.ai_tags == ["tag1", "tag2"]
    assert "politics-test-hint" in fake_client.last_user_prompt


def test_analyze_item_populates_missing_metadata_category():
    class FakeClient:
        async def complete(self, system, user):
            return '{"category": "social_hotspot", "score": 7.0, "reason": "hot", "summary": "brief summary", "tags": []}'

    fake_client = FakeClient()
    analyzer = ContentAnalyzer(fake_client)

    item = _make_item("rss:test:1")
    # metadata starts empty
    item.metadata = {}

    asyncio.run(analyzer._analyze_item(item))

    assert item.ai_category == "social_hotspot"
    assert item.metadata["category"] == "social_hotspot"  # populated because it was missing
