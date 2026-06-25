---
layout: default
title: "Horizon Summary: 2026-06-25 (ZH)"
date: 2026-06-25
lang: zh
---

> 从 341 条内容中筛选出 20 条重要资讯。

---

#### 技术 (Technology)
1. [OpenAI 发布首款定制 AI 推理芯片 Jalapeno](#item-1) ⭐️ 9.0/10 [技术]
2. [电子电路可直接打印在活体组织上](#item-2) ⭐️ 9.0/10 [技术]
9. [Anthropic 指控阿里巴巴非法提取 Claude AI 能力](#item-9) ⭐️ 8.0/10 [技术]
10. [LuaJIT 3.0 语法扩展引发语言身份辩论](#item-10) ⭐️ 8.0/10 [技术]
11. [高通以 40 亿美元收购 AI 初创公司 Modular](#item-11) ⭐️ 8.0/10 [技术]
12. [NVIDIA 45°C 液冷设计大幅降低数据中心用水](#item-12) ⭐️ 8.0/10 [技术]
13. [5 亿美元基金旨在终结呼吸道感染](#item-13) ⭐️ 8.0/10 [技术]
14. [Nub：无需替换运行时即可为 Node.js 提供类似 Bun 的工具包](#item-14) ⭐️ 8.0/10 [技术]
15. [Meta 提出 AI 工程中的‘元框架’概念](#item-15) ⭐️ 8.0/10 [技术]

#### 时政 (Politics)
3. [叙利亚战后蜜月期因逮捕事件告终](#item-3) ⭐️ 9.0/10 [时政]
5. [中国以美国朱姆沃尔特级驱逐舰为导弹试验目标](#item-5) ⭐️ 9.0/10 [时政]
6. [委内瑞拉接连发生地震，造成数十人死亡、数百人受伤](#item-6) ⭐️ 9.0/10 [时政]
7. [普京现在提议与乌克兰进行和平谈判](#item-7) ⭐️ 9.0/10 [时政]
8. [联合国委员会指控以色列蓄意攻击加沙儿童](#item-8) ⭐️ 9.0/10 [时政]
20. [中方制裁引发日本产业崩溃](#item-20) ⭐️ 8.0/10 [时政]

#### 社会热点 (Social Hotspots)
4. [影子账号利用大病患儿家属在短视频平台骗捐](#item-4) ⭐️ 9.0/10 [社会热点]
16. [印度考试泄题：228 万成绩作废，暴露底层青年绝望](#item-16) ⭐️ 8.0/10 [社会热点]
17. [央视曝光高考报考骗局：免费 AI 工具千问被高价倒卖](#item-17) ⭐️ 8.0/10 [社会热点]
18. [2026 年一万个中国版 Codex AI 模型大乱斗](#item-18) ⭐️ 8.0/10 [社会热点]
19. [微信在金矿上孵化豆包](#item-19) ⭐️ 8.0/10 [社会热点]

---

## 技术 (Technology)

<a id="item-1"></a>
### [OpenAI 发布首款定制 AI 推理芯片 Jalapeno](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10 [技术]

OpenAI 宣布推出其首款定制 AI 推理芯片，名为“Jalapeno”，由 Broadcom 合作开发、台积电（TSMC）制造。该芯片从设计到生产仅用时九个月，部分设计流程借助 OpenAI 自身模型加速完成。 此举降低了 OpenAI 在推理任务上对昂贵且功耗高的 NVIDIA GPU 的依赖，有望减少运营成本和能源消耗。这也标志着 AI 公司为优化特定工作负载的性能和效率而设计定制芯片的行业趋势。 Jalapeno 芯片是一款专用集成电路（ASIC），仅针对 AI 推理优化，不用于训练。OpenAI 使用自身模型加速了芯片设计与优化，但具体效果尚不明确。社区消息确认该芯片由台积电（TSMC）制造。

hackernews · jamdesk · 6月24日 17:47 · [社区讨论](https://news.ycombinator.com/item?id=48663324)

**背景**: AI 推理芯片是一种专门用于运行已训练好的 AI 模型（如图像识别或自然语言处理）的处理器，与处理计算密集型模型构建阶段的训练芯片不同。定制芯片（ASIC）在特定推理任务上比通用 GPU 能效高得多，因此谷歌（TPU）和 AWS（Inferentia）等公司都开发了自有芯片。此前 OpenAI 在训练和推理上主要依赖 NVIDIA GPU。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/ai-inference-chip-market-demand-size-segmentation-2026-2033-srgqf">AI Inference Chip Market Demand, Size & Segmentation 2026-2033</a></li>
<li><a href="https://hashrateindex.com/blog/what-is-an-ai-asic-guide-ai-chips/">What Is an AI ASIC? The Complete Guide</a></li>
<li><a href="https://www.brownstoneresearch.com/bleeding-edge/training-vs-inference/">Training vs. Inference - Brownstone Research</a></li>

</ul>
</details>

**社区讨论**: 部分评论者对 OpenAI 声称其模型加速了芯片设计表示怀疑，认为这可能是模糊的营销话术。其他人确认了台积电为制造商，并讨论了定制推理芯片的广阔前景，包括谷歌的 TPU 以及将模型直接烧录到硅片上的初创公司 Taalas。总体而言，社区对能效提升感到兴奋，但对 OpenAI 的设计加速细节存疑。

**标签**: `#OpenAI`, `#custom chip`, `#Broadcom`, `#AI hardware`, `#inference chip`, `#TSMC`

---

<a id="item-2"></a>
### [电子电路可直接打印在活体组织上](https://www.economist.com/science-and-technology/2026/06/24/electronics-can-now-be-printed-onto-living-tissues) ⭐️ 9.0/10 [技术]

研究人员开发出一种方法，利用超声引导的 3D 打印技术，将导电聚合物直接打印在活体组织上，甚至可以在不透明生物组织内部进行打印。 这一突破实现了电子器件与活体组织的无缝集成，为先进医疗植入物、生物集成设备以及无需传统刚性电子器件的实时健康监测铺平了道路。 该技术利用超声引导打印过程，无需侵入性手术即可在体内深处精确制造生物电子结构。导电聚合物具有生物相容性，可以打印出复杂的图案。

rss · The Economist · 6月24日 16:33

**背景**: 传统的生物电子器件通常使用刚性植入物，可能导致组织损伤或排异反应。这项新方法基于 3D 生物打印和导电聚合物的进展，旨在制造与身体和谐集成的设备。斯坦福团队的工作代表了十五年来对无缝电子-组织接口的研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techfinder.stanford.edu/technology/ultrasound-guided-3d-printing-conductive-polymers-bioelectronics-tissue">Ultrasound-guided 3D Printing of Conductive Polymers for...</a></li>
<li><a href="https://www.azosensors.com/news.aspx?newsID=15863">Seamless Integration of Electronics with Living Tissue</a></li>

</ul>
</details>

**标签**: `#bioelectronics`, `#medical technology`, `#3D printing`, `#tissue engineering`

---

<a id="item-9"></a>
### [Anthropic 指控阿里巴巴非法提取 Claude AI 能力](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/) ⭐️ 8.0/10 [技术]

据路透社看到的一封信件，Anthropic 正式指控阿里巴巴非法提取其 Claude AI 模型的能力，称这是该公司已知的最大规模此类攻击。 这一指控凸显了 AI 行业中关于模型蒸馏实践的日益紧张关系，Anthropic 等公司声称其知识产权被盗，而批评者则指出，鉴于许多 AI 模型是在公开抓取的数据上训练的，这具有讽刺意味。 据报道，此次提取涉及中国经销商以低于官方 API 价格 70-90% 的价格提供 Claude 代币，利用共享账户和支付欺诈，然后将模型输出和推理痕迹出售给实验室作为训练数据。

hackernews · htrp · 6月24日 19:48 · [社区讨论](https://news.ycombinator.com/item?id=48664814)

**背景**: 模型蒸馏是一种机器学习技术，将大型“教师”模型的知识转移到较小的“学生”模型，通常用于提高效率。虽然合法的蒸馏很常见，但非法提取涉及未经授权复制模型的能力，Anthropic 声称这里发生了这种情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://iamhemanth.in/blog/model-distillation-attacks-how-ai-capabilities-are-being-stolen-and-what-we-can-do-about-it">Model Distillation Attacks: How AI Capabilities Are Being Stolen and...</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：一些人认为这种做法类似于微调，而另一些人则指出 Anthropic 在利用抓取的网络数据训练后抱怨的虚伪性。少数评论者详细介绍了中国经销商用于压低价格和提取推理痕迹的技术方法。

**标签**: `#AI`, `#model distillation`, `#intellectual property`, `#Anthropic`, `#Alibaba`, `#technology news`

---

<a id="item-10"></a>
### [LuaJIT 3.0 语法扩展引发语言身份辩论](https://github.com/LuaJIT/LuaJIT/issues/1475) ⭐️ 8.0/10 [技术]

LuaJIT 3.0 的 GitHub 议题提议添加类似 C 语言的语法，如用 && 表示逻辑与，以及三元运算符 (x ? y : z)，旨在让来自其他语言的开发者更熟悉。 该提案可能对 Lua 生态系统产生重大影响，因为 LuaJIT 是一个关键实现。它引发了关于保持 Lua 独特语法与采用更常见约定以降低新手门槛之间的讨论。 该提案建议添加 &&、|| 和三元运算符作为替代语法，同时保留原始的 Lua 关键字（and、or）。三元运算符尤其有争议，一些人推荐使用 Lua 风格的 if-then-else 表达式。

hackernews · phreddypharkus · 6月25日 00:41 · [社区讨论](https://news.ycombinator.com/item?id=48667336)

**背景**: LuaJIT 是 Lua 编程语言的高性能即时编译器，广泛应用于游戏和嵌入式系统。Lua 历史上在主要版本之间不保持严格兼容性，这导致了多种类 Lua 语言的生态系统（如 Luau）。提议的语法变更旨在让熟悉类 C 语言的开发者更容易上手。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LuaJIT">LuaJIT - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论意见不一：一些用户认为添加类 C 语法是表面功夫，削弱了 Lua 的独特风格；另一些人则指出替代语法已在 Luau 等项目中出现。一些评论者还提到了他们自己的项目（如 LJS），这些项目尝试为 Lua VM 使用不同的语法。

**标签**: `#LuaJIT`, `#programming languages`, `#syntax`, `#open source`

---

<a id="item-11"></a>
### [高通以 40 亿美元收购 AI 初创公司 Modular](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/) ⭐️ 8.0/10 [技术]

2026 年 6 月 24 日，高通宣布将以约 40 亿美元收购 AI 初创公司 Modular，该公司是 Mojo 编程语言和 MAX AI 基础设施平台的开发者。 此次收购标志着高通战略性地进军 AI 基础设施和 RISC-V 架构，可能挑战 NVIDIA 的 CUDA 主导地位和 ARM 的处理器生态系统。通过将高通的芯片设计与 Modular 的编译器技术结合，有望重塑 AI 硬件-软件栈。 据路透社报道，该交易估值 40 亿美元。Modular 的 Mojo 语言基于 MLIR 编译器框架，可在 CPU、GPU 和 ASIC 上实现高性能内核，高通计划将该技术集成到其未来芯片中，包括 RISC-V 设计。

hackernews · timmyd · 6月24日 13:49 · [社区讨论](https://news.ycombinator.com/item?id=48659798)

**背景**: Mojo 是一种专有编程语言，结合了类似 Python 的语法和系统级性能，面向 AI 和高性能计算。它利用 MLIR 编译器框架来支持包括 GPU 和定制加速器在内的多种硬件。RISC-V 是一种开放标准的指令集架构，是专有 ARM 和 x86 设计的替代方案。高通传统上是 ARM 的授权用户，近年来正扩展至 RISC-V 和 AI 领域，以减少对 ARM 的依赖并在 AI 芯片市场展开竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/RISC-V_architecture">RISC-V architecture</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有人对 Mojo 可能永远无法成为真正的跨平台语言表示失望，而另一些人则认为这是高通构建 RISC-V AI 生态系统的大胆战略举措。多位评论者指出，这与高通的 ARMv9 芯片以及中国使用 ARM 的超算崛起存在潜在协同效应，暗示 AI 硬件格局正在发生更广泛的转变。

**标签**: `#acquisition`, `#Qualcomm`, `#Modular`, `#AI`, `#Mojo`, `#Chris Lattner`

---

<a id="item-12"></a>
### [NVIDIA 45°C 液冷设计大幅降低数据中心用水](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) ⭐️ 8.0/10 [技术]

NVIDIA 发布了一种用于 AI 数据中心的液冷架构，其冷却液温度可达 45°C，将用水量降至接近零，并使得废热可用于区域供暖。 这一创新解决了 AI 数据中心日益增长的水足迹问题，并通过向区域供暖网络提供低品位热量创造新的收入来源，每年可为当地社区节省数百万美元。 该设计采用直接到芯片的液冷方式，冷却液温度高达 45°C（113°F），远高于典型的液冷温度，从而无需蒸发冷却即可散热，并使废热可用于区域供暖。

hackernews · nitin_flanker · 6月24日 14:10 · [社区讨论](https://news.ycombinator.com/item?id=48660178)

**背景**: 传统数据中心依赖空气冷却或较低温度的液冷，通常需要耗水量大的蒸发冷却来散热。区域供暖系统将热量从中央热源分配到多个建筑，如果数据中心的废热温度足够高，可以成为有价值的输入。NVIDIA 的 45°C 冷却液温度足够高，可以输入区域供暖回路，将废热转化为资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techbuzz.ai/articles/nvidia-s-45-c-liquid-cooling-redefines-ai-data-center-energy">NVIDIA's 45 ° C Liquid Cooling Redefines AI Data Center Energy</a></li>
<li><a href="https://www.guru3d.com/story/nvidia-unveils-liquid-cooling-design-for-ai-data-centers/">NVIDIA Unveils 45 ° C Liquid Cooling Design for AI Data Centers</a></li>
<li><a href="https://www.araner.com/blog/data-center-and-district-heating-an-outstanding-combination">Data center and district heating: an outstanding combination</a></li>

</ul>
</details>

**社区讨论**: 评论者注意到了区域供暖的协同潜力，有人建议数据中心可以向社区免费提供热量，每年节省数百万美元。其他人质疑这一设计与现有液冷相比的创新之处，并询问外部温度对效率的影响。还有评论者提到了 NASA 类似的高温水冷方案。

**标签**: `#data center cooling`, `#liquid cooling`, `#water conservation`, `#district heating`, `#NVIDIA`

---

<a id="item-13"></a>
### [5 亿美元基金旨在终结呼吸道感染](https://blog.interceptfund.com/p/ending-respiratory-infections) ⭐️ 8.0/10 [技术]

一项 5 亿美元的慈善基金已启动，旨在通过投资改进空气净化技术和新型预防措施来消除呼吸道感染，该消息由 Intercept Fund 在一篇博客文章中宣布。 这项举措可能通过解决呼吸道感染的根源来改变公共卫生优先事项，从而减轻感冒、流感和长新冠等疾病对全球数百万人的负担。 该基金专注于资助空气净化技术和预防措施，一次研讨会调查指出，资金不足是进展的主要障碍，其次是技术可行性问题。

hackernews · EthanFantl · 6月25日 01:14 · [社区讨论](https://news.ycombinator.com/item?id=48667588)

**背景**: 呼吸道感染，包括普通感冒和流感，导致健康人每年约有 5%的时间处于生病状态。长新冠已使许多人永久残疾，凸显了改善预防和空气质量措施的必要性。

**社区讨论**: 社区评论表达了希望与怀疑的混合情绪：一些人分享了因呼吸道感染导致的个人悲剧，另一些人质疑该基金的规模与 NASA 阿波罗计划等项目的对比，还有少数人对健康人每年 5%时间生病的统计数据表示怀疑。

**标签**: `#respiratory infections`, `#philanthropy`, `#air cleaning`, `#long covid`, `#public health`

---

<a id="item-14"></a>
### [Nub：无需替换运行时即可为 Node.js 提供类似 Bun 的工具包](https://github.com/nubjs/nub) ⭐️ 8.0/10 [技术]

Colin McDonnell 发布了 Nub，这是一个面向 Node.js 的一体化工具包，通过 oxc 驱动的 Node-API 插件添加 TypeScript 编译，并通过 --require 预加载钩子为 Worker 和 Temporal 等 API 注入 polyfill，无需替换 Node 的运行时。 Nub 为 Node.js 用户提供了类似 Bun 的开发体验，可能降低许多项目转向 Bun 的吸引力，其纯附加的方式意味着现有 Node.js 代码和生态系统完全兼容。 编译器由 oxc（The Oxidation Compiler）驱动，这是一个基于 Rust 的高性能工具链，并打包为 Node-API 插件以提高速度。Nub 还注册了模块解析钩子，并为 Node.js 尚未原生支持的 API（如 Worker 和 Temporal）注入 polyfill。

hackernews · colinmcd · 6月24日 14:14 · [社区讨论](https://news.ycombinator.com/item?id=48660267)

**背景**: Bun 是一个流行的 JavaScript 运行时，集成了编译器、包管理器和测试运行器，提供简化的开发体验。Node.js 虽然广泛使用，但需要单独的工具进行 TypeScript 编译，并且缺少一些现代 API（如 Temporal）。Nub 旨在将这些功能引入 Node.js，而无需用户放弃其运行时。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/oxc-project/oxc">GitHub - oxc-project/oxc: ⚓ A collection of high-performance JavaScript tools.</a></li>
<li><a href="https://oxc.rs/docs/guide/what-is-oxc.html">What is Oxc?</a></li>
<li><a href="https://medium.com/@ankushchavan0411/understanding-javascript-temporal-a-better-way-to-handle-dates-and-time-674195c5708f">Understanding JavaScript Temporal : A Better Way to... | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区反应积极，用户称赞这一想法并报告成功迁移（例如，一个单体仓库零问题迁移）。一些人提出了关于 ESM 支持以及使用 --require 与 --import 的技术问题，而另一些人则建议包装 pnpm 进行包管理。

**标签**: `#nodejs`, `#typescript`, `#tooling`, `#bun`, `#open-source`

---

<a id="item-15"></a>
### [Meta 提出 AI 工程中的‘元框架’概念](https://www.latent.space/p/ainews-its-meta-harness-summer) ⭐️ 8.0/10 [技术]

Meta 提出了一个名为‘元框架’的新概念，这是一个用于协调多个 AI 框架的元级框架，据 Latent Space 的 AINews 报道。 这一发展标志着从单个框架工程向更高层次编排层的转变，可能实现更强大、可扩展的多智能体 AI 系统。 ‘元框架’建立在现有的 AI 框架工程概念之上，后者涉及用上下文、约束、反馈循环和工作流所有权来包装 AI 智能体。

rss · Latent Space · 6月25日 02:14

**背景**: AI 框架工程是围绕 AI 智能体构建工程化包装的学科，将原始模型转变为功能系统。一个健壮的框架可以提升即使是平庸的 AI，而一个糟糕的框架可能削弱优秀的模型。‘元框架’进一步提供了协调多个框架的元层，可能用于复杂的多智能体场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dsvgroup.medium.com/what-is-an-ai-harness-and-how-to-build-a-minimal-one-yourself-dc70f1d758f2">What Is An AI Harness And How To Build A Minimal One... | Medium</a></li>
<li><a href="https://www.forbes.com/sites/lanceeliot/2026/06/19/harness-engineering-becomes-vital-backbone-for-ai-makers-and-happy-users/">Harness Engineering Becomes Vital Backbone For AI Makers And...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Meta`, `#harness engineering`, `#newsletter`

---

## 时政 (Politics)

<a id="item-3"></a>
### [叙利亚战后蜜月期因逮捕事件告终](https://www.economist.com/middle-east-and-africa/2026/06/24/middle-east-dispatch-newsletter-syrias-honeymoon-is-over) ⭐️ 9.0/10 [时政]

据中东记者 Gareth Browne 报道，叙利亚政府实施的一次逮捕行动损害了其公众形象，标志着战后蜜月期的结束。 这一事件标志着叙利亚战后稳定性的重大转变，可能削弱政府重建合法性和国际关系的努力。 逮捕的具体细节及被捕者身份尚未披露，但该事件被视为政府战后叙事的转折点。

rss · The Economist · 6月24日 15:34

**背景**: 经过多年内战，巴沙尔·阿萨德领导的叙利亚政府进入了一段相对平静和外交重新接触的时期，常被称为“蜜月期”。这一时期的特点是努力与邻国关系正常化并重建基础设施。此次逮捕事件表明，内部异议或安全挑战可能再次浮现，威胁到这种脆弱的稳定。

**标签**: `#Syria`, `#politics`, `#government`, `#arrest`, `#Middle East`

---

<a id="item-5"></a>
### [中国以美国朱姆沃尔特级驱逐舰为导弹试验目标](https://news.google.com/read/CBMitAFBVV95cUxQaWFHOVdSbm9pRkhiQUNlWXprbEdIbF9IN19SOHFDanI4Q25HYnpwX0lCQXhTbDE2MUJFSkNBcFhyR0xnQ2E1RU9XSXI4ZVRfWlpNNkI2V1RzM0pDc3ZJUVQ3bGE1eTc0Ul96RmcySXducENYLUtmUEhEeXdEUjdkME1KUktseWtJZ2NMOUFnRkU1TEZNUXZsRjlaMGs5dHBvSm5tQzVpdkU0aFhEWFY2RUQ1dXo?hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

近期图片显示，中国将一艘美国海军朱姆沃尔特级驱逐舰作为反舰弹道导弹的试验目标，标志着两国军事对峙的显著升级。 此举展示了中国打击包括隐身驱逐舰在内的先进美国军舰的能力，凸显了美国在太平洋地区海军资产面临的日益增长的威胁，可能改变该地区的战略格局。 朱姆沃尔特级驱逐舰是美国海军最大且最隐身的现役水面战舰，最初设计用于对陆攻击，后改为执行水面作战任务。中国的 DF-21D 反舰弹道导弹被称为‘航母杀手’，射程约 1500 公里，旨在打击海上移动目标。

rss · Buzzing China · 6月24日 07:57

**背景**: 朱姆沃尔特级驱逐舰（DDG-1000）是美国海军的一级三艘导弹驱逐舰，采用隐身内倾船体和综合电力推进系统。最初设计用于对岸火力支援，但因成本超支仅建造了三艘。DF-21D 是中国的一种反舰弹道导弹，能够瞄准航空母舰和大型军舰，约在 2010 年形成初始作战能力。这类导弹由于速度快、末段弹道陡峭，难以拦截。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zumwalt-class_destroyer">Zumwalt-class destroyer</a></li>
<li><a href="https://en.wikipedia.org/wiki/USS_Zumwalt">USS Zumwalt - Wikipedia</a></li>

</ul>
</details>

**标签**: `#China`, `#US`, `#military`, `#missile tests`, `#geopolitics`

---

<a id="item-6"></a>
### [委内瑞拉接连发生地震，造成数十人死亡、数百人受伤](https://news.google.com/rss/articles/CBMikwFBVV95cUxOQ3liWjNhcnpvNXlqdFFrMlREVG1iel9fUEpSb1hFMFVUWks2Zm1aYTZfUkFPYl81Q082MlViNnRkbUxkS09UX1BQQ0NJX0lneUdXMllxbl81ajJfY012YXVJWEE0M2trbHRCd1JKdHltd05zOUdpeVVCVjRPRU9TaXBlZmFWZ1dDeWZsU1NrVmNpaUE?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

委内瑞拉发生一系列接连地震，其中包括一次 7.1 级强震，已造成至少 32 人死亡、数百人受伤，首都加拉加斯数十栋建筑倒塌。 这场重大自然灾害造成了严重的人员伤亡和大范围破坏，需要政府紧急响应和国际关注，同时也凸显了地震活跃地区城市基础设施的脆弱性。 这些地震被报道为接连发生的事件，其中 7.1 级地震最为强烈，临时总统确认至少 32 人死亡，加拉加斯数十栋建筑倒塌。

rss · Buzzing News · 6月25日 06:03

**背景**: 委内瑞拉位于加勒比板块边界附近的地震活跃区，因此容易发生地震。首都加拉加斯人口密集，许多老旧建筑可能不符合现代抗震安全标准，这增加了强震中倒塌的风险。

**标签**: `#Venezuela`, `#earthquake`, `#natural disaster`, `#casualties`, `#breaking news`

---

<a id="item-7"></a>
### [普京现在提议与乌克兰进行和平谈判](https://news.google.com/rss/articles/CBMirwFBVV95cUxPeFlHZ3ZkcGhiSVgtSUttQnljcUpQT2l1bnVxN0ZJcnFDSnV5d3I4YkdocnM5clUtdGUxTEk3UFljbGc1TU5qdko5SzlfV0tCblEtWlNZWlc5OTg5SFdpRzV6TXBKNUlNYTZBcFhacUNtR3lOaGc4SDZiMnhkTl9vb25abnYxaWlhVGw1Smxob0h4MzNldy0tSHc3ZjFHRVNPcHA1dWdsUVo5RlNzaXBv?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

俄罗斯总统弗拉基米尔·普京最近呼吁俄罗斯与乌克兰之间举行和平谈判，这引发了对其时机和动机的质疑。 这一提议可能标志着俄罗斯战略的转变或对战况变化的回应，对战争进程和全球稳定具有重大影响。 该提议是在军事行动和国际制裁持续的背景下提出的，分析人士正在研究这是否反映了真正的意愿还是战术性姿态。

rss · Buzzing News · 6月25日 04:44

**背景**: 俄乌战争始于 2022 年 2 月，已造成大量伤亡和破坏。此前的和平谈判陷入僵局，双方均坚持强硬立场。

**标签**: `#Russia-Ukraine war`, `#peace talks`, `#Putin`, `#geopolitics`, `#international relations`

---

<a id="item-8"></a>
### [联合国委员会指控以色列蓄意攻击加沙儿童](https://news.google.com/rss/articles/CBMivwFBVV95cUxPczBoQV8tZlpNM0pwSUdYckxRdmM4a203N3AtZkRVRkpCUkNtYVBwVnQ5VzlxNm9TdWt3REprdnZ5b2NKM1NDZXVUb0EtTWJ1S19TV2JyQzJMLUhhTGdwN2swaVZMcHNSVXJwT1R4aFljU3lYS0Y2ekI5bm9OS09vSTBUOUZzOWhpbXZFbDY5TzY5LTVhbUR0b2V3QXpCSXNadzh4OFlKUzFSUVI1bnpRbGE3UUJocjZHVGZLOUZ1SQ?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

联合国独立委员会发现以色列蓄意将加沙地带的巴勒斯坦儿童作为袭击目标，并指控其犯有种族灭绝和暴行罪。 这一指控具有重大的国际法律和人道主义影响，可能加剧全球对以色列的压力，并影响战争罪调查。 该委员会的调查结果是对冲突持续调查的一部分，强调蓄意针对儿童是指控种族灭绝的关键要素。

rss · Buzzing News · 6月25日 01:48

**背景**: 联合国巴勒斯坦被占领土问题独立国际调查委员会负责调查该地区违反国际法的行为。根据国际人道法，蓄意针对平民（尤其是儿童）被视为战争罪。

**标签**: `#Israel`, `#Gaza`, `#UN`, `#war crimes`, `#children`, `#human rights`

---

<a id="item-20"></a>
### [中方制裁引发日本产业崩溃](https://www.huxiu.com/article/4868048.html?f=rss) ⭐️ 8.0/10 [时政]

中方对日制裁已开始显现显著效果，导致日本工业领域出现广泛混乱。制裁引发了连锁经济反应，被描述为产业崩溃。 这一事态标志着中日地缘政治紧张局势的重大升级，可能对全球供应链产生长期影响。日本工业领域的混乱可能波及全球依赖日本零部件和技术的行业。 据报道，制裁已导致日本制造业和贸易出现一连串失败，但报告中未详细说明具体措施和受影响的行业。'连锁反应'一词表明影响正在超出最初目标范围。

rss · 虎嗅 · 6月25日 02:30

**背景**: 中日两国经济关系复杂，日本是中国的主要贸易伙伴和投资国。近年来，双方在历史问题、领土争端和技术竞争上的紧张局势加剧。制裁是政府施加压力的工具，通常针对特定行业或实体。当前的制裁似乎范围广泛，足以在日本造成严重的产业混乱。

**标签**: `#China-Japan relations`, `#sanctions`, `#industrial impact`, `#geopolitics`

---

## 社会热点 (Social Hotspots)

<a id="item-4"></a>
### [影子账号利用大病患儿家属在短视频平台骗捐](https://www.huxiu.com/article/4870120.html?f=rss) ⭐️ 9.0/10 [社会热点]

一篇报道揭露，中国短视频平台上出现大量‘影子账号’，冒充真实大病患儿家属进行骗捐，利用平台流量驱动的生态牟利。 这破坏了公众对在线慈善的信任，将捐款从真正需要的家庭分流，同时揭示了平台推荐算法可能放大虚假内容而非真实求助的问题。 报道指出，真实的大病患儿家属正涌向短视频平台求助，但他们面临影子账号的竞争，这些账号使用编造的故事和情感操控来吸引捐款。

rss · 虎嗅 · 6月25日 03:55

**背景**: 中国的短视频平台（如抖音、快手）因其庞大的用户基础和算法驱动的内容分发，已成为在线筹款的主要渠道。推荐算法优先推送能产生高互动的内容，这可能会无意中助长利用情感叙事的虚假帖子。影子账号是模仿合法慈善案例的虚假个人资料，旨在欺骗观众捐款。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10642507/">An overview of video recommender systems: state-of-the-art and research issues - PMC</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2772941924001005">The short video platform recommendation mechanism based on the improved neural network algorithm to the mainstream media - ScienceDirect</a></li>
<li><a href="https://arxiv.org/html/2507.21467v1">Efficient Data Retrieval and Comparative Bias Analysis of Recommendation Algorithms for YouTube Shorts and Long-Form Videos</a></li>

</ul>
</details>

**标签**: `#social media`, `#donation fraud`, `#short video platforms`, `#charity`, `#children's health`, `#online fundraising`

---

<a id="item-16"></a>
### [印度考试泄题：228 万成绩作废，暴露底层青年绝望](https://www.huxiu.com/article/4870139.html?f=rss) ⭐️ 8.0/10 [社会热点]

印度一场大规模考试泄题丑闻导致 228 万考生的成绩被作废，揭露了该国竞争性考试体系中普遍存在的腐败问题。 这一事件凸显了印度底层青年在社会流动性和教育公平方面的严重缺失——一场考试可能决定他们的一生，而系统性腐败进一步堵死了他们的出路。 泄题事件涉及一场重要的招聘考试，228 万考生的规模使其成为印度历史上最大的考试舞弊案之一，当局为维护公正取消了所有成绩。

rss · 虎嗅 · 6月25日 04:28

**背景**: 在印度，政府工作和大学入学的竞争性考试对贫困和农村青年来说极其重要，他们视其为摆脱贫困的唯一途径。然而，频繁的泄题和腐败丑闻侵蚀了人们对系统的信任，使许多合格考生失去机会。

**标签**: `#印度`, `#考试泄题`, `#社会公平`, `#底层青年`, `#教育丑闻`

---

<a id="item-17"></a>
### [央视曝光高考报考骗局：免费 AI 工具千问被高价倒卖](https://www.huxiu.com/article/4870126.html?f=rss) ⭐️ 8.0/10 [社会热点]

央视揭露，不法咨询机构将阿里巴巴免费开源的 AI 模型千问（Qwen）高价转卖给高考考生，收取数千元费用，而该工具本身完全免费提供建议。 这种行为利用信息不对称，侵害焦虑的家庭，破坏教育公平和消费者权益。它凸显了在蓬勃发展的 AI 辅助教育咨询市场中加强监管的紧迫性。 千问是阿里巴巴以 Apache 2.0 许可证发布的开源大语言模型，可在 Hugging Face 等平台免费获取。骗局涉及将模型输出重新包装成付费咨询服务，且未向消费者披露。

rss · 虎嗅 · 6月25日 03:52

**背景**: 高考是中国全国性大学入学考试，考生和家长常寻求专业指导来制定申请策略。像千问这样的 AI 工具可以分析数据并提供个性化建议，但其免费可用性并不广为人知。不法中介利用这一信息差，对本质上免费的服务收取高价。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen-7B-Chat">Qwen / Qwen -7B-Chat · Hugging Face</a></li>

</ul>
</details>

**标签**: `#Gaokao`, `#education`, `#consumer rights`, `#AI tools`, `#social issue`

---

<a id="item-18"></a>
### [2026 年一万个中国版 Codex AI 模型大乱斗](https://www.huxiu.com/article/4870118.html?f=rss) ⭐️ 8.0/10 [社会热点]

据中国科技媒体虎嗅报道，一场包含一万个中国开发的、类似 OpenAI Codex 的 AI 编程智能体的大规模竞赛计划于 2026 年举行。 这一事件凸显了中国在 AI 编程智能体领域的快速进展，可能加速国产 AI 工具的研发与普及，培育出一个挑战 OpenAI Codex 等西方模型的竞争生态。 该竞赛涉及一万个中国版 Codex，暗示这是一场大规模基准测试或大乱斗式的编程能力比拼，但具体规则和组织方尚未披露。

rss · 虎嗅 · 6月25日 03:34

**背景**: OpenAI Codex 是一套 AI 驱动的编程智能体，可自动化编写、重构和调试代码等软件工程任务。中国科技公司一直在开发类似的智能体，常被称为“中国版 Codex”，以在 AI 编程领域展开竞争。2026 年如此规模的竞赛将展现中国 AI 开发的广度，并促进社区参与。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/OpenAI_Codex">OpenAI Codex</a></li>
<li><a href="https://www.reddit.com/r/OpenAI/comments/1n5iqqj/openai_nailed_it_with_codex_for_devs/">openAI nailed it with Codex for devs - Reddit</a></li>

</ul>
</details>

**标签**: `#AI`, `#Codex`, `#China`, `#competition`, `#2026`

---

<a id="item-19"></a>
### [微信在金矿上孵化豆包](https://www.huxiu.com/article/4870111.html?f=rss) ⭐️ 8.0/10 [社会热点]

据报道，微信正在孵化一款名为“豆包”的新产品，利用其庞大的用户生态系统，将 AI 驱动的输入和语音功能直接集成到应用中。 此举可能通过提供先进的 AI 能力显著提升微信内的用户参与度，有可能重塑用户与平台的互动方式，并为社交媒体 AI 集成树立新标准。 豆包以语音输入为核心卖点，并在键盘模式下仅保留拼音，相比微信传统保守的产品理念，这代表了一种更激进的策略。

rss · 虎嗅 · 6月25日 03:19

**背景**: 微信是中国占主导地位的社交媒体平台，拥有超过十亿用户，历史上对添加新功能一直持谨慎态度。豆包似乎是一款 AI 驱动的输入工具，可能与其他科技巨头（如字节跳动）的类似产品竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://min.news/en/tech/acab5e0a87fc30183c53166f7fa5d0ba.html">Doubao is "typed" into WeChat . - iMedia</a></li>
<li><a href="https://blog.aitoearn.ai/doubao-input-in-wechat/">Doubao “Input” in WeChat</a></li>
<li><a href="https://eu.36kr.com/en/p/3839575253993985">WeChat AI: A Narrow Door Opened for Smartphone Makers - Focus...</a></li>

</ul>
</details>

**标签**: `#WeChat`, `#Doubao`, `#social media`, `#product incubation`

---