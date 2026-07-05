# Jiamu Skills · Thinking Models / Sales Enablement / Content Design / Utilities

![GitHub stars](https://img.shields.io/github/stars/isjiamu/jiamu-skills?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Skill](https://img.shields.io/badge/Skill-Agent-111111?style=flat-square)
![Claude Code](https://img.shields.io/badge/Claude%20Code-Supported-6B5B95?style=flat-square)
![Skills](https://img.shields.io/badge/Skills-10-0A7CFF?style=flat-square)

[中文](./README.md) | **English**

A curated collection of Agent Skills for Claude Code and similar agent environments — **10 skills across six categories**: thinking models, decision consulting, sales enablement, investment analysis, content design, and utilities.

> Distilled by [jiamu](https://github.com/isjiamu) from real daily workflows in sales, content creation, and decision consulting — every skill solves a real, recurring problem.

---

## Quick Start (30 seconds)

```bash
npx skills add https://github.com/isjiamu/jiamu-skills
```

Or paste this to any AI agent with shell access:

```text
Install jiamu-skills for me. Clone https://github.com/isjiamu/jiamu-skills to
~/Projects/jiamu-skills, then symlink each skill directory into ~/.claude/skills/,
and verify that SKILL.md is readable under every link.
```

To update an existing installation:

```text
Update jiamu-skills for me. Run git pull in the local repo and tell me the latest commit.
```

Once installed, just talk to your agent:

```text
I feel lost and can't articulate what's wrong.     → triggers gidlin-law
This problem keeps coming back, find the root cause. → triggers five-why
Help me analyze whether to change jobs, from multiple angles. → triggers six-thinking-hats
Start a peer advisory session — I'm torn about starting a business. → triggers peers-advisory-group
```

---

## 📦 Skills Overview

### 🧠 Thinking Models (4)

A complete thinking toolchain — from "can't state the problem" to "decision made".

| Skill | Model | What It Solves | Trigger Phrases |
|-------|-------|----------------|-----------------|
| [**gidlin-law**](./gidlin-law/) | Gidlin's Law | A problem well-stated is half-solved — six-step questioning turns vague troubles into clear problem statements | "help me clarify my thoughts", "I feel lost" |
| [**five-why**](./five-why/) | 5 Whys | Consecutive "why"s peel back symptoms to find systemic root causes and lasting fixes | "5 whys", "root cause analysis" |
| [**first-principles-mentor**](./first-principles-mentor/) | First Principles | Socratic questioning down to axioms, challenge industry conventions, rebuild from zero | "first principles", "analyze the essence" |
| [**six-thinking-hats**](./six-thinking-hats/) | Six Thinking Hats | De Bono's parallel thinking across six dimensions, with structured decision reports | "six thinking hats", "pros and cons", "analyze from multiple angles" |

**Recommended chain**:

```
gidlin-law (define the problem)
  → five-why (find root cause) or first-principles-mentor (deconstruct essence)
    → six-thinking-hats (multi-dimensional decision)
      → peers-advisory-group (deep advisory consultation)
```

### 💡 Decision Consulting (1)

| Skill | Description | Trigger Phrases |
|-------|-------------|-----------------|
| [**peers-advisory-group**](./peers-advisory-group/) | Virtual advisory board — Buffett, Gates, Musk & Jobs question and advise in rounds, backed by real-time Baidu search & encyclopedia data | "start a peer advisory session", "peers advisory" |

### 🎯 Sales Enablement (1)

| Skill | Description | Trigger Phrases |
|-------|-------------|-----------------|
| [**sales-ai-assistant**](./sales-ai-assistant/) | Describe a business scenario, get professional sales content — 25 scenarios (cold outreach, demo follow-up, battle cards, conversion analysis), plus the optimized prompt for learning | "write an email to my client", "competitive analysis" |

### 📈 Investment Analysis (1)

| Skill | Description | Trigger Phrases |
|-------|-------------|-----------------|
| [**stock-advisor**](./stock-advisor/) | A-share analysis pipeline: technical → fundamental → cross-validation → advisory board → magazine report, powered by free AKShare data | "analyze this stock", a ticker symbol, a candlestick screenshot |

### 🎨 Content Design (1)

| Skill | Description | Trigger Phrases |
|-------|-------------|-----------------|
| [**magazine-layout**](./magazine-layout/) | Turn plain text into magazine-style HTML pages — 12 visual styles, Tailwind responsive, multi-engine PDF export | "magazine layout", "format this article" |

### 🛠️ Utilities (2)

| Skill | Description | Trigger Phrases |
|-------|-------------|-----------------|
| [**video-downloader**](./video-downloader/) | Universal video downloader — 1000+ sites (YouTube, Bilibili, Twitter/X, TikTok), quality selection, audio extraction, subtitles | paste a video URL, "download this video" |
| [**gif-splitter**](./gif-splitter/) | Split GIFs exceeding WeChat's 300-frame upload limit — even splitting, frame-rate preserved, batch support | "GIF frame limit", "split this GIF" |

---

## Common Use Cases

| Task | Recommended Approach |
|------|---------------------|
| Mind is a mess, can't state the problem | Start with **gidlin-law** to define it, then pick a deeper tool |
| Same problem keeps recurring | **five-why** to trace the systemic root cause |
| Big decision (job change / startup / investment) | **six-thinking-hats** for six-dimension analysis, or **peers-advisory-group** for deep consultation |
| Challenge conventions, seek disruptive innovation | **first-principles-mentor** — down to axioms, rebuild from zero |
| Sales emails / proposals / battle cards | **sales-ai-assistant** — describe the scenario, get the content |
| Deep-dive a single A-share stock | **stock-advisor** — send a ticker or chart screenshot, full pipeline runs |
| Turn an article into a magazine page / PDF | **magazine-layout** — pick a style, get HTML |
| WeChat GIF upload fails | **gif-splitter** — auto-detect frames and split |

---

## Good Fit / Not a Fit

**✅ Good fit**: personal decisions & retrospectives / bulk sales content production / A-share stock research / visual article presentation / WeChat content-ops asset processing

**❌ Not a fit**: real-time collaborative editing / plain chatbots without shell access (thinking-model skills partially work; utility skills need to run scripts)

---

## 📥 Installation

### Option 1: One-liner (recommended)

```bash
# Install all skills
npx skills add https://github.com/isjiamu/jiamu-skills

# Or just one
npx skills add https://github.com/isjiamu/jiamu-skills --skill six-thinking-hats
```

### Option 2: Paste this to your AI

> Install the `jiamu-skills` collection for me. Steps:
>
> 1. Run `git clone https://github.com/isjiamu/jiamu-skills.git ~/Projects/jiamu-skills`
> 2. Symlink every skill directory (the ones containing SKILL.md) into `~/.claude/skills/`
> 3. Verify SKILL.md is readable under every link
> 4. Tell me which skills were installed — afterwards phrases like "start a peer advisory session" will trigger them

### Option 3: Manual

```bash
git clone https://github.com/isjiamu/jiamu-skills.git ~/Projects/jiamu-skills
for d in ~/Projects/jiamu-skills/*/; do
  [ -f "$d/SKILL.md" ] && ln -s "${d%/}" ~/.claude/skills/$(basename "$d")
done
```

> 💡 Prefer symlinks over copies: one `git pull` keeps every skill up to date.

---

## Platform Support

| Platform | Status | Notes |
|----------|--------|-------|
| Claude Code | ✅ Supported | Native Skill workflow, all skills available |
| Cursor / other local agents | ✅ Works | Needs file read/write and shell access |
| Plain chatbots | ⚠️ Partial | Thinking-model skills can be used as prompts; utility skills (gif-splitter etc.) require local scripts |

---

## 📁 Project Structure

```
jiamu-skills/
├── gidlin-law/               # 🧠 Gidlin's Law advisor
├── five-why/                 # 🧠 5 Whys root-cause advisor
├── first-principles-mentor/  # 🧠 First-principles mentor
├── six-thinking-hats/        # 🧠 Six Thinking Hats facilitator
├── peers-advisory-group/     # 💡 Peer advisory board
├── sales-ai-assistant/       # 🎯 Sales AI assistant (25 scenario templates)
├── stock-advisor/            # 📈 A-share stock advisor (analysis scripts + report templates)
├── magazine-layout/          # 🎨 Magazine layout engine (12 styles + PDF export)
├── video-downloader/         # 🛠️ Universal video downloader
├── gif-splitter/             # 🛠️ GIF splitter
├── CHANGELOG.md
├── LICENSE
└── README.md
```

Every skill directory contains `SKILL.md` (core instructions), optionally with `references/` (templates), `scripts/` (executables), and `README.md` (detailed docs).

---

## 🤝 Contributing

Issues and Pull Requests welcome!

**To contribute a new skill**:
1. Fork this repo and create a new skill directory
2. It must contain `SKILL.md` with name/description frontmatter and trigger scenarios
3. Put reference templates in `references/`, executable scripts in `scripts/`
4. Open a PR describing the skill's purpose and use cases

---

## 📊 Version History

- **v1.6.0** (2026-07-05) - Added the thinking-model series (4 skills); peers-advisory-group now integrates real-time Baidu data; magazine-layout standalone repo archived and merged
- **v1.5.0** (2026-03-28) - Added stock-advisor
- **v1.4.0** (2026-01-26) - Added gif-splitter
- **v1.3.0** (2026-01-23) - Added sales-ai-assistant

Full history in [CHANGELOG.md](./CHANGELOG.md)

---

## 📄 License

MIT License — see [LICENSE](./LICENSE)

## 👤 Author

**jiamu** ([@isjiamu](https://github.com/isjiamu)) — AI tools and productivity practitioner

---

<div align="center">

**⭐ If these skills help you, please give a Star! ⭐**

Made with ❤️ by jiamu

</div>
