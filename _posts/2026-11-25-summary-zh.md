---
layout: default
title: "Horizon Summary: 2026-11-25 (ZH)"
date: 2026-11-25
lang: zh
---

> 从 17 条内容中筛选出 4 条重要资讯。

---

**科技新闻**
1. [OpenAI 预印本论文指出矩阵乘法指数为九分之四](#item-tech-news-1) ⭐️ 10.0/10
2. [GPT-6 模型展示出内在的蛋白质设计能力](#item-tech-news-2) ⭐️ 8.0/10

**科技博客**
1. [Microduck Obstacle Avoidance Workflow in Isaac Lab](#item-tech-blog-1) ⭐️ 8.0/10
2. [过去十二个月中大语言模型的三个转折点](#item-tech-blog-2) ⭐️ 6.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI 预印本论文指出矩阵乘法指数为九分之四](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf) ⭐️ 10.0/10

OpenAI 的一份预印本论文指出矩阵乘法指数为九分之四（即 $\\Theta\(n^\{2.25\}\)$），从而解决了数学和计算机科学中的多个重大问题。该研究否定了矩阵乘法指数等于二的猜想，并在所有域上给出了精确指数。此外，同一篇论文还为线性规划强多项式时间（斯梅尔第九问题）、平均收益博弈和奇偶博弈等长期存在的公开问题提供了多项式时间算法。

hackernews · E-Reverance · 11月25日 01:19 · [社区讨论](https://news.ycombinator.com/item?id=50637220)

**「背景」** 矩阵乘法是线性代数中的核心运算，其计算效率由矩阵乘法指数 $\\omega$ 决定，即能够以 $O\(n^\{\\omega + \\epsilon\}\)$ 算术复杂度将两个 $n \\times n$ 矩阵相乘的下确界指数。长期以来，理论计算机科学家和数学家一直在不断优化该指数的上下界，以寻找更高效的算法。工具引用：\[tool-1-1, tool-1-2, tool-1-3\]

**「影响」** 这一理论突破对算法复杂度分析和理论计算机科学产生了深远影响，有望推动线性规划及图博弈等领域的计算效率提升。

**「社区讨论」** 社区成员指出该研究通过 AI 预印本解决了数学 Top 500 开放问题列表中的多项难题，并讨论了 OpenAI 可能正在利用前沿模型内部推进基础科学研究的策略。同时，部分讨论纠正了原帖标题对渐进复杂度的误读。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Matrix_multiplication">Matrix multiplication - Wikipedia</a></li>
<li><a href="https://mathworld.wolfram.com/MatrixMultiplicationExponent.html">Matrix Multiplication Exponent -- from Wolfram MathWorld</a></li>
<li><a href="https://officechai.com/ai/openai-has-found-a-far-faster-way-to-multiply-matrices-the-math-that-underpins-all-of-modern-ai/">OpenAI Has Found A Far Faster Way To Multiply Matrices , The Math...</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#algorithms`, `#mathematics`, `#computer systems`, `#research`

---

<a id="item-tech-news-2"></a>
### [GPT-6 模型展示出内在的蛋白质设计能力](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities) ⭐️ 8.0/10

OpenAI 宣布其 GPT-6 模型系列具备内在的蛋白质设计能力，能够仅通过推理和代码生成来设计新的蛋白质形状和序列，并在实验室测试中得到验证。在与 Onava 合作进行的实验室测试中，基于 GPT-6.2 设计的蛋白质在五个靶标上均显示出结合证据，且重新设计的抗体也保留了结合能力。尽管该模型在多数蛋白质设计任务上的表现可媲美或优于专业模型，但预测完整的蛋白质结构仍然是其明显的弱点。

rss · OpenAI News · 11月24日 13:00 · [社区讨论](https://news.ycombinator.com/item?id=50634658)

**「背景」** 蛋白质由被称为氨基酸的化学构建块长链组成，其三维折叠结构和氨基酸序列决定了其在生物体内的具体功能。传统的蛋白质设计通常依赖高度定制化的专业生物学模型，但这些模型在处理新指令和跨领域需求时需要进行软件修改或额外训练。

**「影响」** 这一进展表明，通用大语言模型未来有望作为灵活的控制层和推理引擎，直接简化和推动多学科交叉的生物科学研究工作流。

**「社区讨论」** 评论者认为模型的代码编写能力是其取得成功的关键，它能很好地充当连接不同专业工具的“黏合剂”，但也有人指出该研究在生物实验室对照方面仍显薄弱，且所谓“超越专业模型”的说法可能言之过早。

**标签**: `#artificial intelligence`, `#machine learning`, `#protein design`, `#bioinformatics`, `#large language models`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [Microduck Obstacle Avoidance Workflow in Isaac Lab](https://huggingface.co/blog/nvidia/microduck-obstacle-avoidance) ⭐️ 8.0/10

rss · Hugging Face Blog · 11月24日 16:34

**「背景」** 为了让微型机器人 Microduck 在保持固有行走策略不变的前提下学会避开障碍物，作者提出了一种基于时间飞行（ToF）传感器的 Sim2Real 导航控制训练方案。现有的行走策略虽能维持机器人平衡，但缺乏自主转向能力，因此需要一个独立训练的避障控制器来动态调整操纵杆速度指令。

**「方案」** 该工作利用 NVIDIA Isaac Lab 和 Newton 物理引擎搭建了大规模并行仿真环境，通过 SimReady 资源库中的各种模型随机生成障碍路线。作者采用多网格射线投射器模拟 Microduck 头部的 8×8 网格 ToF 传感器，在训练中引入了噪声、延迟和边缘失效等现实扰动。利用 PPO 算法在数千个环境中训练导航策略后，系统将输出的策略导出为 ONNX 格式，配合远程笔记本电脑与真实硬件进行通信部署，实现了由 ToF 传感器引导、操纵杆干预的实时避障控制。

**「启示」** 该工作证明了在复杂移动机器人中，将底层平衡行走策略与上层感知避障控制器解耦并进行 Sim2Real 迁移是完全可行的。这套基于 Isaac Lab 的标准化工作流为高效训练和部署具身智能体提供了极具参考价值的实践范例。

**标签**: `#sim2real`, `#reinforcement-learning`, `#robotics`, `#isaac-lab`, `#obstacle-avoidance`

---

<a id="item-tech-blog-2"></a>
### [过去十二个月中大语言模型的三个转折点](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) ⭐️ 6.0/10

rss · Simon Willison · 11月24日 23:02

**「背景」** 过去一年里，大语言模型与编码代理的底层能力经历了快速演进。作者西蒙·威利森（Simon Willison）回顾了自己在日常开发中从“需要频繁纠错”到“将 AI 视为可靠日常驱动程序”的心路历程，探讨了这一期间重塑软件开发格局的三大关键技术跃升。

**「方案」** 作者指出，第一个转折点出现在大约一年前，当时如 Claude Opus 4.5 与 OpenAI 的 Codex 等模型首次实现了足够的可靠性，使得默认输出大多正确并能真正加速开发。随后的年中出现了以 Claude Fable 5 为代表的“Fable 级”模型，其核心特征是具备极强的自主性，能主动调用工具（如编写本地服务器和截图脚本）来解决复杂故障。第三个转折点则出现在同年秋季，以 Claude Opus 5.5 等模型为代表的系统在 3D 建模、空间推理以及游戏玩法平衡性上取得突破，不仅能生成三维动画，甚至能通过自主游玩测试将枯燥的游戏变得妙趣横生。

**「启示」** 作者认为，过去一年中大语言模型从不稳定的辅助工具演变为具备主动工具使用能力和卓越空间及美学推理的伙伴，这彻底改变了软件开发的形态，也让独立游戏和个人项目的制作效率达到了前所未有的高度。

**标签**: `#AI Coding Assistants`, `#LLM Capabilities`, `#Developer Productivity`, `#Software Engineering`

---