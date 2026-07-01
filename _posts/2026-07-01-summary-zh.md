---
layout: default
title: "Horizon Summary: 2026-07-01 (ZH)"
date: 2026-07-01
lang: zh
---

> 从 62 条内容中筛选出 15 条重要资讯。

---

#### AI 探索 (AI)
2. [英伟达与剑桥发布'红皇后哥德尔机器'，实现 AI 自我进化](#item-2) ⭐️ 9.0/10 [技术]
12. [虎牙 VAM 1.0：一张照片生成实时多模态数字人](#item-12) ⭐️ 7.0/10 [技术]

#### 产品专栏 (Product Management)
1. [AI 从提示工程转向循环工程](#item-1) ⭐️ 9.0/10 [产品经理]
3. [PM Skills Marketplace 在制造业案例中大幅提升产品规划效率](#item-3) ⭐️ 8.0/10 [产品经理]
4. [ChatGPT 广告开启品牌营销新入口](#item-4) ⭐️ 8.0/10 [产品经理]
5. [飞书开源 CLI，剑指 AI Agent 基础设施](#item-5) ⭐️ 8.0/10 [产品经理]
6. [小红书投放：看评论区，别只看点赞](#item-6) ⭐️ 8.0/10 [产品经理]
7. [618 给 AI 上了一课：Agent 并非万能解药](#item-7) ⭐️ 8.0/10 [产品经理]
8. [企业 AI 分层调用：小模型经济学节省 90%成本](#item-8) ⭐️ 8.0/10 [产品经理]

#### 热搜焦点 (Trending)
9. [中国 PMI 重返扩张区间，八部门发文推动工业互联网](#item-9) ⭐️ 8.0/10 [热搜]
10. [AI 算力把全球电网逼到极限](#item-10) ⭐️ 8.0/10 [热搜]
11. [AI 需求导致存储成本飙升 386%，引发结构性通胀](#item-11) ⭐️ 8.0/10 [热搜]
13. [沃什想复活哪个格林斯潘？](#item-13) ⭐️ 7.0/10 [热搜]
14. [Momenta 港股 IPO：从技术理想转向财务杠杆](#item-14) ⭐️ 7.0/10 [热搜]
15. [VC 材料龙头拟与亘元新材合并，宁德时代为重要股东](#item-15) ⭐️ 7.0/10 [热搜]

---

## AI 探索 (AI)

<a id="item-2"></a>
### [英伟达与剑桥发布'红皇后哥德尔机器'，实现 AI 自我进化](https://www.woshipm.com/ai/6422518.html) ⭐️ 9.0/10 [技术]

英伟达与剑桥大学联合发表了一篇题为'红皇后哥德尔机器'（RQGM）的论文，该论文使 AI 系统能够自主编写自己的学习算法，并通过同时进化任务智能体和评估器来实现自我进化，突破了原始哥德尔机长达 20 年的限制。 这一突破可能加速人工超级智能（ASI）的到来，因为它实现了无需数学证明的递归自我改进，可能导致 AI 系统不断超越自身能力，对安全和控制产生深远影响。 RQGM 采用了一种'受控效用进化'机制，在每个 epoch 内评估器被冻结，只有当新评估器在锚点数据上统计意义上优于旧评估器时才被替换，并选择性擦除被替换评估器的评分。实验中，它将代码通过率从 69.9%提升至 71.7%且消耗更少 token，论文接收率从 21.8%提升至 40.5%。

rss · 人人都是产品经理日榜 · 6月30日 02:39

**背景**: 哥德尔机由 Jürgen Schmidhuber 于 2003 年提出，是一种理论上的自我改进系统，要求在修改代码前进行数学证明，因此不切实际。后来的达尔文哥德尔机和赫胥黎哥德尔机放弃了证明，改用进化选择，但评估器是静态的。进化生物学中的红皇后假说指出，物种必须不断进化才能维持相对适应度，这启发了 RQGM 中智能体与评估器的共同进化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/紅皇后假說">红皇后假说 - 维基百科，自由的百科全书</a></li>
<li><a href="https://zh.wikipedia.org/zh-cn/哥德爾機">哥德尔机 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**标签**: `#AI`, `#自我进化`, `#英伟达`, `#红皇后哥德尔机器`, `#递归自我改进`

---

<a id="item-12"></a>
### [虎牙 VAM 1.0：一张照片生成实时多模态数字人](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247900769&idx=1&sn=2a765059e660fffa4d5f87c92e5c8343) ⭐️ 7.0/10 [技术]

虎牙推出了 VAM 1.0（Vivid Avatar Model），这是一个基于 DiT 架构的实时多模态数字人基础模型，仅需一张照片即可生成一个能进行 24 小时直播、聊天、唱跳和玩游戏的完全交互式 AI 数字人。 这一突破打破了行业三大壁垒——时间、交互和真实感，实现了 7×24 小时稳定直播和实时全双工对话与即时打断，可能改变直播和虚拟主播的格局。 VAM 1.0 以 480×832 分辨率、28 帧每秒的实时流式输出，支持全双工对话、即时打断、弹幕回复和多角色策略游戏，并从底层算子到模型权重进行了全链路工程优化。

rss · 量子位 · 6月30日 05:33

**背景**: 多模态数字人结合语音、面部表情和身体动作来创建逼真的虚拟形象。现有的大多数 AI 数字人产品仅支持单向内容输出。虎牙 VAM 1.0 利用 DiT（扩散 Transformer）架构实现了实时双向交互，与以往的解决方案不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.qbitai.com/2026/06/440236.html">24小时直播，只靠一张照片？虎牙实时多模态数字人VAM 1.0率先突围行业...</a></li>
<li><a href="https://news.qq.com/rain/a/20260630A0BBRJ00">虎牙实时多模态数字人来了，虎牙新玩法该咋看？_腾讯新闻</a></li>
<li><a href="https://ai-bot.cn/vam-1-0/">虎牙VAM 1.0 - 虎牙推出的实时多模态数字人基础模型 | AI工具集</a></li>

</ul>
</details>

**标签**: `#AI数字人`, `#多模态`, `#虎牙`, `#直播`, `#实时交互`

---

## 产品专栏 (Product Management)

<a id="item-1"></a>
### [AI 从提示工程转向循环工程](https://www.woshipm.com/ai/6422872.html) ⭐️ 9.0/10 [产品经理]

AI 开发领域正经历一场范式转变，从手动提示工程转向自主循环工程。黄仁勋、吴恩达和安德烈·卡帕西等行业领袖公开表示，未来 3-6 个月内，自改进循环将取代手工编写的提示词，Anthropic 报告称其超过 80%的工程师已在使用自改进循环。 这一转变从根本上改变了 AI 系统的设计方式，从人在回路中转变为人类作为架构师。产品经理和工程师将需要专注于定义目标、验证机制和持久化记忆，而不是编写单个提示词，从而实现全天候自主运行。 “循环工程”一词由 Google Chrome 工程师 Addy Osmani 于 2026 年 6 月提出，一份广泛传播的 11 页白皮书总结了核心概念。一个完整的循环包括五个关键动作：发现、交接、验证、持久化和调度，系统自主衍生子智能体并将输出反馈作为输入。

rss · 人人都是产品经理日榜 · 6月30日 09:32

**背景**: 传统的提示工程需要人类手动编写提示词、审查输出并迭代，实际上使人类成为循环本身。循环工程通过设计自主系统来取代这一过程，系统能够自主发现任务、执行、验证并持久化结果，无需人类干预，人类仅定义高级规则和验证标准。这种方法引入了新的挑战，如“验证债务”——AI 生成的输出被接受的速度快于验证速度所累积的风险——以及“认知投降”，即工程师可能丧失对系统行为的深入理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://addyosmani.com/blog/loop-engineering/">AddyOsmani.com - Loop Engineering</a></li>
<li><a href="https://cacm.acm.org/blogcacm/verification-debt-when-generative-ai-speeds-change-faster-than-proof/">Verification Debt: When Generative AI Speeds Change Faster ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#loop engineering`, `#product design`, `#paradigm shift`, `#autonomous systems`

---

<a id="item-3"></a>
### [PM Skills Marketplace 在制造业案例中大幅提升产品规划效率](https://www.woshipm.com/share/6422579.html) ⭐️ 8.0/10 [产品经理]

一位产品经理使用 PM Skills Marketplace 工具（phuryn/pm-skills）结合 Claude Code，为一家制造业企业构建宿舍管理系统，将原本需要数周的产品发现、市场研究和愿景定义工作压缩到几小时内完成。 这展示了如何将经过验证的产品管理方法论编码为可执行的 AI 工作流，从而大幅加速产品规划阶段，并使高级框架对更多从业者变得可及。 该工具串联了多个技能，例如 /discover（头脑风暴 → 假设映射 → 优先级排序 → 实验设计 → 机会解决方案树）和 /research（用户画像 → 市场细分 → 用户旅程 → 市场规模），生成了机会解决方案树和 TAM/SAM/SOM 分析等结构化输出。

rss · 人人都是产品经理 · 6月30日 09:11

**背景**: PM Skills Marketplace 是 GitHub 上的一个开源仓库，将 100 多个产品管理框架编码为可代理的技能、命令和插件，可与 Claude Code 等 AI 编码工具集成。Claude Code 是 Anthropic 开发的 AI 代理，能够通过自然语言读取代码库、编辑文件和运行命令。机会解决方案树（OST）是 Teresa Torres 创建的用于持续产品发现的视觉框架，帮助团队将期望结果映射到机会和解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/phuryn/pm-skills">GitHub - phuryn/pm-skills: PM Skills Marketplace: 100 ...</a></li>
<li><a href="https://github.com/product-on-purpose/pm-skills">GitHub - product-on-purpose/pm-skills: 67 plug-and-play, best ...</a></li>
<li><a href="https://agentskill.work/en/skills/phuryn/pm-skills">PM Skills Marketplace: 100+ Agentic Skills for Product ...</a></li>

</ul>
</details>

**标签**: `#PM Skills Marketplace`, `#AI工作流`, `#产品发现`, `#产品管理`, `#实践案例`

---

<a id="item-4"></a>
### [ChatGPT 广告开启品牌营销新入口](https://www.woshipm.com/share/6422655.html) ⭐️ 8.0/10 [产品经理]

ChatGPT 自 2026 年 2 月正式向品牌开放广告平台，Nexad 白皮书显示其点击率达 3.99%，几乎是传统聊天机器人广告的十倍，AI 工具和 3C 硬件是最适配的品类。 这标志着从搜索式营销向对话式营销的转变，让品牌能够在用户决策过程中触达他们，而非等到用户形成明确搜索词之后。对于出海品牌而言，ChatGPT 提供了一个高意图的新流量入口，用户群体年轻且受教育程度高。 白皮书显示 ChatGPT 广告点击率 3.99%，非 ChatGPT 聊天机器人广告为 0.40%，单次点击成本约贵一倍。每次会话的深层转化率约 10.5%，且九成以上是新用户。但广告库存目前仅对美国、加拿大、澳大利亚、新西兰和英国开放，自助投放仅限美国广告主。

rss · 人人都是产品经理 · 6月30日 07:50

**背景**: ChatGPT 是 OpenAI 开发的对话式 AI 聊天机器人，周活跃用户 9 亿，每天提问量超过 25 亿次。对话式营销利用 AI 驱动的实时互动引导顾客完成购物旅程，不同于传统基于关键词的搜索广告。Nexad 是一家 AI 原生广告平台，专注于聊天机器人广告投放。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nex.ad/">Nexad — AI-Native Advertising Platform</a></li>
<li><a href="https://www.huxiu.com/article/4827457.html">OpenAI的不归路：关于ChatGPT加入广告的五个冷思考-虎嗅网</a></li>
<li><a href="https://m.bjnews.com.cn/detail/1769070199168009.html">OpenAI“折腰”：ChatGPT卖广告，还能客观回答吗？</a></li>

</ul>
</details>

**标签**: `#ChatGPT广告`, `#品牌营销`, `#出海`, `#对话式营销`, `#Nexad`

---

<a id="item-5"></a>
### [飞书开源 CLI，剑指 AI Agent 基础设施](https://www.woshipm.com/ai/6422602.html) ⭐️ 8.0/10 [产品经理]

2026 年 3 月 28 日，飞书正式开源其 CLI 工具，采用 MIT 许可证并通过 npm 分发。该工具提供超过 200 条命令和 20 多个 AI Agent Skills，覆盖 11 个业务领域，使 AI 智能体能够无缝调用飞书的核心服务。 此举标志着飞书从“人与人协作”工具向“人与 Agent 协作”基础设施的战略转型，将商业价值锁定在云端而非客户端。它可能重塑 SaaS 的收费模式，从按人头订阅转向按用量计费，类似水电煤等基础设施。 CLI 是一个薄客户端，不存储任何本地数据；所有 API 调用、鉴权和数据存储仍在飞书服务端。该工具包含 200 多条命令，覆盖消息、文档、多维表格、电子表格、日历、邮件、任务、会议等，最新版本还提供 26 个 AI Agent Skills。

rss · 人人都是产品经理日榜 · 6月30日 06:51

**背景**: 飞书（海外版称 Lark）是字节跳动开发的企业协作平台，类似 Slack 或 Microsoft Teams。CLI（命令行界面）允许用户和 AI 智能体通过文本命令而非图形界面与系统交互。MIT 许可证是一种宽松的开源许可证，允许任何人自由使用、修改和分发代码，限制极少。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://feishu-cli.com/">Feishu CLI — Official Lark CLI Command-Line Tool for AI Agents & Developers</a></li>
<li><a href="https://github.com/larksuite/cli">GitHub - larksuite/cli: The official Lark/Feishu CLI tool ...</a></li>
<li><a href="https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/">Will Agentic AI Disrupt SaaS? - Bain & Company</a></li>

</ul>
</details>

**标签**: `#Feishu`, `#CLI`, `#open source`, `#AI`, `#SaaS`, `#product strategy`, `#platform`, `#monetization`

---

<a id="item-6"></a>
### [小红书投放：看评论区，别只看点赞](https://www.woshipm.com/share/6422527.html) ⭐️ 8.0/10 [产品经理]

一项新的分析框架揭示，小红书评论区比点赞和收藏更能预测广告转化效果。文章识别了七类关键评论信号，包括购买意向、用户顾虑、场景共鸣、竞品对比和负面反馈。 这一洞察帮助品牌和营销人员避免将广告预算浪费在表面数据高但转化低的笔记上。通过分析评论区，他们可以优化内容策略、改进广告定向，并更好地将内容与用户决策阶段对齐。 七类评论包括：购买信号（问价格/链接）、顾虑信号（担心质量/适用性）、场景信号（用户共鸣生活场景）、比较信号（提及竞品）和负面信号（抱怨）。文章建议品牌在加大投放前先看评论区，并将反复出现的问题作为内容选题的参考。

rss · 人人都是产品经理 · 6月30日 03:01

**背景**: 小红书是一个拥有超过 3 亿月活用户的中国社交电商平台，用户分享生活方式内容和产品评测。品牌常通过付费投流（聚光平台）来提升笔记曝光，但传统的点赞、收藏等指标可能具有误导性。平台算法优先推荐能引发真实用户互动的内容，而评论区比表面互动更能反映用户的购买意图。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1898315756954944656">终于有人把小红书投流一次性说清楚了！！！ - 知乎</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/32458926363">小红书投流全攻略！一文看懂官方6大推广工具 - 知乎</a></li>
<li><a href="https://www.sohu.com/a/934186364_100037848">小红书直播间投流顺序全揭秘：9大法则让每一分预算都炸出效果</a></li>

</ul>
</details>

**标签**: `#小红书投放`, `#评论区分析`, `#投流策略`, `#营销洞察`

---

<a id="item-7"></a>
### [618 给 AI 上了一课：Agent 并非万能解药](https://www.woshipm.com/ai/6422432.html) ⭐️ 8.0/10 [产品经理]

在 2026 年 618 购物节期间，电商平台大力推广 AI 购物助手，但消费者接受度低，总销售额同比仅增长 0.9%。调查显示，仅约 20%的用户在快消品选购时参考 AI 建议，几乎无人直接通过 AI 下单。 这一结果挑战了 AI 和 Agent 技术能自动驱动商业成功的说法，凸显了技术效率与真实用户需求之间的鸿沟。它迫使科技公司重新思考 AI 商业化策略，从流量变现转向直接创造价值，正如字节跳动的豆包转向付费专业版。 京东的 JoyAI App 在 618 期间累计对话用户突破 300 万，但未披露转化数据。豆包日活超 2 亿，每天电商交易额仅约一千万元，远低于每天数千万元的成本。

rss · 人人都是产品经理日榜 · 6月30日 02:17

**背景**: AI Agent（人工智能代理）是一种能够感知环境、自主决策并执行动作的智能实体，超越了简单的聊天机器人，可以执行复杂任务。在电商中，Agent 被期望整合信息、比价并自动下单，降低决策成本。然而，购物并非纯粹的功能性行为，许多消费者享受浏览和发现商品的乐趣，追求情绪价值，而 AI 目前无法满足这一点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1895877953453265781">什么是AI Agent？AI Agent综述，看这一篇就够了！ - 知乎</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1928150775286203320">一文读懂 AI Agent：定义、最新进展与未来趋势 - 知乎</a></li>
<li><a href="https://blog.csdn.net/l01011_/article/details/146495533">AI时代，一文彻底搞懂天天被提到的Agent是什么？_ai agent概念-CSDN博...</a></li>

</ul>
</details>

**标签**: `#AI商业化`, `#Agent`, `#618`, `#电商`, `#产品策略`

---

<a id="item-8"></a>
### [企业 AI 分层调用：小模型经济学节省 90%成本](https://www.woshipm.com/ai/6422939.html) ⭐️ 8.0/10 [产品经理]

Lindy、Uber 等公司开始用 DeepSeek V4 替代 Claude 等昂贵模型，节省高达 90%的成本。这一转变标志着‘小模型经济学’的兴起，企业通过分层调用模型来优化 AI 支出。 这一趋势从根本上改变了企业使用 AI 的方式，从追求 Token 最大化转向成本高效的分层使用。它通过降低先进 AI 能力的成本，推动更广泛的 AI 应用，并为 OpenRouter 等模型路由平台创造了新的商业机会。 DeepSeek V4 Flash 的价格比 Anthropic 模型低 20-50 倍。模型路由平台 OpenRouter 完成 1.13 亿美元 B 轮融资，每周处理 25 万亿 Token，拥有 800 万用户。

rss · 人人都是产品经理日榜 · 6月30日 10:55

**背景**: Token 是 AI 模型输入输出的计量单位，每次 API 调用消耗 Token 并产生费用。‘小模型经济学’是指将简单任务分配给便宜的小模型，复杂任务留给昂贵的旗舰模型的策略，这依赖于模型路由系统自动将请求分配给最具成本效益的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.woshipm.com/tag/小模型经济学">小模型经济学 - 人人都是产品经理</a></li>
<li><a href="https://huggingface.co/collections/deepseek-ai/deepseek-v4">DeepSeek-V4 - a deepseek-ai Collection - Hugging Face</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>

</ul>
</details>

**标签**: `#AI成本管控`, `#模型分层调用`, `#小模型经济学`, `#DeepSeek`, `#Claude`, `#企业AI策略`

---

## 热搜焦点 (Trending)

<a id="item-9"></a>
### [中国 PMI 重返扩张区间，八部门发文推动工业互联网](https://www.tmtpost.com/8047537.html) ⭐️ 8.0/10 [热搜]

中国 6 月制造业采购经理指数（PMI）回升至 50.3%，重返扩张区间；工业和信息化部等八部门联合印发《关于推动工业互联网高质量发展的实施意见》；中上协数据显示，5 月全市场新增首发上市公司 13 家，首发募资总额 111.1 亿元。 这些动态表明中国经济趋于稳定，政府正大力推进数字化工业转型；IPO 数据反映了市场持续活跃，而工业互联网政策旨在加速全国智能制造进程。 PMI 的 50.3%刚好高于 50%的荣枯线；工业互联网政策提出到 2030 年建设 5 万张工业 5G 专网；此外，AI 初创公司 Kimi 估值升至 315 亿美元，年度经常性收入（ARR）突破 3 亿美元，增长强劲。

rss · 钛媒体 · 6月30日 23:20

**背景**: 采购经理指数（PMI）是重要的经济先行指标，高于 50%表示制造业处于扩张状态。工业互联网是指工业系统与互联网技术的深度融合，旨在实现智能制造和数据驱动的优化。此次发文的八部门包括工业和信息化部、国家发展改革委等。Kimi 是月之暗面公司开发的中国 AI 助手，在大语言模型领域参与竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.163.com/dy/article/L0O2ELPM05118O92.html">【钛晨报】推动工业互联网高质量发展，八部门联合发文；中上协：5月全...</a></li>
<li><a href="https://www.36kr.com/newsflashes/3875210246418689">Kimi估值升至315亿美元，ARR突破3亿美元 - 36氪</a></li>
<li><a href="http://www.zqrb.cn/finance/hangyedongtai/2026-06-30/A1782809598239.html">八部门联合发文推动工业互联网高质量发展-证券日报网</a></li>

</ul>
</details>

**标签**: `#PMI`, `#IPO`, `#industrial internet`, `#Kimi`, `#OpenAI`, `#Huawei`, `#iPhone`, `#Porsche`, `#brain-computer interface`, `#film box office`

---

<a id="item-10"></a>
### [AI 算力把全球电网逼到极限](https://www.tmtpost.com/8047043.html) ⭐️ 8.0/10 [热搜]

AI 算力的快速扩张，特别是大规模模型训练，正在对全球电网造成前所未有的压力，可能导致电力短缺和基础设施挑战。 这很重要，因为电力供应限制可能成为 AI 进一步发展的瓶颈，推高科技公司的运营成本，并迫使公用事业公司加速电网升级和可再生能源部署。 训练单个大型 AI 模型可能消耗相当于数千户家庭数月用电量的电力，而超大规模数据中心所需的功率密度对当地电网基础设施造成压力。

rss · 钛媒体 · 6月30日 10:45

**背景**: AI 模型，特别是大型语言模型，需要巨大的计算资源进行训练，通常要在数千个 GPU 上运行数周。容纳这些系统的数据中心消耗大量电力用于计算和冷却。许多电网并非为如此快速的电力需求增长而设计，这引发了关于可靠性的担忧以及新增发电能力的必要性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.technologyreview.com/2025/05/20/1116327/ai-energy-usage-climate-footprint-big-tech/">We did the math on AI’s energy footprint. Here’s the story ...</a></li>
<li><a href="https://iee.psu.edu/news/blog/why-ai-uses-so-much-energy-and-what-we-can-do-about-it">AI’s Energy Demand: Challenges and Solutions for a ...</a></li>
<li><a href="https://www.belfercenter.org/research-analysis/ai-data-centers-us-electric-grid">AI, Data Centers, and the U.S. Electric Grid: A Watershed ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#computing power`, `#energy`, `#power grid`, `#shortage`

---

<a id="item-11"></a>
### [AI 需求导致存储成本飙升 386%，引发结构性通胀](https://www.tmtpost.com/8047039.html) ⭐️ 8.0/10 [热搜]

最新分析报告指出，由于 AI 需求激增，存储成本已飙升 386%，这标志着从周期性价格波动转向由 AI 算力需求驱动的长期结构性短缺。 存储领域的结构性通胀正在重塑全球电子供应链，迫使苹果、微软等公司提价，可能抑制消费需求，同时使存储制造商受益。 主要存储制造商已将 70%的新增产能转向 AI 用的 HBM（高带宽内存），挤压了消费级芯片的供应，并通过长期“照付不议”合同锁定产能。

rss · 钛媒体 · 6月30日 09:22

**背景**: 结构性通胀是指由于经济部门结构失衡而非需求拉动或成本推动导致的物价持续上涨。在此案例中，AI 对高性能内存的旺盛需求造成了结构性错配，存储产能从传统消费市场转向 AI 数据中心，导致价格持续上涨。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/结构性通胀/4069763">结构性通胀_百度百科</a></li>
<li><a href="https://baike.baidu.com/item/结构型通货膨胀/11042783">结构型通货膨胀_百度百科</a></li>
<li><a href="https://www.tmtpost.com/8047039.html">存储涨386%，AI正在制造一场“结构性通胀”-钛媒体官方网站</a></li>

</ul>
</details>

**标签**: `#AI`, `#storage`, `#inflation`, `#structural change`, `#technology trends`

---

<a id="item-13"></a>
### [沃什想复活哪个格林斯潘？](https://www.huxiu.com/article/4871675.html?f=rss) ⭐️ 7.0/10 [热搜]

这篇文章分析了当前经济政策，特别是与凯文·沃什相关的政策，旨在复活前美联储主席艾伦·格林斯潘的哪一部分遗产。它质疑这种复活是聚焦于格林斯潘成功的危机管理，还是他后来受到批评的政策。 这一讨论之所以重要，是因为格林斯潘的任期塑造了现代货币政策，任何复活其做法的尝试都可能标志着美国经济战略的重大转变。它影响到依赖稳定经济指导的投资者、政策制定者和公众。 文章特别审视了前美联储理事凯文·沃什，他可能是复活格林斯潘时代政策的倡导者。文章对比了格林斯潘早期以巧妙处理危机著称的声誉，与他在 2008 年金融危机中扮演的角色。

rss · 虎嗅 · 6月30日 16:09

**背景**: 艾伦·格林斯潘于 1987 年至 2006 年担任美联储主席，期间经历了经济增长期以及 1987 年股市崩盘等危机。他的遗产存在争议：因处理互联网泡沫而受到赞扬，但也因一些被认为导致了 2008 年金融危机的政策而受到批评。前美联储理事凯文·沃什常被提及为潜在的美联储未来主席，他可能会借鉴格林斯潘的做法。

**标签**: `#economics`, `#Greenspan`, `#policy`, `#finance`

---

<a id="item-14"></a>
### [Momenta 港股 IPO：从技术理想转向财务杠杆](https://www.tmtpost.com/8047574.html) ⭐️ 7.0/10 [热搜]

自动驾驶先驱 Momenta 已提交港股上市申请，将其市场叙事从技术演示转向财务杠杆，强调量产收入和软件授权策略。 此次 IPO 标志着自动驾驶行业的一个重要里程碑，表明行业正转向可持续的商业模式。它可能影响其他 AI 和机器人公司对待上市和盈利的方式。 Momenta 的战略侧重于从汽车制造商获得量产收入，并授权其自动驾驶软件，而非依赖风险投资。该公司被称为港股'首个物理 AI 股票'。

rss · 钛媒体 · 6月30日 13:56

**背景**: 物理 AI 指的是在物理世界中运行和交互的 AI 系统，例如自动驾驶汽车和机器人。Momenta 利用深度学习和计算机视觉开发自动驾驶技术。其软件授权模式允许汽车制造商将技术集成到车辆中，从而产生经常性收入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/generative-physical-ai/">What is Physical AI? | NVIDIA Glossary</a></li>
<li><a href="https://evmagazine.com/self-drive/nuro-expands-with-licensing-model-for-autonomous-tech">Nuro Expands with Licensing Model for Autonomous Tech | EV Magazine</a></li>

</ul>
</details>

**标签**: `#Momenta`, `#IPO`, `#autonomous driving`, `#financial leverage`, `#Hong Kong listing`

---

<a id="item-15"></a>
### [VC 材料龙头拟与亘元新材合并，宁德时代为重要股东](https://www.tmtpost.com/8047351.html) ⭐️ 7.0/10 [热搜]

锂电池电解液添加剂 VC（碳酸亚乙烯酯）的龙头企业日科化学，在经历四年 IPO 辅导后，计划与亘元新材合并。全球最大电池制造商宁德时代是亘元新材的重要股东。 此次合并整合了锂电池关键上游材料供应链，且直接涉及宁德时代作为重要股东。这标志着在电池材料领域，企业正从 IPO 转向并购作为更快的市场整合路径。 日科化学在经历了四年 IPO 辅导后，决定转而推进此次合并。VC（碳酸亚乙烯酯）是一种关键的电解液添加剂，可将电池循环寿命提升 10%-15%，并有助于防止过充和气胀。

rss · 钛媒体 · 6月30日 11:10

**背景**: VC（碳酸亚乙烯酯）是锂离子电池中常用的电解液添加剂，能在负极形成稳定的固体电解质界面（SEI），从而提升电池性能与安全性。日科化学是该添加剂的主要生产商，而亘元新材是电池材料领域的另一家企业。宁德时代作为亘元新材的股东，凸显了此次合并对保障供应链的战略重要性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eet-china.com/mp/a354551.html">探究！VC、PS、FEC和DTD添加剂对电池性能的影响！</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1917869539150004638">碳酸亚乙烯酯 VC：锂电成膜保护核心添加剂 - 知乎</a></li>

</ul>
</details>

**标签**: `#M&A`, `#battery materials`, `#CATL`, `#corporate finance`

---