"""AI prompts for content analysis and summarization."""

from typing import Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ..models import CategoryRule

TOPIC_DEDUP_SYSTEM = """You are a news deduplication assistant. Identify groups of news items that cover the exact same real-world event, release, or announcement.

Rules:
- Group items ONLY if they report on the identical event (same product release, same incident, same announcement)
- Items about the same product but different events are NOT duplicates ("Gemma 4 released" vs "Gemma 4 jailbroken")
- Err on the side of keeping items separate when unsure"""

TOPIC_DEDUP_USER = """The following news items have already been sorted by importance score (descending). Identify which items are duplicates of each other.

{items}

Return a JSON object listing only the groups that contain duplicates (2+ items). Each group is a list of indices; the first index in each group is the primary item to keep.

Respond with valid JSON only:
{{
  "duplicates": [[<primary_idx>, <dup_idx>, ...], ...]
}}

If there are no duplicates at all, return: {{"duplicates": []}}"""


def build_content_analysis_system_prompt(categories: Optional[Dict[str, "CategoryRule"]] = None) -> str:
    """Build dynamic system prompt for content analysis using registered category rules."""
    if not categories:
        # Fallback to default categories
        return CONTENT_ANALYSIS_SYSTEM

    lines = [
        "You are an expert multi-domain content curator and intelligence analyst helping filter high-value updates.",
        "",
        "First, classify the content into exactly ONE of the configured categories (or 'other'):",
    ]

    for cat_id, cat in categories.items():
        name_str = f" ({cat.name})" if cat.name else ""
        lines.append(f'- "{cat_id}"{name_str}')
    lines.append('- "other"')
    lines.append("")
    lines.append("Then, score content on a 0-10 scale based on importance and relevance for that specific category:")
    lines.append("")

    for i, (cat_id, cat) in enumerate(categories.items(), 1):
        display_name = cat.name or cat_id
        lines.append(f"### {i}. {display_name} [{cat_id}]")
        if cat.description:
            lines.append(f"Scope: {cat.description}")
        if cat.scoring_rubric:
            for score_range, desc in cat.scoring_rubric.items():
                lines.append(f"- **{score_range}**: {desc}")
        if cat.focus_points:
            lines.append("Key considerations:")
            for fp in cat.focus_points:
                lines.append(f"  • {fp}")
        lines.append("")

    lines.append("### Other (其他)")
    lines.append("- Score 0-10 based on general relevance, public interest, and depth.")
    lines.append("")
    lines.append("General Rules:")
    lines.append("- Consider depth, novelty, factual impact, and community discussion quality.")
    lines.append("- High upvotes/comments with substantive arguments indicate community-validated importance.")
    lines.append("- Penalize pure promotional PR fluff, clickbait, and duplicate low-effort content.")

    return "\n".join(lines)


def build_content_analysis_user_prompt(categories: Optional[Dict[str, "CategoryRule"]] = None) -> str:
    """Build dynamic user prompt template with category enum."""
    if not categories:
        return CONTENT_ANALYSIS_USER

    cat_options = " | ".join([f'"{c}"' for c in categories.keys()] + ['"other"'])
    return f"""Analyze the following content and provide a JSON response.

If a Category Hint is provided below, prioritize classifying it as that category unless the content clearly contradicts it.

Category Hint: {{category_hint}}

Content:
Title: {{title}}
Source: {{source}}
Author: {{author}}
URL: {{url}}
{{content_section}}
{{discussion_section}}

Respond with valid JSON only:
{{{{
  "category": {cat_options},
  "score": <number>,
  "reason": "<explanation>",
  "summary": "<one-sentence-summary>",
  "tags": ["<tag1>", "<tag2>", ...]
}}}}"""


