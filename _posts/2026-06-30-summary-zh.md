---
layout: default
title: "Horizon Summary: 2026-06-30 (ZH)"
date: 2026-06-30
lang: zh
---

> 从 29 条内容中筛选出 9 条重要资讯。

---

#### 技术 (Technology)
1. [美国最高法院裁定地理围栏搜查令需受宪法保护](#item-1) ⭐️ 9.0/10 [技术]
2. [特斯拉 FSD v14 Lite 让 HW3 车型获得 HW4 级智驾能力](#item-2) ⭐️ 9.0/10 [技术]
3. [华为开源盘古 2.0 模型，505B/92B 参数，512K 上下文](#item-3) ⭐️ 9.0/10 [技术]
4. [LongCat-2.0：基于华为昇腾集群训练的 1.6T MoE 模型](#item-4) ⭐️ 8.0/10 [技术]
5. [内存安全上下文切换：setjmp/longjmp 替代方案](#item-5) ⭐️ 8.0/10 [技术]
6. [火箭实验室收购铱星](#item-6) ⭐️ 8.0/10 [技术]
7. [韩国将投入 1 万亿美元用于存储芯片和人形机器人](#item-7) ⭐️ 8.0/10 [技术]
8. [深入解析：CUDA 内核从 CPU 到 GPU 的完整启动路径](#item-8) ⭐️ 8.0/10 [技术]

#### 社会热点 (Social Hotspots)
9. [韩红宣布即日起退出公益行业](#item-9) ⭐️ 7.0/10 [社会热点]

---

## 技术 (Technology)

<a id="item-1"></a>
### [美国最高法院裁定地理围栏搜查令需受宪法保护](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10 [技术]

美国最高法院裁定，允许执法部门获取特定区域内所有移动设备位置数据的地理围栏搜查令需要受到第四修正案的保护，即必须基于可能原因并取得搜查令。大法官埃琳娜·卡根撰写了多数意见，认为即使在公共场所，个人对其位置数据也享有合理的隐私期望。 这项里程碑式的裁决为数字隐私树立了重要先例，限制了执法部门通过谷歌等科技公司进行大规模监控的能力。它直接影响科技公司处理位置数据请求的方式，并加强了数百万智能手机用户的隐私保护。 该案件涉及一起银行抢劫案，谷歌向执法部门提供了银行周围 150 米范围内 19 个账户的位置数据，从而识别出嫌疑人。该裁决适用于地理围栏搜查令（也称为反向位置搜查令），自 2016 年以来执法部门已使用数千次。

hackernews · cdrnsf · 6月29日 15:54 · [社区讨论](https://news.ycombinator.com/item?id=48720924)

**背景**: 地理围栏搜查令是一种搜查令，允许执法部门搜索数据库（如谷歌的 Sensorvault），以查找特定时间段内特定地理区域内的所有活跃移动设备。第四修正案保护公民免受不合理的搜查和扣押，最高法院此前已裁定手机位置数据可受该修正案保护。本案将这些保护扩展到地理围栏搜查令的使用，批评者称其为违宪的拉网式搜查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision">US supreme court rules geofence warrants require constitutional privacy protections | US supreme court | The Guardian</a></li>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者讨论了该裁决的影响，一些人指出法院意见中包含了带有来源的事实引用，这被视为积极进展。其他人则质疑类似的隐私保护是否适用于其他监控技术（如 Flock 车牌识别器），还有一些人对巴雷特大法官持少数意见表示惊讶。

**标签**: `#supreme court`, `#geofence warrants`, `#digital privacy`, `#law enforcement`, `#constitutional law`

---

<a id="item-2"></a>
### [特斯拉 FSD v14 Lite 让 HW3 车型获得 HW4 级智驾能力](https://x.com/Tesla_AI/status/2071592820889260101) ⭐️ 9.0/10 [技术]

6 月 29 日，特斯拉发布了 FSD v14 Lite，将 HW4 版 V14 的智能提炼到 HW3 硬件上。此次更新使 HW3 车辆能够直接学习 HW4 的处理方式，解锁此前仅 HW4 拥有的强化学习和离线模型能力。 这是一个重要的里程碑，因为它将先进的自动驾驶能力扩展到数百万现有 HW3 车辆，无需硬件升级。同时，首次引入停车、出库和倒车功能，标志着 FSD 操作域的重大扩展。 该更新改进了导航、并线、行人交互、交通灯处理和车辆切入等场景，同时减少了错误减速并优化了转向平顺性。用户现在可以预设停车场、街道、车道或路边等停车目的地，速度配置文件也改为全时段可用以进一步自定义驾驶风格。

telegram · zaihuapd · 6月30日 02:26

**背景**: 特斯拉的全自动驾驶（FSD）是一种高级辅助驾驶系统，采用纯视觉方案，使用八个摄像头以及 Occupancy Network 和 Transformer 等神经网络。HW3 和 HW4 指的是特斯拉 Autopilot 计算机硬件的不同代际，HW4 提供更强的处理能力和更清晰的摄像头画面。强化学习和离线模型是先进的 AI 技术，使系统能够从经验中学习并在无需持续在线更新的情况下改进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/特斯拉自动驾驶">特斯拉自动驾驶 - 维基百科，自由的百科全书</a></li>
<li><a href="https://teslaroamer.com/guides/tesla-hw3-vs-hw4">Tesla HW3 vs HW4 Guide | Tesla Roamer</a></li>
<li><a href="https://www.42how.com/en/article/12329">特斯拉的 FSD 芯片：HW3 和 HW4 - 42 号车库</a></li>

</ul>
</details>

**标签**: `#特斯拉`, `#FSD`, `#自动驾驶`, `#HW3`, `#HW4`, `#技术更新`

---

<a id="item-3"></a>
### [华为开源盘古 2.0 模型，505B/92B 参数，512K 上下文](https://t.me/zaihuapd/42259) ⭐️ 9.0/10 [技术]

在华为开发者大会 2026 上，华为宣布开源 openPangu 2.0 模型，包含 505B 参数的 Pro 版和 92B 参数的 Flash 版，支持 512K 上下文窗口。该模型针对华为昇腾 AI 芯片和鸿蒙系统进行了优化，计划从 6 月 30 日起陆续开源七大组件。 这标志着 AI 格局的重大转变，华为旨在将盘古从中国领先的模型转变为全球竞争力的开源 AI 系统。通过以开源方式发布如此大规模的模型，华为挑战了现有的西方主导的 AI 生态系统，并可能加速依赖国产硬件的行业对 AI 的采用。 该模型提供两种尺寸：505B 参数的 Pro 版用于高端任务，92B 参数的 Flash 版用于更快的推理。512K 上下文长度支持处理极长文档。华为计划陆续开源预训练代码等六个组件，但具体时间表和许可条款仍有待观察。

telegram · zaihuapd · 6月30日 06:01

**背景**: 华为的昇腾 AI 芯片（如昇腾 310、910）是该公司自研的 AI 加速器，旨在与英伟达 GPU 在中国市场竞争。鸿蒙是华为的多设备操作系统，支持物联网、智能手机等。盘古模型系列最早于 2021 年发布，此次开源旨在围绕华为的硬件和软件栈构建生态系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bilibili.com/video/BV1if4y1r7dX/">芯 片 工程师眼中的 华 为 昇 腾 ：地表最强 AI 芯 片 ?_哔哩哔哩_bilibili</a></li>
<li><a href="http://paper.people.com.cn/rmrb/pc/attachement/202412/24/626dbc22-d230-4bcd-9de1-0508a7e8c912.pdf">paper.people.com.cn/rmrb/pc/attachement/202412/24/626dbc22-d230...</a></li>
<li><a href="https://www.21jingji.com/article/20260426/herald/d93c8a9cc14b79b8e7ef74240a9c274a.html">DeepSeek-V4官宣时的这行小字，藏着关键细节 - 21经济网</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#Pangu 2.0`, `#open-source`, `#AI`, `#large language model`, `#昇腾`, `#鸿蒙`

---

<a id="item-4"></a>
### [LongCat-2.0：基于华为昇腾集群训练的 1.6T MoE 模型](https://longcat.chat/blog/longcat-2.0/) ⭐️ 8.0/10 [技术]

LongCat-2.0 是一个大规模混合专家（MoE）模型，总参数量达 1.6 万亿，激活参数量为 480 亿，该模型在数万个 AI ASIC 超级计算节点上训练，很可能使用了华为昇腾 910C 芯片。 该模型证明，在不依赖 Nvidia GPU 的情况下进行大规模 AI 训练是可行的，凸显了中国国产 AI 硬件生态的日益成熟。同时，它也展示了非 Nvidia 集群基础设施工程的重要性。 据报道，该模型复用了 DeepSeek V4 的架构和权重，并且可能与秘密发布的 openrouter/owl-alpha 模型是同一个模型。训练集群由 1024 个华为昇腾超级计算节点组成，相当于约 5 万颗 910C 芯片。

hackernews · benjiro29 · 6月30日 00:30 · [社区讨论](https://news.ycombinator.com/item?id=48727116)

**背景**: 混合专家（MoE）是一种 AI 模型架构，它使用多个专门的子模型（专家）来更高效地处理任务，优于单一的巨型模型。华为昇腾 910C 是在美国出口限制下开发的国产 AI 芯片，其 Atlas 950 超级计算节点每机柜集成 64 个 NPU，可扩展至 8192 个 NPU 以支持大规模训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mljourney.com/mixture-of-experts-moe-models-architecture-and-implementation-guide/">Mixture of Experts (MoE) Models: Architecture and ...</a></li>
<li><a href="https://www.huawei.com/en/news/2026/3/mwc-superpod-ai">Huawei Unveiled the Latest SuperPoD, Making an AI ...</a></li>
<li><a href="https://thamizhelango.medium.com/mindspore-zhipu-ai-huawei-ascend-how-china-built-a-frontier-ai-model-without-a-single-nvidia-68403d92cedb">MindSpore, Zhipu AI & Huawei Ascend : How China Built... | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，真正的新闻是在数万个非 Nvidia ASIC 上进行训练的基础设施成就，有用户估计集群规模约为 5 万颗 910C 芯片。其他人指出，该模型可能复用了 DeepSeek V4 的架构，并且有猜测认为它与过去一个月免费使用的 openrouter/owl-alpha 模型是同一个。

**标签**: `#AI`, `#MoE`, `#LongCat`, `#Huawei Ascend`, `#large language model`

---

<a id="item-5"></a>
### [内存安全上下文切换：setjmp/longjmp 替代方案](https://fil-c.org/context_switches) ⭐️ 8.0/10 [技术]

该文章深入探讨了实现内存安全上下文切换的技术细节，指出了 setjmp/longjmp 和 ucontext 的缺陷，并在 Fil-C 语言中提出了一种更安全的替代方案。 这很重要，因为 setjmp/longjmp 和 ucontext 在系统编程中广泛用于协程、纤程和错误处理，但由于栈帧失效问题，它们本质上是不安全的。Fil-C 的方法可以使上下文切换变得内存安全，从而减少底层代码中的错误和安全漏洞。 文章讨论了 setjmp/longjmp 与寄存器分配和栈溢出交互的复杂性，并指出在 Fil-C 中，除非从祖先栈帧调用，否则 longjmp 会触发 panic。文章还与 Boost fibers 和 ucontext 进行了比较，突出了性能和安全性之间的权衡。

hackernews · modeless · 6月30日 00:38 · [社区讨论](https://news.ycombinator.com/item?id=48727177)

**背景**: 上下文切换允许程序保存和恢复执行状态，在 C 语言中通常使用 setjmp/longjmp 或 ucontext。然而，这些 API 是不安全的，因为它们可能跳转到栈帧已被释放的上下文，导致未定义行为。Fil-C 是 C/C++的一种内存安全实现，它能够将所有内存安全错误捕获为 panic，而本文将该安全性扩展到了上下文切换。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fil-c.org/">Fil - C</a></li>
<li><a href="https://github.com/kaniini/libucontext">GitHub - kaniini/libucontext: ucontext implementation ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论对文章的深度表示赞赏，matheusmoreira 希望自己能更早读到这篇文章。anitil 指出管理栈就是管理内存，因此 Fil-C 在这方面有所贡献。nanolith 提供了与 Boost fibers 和 ucontext 性能的技术比较，而 toast0 指出了文章中可能存在的措辞错误。

**标签**: `#memory safety`, `#context switching`, `#setjmp`, `#longjmp`, `#ucontext`, `#systems programming`, `#Fil-C`

---

<a id="item-6"></a>
### [火箭实验室收购铱星](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully) ⭐️ 8.0/10 [技术]

火箭实验室于 2025 年 6 月 29 日宣布，将以现金加股票方式收购铱星通信公司，交易价值约 80 亿美元，企业价值约 80 亿美元。该交易已获双方董事会批准，预计 2027 年年中完成，尚需股东和监管批准。 此次收购打造了一家集发射服务、卫星制造和盈利卫星网络（含宝贵 L 波段频谱）于一体的全集成太空公司。它模仿了 SpaceX 的 Starlink 策略，即通过卫星运营来保证基础发射量，可能重塑卫星通信市场格局。 铱星运营着 66 颗活跃的低地球轨道卫星，提供包括两极在内的全球覆盖，拥有超过 255 万活跃订阅用户。2025 年，铱星营收 8.717 亿美元，运营 EBITDA 为 4.95 亿美元（利润率 57%）。火箭实验室获得了铱星的 L 波段频谱权，并为其 Neutron 和 Electron 火箭锁定了稳定客户。

hackernews · everfrustrated · 6月29日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=48719485)

**背景**: 铱星星座最初由摩托罗拉开发，自 1998 年投入运营，通过 66 颗带有星间链路的低轨卫星提供全球语音和数据服务。卫星通信频谱权稀缺且宝贵，因为它能在不依赖地面基础设施的情况下实现全球连接。火箭实验室成立于新西兰，现总部位于美国，提供小型和中型运载火箭（Electron 和 Neutron），并通过其子公司制造卫星。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Iridium_satellite_constellation">Iridium satellite constellation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Iridium_Communications">Iridium Communications - Wikipedia</a></li>
<li><a href="https://www.wfw.com/articles/spectrum-rights-and-orbital-positions-what-do-space-operators-need-to-know/">Spectrum rights and orbital positions: what do space operators need...</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极，用户指出这与 SpaceX 的 Starlink 策略相似，可作为发射需求对冲，并称赞 Peter Beck 的收购是明智之举。部分人担忧太空垃圾增加和更多卫星对环境的影响，也有人质疑火箭实验室从新西兰迁至美国的转变。

**标签**: `#Rocket Lab`, `#Iridium`, `#space`, `#acquisition`, `#satellite`, `#launch`

---

<a id="item-7"></a>
### [韩国将投入 1 万亿美元用于存储芯片和人形机器人](https://arstechnica.com/ai/2026/06/south-korea-to-spend-1t-on-more-memory-chip-production-and-humanoid-robots/) ⭐️ 8.0/10 [技术]

韩国宣布了一项 1 万亿美元的投资计划，其中 5850 亿美元用于新建存储芯片半导体制造厂，其余资金用于人形机器人开发。这是近年来规模最大的政府主导技术投资之一。 这项投资可能大幅增加全球存储芯片供应，有望缓解短缺，但也带来大宗商品产能过剩的风险。同时对人形机器人的投入表明韩国押注未来机器人产业，但人形形态的实用性仍存在激烈争议。 该计划包括专门用于新建晶圆厂的 5850 亿美元，晶圆厂是制造集成电路的工厂。剩余资金针对人形机器人开发，批评者质疑模仿人体解剖结构是否是最有效的设计。

hackernews · jnord · 6月29日 22:21 · [社区讨论](https://news.ycombinator.com/item?id=48726102)

**背景**: 半导体制造厂（fab）是生产集成电路（即微芯片）的工厂。存储芯片是电子产品必需的大宗商品，韩国是其主要生产国。人形机器人被设计用于在人类建造的环境中移动和互动，但其形态因人体存在已知的低效性而备受争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Semiconductor_fabrication_plant">Semiconductor fabrication plant - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Humanoid_robot">Humanoid robot - Wikipedia</a></li>
<li><a href="https://sixdegreesofrobotics.substack.com/p/the-human-form-is-flawed-so-why-do">The Human Form Is Flawed, So Why Do We Want Humanoid Robots?</a></li>

</ul>
</details>

**社区讨论**: 评论者将存储芯片比作生活必需品，将人形机器人比作投机性的舞蹈课，凸显了机器人投资的不确定性。还有人警告，急于建厂可能导致产能过剩，而几位评论者质疑为何优先选择人形形态而非更高效的设计。

**标签**: `#semiconductors`, `#humanoid robots`, `#South Korea`, `#investment`, `#technology policy`

---

<a id="item-8"></a>
### [深入解析：CUDA 内核从 CPU 到 GPU 的完整启动路径](https://fergusfinn.com/blog/what-happens-when-you-run-a-gpu-kernel/) ⭐️ 8.0/10 [技术]

一篇深度文章详细解释了启动 CUDA 内核背后的硬件和驱动机制，涵盖了门铃寄存器、队列管理描述符（QMD）以及线程束调度。 这篇文章填补了典型 CUDA 解释中的一个关键空白，通常只讲到内核、块和线程束，而没有覆盖从 CPU 到驱动再到 GPU 的路径。理解这一路径有助于开发者优化性能并调试底层问题。 文章详细介绍了使用门铃寄存器通知 GPU 有新任务，并描述了保存内核参数和启动配置的 QMD 格式。还解释了 GPU 的线程束调度器如何选择符合条件的线程束来执行。

hackernews · mezark · 6月29日 13:11 · [社区讨论](https://news.ycombinator.com/item?id=48718863)

**背景**: CUDA 内核启动涉及 CPU 通过驱动程序向 GPU 发送命令，驱动程序写入门铃寄存器并将队列管理描述符（QMD）放入内存。GPU 的流式多处理器（SM）随后调度线程束（每组 32 个线程）来执行内核。线程束调度器快速在线程束之间切换以隐藏内存延迟，这是 GPU 架构的一个关键特性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html">2.3. Writing SIMT Kernels — CUDA Programming Guide</a></li>
<li><a href="https://modal.com/gpu-glossary/device-hardware/warp-scheduler">What is a Warp Scheduler? | GPU Glossary</a></li>
<li><a href="https://stevengong.co/notes/Streaming-Multiprocessor">Streaming Multiprocessor (SM)</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞文章澄清了门铃和 QMD 机制，有人指出它将 CUDA 语法与实际 GPU 提交联系起来。另一人赞赏关于线程束资格和默认流中隐式同步的解释。还有评论者推测了内核优化公司与开源解决方案的未来。

**标签**: `#CUDA`, `#GPU`, `#kernel launch`, `#hardware`, `#NVIDIA`, `#HPC`

---

## 社会热点 (Social Hotspots)

<a id="item-9"></a>
### [韩红宣布即日起退出公益行业](https://weibo.com/1887344341/R6uN2bm9Z) ⭐️ 7.0/10 [社会热点]

知名歌手、慈善家韩红在微博上宣布，即日起退出公益行业。 作为在救灾和扶贫领域长期活跃的高知名度公众人物，韩红的突然退出可能引发公众对中国公益事业面临的挑战和可持续性的广泛讨论。 该声明仅通过她个人微博账号发布了一条简短内容，未提供任何进一步解释或说明。

telegram · zaihuapd · 6月30日 04:47

**背景**: 韩红是中国最知名的明星慈善家之一，于 2012 年创立了韩红爱心慈善基金会，并领导了包括新冠疫情期间在内的多次救灾行动。她的基金会过去曾面临财务违规的质疑和指控，但她一直否认存在不当行为。

**标签**: `#韩红`, `#公益`, `#退出`, `#社会热点`

---