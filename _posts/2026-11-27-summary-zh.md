---
layout: default
title: "Horizon Summary: 2026-11-27 (ZH)"
date: 2026-11-27
lang: zh
---

> 从 16 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [AMD 专用 llama.cpp 分支优化旧款高带宽显卡大模型推理](#item-tech-news-1) ⭐️ 7.0/10

**科技博客**
1. [Nemotron 3.5 解析模型：开源数据与强化微调](#item-tech-blog-1) ⭐️ 8.0/10
2. [构建面向全渠道的销售代理系统](#item-tech-blog-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [AMD 专用 llama.cpp 分支优化旧款高带宽显卡大模型推理](https://devnull.land/amd-specific-llama-cpp) ⭐️ 7.0/10

开发者针对 llama.cpp 推出了专门针对 AMD 旧款数据中心硬件的优化分支，主要适配具有高内存带宽但计算性能相对一般的早期架构。社区成员通过优化 AMD 专有代码和移植部分显卡内核，显著提升了本地运行大语言模型的推理速度与吞吐量。这使得具备高达 32GB 显存及 1 TB/s 带宽的低成本二手老旧显卡，成为运行大模型极具性价比的可行方案。

hackernews · julianlam · 11月26日 17:11 · [社区讨论](https://news.ycombinator.com/item?id=50657265)

**「背景」** llama.cpp 是一个用于在各种硬件上高效运行大语言模型的开源推理框架。早期 AMD 的部分数据中心 GPU 虽然缺乏现代加速核心，但凭借高带宽的 HBM2 显存，在处理大模型内存瓶颈时展现出了独特的潜力。

**「影响」** 这一优化方案让开发者和预算有限的用户能够以极低的成本在本地流畅运行复杂的开源大语言模型。

**「社区讨论」** 社区讨论表明，开发者们通过利用约 200 美元的二手 AMD 显卡搭配定制优化分支与内核移植，成功实现了极高的模型预 fill 和解码速度，并在高上下文长度下保持了良好的稳定性。

**标签**: `#artificial intelligence`, `#machine learning`, `#hardware`, `#open source`, `#llama.cpp`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [Nemotron 3.5 解析模型：开源数据与强化微调](https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin) ⭐️ 8.0/10

rss · Hugging Face Blog · 11月26日 05:05

**「背景」** 为了将复杂文档图像高效转化为结构化数据以支撑检索增强生成与智能体，NVIDIA 与 Hugging Face 推出了 Nemotron 3.5 Parse 模型。面对图表反推数值以及表格行列对齐等严苛挑战，传统的解析方法在准确性与泛化能力上往往显得捉襟见肘。

**「方案」** 作者指出，Parse 3.5 通过监督微调（SFT）奠定了阅读文本、布局、表格和图表的通用能力，随后借助基于群组相对策略优化（GRPO）的带有可验证奖励的强化学习（RLVR）大幅提升了输出的一致性并抑制了重复循环。在架构优化方面，模型采用了 NaViT 动态矩形输入、压缩视觉前缀以及分组查询注意力（GQA-8），并引入了 DFlash2 小草稿模型进行多词元预测以实现激进的投机解码。作者提到，在单张 H200 上，DFlash2 在并发 1 和并发 512 时分别将吞吐量提升了 7.62 倍和 1.52 倍。此外，开发团队还开源了三大类合成数据集，并提供了一套涵盖 SFT 与 RLVR 的完整微调食谱，允许开发者针对特定领域（如牙科表单）进行定制适配与多阶段解析。

**「启示」** 结合大规模合成数据、SFT、RLVR 以及底层架构与投机解码的深度优化，能够显著突破密集文档与复杂图表解析的精度与效率瓶颈。开源这些全套方案与数据集将有力推动多语言和垂直场景下文档智能模型的进一步创新。

**标签**: `#document parsing`, `#reinforcement learning`, `#synthetic data`, `#speculative decoding`, `#fine-tuning`

---

<a id="item-tech-blog-2"></a>
### [构建面向全渠道的销售代理系统](https://latent.space/p/how-clay-builds-gtm-agents-jeff-barg-head-of-ai/) ⭐️ 7.0/10

rss · Latent Space · 11月26日 23:02

**「背景」** 随着业务规模快速增长，Clay 团队在开发面向 Go-to-Market（GTM）的 AI 代理时，面临着海量公司数据分类的成本压力、复杂任务编排的需求以及传统工作流引擎扩展性受限的挑战。

**「方案」** 作者 Jeff Barg 指出，使用分类器对全球 4000 万家公司进行理想客户画像匹配的成本仅需约 1500 美元。在架构方面，团队舍弃了复杂的 Temporal 或 LangGraph，坚持使用轻量级的 BullMQ 来支撑高并发任务，并通过精细的限流和速率控制来平衡企业级与普通用户的负载。同时，Clay 将代码编写代理从最初的简单工具循环重构为运行在云沙箱中的 Pi harness，结合跨 CRM 与 Gong 的新数据层让代理获得全局视野。此外，团队发现目前的模型在自动调试长代理轨迹和定位根本错误方面仍然存在盲区，许多核心技能目前仍依赖人工编写。

**「启示」** 构建成熟的 GTM 代理基础设施不仅需要平衡模型推理成本与高层编排能力，更要在开放性与自动化之间找到平衡点，使产品能够无缝嵌入外部开发者的日常工作流中。

**标签**: `#ai-agents`, `#infrastructure`, `#architecture`, `#llm-orchestration`, `#cost-optimization`

---