---
layout: default
title: "Horizon Summary: 2026-10-23 (ZH)"
date: 2026-10-23
lang: zh
---

> 从 30 条内容中筛选出 6 条重要资讯。

---

**科技新闻**
1. [公共 DNS 解析器 Quad9 宣布退出法国市场](#item-tech-news-1) ⭐️ 8.0/10
2. [Google DeepMind 发布 ForTy 2020 全球森林类型图与时间序列](#item-tech-news-2) ⭐️ 8.0/10

**科技博客**
1. [将数据库状态检查转为强化学习奖励：使用 ThinkingBox 进行智能体后训练](#item-tech-blog-1) ⭐️ 9.0/10
2. [Ensembling IBM Granite Time-Series Models](#item-tech-blog-2) ⭐️ 8.0/10
3. [为什么 AI 算力呈长方形：Modal CEO 谈弹性基础设施与智能时代](#item-tech-blog-3) ⭐️ 7.0/10
4. [PHP 核心漏洞 PHP2Shell 的发现与协同修复](#item-tech-blog-4) ⭐️ 6.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [公共 DNS 解析器 Quad9 宣布退出法国市场](https://quad9.net/news/blog/au-revoir-france/) ⭐️ 8.0/10

公共 DNS 解析器 Quad9 宣布退出法国市场，以应对针对 DNS 解析器执行版权保护网页拦截的法律要求。此前，包括 Canal+ 在内的版权方频繁获取针对体育盗版网站的网页拦截禁令，并将其强加给 Google、Cloudflare 和思科等解析器。Quad9 的 CTO 确认，他们可能在 11 月 24 日之后使用 GeoIP 过滤器阻止法国用户访问其服务，此举凸显了公共 DNS 基础设施在应对版权拦截法律诉讼时面临的严峻合规压力。

hackernews · farrokhi · 10月22日 14:32 · [社区讨论](https://news.ycombinator.com/item?id=50195959)

**「背景」** Quad9 是一个运营公共递归域名服务器的非营利组织，通过任播路由将用户的解析请求引导至最近的服务器，并支持多种加密 DNS 协议以保障隐私安全 \[tool-1-1, tool-1-3\]。近年来，部分法国法院及版权方针对 DNS 解析商发起了一系列网站封锁禁令，要求其对特定侵权或盗版域名实施解析封锁 \[tool-1-2, tool-1-3\]。

**「影响」** 法国用户将无法再使用 Quad9 的公共 DNS 解析服务，这进一步削弱了该地区用户在互联网基础设施层面的隐私和中立选择。

**「社区讨论」** 社区讨论主要集中在对惩罚 DNS 解析器的合理性质疑上，评论者普遍认为这类似于因电话簿列出犯罪分子号码而惩罚电话公司，同时也有人指出此举效仿了两年前思科因类似法律压力退出法国市场的先例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Quad9">Quad 9 - Wikipedia</a></li>
<li><a href="https://quad9.net/news/blog/au-revoir-france/">Farewell, France | Quad 9</a></li>
<li><a href="https://reclaimthenet.org/quad9-considers-leaving-france-over-website-blocking-order">Quad 9 Considers Leaving France Over Website Blocking Order</a></li>

</ul>
</details>

**标签**: `#dns`, `#infrastructure`, `#privacy`, `#law`, `#networking`

---

<a id="item-tech-news-2"></a>
### [Google DeepMind 发布 ForTy 2020 全球森林类型图与时间序列](https://deepmind.google/blog/beyond-tree-cover-mapping-the-worlds-forest-types/) ⭐️ 8.0/10

Google DeepMind 联合 Google Research、世界资源研究所（WRI）及国际应用系统分析研究所（IIASA）发布了森林类型（ForTy）2020 全球地图及 2017 至 2025 年的时间序列数据。该地图基于联合国粮农组织（FAO）的标准，以 10 米分辨率将全球地表划分为原始森林、天然次生林、人工林、人工林场、树木作物与农林复合业以及其他土地等六大类，并在此基础上提供了每年变化的追踪能力。模型训练利用了约 170 万个带标签的位置以及 AlphaEarth Foundations 嵌入数据，经 9000 多个随机位点验证，其森林类型识别准确率达到 90%，森林与非森林分辨准确率为 95%。相关资源已在 Google Earth Engine 上以开放许可形式免费提供。

rss · Google DeepMind · 10月22日 14:30

**「背景」** 传统的全球森林地图主要识别树木覆盖，难以区分具有不同碳储量和生物多样性价值的自然森林与单一树种人工林或农业用地。欧盟新森林砍伐法规（EUDR）等政策要求企业和监管机构不仅需要明确树木的位置，还需要了解其具体的森林类型及采伐后的土地利用变化情况。

**「影响」** 该高分辨率图谱与时间序列数据可帮助政府、企业、研究人员及环保组织更准确地构建无毁林供应链、追踪隐蔽的森林退化并优化全球生态保护决策。

**标签**: `#artificial intelligence`, `#machine learning`, `#geospatial data`, `#open source`, `#environment`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [将数据库状态检查转为强化学习奖励：使用 ThinkingBox 进行智能体后训练](https://huggingface.co/blog/microsoft/thinkingbox-training) ⭐️ 9.0/10

rss · Hugging Face Blog · 10月22日 22:24

**「背景」** 在执行复杂的企业业务工作流时，人工智能智能体经常宣称任务已完成，但实际的数据库状态却与预期不符。传统的评估方式往往依赖单次尝试的准确率，从而掩盖了智能体在多次重复执行时表现出的高不稳定性。

**「方案」** 为了解决这一问题，作者利用 ThinkingBox 将数据库最终状态的判定结果直接转化为强化学习中的可执行奖励。由于传统的组相对策略优化（GRPO）在全部成功或全部失败的零方差任务组中会面临梯度为零的困境，作者引入了基于 Beta 后验的离线策略相对难度过滤机制，固定并挑选出最具有学习对比度的训练任务池。通过对 Qwen3.8-27B 模型进行 50 步的 GRPO 全参数微调，模型在从未见过的 507 个基准测试任务中展现出显著的性能提升：虽然单次尝试成功率（pass@1）从 51.70% 提升至 60.78%，但更具生产可靠性参考价值的“连续 20 次全部成功率（observed 20/20）”更是从 38 个任务大幅跃升至 107 个任务。

**「启示」** 作者的经验表明，将可执行的终端状态判定作为强化学习奖励并结合离线难度过滤，能够有效将智能体从偶尔解题的水平推向高重复一致性的可靠状态，从而为实际生产环境中的可靠性打下坚实基础。

**标签**: `#reinforcement-learning`, `#ai-agents`, `#llm-post-training`, `#evaluation`, `#databases`

---

<a id="item-tech-blog-2"></a>
### [Ensembling IBM Granite Time-Series Models](https://huggingface.co/blog/ibm-research/granite-timeseries-ensemble-r1) ⭐️ 8.0/10

rss · Hugging Face Blog · 10月22日 07:51

**「背景」** 预训练时间序列模型虽然无需针对特定数据集进行训练即可直接预测，但在面对噪声、季节性等不同场景时，用户往往难以抉择究竟该使用哪种单一架构。作者指出，挑选单一模型存在盲目性，而现有的多模型组合策略能够有效分散选错模型的风险。

**「方案」** 作者介绍了一种无需重新训练或拟合权重即可组合四个开源 Granite 模型的默认集成方案。该方案包含“概率集成”（Probabilistic Ensemble，采用等权重概率空间池化）与“IQR 集成”（根据预测区间离散度进行自适应加权）两种组合策略，并支持扩展外部模型。在 GIFT-Eval 基准测试中，两套集成方案在聚合 MASE 及平均 MASE 排名上均优于四个独立成员；其中概率集成取得了更低的 MASE，而 IQR 集成在平均 CRPS 排名上表现突出。不过，作者也坦言该方法存在明显的局限性，包括无法利用跨通道信息、因加载四个成员检查点而导致推理延迟和内存消耗增加，且聚合方法本身并不能保证校准性或对抗分布偏移的能力。

**「启示」** 作者认为，多模型集成的最大价值不在于登顶排行榜，而在于是提供了一个开箱即用的稳健起点，使开发者无需预先挑选单一最佳架构即可在多变的数据上获得稳定表现。

**标签**: `#time-series forecasting`, `#ensemble learning`, `#machine learning architectures`, `#benchmark evaluation`

---

<a id="item-tech-blog-3"></a>
### [为什么 AI 算力呈长方形：Modal CEO 谈弹性基础设施与智能时代](https://www.latent.space/p/modal-d) ⭐️ 7.0/10

rss · Latent Space · 10月22日 17:40

**「背景」** 传统的 GPU 算力合同往往要求客户为固定的容量和时长买单，这与全天候波动、暴涨暴跌的实际 AI 工作负载形成了鲜明对比，导致企业常常陷入闲置浪费或产能不足的困境。

**「方案」** Modal 通过聚合数千家客户的需求来执行“时长转换”，在底层统一调度并切分出极具弹性的算力切片，同时借助进程检查点、GPU 内存快照以及自定义文件系统等底层基础设施大幅缩短冷启动延迟。创始人 Erik Bernhardsson 指出，这种池化方案还能天然平抑不同开源模型交替发布所带来的流量剧烈震荡。此外，随着编码代理与强化学习的爆发，用于运行生成式代码的沙盒环境呈现爆发式增长，迫使平台不断演进虚拟机兼容性及快照复用等核心能力。

**「启示」** 作者认为，在 AI 模型和算力需求高度动态化的时代，独立的服务器端基础设施能够通过需求聚合与极速弹性调度，有效解决传统刚性合同与非线性负载之间的根本矛盾。

**标签**: `#ai-infrastructure`, `#serverless`, `#gpus`, `#sandboxes`, `#scaling`

---

<a id="item-tech-blog-4"></a>
### [PHP 核心漏洞 PHP2Shell 的发现与协同修复](https://www.latent.space/p/ainews-openais-patch-the-planet-program) ⭐️ 6.0/10

rss · Latent Space · 10月22日 07:42

**「背景」** 核心 PHP 引擎中披露了被称为 PHP2Shell 的严重内存破坏漏洞，影响了广泛的 Web 基础设施。由于这些缺陷存在于 PHP 内部对内存耗尽和致命错误的底层处理中，常规的应用程序身份验证或插件补丁无法直接解决该问题。

**「方案」** 研究人员利用 AI 模型（如 OpenAI 的 GPT-5.6 Sol 和 Google 的 Gemini 4 Argon）独立发现了这些漏洞，并与 PHP 基金会及相关机构展开了长达两个月的私密协调修复。在正式补丁发布之前，诸如 Cloudflare 等安全服务商部署了 Web 应用防火墙（WAF）规则来拦截已知的攻击向量。然而，这些防护措施仅能匹配触发引擎进入故障状态的特定请求形态，因此只能视作争取修补时间的临时权宜之计，最终仍依赖于核心引擎的代码升级。

**「启示」** 先进 AI 模型在底层运行时安全审计中展现出了巨大潜力，但面对影响深远的系统级漏洞，及时且广泛的跨行业协同响应依然是确保互联网基础设施安全的决定性因素。

**标签**: `#security`, `#php`, `#ai-assisted-audit`, `#infrastructure`, `#vulnerabilities`

---