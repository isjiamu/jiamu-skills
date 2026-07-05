# magazine-layout-skill

A Claude Code skill that transforms text content into beautifully designed magazine-style HTML pages.

将文本内容转换为精美的杂志风格 HTML 页面，支持 12 种视觉风格和 PDF 导出。

## Features

- 12 unique visual styles (Classic Elegance, Modern Minimalist, Tech Magazine, etc.)
- Tailwind CSS-based responsive design
- Smart pagination for PDF export
- Multiple PDF export engines support (Playwright, WeasyPrint, wkhtmltopdf)

## Installation

```bash
claude plugin marketplace add isjiamu/magazine-layout-skill
```

## Usage

Trigger phrases:
- "杂志排版"、"杂志设计"、"文章排版"
- "magazine layout"
- 将文章/文本转换为杂志风格 HTML

## Available Styles

| Style | Best For |
|-------|----------|
| Classic Elegance | Literature, essays, memoirs |
| Modern Minimalist | Tech blogs, modern articles |
| Tech Magazine | Programming, technical content |
| Nature & Lifestyle | Travel, food, lifestyle |
| Bold Editorial | Opinion pieces, commentary |
| Vintage Retro | Historical, nostalgic content |
| Corporate Professional | Business reports, corporate docs |
| Creative Art | Design, artistic content |
| Academic Journal | Research papers, academic writing |
| Fashion Luxe | Fashion, luxury content |
| News & Report | News articles, journalism |
| Dark Mode Tech | Developer content |

## Structure

```
magazine-layout-skill/
├── SKILL.md              # Core skill instructions
├── references/
│   └── styles.md         # 12 style templates with full CSS
└── scripts/
    └── html_to_pdf.py    # PDF conversion script
```

## License

MIT License

## Author

**jiamu** ([@isjiamu](https://github.com/isjiamu))
