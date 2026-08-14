"""Unit tests for self-contained deep-dive enrichment and summarizer formatting."""

import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock
from datetime import datetime, timezone

from src.ai.summarizer import DailySummarizer
from src.ai.enricher import ContentEnricher
from src.ai.utils import parse_json_response
from src.models import ContentItem, SourceType


def test_format_item_renders_takeaways_and_deep_dive():
    summarizer = DailySummarizer()
    item = ContentItem(
        id="rss:deep-1",
        source_type=SourceType.RSS,
        title="OpenAI 发布新一代架构细节",
        url="https://openai.com/blog/deep-arch",
        content="full article content",
        author="OpenAI",
        published_at=datetime(2026, 8, 14, 12, 0, tzinfo=timezone.utc),
    )
    item.ai_score = 9.5
    item.ai_category = "technology"
    item.metadata = {
        "title_zh": "OpenAI 架构重大升级深度解读",
        "key_takeaways_zh": [
            "推理速度提升 40%，上下文窗口扩展至 1M",
            "开源 8B 与 32B 基础权重，Apache 2.0 协议",
            "需要 CUDA 12.4+ 环境"
        ],
        "deep_dive_zh": "本次更新的核心在于解决长上下文下的显存瓶颈。团队引入了全新的层次化路由机制，在处理 100k+ 词元时仅激活前 15% 的 KV Cache 节点...",
        "background_zh": "KV Cache 是大语言模型推理时存储历史对话计算结果的显存区域。",
        "community_discussion_zh": "社区对 8B 模型的本地端侧性能普遍好评。",
    }
    item.ai_tags = ["LLM", "OpenAI", "开源"]

    labels = {
        "header": "Horizon 每日速递",
        "source": "来源",
        "key_takeaways": "核心要点速览",
        "deep_dive": "深度内容详析",
        "background": "背景",
        "discussion": "社区讨论",
        "references": "参考链接",
        "tags": "标签",
    }

    formatted = summarizer._format_item(item, labels, language="zh", index=1)

    # Verify key takeaways list
    assert "**核心要点速览**:" in formatted
    assert "- 推理速度提升 40%，上下文窗口扩展至 1M" in formatted
    assert "- 开源 8B 与 32B 基础权重，Apache 2.0 协议" in formatted

    # Verify deep dive
    assert "**深度内容详析**:" in formatted
    assert "本次更新的核心在于解决长上下文下的显存瓶颈" in formatted

    # Verify background & discussion & tags
    assert "**背景**: KV Cache 是大语言模型推理时存储历史对话计算结果的显存区域。" in formatted
    assert "**社区讨论**: 社区对 8B 模型的本地端侧性能普遍好评。" in formatted
    assert "**标签**: `#LLM`, `#OpenAI`, `#开源`" in formatted


def test_parse_json_response_with_reasoning_and_dirty_json():
    # Test reasoning models with <think> tag and trailing commas
    response = """
    <think>
    I should analyze the key takeaways and extract the facts.
    Let's organize the output as JSON.
    </think>
    ```json
    {
      "title_zh": "大模型架构更新",
      "key_takeaways_zh": ["提升性能", "降低显存",],
      "deep_dive_zh": "核心原理解析...",
      "whats_new_zh": {"text": "全新架构发布"},
      "background_zh": "大语言模型推理优化",
    }
    ```
    """
    parsed = parse_json_response(response)
    assert parsed is not None
    assert parsed["title_zh"] == "大模型架构更新"
    assert parsed["key_takeaways_zh"] == ["提升性能", "降低显存"]
    assert parsed["deep_dive_zh"] == "核心原理解析..."


def test_enricher_handles_complex_and_nested_model_outputs():
    async def _test():
        mock_client = MagicMock()
        mock_client.config = MagicMock()
        mock_client.config.enrichment_concurrency = 1
        # Response with thinking block, dict sub-fields, and trailing commas
        mock_client.complete = AsyncMock(return_value="""
        <think>Some reasoning...</think>
        {
          "title_zh": "测试标题",
          "key_takeaways_zh": "- 要点一\\n- 要点二",
          "deep_dive_zh": {"text": "深度分析正文"},
          "whats_new_zh": {"value": "发布新功能"},
          "why_it_matters_zh": ["极其重要", "影响深远"],
          "background_zh": {"text": "背景介绍"},
          "community_discussion_zh": ["网友普遍赞同"],
        }
        """)

        enricher = ContentEnricher(mock_client)
        enricher._extract_concepts = AsyncMock(return_value=[])
        enricher._web_search = AsyncMock(return_value=[])

        item = ContentItem(
            id="rss:complex-1",
            source_type=SourceType.RSS,
            title="Complex Item",
            url="https://example.com/item",
            published_at="2026-08-14T00:00:00Z",
        )
        await enricher._enrich_item(item)

        assert item.metadata["title_zh"] == "测试标题"
        assert item.metadata["key_takeaways_zh"] == ["要点一", "要点二"]
        assert item.metadata["deep_dive_zh"] == "深度分析正文"
        assert "发布新功能" in item.metadata["detailed_summary_zh"]
        assert "极其重要" in item.metadata["detailed_summary_zh"]
        assert item.metadata["background_zh"] == "背景介绍"
        assert item.metadata["community_discussion_zh"] == "网友普遍赞同"

    asyncio.run(_test())
