---
layout: default
title: "Horizon Summary: 2026-11-24 (ZH)"
date: 2026-11-24
lang: zh
---

> 从 39 条内容中筛选出 5 条重要资讯。

---

**科技新闻**
1. [英伟达董事会重新任命黄仁勋为首席执行官](#item-tech-news-1) ⭐️ 8.0/10
2. [OpenAI 与 Cisco 联合发布开源运行时 Shirudo](#item-tech-news-2) ⭐️ 8.0/10
3. [Google DeepMind 利用 AI 智能体与形式化验证优化量子算法](#item-tech-news-3) ⭐️ 8.0/10
4. [OpenAI 发布 Python Agents SDK v1.0.0-alpha.2](#item-tech-news-4) ⭐️ 7.0/10

**科技博客**
1. [RoboTrack: 点跟踪技术助力真实机器人操作](#item-tech-blog-1) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [英伟达董事会重新任命黄仁勋为首席执行官](https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html) ⭐️ 8.0/10

英伟达董事会在与美国政府高级官员进行讨论后，于 2026 年 11 月 23 日宣布重新任命黄仁勋为公司总裁、首席执行官兼董事会成员。此前，董事会在不到两周前迅速将其罢免，而此次一致投票决定重新上任是在收到美国政府输入信息并确认其不构成国家安全风险后做出的。这一领导层的逆转凸显了这家人工智能硬件巨头在复杂的地缘政治和行业监管环境中的关键地位。

hackernews · jaz · 11月23日 14:00 · [社区讨论](https://news.ycombinator.com/item?id=50611576)

**「背景」** 黄仁勋此前因涉嫌婚外情及相关安全传闻而卸任英伟达首席执行官职务。在英伟达董事会与美国政府高级官员进行沟通并获得安全评估后，其董事会全票通过了恢复其职务的决定。

**「影响」** 黄仁勋的迅速回归消除了英伟达在人工智能硬件快速发展期间因最高层变动而带来的战略不确定性。

**「社区讨论」** 社区成员对董事会在两周内实现全票 180 度大转弯感到惊讶，并指出美国政府的意见在此次决策中起到了关键作用。讨论还引发了对跨国企业实际治理结构与名义治理结构差异的广泛思考。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/nov/23/jensen-huang-reinstated-as-nvidia-chief-executive">Jensen Huang reinstated as Nvidia CEO | Jensen ... | The Guardian</a></li>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director">NVIDIA Board Reinstates Jensen Huang as President, CEO and...</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#hardware`, `#industry news`, `#leadership`

---

<a id="item-tech-news-2"></a>
### [OpenAI 与 Cisco 联合发布开源运行时 Shirudo](https://openai.com/index/introducing-shirudo) ⭐️ 8.0/10

OpenAI 和 Cisco 联合推出了开源运行时 Shirudo，旨在利用 AI 生成的防护罩在不重启系统的情况下保护运行中的 Linux 服务。该项目结合了 OpenAI 的前沿 AI 技术与 Cisco 的基础设施安全专长，利用 eBPF 技术在操作系统内核中针对性地拦截漏洞路径。在一次控制测试中，由 OpenAI Codex 生成的防护罩成功阻断了运行中的 Elasticsearch 服务所面临的 Java4Shell 漏洞攻击。Shirudo 具备实时保护、机器速度防御、通过加密签名与内核验证实现的受信任部署，以及基于 TPM 的硬件辅助验证能力。该项目采用 BSD 2-Clause 许可证开源，其 BPF 程序则采用 BSD 和 GPL 双许可证。

rss · OpenAI News · 11月23日 21:20

**「背景介绍」** eBPF 是一项允许在 Linux 操作系统内核中安全运行沙箱程序的技术，无需修改内核源码或加载内核模块即可实现高效的网络监控和系统追踪。在传统的漏洞管理中，测试和部署补丁通常需要数天或数周时间，而直接禁用相关系统操作又容易导致业务中断。

**标签**: `#artificial intelligence`, `#open source`, `#security`, `#Linux`, `#infrastructure`

---

<a id="item-tech-news-3"></a>
### [Google DeepMind 利用 AI 智能体与形式化验证优化量子算法](https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/) ⭐️ 8.0/10

Google DeepMind 联合 Google Quantum AI 团队，利用 Gemini 智能体协作团队与 Lean 形式化定理证明器，成功优化了用于惯性约束核聚变、药物代谢模拟及基础量子运算的量子算法与电路。研究人员通过数学证明确保了结果的正确性，在多项测试中取得了显著进展：例如将惯性约束聚变相关计算成本降低 11.8 倍并把所需内存从 5,650 个降至 4,338 个纠错量子比特，将光敏分子模拟成本降低 8 倍，对细胞色素 P450 酶的模拟实现 2.5 倍提升且内存降至 333 个量子比特，同时在 Grover 算法特定实现和 arcsin 常规例程上分别实现了 2.57 倍和 290 倍的加速。为了促进社区在该方向的发展，Google DeepMind 已将相关的 Lean 库、问题规格说明以及经过验证的解决方案在 GitHub 上开源。

rss · Google DeepMind · 11月23日 16:59

**「背景介绍」** 量子计算机利用量子力学原理处理特定复杂计算，但早期硬件资源极为有限，因此需要高度优化的算法和电路来减少所需的量子比特与操作数。形式化验证则借助数学工具来严格证明软件或算法逻辑的正确性，从而避免在无法进行经典或早期量子测试的大规模场景下出现错误。

**「影响」** 该研究开源的 Lean 库与智能化搜索方法压缩了原本需要多年人工设计的流程，能够显著加速量子计算在清洁能源、药物研发及基础科学领域的应用探索。

**标签**: `#Quantum Computing`, `#Artificial Intelligence`, `#Formal Verification`, `#Open Source`, `#Algorithms`

---

<a id="item-tech-news-4"></a>
### [OpenAI 发布 Python Agents SDK v1.0.0-alpha.2](https://github.com/openai/openai-agents-python/releases/tag/v1.0.0-alpha.2) ⭐️ 7.0/10

OpenAI 于近日发布了 openai-agents-python 的 v1.0.0-alpha.2 版本，引入了对跨工作节点会话恢复、工具执行钩子、文本脱敏以及详细操作追踪的支持。该预览版捆绑了原生 Codex 运行时，兼容 CPython 3.10 至 3.14 环境，并采用全新的持久化状态格式。由于 alpha.2 版本引入了新的写入格式，升级时必须先更新检查点读取器再更新写入器。用户可以通过指定的平台 wheel 包及 SHA-256 哈希值进行安装。

github · markstuart-oai · 11月23日 20:11

**「背景」** OpenAI 代理 SDK（Agents SDK）旨在帮助开发者构建和管理基于大语言模型的复杂多智能体应用。随着分布式智能体和长时间运行任务的普及，跨节点状态持久化、工具调用安全拦截及执行追踪成为了核心需求。

**「影响」** 使用该 SDK 的开发者能够实现更具弹性的工作流故障恢复和更细粒度的工具执行控制。不过由于状态架构的变更，从 alpha.1 升级时需要严格遵守升级顺序并处理不兼容的快照。

**标签**: `#artificial intelligence`, `#machine learning`, `#software engineering`, `#open source`, `#developer tools`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [RoboTrack: 点跟踪技术助力真实机器人操作](https://huggingface.co/blog/allenai/robotrack) ⭐️ 8.0/10

rss · Hugging Face Blog · 11月23日 17:20

**「背景」** 在真实世界的机器人操作中，传统的视频点跟踪器在复杂场景和视角变化下往往表现不佳，现有的基准测试也难以暴露出这些实际应用中的盲点。

**「方案」** 作者推出了包含 307 个人工标注视频的基准测试 RoboTrack-Bench，以及利用模拟环境生成的 1500 万轨迹训练集 RoboTrack-15M。通过对点采样策略的调整，作者运用 Jensen-Shannon 散度成功解决了模拟数据与真实视频在运动分布上的不匹配问题。在此基础上微调出的 RoboTracker 和 RoboTracker-Warp 模型在各项机器人基准测试中取得了显著进步。在湿实验室移液操作的实际测试中，基于点跟踪的方法在面对遮挡和较大位移时，其成功率大幅超越了传统的光学流和对象掩码方法。

**「启示」** 该研究证明，利用经过精心校准的模拟数据训练点跟踪器，能有效突破真实机器人操作中的视觉感知瓶颈，为高精度的自动化任务提供可靠支持。

**标签**: `#robotics`, `#computer vision`, `#point tracking`, `#simulation data`, `#benchmarking`

---