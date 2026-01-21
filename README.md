# jiamu-skills

A curated collection of Claude Code skills for daily productivity workflows.

甲木常用的 Claude Code Skills 集合，包含日常工作流中积累的高效技能扩展。

## Skills

| Skill | Description |
|-------|-------------|
| [magazine-layout](./magazine-layout/) | 将文本内容转换为精美的杂志风格 HTML 页面，支持 12 种视觉风格和 PDF 导出 |
| [peers-advisory-group](./peers-advisory-group/) | 私董会专家助手，通过顶级商业领袖（巴菲特、盖茨、马斯克、乔布斯）的多轮提问帮助深入分析问题 |

## Installation

### Via Claude Code Plugin Marketplace

```bash
claude plugin marketplace add isjiamu/jiamu-skills
```

### Manual Installation

Clone this repository to your Claude Code skills directory:

```bash
git clone https://github.com/isjiamu/jiamu-skills.git ~/.claude/skills/jiamu-skills
```

## Usage

### magazine-layout

Trigger phrases:
- "杂志排版"、"杂志设计"、"文章排版"
- "magazine layout"
- 将文章转换为杂志风格 HTML

Features:
- 12 unique visual styles (Classic, Modern, Tech, Nature, etc.)
- Tailwind CSS-based responsive design
- PDF export support via multiple engines

### peers-advisory-group

Trigger phrases:
- "开始私董会"、"私董会"
- "peers advisory"

Features:
- Structured advisory process with 4 virtual advisors
- Multi-round questioning methodology
- Customizable advisor roster
- Optional magazine-style HTML report generation

## Structure

```
jiamu-skills/
├── magazine-layout/
│   ├── SKILL.md              # Core skill instructions
│   ├── references/
│   │   └── styles.md         # 12 style templates
│   └── scripts/
│       └── html_to_pdf.py    # PDF conversion script
├── peers-advisory-group/
│   ├── SKILL.md              # Core skill instructions
│   └── references/
│       ├── default-advisors.md
│       ├── feedback-template.md
│       ├── reflect-template.md
│       └── report-template.md
├── LICENSE
└── README.md
```

## License

MIT License - see [LICENSE](./LICENSE) for details.

## Author

**jiamu** ([@isjiamu](https://github.com/isjiamu))
