---
layout: default
title: "Horizon Summary: 2026-11-06 (ZH)"
date: 2026-11-06
lang: zh
---

> 从 26 条内容中筛选出 4 条重要资讯。

---

**科技新闻**
1. [Claude Code 被曝会将用户邮箱地址发送至外部网站](#item-tech-news-1) ⭐️ 8.0/10
2. [OpenAI 推出 GPT-6 Cyber 专注于漏洞发现与修复](#item-tech-news-2) ⭐️ 8.0/10
3. [Google DeepMind 发布 Gemini Omni 1.2 Flash 视频生成模型](#item-tech-news-3) ⭐️ 8.0/10

**科技博客**
1. [NVIDIA Cosmos 3 Open Models for Interactive World Simulation](#item-tech-blog-1) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Claude Code 被曝会将用户邮箱地址发送至外部网站](https://github.com/anthropics/claude-code/issues/107757) ⭐️ 8.0/10

近期的一项问题报告与社区讨论显示，开发工具 Claude Code 在运行过程中意外将用户的电子邮箱地址及相关身份标识发送给外部网站，引发了用户的隐私担忧。子代理在发送带有特定用户标识和公司信息的请求头（User-Agent）时触发了此行为。Anthropic 维护者已迅速发布了包含 \`cc-plugin-privacy\` 内置模块的 2.1.317 及更新版本来拦截该行为。

hackernews · motoroco · 11月5日 22:17 · [社区讨论](https://news.ycombinator.com/item?id=50385272)

**「背景」** Claude Code 是 Anthropic 推出的用于开发人员的命令行 AI 辅助工具，能够代表用户执行各种编码和联网任务。在与外部网络或 API 交互时，AI 代理可能会通过请求头或附加参数携带调用者的环境与身份上下文。

**「影响」** 使用受影响版本的开发者可能在不知情的情况下泄露了个人隐私信息，部分用户报告称因此收到了包含个人姓名的定制垃圾邮件。升级到 2.1.317 或更高版本并启用隐私模块的用户可以阻止该行为。

**「社区讨论」** 社区成员对此次隐私泄露感到震惊，许多人将近期收到的个性化垃圾邮件激增归咎于此。部分开发者指出，子代理在通过 curl 等工具进行网络请求时会将真实姓名和公司名称写入 UA 头中，并呼吁加强对 AI 工具数据外发行为的控制。

**标签**: `#artificial intelligence`, `#privacy`, `#software engineering`, `#security`

---

<a id="item-tech-news-2"></a>
### [OpenAI 推出 GPT-6 Cyber 专注于漏洞发现与修复](https://openai.com/index/introducing-gpt-6-cyber) ⭐️ 8.0/10

OpenAI 推出了名为 GPT-6 Cyber 的专业网络安全模型，旨在寻找可利用的漏洞并在授权范围内开发相应的修复方案。该模型代表了人工智能驱动的网络安全代理在漏洞发现与修复前沿领域的重要发展。它结合了先进的机器学习技术，旨在帮助安全人员更高效地管理和修补系统安全风险。

rss · OpenAI News · 11月5日 09:00

**「背景」** 随着人工智能技术的快速发展，大语言模型在软件开发和代码分析领域的应用日益广泛。网络安全代理利用这些模型自动检测代码中的安全缺陷，已成为现代漏洞管理和防御工程的重要研究方向。

**「影响」** 安全团队和开发人员可以利用该模型在授权范围内更高效地识别系统漏洞并生成修复补丁。这将显著提升漏洞响应的速度，但同时也对确保模型在合规边界内运行提出了更高的要求。

**标签**: `#artificial intelligence`, `#cybersecurity`, `#machine learning`, `#vulnerability management`

---

<a id="item-tech-news-3"></a>
### [Google DeepMind 发布 Gemini Omni 1.2 Flash 视频生成模型](https://deepmind.google/blog/gemini-omni-12-flash-fast-and-cost-effective-with-longer-clips/) ⭐️ 8.0/10

Google DeepMind 发布了 Gemini Omni 1.2 Flash 模型，现已在 Gemini API 及企业版中全面上线。该版本引入了原生 15 秒视频生成、多轮对话编辑以及增强的参考遵循能力，同时价格比上一代 Omni 1.1 下调了 30%，720p 视频定价为每秒 0.07 美元。新技术支持在 3 秒到 15 秒之间按 1 秒增量指定时长，并改进了角色、产品、风格图像及音频提示的一致性，输出内容带有 SynthID 水印。

rss · Google DeepMind · 11月5日 17:05

**「背景介绍」** Gemini Omni 是 Google 推出的多模态生成模型系列，专注于处理和生成包含视频、音频及文本在内的复杂内容。随着 AI 视频生成技术在广告创作和企业应用中的普及，降低成本和延长单次生成时长一直是行业的重要演进方向。

**「影响」** 使用该模型的开发者、企业和创作者可以借助 30% 的价格降幅和更长的视频时长，以更低的成本在大规模视频制作和多轮编辑工作流中保持品牌及角色的高一致性。

**标签**: `#artificial intelligence`, `#machine learning`, `#video generation`, `#apis`, `#google deepmind`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [NVIDIA Cosmos 3 Open Models for Interactive World Simulation](https://huggingface.co/blog/nvidia/cosmos-interactive-world-simulation) ⭐️ 7.0/10

rss · Hugging Face Blog · 11月5日 19:35

**「背景」** 为了满足机器人和自动驾驶对高度交互式模拟环境的需求，NVIDIA 推出了 Cosmos 3 模型的四个全新开源权重检查点。现有方法在处理多模态观察和动态场景变化时往往面临局限，难以在保持视觉真实感的同时实现高效的实时交互。

**「方案」** 该系列模型包含 16B 可训练参数，基于 Mixture-of-Transformers 骨干网络，通过注意力机制连接文本处理与视觉生成网络。其架构采用时序因果注意力机制，利用键值缓存保留历史信息，支持分块流式生成。训练过程分为四个阶段：阶段 0 进行双向适应以学习控制与视频的关系；阶段 1 采用教师强制预测短片段；阶段 2 利用一致性蒸馏在四步内生成片段；阶段 3 则通过自强制（self-forcing）技术暴露生成历史，配合冷冻教师和辅助评分模型修正误差累积。不同检查点针对特定场景设计，例如 Transfer-Auto 负责离线多传感器驾驶数据生成，Sim-Auto 提供流式驱动模拟，Sim-Transfer 将物理模拟器控制转化为真实感视频，而 Sim-Bimanual 则直接根据机器人动作预测下一个观察画面。

**「启示」** NVIDIA 的 Cosmos 3 模型通过开放权重和四阶段训练配方，为研究人员和开发者提供了一个构建响应式模拟世界的共同起点。这不仅有助于推进机器人和自动驾驶策略的学习与评估，也为未来探索动作与观察的动态闭环开辟了新路径。

**标签**: `#world models`, `#generative AI`, `#robotics`, `#autonomous driving`, `#model training`

---