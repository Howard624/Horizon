---
layout: default
title: "Horizon Summary: 2026-10-31 (ZH)"
date: 2026-10-31
lang: zh
---

> 从 12 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [Cursor 市场上的 Claude Code 扩展遭遇恶意篡改](#item-tech-news-1) ⭐️ 8.0/10
2. [OpenAI 宣布将通过 robots.txt 信号尊重网站的 AI 训练偏好](#item-tech-news-2) ⭐️ 7.0/10

**科技博客**
1. [构建一个会说话的万圣节鬼屋投影](#item-tech-blog-1) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Cursor 市场上的 Claude Code 扩展遭遇恶意篡改](https://phorion.io/blog/offical-claude-code-vsx-compromise/) ⭐️ 8.0/10

近期，一个恶意团伙在 Cursor 市场上发布了被篡改的 Claude Code 扩展程序，该扩展并非由 Anthropic 官方开发。受影响的版本在周四太平洋时间上午 2:27 至下午 1:35 之间处于上线状态，会自动向用户的系统中注入未授权的 SSH 公钥。这一供应链安全事件引发了开发者对第三方插件市场安全性的广泛关注，目前官方正与 Cursor 团队紧密合作进行处理。

hackernews · \_chall · 10月30日 07:09 · [社区讨论](https://news.ycombinator.com/item?id=50300683)

**「背景」** Cursor 市场和 Open VSX 注册表允许第三方开发者分发编辑器扩展，但这也为恶意行为者利用供应链漏洞注入恶意代码提供了可乘之机。SSH 授权密钥文件（authorized\_keys）如果被未经授权地写入公钥，会导致攻击者能够直接获得受害机器的远程访问权限。

**「影响」** 在此期间安装了该受感染扩展的 Cursor 用户面临设备被远程控制的安全风险，建议立即检查并清理 SSH 授权密钥文件。官方渠道发布的原生扩展并未受到此次事件的影响。

**「社区讨论」** 社区成员指出，受影响的主要是 Cursor 市场及 Open VSX 上的非官方构建版本，Anthropic 官方渠道保持安全。多位用户在讨论中分享了通过检查本地 authorized\_keys 文件中是否包含名为 &quot;svc-telemetry&quot; 的公钥来判断机器是否受损的具体方法。

**标签**: `#security`, `#developer tools`, `#cursor`, `#anthropic`, `#supply chain attack`

---

<a id="item-tech-news-2"></a>
### [OpenAI 宣布将通过 robots.txt 信号尊重网站的 AI 训练偏好](https://openai.com/index/helping-websites-express-ai-training-preferences) ⭐️ 7.0/10

OpenAI 宣布将遵守一个共享的 robots.txt 信号，以协助网站运营商向参与的提供商传达其对人工智能模型训练偏好的设置。这一举措让网站所有者能够更便捷地管理其内容在 AI 模型训练中的使用方式。该共享信号为整个行业在网页抓取和数据使用政策方面提供了一种标准化的沟通途径。

rss · OpenAI News · 10月30日 09:30

**「背景」** robots.txt 是网站用来向网络爬虫和搜索引擎机器人传达访问权限和抓取规则的标准文本文件。随着人工智能大语言模型的兴起，如何通过网络公开数据进行模型训练以及如何尊重网站所有者的版权和意愿，已成为行业内备受关注的议题。

**「影响」** 网站运营商现在可以通过统一的 robots.txt 机制更有效地控制其内容是否参与 OpenAI 的 AI 模型训练。此举有助于减少网络内容抓取引发的版权争议，并为网络生态提供更清晰的数据合规标准。

**标签**: `#artificial intelligence`, `#web scraping`, `#policy`, `#machine learning`, `#open source`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [构建一个会说话的万圣节鬼屋投影](https://huggingface.co/blog/nvidia/nemotron-halloween) ⭐️ 7.0/10

rss · Hugging Face Blog · 10月30日 17:57

**「背景」** 为了让万圣节的来访者获得独特的互动体验，作者决定将自家的车库门变成一个脾气暴躁、会讲海盗故事且对“请”字毫无抵抗力的活体建筑——MonsterHouse。为了实现这一设想，系统必须在本地工作站上实时运行语音识别、对话生成、语音合成及面部动画，同时严格控制延迟和计算资源。

**「方案」** 作者采用 NVIDIA Nemotron Voice Agent 作为核心架构，将 Nemotron 3 ASR 用于语音转文本，并选择经过 LoRA 微调的开源轻量语言模型 Nemotron 3.5 Bolt E4B（4GB 量化版本）来承担对话大脑。为了实现生动的语音和视觉表现，系统结合了 Magpie TTS Zeroshot 进行零样本声音克隆，并通过 Audio2Face-3D 驱动 Unreal Engine 5 中的木质面部动画。在硬件部署上，作者将工作负载拆分到双 GPU 工作站上运行，其中 RTX PRO 6000 负责大语言模型与语音管道，RTX PRO 4000 负责图形渲染与动画。此外，系统通过引入针对常见问候和答谢的文本及音频缓存机制，将中位响应延迟从完整生成的 1.70 秒大幅缩短至 0.72 秒。

**「启示」** 该项目展示了如何利用 NVIDIA 的一系列开源模型与工具链，在本地硬件上高效构建低延迟、具身化的实时交互式智能体。作者的工程实践证明，通过合理搭配语音管道、小语言模型与响应缓存，复杂的全双工互动应用完全能够在单机工作站上流畅运行。

**标签**: `#conversational AI`, `#speech recognition`, `#edge computing`, `#animation`, `#system architecture`

---