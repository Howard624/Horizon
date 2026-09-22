---
layout: default
title: "Horizon Summary: 2026-09-23 (ZH)"
date: 2026-09-23
lang: zh
---

> 从 38 条内容中筛选出 5 条重要资讯。

---

**科技新闻**
1. [OpenAI 推出 GPT-6 Sol 与 Luna 模型](#item-tech-news-1) ⭐️ 9.0/10
2. [OpenAI 推出面向 GPT-6 的改进型提示词缓存功能](#item-tech-news-2) ⭐️ 8.0/10
3. [OpenAI 发布 Codex rust-v0.156.0 版本](#item-tech-news-3) ⭐️ 7.0/10

**科技博客**
1. [Transformers Natively Runs llama.cpp GGUF Quants on Apple Silicon](#item-tech-blog-1) ⭐️ 8.0/10
2. [Xiaomi MiMo-V2.6 and Recent Frontier AI Breakthroughs](#item-tech-blog-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI 推出 GPT-6 Sol 与 Luna 模型](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 9.0/10

OpenAI 推出了全新的 GPT-6 Sol 与 Luna 模型，引发了开发者和用户对其定价结构与实际体验的广泛关注。社区讨论显示，GPT-6 Luna 的价格降至 GPT-5.6 Luna 的一半，在成本上具有显著优势。与此同时，开发者们也在探讨新模型在代理工作流、使用限制以及编码体验等方面的表现。

hackernews · OpenAI News · 9月22日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49805509)

**「背景」** OpenAI 于 2026 年 9 月发布了 GPT-6 系列的中低端模型 Sol 与 Luna，作为旗舰模型 GPT-6 Astra 的补充。这些新模型旨在通过更低的 API 定价和改进的代码及智能体工作流性能，满足开发者对高性价比和高吞吐量任务的需求。

**「影响」** 价格的大幅下降和性能的提升，让开发者和普通用户能够以更低的成本获得更强大的 AI 能力，进而改变了多个主流 AI 编码与对话工具的性价比格局。

**「社区讨论」** 社区成员对 GPT-6 Luna 的大幅降价表示欢迎，并分享了新模型的各项测试与实际使用体验。不过，也有开发者对新版本能否延续前代模型那种自然顺畅的工程直觉和协作感表示了一丝担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT - 6 Sol and Luna | OpenAI</a></li>
<li><a href="https://coursiv.io/blog/gpt-6-sol-luna">GPT - 6 Sol and Luna : Pricing, Benchmarks, Availability | Coursiv Blog</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#machine learning`, `#large language models`, `#openai`

---

<a id="item-tech-news-2"></a>
### [OpenAI 推出面向 GPT-6 的改进型提示词缓存功能](https://openai.com/index/better-prompt-caching-for-gpt-6) ⭐️ 8.0/10

OpenAI 推出了针对 GPT-6 的改进型提示词缓存功能，旨在提升缓存命中率并降低延迟与成本。该更新引入了全新的诊断工具、显式断点以及可减少推理延迟的控制选项。这些基础设施升级能够显著优化大规模语言模型在生产环境中的运行效率。

rss · OpenAI News · 9月22日 21:00

**「背景」** 提示词缓存是一种大型语言模型推理优化技术，它通过存储和复用先前处理过的输入前缀来减少重复计算。这项技术能够有效降低高频交互和长文本应用场景下的 API 调用成本并缩短响应时间。

**「影响」** 使用 GPT-6 的开发者和企业将能够通过更高的缓存命中率和显式控制来降低推理成本并改善响应延迟。

**标签**: `#artificial intelligence`, `#machine learning`, `#prompt caching`, `#llm optimization`, `#infrastructure`

---

<a id="item-tech-news-3"></a>
### [OpenAI 发布 Codex rust-v0.156.0 版本](https://github.com/openai/codex/releases/tag/rust-v0.156.0) ⭐️ 7.0/10

OpenAI 于近日发布了 Codex 的 rust-v0.156.0 版本，带来了多项重大功能更新与安全修复。新版本引入了可通过 \`/tui\` 启动的可选全屏终端界面，支持转录搜索、鼠标选择和右键复制；默认开启语音对话功能，配有 F8 快捷键、\`/voice settings\` 选择器以及适用于 Linux 和 Windows 的内置音频运行时。此外，更新还新增了用于查看账户使用情况和令牌总数的 \`/usage\` 分析仪表盘、默认启用的 Worktree 会话支持、六个新的终端主题，并修复了包括 Windows 离线沙箱、剪贴板转发以及 OAuth 凭证刷新在内的多项安全漏洞与缺陷。

github · github-actions\[bot\] · 9月22日 19:51

**「背景信息」** OpenAI Codex 是一款广泛用于软件工程的 AI 辅助编程工具，旨在通过命令行和终端界面帮助开发者更高效地编写、调试和管理代码。

**「影响与意义」** 该版本显著增强了开发者的终端交互体验与语音协作能力，同时修复了多项沙箱隔离漏洞，提升了整体运行安全性。

**标签**: `#AI`, `#Software Engineering`, `#Developer Tools`, `#OpenAI`, `#Releases`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [Transformers Natively Runs llama.cpp GGUF Quants on Apple Silicon](https://huggingface.co/blog/transformers-llama-cpp-quants) ⭐️ 8.0/10

rss · Hugging Face Blog · 9月22日 00:00

**「背景」** 为了让用户更便捷地在本地设备上运行大模型，Hugging Face 的 transformers 库引入了对 llama.cpp GGUF 量化格式的原生支持。作者指出，尽管 llama.cpp 已经成为本地推理的高效引擎，但开发者通常需要更具灵活性且与 Python 生态紧密结合的解决方案。

**「方案」** Hugging Face 通过复用 llama.cpp 的 ggml 内核（包括用于量化权重读取的 ggml-quantization、融合归一化的 ggml-norm、Metal 闪现注意力的 ggml-attn 等），实现了在 Apple Silicon 上直接加载和运行 GGUF 模型。用户只需通过 from\_pretrained 传入 gguf\_file 参数即可无缝使用标准的 transformers API，甚至可以通过 transformers serve 提供与 OpenAI 兼容的 API 服务。此外，作者对生成循环（generate loop）进行了关键优化，例如在没有填充时早期丢弃不必要的注意力掩码、异步延迟停止检查，从而减少了 CPU 与 GPU 之间的同步等待开销。基准测试表明，在 M2 Max 芯片上，优化后的 transformers 库在多个密集模型和混合专家模型（MoE）上的推理性能已经非常接近专门的 llama.cpp。

**「启示」** 通过将高效的底层内核与优化的 Python 生成循环相结合，transformers 证明了在保持本地高性能推理的同时，开发者依然可以享受 Python 生态带来的灵活性与便利性。

**标签**: `#transformers`, `#llama.cpp`, `#GGUF`, `#model quantization`, `#Apple Silicon`

---

<a id="item-tech-blog-2"></a>
### [Xiaomi MiMo-V2.6 and Recent Frontier AI Breakthroughs](https://www.latent.space/p/ainews-xiaomi-mimo-v26-pro-1t-a42b) ⭐️ 7.0/10

rss · Latent Space · 9月22日 06:30

**「背景」** 随着大模型技术持续演进，开源社区与各大实验室正加速推进前沿模型的发布。传统模型在强化学习（RL）和多模态对齐方面往往面临高昂成本与架构限制，亟需更高效的训练方法与端到端优化。

**「方案」** 小米推出的 MiMo-V2.6 系列包含原生全模态模型及高速版本，其核心亮点在于高度透明且规模化的强化学习训练栈。根据作者总结，该模型通过扩展 RL 计算规模，采用异步架构实现大规模批处理与高吞吐量，并结合丰富的多任务训练套件以及更精确的评分器计算，闭环优化了长视距 RL 任务。此外，生态系统中涌现出诸如 Jev 等高效决策模型、各类 KV 缓存及推理优化技术，进一步压缩了整体计算成本并提升了运行效率。

**「启示」** 高质量的开源强化学习环境与极致的推理优化正在成为接替预训练语料库的关键战略杠杆，显著加速了前沿 AI 能力的普及与落地。

**标签**: `#frontier-models`, `#reinforcement-learning`, `#inference-optimization`, `#open-weights`, `#ai-agents`

---