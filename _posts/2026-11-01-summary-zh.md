---
layout: default
title: "Horizon Summary: 2026-11-01 (ZH)"
date: 2026-11-01
lang: zh
---

> 从 11 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [Andrej Karpathy 推出基于 Hacker News 推荐的视频浏览界面 HackerTube](#item-tech-news-1) ⭐️ 8.0/10

**科技博客**
1. [ChatGPT 账户接管漏洞的技术复盘](#item-tech-blog-1) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Andrej Karpathy 推出基于 Hacker News 推荐的视频浏览界面 HackerTube](https://karpathy.bearblog.dev/hacker-tube/) ⭐️ 8.0/10

Andrej Karpathy 推出了一个名为 HackerTube 的替代视频浏览界面，收录了自 2007 年以来从 Hacker News 评论中挖掘出的 6,454 个精选视频。该平台通过 YouTube 风格的界面呈现这些内容，完全去除了现代视频平台常见的互动诱导和成瘾性优化设计，专注于纯粹的技术与知识内容。开发者还可以下载包含专用 DATA.md 文件的完整数据包，交由 AI 代理进行定制、分析或构建衍生应用。

hackernews · karpathy · 10月31日 19:56 · [社区讨论](https://news.ycombinator.com/item?id=50319510)

**「背景」** 现代主流视频网站通常采用高度优化的推荐算法，通过最大化用户的点击和停留时长来提升广告收益。Hacker News 作为长期汇聚技术人员和极客的社区，其历史评论中沉淀了大量由真实用户分享的高质量视频链接。

**「影响」** 该项目为广大开发者和知识探索者提供了一个免受算法干扰的纯粹学习环境，同时也为 AI 辅助开发提供了结构清晰的开源数据集。

**「社区讨论」** 社区用户对这种摆脱了算法诱导和网红垃圾信息的浏览体验表示高度赞赏，并积极探讨了将其作为 AI 代理输入或添加按时间排序等实用功能的潜力。

**标签**: `#artificial intelligence`, `#open source`, `#software engineering`, `#web development`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [ChatGPT 账户接管漏洞的技术复盘](https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/) ⭐️ 7.0/10

rss · Simon Willison · 10月31日 23:15

**「背景」** Parameter Labs 发现并分析了 ChatGPT 在实现 HTML 预览时存在的漏洞，攻击者借此能够通过复杂的攻击链实现账户接管。

**「方案」** 作者指出，该攻击链首先利用了父页面通过 postMessage 接收消息时的不安全 innerHTML 处理方式，允许沙箱内的 iframe 向父页面注入自定义 HTML。由于缺少对消息发送源的严格限制，攻击者得以注入一个不受沙箱约束的新 iframe。随后，攻击利用了内容安全策略（CSP）中允许加载脚本的 YouTube 白名单域名，通过其 oEmbed 端点反射并执行了 JavaScript。一旦在主页面获得脚本执行权限，攻击者便能轻松获取用户的私有 API 数据并通过图像引用外泄。

**「启示」** 这起漏洞展示了当 iframe 通信、DOM 注入与 CSP 白名单组合使用时可能产生的严重安全风险。OpenAI 随后修复了该漏洞并支付了漏洞赏金。

**标签**: `#browser-security`, `#iframes`, `#content-security-policy`, `#vulnerabilities`, `#javascript`

---