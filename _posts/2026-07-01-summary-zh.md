---
layout: default
title: "Horizon Summary: 2026-07-01 (ZH)"
date: 2026-07-01
lang: zh
---

> 从 267 条内容中筛选出 21 条重要资讯。

---

#### Tech
1. [Anthropic 发布 Claude Sonnet 5，增强自主代理能力](#item-1) ⭐️ 9.0/10 [技术]
8. [华为开源盘古 2.0 模型，505B 参数](#item-8) ⭐️ 9.0/10 [技术]
9. [Claude Code 秘密在请求中嵌入隐写标记](#item-9) ⭐️ 8.0/10 [技术]
10. [Anthropic 推出 Claude Science 数据科学研究工具](#item-10) ⭐️ 8.0/10 [技术]
11. [Kubernetes 被移植到浏览器中用于学习](#item-11) ⭐️ 8.0/10 [技术]
12. [自制毫米波雷达用于材料分类](#item-12) ⭐️ 8.0/10 [技术]
13. [ChatGPT 全球采用率持续增长](#item-13) ⭐️ 8.0/10 [技术]
14. [科技周报：AI、硬件与行业动态](#item-14) ⭐️ 8.0/10 [技术]
17. [美团开源万亿参数大模型 LongCat-2.0](#item-17) ⭐️ 8.0/10 [技术]
18. [腾讯与长鑫存储签署超 200 亿元 DRAM 供应协议](#item-18) ⭐️ 8.0/10 [技术]
20. [Anthropic 获美政府批准，恢复向关键基础设施部署 Mythos 5](#item-20) ⭐️ 8.0/10 [技术]

#### Politics
2. [希望、反弹与美国政治斗争](#item-2) ⭐️ 9.0/10 [时政]
3. [台湾芯片产业影响美国政策](#item-3) ⭐️ 9.0/10 [时政]
4. [美国作为全球榜样的道德权威下降](#item-4) ⭐️ 9.0/10 [时政]
5. [美国众议院中国委员会质询百时美施贵宝和辉瑞临床试验地点](#item-5) ⭐️ 9.0/10 [时政]
6. [阿曼在美伊战争后提议征收霍尔木兹海峡过境费](#item-6) ⭐️ 9.0/10 [时政]
7. [伊朗拒绝马克龙的霍尔木兹海峡计划](#item-7) ⭐️ 9.0/10 [时政]

#### Social Hot Topics
15. [市民自建网站曝光深圳食品安全抽检惊心数据](#item-15) ⭐️ 8.0/10 [社会热点]
16. [Unity 将于 2026 年 6 月关停中国大陆及港澳大部分全球游戏服务](#item-16) ⭐️ 8.0/10 [社会热点]
19. [三大外卖平台达成反内卷共识](#item-19) ⭐️ 8.0/10 [社会热点]

#### 其他 (Other)
21. [麦凯的《大众幻想与群众癫狂》经典回顾](#item-21) ⭐️ 7.0/10 [其他]

---

## Tech

<a id="item-1"></a>
### [Anthropic 发布 Claude Sonnet 5，增强自主代理能力](https://www.anthropic.com/news/claude-sonnet-5) ⭐️ 9.0/10 [技术]

Anthropic 发布了 Claude Sonnet 5，这是一款更快、更具自主代理能力的模型，能够自主规划、使用工具并执行任务，与前代相比在成本效率和速度上均有提升。 此次发布标志着在使高级自主代理 AI 能力更易获取且更具成本效益方面迈出了重要一步，可能加速自主 AI 代理在开发工作流和企业应用中的采用。 根据社区基准测试，Sonnet 5 达到了 GLM-5.2 级别的性能，成本翻倍但速度也翻倍，不过在常识知识、组合工具调用任务和谜题解决方面存在弱点。

hackernews · marinesebastian · 6月30日 17:59 · [社区讨论](https://news.ycombinator.com/item?id=48736605)

**背景**: 自主代理 AI 指的是能够自主运行、设定目标并适应新情况而无需持续人工干预的 AI 系统。与需要为每一步提供明确指令的传统 AI 模型不同，像 Claude Sonnet 5 这样的自主代理模型可以规划、使用浏览器和终端等工具，并独立执行多步骤任务。此次发布基于 Anthropic 的 Claude 模型系列，Sonnet 定位为速度和能力之间的平衡选项。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/agentic-ai">What is Agentic AI? | IBM</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-ai">What is agentic AI? Definition and differentiators | Google Cloud</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些用户质疑 Sonnet 5 在较高努力级别下与 Opus 相比的成本效益，而其他用户报告了基准测试结果，显示其在常识和工具调用方面存在特定弱点。一位用户担心针对完全自主代理开发的优化可能会降低其他领域的性能，另一位用户报告称在实际实验中 Sonnet 子代理浪费了 tokens。

**标签**: `#AI`, `#Claude`, `#Anthropic`, `#machine learning`, `#agentic AI`

---

<a id="item-8"></a>
### [华为开源盘古 2.0 模型，505B 参数](https://t.me/zaihuapd/42259) ⭐️ 9.0/10 [技术]

在 2026 年华为开发者大会上，华为宣布开源盘古 2.0 模型，包含 505B 参数的 Pro 版和 92B 参数的 Flash 版，支持 512K token 上下文窗口。公司计划从 6 月 30 日起陆续开源七大组件。 此次发布标志着华为在开源大语言模型领域的重大进展，有望挑战 GPT-4 和 LLaMA 等全球领先模型。505B 参数规模和 512K 上下文长度使盘古 2.0 成为在中外 AI 生态中具有竞争力的基础模型。 该模型针对华为昇腾 AI 处理器和鸿蒙系统进行了优化，开源组件包括预训练代码、推理代码和模型权重。余承东指出，虽然华为的算力大量支持了国内其他企业需求，但公司仍致力于引领 AI 模型领域。

telegram · zaihuapd · 6月30日 06:01

**背景**: 大语言模型（LLM）是在海量文本数据上训练的人工智能系统，能够生成类似人类的文本。上下文长度指模型单次前向传递能处理的最大 token 数（词或子词）；512K 上下文可处理极长文档或对话。华为的昇腾 AI 处理器是自研的 AI 芯片，公司早在全球 AI 热潮之前就开始开发盘古模型系列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/huaweis-homegrown-ai-chip-examined-chinese-fab-smic-produced-ascend-910b-is-massively-different-from-the-tsmc-produced-ascend-910">Huawei's homegrown AI chip examined — Chinese fab SMIC-produced Ascend 910B is massively different from the TSMC-produced Ascend 910 | Tom's Hardware</a></li>
<li><a href="https://datanorth.ai/blog/context-length">Context Length in LLMs: What Is It and Why It Is Important?</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#AI`, `#Pangu`, `#open-source`, `#large language model`

---

<a id="item-9"></a>
### [Claude Code 秘密在请求中嵌入隐写标记](https://thereallo.dev/blog/claude-code-prompt-steganography) ⭐️ 8.0/10 [技术]

Anthropic 的开发者工具 Claude Code 被发现会在 API 请求中嵌入隐写标记，用于检测未经授权的使用（例如中国企业的模型蒸馏行为）。这些标记以未向用户披露的方式隐藏，引发了透明度方面的担忧。 这种做法通过秘密修改用户流量且未明确披露，破坏了用户对 AI 开发者工具的信任，可能违反用户对透明度和控制权的期望。它还凸显了公司保护模型的需求与开发者了解其机器上运行的软件实际行为的权利之间的更广泛矛盾。 这些隐写标记以不易被随意检查发现的方式嵌入请求负载中，但已被社区逆向工程破解。标记设计为能够通过自定义 API 网关传输，使其难以在不被察觉的情况下被剥离。

hackernews · kirushik · 6月30日 15:44 · [社区讨论](https://news.ycombinator.com/item?id=48734373)

**背景**: 隐写术是一种将秘密信息隐藏在另一个非秘密信息或媒介（如图像或文本文件）中的做法，使得隐藏信息不易被未察觉的观察者发现。在 AI 领域，隐写水印有时被用于在 AI 生成的内容中嵌入不可见信号，以追踪其来源或检测滥用行为。Claude Code 是 Anthropic 的命令行开发者工具，与他们的 Claude AI 模型集成，用于辅助编码任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Steganography">Steganography</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_content_watermarking">AI content watermarking - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_watermarking">Digital watermarking - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论存在分歧：一些人批评 Anthropic 缺乏透明度且行为不光明，而另一些人则认为其意图（防止中国企业的模型蒸馏）是明确的，且反对声音被夸大了。一些评论者指出，该实现方式很粗糙，本可以更巧妙地避免检测，而另一些人则指出，像 Codex CLI 这样的开源替代品不太可能采取此类做法。

**标签**: `#steganography`, `#Claude Code`, `#AI ethics`, `#reverse engineering`, `#transparency`

---

<a id="item-10"></a>
### [Anthropic 推出 Claude Science 数据科学研究工具](https://claude.com/product/claude-science) ⭐️ 8.0/10 [技术]

Anthropic 推出了 Claude Science，这是一个面向科学研究的 AI 工作台，集成了本地服务器和数据库连接，能够进行数据分析并生成可审计的工件。 此次发布标志着将大语言模型应用于专业科学工作流程的重要一步，可能加速药物发现和分子建模等领域的研究。同时，它也引发了关于大语言模型在高风险数据分析中产生幻觉风险的重要讨论。 Claude Science 运行一个本地服务器，通过基于 Web 的 UI 连接，允许安全地连接到机构数据库和计算集群。它生成可审计的工件，追踪分析的每一步，有助于缓解幻觉问题。

hackernews · lebovic · 6月30日 17:07 · [社区讨论](https://news.ycombinator.com/item?id=48735770)

**背景**: 像驱动 Claude 的大语言模型可能会生成听起来合理但事实上不正确的信息，这被称为幻觉。在准确性至关重要的科学研究中部署 AI 时，这是一个关键挑战。Claude Science 旨在通过提供透明、可追踪的分析流程并与可信数据源集成来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-science-ai-workbench">Claude Science, an AI workbench for scientists, is now available</a></li>
<li><a href="https://claude.com/product/claude-science">Claude Science beta | Claude by Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/LLM_hallucination">LLM hallucination</a></li>

</ul>
</details>

**社区讨论**: 社区评论既表达了热情也提出了质疑。一位用户指出，类似工具经常编造数据并伪造数据库连接，质疑 Claude Science 如何防范这一点。另一位构建了相关工具的用户强调了与机构集群集成的价值。第三位用户指出了本地服务器和 Web UI 的架构，认为它适合严格管控的制药环境。总体而言，讨论集中在幻觉风险和工具的实际效用上。

**标签**: `#Claude Science`, `#Anthropic`, `#AI`, `#data science`, `#LLM`

---

<a id="item-11"></a>
### [Kubernetes 被移植到浏览器中用于学习](https://ngrok.com/blog/i-ported-kubernetes-to-the-browser) ⭐️ 8.0/10 [技术]

ngrok 的一位开发者创建了名为 'webernetes' 的项目，将 Kubernetes 完全移植到浏览器中运行，用户无需任何本地安装即可与模拟的 Kubernetes 集群进行交互。 该项目通过消除环境配置障碍，让 Kubernetes 教育变得更加普及；任何拥有浏览器的人都可以实验集群概念和 kubectl 命令，从而加速容器编排的学习和采用。 基于浏览器的集群使用自定义时钟机制来模拟时间推进，并且不在浏览器中运行实际容器；相反，它提供了 Kubernetes 资源和行为的概念性模拟。

hackernews · peterdemin · 6月30日 20:48 · [社区讨论](https://news.ycombinator.com/item?id=48738985)

**背景**: Kubernetes 是一个开源容器编排平台，用于自动化容器化应用的部署、扩展和管理。Ngrok 是一种隧道服务，可将本地服务器安全地暴露到互联网上。'Wbernetes' 利用 ngrok 的基础设施，直接在浏览器中提供交互式 Kubernetes 学习环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kubernetes">Kubernetes - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ngrok">Ngrok</a></li>
<li><a href="https://ngrok.com/">ngrok: deliver your apps, APIs, and AI on local and prod</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍称赞该项目具有创新性，对概念教育很有用，有人称其为“即时经典”。一些人质疑它是否真的在浏览器中运行容器，指出它模拟而非执行真实工作负载。其他人则强调了在模拟 Kubernetes 环境中测试 AI 生成代码的价值。

**标签**: `#kubernetes`, `#browser`, `#education`, `#ngrok`, `#webernetes`

---

<a id="item-12"></a>
### [自制毫米波雷达用于材料分类](https://gauthier-lechevalier.com/radar) ⭐️ 8.0/10 [技术]

一位开发者构建了一个概念验证的毫米波雷达系统，通过分析反射信号来分类材料，并发布了详细的技术文章，包括设计选择、测试结果以及从失败中吸取的教训。 该项目表明低成本毫米波雷达有望实现非破坏性材料识别，例如建筑物中的石棉检测，而社区讨论既肯定了其潜力，也指出了仍存在的重大技术挑战。 该雷达很可能工作在 60–77 GHz 频段，利用信号处理根据介电特性区分材料；作者坦诚分享了失败经验，例如灵敏度限制以及难以区分相似材料。

hackernews · GL26 · 6月30日 17:29 · [社区讨论](https://news.ycombinator.com/item?id=48736137)

**背景**: 毫米波雷达使用毫米波长的电磁波（30–300 GHz）来探测物体并测量其特性。利用雷达进行材料分类依赖于反射率、介电常数和散射行为的差异。此前的研究已探索使用 60 GHz 和 77 GHz 雷达单元进行材料识别，但实际部署仍面临灵敏度、几何依赖性以及真实环境变化等挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mmwave_sensing">mmWave sensing - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2202.05169">[2202.05169] Radar-based Materials Classification Using Deep Wavelet Scattering Transform: A Comparison of Centimeter vs. Millimeter Wave Units</a></li>
<li><a href="https://community.infineon.com/gfawx74859/attachments/gfawx74859/Radarsensor/3615/1/radar+material+classification.pdf?nobounce">Material Classification using 60-GHz Radar and Deep ...</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该项目的教育价值和对失败的坦诚记录，但有人质疑该系统能否在相关浓度下可靠检测石棉，指出概念验证仅测试了常见材料。其他人则提出了替代应用，例如检测材料中的不连续性用于工业检测或医学成像。

**标签**: `#mmWave`, `#radar`, `#material classification`, `#asbestos detection`, `#hardware`, `#DIY`

---

<a id="item-13"></a>
### [ChatGPT 全球采用率持续增长](https://openai.com/index/how-chatgpt-adoption-has-expanded) ⭐️ 8.0/10 [技术]

OpenAI 发布了新的 Signals 数据，显示 ChatGPT 的全球采用率正在增长，用户在不同地区和语言中增加了使用频率并探索更多功能。 这表明 ChatGPT 正成为全球用户更重要的工具，可能加速人工智能融入日常工作和跨文化交流。 该数据来自追踪使用模式的 OpenAI Signals，突出了用户参与度和所使用功能范围的增长。

rss · OpenAI Blog · 6月30日 09:00

**背景**: ChatGPT 是 OpenAI 开发的对话式 AI 模型，能够根据提示生成类似人类的文本。自 2022 年底推出以来，它在教育、商业等多个领域迅速普及。

**标签**: `#ChatGPT`, `#AI adoption`, `#OpenAI`, `#global growth`

---

<a id="item-14"></a>
### [科技周报：AI、硬件与行业动态](https://www.v2ex.com/t/1224077#reply0) ⭐️ 8.0/10 [技术]

第 190 期《偷懒爱好者周刊》（2026 年 7 月 1 日）总结了 6 月最后一周的重大科技事件，包括 OpenAI 首款自研 AI 芯片、字节跳动的 Seedance 2.5 视频生成模型，以及全球最快超算“灵晟”达到 2.19 百亿亿次浮点运算。 这份周报汇集了 AI、硬件和能源领域的多项高影响力进展，反映了全球科技行业创新与竞争加速的趋势。读者可以快速了解可能影响市场的趋势，从 AI 芯片自给自足到超算领先地位。 值得注意的事件包括 SpaceX 与 Reflection AI 签署 63 亿美元算力协议、高通计划以约 40 亿美元收购 AI 芯片初创公司 Modular，以及苹果大幅上调全系产品价格。周刊还分享了三个有趣网站、三个实用工具和三个收藏资源。

rss · V2EX · 6月30日 23:44

**背景**: 《偷懒爱好者周刊》是一份面向普通科技爱好者的中文新闻通讯，精选科技新闻、工具和资源。本期内容涵盖从 AI 模型发布（如字节跳动的 Seedance 2.5、OpenAI 的 GPT-5.6）到硬件里程碑（如 5 兆瓦超级电容、灵晟超算）以及行业动态（如甲骨文裁员、阿里巴巴起诉美国国防部）的广泛话题。

**标签**: `#AI`, `#hardware`, `#weekly roundup`, `#OpenAI`, `#SpaceX`, `#ByteDance`, `#supercomputer`

---

<a id="item-17"></a>
### [美团开源万亿参数大模型 LongCat-2.0](https://www.donews.com/news/detail/1/6614732.html) ⭐️ 8.0/10 [技术]

美团发布了 LongCat-2.0，这是一个开源的大语言模型，拥有超过一万亿参数，支持 100 万 token 的上下文窗口，并完全使用国产芯片在万卡集群上完成训练。 这标志着中国 AI 生态的重大突破，证明了国产芯片能够训练最先进的万亿参数模型，减少对外国硬件的依赖。该模型在代码和 Agent 任务上的性能超越了领先的闭源模型，可能加速开源 AI 的发展。 LongCat-2.0 支持 100 万 token 的上下文，能够处理极长的文档或对话。它是在国产万卡集群上训练的，凸显了中国在大规模 AI 基础设施方面的进展。

rss · DoNews · 6月30日 03:38

**背景**: 拥有万亿参数的大语言模型需要巨大的计算资源和先进硬件，通常来自 NVIDIA 等公司。上下文窗口决定了模型一次能考虑多少文本；100 万 token 非常庞大。开源模型允许更广泛的访问和社区改进，而国产芯片训练则降低了地缘政治风险。

**标签**: `#大模型`, `#美团`, `#开源`, `#国产芯片`, `#万亿参数`

---

<a id="item-18"></a>
### [腾讯与长鑫存储签署超 200 亿元 DRAM 供应协议](https://www.donews.com/news/detail/1/6614347.html) ⭐️ 8.0/10 [技术]

据报道，腾讯已与长鑫存储（CXMT）签署了一份价值超过 200 亿元人民币（约 28 亿美元）的长期 DRAM 供应协议，期限为 3 至 5 年。该协议可能还包括高带宽内存（HBM），并且长鑫存储正在与其他互联网公司洽谈类似合作。 该协议意义重大，因为它为腾讯的人工智能和云基础设施确保了稳定的 DRAM 供应，同时为长鑫存储在潜在 IPO 前提供了重要客户。这也凸显了中国在地缘政治紧张局势下推动建立自主内存芯片供应链的努力。 该协议据报道价值超过 200 亿元人民币，期限为 3 至 5 年。可能包括 HBM（一种用于 AI 加速器的关键组件），并且长鑫存储正在积极寻求与其他中国互联网公司达成类似协议。

rss · DoNews · 6月30日 00:57

**背景**: 长鑫存储（CXMT）是中国领先的 DRAM 制造商，专注于生产用于服务器和 AI 硬件等各种应用的内存芯片。DRAM 是一种易失性内存，用于计算机和服务器的临时数据存储，而 HBM 是一种用于 AI 加速器的高性能变体。腾讯作为主要的云和 AI 公司，其数据中心需要大量内存芯片。

**标签**: `#semiconductor`, `#DRAM`, `#HBM`, `#Tencent`, `#ChangXin Memory`, `#supply chain`, `#AI hardware`

---

<a id="item-20"></a>
### [Anthropic 获美政府批准，恢复向关键基础设施部署 Mythos 5](https://t.me/zaihuapd/42260) ⭐️ 8.0/10 [技术]

6 月 27 日，美国政府通知 Anthropic，其最强的网络安全模型 Mythos 5 可重新部署给运营和守卫美国关键基础设施的组织。自 6 月 12 日起，Anthropic 一直与政府合作，推动恢复 Mythos 5 和 Fable 5 两款模型的访问权限。 这一批准标志着 AI 治理与国家安全合作的重要一步，展示了先进 AI 模型如何安全地用于关键防御领域。它为政府监督敏感领域中的强大 AI 系统树立了先例。 目前仅 Mythos 5 获准重新部署，Fable 5 模型仍在协商中。Anthropic 正在迅速为获批组织恢复访问，同时继续与政府协商，争取扩大 Mythos 5 的适用范围。

telegram · zaihuapd · 6月30日 07:04

**背景**: Mythos 5 是 Anthropic 最强的网络安全 AI 模型，旨在帮助防御关键基础设施免受网络威胁。该模型此前已部署，但访问权限因政府审查而暂停。此次合作反映了政府对监管和利用先进 AI 以维护国家安全的日益关注。

**标签**: `#Anthropic`, `#Mythos 5`, `#AI deployment`, `#critical infrastructure`, `#US government`, `#cybersecurity`

---

## Politics

<a id="item-2"></a>
### [希望、反弹与美国政治斗争](https://www.economist.com/essay/2026/06/30/hope-backlash-and-the-battle-for-america) ⭐️ 9.0/10 [时政]

《经济学人》发表了一篇分析文章，探讨希望与反弹这两种力量如何塑造美国当前的政治斗争，可能涉及选举动态和社会分裂。 这篇分析提供了关于驱动美国政治的意识形态和情感潮流的高层视角，帮助读者理解可能影响未来选举和政策方向的深层紧张关系。 该文章是《经济学人》对美国政治持续报道的一部分，可能借鉴历史模式和近期事件来构建希望与反弹的叙事框架。

rss · The Economist · 6月30日 20:44

**背景**: 近几十年来，美国政治日益两极分化，进步与抵抗的叙事相互竞争。'反弹'通常指对社会或文化变革的政治反应，而'希望'则代表对改革或团结的渴望。这篇文章似乎探讨了这两种对立力量在当前政治格局中如何相互作用。

**标签**: `#politics`, `#America`, `#election`, `#backlash`, `#hope`

---

<a id="item-3"></a>
### [台湾芯片产业影响美国政策](https://www.economist.com/international/2026/06/30/allies-learn-how-to-bully-america) ⭐️ 9.0/10 [时政]

《经济学人》分析指出，台湾可能通过其由台积电主导的半导体产业，利用芯片制造能力影响未来特朗普政府的美国政策。 这之所以重要，是因为台积电控制着全球约 70%的半导体代工市场，成为苹果、英伟达和高通等美国公司所需先进芯片供应链的关键瓶颈。任何中断都可能带来严重的经济和地缘政治后果。 分析指出，台湾 2022 年集成电路出口额达 1840 亿美元，占其 GDP 的近 25%，台积电约占台湾证券交易所主要指数的 30%。美国一直试图通过《芯片法案》等措施实现芯片生产多元化，但台湾的主导地位依然稳固。

rss · The Economist · 6月30日 20:31

**背景**: 台积电成立于 1987 年，是全球最大的专业半导体代工厂，为苹果、英伟达和 AMD 等主要客户生产芯片。它在代工市场占据主导地位，全球份额约 70%。其 3 纳米和 5 纳米等先进制程对人工智能和高性能计算至关重要。台湾的地缘政治局势增加了复杂性，中国宣称对该岛拥有主权，使得台积电的角色成为一项战略资产。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TSMC">TSMC</a></li>
<li><a href="https://www.csis.org/analysis/mapping-semiconductor-supply-chain-critical-role-indo-pacific-region">Mapping the Semiconductor Supply Chain: The Critical Role of the Indo-Pacific Region | CSIS</a></li>

</ul>
</details>

**标签**: `#Taiwan`, `#chipmaking`, `#geopolitics`, `#US-China relations`, `#Donald Trump`

---

<a id="item-4"></a>
### [美国作为全球榜样的道德权威下降](https://www.economist.com/essay/2026/06/30/what-remains-of-the-city-upon-the-hill) ⭐️ 9.0/10 [时政]

历史学家迈克尔·贝施洛斯在《经济学人》的一篇新文章中提出，美国因背弃其建国原则，已无法再作为全球榜样。 一位著名历史学家在主流媒体上的这一反思，标志着对美国全球角色的看法发生了重大转变，可能影响国际信任和联盟关系。 文章标题引用了约翰·温思罗普的‘山巅之城’比喻，这一比喻长期以来象征着美国成为世界道德灯塔的抱负。

rss · The Economist · 6月30日 13:07

**背景**: ‘山巅之城’这一说法源自清教徒领袖约翰·温思罗普在 1630 年的一次布道，他设想马萨诸塞湾殖民地成为一个模范的基督教社区。几个世纪以来，这一理念演变为美国例外论的核心部分——即美国有独特的使命来领导和激励其他国家。文章认为，近期的行动和政策已经侵蚀了这种道德权威。

**标签**: `#America`, `#founding principles`, `#global leadership`, `#political analysis`, `#The Economist`

---

<a id="item-5"></a>
### [美国众议院中国委员会质询百时美施贵宝和辉瑞临床试验地点](https://news.google.com/read/CBMimAFBVV95cUxQbnJ6LUx3V1lrNlFZSmRqMUFjTVJLMkxTU3VsdTRJeDlrYkt1NFVveWJxTGFtT28yT3lOTmlUWVpKTTFzeEJRanl0VkxwYVFwYjF2azJ2cExyNVNBTElIcnBhdE51Q1p0Y041N1NoTDhXcmhmaVplUVIyakFiZ1c2OG80Q2VqU01ZV0NORk9uenpsMDl0R2sxUA?hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

美国众议院中国问题特别委员会已向百时美施贵宝和辉瑞发出信函，质询其在中国使用临床试验地点的情况。这标志着国会对制药公司与中国关系的审查进一步升级。 此次调查表明，华盛顿两党对美国制药公司在中国进行临床试验可能带来的国家安全风险日益担忧。这可能会重塑药企管理全球试验运营的方式，并增加合规成本。 该委员会正在特别审查这些试验的患者数据是否可能被中国政府获取，以及试验地点是否对知识产权构成风险。百时美施贵宝和辉瑞尚未公开回应此次质询。

rss · Buzzing China · 6月30日 10:00

**背景**: 美国众议院中国问题特别委员会旨在调查中国对美国国家安全和经济利益构成的威胁。由于成本较低且患者群体庞大，在中国进行临床试验已成为全球药物开发的常见做法，但美中在数据安全和技术转让方面的紧张局势使这一做法受到越来越多的审查。

**标签**: `#US-China relations`, `#pharmaceutical industry`, `#congressional investigation`, `#clinical trials`, `#national security`

---

<a id="item-6"></a>
### [阿曼在美伊战争后提议征收霍尔木兹海峡过境费](https://news.google.com/rss/articles/CBMimgFBVV95cUxQWU5DMS1mNG9RNm8yTTkzclFNMWVNRmtCNmI0M1kxdEF4RkdrTlJBV1lCeTFpUGVFcDVRRzdoSDZBYkJYbWRKaEJOWTBwREZUS3ZEMFlCYWU3N2F3eGREWHJBM0l4Q09lLWItS3VvenpzUjlJbTAyc0pzNi1zaVNKS1FwTTF3MUkxX2FTX1k0LUcyTm4xMkxscmd3?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

据报道，阿曼在美伊战争结束后提出了一项计划，拟对通过霍尔木兹海峡的船只征收过境费。 霍尔木兹海峡是全球石油运输的关键咽喉，任何新的收费制度都可能对国际能源市场、航运成本和地区地缘政治稳定产生重大影响。 该提议据称是在美伊战争后提出的，但具体细节如费用金额、实施时间表和法律依据尚未披露。

rss · Buzzing News · 6月30日 16:11

**背景**: 霍尔木兹海峡连接波斯湾与阿曼湾及阿拉伯海，全球约 20%的石油经此运输。阿曼位于海峡入口，历史上在地区冲突中保持中立立场。征收过境费将是一种新颖的机制，因为该水道传统上受国际海洋法和航行自由原则管辖。

**标签**: `#US-Iran war`, `#Oman`, `#Strait of Hormuz`, `#geopolitics`, `#oil transit`, `#international relations`

---

<a id="item-7"></a>
### [伊朗拒绝马克龙的霍尔木兹海峡计划](https://news.google.com/rss/articles/CBMikAFBVV95cUxQb2p2djNjY0JQWEFJd3pmRGNkdXlMU1lWRzZsdnpNS0lveUZkTXMtSVpySmtKOFQ2NjZmaXNodWxHcjNlY2dINTROcnQ3elVCbUoyMkc0TTdEWGhjWm4wNEwycm54ZnllVkhSSEt2NHlYeVpxVTFMN1RVV0ZNcVJWVUNLZWNkeG5RSDh0M293dUs?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

伊朗正式拒绝了法国总统埃马纽埃尔·马克龙提出的确保霍尔木兹海峡安全通行的外交计划，该海峡是全球关键的石油咽喉要道。 这一拒绝加剧了地区紧张局势，并威胁全球能源安全，因为霍尔木兹海峡承载着全球约 20%的石油运输量。 据报道，该计划旨在缓和伊朗与西方国家之间因油轮扣押和海峡军事对峙而引发的近期冲突。

rss · Buzzing News · 6月30日 15:38

**背景**: 霍尔木兹海峡是位于伊朗和阿曼之间的一条狭窄水道，连接波斯湾与阿曼湾及阿拉伯海。它是油轮的重要运输路线，任何中断都可能导致全球油价大幅波动。伊朗此前曾威胁要封锁该海峡，以回应制裁或军事压力。

**标签**: `#Iran`, `#Macron`, `#Strait of Hormuz`, `#geopolitics`, `#oil`

---

## Social Hot Topics

<a id="item-15"></a>
### [市民自建网站曝光深圳食品安全抽检惊心数据](https://www.v2ex.com/t/1224047#reply5) ⭐️ 8.0/10 [社会热点]

一位市民自建网站，爬取了深圳三年来的食品安全抽检数据，显示食荚豌豆（合格率 60%）、草虾（69.7%）等生鲜食材合格率极低。该网站还提供了高危食材排名和日常避坑建议。 这个数据驱动的公益项目直接揭示了深圳生鲜供应链中系统性的食品安全风险，影响消费者行为和公共健康。它为市民提供了可操作的采购建议，并凸显了加强监管的必要性。 数据仅覆盖某生鲜平台在售商品，每项食材检测次数不少于 5 次。抽检量最大的高危蔬菜是豇豆（676 次，合格率 81.7%），荔枝、番木瓜等热带水果存在保鲜药剂残留问题，水产则常检出兽药/抗生素残留。

rss · V2EX · 6月30日 14:33

**背景**: 中国的食品安全抽检由监管部门对农产品进行农药残留、兽药和污染物检测。通常合格率较高，但部分品类问题突出。这个市民项目利用某生鲜电商平台内部抽检报表，制作了透明排名，填补了消费者认知的空白。

**标签**: `#food safety`, `#Shenzhen`, `#public health`, `#data visualization`, `#consumer protection`

---

<a id="item-16"></a>
### [Unity 将于 2026 年 6 月关停中国大陆及港澳大部分全球游戏服务](https://www.donews.com/news/detail/3/6614978.html) ⭐️ 8.0/10 [社会热点]

Unity 宣布自 2026 年 6 月 30 日起，将关停中国大陆及港澳地区的大部分全球游戏服务，仅保留广告、应用内购买和身份认证，并提供本地化替代方案。 这一重大业务调整直接影响该地区大量游戏开发者和相关行业，可能重塑本地游戏开发生态，迫使开发者迁移到替代平台或服务。 保留的服务包括广告、应用内购买和身份认证，同时公司将提供本地化替代方案来取代关停的服务。关停服务的具体范围以及本地替代方案的具体内容尚未完全公布。

rss · DoNews · 6月30日 06:25

**背景**: Unity 是一个广泛使用的跨平台游戏引擎，提供包括分析、云构建和多人网络在内的一系列服务。由于监管和市场环境的变化，该公司一直在调整其在中国的业务战略，此举似乎是更广泛本地化努力的一部分。

**标签**: `#Unity`, `#游戏服务`, `#关停`, `#中国大陆`, `#港澳地区`, `#游戏行业`

---

<a id="item-19"></a>
### [三大外卖平台达成反内卷共识](https://www.donews.com/news/detail/1/6614336.html) ⭐️ 8.0/10 [社会热点]

在北京市场监管部门的协调下，美团、京东和淘宝闪购达成五点共识，停止分钟级配送竞速，推动理性营销、规范配送和商家扶持。 这标志着竞争平台之间罕见的政府调解合作，以遏制平台经济中的‘内卷’，可能降低运营成本并改善对消费者和商家的服务质量。 共识涵盖五个方面：停止分钟级速度竞争、采取理性促销策略、规范配送行为、加大商家扶持力度，以及在北京市场监管下建立长期协调机制。

rss · DoNews · 6月30日 00:52

**背景**: 近年来，中国主要外卖平台陷入激烈的‘分钟级竞速’——竞相以最短时间送达订单，往往以骑手安全和运营成本为代价。这种现象被称为‘内卷’，因助长不健康竞争和资源浪费而受到批评。北京市场监管部门现推出平台经济领域首个‘破卷向善’协商机制，引导平台走向可持续发展。

**标签**: `#外卖平台`, `#市场监管`, `#行业共识`, `#反内卷`, `#理性促销`

---

## 其他 (Other)

<a id="item-21"></a>
### [麦凯的《大众幻想与群众癫狂》经典回顾](https://www.gutenberg.org/ebooks/24518) ⭐️ 7.0/10 [其他]

查尔斯·麦凯 1852 年出版的《非同寻常的大众幻想与群众性癫狂》一书在 Hacker News 上被重新讨论，引发了关于其历史准确性以及对群体心理和金融泡沫的持久见解的讨论。 这本书仍然是理解群体心理和金融狂热的基石，而关于其事实准确性的持续辩论凸显了批判性审视那些塑造现代经济思想的历史叙述的重要性。 麦凯的书著名地描述了郁金香狂热、南海泡沫等幻想，但后来的研究表明郁金香泡沫的故事被夸大了，缺乏广泛经济影响的证据。

hackernews · lstodd · 6月30日 12:47 · [社区讨论](https://news.ycombinator.com/item?id=48731989)

**背景**: 查尔斯·麦凯的著作是一部关于群体行为和非理性行为的故事集，涵盖从南海泡沫到十字军东征和预言等内容。尽管广受欢迎，但其可靠性受到现代历史学家的质疑，他们指出书中存在修饰和缺乏原始资料的问题。

**社区讨论**: 评论者表达了不同的观点：一些人认为这本书有趣且富有洞察力，而另一些人则警告说它夸大了郁金香狂热等事件。几位评论者推荐了更严谨的学术著作，如 Quinn 和 Turner 的《繁荣与萧条》。

**标签**: `#crowd psychology`, `#financial bubbles`, `#history`, `#book review`, `#behavioral economics`

---