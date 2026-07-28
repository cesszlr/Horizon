---
layout: default
title: "Horizon Summary: 2026-07-28 (ZH)"
date: 2026-07-28
lang: zh
---

> 从 268 条内容中筛选出 20 条重要资讯。

---

#### Tech
7. [月之暗面开源 2.8 万亿参数 Kimi K3 模型](#item-7) ⭐️ 9.0/10 [技术]
9. [谷歌透露 Gemini 4 为迄今最雄心预训练项目，预计年底发布](#item-9) ⭐️ 9.0/10 [技术]
10. [Anthropic 阐明对开放权重模型的立场](#item-10) ⭐️ 8.0/10 [技术]
11. [研究人员利用漏洞完全控制沃尔沃/埃契尔车队平台](#item-11) ⭐️ 8.0/10 [技术]
12. [Libsm64：超级马里奥 64 角色可嵌入其他游戏引擎](#item-12) ⭐️ 8.0/10 [技术]
14. [AI 算力需求推动核聚变与 SMR 投资热潮](#item-14) ⭐️ 8.0/10 [技术]
15. [长鑫科技科创板首日暴涨 471.59%](#item-15) ⭐️ 8.0/10 [技术]
16. [Fastjson 1.x 高危 RCE 漏洞无需 Gadget 或 AutoType](#item-16) ⭐️ 8.0/10 [技术]
17. [中芯国际测试中国首台国产 DUV 光刻机](#item-17) ⭐️ 8.0/10 [技术]
18. [Python-build-standalone：便携式 Python 发行版指南](#item-18) ⭐️ 7.0/10 [技术]
20. [ccteam：管理 50+并行 AI 编码代理的开源工具](#item-20) ⭐️ 7.0/10 [技术]

#### Politics
1. [巴西总统大选：特朗普、关税与中国关系成焦点](#item-1) ⭐️ 9.0/10 [时政]
2. [乌克兰四年来最高平民伤亡，儿童遇难](#item-2) ⭐️ 9.0/10 [时政]
3. [特朗普因库存警告暂停对伊战争](#item-3) ⭐️ 9.0/10 [时政]
4. [特朗普警告：若伊朗谈判失败将采取强力军事行动](#item-4) ⭐️ 9.0/10 [时政]
5. [最高法院支持特朗普后，为数千人保留 TPS 的斗争](#item-5) ⭐️ 9.0/10 [时政]
6. [特朗普叫停空袭后，伊朗称仍控制海峡且无意谈判](#item-6) ⭐️ 9.0/10 [时政]

#### Social Hot Topics
8. [美素佳儿奶粉被曝铅超标 9 倍，公司配合调查](#item-8) ⭐️ 9.0/10 [社会热点]
13. [长鑫市值 3.6 万亿：高点还是起点？](#item-13) ⭐️ 8.0/10 [社会热点]
19. [OpenAI 网站在中国可访问，V2EX 用户热议](#item-19) ⭐️ 7.0/10 [社会热点]

---

## Tech

<a id="item-7"></a>
### [月之暗面开源 2.8 万亿参数 Kimi K3 模型](https://www.donews.com/news/detail/1/6648548.html) ⭐️ 9.0/10 [技术]

月之暗面（Moonshot AI）开源了 Kimi K3 模型，该模型拥有 2.8 万亿参数，采用混合专家（MoE）架构，支持 100 万 token 上下文窗口和原生视觉理解，性能达到开源模型前沿水平。 此次发布标志着中国公司首次开源达到 3 万亿参数级别的模型，推动了开源 AI 的前沿，并在长上下文处理和智能体能力方面展示了显著进步。 Kimi K3 引入了两项新颖的架构创新：Kimi Delta Attention（KDA），一种线性注意力机制，在长上下文下解码速度提升超过 6 倍；以及 Attention Residuals（AttnRes），一种可替代标准残差连接的模块，提高了训练效率。

rss · DoNews · 7月27日 20:15

**背景**: 大型语言模型通常使用 Transformer 架构，其注意力机制的计算复杂度随序列长度呈二次方增长，导致长上下文处理成本高昂。Kimi Delta Attention 是一种线性注意力变体，降低了这种复杂度；而 Attention Residuals 允许每一层通过基于深度的学习注意力机制，有选择地聚合来自之前层的信息，从而改善梯度流动和模型深度扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.26692">[2510.26692] Kimi Linear: An Expressive, Efficient Attention ... GitHub - MoonshotAI/Kimi-Linear GitHub - hwilner/kimi-delta-attention: Educational ... KDA (Kimi Delta Attention) | fla-org/flash-linear-attention ... Kimi-Linear A arXiv:2510.26692v2 [cs.CL] 1 Nov 2025 Kimi K3 Technical Advancements Explained - nextbigfuture.com</a></li>
<li><a href="https://github.com/MoonshotAI/Attention-Residuals">GitHub - MoonshotAI/Attention-Residuals</a></li>
<li><a href="https://digg.com/tech/hm2wuequ">Moonshot AI's Kimi-K3 tops Frontend Code Arena · Digg</a></li>

</ul>
</details>

**标签**: `#AI`, `#open source`, `#Kimi K3`, `#large language model`, `#MoE`

---

<a id="item-9"></a>
### [谷歌透露 Gemini 4 为迄今最雄心预训练项目，预计年底发布](https://9to5google.com/2026/07/26/google-gemini-4-teases/) ⭐️ 9.0/10 [技术]

谷歌 CEO Sundar Pichai 在 Alphabet 2026 年第二季度财报电话会议上宣布，下一代大语言模型 Gemini 4 已投入训练。他称这是谷歌迄今为止最具雄心的预训练项目，预计于 2026 年 11 月或 12 月发布。 Gemini 4 代表了谷歌在 AI 开发中的下一步重大举措，旨在突破基础模型的能力边界。其发布可能显著影响 AI 竞争格局，尤其是在通往通用人工智能（AGI）的竞赛中。 Pichai 强调谷歌将优先将算力分配给前沿 AGI 研发，以确保 Gemini 4 发布时仍处于行业前沿。此外，Gemini 3.x Flash 系列将保持几乎每月一次的迭代频率，重点提升智能编码等能力。

telegram · zaihuapd · 7月27日 04:06

**背景**: AI 预训练是构建大语言模型（LLM）的第一阶段，也是资源消耗最大的阶段，模型从海量无标签数据中学习，以发展对语言和知识的广泛理解。基础模型（如 Gemini 4）是在多样化数据上训练的大规模 AI 模型，可适应多种下游任务。通用人工智能（AGI）是一种假设性的 AI 系统，能够在任何任务上达到或超越人类认知能力，是许多 AI 实验室的长期目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Artificial_general_intelligence">Artificial general intelligence - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Foundation_model">Foundation model</a></li>
<li><a href="https://www.eesel.ai/blog/ai-pretraining">AI pretraining | eesel AI</a></li>

</ul>
</details>

**标签**: `#Google`, `#Gemini 4`, `#AI`, `#pretraining`, `#AGI`

---

<a id="item-10"></a>
### [Anthropic 阐明对开放权重模型的立场](https://www.anthropic.com/news/position-open-weights-models) ⭐️ 8.0/10 [技术]

Anthropic 发布了一份政策声明，主张对所有足够强大的 AI 模型（包括开放权重模型）进行强制安全测试。批评者认为，这一要求因高昂成本和监管障碍实际上会禁止开放模型。 这一声明凸显了 AI 安全与开放性之间的紧张关系，可能影响未来的监管政策。它影响到依赖开放权重模型的开发者、研究人员和公司。 Anthropic 未明确说明谁将执行安全测试或测试成本，这引发了人们对其可能被用来限制访问的担忧。一些人认为该提议实际上是对开放权重模型的禁令。

hackernews · surprisetalk · 7月27日 22:03 · [社区讨论](https://news.ycombinator.com/item?id=49076057)

**背景**: 开放权重模型是指其训练参数（权重）公开发布的 AI 模型，允许他人运行、研究和修改。它们与完全开源模型不同，可能不包含训练代码或数据。例如 Meta 的 Llama 和 Google 的 Gemma。这些模型促进了更广泛的访问和创新，但也引发了安全担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.analyticsvidhya.com/blog/2025/04/open-weight-models/">What are Open Source and Open Weight Models ? | Analytics Vidhya</a></li>
<li><a href="https://promptmetheus.com/resources/llm-knowledge-base/open-weights-model">Open - weights Model | LLM Knowledge Base</a></li>

</ul>
</details>

**社区讨论**: 社区评论大多批评 Anthropic 的立场。评论者认为强制安全测试实际上会禁止开放模型，并将其与过去的监管策略相比较。一些人指责 Anthropic 虚伪，指出其 CEO 过去反对禁令，现在却支持对中国的芯片禁令。其他人则认为这是为了保护 Anthropic 的商业利益。

**标签**: `#AI`, `#open-weights`, `#Anthropic`, `#safety testing`, `#policy`

---

<a id="item-11"></a>
### [研究人员利用漏洞完全控制沃尔沃/埃契尔车队平台](https://eaton-works.com/2026/07/27/my-eicher-hack/) ⭐️ 8.0/10 [技术]

一名安全研究人员发现并利用了沃尔沃/埃契尔车队管理平台的多个漏洞，从而获得了对所有用户和车辆的管理员控制权。该研究人员负责任地披露了问题，但数周未获回应，之后主要漏洞被悄然修复。 此事件凸显了依赖云的汽车系统的严重安全风险，单个平台漏洞可能危及整个车队。它还强调了改进漏洞披露实践和维修权运动的必要性，因为现代汽车越来越依赖专有云服务。 研究人员无需身份验证即可访问内部 API，从而控制所有用户和车辆。漏洞于 2025 年 11 月报告，但在未获回应后，研究人员于 2026 年 7 月公开了细节，并指出主要问题仅在多次跟进后才被修复。

hackernews · EatonZ · 7月27日 15:08 · [社区讨论](https://news.ycombinator.com/item?id=49070756)

**背景**: 沃尔沃 Connect 是一个数字车队管理系统，为卡车提供近乎实时的数据和分析，使车队运营商能够监控性能并规划维护。此类云连接系统引入了网络安全风险，漏洞可能被远程利用。维修权运动倡导车主自由维护和修改车辆的权利，而这往往受到制造商设置的软件障碍和对专有云服务的依赖的阻碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.volvogroup.com/en/news-and-media/news/2023/oct/volvo-trucks-launches-volvo-connect-all-in-one-fleet-management-portal.html">Volvo Trucks Launches Volvo Connect, All-in-One Fleet Management Portal</a></li>
<li><a href="https://www.trendmicro.com/vinfo/us/security/news/internet-of-things/in-transit-interconnected-at-risk-cybersecurity-risks-of-connected-cars">In Transit, Interconnected, at Risk: Cybersecurity Risks of Connected Cars | Trend Micro (US)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Right_to_repair_movement">Right to repair movement</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了对依赖云的汽车安全的担忧，一位用户提到一辆宝马因手机信号不佳而无法启动。另一位评论者区分了保护用户的安全和为公司提供诉讼保护的安全剧场。还分享了一个 FSF 维修权视频的链接，表明对维修权运动的支持。

**标签**: `#security`, `#vulnerability`, `#Volvo`, `#Eicher`, `#fleet platform`, `#car hacking`, `#right-to-repair`

---

<a id="item-12"></a>
### [Libsm64：超级马里奥 64 角色可嵌入其他游戏引擎](https://github.com/libsm64/libsm64) ⭐️ 8.0/10 [技术]

Libsm64 是一个库，它从《超级马里奥 64》中提取角色马里奥，并允许将其嵌入到其他游戏中，通过对原始游戏代码的逆向工程实现跨游戏角色移植。 这展示了一种新颖的游戏互操作性和角色移植方法，无需依赖区块链或专有系统即可实现‘元宇宙’的承诺。它为创意混搭和模组社区开辟了可能性。 该库基于 2019 年公开的《超级马里奥 64》完整反编译项目。它提供了干净的 API，可将马里奥的动作和渲染集成到外部引擎中，已有在《半条命 2》等游戏中的示例。

hackernews · klaussilveira · 7月27日 10:04 · [社区讨论](https://news.ycombinator.com/item?id=49067352)

**背景**: 《超级马里奥 64》最初于 1996 年在 Nintendo 64 上发布。2019 年，一个逆向工程团队完成了游戏代码的完整反编译，使其能够移植到其他平台。Libsm64 基于此反编译，仅提取角色逻辑和渲染，使其可作为库在其他游戏引擎中使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/libsm64/libsm64">GitHub - libsm 64 / libsm 64 : Mario 64 as a library for use in external...</a></li>
<li><a href="https://github.com/n64decomp/sm64">GitHub - n64decomp/sm64: A Super Mario 64 decompilation, brought to you by a bunch of clever folks. · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区反应极为积极，用户称其‘不可思议’，并将其与无需炒作的元宇宙承诺相提并论。一些用户分享了马里奥在《半条命 2》等游戏中的演示视频，还有一个精选的项目列表使用 libsm64。

**标签**: `#reverse engineering`, `#game development`, `#interoperability`, `#library`, `#Super Mario 64`

---

<a id="item-14"></a>
### [AI 算力需求推动核聚变与 SMR 投资热潮](https://www.tmtpost.com/8074899.html) ⭐️ 8.0/10 [技术]

文章分析了 AI 算力需求的爆发如何推动先进核能技术（可控核聚变和小型模块化反应堆 SMR）成为投资热点，并指出中美竞争已从政策层面延伸到定价权争夺。 这一转变将先进核能定位为满足 AI 数据中心巨大能源需求的关键解决方案，而中美在定价权上的竞争可能重塑全球能源市场和技术领导地位。 该分析聚焦于可控核聚变和 SMR 的投资格局，指出这些技术虽仍在开发中，但因 AI 的能源需求而吸引越来越多资本。中美竞争已延伸至定价权，表明双方在成本竞争力上的战略较量。

rss · 钛媒体 · 7月27日 09:20

**背景**: 可控核聚变旨在通过可控、持续的核聚变反应，在地球上复制太阳的能量产生过程，常被称为“人造太阳”。小型模块化反应堆（SMR）是紧凑型、工厂预制的核反应堆，可快速部署，非常适合为 AI 数据中心供电。这两项技术都被视为未来的能源解决方案，核聚变提供几乎无限的清洁能源，而 SMR 提供灵活、低碳的电力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tradingkey.com/zh-hans/analysis/stocks/us-stock/250754423-america-stocks-nuscale-smr-tradingkey-viga-liu">【深度分析】突破AI能源瓶颈：NuScale SMR 引领核能新时代</a></li>
<li><a href="https://news.pedaily.cn/202505/550308.shtml">一天吃透一条产业链： 可 控 核 聚 变 _投资界</a></li>
<li><a href="https://www.jiuyangongshe.com/a/7mcyk084y2">开新服了！ 核 聚 变</a></li>

</ul>
</details>

**标签**: `#nuclear fusion`, `#SMR`, `#AI`, `#investment`, `#US-China competition`, `#energy`

---

<a id="item-15"></a>
### [长鑫科技科创板首日暴涨 471.59%](https://www.stcn.com/article/detail/4042119.html) ⭐️ 8.0/10 [技术]

国产存储龙头长鑫科技（CXMT）7 月 27 日登陆科创板，开盘价 49.5 元，较发行价 8.66 元暴涨 471.59%。此次 IPO 募资总额最高达 666 亿元，创科创板历史纪录。 此次上市凸显了中国推动半导体自主可控的决心，以及科创板对关键科技企业的融资支持。长鑫科技的大涨反映了投资者对国产存储芯片前景的信心，尤其是在中美科技竞争加剧的背景下。 长鑫科技是中国领先的 DRAM 制造商，截至 2020 年采用 19 纳米工艺生产 LPDDR4 和 DDR4 内存，月产能 4 万片晶圆。公司预计 2026 年上半年实现扭亏为盈，归母净利润预计 500 亿至 570 亿元。

telegram · zaihuapd · 7月27日 01:29

**背景**: 科创板是上海证券交易所于 2019 年设立的纳斯达克式板块，旨在支持科技创新企业。长鑫科技成立于 2016 年，是中国少数几家 DRAM 制造商之一，致力于减少对外国存储芯片的依赖。此次 IPO 是中国半导体产业自主化进程中的一个里程碑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://www.cxmt.com/en/">ABOUT CXMT - CXMT</a></li>
<li><a href="https://language.chinadaily.com.cn/a/201906/30/WS5d1817a0a3103dbf1432b082_3.html">2019年6月新闻热词汇总 - Chinadaily.com.cn</a></li>

</ul>
</details>

**标签**: `#IPO`, `#semiconductor`, `#CXMT`, `#STAR Market`, `#Chinese tech`

---

<a id="item-16"></a>
### [Fastjson 1.x 高危 RCE 漏洞无需 Gadget 或 AutoType](https://t.me/zaihuapd/42797) ⭐️ 8.0/10 [技术]

安全研究人员 Kirill Firsov 披露了 Fastjson 1.x 版本 1.2.68 至 1.2.83 中存在的高危远程代码执行漏洞。该漏洞无需开启 autoType 支持，也无需依赖 classpath gadget 链，可在 JDK 8、17 和 21 上利用。 该漏洞非常严重，因为它影响广泛使用的 Java JSON 库，且无需开启 autoType 或特定 gadget 即可利用。由于 Fastjson 1.x 已停止维护，用户必须升级到 Fastjson2 才能修复，这可能带来较大的迁移工作量。 该漏洞影响 Fastjson 1.x 的 1.2.68 至 1.2.83 版本，可在 JDK 8、17 和 21 等多个版本上利用。Fastjson 1.x 已于 2024 年 10 月停止维护，官方不会发布安全补丁，唯一建议的修复措施是升级到 Fastjson2。

telegram · zaihuapd · 7月27日 10:31

**背景**: Fastjson 是阿里巴巴开发的流行 Java JSON 序列化/反序列化库。autoType 功能允许在反序列化时自动解析类型，历史上曾引发多个漏洞。Gadget 链是在反序列化过程中可用于执行任意代码的类序列。该漏洞的特别之处在于它无需开启 autoType 或依赖特定 gadget 链，从而更容易被利用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/alibaba/fastjson">GitHub - alibaba/fastjson: FASTJSON 2.0.x has been released, faster and more secure, recommend you upgrade. · GitHub</a></li>
<li><a href="https://github.com/alibaba/fastjson2">GitHub - alibaba/fastjson2: 🚄 FASTJSON2 is a Java JSON library with excellent performance.</a></li>
<li><a href="https://github.com/alibaba/fastjson/wiki/enable_autotype">enable_autotype · alibaba/fastjson Wiki · GitHub</a></li>

</ul>
</details>

**标签**: `#fastjson`, `#security`, `#vulnerability`, `#RCE`, `#java`

---

<a id="item-17"></a>
### [中芯国际测试中国首台国产 DUV 光刻机](https://t.me/zaihuapd/42800) ⭐️ 8.0/10 [技术]

中芯国际正在测试中国首台由上海初创公司宇量昇自主研发的深紫外（DUV）光刻机。该设备用于生产 28 纳米芯片，并尝试通过多重图形化工艺实现 7 纳米甚至 5 纳米节点。 这标志着中国半导体自给自足努力的一个重要里程碑，减少了对 ASML 等外国设备的依赖。成功可能改变全球芯片供应链和地缘政治格局。 大部分零部件已实现国产化，但仍有部分依赖进口。业内人士称，实现量产和稳定良率至少需要一至两年，最早可能于 2027 年进入量产。

telegram · zaihuapd · 7月27日 14:10

**背景**: DUV 光刻技术使用深紫外光（如 193 纳米波长）在硅片上刻印电路图案。它是制造约 50 纳米特征尺寸芯片的主流技术，但 7 纳米和 5 纳米等先进节点需要多重图形化技术来突破分辨率限制。目前中国最先进的芯片仍依赖荷兰 ASML 的 DUV 设备，而 EUV 光刻机因美国出口管制被禁止对华销售。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DUV_lithography">DUV lithography</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multiple_patterning">Multiple patterning - Wikipedia</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#lithography`, `#SMIC`, `#China`, `#technology`, `#DUV`, `#chip manufacturing`

---

<a id="item-18"></a>
### [Python-build-standalone：便携式 Python 发行版指南](https://gregoryszorc.com/docs/python-build-standalone/main/) ⭐️ 7.0/10 [技术]

一份关于 python-build-standalone 的详细指南已发布，记录了这些自包含 Python 发行版的构建方式，以及它们如何被 uv、pipx 和 Hatch 等工具用于提供便携式 Python 环境。 这些发行版简化了 Python 的分发和版本管理，使开发者能够将 Python 捆绑到应用程序中，而无需系统安装 Python。它们现在由 uv 背后的公司 Astral 维护，确保持续的兼容性和改进。 这些发行版注重便携性和自包含性，常用于将 Python 嵌入其他应用程序。该指南介绍了如何使用这些构建，该项目由 Astral 在 python-build-standalone 仓库下维护。

hackernews · jcbhmr · 7月27日 18:43 · [社区讨论](https://news.ycombinator.com/item?id=49073942)

**背景**: 自包含 Python 发行版是预构建的二进制文件，包含 Python 解释器和标准库，旨在轻松重新分发并无需系统 Python 即可运行。它们被 uv 等现代 Python 工具用于按需安装 Python，并被 PyOxidizer 等项目用于创建单文件可执行文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pyoxidizer.readthedocs.io/">PyOxidizer Project — PyOxidizer 0.23.0 documentation</a></li>
<li><a href="https://pypi.org/project/pyoxidizer/">pyoxidizer · PyPI</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了这些发行版的广泛使用。Astral 的 charliermarsh 确认 uv 使用它们，simonw 称赞其质量并指出 Astral 的维护，rsyring 提到 PyOxidizer 用于单文件可执行文件，zie 提到 APE/Cosmopolitan 跨平台二进制文件。总体情绪积极，强调实用价值。

**标签**: `#python`, `#standalone`, `#distribution`, `#uv`, `#PyOxidizer`

---

<a id="item-20"></a>
### [ccteam：管理 50+并行 AI 编码代理的开源工具](https://www.v2ex.com/t/1230260#reply3) ⭐️ 7.0/10 [技术]

一位开发者发布了开源工具 ccteam，它能将 Claude Code、Codex、Grok 等多个 AI 编码代理编排成一个协作团队，让用户从单一界面管理超过 50 个并行代理。 该工具解决了同时管理多个 AI 编码代理时的常见痛点——通常需要持续的人工监督且效率低下。通过实现代理之间的无缝协作和任务委派，ccteam 提升了开发者的生产力，并支持更自主的工作流程。 ccteam 采用 MIT 许可证，已在 GitHub 上开源。它支持通过 Telegram 或飞书进行通信，用户还可以从浏览器控制台监控进度并下达指令。

rss · V2EX · 7月27日 16:18

**背景**: AI 编码代理是能够自主编写、审查和重构代码的 AI 系统。开发者通常会使用来自不同提供商的多个代理，每个代理都有独特的优势——例如 Grok 速度快适合探索，Claude 思考深入适合规划，Codex 稳定可靠适合长编码任务。单独管理这些代理可能很繁琐，因为每个都需要单独关注和手动交接。ccteam 提供了一个统一的编排层，将这些孤立的代理转变为一个协作团队。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.faros.ai/blog/best-ai-coding-agents-2026">Best AI Coding Agents for 2026: Real-World Developer Reviews</a></li>
<li><a href="https://grokipedia.com/page/Coding_agent">Coding agent</a></li>

</ul>
</details>

**标签**: `#ccteam`, `#AI agents`, `#productivity`, `#open source`, `#code agents`

---

## Politics

<a id="item-1"></a>
### [巴西总统大选：特朗普、关税与中国关系成焦点](https://news.google.com/read/CBMivAFBVV95cUxPdG9HWHNTQl81YzZrMnc4WlZUUnk1em9tcEljVlowNGpEeXkxVktyWFBGUjgtYlcwNDUwbUNDNk1vSE4xdjlFTExvNU52UVJ0dFlTNHozaUR3NmtuWG4zR3VZRHRRbzZZUWllMFRiSWtESlBhNHBVVzRVXzJKRFpvbksxYndJR2ZXOWRXeTdqOGhEZmh1dWhob3BzUC1mNGJucHdKTFdaclJweW8wOGdWaGtVVUVZVzZrU0xMT9IBvAFBVV95cUxPeDQ5RTRncjJKRmoxNUw3ZDkwRGtpQUhzcW5oVlByNXRUVG05amQyb2xUX1pSWEhRZEszSzMydXMyMDUwTFo1aUZ2TXVqWVhPUVNETTNnRUVLMkI4MXRZb3NSUC1qVzFBUDlqUF9wUF9pQkU5dlpnd050c1A4My1hRFBwS3d4NnZaTHk4NUZZVDljQjYtQU5teldZc2RRVm5jeFg4dlA4bWMyeHc3TnVKSlV6ZzYwZVBxVzMzRQ?hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

巴西总统大选日益聚焦于候选人对美国前总统特朗普、贸易关税以及与中国关系的立场，这些问题成为竞选的核心议题。 巴西大选的结果将对国际贸易和地缘政治联盟产生重大影响，因为巴西是全球主要经济体，也是美国和中国的重要合作伙伴。 此次大选预计将受到全球密切关注，候选人在关税和外交政策上的立场可能重塑巴西的经济关系。

rss · Buzzing China · 7月27日 15:00

**背景**: 巴西是全球最大经济体之一，也是全球贸易的关键参与者。其外交政策历来在美国和中国之间寻求平衡。即将举行的总统大选将决定该国在这些关键问题上的方向，影响贸易协定和外交关系。

**标签**: `#Brazil`, `#presidential election`, `#Trump`, `#tariffs`, `#China`, `#geopolitics`

---

<a id="item-2"></a>
### [乌克兰四年来最高平民伤亡，儿童遇难](https://news.google.com/rss/articles/CBMirwFBVV95cUxPcmlweHZiN0lwckYxRGZlbjQzU2gxLUJBTS1VeE1fN1l6eXhleDdCYjFOT1RPUUxQQkY2UUV6Z3Z5QWkzX0NIbTBxckUyWXVLQ3Z2YmdfbDFHaXJtY0tUYl9yQ1RpRzRwR3d4a0x6TG56UFJKNGN3cGFoejdFRF90VElBcWo5RzVyeWJ3QlZPRF96bGRsNDc4UGZ5aG9yVDVldENBUXE3NnQ1d3ZhX3dZ?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

乌克兰报告了四年来战争中最高的平民伤亡，最新遇难者中包括儿童。 这凸显了乌克兰战争造成的惨重人员伤亡，冲突持续夺走平民生命，包括儿童。这强调了国际社会关注保护冲突地区平民的紧迫性。 报告显示平民伤亡达到四年来最高水平，死者中包括儿童。初步报告未提供具体数字或日期。

rss · Buzzing News · 7月27日 23:21

**背景**: 乌克兰冲突已持续多年，平民伤亡一直是令人关切的问题。这份报告显示，当前平民死亡人数是过去四年来最高的，凸显了冲突的持续严重性。

**标签**: `#Ukraine`, `#war`, `#civilian casualties`, `#children`, `#politics`

---

<a id="item-3"></a>
### [特朗普因库存警告暂停对伊战争](https://news.google.com/rss/articles/CBMimwFBVV95cUxQZFU4MWFWcGx1cUhwV3p6LTc1YXFCeC1VY0pqclQ2ejRURTdhanQ0cXBodGdhREw3c0pIQUw1RHp4R3R5Nk9jV1lzWUNhSUd1dFl3WXFSdVBmcG9TWW5nZFJLNFQ0LUtwMDdhTjVEdFpnYW4tMkREOXlaMmdkdTI0VTFTc3RkU3F1UXpGQm1iX2VuSkxnbTA5d0plbw?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

特朗普总统因库存告急警告暂停了对伊朗的军事行动，为通过外交谈判解决霍尔木兹海峡对峙留出空间。 这一事态标志着美伊紧张局势的重大转变，可能避免全面冲突。同时也凸显了后勤和库存问题如何影响高风险的地缘政治决策。 暂停敌对行动据报道是由于库存不足的警告，可能涉及精确制导弹药。这一决定为谈判解决霍尔木兹海峡的持续对峙提供了空间。

rss · Buzzing News · 7月27日 20:09

**背景**: 美国和伊朗长期处于对峙状态，尤其是在霍尔木兹海峡这一关键石油运输通道。近期紧张局势因美国军事部署和伊朗威胁而升级。关于库存的警告可能涉及关键弹药消耗的担忧，这会影响持续军事行动。此次暂停表明战术转向优先通过外交途径解决。

**标签**: `#Trump`, `#Iran`, `#war`, `#geopolitics`, `#US foreign policy`

---

<a id="item-4"></a>
### [特朗普警告：若伊朗谈判失败将采取强力军事行动](https://news.google.com/rss/articles/CBMidkFVX3lxTE16SnRDZDYydVNWMnRSdHM3VldleXNaUUpzRTlhOXk2bjh2RTFuam9GTlE0bjZUYktsVlNtejhvWmV5Zm1ZUTBpdGJzVGtHalRGWlkwQXJ1M0FNOThHYk8zd0hvOUNOTEpSbDN2QlpJVC1xTFZ1Wmc?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

前总统唐纳德·特朗普在接受 Axios 采访时表示，如果与伊朗的外交谈判失败，他已准备好采取‘强力军事行动’。 这一来自前美国总统及重要政治人物的声明表明，美伊紧张局势可能升级，并可能影响当前的外交政策讨论，凸显了如果外交失败则军事冲突的可能性。 该警告是在接受 Axios 采访时作出的，但未提供军事行动的具体性质或时间表。

rss · Buzzing News · 7月27日 15:37

**背景**: 美伊关系数十年来一直紧张，争端涉及伊朗核计划及地区影响力。特朗普在总统任期内对伊朗推行‘极限施压’政策，包括退出核协议并实施制裁。现任拜登政府试图重启外交谈判，但进展停滞。特朗普的声明反映了他对伊朗政策的强硬立场。

**标签**: `#Trump`, `#Iran`, `#military action`, `#geopolitics`, `#US foreign policy`

---

<a id="item-5"></a>
### [最高法院支持特朗普后，为数千人保留 TPS 的斗争](https://news.google.com/rss/articles/CBMikwFBVV95cUxPU293NnliREIwWnpFa3F5emEzWWV1dm1sXzd1bVRVaDB3emx4UTNySmZLc1BxZmROSlZ6TDdLZkFFLXN2eGk4RkZOcnRpbHJIZE91MlBmUzMxNmRIS2xqSTBFQjNFc2daTlo1bkxVNk92eFZhOHdRckNCQm5RZFl5LXV2cUdfNThESkMzVk5aUl8zN1k?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

最高法院裁定支持特朗普政府终止临时保护身份（TPS）的权力，这引发了持续的法律和倡导努力，以保留数千名受影响个人的身份。 这一裁决影响了数千名在美国建立生活的 TPS 持有者，并凸显了围绕移民执法和行政权力的持续法律和政治斗争。 文章深入报道了在最高法院裁决后，保护 TPS 受益人的运动，该裁决确认了总统终止该计划的广泛裁量权。

rss · Buzzing News · 7月27日 15:21

**背景**: 临时保护身份（TPS）是一种临时移民身份，授予来自经历武装冲突、自然灾害或其他非常条件而无法安全返回的国家的国民。它允许受益人在指定期限内在美国生活和工作。特朗普政府试图终止多个国家的 TPS，这引发了法律挑战，并最终上诉至最高法院。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://usafacts.org/articles/temporary-protected-status-tps-definition/">What is Temporary Protected Status ( TPS )? | USAFacts</a></li>
<li><a href="https://www.nolo.com/dictionary/temporary-protected-status-tps-term.html">Temporary Protected Status ( TPS ) Definition</a></li>

</ul>
</details>

**标签**: `#Supreme Court`, `#Trump`, `#TPS`, `#Immigration`, `#Politics`

---

<a id="item-6"></a>
### [特朗普叫停空袭后，伊朗称仍控制海峡且无意谈判](https://news.google.com/rss/articles/CBMi1AFBVV95cUxQVGc0N0FMM0JkWC1rTUFEUUgycGtHOWxZY0VXaW9reFE5TzBoc0czUzd4MVk3NXJtNnp4WU1yRDRZa2dibWhsdERvaWV5bjZtZ1N2czlpZmo4V1BMM1c1Tzh1cktZYVI2bWhGMEJEbl9hR0U4b2JvX3lpcWVhT05lVWR0SkliR1l0T3F5WS1LQ0JrOFBwVjNkM1hObk1hcm50YlNGZVhLeGpHX1hVcElEb09TYzh0bjhXZG1qeHhUUVB4elJXWmlYN1V6NV9KVzBCVE1ZNQ?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

伊朗宣布，在特朗普叫停空袭后，它仍然控制着霍尔木兹海峡，并且无意进行谈判。 这一事态升级了美伊之间的地缘政治紧张局势，威胁全球石油供应稳定，并增加了该地区军事对抗的风险。 霍尔木兹海峡是重要的海上通道，全球约 20%的石油经过此地。特朗普叫停空袭表明此前有美军行动，但具体细节尚不明确。

rss · Buzzing News · 7月27日 14:33

**背景**: 霍尔木兹海峡连接波斯湾与阿曼湾，是中东石油出口的关键通道。美伊两国已冲突数十年，近期因伊朗核计划及地区影响力问题紧张局势升级。特朗普叫停空袭之际，双方军事对峙加剧。

**标签**: `#Iran`, `#US`, `#geopolitics`, `#Strait of Hormuz`, `#conflict`

---

## Social Hot Topics

<a id="item-8"></a>
### [美素佳儿奶粉被曝铅超标 9 倍，公司配合调查](https://www.donews.com/news/detail/1/6647878.html) ⭐️ 9.0/10 [社会热点]

美素佳儿某批次奶粉被曝铅含量超标近 9 倍，公司回应称正配合监管部门核查。 婴儿配方奶粉中的铅污染是严重的公共卫生问题，可能影响婴儿的神经发育。这一事件引发了广泛的公众担忧，并可能促使更严格的食品安全监管。 具体涉事批次和铅超标的确切数值尚未公布。公司呼吁公众在调查期间勿轻信未经证实的信息。

rss · DoNews · 7月27日 07:05

**背景**: 铅是一种有毒重金属，可在体内积累，尤其对婴儿可能导致发育迟缓。婴儿配方奶粉的重金属含量受到严格监管，任何超标都会受到高度重视。此次涉嫌超标近 9 倍的情况极为严重，若经证实将对健康构成重大风险。

**标签**: `#infant formula`, `#lead contamination`, `#food safety`, `#public health`, `#controversy`

---

<a id="item-13"></a>
### [长鑫市值 3.6 万亿：高点还是起点？](https://www.tmtpost.com/8081048.html) ⭐️ 8.0/10 [社会热点]

一篇分析文章讨论了长鑫存储 3.6 万亿元市值是高点还是起点的议题。 这一讨论凸显了中国存储芯片领军企业市值的飙升及其对 A 股市场的潜在影响，反映了市场对国内半导体进步的高度期待。 文章可能分析了市盈率等估值指标，并将长鑫与三星、SK 海力士等全球同行进行比较，但摘要中未提供具体细节。

rss · 钛媒体 · 7月27日 10:43

**背景**: 长鑫存储是中国领先的 DRAM 制造商，是中国推动半导体自给自足的一部分。虽然它并未公开上市，但其估值作为国内存储芯片行业的晴雨表备受关注。3.6 万亿元的数字可能指的是基于私募融资轮或分析师估计的假设市值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jiuyangongshe.com/a/2z5j06y178w">长 鑫 存 储 上市催化！ 手握 长 期订单的10大 存 储 产业链核心标的梳理</a></li>

</ul>
</details>

**标签**: `#A股`, `#长鑫`, `#市值`, `#估值`, `#财经热点`

---

<a id="item-19"></a>
### [OpenAI 网站在中国可访问，V2EX 用户热议](https://www.v2ex.com/t/1230274#reply1) ⭐️ 7.0/10 [社会热点]

V2EX 上一位用户发现，OpenAI 网站（openai.com）现在可以直接从中国大陆访问，无需使用 VPN，这与之前被屏蔽的状态相比是一个重大变化。 这一变化可能预示着中国互联网审查政策对 AI 平台的潜在调整，将影响依赖 OpenAI 服务的开发者、研究人员和企业。 这种可访问性可能在中国不同地区和互联网服务提供商之间不一致，目前尚不清楚这一变化是故意的还是暂时的路由问题。

rss · V2EX · 7月27日 22:10

**背景**: OpenAI 的网站此前在中国被屏蔽，这是中国互联网审查系统（俗称‘防火墙’）的一部分，该系统限制了许多外国网站的访问。V2EX 是一个面向技术专业人士的流行中文在线社区，类似于 Reddit，用户在这里讨论技术和互联网相关话题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-tw/V2EX">V2EX - 維基百科，自由的百科全書</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#China`, `#internet censorship`, `#accessibility`, `#V2EX`

---