---
layout: default
title: "Horizon Summary: 2026-08-02 (ZH)"
date: 2026-08-02
lang: zh
---

> 从 74 条内容中筛选出 12 条重要资讯。

---

#### AI 探索 (AI)
8. [如何让 GPU 不再闲置：AI 基础设施效率革命](#item-8) ⭐️ 8.0/10 [技术]

#### 产品专栏 (Product Management)
1. [开源鸿蒙下半场：嵌入式 AI 硬件成为核心机遇](#item-1) ⭐️ 8.0/10 [产品经理]
2. [Kimi K3 开放权重，AI 竞争转向成本、工作流与安全](#item-2) ⭐️ 8.0/10 [产品经理]
3. [Decagon 联合创始人亲述从 2 人到 1000 人的创业历程](#item-3) ⭐️ 8.0/10 [产品经理]
4. [Agent 可观测性：PM 必须懂的三层设计](#item-4) ⭐️ 8.0/10 [产品经理]
5. [模型是电，产品是电器：AI 产品真正的壁垒是数据回路](#item-5) ⭐️ 8.0/10 [产品经理]
6. [Agent 评测实战：别让'感觉还行'毁在上线前](#item-6) ⭐️ 8.0/10 [产品经理]

#### 热搜焦点 (Trending)
7. [一封价值 1100 亿的道歉信](#item-7) ⭐️ 8.0/10 [热搜]
9. [OpenAI 或因投资者担忧推迟 IPO 至明年](#item-9) ⭐️ 8.0/10 [热搜]
10. [全球车企重新调整战略方向](#item-10) ⭐️ 7.0/10 [热搜]
11. [库克最会赚的钱，继任未必收得到](#item-11) ⭐️ 7.0/10 [热搜]
12. [安慰人成为暴利行业](#item-12) ⭐️ 7.0/10 [热搜]

---

## AI 探索 (AI)

<a id="item-8"></a>
### [如何让 GPU 不再闲置：AI 基础设施效率革命](https://www.tmtpost.com/8088046.html) ⭐️ 8.0/10 [技术]

本文探讨了如何通过 NVIDIA 多实例 GPU（MIG）和时间切片等技术，最大化 AI 基础设施中的 GPU 利用率，从而挖掘硅片的极限性能。 随着 AI 工作负载的快速增长，高效的 GPU 利用率对于降低基础设施成本和提高吞吐量至关重要，因此这一分析对数据中心和 AI 公司具有重要价值。 MIG 提供硬件级别的分区和强隔离性，而时间切片则提供灵活的共享但隔离性较弱，各自适用于不同的工作负载类型。

rss · 钛媒体 · 8月1日 08:19

**背景**: GPU 对于 AI 训练和推理至关重要，但由于工作负载的波动性，它们常常未被充分利用。NVIDIA 多实例 GPU（MIG）等技术允许将单个 GPU 分割成多个隔离的实例，从而提高利用率。时间切片则允许多个工作负载随时间共享一个 GPU，但隔离性较差。优化 GPU 利用率是降低 AI 基础设施成本和提高效率的关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud-atlas.readthedocs.io/zh-cn/latest/kvm/iommu/mig/intro_mig.html">NVIDIA Multi - Instance GPU ( MIG ) 技 术 简介 — Cloud Atlas: Discovery...</a></li>
<li><a href="https://www-nvidia-cn.nproxy.org/technologies/multi-instance-gpu/">多实例 GPU ( MIG ) | NVIDIA</a></li>
<li><a href="https://www.eechina.com/thread-904181-1-1.html">Gartner发布塑造 AI ...</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#GPU utilization`, `#efficiency`, `#silicon`, `#technology`

---

## 产品专栏 (Product Management)

<a id="item-1"></a>
### [开源鸿蒙下半场：嵌入式 AI 硬件成为核心机遇](https://www.woshipm.com/share/6438539.html) ⭐️ 8.0/10 [产品经理]

开源鸿蒙进入发展下半场，重心从系统移植适配转向嵌入式 AI 硬件开发，利用其分布式架构、轻量化内核和开源优势。 这一转变使得嵌入式设备能够本地处理 AI，减少对云端的依赖和延迟，同时满足国产化采购需求，为差异化硬件产品创造新市场。 OpenHarmony 6.1 LTS 作为稳定基线，原生支持 RISC-V 和 ARM 芯片。分布式软总线实现设备无缝协作，但成功需要深度 AI 集成，而非仅仅移植系统。

rss · 人人都是产品经理 · 8月1日 05:53

**背景**: 开源鸿蒙（OpenHarmony）是开放原子开源基金会旗下的开源操作系统，专为物联网和嵌入式设备设计。它具备分布式软总线实现设备互联，轻量化内核（LiteOS）适用于低功耗设备，以及统一驱动框架（HDF）方便硬件适配。向嵌入式 AI 硬件的转变利用这些能力，为边缘设备带来本地智能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/716011047">OpenHarmony-HDF驱动框架介绍及加载过程分析 - 知乎</a></li>
<li><a href="https://zh.wikipedia.org/zh-cn/LiteOS">LiteOS - 维基百科，自由的百科全书</a></li>
<li><a href="https://segmentfault.com/a/1190000046431051">segmentfault.com/a/1190000046431051</a></li>

</ul>
</details>

**标签**: `#开源鸿蒙`, `#OpenHarmony`, `#嵌入式AI`, `#硬件开发`, `#产品战略`, `#市场机遇`

---

<a id="item-2"></a>
### [Kimi K3 开放权重，AI 竞争转向成本、工作流与安全](https://www.woshipm.com/ai/6437339.html) ⭐️ 8.0/10 [产品经理]

7 月 27 日，月之暗面发布了 Kimi K3 的完整模型权重，该模型拥有 2.8 万亿参数、100 万 token 上下文窗口，并支持视觉理解。 此次开放权重将 AI 竞争从模型性能转向三个现实战场：谁能承担推理成本、谁能将模型嵌入真实工作流、谁能为开放能力建立安全边界。 Kimi K3 拥有 2.8 万亿参数、100 万 token 上下文窗口，支持视觉理解。官方 API 定价为缓存命中输入每百万 token 0.30 美元，未命中输入 3.00 美元，输出 15.00 美元，并建议使用 64 个或更多加速器部署。

rss · 人人都是产品经理日榜 · 8月1日 04:48

**背景**: 开放权重意味着模型训练后的参数被发布，用户可以进行推理和微调，但通常不包含训练代码和数据，这与完全开源不同。推理成本是指在生产环境中运行模型的计算开销，成为部署的关键考量。将 AI 嵌入工作流意味着将模型集成到特定业务流程中，以实现可衡量的效率和成果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnet.com/tech/services-and-software/openais-new-models-arent-really-open-what-to-know-about-open-weights-ai/">OpenAI's New Models Aren't Really Open : What to Know... - CNET</a></li>
<li><a href="https://www.nvidia.com/en-us/solutions/ai/inference/balancing-cost-latency-and-performance-ebook/">AI Inference : Balancing Cost , Latency, and Performance | NVIDIA</a></li>
<li><a href="https://www.linkedin.com/pulse/from-hype-habit-embedding-ai-everyday-workflows-salient-process-ublue">From Hype to Habit: Embedding AI in Everyday Workflows</a></li>

</ul>
</details>

**标签**: `#Kimi K3`, `#AI competition`, `#open weights`, `#product management`, `#cost`, `#workflow`, `#security`

---

<a id="item-3"></a>
### [Decagon 联合创始人亲述从 2 人到 1000 人的创业历程](https://www.woshipm.com/share/6438526.html) ⭐️ 8.0/10 [产品经理]

在 a16z 的一场活动中，Decagon 联合创始人 Ashwin Sreenivas 讲述了公司从两人公寓起步到如今 500 多人团队的早期历程，并分享了客户发现、团队建设和产品开发的关键决策。 这一亲身经历为产品经理和创业者提供了宝贵的经验，展示了如何在竞争激烈的 AI 客服领域验证想法、找到产品市场契合点并扩展团队。 创始人特意瞄准有预算且见多识广的买家，使用特定的提问技巧来发现真实优先级。他们在获得三个愿意支付 8 万美元的客户后才开始构建产品，并通过资源限制自然过滤非必要工作，保持了以客户为中心的文化。

rss · 人人都是产品经理 · 8月1日 04:08

**背景**: Decagon 是一家企业级 AI 客服代理公司，服务于航空公司、电信运营商和银行等大型客户。两位联合创始人在 a16z 的一次活动中相识，因共同的创业经历和专注于单一客户群体的想法而合作。他们最初不愿进入拥挤的聊天机器人市场，但在意识到客服问题仍未得到解决后进行了转型。

**标签**: `#AI客服`, `#创业`, `#产品经理`, `#Decagon`, `#团队建设`, `#产品开发`

---

<a id="item-4"></a>
### [Agent 可观测性：PM 必须懂的三层设计](https://www.woshipm.com/ai/6435165.html) ⭐️ 8.0/10 [产品经理]

一篇文章提出了 AI Agent 系统的三层可观测性框架，强调 Trace 链路、决策日志和 Token 消耗可视化，以避免黑盒问题。 随着 AI Agent 变得越来越复杂和自主，可观测性对于调试、成本控制和信任至关重要。该框架为产品经理提供了实用指南，以避免技术债务并确保系统可靠性。 该框架包括三个层次：具有唯一步骤 ID 和毫秒时间戳的 Trace 链路、捕获 Agent 推理过程的决策日志，以及用于成本和异常检测的 Token 消耗监控。分级采样策略平衡了存储成本、隐私和噪音。

rss · 人人都是产品经理日榜 · 8月1日 03:06

**背景**: AI Agent 是使用大语言模型自主规划和执行任务的系统，其执行路径是动态生成的。可观测性在此背景下超越了传统日志，包括追踪整个执行链、捕获 Agent 的内部推理（决策日志），以及监控 Token 消耗作为成本和健康指标。LangSmith 和 Langfuse 等工具可以自动捕获这些追踪信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agent-trace.dev/">Agent Trace</a></li>
<li><a href="https://www.tmogroup.com.cn/insights/ai-agents-explained/">AI Agent工作原理：如何连接数据、决策与行动，助力企业数字化转型？ - TMO Group</a></li>
<li><a href="https://juejin.cn/post/7644822313693577254">token 与tokenpony...</a></li>

</ul>
</details>

**标签**: `#可观测性`, `#Agent`, `#产品经理`, `#日志追踪`, `#AI产品`

---

<a id="item-5"></a>
### [模型是电，产品是电器：AI 产品真正的壁垒是数据回路](https://www.woshipm.com/ai/6437579.html) ⭐️ 8.0/10 [产品经理]

月之暗面于 2026 年 7 月 27 日开源了 Kimi K3 模型，该模型拥有 2.8 万亿参数，支持视觉理解和百万词元上下文。文章指出，随着开源模型能力逼近闭源，AI 产品必须通过数据回路和工作流嵌入来构建护城河，而非仅仅依赖模型能力。 这为 AI 产品经理提供了战略框架，强调在模型能力商品化的趋势下，数据回路和工作流嵌入成为关键差异化因素。文章通过 Jasper 的衰落和 Cursor 的崛起等实例，揭示了 AI 产品真正的生存法则。 文章指出，Kimi K3 的整体表现仍落后于 OpenAI 和 Anthropic 最强的闭源模型，但对多数产品场景而言差距已不可感知。此外，英伟达计划五年投入 260 亿美元用于开放权重模型研发，推理成本两年内下降超过 95%。

rss · 人人都是产品经理日榜 · 8月1日 02:28

**背景**: Kimi K3 是月之暗面开发的大型语言模型，拥有 2.8 万亿参数，是最大的开源权重模型之一。开源 AI 模型正在迅速进步，部分模型在众多应用场景中已能与闭源模型匹敌。文章提出了'数据回路'概念——即用户互动持续改进产品——作为可持续的竞争优势，与仅仅封装现有 AI 能力的模式形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_K3">Kimi K3</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**标签**: `#AI product management`, `#data loop`, `#workflow embedding`, `#competitive moat`, `#open source models`, `#Kimi K3`, `#product strategy`

---

<a id="item-6"></a>
### [Agent 评测实战：别让'感觉还行'毁在上线前](https://www.woshipm.com/evaluating/6436624.html) ⭐️ 8.0/10 [产品经理]

本文从产品经理视角出发，结合实战经验，系统化地拆解了 AI Agent 评测框架的构建方法，包括类型划分、指标定义和评测集设计，以解决非确定性、黑盒化和错误级联等核心难题。 随着 AI Agent 在生产环境中越来越普及，建立严格的评测框架对于确保可靠性和避免代价高昂的故障至关重要。本文为产品经理提供了可落地的策略，将不稳定的智能行为收敛为可发布的工程质量。 该框架将 Agent 分为六种类型并定制指标，定义了三级指标体系（P0 上线门禁、P1 版本对比、P2 体验优化）。它强调从单轮、整段会话、执行轨迹和业务结果四个层面进行评测，而非仅看单轮平均分。

rss · 人人都是产品经理日榜 · 8月1日 01:48

**背景**: AI Agent 与传统软件不同，具有非确定性——相同输入可能每次产生不同输出。它们也是'黑盒'系统，内部推理过程不透明，且错误会随着 Agent 调用工具和修改系统状态而级联放大。传统的单元测试等方法已不足以应对这些挑战。本文借鉴了 Anthropic 等机构的评测方法论，从产品经理视角提供了系统化评测的实践指南。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.woshipm.com/ai/6324676.html">AI 产品经理必读：Anthropic 万字长文拆解， Agent ...</a></li>
<li><a href="https://www.memexlab.ai/zh-Hans/blog/anthropic-agent-evaluation-guide">Anthropic Agent 评 估指南读后感：你的 Agent 真的变好了吗</a></li>
<li><a href="https://m.aitntnews.com/newDetail.html?newId=21467">一文搞懂 Agents 评 测 丨Anthropic 最新万字长文</a></li>

</ul>
</details>

**标签**: `#Agent评测`, `#AI产品经理`, `#质量保障`, `#产品管理`

---

## 热搜焦点 (Trending)

<a id="item-7"></a>
### [一封价值 1100 亿的道歉信](https://www.huxiu.com/article/4880007.html?f=rss) ⭐️ 8.0/10 [热搜]

一封高调的道歉信据称造成了 1100 亿元的损失，该信件的发布正在中国社交媒体和商业圈引发广泛讨论。 这一事件凸显了中国企业丑闻或监管行动所涉及的巨大财务风险，并突显了公众舆论对企业行为和市场动态日益增长的影响力。 这封道歉信与一次重大财务损失有关，可能是市值下跌或监管罚款，并且它已成为微博等平台上的热门话题。

rss · 虎嗅 · 8月1日 16:40

**背景**: 在中国，企业领导人在重大事件后有时会发布高调的道歉信，以应对公众抗议或监管压力。1100 亿元的数字可能指的是该事件的总经济影响，例如股价暴跌或巨额罚款。此类道歉通常旨在恢复信任并减轻进一步损害。

**标签**: `#apology`, `#corporate`, `#finance`, `#trending`, `#China`

---

<a id="item-9"></a>
### [OpenAI 或因投资者担忧推迟 IPO 至明年](https://36kr.com/newsflashes/3920415886061193?f=rss) ⭐️ 8.0/10 [热搜]

据报道，OpenAI 可能将其 IPO 推迟到明年，原因是投资者对其现金消耗速度过快表示担忧，同时竞争对手 Anthropic 正在加速其 IPO 计划。 这一动态凸显了投资者对 AI 初创公司财务可持续性的日益关注，以及 AI 行业竞争的加剧，可能重塑 AI 公司估值和上市格局。 Anthropic 的营收增长和估值近期已超过 OpenAI，并正在加速秋季 IPO 计划，已开始与潜在投资者会面。OpenAI 最初希望抢在 Anthropic 之前上市，但现在可能推迟到明年。

rss · 36氪 · 8月1日 04:45

**背景**: OpenAI 是 ChatGPT 的创建者，也是一家领先的 AI 研究机构。Anthropic 是由前 OpenAI 员工创立的竞争对手 AI 初创公司，以其 Claude AI 模型闻名。IPO（首次公开募股）是私营公司首次向公众出售股票的行为，通常用于筹集资金。投资者对现金消耗速度和竞争的担忧是影响 IPO 时机的常见因素。

**标签**: `#OpenAI`, `#IPO`, `#Anthropic`, `#competition`, `#investor concerns`

---

<a id="item-10"></a>
### [全球车企重新调整战略方向](https://www.huxiu.com/article/4880010.html?f=rss) ⭐️ 7.0/10 [热搜]

全球汽车制造商正在根据不断变化的市场条件和技术进步（如电动汽车和自动驾驶的兴起）调整其战略重点。 这一重新调整反映了汽车行业的根本性变革，影响着全球供应链、投资决策和竞争格局。 文章强调，汽车制造商正在重新评估其在电气化、软件集成和市场扩张方面的策略，但未提及具体公司名称或详细战略。

rss · 虎嗅 · 8月1日 23:09

**背景**: 汽车行业正经历从内燃机向电动动力系统的重大转型，这一转变受到环保法规和消费者偏好变化的推动。此外，软件定义汽车和新型出行服务正在重塑传统商业模式。这一背景解释了为何汽车制造商感到有必要重新调整其战略。

**标签**: `#automotive`, `#industry trends`, `#strategy`, `#global`

---

<a id="item-11"></a>
### [库克最会赚的钱，继任未必收得到](https://www.huxiu.com/article/4879960.html?f=rss) ⭐️ 7.0/10 [热搜]

一篇分析指出，苹果公司利润丰厚的 App Store 佣金模式正面临全球监管和竞争的双重挑战，可能危及未来的收入来源。 这很重要，因为 App Store 佣金是苹果重要的利润来源，任何削弱都可能严重影响其财务表现和商业模式，也反映了全球科技监管的趋势。 关键细节包括欧盟《数字市场法案》要求苹果允许侧载，以及来自开发者和政府要求降低佣金率的压力日益增大。

rss · 虎嗅 · 8月1日 23:00

**背景**: 苹果 App Store 对大多数交易收取 30%的佣金，这一模式一直备受批评。近年来，该模式在全球面临法律和监管挑战，例如 Epic Games 诉讼和欧盟新规。文章暗示，未来的苹果 CEO 可能无法维持这一收入来源。

**标签**: `#Apple`, `#App Store`, `#commission fees`, `#regulation`, `#Tim Cook`, `#business model`

---

<a id="item-12"></a>
### [安慰人成为暴利行业](https://www.huxiu.com/article/4880009.html?f=rss) ⭐️ 7.0/10 [热搜]

这篇文章分析了情感安慰服务如何演变成一个高利润行业，利用人们的心理痛苦和孤独感来盈利。 这凸显了情感支持被商品化的趋势，引发了对剥削和心理健康货币化伦理的担忧。 文章可能讨论了付费情感支持的各种形式，如在线倾听服务和类似治疗的平台，以及驱使人们为安慰付费的心理机制。

rss · 虎嗅 · 8月1日 22:38

**背景**: 情感安慰作为一种服务随着数字平台的兴起而出现，人们可以付费获得共情倾听或建议。这是更广泛的“注意力经济”和人类情感货币化的一部分。“痛苦税”一词指的是人们为寻求情感痛苦缓解而持续付出的代价。

**标签**: `#emotional comfort`, `#monetization`, `#mental health`, `#trending topic`, `#business analysis`

---