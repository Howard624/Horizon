---
layout: default
title: "Horizon Summary: 2026-09-22 (ZH)"
date: 2026-09-22
lang: zh
---

> 从 24 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [小米发布 MiMo v2.6 大模型：包含 Flash 与 Pro 两个变体](#item-tech-news-1) ⭐️ 8.0/10

**科技博客**
1. [Pruning LLMs Like a Physicist via Ising Optimization](#item-tech-blog-1) ⭐️ 8.0/10
2. [Jev 和决策模型：放弃文本输出的全新大模型形态](#item-tech-blog-2) ⭐️ 6.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [小米发布 MiMo v2.6 大模型：包含 Flash 与 Pro 两个变体](https://mimo.xiaomi.com/mimo-v2-6) ⭐️ 8.0/10

小米正式发布了 MiMo v2.6 大语言模型，推出了 Flash 和 Pro 两个版本并随附了详尽的技术文档。其中 Flash 版本拥有 3090 亿总参数量、激活参数量为 150 亿，而 Pro 版本则拥有 1.02 万亿总参数量、激活参数量为 420 亿。小米在此次发布中展现了较高的透明度，不仅公开了详细的方法论，还分享了训练过程中的实时仪表盘供公众参考。

hackernews · volf\_ · 9月21日 20:12 · [社区讨论](https://news.ycombinator.com/item?id=49792730)

**「背景」** 小米 MiMo 系列是由小米推出的大型语言模型，此前曾引入混合策略强化学习（MORL）等技术来整合多项奖励信号。随着多代模型的迭代，该系列不断扩展并在架构和多模态能力方面持续演进。

**「影响」** 该模型的开源及高性价比特性引发了开发者的广泛关注，为评估和对比中美大模型性能提供了新的重要选项。

**「社区讨论」** 社区用户对小米在模型训练过程中展现出的高度透明度（如实时训练仪表盘和详细的技术报告）表示赞赏，并对其带来的高性价比和参数配置展现出浓厚兴趣。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Xiaomi_MiMo">Xiaomi MiMo - Wikipedia</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#machine learning`, `#open models`, `#large language models`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [Pruning LLMs Like a Physicist via Ising Optimization](https://huggingface.co/blog/MultiverseComputingCAI/pruning-llms-like-a-physicist-block-removal-as-an) ⭐️ 8.0/10

rss · Hugging Face Blog · 9月21日 13:44

**「背景」** 作者指出，现有大模型区块剪枝方法多采用均场假设，将每个区块视为独立实体或仅处理连续区块，忽略了区块间的复杂成对耦合。随着模型加深和架构异构化，这种简化在深度压缩时会导致性能严重下降。

**「方案」** 该研究将大语言模型的区块剪枝重新表述为一个等效于 Ising 自旋玻璃的约束二元优化（CBO）问题。通过对模型损失进行二阶泰勒展开，计算出捕获区块间相互作用的 Hessian 矩阵，进而将寻找最优剪枝组合转化为能量最小化任务。该方法仅需基于小型校准数据集计算一次全套耦合，便能以极低成本对候选配置进行评估。对于大规模模型，作者利用经典和量子启发式求解器快速获取低能量状态。实验表明，最优解往往并非绝对的基态，而是包含探索早期区块剪枝的低激发态。在 Llama-3.3-70B 等模型的深度压缩测试中，该方法在不经重训的情况下显著优于传统的区块影响力基线，且能无缝扩展至 Mamba2、注意力层与 MoE 层交错的混合架构。

**「启示」** 将大模型剪枝建模为物理学中的自旋玻璃优化问题，能够有效捕捉区块间的深度耦合关系，从而在深度压缩时实现远超传统启发式方法的性能表现。

**标签**: `#LLM Compression`, `#Optimization`, `#Statistical Physics`, `#Model Pruning`

---

<a id="item-tech-blog-2"></a>
### [Jev 和决策模型：放弃文本输出的全新大模型形态](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 6.0/10

rss · Simon Willison · 9月21日 23:09

**「背景」** 传统大模型虽然功能强大，但在面对分类、评级或排序等结构化决策任务时，往往受限于高昂的文本生成成本和复杂的解析流程。

**「方案」** 作者介绍了一种被称为“系统一级模型”或“决策模型”的新形态大模型 Jev，它接收非结构化文本输入，但摒弃了文本生成，转而输出对应类别、是否判断及评分的浮点数与置信度。由于仅对输入计费且单价极低，该模型非常适合用于垃圾邮件检测、标签推荐以及搜索结果重排等并行分类任务。然而，作者指出其完全不提供文本解释的黑盒特性也带来了严峻的治理挑战，使得潜在的偏见更难被察觉，因此严格的评估和结构化实验变得比以往更加重要。

**「启示」** Jev 这类输出概率决策的新模型形态展示了极高的速度与经济性，但其不透明的黑盒输出也对 AI 治理和系统评估提出了更高要求。

**标签**: `#llm`, `#machine-learning`, `#classification`, `#api-design`, `#ai-governance`

---