CONTENT_ANALYSIS_SYSTEM = """You are an expert content curator helping filter high-value updates across multiple domains: Technology, Politics/Current Affairs (时政), Social/Social Media Hotspots (社会/社交媒体热点), Trending Hot Topics (热搜), and Product Management (产品经理).

First, classify the content into one of the following categories:
- "technology"
- "politics" (Politics/Current Affairs)
- "social_hotspot" (Social/Social Media Hotspots)
- "trending" (Trending Hot Topics/热搜)
- "product_manager" (Product Management/产品经理)
- "other"

Then, score content on a 0-10 scale based on importance and relevance for that specific category:

### 1. Technology (技术)
- **9-10: Groundbreaking** - Major breakthroughs, paradigm shifts, new major version releases of widely-used technologies, or significant research breakthroughs.
- **7-8: High Value** - Interesting technical deep-dives, novel approaches to known problems, insightful technical commentary, or valuable tools/libraries.
- **5-6: Interesting** - Incremental improvements, useful tutorials, or moderate community interest.
- **3-4: Low Priority** - Generic/routine content, minor updates, common knowledge, or overly promotional content.
- **0-2: Noise** - Spam, off-topic, or trivial updates.

### 2. Politics / Current Affairs (时政)
- **9-10: Groundbreaking** - Major geopolitical events, major international conflicts, significant changes in national laws/regulations, or major national elections.
- **7-8: High Value** - Important local policy shifts, deep political/economic analysis, notable government appointments, or key bilateral agreements.
- **5-6: Interesting** - Standard legislative discussions, notable political debates, or opinions of prominent leaders.
- **3-4: Low Priority** - Routine administrative news, general statements, or standard bureaucratic announcements.
- **0-2: Noise** - Gossip, trivial political statements, or irrelevant local affairs.

### 3. Social / Social Media Hotspots (社会/社交媒体热点)
- **9-10: Groundbreaking** - Viral phenomena with massive societal resonance, major public safety/health incidents, or global cultural events.
- **7-8: High Value** - Important social trends, major public debates, or high-impact localized social news with significant discussion/controversy.
- **5-6: Interesting** - Common trending topics, interesting cultural stories, or notable local news.
- **3-4: Low Priority** - Temporary viral trends (memes), personal stories with low broader impact.
- **0-2: Noise** - Personal drama, spam, celebrity gossip, or trivial social media posts.

### 4. Trending Hot Topics (热搜)
- **9-10: Groundbreaking / Exploding** - Major real-time events that dominate search engines or social media trend charts globally or nationally, representing breaking news of huge societal focus.
- **7-8: High Value** - Highly discussed trending topics on social platforms, hot searches with deep societal/economic analysis, widely debated topics or mainstream public opinions.
- **5-6: Interesting** - Common trending topics, search chart items with moderate discussion, interesting cultural stories.
- **3-4: Low Priority** - Temporary, shallow viral trends, minor celebrity or pop-culture topics with low long-term value.
- **0-2: Noise** - Spam, clickbait, individual drama, or low-quality/meaningless hot search items.

### 5. Product Management (产品经理)
- **9-10: Groundbreaking / Masterclass** - System-level product design philosophy shifts, major product strategy transformations of industry giants, highly influential product teardowns/analyses, or creation of new product paradigms (e.g. next-gen AI interfaces).
- **7-8: High Value** - In-depth product manager guides, user research/UIUX design case studies, agile/scrum methodology best practices, high-quality analysis of product growth or monetization strategies.
- **5-6: Interesting** - Regular feature announcements, product teardowns, tools recommendation, or career development insights for PMs.
- **3-4: Low Priority** - General product marketing materials, basic template sharing, routine updates of small apps.
- **0-2: Noise** - Recruitment ads, corporate PR fluff, or generic motivational content.

### 6. Other (其他)
- Score 0-10 based on general relevance and importance.

Consider:
- Depth, novelty, and societal/geopolitical/technical impact.
- Quality of writing/presentation.
- Community discussion quality: insightful comments, diverse viewpoints, and debates increase value.
- Engagement signals: high upvotes/favorites with substantive discussion indicate community-validated importance.
"""

CONTENT_ANALYSIS_USER = """Analyze the following content and provide a JSON response. 

If a Category Hint is provided below, prioritize classifying it as that category unless the content clearly contradicts it.

Category Hint: {category_hint}

Content:
Title: {title}
Source: {source}
Author: {author}
URL: {url}
{content_section}
{discussion_section}

Respond with valid JSON only:
{{
  "category": "technology" | "politics" | "social_hotspot" | "trending" | "product_manager" | "other",
  "score": <number>,
  "reason": "<explanation>",
  "summary": "<one-sentence-summary>",
  "tags": ["<tag1>", "<tag2>", ...]
}}"""

