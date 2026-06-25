---
layout: default
title: "Horizon Summary: 2026-06-25 (ZH)"
date: 2026-06-25
lang: zh
---

> 从 294 条内容中筛选出 18 条重要资讯。

---

1. [OpenAI 携手 Broadcom 发布首款自研 AI 芯片 'Jalapeno'](#item-1) ⭐️ 9.0/10
2. [高通以 40 亿美元收购 AI 初创公司 Modular](#item-2) ⭐️ 9.0/10
3. [TRM 思考奖励模型：量化大模型推理质量](#item-3) ⭐️ 9.0/10
4. [电子器件可直接打印到活体组织上](#item-4) ⭐️ 9.0/10
5. [Anthropic 指控阿里巴巴对 Claude 发动大规模蒸馏攻击](#item-5) ⭐️ 9.0/10
6. [Databricks 领导者呼吁为 Agent Cloud 构建开放生态系统](#item-6) ⭐️ 8.0/10
7. [Claude Slackbot 升级：多人、主动、持久化智能体](#item-7) ⭐️ 8.0/10
8. [微信豪赌小程序范式变革](#item-8) ⭐️ 8.0/10
9. [OpenAI Codex 漏洞导致过度日志写入，可能损坏 SSD](#item-9) ⭐️ 8.0/10
10. [国产存储登顶 IO500 生产榜单](#item-10) ⭐️ 8.0/10
11. [硅谷应向它鄙视的电子表格分析师学习](#item-11) ⭐️ 7.0/10
12. [美国必须避免的量子计算供应链陷阱](#item-12) ⭐️ 7.0/10
13. [大型 AI 实验室为何大量招聘哲学家](#item-13) ⭐️ 7.0/10
14. [AI 投资挤压企业预算](#item-14) ⭐️ 7.0/10
15. [人机即兴：AI 协作的新范式](#item-15) ⭐️ 7.0/10
16. [中国的“千帆星座”：星链的新对手？](#item-16) ⭐️ 7.0/10
17. [警惕伪装成官方页面的恶意 curl 脚本](#item-17) ⭐️ 7.0/10
18. [OpenTag：在 GitHub 和 Slack 中 @ AI 智能体的开源协议](#item-18) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI 携手 Broadcom 发布首款自研 AI 芯片 'Jalapeno'](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI 与 Broadcom 联合发布了专为大语言模型推理设计的自研芯片 Jalapeno，由台积电制造。该芯片从设计到量产仅用九个月，部分流程借助 OpenAI 自身模型加速完成。 这标志着 OpenAI 首次涉足自研芯片领域，减少了对 NVIDIA GPU 在推理任务上的依赖，有望大幅降低成本。这也反映了行业趋势：领先的 AI 公司正通过定制硬件来优化自身模型的性能与效率。 Jalapeno 是一款纯推理芯片，专为运行已训练好的模型而优化，而非用于训练。社区讨论中提到的权重固化在 ROM 中的架构理念，可能通过将乘法运算简化为加法来实现极高的吞吐量。

hackernews · jamdesk · 6月24日 17:47 · [社区讨论](https://news.ycombinator.com/item?id=48663324)

**背景**: AI 推理芯片是专门用于高效运行已训练模型的处理器，与 NVIDIA H100 等兼顾训练与推理的芯片不同。谷歌等公司早已使用自研 TPU 进行推理，而 OpenAI 此前完全依赖 NVIDIA 和 Azure 的 GPU。这一自研芯片的推出反映了 AI 推理工作负载的快速增长——在生产系统中，推理已占据大部分计算资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip | OpenAI</a></li>
<li><a href="https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html">OpenAI and Broadcom reveal Jalapeno, first AI chip in partnership</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/openai-jalapeno-ai-inference-chip-broadcom">OpenAI unveils Jalapeño chip for large-scale inference workloads</a></li>

</ul>
</details>

**社区讨论**: 评论者对 OpenAI 声称其模型加速了芯片设计表示怀疑，认为这可能是模糊的营销话术。也有人讨论了权重固化在 ROM 中的架构优势，指出虽然这种设计能带来巨大吞吐量，但会导致芯片体积极大。部分评论将其与谷歌 TPU 以及 Taalas 等将模型权重直接烧录进硅片的初创公司进行了比较。

**标签**: `#AI hardware`, `#OpenAI`, `#semiconductors`, `#inference chips`, `#Broadcom`

---

<a id="item-2"></a>
## [高通以 40 亿美元收购 AI 初创公司 Modular](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/) ⭐️ 9.0/10

高通宣布以约 40 亿美元收购 AI 初创公司 Modular，该公司专注于编译器技术和 Mojo 编程语言。此次收购旨在增强高通的 AI 推理能力和编译器堆栈。 此次收购巩固了高通在 AI 推理市场的地位，为基于 ARM 的芯片提供了 NVIDIA CUDA 生态系统的替代方案。它可能加速 ARMv9 在 AI 工作负载中的采用，并挑战 NVIDIA 在 AI 计算领域的主导地位。 据路透社报道，该交易价值 40 亿美元。Modular 的技术包括 MAX 编译器堆栈和 Mojo 编程语言，后者设计为类似 Python 但具有高性能，适用于 AI 和机器学习工作负载。

hackernews · timmyd · 6月24日 13:49 · [社区讨论](https://news.ycombinator.com/item?id=48659798)

**背景**: Modular 由 Chris Lattner 创立，他是 LLVM 和 Swift 的原始创建者。该公司开发了 Mojo 编程语言，它结合了 Python 的易用性和类似 C 的性能，以及用于跨多种硬件优化 AI 推理的 MAX 编译器堆栈。高通是 ARM 芯片的领先设计商，此次收购符合其从移动领域扩展到 AI 和数据中心市场的战略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.aibase.com/news/828">AI startup Modular raises $100 million in funding to simplify AI ...</a></li>
<li><a href="https://mlc.ai/">MLC - A Community of Machine Learning Compilers</a></li>

</ul>
</details>

**社区讨论**: 社区对此次收购表达了复杂情绪。一些人注意到时机问题，并对 Mojo 的发展方向提出质疑，而另一些人则强调了与 ARMv9 的战略契合以及挑战 NVIDIA CUDA 堆栈的潜力。也有人持怀疑态度，因为创始人 Chris Lattner 过去曾评论硬件公司未能打造出好的 AI 堆栈。

**标签**: `#Qualcomm`, `#Modular`, `#AI`, `#acquisition`, `#compiler`

---

<a id="item-3"></a>
## [TRM 思考奖励模型：量化大模型推理质量](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247899199&idx=3&sn=b0d6764e50d881295fd85b75f8f9434a) ⭐️ 9.0/10

这项工作首次提供了评估推理过程本身（而不仅仅是最终答案）的可靠指标，对于提高强化学习训练的稳定性和模型对齐至关重要。它使得对大模型推理能力进行更有针对性的优化成为可能，并为评估思维链质量树立了新标准。 TRM 基于 ME²原则构建，并使用有向无环图（DAG）抽象复杂推理结构。它通过句子级思考监督进行训练，可应用于测试时扩展（Test-Time Scaling）和强化学习，在 STEM 和数学任务上提升模型性能。

rss · 量子位 · 6月24日 04:00

**背景**: 奖励模型在强化学习中用于向语言模型提供反馈，但传统模型通常只评估最终结果（结果奖励模型），而非推理过程。过程奖励模型尝试对每一步评分，但缺乏细粒度监督。TRM 通过引入句子级思考监督解决了这一问题，从而能够更准确地评估推理质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://36kr.com/p/3866659734279170">TRM 思 考 奖 励 模 型 上线，大 模 型 推理质量终于能量化了-36氪</a></li>
<li><a href="https://www.aitntnews.com/newDetail.html?newId=26520">TRM 思 考 奖 励 模 型 上线，大 模 型 推理质量终于能量化了 | ICML‘26 Oral</a></li>
<li><a href="https://arxiv.org/abs/2509.25409">From Faithfulness to Correctness: Generative Reward Models that ...</a></li>

</ul>
</details>

**标签**: `#大模型`, `#推理质量`, `#奖励模型`, `#ICML`, `#开源`

---

<a id="item-4"></a>
## [电子器件可直接打印到活体组织上](https://www.economist.com/science-and-technology/2026/06/24/electronics-can-now-be-printed-onto-living-tissues) ⭐️ 9.0/10

莱斯大学的研究人员开发出一种方法，利用聚焦微波束将电子电路直接 3D 打印到包括活体组织在内的脆弱材料上。这一突破使得电子器件可以打印到牛股骨、人工髋关节甚至活体叶片等表面上。 这项技术通过将电子器件与活体组织无缝集成，可能彻底改变医疗植入物和生物混合设备，为脑植入物、生物传感器和先进假肢带来新的可能性。它代表了生物电子学和组织工程领域的重大范式转变，有望带来更有效、创伤更小的医疗手段。 该打印过程使用聚焦微波束沉积导电材料，而不会损伤下方的活体组织。该技术已在多种基底上得到验证，包括骨骼、合成植入物和植物叶片，展示了其在不同生物医学应用中的多功能性。

rss · The Economist · 6月24日 16:33

**背景**: 生物混合系统将生物材料（如细胞或组织）与人工组件（如电子器件或机械结构）相结合，融合了生物体的能力与人造技术的精确性。传统上，将电子器件与活体组织集成的方法通常涉及刚性组件或侵入性操作，可能导致损伤或排异反应。这种新方法通过将电路直接打印到组织上，提供了一种更温和、更直接的生物混合设备制造方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.economist.com/science-and-technology/2026/06/24/electronics-can-now-be-printed-onto-living-tissues">Electronics can now be printed onto living tissues</a></li>
<li><a href="https://en.wikipedia.org/wiki/Biohybrid_system">Biohybrid system - Wikipedia</a></li>
<li><a href="https://singularityumexico.com/en/scientists-merge-biology-and-technology-by-3d-printing-electronics-inside-living-worms/">Scientists Merge Biology and Technology by 3D Printing Electronics ...</a></li>

</ul>
</details>

**标签**: `#bioelectronics`, `#medical devices`, `#tissue engineering`, `#printed electronics`, `#biotechnology`

---

<a id="item-5"></a>
## [Anthropic 指控阿里巴巴对 Claude 发动大规模蒸馏攻击](https://www.cnbc.com/2026/06/24/anthropic-alibaba-distillation-campaign.html) ⭐️ 9.0/10

Anthropic 于 2026 年 6 月 10 日致信美国参议院银行委员会，指控阿里巴巴通过近 2.5 万个欺诈账户，在 2026 年 4 月 22 日至 6 月 5 日期间与 Claude 进行了超过 2880 万次交互，非法提取其 Claude AI 模型的能力。 这一事件凸显了中美之间围绕 AI 知识产权盗窃的紧张局势升级，并对专有 AI 模型的安全性提出了关键质疑。如果指控成立，可能为针对模型蒸馏攻击的法律和监管行动树立先例，影响 AI 公司保护其模型的方式。 此次攻击针对 Anthropic 的先进模型 Mythos Preview，信件在国会 AI 听证会前夕发出。阿里巴巴尚未回应指控，且该公司近期被列入五角大楼的'中国军事公司'清单。

telegram · zaihuapd · 6月25日 01:36

**背景**: 模型蒸馏是一种合法的机器学习技术，其中较小的'学生'模型通过从较大的'教师'模型的输出中学习，以较低的计算成本实现相似的性能。然而，当未经授权对专有模型使用时，就变成了蒸馏攻击，一种知识产权盗窃形式。美国政府此前曾指责中国大规模窃取 AI 知识产权，并于 2026 年 6 月以国家安全为由限制 Anthropic 的 Mythos 和 Fable 模型出口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.freebuf.com/articles/471439.html">大 模 型 中的 蒸 馏 攻 击 技术原理 - FreeBuf网络安全行业门户</a></li>
<li><a href="https://jangwook.net/zh/blog/zh/ai-distillation-attacks-enterprise-defense/">AI 模 型 蒸 馏 攻 击 实态——CTO必知的IP保护策略</a></li>
<li><a href="https://www.amazonaws.cn/en/knowledge/what-is-model-distillation/">what-is-model-distillation - 什么是模型蒸馏 - 亚马逊云科技</a></li>

</ul>
</details>

**社区讨论**: 许多评论者表示怀疑，认为 Anthropic 本身在未经许可的情况下使用大量人类生成内容训练 Claude，因此这一指控显得虚伪。一些人指出，这种竞争情报收集是行业标准做法，而另一些人则提供了技术背景，说明中国转售商如何通过汇集账户和转售输出来压低官方 API 价格。

**标签**: `#AI安全`, `#模型蒸馏`, `#知识产权`, `#地缘政治`, `#Anthropic`

---

<a id="item-6"></a>
## [Databricks 领导者呼吁为 Agent Cloud 构建开放生态系统](https://www.latent.space/p/databricks) ⭐️ 8.0/10

在一次罕见的联合采访中，Databricks 联合创始人 Matei Zaharia 和 Reynold Xin 主张，开放生态系统对于每家公司构建自己的 Agent Cloud 至关重要。 这一立场强化了在快速发展的 AI 基础设施领域中开源原则的重要性，可能影响企业大规模采用和部署 AI 代理的方式。 采访未提供具体技术细节，但领导者强调，专有锁定将阻碍基于代理的架构在各行业的广泛采用。

rss · Latent Space · 6月24日 18:53

**背景**: Agent Cloud 是指基于云的平台，用于部署和编排 AI 代理，通常集成大语言模型和检索增强生成（RAG）。Databricks 是领先的数据和 AI 平台，最近将 OpenAI 的前沿模型整合到其生态系统中。AI 中的开放生态系统概念意味着工具、模型和基础设施可互操作，不受单一供应商控制，使公司能够定制并拥有自己的 AI 解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.mainfra.me/p/agent-clouds">Agent Clouds - by Philippe Page - Mainframe</a></li>
<li><a href="https://www.databricks.com/">Databricks : Leading Data and AI Platform for Enterprises</a></li>
<li><a href="https://sacra.com/c/databricks/">Databricks revenue, valuation & funding | Sacra</a></li>

</ul>
</details>

**标签**: `#open source`, `#AI ecosystem`, `#agent clouds`, `#Databricks`, `#machine learning`

---

<a id="item-7"></a>
## [Claude Slackbot 升级：多人、主动、持久化智能体](https://www.latent.space/p/ainews-claude-tag-multiplayer-proactive) ⭐️ 8.0/10

Anthropic 发布了 Claude Slackbot 的重大升级，引入了多人协作、主动行动和持久化记忆的智能体能力，允许多个 AI 智能体协作、无需提示即可主动行动，并在多次会话中保留记忆。 此次升级将 Slack 从简单的聊天机器人界面转变为持久化、协作式 AI 智能体平台，通过让智能体作为持续队友而非孤立助手工作，可能彻底改变工作流自动化和团队生产力。 升级使智能体能够在共享 Slack 频道中协同工作（多人协作），基于上下文主动行动（主动），并在多次交互中保持持久身份和记忆（持久化），这基于 Anthropic 的 Claude 模型和 Slack 现有的 Slackbot 基础设施。

rss · Latent Space · 6月24日 07:14

**背景**: 传统 AI 助手是被动且基于会话的，每次任务后丢失上下文。多智能体系统涉及多个交互智能体解决复杂问题，而主动智能体监控上下文并在被询问前主动参与。持久化智能体跨会话保持身份和记忆。此次升级将这三个概念整合到 Slack 中，将 AI 从私人助手转变为持久队友。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multi-agent_system">Multi-agent system - Wikipedia</a></li>
<li><a href="https://slack.com/blog/productivity/proactive-ai-agents-definition-core-components-and-business-value">Proactive AI Agents: Definition, Core Components, and Business Value | Slack</a></li>
<li><a href="https://gravitydevops.com/ai-news-roundup-2026-06-24-evening-claude-tag-slack-agents/">AI News Roundup: Claude Tag Brings Persistent AI Agents Into Slack</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude`, `#Slack`, `#agents`, `#product update`

---

<a id="item-8"></a>
## [微信豪赌小程序范式变革](https://www.huxiu.com/article/4869561.html?f=rss) ⭐️ 8.0/10

微信正在从根本上改写其小程序范式和流量分发逻辑，这标志着该平台的一次重大战略赌注。 这一转变将深刻影响微信生态内的数百万开发者和商家，可能重塑流量分配方式以及小程序的构建和发现机制。 虽然具体技术细节尚未披露，但这一变化涉及小程序开发的新范式以及流量分发逻辑的修订，将偏离现有模式。

rss · 虎嗅 · 6月24日 22:50

**背景**: 微信小程序是运行在微信生态系统内的轻量级应用，用户无需离开微信即可使用服务。流量分发逻辑指的是微信如何将用户流量分配给不同的小程序，这历来是商业成功的关键因素。通过改写范式和分发逻辑，微信正试图解决开发者痛点并改善内容发现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/beautywe">BeautyWe - GitHub</a></li>
<li><a href="https://zengzhangkexue.com/?p=70289">浅谈直播间的 流 量 密码和底层 分 发 逻 辑 _增长科学</a></li>
<li><a href="https://m.okjike.com/originalPosts/627e1fdf3ac80ccc5c07223a?s=ewoidSI6ICI1ZDE1YzEzNmM3ZmUwODAwMTg0YTgwYTMiCn0=">电商向的平台 流 量 分 发 逻 辑 对比：拼多多🆚快手🆚阿里🆚...</a></li>

</ul>
</details>

**标签**: `#WeChat`, `#mini-programs`, `#traffic distribution`, `#platform strategy`, `#China tech`

---

<a id="item-9"></a>
## [OpenAI Codex 漏洞导致过度日志写入，可能损坏 SSD](https://www.v2ex.com/t/1222665#reply13) ⭐️ 8.0/10

OpenAI Codex 的一个漏洞导致它以极高频率向本地 SQLite 文件（~/.codex/logs_2.sqlite）写入 TRACE 级别日志，可能在数月内耗尽消费级 SSD 的寿命。社区分享了一个临时解决方案，使用 SQLite 触发器阻止日志插入。 该漏洞可能悄无声息地毁掉重度 Codex 用户的 SSD，导致数据丢失和硬件故障。它暴露了本地持续运行的 AI 工具在日志管理上的严重疏忽。 报告显示 Codex 每年可写入高达 640 TB，有用户在 21 天内记录了 37 TB 的写入量。临时方案使用 SQLite 触发器忽略对 logs 表的所有插入操作，但这并非官方补丁。

rss · V2EX · 6月25日 00:39

**背景**: OpenAI Codex 是一个命令行工具，利用 AI 从自然语言生成代码。它维护一个本地 SQLite 数据库用于日志记录。TRACE 是最详细的日志级别，用于调试，但通常不应占据用户端日志的主导地位。对 SSD 的过度写入会因有限的写入寿命而显著缩短其使用寿命。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://trustpost.org/openai-codex-logging-bug-ssd/">OpenAI Codex Bug Writes 640 TB Per Year and Can Kill Your SSD</a></li>
<li><a href="https://www.techtimes.com/articles/318876/20260622/openai-codex-cli-bug-silently-writes-640-tb-year-your-ssd-no-patch.htm">OpenAI Codex CLI Bug Silently Writes 640 TB/Year to Your SSD : No...</a></li>
<li><a href="https://www.sqlite.org/lang_createtrigger.html">CREATE TRIGGER</a></li>

</ul>
</details>

**社区讨论**: V2EX 社区讨论（13 条回复）确认了该漏洞，并分享了额外的诊断步骤和临时方案，许多用户报告了类似的 SSD 写入问题，并对缺乏官方修复表示担忧。

**标签**: `#OpenAI`, `#Codex`, `#bug`, `#SSD`, `#logging`

---

<a id="item-10"></a>
## [国产存储登顶 IO500 生产榜单](https://www.tmtpost.com/8039798.html) ⭐️ 8.0/10

国产存储系统在 IO500 生产榜单的带宽和元数据两个类别中均获得第一名，标志着行业的历史性里程碑。 这表明中国存储技术在高性能计算领域已达到世界一流水平，可能重塑全球存储系统的竞争格局。 IO500 生产榜单要求提交的系统满足冗余和实际使用的严格标准，因此这一成就尤其重要，它反映的是可部署的实际性能而非理论基准。

rss · 钛媒体 · 6月25日 02:58

**背景**: IO500 基准测试是评估高性能存储系统的领先标准，测量带宽（IOR）和元数据（mdtest）性能。生产榜单是其中的一个子集，仅包含在实际生产环境中使用的系统，确保结果代表真实世界的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://io500.org/">IO500 - ISC26 - Production List</a></li>
<li><a href="https://io500.org/list/isc23/production">IO500 - ISC23 - Production List</a></li>

</ul>
</details>

**标签**: `#storage`, `#high-performance computing`, `#IO500`, `#China`, `#technology milestone`

---

<a id="item-11"></a>
## [硅谷应向它鄙视的电子表格分析师学习](https://www.economist.com/business/2026/06/24/silicon-valley-has-much-to-learn-from-the-spreadsheet-jockeys-it-despises) ⭐️ 7.0/10

《经济学人》发表评论文章，认为硅谷对基于电子表格的财务分析的轻视，忽视了传统金融在纪律性和严谨性方面提供的宝贵经验。 这挑战了优先考虑增长和颠覆而非财务基础的主流科技文化，可能影响初创公司和科技企业对待商业战略和问责制的方式。 文章的副标题“即使金融市场不同意”表明，尽管市场持怀疑态度，但采纳财务严谨性的论点仍然有效。

rss · The Economist · 6月24日 19:17

**背景**: 硅谷长期以来以崇尚快速增长、颠覆和“快速行动，打破常规”的文化为特征，常将传统财务分析视为缓慢和保守。电子表格分析师——构建详细模型的财务分析师——有时被科技创业者视为缺乏远见。这篇文章认为这种轻视是错误的，因为财务纪律可以为不可持续的增长提供关键约束，并帮助公司实现长期成功。

**标签**: `#Silicon Valley`, `#finance`, `#business strategy`, `#tech culture`, `#analysis`

---

<a id="item-12"></a>
## [美国必须避免的量子计算供应链陷阱](https://www.economist.com/by-invitation/2026/06/24/the-quantum-computing-mistakes-america-must-avoid) ⭐️ 7.0/10

《经济学人》的一篇评论文章警告称，美国在减少量子计算供应链依赖方面的努力，如果管理不当，可能会犯下战略错误。 量子计算是一项关键的新兴技术，供应链漏洞可能削弱美国的竞争力和国家安全。文章强调需要采取平衡的方法，避免在忽视全球合作伙伴关系的情况下过度依赖国内生产。 作者 Joshua Zoffer 和 Chris Miller 认为，虽然摆脱依赖很重要，但仓促或目标不明确的政策可能造成新的漏洞。他们警告不要重蹈半导体等其他高科技领域的覆辙。

rss · The Economist · 6月24日 11:06

**背景**: 量子计算依赖于复杂的全球供应链，涉及低温系统、控制电子设备和量子比特材料等专用组件。美国目前在许多此类组件上依赖外国供应商，这引发了对韧性和安全的担忧。半导体行业类似的担忧导致了《芯片法案》的出台，该法案旨在促进国内制造，但也因效率低下而受到批评。

**标签**: `#quantum computing`, `#supply chain`, `#policy`, `#geopolitics`, `#technology strategy`

---

<a id="item-13"></a>
## [大型 AI 实验室为何大量招聘哲学家](https://www.economist.com/science-and-technology/2026/06/24/why-big-ai-labs-are-hiring-so-many-philosophers) ⭐️ 7.0/10

OpenAI、DeepMind 和 Anthropic 等主要 AI 实验室正在大量招聘哲学家，以应对先进 AI 技术带来的复杂伦理和概念挑战，包括对齐问题、意识问题和道德主体性问题。 这一趋势表明，AI 行业认识到纯粹的技术解决方案不足以确保 AI 的安全和有益性，哲学专业知识对于应对 AI 发展带来的深层规范和概念问题至关重要。 AI 实验室中的哲学家致力于解决价值对齐、可解释性、公平性以及智能定义等问题，通常与工程师和研究人员合作，影响 AI 系统的设计和部署。

rss · The Economist · 6月24日 09:44

**背景**: 随着 AI 系统变得更加强大和自主，它们引发了一些根本性问题：它们应该追求什么目标？如何确保它们符合人类价值观？它们可能拥有什么权利或道德地位？这些本质上是哲学问题，超出了技术工程的范畴。哲学家在伦理学、逻辑学和概念分析方面受过训练，这有助于 AI 实验室在潜在问题演变成危机之前预见并解决它们。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ethics_of_artificial_intelligence">Ethics of artificial intelligence - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_general_intelligence">Artificial general intelligence - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#philosophy`, `#AI research`, `#industry trends`, `#technology`

---

<a id="item-14"></a>
## [AI 投资挤压企业预算](https://www.economist.com/podcasts/2026/06/24/ai-is-squeezing-business-budgets) ⭐️ 7.0/10

《经济学人》报道称，AI 投资正在挤压企业预算，迫使企业重新分配资源，优先考虑 AI 项目而非其他支出。 这一趋势凸显了 AI 对企业战略日益增长的经济影响，因为公司必须在 AI 采用与其他运营需求之间取得平衡，可能重塑行业支出模式。 该分析基于《经济学人》的播客摘要，聚焦企业在为 AI 分配预算时面临的权衡，未提供具体财务数据或案例研究。

rss · The Economist · 6月24日 09:00

**背景**: AI 在各行业的采用加速，需要在技术、人才和基础设施上进行大量前期投资。这常常迫使公司削减其他领域的成本，如营销或研发，以资助 AI 项目。

**标签**: `#AI`, `#economics`, `#business strategy`, `#technology trends`

---

<a id="item-15"></a>
## [人机即兴：AI 协作的新范式](https://www.huxiu.com/article/4870041.html?f=rss) ⭐️ 7.0/10

一种新的人机即兴范式被提出，从传统的指令控制协作转向人类与 AI 系统之间的自发、共创互动。这种方法强调实时适应和共同价值创造，而非预定义的工作流程。 这一范式可能改变组织和个体利用 AI 的方式，在动态环境中实现更流畅、更具创造性的问题解决。它挑战了当前以效率为中心的 AI 部署模式，为设计、音乐和商业战略等领域的创新开辟了新可能。 这一概念借鉴了生成式 AI 使用与即兴能力的研究，表明 AI 可以通过技术可供性增强人类的即兴能力。实际案例包括用于共同创作即兴故事的 AI 代理，以及将 AI 视为协作伙伴的音乐即兴系统。

rss · 虎嗅 · 6月24日 22:11

**背景**: 传统的人机协作遵循预定义的规则和工作流程，在不可预测的情况下限制了灵活性。即兴创作是表演艺术中的一个概念，涉及在结构化框架内的自发创造。生成式 AI 的最新进展使机器能够参与实时共创，从简单的响应生成转向协作叙事和音乐创作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://humanmachine.live/">Human_Machine_Improv - Improvised comedy with Artificial Intelligence</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-031-97254-6_22">Being the Artificial Player: Good Practices in Collective Human-Machine ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0166497226000702">Generative AI usage and improvisation capability</a></li>

</ul>
</details>

**标签**: `#AI`, `#human-machine collaboration`, `#value creation`, `#paradigm shift`

---

<a id="item-16"></a>
## [中国的“千帆星座”：星链的新对手？](https://news.google.com/read/CBMiugFBVV95cUxPOWxQME9aVmRRZkpLTHVUV05wWFB6RncwbFhfTVowUDdoWXNfX00taUcza09ZelpMZ2VwajBmZFpZRFJ4S19VSEw1dmNsOHY4NHQzM29uazlsN1R6SEJnOF83OXlMa2dWSmJpLVprMk9OTWItZjhyVTVQWEd0ZVhzemwtdmRpc2oyc3pIRF9uVEVkNGpLY3lMNmk4blF1R1pleEJST1djbEN3Uk5pWGxkSVB1QTUxbEJxbFE?hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 7.0/10

《卫报》发表文章，探讨中国的“千帆星座”（SpaceSail）卫星互联网项目及其与埃隆·马斯克的“星链”竞争的潜力。该项目由国有背景的上海垣信卫星科技有限公司于 2023 年启动，旨在提供全球高速互联网覆盖。 “千帆星座”标志着中国大举进入卫星互联网竞赛，可能挑战“星链”的主导地位并重塑全球连接格局。这场竞争具有重大的地缘政治和技术影响，因为对天基互联网基础设施的控制已成为战略优先事项。 “千帆星座”计划分三个阶段部署多达 14,000 颗低地球轨道卫星，其中 2024 年预计发射 108 颗。该星座是中国规划的三个“万星星座”之一，旨在提供全球宽带服务。

rss · Buzzing China · 6月25日 01:02

**背景**: 卫星互联网星座利用大量低地球轨道卫星网络，为偏远和服务不足的地区提供宽带覆盖。SpaceX 运营的“星链”目前以数千颗在轨卫星领先市场。中国的“千帆星座”项目是一项国有支持的倡议，旨在创建类似的全球网络，反映了天基通信日益增长的战略重要性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qianfan">Qianfan - Wikipedia</a></li>
<li><a href="https://www.theguardian.com/world/2026/jun/25/china-spacesail-rival-elon-musk-starlink-space-satelites-low-earth-orbit">What is China ’s SpaceSail , and could it rival Elon... | The Guardian</a></li>
<li><a href="http://english.scio.gov.cn/in-depth/2024-08/09/content_117358240.htm">China 's new mega-constellation marks milestone in satellite internet</a></li>

</ul>
</details>

**标签**: `#SpaceSail`, `#Starlink`, `#satellite internet`, `#China`, `#technology competition`

---

<a id="item-17"></a>
## [警惕伪装成官方页面的恶意 curl 脚本](https://www.v2ex.com/t/1222709#reply0) ⭐️ 7.0/10

一位开发者在搜索 Claude Code 时，差点执行了一个伪装成 Claude AI 官方页面的恶意 curl 脚本，该脚本包含指向可疑域名的混淆代码。 此事件凸显了一种日益增长的供应链攻击手段：攻击者通过 curl | sh 诱导开发者执行恶意脚本，可能危及系统安全和凭据。 恶意脚本托管在 claude.ai 下的一个分享页面，但实际指向名为 proviewhomeinspections 的域名，并通过对话框要求用户输入密码，从而引起警觉。

rss · V2EX · 6月25日 03:01

**背景**: curl | sh 模式是一种常见的软件安装方式（例如 Rust、Homebrew），通过将脚本直接管道传输到 shell 中执行。然而，这种做法本身存在风险，因为它会在未经验证的情况下执行不可信代码，攻击者可以通过混淆技术隐藏恶意负载以逃避检测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/miaoxworld/OpenClawInstaller/blob/main/install.sh">OpenClawInstaller/install.sh at main - GitHub</a></li>
<li><a href="https://cloud.tencent.com/developer/article/2416244">前端开发者必备 技 能：JS 混 淆 -腾讯云开发者社区-腾讯云</a></li>
<li><a href="https://blog.wangyuchao.cn/posts/f1ee5a16.html">代 码 混 淆 123 | 揽星河</a></li>

</ul>
</details>

**标签**: `#安全`, `#curl`, `#供应链攻击`, `#Claude Code`, `#恶意脚本`

---

<a id="item-18"></a>
## [OpenTag：在 GitHub 和 Slack 中 @ AI 智能体的开源协议](https://www.v2ex.com/t/1222692#reply0) ⭐️ 7.0/10

OpenTag 是一个开源协议，允许用户在 GitHub issue、PR 评论或 Slack 线程中 @ 一个 AI 智能体，该智能体在用户本地仓库中执行任务，并将结果写回原线程。它被设计为 Anthropic 的 Claude Tag 的开放替代方案，支持多种智能体执行器，如 Claude Code、Codex 和自定义 runner。 OpenTag 将 AI 智能体调用工作流与特定模型或平台解耦，使团队能够灵活选择自己喜欢的智能体和通信工具。这解决了当前开发者需要将上下文复制到独立聊天界面才能使用 AI 辅助的关键集成痛点。 该项目目前包含 GitHub 和 Slack 适配器、本地优先执行模型（智能体仅在显式绑定的仓库中运行），以及内置的 echo（冒烟测试）、Claude Code 和 Codex 执行器。它仍处于早期阶段（v0），使用 TypeScript 构建。

rss · V2EX · 6月25日 02:26

**背景**: Claude Tag 是 Anthropic 的一项功能，允许用户在 Slack 中 @Claude 来执行任务并发布结果。但它仅限于 Claude 模型和 Slack，并且需要企业版计划。OpenTag 旨在提供类似的交互，但采用开放协议，可与任何智能体执行器和任何通信平台配合使用，位于 OpenClaw 和 Hermes 等实际执行任务的智能体之上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI)</a></li>
<li><a href="https://www.anthropic.com/news/introducing-claude-tag">Introducing Claude Tag \ Anthropic</a></li>
<li><a href="https://hermes-agent.org/">Hermes Agent — Open-Source AI Agent with Persistent Memory</a></li>

</ul>
</details>

**标签**: `#AI agent`, `#open source`, `#developer tools`, `#workflow automation`, `#GitHub integration`

---