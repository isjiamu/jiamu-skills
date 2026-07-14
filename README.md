# Jiamu Skills · 思维模型 / 销售赋能 / 内容设计 / 实用工具

![GitHub stars](https://img.shields.io/github/stars/isjiamu/jiamu-skills?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Skill](https://img.shields.io/badge/Skill-Agent-111111?style=flat-square)
![Claude Code](https://img.shields.io/badge/Claude%20Code-Supported-6B5B95?style=flat-square)
![Skills](https://img.shields.io/badge/Skills-11-0A7CFF?style=flat-square)

**中文** | [English](./README.en.md)

一套适配 Claude Code 等 Agent 环境的技能合集，覆盖**思维模型、决策咨询、销售赋能、投资分析、内容设计和实用工具**六大类，共 11 个技能。

> 由 [甲木](https://github.com/isjiamu) 在日常销售、内容创作和决策咨询工作流中沉淀而成——每个技能都解决一个真实、反复出现的问题。

---

## 30 秒开始

```bash
npx skills add https://github.com/isjiamu/jiamu-skills
```

也可以直接把这段话发给有 shell 权限的 AI Agent：

```text
帮我安装 jiamu-skills。请把 https://github.com/isjiamu/jiamu-skills 克隆到
~/Projects/jiamu-skills，然后把其中每个技能目录符号链接到 ~/.claude/skills/ 下，
完成后验证每个链接下都能读到 SKILL.md。
```

已经安装过的话，用这段话更新：

```text
帮我更新 jiamu-skills。请进入本地仓库执行 git pull，然后告诉我当前最新 commit。
```

安装后直接对 Agent 说：

```text
我最近很迷茫，帮我理清思路。          → 触发 gidlin-law
这个问题老是反复出现，帮我找找根因。    → 触发 five-why
帮我从多个角度分析要不要换工作。       → 触发 six-thinking-hats
开始私董会，我在纠结要不要创业。       → 触发 peers-advisory-group
给这个新品做一条 15 秒的品牌广告片。   → 触发 tvc-ad-film
```

---

## 📦 技能总览

### 🧠 思维模型（4个）

从"说不清问题"到"做出决策"的完整思维工具链。

| 技能 | 思维模型 | 解决什么 | 触发关键词 |
|------|---------|---------|-----------|
| [**gidlin-law**](./gidlin-law/) | 吉德林法则 | 把问题写清楚，就已经解决了一半——六步提问把模糊困扰变成清晰问题陈述 | "帮我理清思路"、"我很迷茫"、"吉德林" |
| [**five-why**](./five-why/) | 5Why 分析法 | 连续追问"为什么"剥离表象，找到机制性根因并制定根治对策 | "5Why"、"找根因"、"根本原因分析" |
| [**first-principles-mentor**](./first-principles-mentor/) | 第一性原理 | 苏格拉底式提问拆解至基本公理，挑战行业惯例，从零重构方案 | "第一性原理"、"分析本质"、"回归本源" |
| [**six-thinking-hats**](./six-thinking-hats/) | 六顶思考帽 | 德·博诺平行思维法，六个维度系统化分析，产出结构化决策报告 | "六顶思考帽"、"利弊分析"、"多角度分析" |

**推荐串联用法**：

```
gidlin-law（定义问题）
  → five-why（找根因）或 first-principles-mentor（拆解本质）
    → six-thinking-hats（多维决策）
      → peers-advisory-group（私董会深度咨询）
```

### 💡 决策咨询（1个）

| 技能 | 描述 | 触发关键词 |
|------|------|-----------|
| [**peers-advisory-group**](./peers-advisory-group/) | 私董会专家助手——巴菲特、盖茨、马斯克、乔布斯四位幕僚多轮提问与反馈，融合百度搜索/百科实时数据"带着数据聊" | "开始私董会"、"私董会" |

### 🎯 销售赋能（1个）

| 技能 | 描述 | 触发关键词 |
|------|------|-----------|
| [**sales-ai-assistant**](./sales-ai-assistant/) | 销售AI助手——描述业务场景即可生成专业销售内容，覆盖25个场景（陌生开发、演示跟进、竞品对战卡、转化分析等），同时输出优化提示词供学习 | "我要给客户发封邮件"、"竞品分析" |

### 📈 投资分析（1个）

| 技能 | 描述 | 触发关键词 |
|------|------|-----------|
| [**stock-advisor**](./stock-advisor/) | A股投资顾问——全自动分析流水线：技术面 → 基本面 → 交叉验证 → 私董会决策 → 杂志报告，AKShare 免费数据驱动 | "帮我分析股票"、股票代码、K线图截图 |

### 🎨 内容设计（2个）

| 技能 | 描述 | 触发关键词 |
|------|------|-----------|
| [**magazine-layout**](./magazine-layout/) | 杂志排版工具——文本秒变高颜值杂志页面，12种视觉风格，Tailwind 响应式，支持多引擎PDF导出 | "杂志排版"、"文章排版"、"magazine layout" |
| [**tvc-ad-film**](./tvc-ad-film/) | TVC 产品广告片——从产品理解、6 个创意方向、分镜脚本和逐镜头提示词，到锚点、关键帧、视频生成与合成，完成 15–25 秒品牌短片 | "做一条 TVC"、"产品广告片"、"品牌短片"、"新品上市视频" |

### 🛠️ 实用工具（2个）

| 技能 | 描述 | 触发关键词 |
|------|------|-----------|
| [**video-downloader**](./video-downloader/) | 通用视频下载器——支持1000+网站（YouTube、Bilibili、Twitter/X、TikTok），可选质量、提取音频、下载字幕 | 直接发视频链接、"下载视频" |
| [**gif-splitter**](./gif-splitter/) | GIF动图切分器——解决微信公众号"帧数超过300帧"限制，智能均分、保留帧率、支持批量 | "GIF帧数超限"、"切分GIF" |

---

## 常见使用场景

| 任务 | 推荐方式 |
|------|---------|
| 脑子很乱，说不清问题在哪 | 先用 **gidlin-law** 六步定义问题，再决定用哪个工具深入 |
| 同一个问题反复出现 | **five-why** 溯源找机制性根因，输出根治对策 |
| 重大决策（换工作/创业/投资） | **six-thinking-hats** 六维分析，或 **peers-advisory-group** 私董会深度咨询 |
| 挑战行业惯例、寻找颠覆式创新 | **first-principles-mentor** 拆到公理再重构 |
| 写销售邮件/方案/竞品对比 | **sales-ai-assistant** 描述场景直接生成 |
| 个股深度分析 | **stock-advisor** 发股票代码或K线截图，全流水线自动跑 |
| 文章排版成杂志页面/PDF | **magazine-layout** 选风格生成HTML |
| 用产品图制作品牌投放级广告短片 | **tvc-ad-film** 先选创意方向，再确认分镜和关键帧，生成并合成 TVC |
| 公众号GIF上传失败 | **gif-splitter** 自动检测帧数并切分 |

---

## 适合 / 不适合

**✅ 合适**：个人决策与复盘 / 销售内容批量生产 / A股个股研究 / 文章视觉化呈现 / TVC 广告短片策划与生成 / 公众号运营中的素材处理

**❌ 不合适**：需要实时协作编辑的场景 / 无 shell 权限的普通 Chatbot（思维模型类勉强可用，工具类无法运行脚本）

---

## 📥 安装

### 方式一：一行命令安装（推荐）

```bash
# 安装全部技能
npx skills add https://github.com/isjiamu/jiamu-skills

# 或只装某一个
npx skills add https://github.com/isjiamu/jiamu-skills --skill six-thinking-hats
```

### 方式二：把下面这段话直接发给 AI

> 帮我安装 `jiamu-skills` 这个 Claude Code 技能合集。请按下面步骤做：
>
> 1. 执行 `git clone https://github.com/isjiamu/jiamu-skills.git ~/Projects/jiamu-skills`
> 2. 把仓库里每个技能目录（含 SKILL.md 的目录）符号链接到 `~/.claude/skills/` 下
> 3. 验证每个链接下都能读到 `SKILL.md`
> 4. 告诉我装好了哪些技能，之后我说"开始私董会"之类的话就会触发对应技能

### 方式三：手动命令行

```bash
git clone https://github.com/isjiamu/jiamu-skills.git ~/Projects/jiamu-skills
for d in ~/Projects/jiamu-skills/*/; do
  [ -f "$d/SKILL.md" ] && ln -s "${d%/}" ~/.claude/skills/$(basename "$d")
done
```

> 💡 推荐用符号链接而不是拷贝：仓库 `git pull` 之后所有技能自动同步最新版。

---

## 平台支持

| 平台 | 状态 | 说明 |
|------|------|------|
| Claude Code | ✅ 支持 | 原生 Skill 工作流，全部技能可用 |
| Cursor / 其他本地 Agent | ✅ 可用 | 需要能读写文件并执行 shell 命令 |
| 普通 Chatbot | ⚠️ 部分可用 | 思维模型类可把 SKILL.md 当提示词用；工具类（gif-splitter 等）依赖本地脚本 |

---

## 📁 项目结构

```
jiamu-skills/
├── gidlin-law/               # 🧠 吉德林法则顾问
├── five-why/                 # 🧠 5Why溯源顾问
├── first-principles-mentor/  # 🧠 第一性原理思维导师
├── six-thinking-hats/        # 🧠 六顶思考帽决策引导师
├── peers-advisory-group/     # 💡 私董会专家助手
├── sales-ai-assistant/       # 🎯 销售AI助手（25个场景模板）
├── stock-advisor/            # 📈 A股投资顾问（分析脚本 + 报告模板）
├── magazine-layout/          # 🎨 杂志排版工具（12种风格 + PDF导出）
├── tvc-ad-film/              # 🎨 TVC产品广告片（创意 + 分镜 + 生成合成）
├── video-downloader/         # 🛠️ 通用视频下载器
├── gif-splitter/             # 🛠️ GIF动图切分器
├── CHANGELOG.md
├── LICENSE
└── README.md
```

每个技能目录均包含 `SKILL.md`（核心指令），按需附带 `references/`（参考模板）、`scripts/`（可执行脚本）、`README.md`（详细文档）。

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

**贡献新技能**：
1. Fork 本仓库，创建新的技能目录
2. 必须包含 `SKILL.md`（含 name/description frontmatter 和触发场景）
3. 参考模板放 `references/`，可执行脚本放 `scripts/`
4. 提交 PR 并说明技能的用途和使用场景

---

## 📊 版本历史

- **v1.7.0** (2026-07-14) - 新增 tvc-ad-film：从产品理解、创意提案和分镜提示词，到关键帧、视频生成与合成的 TVC 广告片工作流
- **v1.6.0** (2026-07-05) - 新增思维模型系列4件套；peers-advisory-group 融合百度实时数据；magazine-layout 独立仓库归档合并
- **v1.5.0** (2026-03-28) - 新增 stock-advisor
- **v1.4.0** (2026-01-26) - 新增 gif-splitter
- **v1.3.0** (2026-01-23) - 新增 sales-ai-assistant

完整更新记录见 [CHANGELOG.md](./CHANGELOG.md)

---

## 📄 许可证

MIT License - 详见 [LICENSE](./LICENSE)

## 👤 作者

**甲木 / jiamu** ([@isjiamu](https://github.com/isjiamu)) — 专注于AI工具和生产力提升的实践者

---

<div align="center">

**⭐ 如果这些技能对你有帮助，请给个 Star 支持！⭐**

Made with ❤️ by jiamu

</div>
