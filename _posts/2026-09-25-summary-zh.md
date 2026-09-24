---
layout: default
title: "Horizon Summary: 2026-09-25 (ZH)"
date: 2026-09-25
lang: zh
---

> 从 22 条内容中筛选出 5 条重要资讯。

---

**科技新闻**
1. [开源 Android 应用商店 F-Droid 2.0 发布重大改版更新](#item-tech-news-1) ⭐️ 8.0/10
2. [Google DeepMind 推出的 Gemini 3.8 Live 引入实时数字人功能](#item-tech-news-2) ⭐️ 8.0/10

**科技博客**
1. [Foundries vs Navigators in Scientific Research](#item-tech-blog-1) ⭐️ 8.0/10
2. [使用 LFM2.5-VL-DSpark 加速视觉语言模型](#item-tech-blog-2) ⭐️ 7.0/10
3. [Meta Connect 2026 与近期人工智能生态进展](#item-tech-blog-3) ⭐️ 6.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [开源 Android 应用商店 F-Droid 2.0 发布重大改版更新](https://f-droid.org/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html) ⭐️ 8.0/10

开源 Android 应用商店 F-Droid 官方于 2026 年 9 月 24 日发布了 2.0 版本，为该平台带来了重大的架构重构与用户界面重新设计。此次更新标志着该开源应用商店迈入新阶段，旨在改善整体移动端体验。不过，具体的性能数据、兼容性限制及底层技术细节在本次发布公告中暂未详细披露。

hackernews · daveoc64 · 9月24日 15:26 · [社区讨论](https://news.ycombinator.com/item?id=49831968)

**「背景」** F-Droid 是一个专为 Android 平台打造的开源应用商店，长期以来致力于提供完全自由且开源的软件分发。在此次 2.0 版本发布前，其客户端界面和架构多年未经历过如此大规模的重构，社区用户此前也经常对其传统界面的易用性提出改进意见。

**「影响」** 使用 F-Droid 的开源生态用户将迎来全新的界面交互，同时这也缓解了部分用户对旧版客户端体验及特权扩展配置繁琐的长期不满。

**「社区讨论」** 社区用户对此次改版反应不一，部分用户赞赏其终于迎来大版本翻新并摆脱了旧的痛点，但也有人批评新界面盲目追随无边界等现代设计趋势，并对其排版细节和未来面对 Google 限制时的走向表示担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://daily.dev/posts/f-droid-2-0-gyxrkowac">F-Droid 2.0 | daily.dev</a></li>
<li><a href="https://alternativeto.net/news/2026/9/open-source-android-app-store-f-droid-2-0-arrives-with-a-major-design-and-code-overhaul/">Open source Android app store F-Droid 2.0 arrives with a major design and code overhaul | AlternativeTo</a></li>

</ul>
</details>

**标签**: `#open source`, `#android`, `#mobile development`, `#software release`, `#user interface`

---

<a id="item-tech-news-2"></a>
### [Google DeepMind 推出的 Gemini 3.8 Live 引入实时数字人功能](https://deepmind.google/blog/introducing-gemini-38-live-with-live-avatar/) ⭐️ 8.0/10

Google DeepMind 推出了 Gemini 3.8 Live 及其实时数字人功能，将近实时的视频生成与原生实时对话模型相结合，面向企业应用提供动态视觉呈现。该功能具备精准的唇形同步、自然表情和流畅的轮流对话能力，支持跨 97 种语言的无缝多语言语音同步，且不降低视频保真度。此外，它还支持异步工具调用，允许在保持对话连续性的同时在后台处理复杂任务，并且所有音视频输出均通过 SynthID 添加了水印以确保透明度。

rss · Google DeepMind · 9月24日 16:20

**「背景」** 实时多模态对话模型通过同时处理音频和视频输入，使人工智能代理能够像人类一样通过声音、视觉和面部表情进行更自然的交互。随着企业对互动式客户服务和虚拟导览需求的增长，将高保真实时视觉形象与先进推理能力相结合成为了当前多模态人工智能发展的重要方向。

**「影响」** 企业用户现在可以通过 Gemini Enterprise 将具备自定义品牌形象和多语言支持的实时数字人集成到客户服务和交互式 walkthrough 中。

**标签**: `#artificial intelligence`, `#multimodal models`, `#machine learning`, `#computer vision`, `#industry news`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [Foundries vs Navigators in Scientific Research](https://www.latent.space/p/foundries-vs-navigators-lowering) ⭐️ 8.0/10

rss · Latent Space · 9月24日 15:03

**「背景」** 在人工智能与科学研究结合的浪潮中，尽管前沿实验室正尝试用 AI 改变物理实验，但科学研究的核心瓶颈依然是耗时且成本高昂的湿实验。作者指出，虽然知识工作因 AI 而加速，但实验本身的吞吐量并未同步提升，导致科学界面临“思考变便宜而行动依然昂贵”的困境。

**「方案」** 作者提出生物医药行业应对这一挑战的两种主要方式：一是通过实体“foundries”降低物理测量的成本，以工业化方式快速生成实验数据；二是利用 AI“navigators”来消耗思考的剩余价值，降低数据分析、内部工具构建和战略决策的摩擦。在实际应用中，快速编写代码使得实验分析与方案调整在数小时内即可完成，而不再受制于传统的计算资源排队。团队还通过自主搭建轻量级的数据门户，摆脱了通用商业软件的框架限制，并利用大语言模型代理对数百个疾病靶点进行了从宏观筛选到深度质询的两阶段分诊，将原本需要耗费大量专家时间的工作规模化。然而，作者也坦言这种模式存在挑战，例如按需生成的代码和分析界面带来了复现性难题。

**「启示」** 文章的核心观点指出，当前加速科学研究的最强大 AI 并非专注于科学数据的模型，而是能够帮助科学家和高管在每周一清晨明确“什么值得去做”的导航工具。这种降低思维成本并赋能全流程决策的模式，对各类重研发的工程与软件组织同样具有深远意义。

**标签**: `#biotechnology`, `#artificial intelligence`, `#scientific research`, `#software engineering`, `#workflow automation`

---

<a id="item-tech-blog-2"></a>
### [使用 LFM2.5-VL-DSpark 加速视觉语言模型](https://huggingface.co/blog/LiquidAI/lfm2-5-vl-dspark) ⭐️ 7.0/10

rss · Hugging Face Blog · 9月24日 14:08

**「背景」** 视觉语言模型在边缘设备和数据中心部署时，解码阶段常常面临严重的性能瓶颈。传统的推理方式在处理包含图像和文本的复杂任务时耗时较长，现有的优化方法难以在保持准确率的同时显著提升生成速度。

**「方案」** 作者介绍了 LFM2.5-VL-DSpark 视觉语言投机解码草稿模型，它通过捕获目标模型在固定分层处的隐藏状态并将其投影到共享表示中，在仅增加 8.9% 参数量（约 2.80 亿参数）的情况下生成候选标记块。该模型在多项基准测试中展现出显著的加速效果：在设备端使用 MLX 运行时解码速度提升达 2.30 倍至 3.13 倍，而在 H100 GPU 上解码速度也可提升 2.04 倍至 2.66 倍。同时，作者也客观指出，由于视觉编码和预填充阶段不受投机解码加速，整体端到端收益会受到阿姆达尔定律的限制。

**「启示」** 通过轻量级的草稿模型和开箱即用的生态集成，视觉语言模型能够在不损失准确率的前提下实现高效推理，推动边缘端和数据中心 AI 性能的全面提升。

**标签**: `#speculative decoding`, `#vision-language models`, `#inference optimization`, `#machine learning infrastructure`

---

<a id="item-tech-blog-3"></a>
### [Meta Connect 2026 与近期人工智能生态进展](https://www.latent.space/p/ainews-meta-connect-2026-muse-glasses) ⭐️ 6.0/10

rss · Latent Space · 9月24日 08:12

**「背景」** 随着个人智能体市场的日益拥挤，各大科技巨头纷纷探索如何将前沿大模型能力与硬件生态深度整合，以争夺下一代人机交互的主导权。

**「方案」** Meta 在 Connect 2026 大会上推出了以个人智能体 Muse 为核心的软硬件生态，发布了支持语音和实时视频交互的 Muse、具备计算机使用能力的 Mac 客户端、配套的邮件与商务连接器，以及 Ray-Ban Meta Gen 3 眼镜、首款 VR 眼镜和钥匙扣设备 Muse Charm 等硬件，同时展示了低延迟的 Muse Realtime Avatar。在行业其他动态方面，作者提到 Anthropic 的 Claude 协助发现了新的噬菌体逆转录酶系统，Claude Opus 5.5 在编码基准测试中表现亮眼，而开源领域和基础设施也迎来了诸如 FLUX 3 Action 等一系列模型与架构更新。

**「启示」** Meta 正在通过“分发渠道加自有硬件”的深度绑定策略加速个人智能体的落地，而整个行业在模型能力飞速提升的同时，也面临着严峻的安全治理与推理效率挑战。

**标签**: `#artificial intelligence`, `#hardware`, `#llm benchmarks`, `#open models`, `#industry news`

---