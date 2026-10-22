---
layout: default
title: "Horizon Summary: 2026-10-22 (ZH)"
date: 2026-10-22
lang: zh
---

> 从 34 条内容中筛选出 6 条重要资讯。

---

**科技新闻**
1. [Railway Security Disclosure](#item-tech-news-1) ⭐️ 8.0/10

**科技博客**
1. [如何通过专用词汇表将小型语言模型推理成本降低 77%](#item-tech-blog-1) ⭐️ 9.0/10
2. [Profiling TorchNeuron: System-Level Profiling on AWS Trainium](#item-tech-blog-2) ⭐️ 9.0/10
3. [NVIDIA Kumo Relational 模型：无需训练的零样本关系型数据预测](#item-tech-blog-3) ⭐️ 8.0/10
4. [Claude Mods 与注意力接口的崛起](#item-tech-blog-4) ⭐️ 8.0/10
5. [\[AINews\] DeepSeek DeepInfer: Open Source SOTA Inference running 155T toks/day/cluster making $22m/day at ~80% margin for a 81 day payback](#item-tech-blog-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Railway Security Disclosure](https://blog.railway.com/p/security-disclosure-wednesday-october-21st) ⭐️ 8.0/10

Railway published a security disclosure following incidents where attackers compromised services and accessed stored secrets and environment variables.

hackernews · passenger · 10月21日 21:58 · [社区讨论](https://news.ycombinator.com/item?id=50188228)

**标签**: `#security`, `#cloud computing`, `#infrastructure`, `#vulnerabilities`, `#devops`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [如何通过专用词汇表将小型语言模型推理成本降低 77%](https://huggingface.co/blog/Dharma-AI/vocabx-vocabulary-specialization) ⭐️ 9.0/10

rss · Hugging Face Blog · 10月21日 17:35

**「背景」** 作者指出，通用开源模型（如 Qwen）的词汇表继承自多领域和多语言的通用设计，这给特定领域的模型带来了严重的文本碎片化以及计算资源的双重浪费。

**「方案」** 作者团队开发了 VocabX 方法，通过成本加权而非单纯基于频率来重新构建词汇表，同时在子词调整和宏标记（如 JSON 框架等重复结构）两个层面进行优化，并通过统计估计弥补样本盲区。在葡萄牙语作文自动评分系统的实际测试中，该方法将模型的输出长度从 350 个标记大幅缩减至 101 个，使 measured inference cost 降低了 77%，同时保持甚至提升了评分准确率。

**「启示」** 通过对小型语言模型的词汇表进行领域和成本维度的定制化特化，可以显著减少不必要的计算开销，从而在不改变基础模型和训练方案的前提下大幅压低实际生产中的推理成本。

**标签**: `#tokenization`, `#inference optimization`, `#small language models`, `#domain specialization`, `#machine learning engineering`

---

<a id="item-tech-blog-2"></a>
### [Profiling TorchNeuron: System-Level Profiling on AWS Trainium](https://huggingface.co/blog/amazon/profiling-torchneuron-part-1) ⭐️ 9.0/10

rss · Hugging Face Blog · 10月21日 16:04

**「背景」** 机器学习 practitioners often struggle to identify why models run slowly despite having intuitions about optimization. This guide explores how to systematically analyze inference performance on AWS Trainium using TorchNeuron and PyTorch profiler tools.

**「方案」** The author demonstrates how to configure torch.profiler with the Neuron backend using NeuronConfig and NeuronProfiler to capture device and runtime data. By analyzing the key\_averages\(\) table and Neuron Explorer visual traces across three RMSNorm implementations—naive eager operations, built-in fused functions, and torch.compile—the author reveals how kernel dispatch overhead impacts execution. While the naive implementation incurs multiple device calls and intermediate memory allocations totaling 2,355 µs, both the built-in fused kernel and torch.compile reduce device time to around 400 µs by fusing operations into a single execution path.

**「启示」** Combining key averages with visual execution traces allows developers to pinpoint device bottlenecks and confirm how operator fusion eliminates overhead between hardware dispatches. This profiling workflow scales directly to larger models to guide effective optimization choices.

**标签**: `#AWS Trainium`, `#PyTorch`, `#Performance Profiling`, `#Operator Fusion`, `#TorchNeuron`

---

<a id="item-tech-blog-3"></a>
### [NVIDIA Kumo Relational 模型：无需训练的零样本关系型数据预测](https://huggingface.co/blog/nvidia/kumo-relational) ⭐️ 8.0/10

rss · Hugging Face Blog · 10月21日 18:26

**「背景」** 在企业级应用中，预测性建模通常依赖于复杂的多表连接、耗时的特征工程以及针对特定任务的监督学习训练，这使得传统机器学习流程显得繁琐且缺乏灵活性。

**「方案」** 根据作者介绍，NVIDIA Kumo Relational 是一种预训练的关系型基础模型，能够直接对多表数据库进行零样本和少样本预测，而无需将表格扁平化。该模型采用自动上下文生成技术，利用预测查询语言（PQL）抓取多达 10,000 个历史示例作为上下文。其架构内部结合了轻量级的表格内注意力机制（列注意力与行注意力）以及跨表的图注意力与样本间注意力，从而在避免平方级成本的同时实现了高效的结构化推理。在预训练阶段，模型基于生成的多样化合成关系数据进行训练，学习过滤、关联和聚合跨表信息。评测结果表明，在多个基准测试中，该模型不仅超越了传统监督学习与专家工程梯度提升树，其推理速度也表现出极佳的效率，同时作者指出它在处理具有强时间动态和有效关系的数据时效果最佳。

**「启示」** 该研究表明关系型基础模型能够通过上下文学习直接驾驭复杂的企业数据库，从而开启了用通用预训练模型替代繁琐特征工程和定制化监督管线的新阶段。

**标签**: `#Machine Learning`, `#Foundation Models`, `#Relational Databases`, `#In-Context Learning`, `#Structured Data`

---

<a id="item-tech-blog-4"></a>
### [Claude Mods 与注意力接口的崛起](https://www.latent.space/p/claude-mods) ⭐️ 8.0/10

rss · Latent Space · 10月21日 13:04

**「背景」** 随着 AI 模型将更多功能吸收到权重中，传统的智能体工具链（harness）正逐渐转变为“注意力接口”，即决定模型何时打断用户、展示什么信息以及请求何种决策的交互层。然而，市面上如 ChatGPT 的生成式 UI 或 Cursor 的 PR 路由虽然提供了此类接口，却将交互设计的主导权握在厂商手中，限制了用户的个性化控制。

**「方案」** 作者指出，Anthropic 推出的 Claude Code 插件系统（Claude Mods）允许用户通过编写或由 Claude 代劳来定制 TypeScript/JavaScript 函数，从而实现对执行与渲染流程的干预。这种机制反转了工具链的方向，使其从“面向机器的代理”转变为“面向人类注意力的接口”。例如，内置的“You Should Know”插件能通过侧边代理捕获隐藏在踪迹中的关键遗漏，而作者开发的“Next Steps Supervisor”则能在复杂操作后自动提供下一步的快捷按钮。不过，作者也坦言了这类可编程插件带来的实际代价，包括高频触发带来的信息噪音、消耗额外 Token 的成本，以及缺乏沙箱隔离所带来的安全信任风险。

**「启示」** 作者认为，未来的工具链可能演变为一个让用户与 AI 共同塑造交互界面的平台，而其终极形态将是由 AI 自动识别工作流中的摩擦点并反向推荐和优化插件。这种可塑的工具链设计展示了人机协作的新可能，也促使开发者重新思考如何在个性化效率与注意力损耗之间取得平衡。

**标签**: `#AI Agents`, `#Developer Tools`, `#Agent Harness`, `#Interface Design`, `#Claude Code`

---

<a id="item-tech-blog-5"></a>
### [\[AINews\] DeepSeek DeepInfer: Open Source SOTA Inference running 155T toks/day/cluster making $22m/day at ~80% margin for a 81 day payback](https://www.latent.space/p/ainews-deepseek-deepinfer-open-source) ⭐️ 7.0/10

An analysis of DeepSeek&\#x27;s DeepInfer release, examining its disaggregated prefill/decode architecture, high cache hit rates, and the underlying economics of high-margin token serving.

rss · Latent Space · 10月21日 06:54

**标签**: `#llm-inference`, `#system-architecture`, `#prompt-caching`, `#infrastructure-economics`

---