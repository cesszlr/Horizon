from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from unittest.mock import AsyncMock
from unittest.mock import MagicMock

from src.models import RSSSourceConfig
from src.scrapers.rss import RSSScraper


def test_rss_ids_are_deterministic() -> None:
    feed = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0"><channel><title>Test</title>
      <item>
        <guid>entry-1</guid>
        <title>Item 1</title>
        <link>https://example.com/item-1</link>
        <pubDate>Fri, 24 Apr 2026 12:00:00 GMT</pubDate>
        <description>Hello</description>
      </item>
    </channel></rss>
    """
    response = MagicMock()
    response.text = feed
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    source = RSSSourceConfig(name="Test", url="https://example.com/feed.xml")
    scraper = RSSScraper([source], client)
    since = datetime(2026, 4, 24, 0, 0, tzinfo=timezone.utc)

    first = asyncio.run(scraper.fetch(since))[0].id
    second = asyncio.run(scraper.fetch(since))[0].id

    assert first == second
    assert first == "rss:example.com_feed.xml:5e2d5d1e58e94d76"


def test_rss_date_fallbacks() -> None:
    # Test feed with channel lastBuildDate but no item pubDate
    feed_with_channel_date = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0"><channel><title>Test Channel Date</title>
      <lastBuildDate>Fri, 24 Apr 2026 12:00:00 GMT</lastBuildDate>
      <item>
        <guid>entry-1</guid>
        <title>Item 1</title>
        <link>https://example.com/item-1</link>
        <description>Hello</description>
      </item>
    </channel></rss>
    """
    response_1 = MagicMock()
    response_1.text = feed_with_channel_date
    response_1.raise_for_status.return_value = None

    # Test feed with no date at all
    feed_with_no_date = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0"><channel><title>Test No Date</title>
      <item>
        <guid>entry-2</guid>
        <title>Item 2</title>
        <link>https://example.com/item-2</link>
        <description>World</description>
      </item>
    </channel></rss>
    """
    response_2 = MagicMock()
    response_2.text = feed_with_no_date
    response_2.raise_for_status.return_value = None

    client = AsyncMock()
    client.get.side_effect = [response_1, response_2]

    source_1 = RSSSourceConfig(name="Test 1", url="https://example.com/feed1.xml")
    source_2 = RSSSourceConfig(name="Test 2", url="https://example.com/feed2.xml")

    scraper = RSSScraper([source_1, source_2], client)
    since = datetime(2026, 4, 24, 0, 0, tzinfo=timezone.utc)

    items = asyncio.run(scraper.fetch(since))
    assert len(items) == 2

    # Item 1 should have the channel-level date
    assert items[0].published_at == datetime(2026, 4, 24, 12, 0, tzinfo=timezone.utc)

    # Item 2 should have a current timestamp (which is after since)
    assert items[1].published_at > since

