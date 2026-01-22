# jiamu-skills

A curated collection of Claude Code skills for daily productivity workflows.

甲木常用的 Claude Code Skills 集合，包含日常工作流中积累的高效技能扩展。

## Skills

| Skill | Description |
|-------|-------------|
| [magazine-layout](./magazine-layout/) | 将文本内容转换为精美的杂志风格 HTML 页面，支持 12 种视觉风格和 PDF 导出 |
| [peers-advisory-group](./peers-advisory-group/) | 私董会专家助手，通过顶级商业领袖（巴菲特、盖茨、马斯克、乔布斯）的多轮提问帮助深入分析问题 |
| [video-downloader](./video-downloader/) | 通用视频下载工具，支持 YouTube、Bilibili、Twitter/X、TikTok 等 1000+ 网站，基于 yt-dlp |

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

### video-downloader

Trigger phrases:
- 提供任意视频链接（YouTube、Bilibili、Twitter 等）
- "下载这个视频"、"帮我下载"
- "download video"

Features:
- 支持 1000+ 网站（YouTube、Bilibili、Twitter/X、TikTok、Vimeo 等）
- 多种质量选择（360p 到 4K）
- 音频提取（MP3）
- 字幕下载
- WebM 转 MP4 格式转换

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
├── video-downloader/
│   ├── SKILL.md              # Core skill instructions
│   ├── scripts/
│   │   └── download.py       # Video download script
│   └── references/
│       └── platform-tips.md  # Platform-specific tips
├── LICENSE
└── README.md
```

## License

MIT License - see [LICENSE](./LICENSE) for details.

## Author

**jiamu** ([@isjiamu](https://github.com/isjiamu))
