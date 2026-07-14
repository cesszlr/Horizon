---
layout: default
title: "Horizon Summary: 2026-07-14 (ZH)"
date: 2026-07-14
lang: zh
---

> 从 240 条内容中筛选出 19 条重要资讯。

---

#### Tech
7. [无需打开 Xcode 即可构建和发布 Mac/iOS 应用](#item-7) ⭐️ 8.0/10 [技术]
10. [苹果 SpeechAnalyzer API：速度超越 Whisper，准确度略低](#item-10) ⭐️ 7.0/10 [技术]
11. [世嘉 CD 游戏 Silpheed 的艺术与工程](#item-11) ⭐️ 7.0/10 [技术]
12. [Telegram 的 t.me 域名被暂停，引发技术和法律讨论](#item-12) ⭐️ 7.0/10 [技术]
13. [三星健康应用：拒绝 AI 训练将删除数据](#item-13) ⭐️ 7.0/10 [技术]
14. [开放数据在 Climate.gov 关闭后保存了数据](#item-14) ⭐️ 7.0/10 [技术]
15. [对 15 款电子垃圾 GPU 进行现代 AI 工作负载基准测试](#item-15) ⭐️ 7.0/10 [技术]
16. [Oh My HuggingFace：开源 Hugging Face 桌面客户端](#item-16) ⭐️ 7.0/10 [技术]
17. [Vibe Animation：开源的自然语言 GSAP 动画生成工具](#item-17) ⭐️ 7.0/10 [技术]
19. [MiniRouter：智能 AI 模型路由，平衡成本与性能](#item-19) ⭐️ 7.0/10 [技术]

#### Politics
1. [美国对伊朗发动新一轮空袭，恢复海上封锁](#item-1) ⭐️ 10.0/10 [时政]
2. [美国与伊朗在霍尔木兹海峡互发袭击](#item-2) ⭐️ 10.0/10 [时政]
3. [美国连续第二晚空袭伊朗](#item-3) ⭐️ 10.0/10 [时政]
4. [美国对伊朗发动第二夜空袭](#item-4) ⭐️ 10.0/10 [时政]
5. [昂山素季生死未卜](#item-5) ⭐️ 9.0/10 [时政]
6. [中国拘留研究朝鲜核试验的美国地震学家](#item-6) ⭐️ 9.0/10 [时政]

#### Social Hot Topics
8. [中国十五五规划获批，Meta 追加 400 亿美元数据中心投资，字节跳动否认智能驾驶](#item-8) ⭐️ 8.0/10 [社会热点]
9. [从原料到算力核按钮：稀土如何改写全球半导体利润格局？](#item-9) ⭐️ 8.0/10 [社会热点]
18. [AI 编程时代，基础学习过时了吗？](#item-18) ⭐️ 7.0/10 [社会热点]

---

## Tech

<a id="item-7"></a>
### [无需打开 Xcode 即可构建和发布 Mac/iOS 应用](https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/) ⭐️ 8.0/10 [技术]

一位开发者展示了如何完全通过命令行使用 xcodebuild、altool 和 notarytool 等工具构建、签名和公证 Mac 和 iOS 应用，而无需启动 Xcode。 这种工作流使开发者能够将 Apple 平台构建集成到 CI/CD 流水线中，自动化发布，并使用编码代理或 LLM 进行开发，从而可能提高生产力和灵活性。 该方法依赖于 Apple 的命令行工具，如用于构建的 xcodebuild，以及用于代码签名和公证的 notarytool（自 2023 年 11 月起已取代已弃用的 altool）。第三方工具如 xtool 和 strudel 通过封装这些命令进一步简化了流程。

hackernews · speckx · 7月13日 18:22 · [社区讨论](https://news.ycombinator.com/item?id=48896665)

**背景**: Xcode 是 Apple 用于 macOS 和 iOS 开发的集成开发环境 (IDE)，但它体积庞大且不适合自动化。Apple 提供了命令行工具，如 xcodebuild 和 notarytool，允许在没有图形界面的情况下构建、测试和公证应用。这种工作流对于持续集成 (CI) 系统以及偏好终端或 AI 辅助工作流的开发者特别有用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.apple.com/library/archive/technotes/tn2339/_index.html">Technical Note TN2339: Building from the Command Line with Xcode...</a></li>
<li><a href="https://developer.apple.com/documentation/technotes/tn3147-migrating-to-the-latest-notarization-tool">TN3147: Migrating to the latest notarization tool | Apple ...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论既充满热情也保持谨慎。一些开发者分享了替代工具，如 xtool（用于在 Linux 上构建 iOS 应用）和 strudel（用于签名/公证的 CLI），而另一些人则对在沙箱外运行编码代理表示安全担忧，引用了 xAI 上传用户主目录等事件。总体而言，大家对这种工作流的潜力持积极态度，但也强烈呼吁注意安全。

**标签**: `#Xcode`, `#iOS development`, `#Mac development`, `#CLI`, `#developer tools`, `#security`

---

<a id="item-10"></a>
### [苹果 SpeechAnalyzer API：速度超越 Whisper，准确度略低](https://get-inscribe.com/blog/apple-speech-api-benchmark.html) ⭐️ 7.0/10 [技术]

苹果在 iOS 26 和 macOS 26 中推出的新 SpeechAnalyzer API，与 OpenAI 的 Whisper 及之前的 SFSpeechRecognizer 进行了基准测试。结果显示，SpeechAnalyzer 的运行速度比 Whisper Small 快三倍，在 LibriSpeech 上准确度更高，但略逊于 Whisper Large-V2 等更大模型。 这一基准测试意义重大，因为苹果的本地 SpeechAnalyzer API 为基于云或第三方的语音识别提供了有竞争力的替代方案，可能减少对 Whisper 等服务的依赖。它可能重塑苹果平台上的转录应用格局，尤其适用于实时转录场景。 值得注意的是，苹果的新 SpeechAnalyzer API 缺少旧版 SFSpeechRecognizer 中的自定义词汇功能，该功能允许开发者提高特定关键词的准确度。基准测试在 LibriSpeech 数据集上进行，评估了清晰和嘈杂语音的表现。

hackernews · get-inscribe · 7月13日 16:06 · [社区讨论](https://news.ycombinator.com/item?id=48894752)

**背景**: Whisper 是 OpenAI 开发的开源自动语音识别（ASR）模型，以其跨语言和口音的鲁棒性而闻名。苹果之前的语音识别 API SFSpeechRecognizer 在 iOS 10 中引入，现已被 iOS 26 中的 SpeechAnalyzer 和 SpeechTranscriber 取代。本地语音识别具有隐私优势，因为音频数据无需发送到云端。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://get-inscribe.com/blog/apple-speech-api-benchmark.html">Apple 's New Speech API vs Whisper: The First Real Benchmark</a></li>
<li><a href="https://developer-mdn.apple.com/videos/play/wwdc2025/277/">Bring advanced speech -to-text to your app with... - Apple Developer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Whisper_(speech_recognition_system)">Whisper (speech recognition system)</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，虽然 SpeechAnalyzer 速度快且适合实时转录，但 Nvidia 的 Nemotron 和 Parakeet、Mistral 的 Voxtral 以及 Cohere Transcribe 等更新模型被认为是当前最先进的。一些用户担心苹果的原生 API 可能使付费的 Whisper 封装应用过时，而其他用户则分享了实际使用经验和实现。

**标签**: `#Apple`, `#SpeechAnalyzer`, `#API`, `#Whisper`, `#benchmark`, `#speech recognition`, `#machine learning`

---

<a id="item-11"></a>
### [世嘉 CD 游戏 Silpheed 的艺术与工程](https://fabiensanglard.net/silpheed/index.html) ⭐️ 7.0/10 [技术]

Fabien Sanglard 发表了一篇关于世嘉 CD 游戏《Silpheed》的深入技术分析，揭示了它如何利用预渲染的全动态视频和巧妙的工程技巧来模拟 3D 图形。 这篇分析突显了在硬件严重受限的情况下早期 3D 模拟的巧思，为复古游戏开发提供了宝贵经验，并保存了一段游戏历史。 游戏根据玩家位置循环播放预渲染的帧，这种技术被称为精灵堆叠或 2.5D，因为世嘉 CD 不具备实时 3D 多边形处理能力。

hackernews · ibobev · 7月13日 14:52 · [社区讨论](https://news.ycombinator.com/item?id=48893639)

**背景**: 世嘉 CD 是世嘉 Genesis 的附加组件，使用 CD-ROM，支持全动态视频（FMV）游戏。《Silpheed》是一款射击游戏，利用预渲染图形模拟 3D，这是该平台上众多 FMV 游戏的常见技巧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://asibiont.com/en/blog/iskusstvo-i-inzheneriya-sega-cd-silpheed-kak-vibe-coding-vozrozhdaet-kultovuyu-eru">The Art and Engineering of Sega CD Silpheed ... — ASI Biont Blog</a></li>
<li><a href="https://www.mobygames.com/game/11910/silpheed/">Silpheed (1993) - MobyGames</a></li>
<li><a href="https://www.fmvworld.com/console_segacd.html">Games for Sega CD | FMV Games List - FMV World</a></li>

</ul>
</details>

**社区讨论**: 评论者们对《Silpheed》的技术成就表达了怀旧和惊叹，有人对音频设置提出了修正，并指出这篇文章是重新提交的。总体而言，讨论热烈且对工程细节表示赞赏。

**标签**: `#retro gaming`, `#Sega CD`, `#game development`, `#FMV`, `#engineering`

---

<a id="item-12"></a>
### [Telegram 的 t.me 域名被暂停，引发技术和法律讨论](https://www.whois.com/whois/t.me) ⭐️ 7.0/10 [技术]

Telegram 用于短链接的 t.me 域名已被暂停，WHOIS 记录显示其状态代码包括 clientHold 和 clientRenewProhibited。 此次暂停影响了数百万依赖 t.me 链接访问频道和机器人的 Telegram 用户，并引发了对该平台在面临多项法律调查时依赖 GoDaddy 作为注册商的担忧。 根据 ICANN 的 EPP 状态代码，诸如 clientRenewProhibited 和 serverDeleteProhibited 等域名状态代码通常用于法律纠纷或域名面临删除的情况。

hackernews · Tiberium · 7月13日 19:52 · [社区讨论](https://news.ycombinator.com/item?id=48897878)

**背景**: Telegram 是一款于 2013 年推出的基于云的即时通讯服务，以其对隐私和安全的关注而闻名。t.me 域名用于生成重定向到 Telegram 聊天、频道或机器人的短链接。域名暂停可能由多种原因引起，包括 ICANN 验证失败、滥用举报或法律行动。注册商 GoDaddy 是最大的域名注册商之一，但因缺乏透明度而受到批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Telegram_(software)">Telegram (software) - Wikipedia</a></li>
<li><a href="https://domaindetails.com/kb/troubleshooting/why-domain-suspended">Why Was My Domain Suspended? Causes and Recovery (2025)</a></li>
<li><a href="https://www.namecheap.com/support/knowledgebase/article.aspx/10626/46/why-has-my-domain-been-suspended/">Why has my domain been suspended? - Domains - Namecheap.com</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的社区评论对 Telegram 使用 GoDaddy 作为注册商表示惊讶，并猜测此次暂停可能与印度、俄罗斯或法国的法律调查有关。一些用户指出了域名状态代码的技术含义，并分享了使用 telegram.me 等替代方案。

**标签**: `#Telegram`, `#domain suspension`, `#ICANN`, `#GoDaddy`, `#legal investigations`

---

<a id="item-13"></a>
### [三星健康应用：拒绝 AI 训练将删除数据](https://neow.in/cWsyMTV3) ⭐️ 7.0/10 [技术]

三星健康应用更新了政策，警告用户如果选择退出允许其数据用于 AI 训练，他们的个人健康数据将从应用中被删除。 这一政策引发了严重的隐私担忧，因为它迫使用户在失去健康数据或允许其敏感医疗信息用于 AI 训练之间做出选择，可能为健康应用的数据实践树立了一个令人担忧的先例。 该政策特别针对四类数据：睡眠、药物、医疗记录和周期追踪详情。选择退出的用户其数据将被删除，实际上使三星健康应用的许多功能无法使用。

hackernews · bundie · 7月13日 20:01 · [社区讨论](https://news.ycombinator.com/item?id=48897991)

**背景**: 三星健康是一款预装在三星 Galaxy 设备上并可在其他 Android 设备上使用的健身和健康追踪应用。它收集用户及其连接设备的各种健康指标。AI 训练涉及使用这些数据来改进算法和功能，但由于健康数据高度敏感，这引发了隐私担忧。该应用的新政策似乎要求用户同意 AI 训练作为将数据存储在三星服务器上的条件。

**社区讨论**: 社区评论对三星的做法表达了强烈不满。用户批评该政策的强制性，有人指出拒绝同意会使设备可用性降低，并质疑是否应获得退款。其他人则强调了应用现有的问题，如广告和损坏的数据导出功能。然而，一些用户看到了积极的一面：如果你拒绝，你的敏感健康数据将被删除且不会用于 AI 训练。

**标签**: `#Samsung Health`, `#AI training`, `#data privacy`, `#data deletion`, `#user consent`

---

<a id="item-14"></a>
### [开放数据在 Climate.gov 关闭后保存了数据](https://werd.io/climate-gov-was-destroyed-open-data-saved-it/) ⭐️ 7.0/10 [技术]

一篇博客文章报道，Climate.gov 被关闭后，开放数据倡议和社区存档努力保存了政府的气候数据，引发了关于去中心化存档和公共数据所有权的讨论。 这一事件凸显了政府数据在政治变动下的脆弱性，并强调了开放数据和去中心化存档对于确保公众获取关键气候信息的重要性。 博客文章描述了志愿者如何使用 IPFS 等工具存档数据，但指出这项工作依赖捐赠而非持续的政府资金。评论者建议政府静态内容默认应发布在 IPFS 上。

hackernews · benwerd · 7月13日 19:57 · [社区讨论](https://news.ycombinator.com/item?id=48897945)

**背景**: Climate.gov 是美国政府提供气候数据和资源的网站。开放数据倡议倡导政府信息免费公开访问。IPFS（星际文件系统）是一种去中心化的文件存储和共享协议，能够实现弹性存档。开放政府倡议通过开放数据政策促进透明度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/InterPlanetary_File_System">InterPlanetary File System - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open_Government_Initiative">Open Government Initiative - Wikipedia</a></li>
<li><a href="https://pinata.cloud/blog/ipfs-as-an-archival-storage-solution/">IPFS As An Archival Storage Solution</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍支持开放数据，并认为政府数据默认应为公共领域。有人提议将 IPFS 作为政府静态内容的默认发布平台。关于资金存在分歧：一位评论者指出依赖捐赠并不理想，另一位则质疑该说法的准确性。

**标签**: `#open data`, `#climate data`, `#government`, `#IPFS`, `#archiving`, `#public domain`

---

<a id="item-15"></a>
### [对 15 款电子垃圾 GPU 进行现代 AI 工作负载基准测试](https://esologic.com/benchmarking-tesla-gpus/) ⭐️ 7.0/10 [技术]

一项针对 15 款老旧 GPU 的详细基准测试发布，评估了它们在现代 AI 和机器学习任务中的可行性。 这项分析为经济实惠的硬件配置提供了实用见解，帮助爱好者和小型团队利用电子垃圾 GPU 进行 AI 工作，而无需购买昂贵的新硬件。 该基准测试涵盖多款老旧 GPU（包括 Tesla 系列），并测量了它们在推理和微调等现代 AI 工作负载上的性能。

hackernews · eso_logic · 7月13日 13:48 · [社区讨论](https://news.ycombinator.com/item?id=48892638)

**背景**: 随着 AI 模型规模扩大，对 GPU 显存和算力的需求增加，但高端 GPU 价格昂贵。将数据中心或矿机中的老旧 GPU 重新利用是一种低成本替代方案，尽管它们可能缺乏 FP8 支持等现代特性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://inteleca.com/high-performance-computing-gpu/">High-Performance Computing (HPC) GPUs in Enterprise IT</a></li>
<li><a href="https://bitproit.com/the-aftermath-of-the-merge/">The Aftermath of the Merge on GPU mining profitability and the GPU ...</a></li>
<li><a href="https://dataforcee.us/2025/12/28/breaking-the-hardware-barrier-software-fp8-for-older-gpus/">Breaking the Hardware Barrier: Software FP8 for Older GPUs</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了各自的经验，一位用户称赞 Tesla P4 功耗低、成本低，另一位则推荐 Radeon Pro V620，因其对 ROCm 支持更好且功能更新。

**标签**: `#GPU`, `#benchmarking`, `#e-waste`, `#AI workloads`, `#hardware`

---

<a id="item-16"></a>
### [Oh My HuggingFace：开源 Hugging Face 桌面客户端](https://www.v2ex.com/t/1227067#reply0) ⭐️ 7.0/10 [技术]

一款名为 Oh My HuggingFace 的开源桌面客户端正式发布，支持断点续传、通过 hf-mirror.com 镜像下载以及缓存可视化清理，覆盖 macOS、Windows 和 Linux 平台。 该工具解决了 Hugging Face 用户的常见痛点，如无法断点续传大文件、缺乏下载管理和缓存占用空间不透明等问题。对于访问 Hugging Face 受限地区的用户尤为实用，因为它原生支持镜像站点。 该客户端基于 Electron 构建，采用严格的安全措施：零遥测、通过系统钥匙串加密 Token、渲染进程完全沙箱化。它兼容 Hugging Face 标准缓存目录，可无缝复用 transformers 和 huggingface-cli 等工具。

rss · V2EX · 7月13日 19:11

**背景**: Hugging Face Hub 是一个托管超过 200 万个模型、150 万个数据集和 AI 应用（Spaces）的平台。用户通常通过浏览器或命令行工具 huggingface-cli 下载模型，但浏览器下载缺乏断点续传和管理功能，缓存目录可能悄无声息地占用数百 GB 磁盘空间。Oh My HuggingFace 提供了一个专用桌面客户端来高效管理这些任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/docs/hub/en/index">Hugging Face Hub documentation · Hugging Face</a></li>
<li><a href="https://hf-mirror.com/">HF-Mirror</a></li>

</ul>
</details>

**标签**: `#开源`, `#Hugging Face`, `#桌面客户端`, `#下载工具`, `#AI`

---

<a id="item-17"></a>
### [Vibe Animation：开源的自然语言 GSAP 动画生成工具](https://www.v2ex.com/t/1227053#reply0) ⭐️ 7.0/10 [技术]

开发者发布了开源工具 Vibe Animation，它利用 Claude Agent 通过自然语言描述生成 GSAP 动画。该工具支持实时预览、选中元素进行定向修改，并可导出为 MP4/GIF/JSON 格式。 Vibe Animation 降低了创建复杂 GSAP 动画的门槛，让非开发者也能通过自然语言描述制作网页动画。其“选中即上下文”机制解决了 AI 在修改特定元素时丢失上下文的常见问题。 该工具使用 Claude Agent SDK 和 MCP 工具来确保 AI 修改受控且安全。它具备真实的 GSAP 时间轴预览、类似 git 的版本树用于历史回滚，以及基于 WebCodecs 和自研编码器的浏览器端导出功能。

rss · V2EX · 7月13日 15:43

**背景**: GSAP（GreenSock Animation Platform）是一个流行的 JavaScript 动画库，用于创建高性能网页动画。Vibe coding 是由 Andrej Karpathy 提出的概念，指通过自然语言描述让 AI 生成代码。Claude 是 Anthropic 开发的 AI 模型，其 Agent SDK 允许构建能与工具和 API 交互的 AI 代理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/greensock/GSAP">GitHub - greensock/ GSAP : GSAP (GreenSock Animation Platform)...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (AI) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#开源`, `#AI`, `#动画`, `#GSAP`, `#Vibe Animation`, `#工具`

---

<a id="item-19"></a>
### [MiniRouter：智能 AI 模型路由，平衡成本与性能](https://www.v2ex.com/t/1227031#reply0) ⭐️ 7.0/10 [技术]

一位程序员开发并开源了 MiniRouter，这是一个智能路由工具，可根据任务难度自动选择 AI 模型，旨在平衡成本与性能。它提供与 OpenAI 和 Anthropic 兼容的统一 API，并支持多渠道切换和使用统计。 该工具解决了 AI API 调用中常见的过度支出问题，通过将简单任务路由到廉价模型、复杂任务路由到更强模型，帮助开发者和团队在不牺牲质量的前提下优化 AI 成本。随着 AI 使用量的增长，这一点变得越来越重要。 MiniRouter 提供自动任务难度评估、统一 API 管理、API 密钥和额度控制，以及 Token、费用和延迟的详细统计。它还能解释每次请求为何选择特定模型，增加了透明度。

rss · V2EX · 7月13日 13:40

**背景**: 许多开发者使用来自不同提供商的多种 AI 模型，每种模型都有不同的成本和能力。如果没有智能路由，他们通常会对所有任务默认使用最强大的模型，导致不必要的开支。像 MiniRouter 这样的模型路由工具会自动按复杂度分类任务，并将其分派到最具成本效益的模型，类似于网络中的负载均衡器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.v2ex.com/t/1227031">最近 token 烧得多了，自己手搓了个智能路由 MiniRouter - V2EX</a></li>
<li><a href="https://blog.csdn.net/weixin_42521558/article/details/161028578">开源AI路由网关free-ai-router：统一管理多模型API，实现智能路由与成...</a></li>
<li><a href="https://cloud.tencent.com/developer/article/2654271">114：多模型Router智能路由策略：根据任务动态选模型节省成本</a></li>

</ul>
</details>

**标签**: `#AI`, `#模型路由`, `#开源`, `#成本优化`, `#V2EX`

---

## Politics

<a id="item-1"></a>
### [美国对伊朗发动新一轮空袭，恢复海上封锁](https://news.google.com/rss/articles/CBMiekFVX3lxTFBBbm13U1h4Tm5zUlRQalhLOVRSUHVvY3VVQ1BOaUotQzl3NTBqVDZzLXpKN190YUk1LTlONkVWaDVwR2hqZU13bEdSdk0tY1gxUmFJSk1OTjB3ZjZhR05YcHVmS252QWdpU3VJb1UxenV5OHdnNm84OWRR?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 10.0/10 [时政]

美国根据特朗普总统的命令，对伊朗发动了新一轮军事空袭，并恢复了海上封锁。这标志着两国之间持续冲突的显著升级。 此次升级可能进一步破坏中东稳定，影响全球石油市场和国际安全。恢复封锁还可能扰乱海上贸易路线，波及全球经济。 此次空袭和封锁是美国对伊朗施压的更广泛战略的一部分，但具体目标和封锁范围尚未详细说明。局势仍不稳定，可能进一步发生军事冲突。

rss · Buzzing News · 7月13日 22:54

**背景**: 美国与伊朗长期存在紧张关系，包括围绕伊朗核计划及地区影响力的争端。特朗普政府此前曾对伊朗实施制裁并采取军事行动，而拜登政府则寻求外交接触。最新举措标志着美国恢复更强硬的立场。

**标签**: `#Iran`, `#US`, `#war`, `#geopolitics`, `#conflict`

---

<a id="item-2"></a>
### [美国与伊朗在霍尔木兹海峡互发袭击](https://news.google.com/rss/articles/CBMibkFVX3lxTFBnVjhScnVheUNnYXhMcjVVRlZuS2RiMGgwQTNxRWxtU1AxWlM1elZTRGxjU0xwVFNwb3A3YkluVzN4WGlsUlVrbmZtT0hwRlVsYnozb2Q1cXhHTXU2QlFyMlNzaHFQUzh1cVVmWW1n?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 10.0/10 [时政]

美国与伊朗在霍尔木兹海峡这一关键国际水道附近互发了军事打击。这标志着两国之间的敌对行动出现了重大且即时的升级。 这场冲突威胁到全球约 20%石油运输所经过的霍尔木兹海峡的自由通航，可能引发全球能源危机。美伊之间的直接军事接触也增加了爆发涉及其他大国的更广泛地区战争的风险。 霍尔木兹海峡连接波斯湾与阿曼湾，是原油和液化天然气的重要运输通道。随着局势的发展，关于此次袭击的具体细节，包括使用的武器和伤亡情况，仍在陆续披露中。

rss · Buzzing News · 7月13日 08:37

**背景**: 由于其对全球能源供应具有战略重要性，霍尔木兹海峡长期以来一直是美伊紧张局势的爆发点。此前的事件包括扣押油轮和袭击航运，但两国之间的直接军事打击代表着一次重大升级。当前的冲突是美伊之间长期地缘政治对抗的一部分，自美国退出伊核协议以来，这种对抗进一步加剧。

**标签**: `#US`, `#Iran`, `#Strait of Hormuz`, `#military conflict`, `#geopolitics`

---

<a id="item-3"></a>
### [美国连续第二晚空袭伊朗](https://news.google.com/rss/articles/CBMibkFVX3lxTE91YV9WLTU4cXN4cjF5RWVKc3lJUlpWQ1BjS2RqUURnTzVRN1VhTUthTjBsdjNHZ1FRam1KMHM3Tkh4ZTJBdlhYZTVXeENUWDVkWnQ2NDBHY2xoZGJSOEtmaEp3Y0M5NTMzbDB5QUl3?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 10.0/10 [时政]

2026 年 7 月 12 日，美国连续第二晚对伊朗发动空袭，进一步加剧了两国间的军事紧张局势。 这标志着美伊冲突的重大升级，可能对地区稳定和国际安全产生全球性影响。 此次空袭是继前一晚攻击后的持续军事行动，具体目标和损失评估尚未公布。

rss · Buzzing News · 7月13日 05:28

**标签**: `#US`, `#Iran`, `#airstrikes`, `#geopolitics`, `#conflict`

---

<a id="item-4"></a>
### [美国对伊朗发动第二夜空袭](https://news.google.com/rss/articles/CBMic0FVX3lxTFBWM2xxSUF3aEVMRDZvd3BaWU1UbnJnd1dHRUxqOS12MzhMbDljeklxNFlMYUxuRkNwQlhSejdMUkVqWWRSY1Vnb25BUi1NalVUcmZIMW1HWDE1eUc3MEEzNlNtLXZsaHdEaDVwQjZaM2U3UHc?oc=5&hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 10.0/10 [时政]

美国连续第二晚对伊朗发动空袭，进一步加剧了两国之间的军事紧张局势。 这标志着美国与伊朗冲突的重大升级，可能对地区稳定和全球安全产生影响。此举表明美国对伊朗军事政策的显著转变。 这些空袭是持续军事行动的一部分，具体目标和地点尚未公布。连续第二晚的打击表明这是一场持续的行动，而非一次性回应。

rss · Buzzing News · 7月13日 03:53

**背景**: 美伊紧张关系已持续多年，根源在于伊朗核计划及其地区影响力等争端。美国此前曾打击伊朗支持的武装力量，但直接对伊朗领土发动空袭标志着重大升级。此为突发新闻，更多细节预计将陆续公布。

**标签**: `#US`, `#Iran`, `#military strikes`, `#geopolitics`, `#conflict`, `#breaking news`

---

<a id="item-5"></a>
### [昂山素季生死未卜](https://www.economist.com/asia/2026/07/13/is-aung-san-suu-kyi-dead) ⭐️ 9.0/10 [时政]

据《经济学人》报道，缅甸被监禁的领导人昂山素季自 2022 年以来从未露面，她的生死状况不明。 作为诺贝尔奖得主和前领导人，昂山素季的命运不明可能影响缅甸的政治稳定和国际关系。 报道指出，昂山素季自 2022 年以来从未露面，官方未提供任何关于她健康状况或下落的信息。

rss · The Economist · 7月13日 13:31

**背景**: 昂山素季是缅甸政治人物和诺贝尔和平奖得主，曾领导缅甸的民主转型。她在 2021 年 2 月军事政变后被军方拘留，此后一直与外界隔绝。她的失踪引起了人权组织和国际社会的担忧。

**标签**: `#Aung San Suu Kyi`, `#Myanmar`, `#politics`, `#detention`, `#uncertainty`

---

<a id="item-6"></a>
### [中国拘留研究朝鲜核试验的美国地震学家](https://news.google.com/read/CBMiuAFBVV95cUxPM2RCTlAtbmVLSG1sQjJCblpURk9nQ2JPWFpoR1dKNWJxQVVZNGpRM1hGSEFKa1VQQy14UnhtcTFOeGswVUhFQXJ3ZWRyekU4NXNzaWhPY2xyN0JoYVg3bnFXTURPSHUyYTZEOUZOWDdIQmZMTVlKV0RHU19qNjRwUDM4NFVZRVp0YnBETnhwWkxKVkpEMHpEY0ZKNEFqdzFQNjlFRE5uMUNyT2hvSXZvc2Q2Q2lIT0l1?hl=en-US&gl=US&ceid=US%3Aen) ⭐️ 9.0/10 [时政]

据路透社独家报道，中国拘留了一名研究朝鲜核试验的美国地震学家。这一事件可能加剧中美之间的外交紧张局势。 这一事件凸显了从事核扩散等敏感课题研究的科学家所面临的地缘政治风险。它还可能影响核试验监测与防扩散方面的国际合作。 该地震学家的身份及具体指控尚未公开。此次拘留似乎是中国以国家安全为由拘留外国公民的更大模式的一部分。

rss · Buzzing China · 7月13日 21:08

**背景**: 地震学家利用地震波来区分地震和爆炸，包括地下核试验。法医地震学是执行《全面禁止核试验条约》（CTBT）的关键技术。国际监测系统在全球设有 150 多个地震台站，用于探测核试验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forensic_seismology">Forensic seismology - Wikipedia</a></li>
<li><a href="https://eos.org/articles/could-seismic-networks-reveal-hard-to-detect-nuclear-tests">Could Seismic Networks Reveal Hard-to-Detect Nuclear Tests? - Eos</a></li>

</ul>
</details>

**标签**: `#China`, `#United States`, `#seismologist`, `#North Korea`, `#nuclear tests`, `#detention`, `#geopolitics`

---

## Social Hot Topics

<a id="item-8"></a>
### [中国十五五规划获批，Meta 追加 400 亿美元数据中心投资，字节跳动否认智能驾驶](https://www.tmtpost.com/8063498.html) ⭐️ 8.0/10 [社会热点]

国务院批复同意《扩大消费'十五五'规划》和《国民健康'十五五'规划》；Meta 宣布追加 400 亿美元投资路易斯安那州数据中心；字节跳动回应没有做智能驾驶业务的计划。此外，阶跃星辰发布全球首款大模型原生智能体手机，苹果调整 Mac 芯片路线图加速 AI 芯片研发，海南确认成为首个禁售燃油车省份。 这些动态表明中国在'十五五'规划下将重点扩大内需和提升国民健康水平，同时科技巨头持续加大对 AI 基础设施和硬件的投入。规划的获批将为 2026-2030 年的国家政策提供指导，企业动向则反映了 AI 和电动汽车转型的加速。 '十五五'规划是 2026-2030 年的初步框架，重点在于扩大消费和国民健康。Meta 的 400 亿美元投资是在此前宣布的 100 亿美元路易斯安那州数据中心基础上的追加。阶跃星辰的智能体手机搭载 Step AOS 系统和 Amoo 智能体，旨在实现模型、软件、硬件三位一体。

rss · 钛媒体 · 7月13日 23:20

**背景**: 中国的五年规划是全面的国家发展战略，为每个五年周期设定经济和社会发展目标。'十五五'规划将接替当前的'十四五'规划，为 2026-2030 年确定优先事项。'大模型原生智能体手机'是一种新型智能手机，它将大型 AI 模型深度集成到操作系统中，使设备能够主动代表用户执行任务和做出决策。海南禁售燃油车与中国 2060 年实现碳中和的目标一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.yicai.com/news/103272786.html">阶跃星辰推出全球首款大模型原生智能体手机</a></li>
<li><a href="https://pitchhub.36kr.com/project/3092185436618760?specialWeb=1&header=hide">阶 跃 星 辰 | 项目信息-36氪</a></li>

</ul>
</details>

**标签**: `#经济形势`, `#十五五规划`, `#国民健康`, `#自然资源`, `#康复辅具`, `#菜鸟供应链`, `#阶跃星辰`, `#苹果Mac芯片`, `#海南禁售燃油车`

---

<a id="item-9"></a>
### [从原料到算力核按钮：稀土如何改写全球半导体利润格局？](https://www.tmtpost.com/8062719.html) ⭐️ 8.0/10 [社会热点]

一篇新分析指出，稀土和算力金属正成为重新定义全球半导体产业链利润分配的关键因素，中国在关键材料供应上的主导地位带来了战略杠杆。 这一转变意义重大，因为稀土和算力金属是 AI 芯片和先进半导体的关键材料，而供应集中在中国可能重塑全球科技竞争、供应链安全和地缘政治格局。 文章重点介绍了镓等‘算力金属’，镓用于氮化镓和砷化镓晶圆以制造高性能芯片。中国控制着全球约 90%的镓供应，近期的出口管制进一步收紧了供应，造成结构性短缺。

rss · 钛媒体 · 7月13日 10:43

**背景**: 稀土和算力金属是半导体制造的关键原材料，尤其是用于 AI 和高性能计算。中国长期以来主导着这些材料的供应链，引发了对依赖性和脆弱性的担忧。随着 AI 基础设施建设推动需求，而供应受地缘政治因素和出口管制制约，‘算力金属’概念受到关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jiuyangongshe.com/a/jsnt21h3hs">13大 算 力 金 属 梳理：一文看懂 算 力 金 属 投资逻辑与核心概念股</a></li>
<li><a href="https://renrenaicang.com/articles/daily-f445a964d29a.html">AI基建催生 算 力 金 属 热潮 供给端硬约束成核心逻辑</a></li>

</ul>
</details>

**标签**: `#rare earth`, `#semiconductor`, `#global supply chain`, `#geopolitics`, `#profit distribution`

---

<a id="item-18"></a>
### [AI 编程时代，基础学习过时了吗？](https://www.v2ex.com/t/1227032#reply11) ⭐️ 7.0/10 [社会热点]

V2EX 上一个讨论帖引发了关于 AI 编程工具是否让学习编程基础变得不必要的辩论。该帖子探讨了程序员在 AI 辅助编程时代应该如何适应。 这场辩论反映了开发者社区的一个关键时刻，随着 GitHub Copilot 等 AI 工具成为主流，其结果可能影响编程教育的方向以及未来开发者应优先掌握的技能。 该讨论发生在 V2EX（一个知名的中文技术社区）上，表明中国开发者社区对此话题的高度关注。帖子中可能包含了从强调基础重要性的资深程序员到高度依赖 AI 工具的新手等多种观点。

rss · V2EX · 7月13日 13:40

**背景**: AI 编程工具，如 GitHub Copilot 和 ChatGPT，可以根据自然语言提示生成代码片段甚至整个函数。这引发了一场辩论：学习传统的编程基础——如算法、数据结构和调试——是否仍然必要。许多人认为，虽然 AI 可以提高生产力，但扎实的基础知识对于有效解决问题和保证代码质量至关重要。另一些人则认为，随着 AI 的改进，对深层编程知识的需求可能会减少，焦点将转向更高层次的设计和提示工程。

**标签**: `#AI programming`, `#programming education`, `#developer debate`, `#V2EX`, `#tech community`

---