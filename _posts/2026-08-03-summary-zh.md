---
layout: default
title: "Horizon Summary: 2026-08-03 (ZH)"
date: 2026-08-03
lang: zh
---

> 从 202 条内容中筛选出 20 条重要资讯。

---

#### Tech
7. [Karpathy 提出将 AI 生成的 3D 场景作为物理世界理解基准](#item-7) ⭐️ 8.0/10 [技术]
8. [阿里开源 22B 实时数字人生成模型](#item-8) ⭐️ 8.0/10 [技术]
9. [AI 早报：DeepSeek-V4-Flash 上线、OpenAI 数学突破、亚马逊 500 亿投资、版权裁决](#item-9) ⭐️ 8.0/10 [技术]
10. [全球 AI 芯片每 9 个月翻番，2028 年将达 2 亿颗](#item-10) ⭐️ 8.0/10 [技术]
11. [中国 AI 算法追踪比特币洗钱，准确率近 90%](#item-11) ⭐️ 8.0/10 [技术]
12. [Kakehashi：实验性 macOS 兼容层登陆 Linux ARM](#item-12) ⭐️ 7.0/10 [技术]
13. [RISC OS Open 庆祝保存与开发二十周年](#item-13) ⭐️ 7.0/10 [技术]
14. [F*：面向证明的编程语言](#item-14) ⭐️ 7.0/10 [技术]
16. [Meshdiff：在浏览器中可视化比较两个 STL 版本](#item-16) ⭐️ 7.0/10 [技术]
17. [欧盟 AI 透明度规则：机器标记与可见标签之别](#item-17) ⭐️ 7.0/10 [技术]
19. [零成本本地动画点播台搭建方案](#item-19) ⭐️ 7.0/10 [技术]
20. [冒险岛 v083 网页版：v86 与 d3d8-webgpu 实现](#item-20) ⭐️ 7.0/10 [技术]

#### Politics
1. [以色列对哈马斯解除武装协议深表关切](#item-1) ⭐️ 9.0/10 [时政]
2. [《华尔街日报》称特朗普下令本周末袭击伊朗](#item-2) ⭐️ 9.0/10 [时政]
3. [乌克兰称袭击俄罗斯大型炼油厂和机场，莫斯科报告 8 人死亡](#item-3) ⭐️ 9.0/10 [时政]
4. [莫斯科市长称餐厅爆炸是恐怖袭击](#item-4) ⭐️ 9.0/10 [时政]
5. [俄罗斯夜间炮击基辅致 9 人死亡，防空争议持续](#item-5) ⭐️ 9.0/10 [时政]
6. [特朗普取消对伊朗的预定打击行动](#item-6) ⭐️ 9.0/10 [时政]

#### Social Hot Topics
15. [eBay 骚扰行动导致 5600 万美元赔偿](#item-15) ⭐️ 7.0/10 [社会热点]

#### 其他 (Other)
18. [独立开发者刻意保持浏览器插件小而稳](#item-18) ⭐️ 7.0/10 [产品经理]

---

## Tech

<a id="item-7"></a>
### [Karpathy 提出将 AI 生成的 3D 场景作为物理世界理解基准](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 8.0/10 [技术]

Andrej Karpathy 在推文中提出，将 AI 生成的 3D 内容（例如“骑自行车的鹈鹕”场景）作为评估模型对物理世界理解的新基准，引发了关于其有效性和影响的讨论。 这种方法将 AI 评估从静态图像生成转向动态 3D 场景，要求模型更深入地理解物理、空间关系和物体交互。这可能会催生更强大的基准测试，更好地反映对真实世界的理解。 社区讨论指出，该基准是定性和主观的，一些人认为当前模型（如 Anthropic 的模型）可能专门针对生成 three.js 代码进行了训练，而非展示真正的物理理解。‘骑自行车的鹈鹕’这个例子被认为已经不再具有挑战性。

hackernews · delichon · 8月2日 04:05 · [社区讨论](https://news.ycombinator.com/item?id=49140998)

**背景**: AI 生成的 3D 内容是一个新兴领域，模型可以根据文本或图像创建 3D 场景。Spline 和腾讯混元等平台提供 AI 驱动的 3D 生成。将此类内容用作基准测试，可以检验模型理解和模拟物理原理的能力，超越了传统的 2D 图像生成基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spline.design/ai-generate">Spline AI 3 D Generation – The power of AI for the 3rd dimension.</a></li>
<li><a href="https://hunyuan3d.online/">Tencent Hunyuan AI : 2D to 3 D Model Generator</a></li>
<li><a href="https://www.emergentmind.com/topics/physics-iq-benchmark">Physics -IQ Benchmark Overview</a></li>

</ul>
</details>

**社区讨论**: 社区评论中既有支持也有怀疑。一些人认为该基准是衡量物理世界理解进展的有价值一步，而另一些人则警告说，它可能只衡量代码生成能力，并且对 AI 内容的接触降低了质量期望。还有人建议转而构建更好的 AI 聊天界面。

**标签**: `#AI`, `#benchmarking`, `#3D generation`, `#machine learning`, `#Karpathy`

---

<a id="item-8"></a>
### [阿里开源 22B 实时数字人生成模型](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247908954&idx=3&sn=1f4f3bf12d5fa00e2c37a4dcb7f71de9) ⭐️ 8.0/10 [技术]

阿里巴巴开源了一个 220 亿参数的模型，能够实时稳定生成数字人，支持自定义角色的流式交互，实现分钟级的长视频生成且无漂移。 这一突破解决了长视频生成中的时间漂移问题，实现了稳定的实时数字人形象，可用于虚拟助手、直播和互动娱乐等场景。开源 22B 模型降低了开发者和研究人员使用该技术的门槛。 该模型拥有 220 亿参数，支持自定义角色的流式交互。它实现了分钟级的实时稳定生成，克服了自回归视频生成中常见的漂移问题。

rss · 量子位 · 8月2日 02:00

**背景**: 数字人生成涉及创建逼真的虚拟形象，使其能够说话和交互。长视频生成常面临时间漂移问题，即错误随时间累积导致质量下降。之前的方案如 MetaHuman-Stream 集成了多种模型实现实时交互，但长时间稳定性仍是挑战。阿里巴巴的模型据称实现了分钟级的稳定生成，是重大改进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai-nav.net/3835.html">MetaHuman-Stream – 实时 交 互 流 式 AI 数 字 人 技术 | AI导航站</a></li>
<li><a href="https://news.qq.com/rain/a/20260212A042RC00">特拉维夫大学创新技术：让AI视频生成不再“跑偏”的神奇记忆管理术_腾讯新闻</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1948652330191922005">分钟级长视频生成迎来“记忆革命”，7倍成本降低，2.2倍端到端生成速度提升!｜斯坦福&字节 - 知乎</a></li>

</ul>
</details>

**标签**: `#AI`, `#digital human`, `#real-time generation`, `#open source`, `#Alibaba`, `#22B model`

---

<a id="item-9"></a>
### [AI 早报：DeepSeek-V4-Flash 上线、OpenAI 数学突破、亚马逊 500 亿投资、版权裁决](https://www.tmtpost.com/8088267.html) ⭐️ 8.0/10 [技术]

DeepSeek 发布 V4-Flash（284B 参数、1M 上下文），OpenAI Astra 用 Lean 证明攻克 10 道数学难题，亚马逊 500 亿美元投资 OpenAI 并锁定云合同，慕尼黑法院裁定 Suno AI 音乐生成侵权确立版权规则。 这些进展标志着 AI 竞争、研究能力、企业投资和法律框架的重大转变。它们将影响模型效率、AI 自主性、云市场动态和版权执法。 DeepSeek-V4-Flash 每个 token 仅激活 284B 参数中的 13B，效率极高。OpenAI Astra 的解决方案估计花费 2000 美元 token 成本，可公开验证，但模型尚未对外开放测试。

rss · 钛媒体 · 8月2日 00:16

**背景**: DeepSeek 是中国 AI 公司，其 MoE 模型每个 token 仅激活部分参数以提高效率。OpenAI Astra 使用 Lean 形式化验证自主解决数学问题。亚马逊投资 OpenAI 体现云服务商与 AI 公司深度绑定趋势。Suno 是流行的 AI 音乐平台，慕尼黑法院裁决为 AI 音乐版权确立先例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash">DeepSeek V 4 Flash - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://www.implicator.ai/openai-astra-10-math-problems-lean-proofs/">OpenAI Says Astra Solved 10 Math Problems With Lean Proofs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Suno_(platform)">Suno (platform) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#DeepSeek`, `#OpenAI`, `#Amazon`, `#copyright`, `#technology news`

---

<a id="item-10"></a>
### [全球 AI 芯片每 9 个月翻番，2028 年将达 2 亿颗](https://www.nytimes.com/interactive/2026/07/29/technology/ai-chips-data-center-boom.html) ⭐️ 8.0/10 [技术]

据 Epoch AI 估算，全球 AI 芯片数量每 9 个月翻一番，预计到 2028 年底将达到 2 亿颗。IDC 预测，全球 AI 基础设施投资将在 2029 年突破 1 万亿美元，而去年为 3180 亿美元。 AI 芯片的爆炸式增长凸显了规模定律在 AI 发展中的主导地位，推动了万亿美元级别的投资，并加剧了中美之间的竞争。然而，大规模基础设施建设也引发了电价上涨、环境影响以及投机泡沫风险的担忧。 美国目前控制着全球约 80%的 AI 算力，仅谷歌一家的 AI 芯片数量据信是中国所有公司总和的四倍。中国正通过自主研发半导体和建设 AI 基础设施加速追赶。

telegram · zaihuapd · 8月2日 01:01

**背景**: AI 规模定律是经验性观察，表明神经网络性能会随着模型规模、训练数据和计算资源的增加而可预测地提升。这推动了对专用 AI 芯片（如 GPU 和 TPU）的需求，这些芯片针对深度学习所需的并行计算进行了优化。AI 芯片数量每 9 个月翻一番的快速增长，反映了超越传统半导体趋势（如摩尔定律）的加速发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_scaling_law">AI scaling law</a></li>
<li><a href="https://blogs.nvidia.com/blog/ai-scaling-laws/">How Scaling Laws Drive Smarter, More Powerful AI | NVIDIA Blog</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#scaling laws`, `#infrastructure investment`, `#US-China competition`, `#data centers`

---

<a id="item-11"></a>
### [中国 AI 算法追踪比特币洗钱，准确率近 90%](https://www.scmp.com/news/china/science/article/3362493/chinese-police-ai-algorithm-tracks-bitcoin-money-laundering-90-accuracy) ⭐️ 8.0/10 [技术]

中国人民公安大学的研究团队开发了一款结合记忆模块与大语言模型的 AI 框架，能够以近 90%的准确率识别非法加密货币交易。该研究成果已发表在同行评审期刊《情报杂志》上。 这一成果为执法部门提供了打击匿名加密货币交易中洗钱行为的强大工具，而这类洗钱活动在全球范围内日益严峻。该算法的高准确率和可解释性有望显著提升监管技术，帮助当局更有效地追踪非法资金流动。 该框架整合了用于长期信息存储的记忆模块和用于理解交易背景的大语言模型，为监管部门提供了可解释、可推广的解决方案。中国最高检察院数据显示，2025 年全国检方共起诉 3,259 名涉及虚拟货币与地下银行洗钱案的嫌疑人。

telegram · zaihuapd · 8月2日 08:22

**背景**: 人工智能中的记忆模块允许模型长期保留和回忆信息，从而提升其在大量交易中追踪模式的能力。大语言模型（LLM）是经过海量文本数据训练的 AI 系统，能够理解和生成类似人类的文本，可用于分析交易叙述或检测可疑模式。结合这两种技术，该算法既能记住历史交易行为，又能解读复杂的交易背景，从而实现高检测准确率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/">Titans + MIRAS: Helping AI have long-term memory</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agent-memory">What Is AI Agent Memory? | IBM</a></li>

</ul>
</details>

**标签**: `#AI`, `#blockchain`, `#money laundering`, `#China`, `#law enforcement`, `#cryptocurrency`

---

<a id="item-12"></a>
### [Kakehashi：实验性 macOS 兼容层登陆 Linux ARM](https://github.com/wie-project/kakehashi) ⭐️ 7.0/10 [技术]

Kakehashi 是一个实验性的用户空间翻译层，能够在 Linux ARM 上原生运行 macOS ARM64 二进制文件。早期原型已成功运行 7-Zip、curl 和 Xcode 工具，并在包含 8000 个文件的目录树上通过了多线程压缩测试。 如果成功，Kakehashi 将能够像 Wine 运行 Windows 应用程序一样，在 Linux 上无需硬件模拟即可运行 macOS 软件。这对于 Apple Silicon Mac 和 ARM 服务器等 ARM 平台尤其有价值，将扩展 Linux on ARM 的软件生态。 该项目以命令行界面为主，不使用 JIT 编译器；它加载 Darwin Mach-O 二进制文件，映射独立的 libSystem，并翻译 BSD 系统调用。目前 7-Zip 的运行速度比原生 Linux 执行慢约 5.2 倍，但开发者已制定了优化计划以缩小差距。

hackernews · vlad_kalinkin · 8月2日 16:26 · [社区讨论](https://news.ycombinator.com/item?id=49145937)

**背景**: macOS 和 Linux 拥有不同的内核和系统库，因此 macOS 二进制文件无法直接在 Linux 上运行。兼容层如 Wine（用于 Windows）和 Darling（用于 macOS）通过翻译系统调用并提供替代库实现来解决这一问题。Darling 是一个成熟的 macOS 兼容层，但主要针对 x86_64，目前有一个开放的 ARM64 支持拉取请求。Kakehashi 是一个全新的实验性项目，专门针对 ARM64，并且完全在用户空间运行，无需内核模块。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/wie-project/kakehashi">wie-project/ kakehashi : Userspace macOS translation layer for Linux ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Darling_(software)">Darling (software) - Wikipedia</a></li>
<li><a href="https://www.darlinghq.org/">Darling | macOS translation layer for Linux</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区反应积极，许多人表达了长期关注。评论者将 Kakehashi 与 Darling 项目进行比较，并建议潜在的合作。一些人指出该项目仍处于早期阶段但很有前景，另一些人则提出了用例，例如通过类似 yabridge 的层在 Linux 上运行 Audio Unit 插件。

**标签**: `#macOS`, `#Linux`, `#ARM`, `#compatibility layer`, `#open source`, `#reverse engineering`

---

<a id="item-13"></a>
### [RISC OS Open 庆祝保存与开发二十周年](https://www.riscosopen.org/news/articles/2026/06/20/twenty-years-of-risc-os-open) ⭐️ 7.0/10 [技术]

2026 年 6 月 20 日，RISC OS Open 迎来了成立二十周年，纪念其在保存和发展 RISC OS 操作系统方面走过的二十年历程。 这一里程碑凸显了一个小而充满热情的社区对保持这一具有历史意义的操作系统生命力的持久奉献，影响了复古计算和 ARM 平台上的开源开发。 RISC OS 以其在 Raspberry Pi 等硬件上极快的启动速度而闻名，其源代码于 2018 年完全以 Apache 许可证开源，从而实现了社区驱动的持续开发。

hackernews · AlexeyBrin · 8月2日 12:36 · [社区讨论](https://news.ycombinator.com/item?id=49143967)

**背景**: RISC OS 最初由 Acorn Computers 于 1987 年为其基于 ARM 的 Archimedes 个人计算机开发。Acorn 解散后，该操作系统由多家公司维护，直到 RISC OS Open 成立以管理其开源发布。该操作系统采用模块化设计并配备图形用户界面，至今仍可在 Raspberry Pi 等现代 ARM 设备上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC_OS">RISC OS - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/RISC_OS_Open">RISC OS Open</a></li>

</ul>
</details>

**社区讨论**: 社区成员表达了对在 RISC OS 上进行开发的怀念，有人回忆完全用 ARM 汇编语言编写了一个流行的定制工具。其他人则对该项目的持久性感到惊讶，并称赞该操作系统在 Raspberry Pi 上的快速启动，同时还强调了像 Sibelius 这样起源于该平台的著名应用程序。

**标签**: `#RISC OS`, `#open source`, `#operating system`, `#retro computing`, `#ARM`

---

<a id="item-14"></a>
### [F*：面向证明的编程语言](https://fstar-lang.org/) ⭐️ 7.0/10 [技术]

F* 是一种通用的面向证明的编程语言，允许开发者同时编写代码和形式化证明。最近它在 Hacker News 上引发了讨论，获得了 146 个点赞和 64 条评论。 F* 代表了形式化验证的一种重要方法，使开发者能够证明程序的正确性和安全属性。它在 Hacker News 上的讨论表明开发者社区对面向证明的编程兴趣日益增长。 F* 的类型系统包含依赖类型、单子效应和精化类型，并利用 SMT 求解器进行自动验证。程序可以提取到 OCaml、F#、C、WebAssembly 或汇编语言。

hackernews · ducktective · 8月2日 12:31 · [社区讨论](https://news.ycombinator.com/item?id=49143925)

**背景**: 形式化验证是通过数学方法证明程序满足规范的过程。像 F* 这样的面向证明的编程语言允许开发者用同一种语言编写代码和证明，使验证更加便捷。F* 受 ML 和 OCaml 影响，专为高可靠性软件设计。它是微软研究院和法国国家信息与自动化研究所（Inria）的联合项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/F*_(programming_language)">F* (programming language)</a></li>
<li><a href="https://fstar-lang.org/">F*: A Proof-Oriented Programming Language</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论既有正面反馈也有批评。一些用户赞赏 F* 与 C 代码交互的能力，而另一些用户则批评主页上缺乏可见的语法示例。还有人对它的工业应用表示好奇。

**标签**: `#programming language`, `#formal verification`, `#proof-oriented`, `#functional programming`, `#Hacker News`

---

<a id="item-16"></a>
### [Meshdiff：在浏览器中可视化比较两个 STL 版本](https://meshdiff.com/) ⭐️ 7.0/10 [技术]

Meshdiff 是一款全新的浏览器端工具，用户可以在客户端完全本地地可视化比较两个 STL 文件版本，无需将数据上传到服务器。 该工具对 3D 打印和建模工作流程非常重要，因为它允许直接在浏览器中快速、私密地进行版本比较，减少了对专业软件的需求，并确保了数据隐私。 Meshdiff 完全在客户端运行，使用 WebGL 和 JavaScript，支持 STL、3MF 和 OBJ 格式。它能够高亮显示版本之间新增的材料、移除的材料以及尺寸偏差。

hackernews · projscope · 8月2日 11:34 · [社区讨论](https://news.ycombinator.com/item?id=49143479)

**背景**: STL（立体光刻）是一种常见的 3D 打印文件格式，通过三角形来描述表面几何形状。Meshdiff 受 git diff 启发，为 3D 网格提供可视化比较。它由 Timothy Stiles 创建，既可作为命令行工具也可作为网页应用使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/STL_(file_format)">STL (file format)</a></li>
<li><a href="https://meshdiff.com/">Meshdiff — Compare 3D Model Versions (STL, 3MF, OBJ Diff Tool)</a></li>
<li><a href="https://github.com/TimothyStiles/meshdiff">GitHub - TimothyStiles/ meshdiff : A command line tool to visually diff ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员建议添加同步视口旋转等功能，并希望与 GitHub 集成用于拉取请求预览。一些用户最初将 STL 与 C++标准模板库混淆，但该工具因其客户端优先的特性而受到好评。

**标签**: `#3D modeling`, `#STL`, `#browser tool`, `#comparison`, `#client-side`

---

<a id="item-17"></a>
### [欧盟 AI 透明度规则：机器标记与可见标签之别](https://www.v2ex.com/t/1231592#reply0) ⭐️ 7.0/10 [技术]

欧盟委员会更新了《AI 法案》第 50 条透明度规则的指南和 FAQ，明确要求 AI 生成内容需同时具备机器可读标记和场景特定的可见披露，而非单一通用标签。技术分析将合规拆分为提供方系统能力和业务使用方披露两个层面。 这一澄清对面向欧盟市场的 AI 产品开发者至关重要，它区分了技术标记义务和场景披露责任，并强调了实质性人工审核和编辑问责的必要性，而许多现有内容工作流在这方面存在不足。 机器可读标记必须有效、可靠且可互操作，欧盟正在开发标准化标签。业务使用方必须披露深度伪造、情感识别/生物特征分类，以及未经实质性人工审核和编辑问责的公共利益文字。

rss · V2EX · 8月2日 21:50

**背景**: 欧盟《AI 法案》是一项具有里程碑意义的人工智能监管法规。第 50 条自 2026 年 8 月 2 日起生效，要求生成式 AI 系统的提供方以机器可读格式标记输出，并要求业务使用方在特定场景下披露 AI 生成内容。区分提供方和业务使用方的角色是合规的关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialintelligenceact.eu/transparency-rules-article-50/">The EU AI Act’s Transparency Rules: A Practical Guide to Article 50 | EU Artificial Intelligence Act</a></li>
<li><a href="https://artificialintelligenceact.eu/article/50/">Article 50: Transparency Obligations for Providers and Deployers of Certain AI Systems | EU Artificial Intelligence Act</a></li>
<li><a href="https://humantext.pro/blog/eu-ai-act-article-50-explained">EU AI Act Article 50 Explained: Practical Compliance</a></li>

</ul>
</details>

**标签**: `#EU AI Act`, `#AI transparency`, `#product implementation`, `#machine-readable marking`, `#AI regulation`

---

<a id="item-19"></a>
### [零成本本地动画点播台搭建方案](https://www.v2ex.com/t/1231570#reply1) ⭐️ 7.0/10 [技术]

一位 V2EX 用户分享了一份详细指南，介绍如何使用 ZMServer 和 ZWPlayer 搭建零成本的本地动画流媒体系统，方便在家庭网络内任何设备上管理和播放儿童视频。 该方案解决了暑假期间家长管理儿童视频的常见痛点，提供了一种实用且零成本的方法来本地管理和播放儿童教育视频，减少对云服务的依赖，并简化了非技术家庭成员的操作。 该系统使用 ZMServer 自动扫描指定文件夹并生成播放列表，ZWPlayer 提供在线播放器，支持字幕全文检索和视频/音频片段截取功能，便于语言学习。

rss · V2EX · 8月2日 14:18

**背景**: 本地媒体服务器允许同一家庭网络内的设备流式传输内容，无需依赖互联网。传统上，管理儿童视频涉及深层文件夹层次或复杂的 NAS 设置。该方案通过使用轻量级服务器（ZMServer）自动索引视频文件并生成可通过网页播放器访问的播放列表来简化这一过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ZhongHuaRong/ZMServer">GitHub - ZhongHuaRong/ ZMServer · GitHub</a></li>

</ul>
</details>

**标签**: `#local media server`, `#kids video management`, `#ZMServer`, `#DIY`, `#parenting tech`

---

<a id="item-20"></a>
### [冒险岛 v083 网页版：v86 与 d3d8-webgpu 实现](https://www.v2ex.com/t/1231558#reply14) ⭐️ 7.0/10 [技术]

基于 v86 x86 模拟器和 d3d8-webgpu 转换层，冒险岛 v083 版本现已完全在浏览器中运行，加载约 1-2 分钟后可达 30-40 帧每秒。 该项目通过结合 x86 虚拟化与现代 Web 图形 API，为复古游戏模拟提供了新思路，有望让经典游戏无需本地安装或高性能硬件即可在浏览器中畅玩。 该模拟使用 v86 模拟 x86 环境，并通过 d3d8-webgpu 将 Direct3D 8 调用转换为 WebGPU，从而在浏览器中实现硬件加速图形。项目提供了测试账号供立即体验。

rss · V2EX · 8月2日 11:40

**背景**: v86 是一个开源 x86 PC 模拟器，通过 WebAssembly 在浏览器中运行，性能接近原生。WebGPU 是一种现代 Web API，提供高效的 GPU 访问，类似于 Vulkan、Metal 或 Direct3D 12。d3d8-webgpu 是一个兼容层，将 Direct3D 8 图形调用转换为 WebGPU，使为 Direct3D 8 设计的旧游戏能在网页上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/copy/v86">GitHub - copy/v86: x86 PC emulator and x86-to-wasm JIT, running in the browser · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebGPU">WebGPU - Wikipedia</a></li>

</ul>
</details>

**标签**: `#retro gaming`, `#web emulation`, `#v86`, `#d3d8-webgpu`, `#MapleStory`, `#browser game`

---

## Politics

<a id="item-1"></a>
### [以色列对哈马斯解除武装协议深表关切](https://news.google.com/rss/articles/CBMiswFBVV95cUxPUU5CY216dkdHTXZGZUZYUmt6WXRhZWlSMTVmc2xydFZwb3ZCQ2Vfbk0wRzI1aWxNRHpkUTgyUks3aHNGZ2dkS2RvSWhGbXFoNERoZGs0a1FOSVUwUi1YTVlLVXBTek5YRzcxb0FMQlIxdjRQeFIyNlA5Szh1MFhnVHhUZ1RFUk1Gdi1yUFRUcS1HSmhzLTFESGh3N1BRVG9EVTBqLWFJdUxwTXN0UUlpN2R0QQ?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

以色列已正式对与哈马斯拟议的解除武装协议表示严重关切，表明该协议可能面临障碍。 这一事态可能对正在进行的停火谈判以及更广泛的中东和平进程产生重大影响，因为解除哈马斯武装是以色列的关键要求。 该协议的具体条款以及以色列关切的细节尚未披露，但这一声明反映了双方之间的深度不信任。

rss · Buzzing News · 8月2日 18:32

**背景**: 哈马斯是一个自 2007 年以来控制加沙地带的巴勒斯坦武装组织。以色列与哈马斯多次发生冲突，解除哈马斯武装一直是以色列在任何和平协议中的长期目标。当前的协议是为实现持久停火而做出的更广泛努力的一部分。

**标签**: `#Israel`, `#Hamas`, `#disarmament`, `#geopolitics`, `#Middle East`

---

<a id="item-2"></a>
### [《华尔街日报》称特朗普下令本周末袭击伊朗](https://news.google.com/rss/articles/CBMisgFBVV95cUxPSDBJUW9hNDF0UEVzelo4M3N0c1JyWHZWVjhxa1hEanZzMHQ0YzNUbnJPUDRDbTBuSFJFaXBJMjB4TFVaMV9IQVZ3dDRaUEJlYUhnRk1PSk85djZyRWljM3oyaEJ3STR3Ny1rTlB1RFR1anYydmt6X1c4bG9JQ2cyWmJDVzRhd2pVVFFBSURPWDVOcDFZb2RLcXRhbnFKUjFqQ1BtdEQzRE93emNRVnZvM0dR?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

《华尔街日报》报道称，特朗普总统已下令最早于本周末对伊朗发动潜在军事袭击。 这一事态标志着美伊紧张局势的重大升级，可能对全球石油市场和地区稳定产生深远的地缘政治和经济影响。 报道未明确说明计划袭击的具体性质或规模，也不清楚该命令是否已最终确定或取决于某些条件。'最早本周末'的时间表表明局势正在迅速发展。

rss · Buzzing News · 8月2日 17:12

**背景**: 美伊关系数十年来一直紧张，近期冲突点包括 2018 年美国退出伊朗核协议以及 2020 年伊朗将军卡西姆·苏莱曼尼被暗杀。伊朗还被指控支持激进组织并发展核计划，以色列和美国视其为威胁。任何直接军事行动都将代表当前制裁、网络攻击和代理人冲突之外的重大升级。

**标签**: `#Trump`, `#Iran`, `#military attack`, `#geopolitics`, `#WSJ`

---

<a id="item-3"></a>
### [乌克兰称袭击俄罗斯大型炼油厂和机场，莫斯科报告 8 人死亡](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1oYUZ6VWhYbnNlNndSMVlVdmtXeU0wWEFJek51QUtTNm1Taks0ODMwTzdhV3hnbkQtVUc0Sy01S1p1akNpY2lqeTl2RkRyTWhJMTlNdEMxQ2lXQQ?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

乌克兰声称袭击了俄罗斯一家大型炼油厂和一个机场，而莫斯科方面报告称袭击造成 8 人死亡。 此次袭击针对俄罗斯关键基础设施，使冲突升级，并展示了乌克兰打击俄罗斯纵深目标的能力。报告的人员伤亡为持续战争增添了重大人员损失。 炼油厂和机场的具体位置尚未披露，但此次袭击标志着局势显著升级。莫斯科方面确认 8 人死亡，表明袭击规模较大。

rss · Buzzing News · 8月2日 16:56

**背景**: 乌克兰-俄罗斯战争始于 2022 年 2 月俄罗斯全面入侵。此后，乌克兰偶尔打击俄罗斯境内目标，包括石油基础设施，以扰乱俄罗斯军事后勤。此次最新袭击似乎是针对俄罗斯领土的较重大打击之一。

**标签**: `#Ukraine`, `#Russia`, `#war`, `#oil refinery`, `#airfield`, `#casualties`, `#geopolitics`

---

<a id="item-4"></a>
### [莫斯科市长称餐厅爆炸是恐怖袭击](https://news.google.com/rss/articles/CBMilAFBVV95cUxOdEdjSGk3eVZ6RnVUb3ZXcjZINEo3bE9qZHpYbUhid2t1ck9PVm5MNGhHUjhjYUxjalhidnVydVFOTXVzSnFWSWczSHNxVFlhbVU3NXNjRkJQRnBQR0RtR0hEZmdVUlVPbzllZmtTWEpSVW91WmdjZUptYjhnZkR3S293QXNvcS04Q292NzU3MEhVVmlw0gGUAUFVX3lxTFB5ZzlrQjZOZXh3VXpNZXN0cVIwWlh3SmJtU2J4WW1GVWJsSWgwbGI5dDE1dmdray1SeTZKVENrSDktMjVXSy04SmRORnZsMWtwZ0xIRjlWTHMtc0tsdEIzSW5vVkUzR29PV0dqZWZyZDJaRHRMaXhFMURqekRIbV9MTnkwanFqLWxKYW5wMDREc3A0ekk?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

一枚炸弹在莫斯科一家高档餐厅爆炸，造成 3 人死亡、至少 21 人受伤。莫斯科市长称这起事件是‘残暴的恐怖袭击’。 这起发生在俄罗斯首都的袭击凸显了持续存在的安全威胁，并可能加剧政治紧张局势。它可能导致安全措施加强，并影响莫斯科的公众情绪。 据描述，炸弹是简易或自制装置，有报道称由一名女性携带。爆炸发生在餐厅外或入口处，造成顾客伤亡。

rss · Buzzing News · 8月2日 13:12

**背景**: 简易爆炸装置（IED）是一种使用非军用部件制造的炸弹，常用于非对称战争。莫斯科市长迅速将爆炸定性为‘残暴的恐怖袭击’，表明了官方的定性立场。此类袭击在莫斯科市中心较为罕见，具有重大的政治影响。

**标签**: `#Moscow`, `#terror attack`, `#restaurant blast`, `#politics`, `#current affairs`

---

<a id="item-5"></a>
### [俄罗斯夜间炮击基辅致 9 人死亡，防空争议持续](https://news.google.com/rss/articles/CBMiigFBVV95cUxNd2x5Q0xXZVVieFNuWVNiZnlwNHU4RndQRzJNTzNmeWZ3S19KUGd6TnlUeGVZNEJVZnhpT1YyMUJmSlA5aDNYbjU0TFNZX0Z6d0hDTGdMdWtmTFRHYjhTMnRLRy1jRDlvYXVfWElObVdESFFTaHE1TnNfS3RWRFJiTEJ5dVVFd0pBWUE?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

俄罗斯一夜之间对基辅发动导弹和无人机猛烈炮击，造成 9 人死亡，而乌克兰与美国之间关于防空武器供应的争议仍在持续。 此次袭击凸显了乌克兰平民面临的持续威胁，以及先进防空系统的迫切需求，而这一问题已成为美乌关系中的一个争议点。 据报道，此次炮击使用了多种导弹和无人机，压倒了基辅的防空系统。9 名遇难者包括平民，这次袭击凸显了缺乏足够防护的城市所面临的脆弱性。

rss · Buzzing News · 8月2日 10:48

**背景**: 自 2022 年 2 月俄罗斯全面入侵以来，乌克兰一直依赖西方提供的爱国者（Patriot）和 NASAMS 等防空系统来保护其城市。然而，美国国会的政治辩论推迟了额外的援助计划，导致弹药和系统短缺。这场围绕防空支持的持续争议使乌克兰城市更容易遭受俄罗斯的打击。

**标签**: `#Russia`, `#Ukraine`, `#Kyiv`, `#air defense`, `#war`

---

<a id="item-6"></a>
### [特朗普取消对伊朗的预定打击行动](https://news.google.com/rss/articles/CBMibkFVX3lxTFBmRm9ldjJOd2ZubDZtNFZ2YTdlLVJ4QWxpTEwtek1weGtPdW02blI1Mlpsa0hLUFRpeGRKaTN6bmlacldaSzVodG5ieVRpMC15RG9SWXNROHZ5eTBBb3llUnV5aVhEOXBEMHd3YnJB?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

美国前总统唐纳德·特朗普宣布取消原定对伊朗的军事打击，称中东盟友提出了请求，且结束战争的谈判已取得进展。 这一决定标志着美伊紧张局势的重大转变，可能避免大规模军事升级，并为外交解决方案打开大门。 特朗普表示，取消打击的前提是‘迅速’达成协议，并且与中东盟友已就协议框架达成一致。

rss · Buzzing News · 8月2日 10:32

**背景**: 美国与伊朗长期处于冲突状态，近几个月紧张局势不断升级。特朗普此次宣布是在中东盟友参与斡旋停火与结束敌对行动的谈判背景下作出的。

**标签**: `#US-Iran`, `#Trump`, `#war`, `#geopolitics`, `#breaking news`

---

## Social Hot Topics

<a id="item-15"></a>
### [eBay 骚扰行动导致 5600 万美元赔偿](https://www.ft.com/content/06ec1b03-d4af-40cf-b12a-4ba5a410f6d2) ⭐️ 7.0/10 [社会热点]

eBay 的安全团队骚扰了一对运营批评该公司的新闻通讯的夫妇，导致 5600 万美元的和解，以及多名高管被判刑，其中包括前安全与安保高级总监 Jim Baugh 被判处 57 个月监禁。 此案凸显了企业权力的危险以及安全团队可能被用来对付批评者的风险。它警示了大型企业内部问责和监督的重要性。 骚扰行动包括发送威胁信息、监视这对夫妇的住所，并试图在他们的车上安装 GPS 追踪器。涉案的安全团队成员包括前警察队长，5600 万美元的和解金额是此类案件中最大的之一。高管 Brian Gilbert 和 David Harville 也受到了判决。

hackernews · JumpCrisscross · 8月2日 19:19 · [社区讨论](https://news.ycombinator.com/item?id=49147435)

**背景**: David 和 Ina Steiner 运营着批评 eBay 商业实践的新闻通讯 'eBay Bytes'。作为回应，eBay 的安全团队发起了一场协调的骚扰行动来恐吓他们。此案凸显了企业安全资源如何被滥用来压制批评者，并导致相关人员承担法律后果。

**社区讨论**: 评论者对此事是否孤立事件表示怀疑，质疑 eBay 是否还针对过其他批评者。还有人担忧安全团队中前警察队长的参与。部分评论转向讨论 eBay 的高额费用，但总体情绪是愤怒并要求进一步调查。

**标签**: `#eBay`, `#harassment`, `#corporate accountability`, `#legal`, `#security team`

---

## 其他 (Other)

<a id="item-18"></a>
### [独立开发者刻意保持浏览器插件小而稳](https://www.v2ex.com/t/1231589#reply3) ⭐️ 7.0/10 [产品经理]

一位独立开发者分享了他的 Chrome 插件经验，该插件自动按域名和最近使用时间整理标签页，日活约 1200，付费用户 300 多，采用 29 元一次性买断模式。他刻意不添加同步、AI 等复杂功能，以保持低维护成本和个人自由。 这挑战了独立开发必须追求规模的普遍观念，展示了一种以低维护成本和自由时间为优先的可持续模式。为产品经理和独立开发者在权衡增长与生活质量时提供了宝贵参考。 该插件所有数据本地存储，无服务器依赖，维护成本几乎为零。开发者估计两年内实际投入时间不到一个月，月收入在 2000-3000 元之间波动。

rss · V2EX · 8月2日 18:34

**背景**: 浏览器扩展是运行在浏览器中的小程序，用于增强功能。标签页管理工具帮助用户整理大量打开的标签页，这是重度浏览器用户的常见痛点。独立开发者常常面临两难：添加功能以促进增长，还是保持简单以减少工作量。

**标签**: `#indie development`, `#product strategy`, `#browser extension`, `#monetization`, `#minimalism`

---