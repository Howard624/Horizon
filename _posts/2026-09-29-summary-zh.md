---
layout: default
title: "Horizon Summary: 2026-09-29 (ZH)"
date: 2026-09-29
lang: zh
---

> 从 21 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [Anthropic 发布 Sonnet 5.5 模型并引发社区对其安全性与基准测试的热议](#item-tech-news-1) ⭐️ 9.0/10

**科技博客**
1. [Holo4：全能型计算机操作智能体系列](#item-tech-blog-1) ⭐️ 6.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Anthropic 发布 Sonnet 5.5 模型并引发社区对其安全性与基准测试的热议](https://www.anthropic.com/claude-sonnet-5-5) ⭐️ 9.0/10

Anthropic 推出了全新人工智能模型 Sonnet 5.5，引发了开发人员和社区对其基准测试性能、网络安全能力以及模型限制的广泛讨论。根据系统卡显示，Sonnet 5.5 的网络安全能力较 Sonnet 5 有显著提升，因此部署了与 Opus 5.5 类似的防护措施，高风险网络安全任务会回退至 Sonnet 5。此外，虽然 Sonnet 5.5 在 Terminal-Bench 中获得了 70.6 的高分超越了 Opus 5.5 的 66.4 分，但分析表明这主要是由于 Opus 触发安全回退的比例（10%）远高于 Sonnet（1.5%）所致。

hackernews · D2OQZG8l5BI1S06 · 9月28日 17:58 · [社区讨论](https://news.ycombinator.com/item?id=49881850)

**「背景」** Claude Sonnet 5.5 是 Anthropic 推出的最新中端 AI 模型，作为其速度更快、成本更低的工作伙伴，旨在满足日常高频应用和复杂代理任务的需求 \[tool-1-1, tool-1-3\]。这一模型延续了 Anthropic 在 5.5 产品线中的技术演进，定位在高性能的 Opus 模型与高性价比的 Haiku 模型之间 \[tool-1-1, tool-1-3\]。

**「影响」** 使用 Anthropic 模型的开发者在处理高风险网络安全相关任务时，可能会频繁遇到模型自动回退至旧版本的情况。

**「社区讨论」** 社区讨论集中在安全性回退机制对基准测试结果的影响上，同时部分用户指出中国开源和商业模型在性价比上极具竞争力，而另一些用户则分享了高阶套餐在日常多会话开发中的高效体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-sonnet-5-5">Introducing Claude Sonnet 5.5 \ Anthropic</a></li>
<li><a href="https://techcrunch.com/2026/09/28/anthropic-releases-sonnet-5-5-which-it-calls-a-significantly-cheaper-faster-work-partner/">Anthropic releases Sonnet 5 . 5 , which it calls... | TechCrunch</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#machine learning`, `#frontier models`, `#llm benchmarks`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [Holo4：全能型计算机操作智能体系列](https://huggingface.co/blog/Hcompany/holo4) ⭐️ 6.0/10

rss · Hugging Face Blog · 9月28日 09:44

**「背景」** 大多数智能体模型通常仅针对单一界面训练，在需要同时结合图形界面、代码、MCP 与 API 的真实业务场景中往往捉襟见肘。为此，作者推出了全新的 Holo4 系列智能体模型。

**「方案」** Holo4 包含 27B 稠密模型与 35B-A3B 混合专家模型两种规模，并通过监督学习与强化学习在由 Agentic Task Factory 生成的丰富环境和任务中进行训练。作者团队还重建了执行循环与上下文管理的训练框架，使其具备更可靠的长期记忆和桌面 Shell 支持。在 OSWorld 2.0 等基准测试中，Holo4 27B 取得了 61.7%的分数，虽然略逊于部分顶级闭源模型，但其参数规模与任务成本显著更低。此外，作者利用相同的后训练方案将 Nemotron 3 Nano Omni 适配为 Holotron4 Nano，展现出良好的跨规模泛化能力。

**「启示」** 通过结合多界面交互训练与优化的执行框架，Holo4 证明了开源模型能够以远低于闭源前沿模型的成本，胜任跨平台的复杂真实业务工作流。

**标签**: `#AI Agents`, `#Model Release`, `#Reinforcement Learning`, `#Benchmarks`

---