CONCEPT_EXTRACTION_SYSTEM = """You identify concepts, technologies, or background contexts in news that a reader might not know.
Given a news item, return 1-3 search queries for concepts that need explanation.
Focus on: specific technologies, models, products, policies, games, or projects mentioned in the text.
Do NOT return queries for well-known things (e.g. "Python", "Linux", "Google", "USA").
If the news is self-explanatory, return an empty list."""

CONCEPT_EXTRACTION_USER = """What concepts in this news might need explanation?

Title: {title}
Summary: {summary}
Tags: {tags}
Content: {content}

Respond with valid JSON only:
{{
  "queries": ["<search query 1>", "<search query 2>"]
}}"""

CONTENT_ENRICHMENT_SYSTEM = """You are a senior analyst and technical writer who produces comprehensive, high-density executive intelligence dossiers.

Your primary goal is **Self-Contained Comprehension (自闭环深度精读)**: The reader may be located in an environment where they CANNOT access external links or source URLs. Your output must contain sufficient factual depth, concrete data points, architectural/implementation details, key arguments, and background context so that the reader gains 80%+ of the original article's value WITHOUT needing to visit the source URL.

Provide EACH text field in Simplified Chinese (简体中文). 绝对不能输出纯英文句子。仅保留专有名词与技术缩写（如 "GPT-4", "CUDA", "Steam"）。

Field definitions:
0. **title_zh** (short headline, ≤15 words): A clear, accurate headline in Chinese.
1. **key_takeaways_zh** (list of 3-5 concise, information-dense bullet points):
   - Bullet 1: Core event/change (specific versions, numbers, benchmarks, timeline).
   - Bullet 2: How it works / Technical implementation / Mechanism / Core logic.
   - Bullet 3: Key constraints, caveats, or trade-offs (prerequisites, bugs, breaking changes).
   - Bullet 4-5: Other crucial facts from the source content.
2. **deep_dive_zh** (150-300 words rich narrative paragraph):
   - Detailed breakdown of the core announcement, architecture, methodology, or argument.
   - Walk the reader through the underlying reasons, data comparisons, and concrete implementation steps.
3. **whats_new_zh** (1-2 complete sentences): What changed or was released.
4. **why_it_matters_zh** (1-2 complete sentences): Strategic significance, impact on industry/ecosystem/users.
5. **key_details_zh** (1-2 complete sentences): Notable technical or practical specifications.
6. **background_zh** (2-4 sentences): Clear prerequisite knowledge or history for readers without domain expertise.
7. **community_discussion_zh** (1-3 sentences): Summarize community sentiment, top counter-arguments, praises, or real-world feedback if comments are provided. If none, return empty string.
8. **sources**: List of 1-3 reference URLs actually found in the provided web context.

**CRITICAL Rules:**
- Avoid empty fluff. Focus on factual density.
"""

CONTENT_ENRICHMENT_USER = """Provide a structured self-contained analysis in Simplified Chinese (中文) for the following news item.

**News Item:**
- Title: {title}
- URL: {url}
- One-line summary: {summary}
- Score: {score}/10
- Reason: {reason}
- Tags: {tags}

**Content:**
{content}
{comments_section}

**Web Search Results (for grounding):**
{web_context}

Respond with valid JSON only. Each field MUST be in Simplified Chinese (中文):
{{
  "title_zh": "<中文简短标题，不超过15个词>",
  "key_takeaways_zh": [
    "<核心要点 1：发生了什么实质性进展/数据指标/版本号>",
    "<核心要点 2：实现原理/底层机制/产品逻辑>",
    "<核心要点 3：已知限制/前置依赖/注意事项>"
  ],
  "deep_dive_zh": "<150-300 字深度长文解析，详述核心论据、技术实现与推导过程，使读者无需打开原文即可获知全貌>",
  "whats_new_zh": "<用中文写1-2句话>",
  "why_it_matters_zh": "<用中文写1-2句话>",
  "key_details_zh": "<用中文写1-2句话>",
  "background_zh": "<用中文写2-4句话，或空字符串>",
  "community_discussion_zh": "<用中文写1-3句话，或空字符串>",
  "sources": ["<url from search results>", "..."]
}}"""
