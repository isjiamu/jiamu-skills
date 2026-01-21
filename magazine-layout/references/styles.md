# Magazine Layout Styles Reference

This document contains 12 distinct magazine layout styles. Each style has its own visual identity, color scheme, typography, and layout characteristics.

## Table of Contents

1. [Smart Pagination CSS (Required)](#smart-pagination-css-required)
2. [Classic Elegance](#1-classic-elegance)
3. [Modern Minimalist](#2-modern-minimalist)
4. [Tech Magazine](#3-tech-magazine)
5. [Nature & Lifestyle](#4-nature--lifestyle)
6. [Bold Editorial](#5-bold-editorial)
7. [Vintage Retro](#6-vintage-retro)
8. [Corporate Professional](#7-corporate-professional)
9. [Creative Art](#8-creative-art)
10. [Academic Journal](#9-academic-journal)
11. [Fashion Luxe](#10-fashion-luxe)
12. [News & Report](#11-news--report)
13. [Dark Mode Tech](#12-dark-mode-tech)

---

## Smart Pagination CSS (Required)

**IMPORTANT**: Always include this CSS in every generated HTML to ensure proper PDF page breaks. This prevents content from being awkwardly cut in the middle of elements.

```css
/* ========== 智能分页控制 - 必须包含 ========== */
/* 打印/PDF模式 */
@media print {
  /* 标题类：后面禁止分页，确保标题与内容在一起 */
  h1, h2, h3, h4,
  .chapter-number,
  .chapter-title,
  .section-header,
  .method-title {
    page-break-after: avoid;
    break-after: avoid;
  }

  /* 块级元素：内部禁止分页 */
  blockquote,
  .highlight-box,
  .key-point,
  .abstract,
  .stage-item,
  .question-item,
  .game-element,
  .numbered-item,
  .list-item,
  .code-block,
  .terminal,
  figure,
  img,
  table,
  .card {
    page-break-inside: avoid;
    break-inside: avoid;
  }

  /* 列表容器：尽量保持完整 */
  ul, ol,
  .numbered-list,
  .question-list,
  .stage-list {
    page-break-inside: avoid;
    break-inside: avoid;
  }

  /* 分隔线后面禁止立即分页 */
  .elegant-divider,
  .divider,
  .section-divider,
  .nature-divider,
  .vintage-divider,
  .art-divider,
  hr {
    page-break-after: avoid;
    break-after: avoid;
  }

  /* 方法论/重要区块保持完整 */
  .method-section,
  .inner-border {
    page-break-inside: avoid;
    break-inside: avoid;
  }

  /* 段落：孤行寡行控制 - 至少保留3行 */
  p {
    orphans: 3;
    widows: 3;
  }

  /* 可选：章节从新页开始 */
  section.new-page {
    page-break-before: always;
    break-before: always;
  }
}

/* 非打印时也应用，确保 Playwright/PDF 渲染一致 */
blockquote, .highlight-box, .key-point, .abstract,
.stage-item, .question-item, .game-element,
.code-block, .terminal, .stage-list, .question-list,
figure, img, table, .card {
  page-break-inside: avoid;
  break-inside: avoid;
}

h1, h2, h3, h4, .chapter-number, .chapter-title,
.section-header, .method-title {
  page-break-after: avoid;
  break-after: avoid;
}

.elegant-divider, .divider, .section-divider,
.nature-divider, .vintage-divider, .art-divider, hr {
  page-break-after: avoid;
  break-after: avoid;
}
```

### Pagination Rules Explained

| CSS Property | Effect | Use Case |
|--------------|--------|----------|
| `page-break-inside: avoid` | Prevents page break inside element | Quotes, cards, lists |
| `page-break-after: avoid` | Prevents page break after element | Headings, dividers |
| `page-break-before: always` | Forces new page before element | New chapters |
| `orphans: 3` | Minimum lines at bottom of page | Paragraphs |
| `widows: 3` | Minimum lines at top of page | Paragraphs |

---

## 1. Classic Elegance

**Description**: Traditional magazine style with serif fonts, warm tones, and refined typography. Perfect for literature, essays, and thoughtful content.

**Color Palette**:
- Primary: `#2c3e50` (Dark Blue-Gray)
- Secondary: `#8b7355` (Warm Brown)
- Background: `#faf8f5` (Cream)
- Accent: `#c9a959` (Gold)

**Typography**:
- Headings: `'Playfair Display', serif`
- Body: `'Source Serif Pro', serif`
- Chinese: `'Noto Serif SC', serif`

**Key Features**:
- Drop cap on first paragraph
- Elegant dividers with ornamental symbols
- Pull quotes with decorative borders
- Generous margins and line height (1.9)

**Template**:
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{TITLE}}</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Source+Serif+Pro:wght@300;400;600&family=Noto+Serif+SC:wght@400;600;700&display=swap" rel="stylesheet">
<style>
/* ========== 智能分页控制 ========== */
@media print {
  h1, h2, h3, .chapter-number, .chapter-title { page-break-after: avoid; break-after: avoid; }
  blockquote, .highlight-box, .stage-item, .question-item, .numbered-item, .list-item, figure, img { page-break-inside: avoid; break-inside: avoid; }
  .numbered-list, .question-list, .stage-list { page-break-inside: avoid; break-inside: avoid; }
  .elegant-divider { page-break-after: avoid; break-after: avoid; }
  .method-section { page-break-inside: avoid; break-inside: avoid; }
  p { orphans: 3; widows: 3; }
}
blockquote, .highlight-box, .stage-item, .question-item, .stage-list, .question-list { page-break-inside: avoid; break-inside: avoid; }
h1, h2, h3, .chapter-number, .chapter-title { page-break-after: avoid; break-after: avoid; }
.elegant-divider { page-break-after: avoid; break-after: avoid; }

/* ========== 主题样式 ========== */
:root {
  --color-primary: #2c3e50;
  --color-secondary: #8b7355;
  --color-bg: #faf8f5;
  --color-accent: #c9a959;
}
body { font-family: 'Source Serif Pro', 'Noto Serif SC', serif; background: #e8e4de; color: #333; }
h1, h2, h3 { font-family: 'Playfair Display', 'Noto Serif SC', serif; color: var(--color-primary); }
.magazine-page {
  width: 100%;
  max-width: 800px;
  background: var(--color-bg);
  padding: 60px 80px;
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.15);
  margin: 0 auto;
}
.drop-cap::first-letter {
  float: left;
  font-size: 4.5em;
  line-height: 0.8;
  margin: 0.1em 0.15em 0 0;
  font-family: 'Playfair Display', serif;
  color: var(--color-accent);
  font-weight: 700;
}
.elegant-divider {
  display: flex;
  align-items: center;
  margin: 2.5rem 0;
}
.elegant-divider::before, .elegant-divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: linear-gradient(to right, transparent, var(--color-secondary), transparent);
}
.elegant-divider span {
  padding: 0 1.5rem;
  color: var(--color-accent);
  font-size: 1.5rem;
}
blockquote {
  border-left: 3px solid var(--color-accent);
  padding-left: 2rem;
  margin: 2rem 0;
  font-style: italic;
  color: var(--color-secondary);
}
.content { line-height: 1.9; letter-spacing: 0.02em; color: #333; }
.content p { margin-bottom: 1.5rem; }
.highlight-box {
  background: linear-gradient(135deg, rgba(201,169,89,0.1) 0%, rgba(139,115,85,0.1) 100%);
  padding: 1.5rem 2rem;
  border-radius: 0.5rem;
  margin: 2rem 0;
  border-left: 4px solid var(--color-accent);
}
.chapter-number { font-family: 'Playfair Display', serif; font-size: 3rem; color: var(--color-accent); font-weight: 700; }
.chapter-title { font-size: 1.6rem; font-weight: 700; margin-bottom: 1.5rem; border-bottom: 2px solid var(--color-accent); padding-bottom: 0.5rem; }
.numbered-item { padding-left: 2rem; position: relative; margin-bottom: 1rem; }
.numbered-item::before { content: counter(item) "."; counter-increment: item; position: absolute; left: 0; color: var(--color-accent); font-weight: 600; }
.numbered-list { counter-reset: item; }
.list-item { padding-left: 1.5rem; position: relative; margin-bottom: 0.75rem; }
.list-item::before { content: '•'; position: absolute; left: 0; color: var(--color-accent); }
</style>
</head>
<body class="min-h-screen py-8 px-4">
<article class="magazine-page">
{{CONTENT}}
</article>
</body>
</html>
```

---

## 2. Modern Minimalist

**Description**: Clean, spacious design with sans-serif fonts. Emphasizes white space and typography hierarchy.

**Color Palette**:
- Primary: `#111827` (Near Black)
- Secondary: `#6b7280` (Gray)
- Background: `#ffffff` (Pure White)
- Accent: `#3b82f6` (Blue)

**Typography**:
- Headings: `'Inter', sans-serif`
- Body: `'Inter', sans-serif`
- Chinese: `'Noto Sans SC', sans-serif`

**Template**:
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{TITLE}}</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Noto+Sans+SC:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>
/* ========== 智能分页控制 ========== */
@media print {
  h1, h2, h3 { page-break-after: avoid; break-after: avoid; }
  blockquote, .highlight-box, .card, figure, img { page-break-inside: avoid; break-inside: avoid; }
  .divider { page-break-after: avoid; break-after: avoid; }
  p { orphans: 3; widows: 3; }
}
blockquote, .highlight-box, .card { page-break-inside: avoid; break-inside: avoid; }
h1, h2, h3 { page-break-after: avoid; break-after: avoid; }

/* ========== 主题样式 ========== */
body { font-family: 'Inter', 'Noto Sans SC', sans-serif; background: #f3f4f6; }
.magazine-page {
  width: 100%;
  max-width: 800px;
  background: #ffffff;
  padding: 80px;
  box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
  margin: 0 auto;
}
h1 { font-size: 3rem; font-weight: 700; letter-spacing: -0.02em; line-height: 1.1; color: #111827; margin-bottom: 1.5rem; }
h2 { font-size: 1.5rem; font-weight: 600; color: #374151; margin: 2rem 0 1rem; }
.subtitle { font-size: 1.25rem; color: #6b7280; font-weight: 300; margin-bottom: 3rem; }
.content { line-height: 1.75; color: #374151; font-weight: 400; }
.content p { margin-bottom: 1.5rem; }
.divider { height: 1px; background: #e5e7eb; margin: 3rem 0; }
blockquote {
  padding: 1.5rem 2rem;
  background: #f9fafb;
  border-radius: 0.5rem;
  margin: 2rem 0;
  color: #4b5563;
  border-left: 4px solid #3b82f6;
}
.accent { color: #3b82f6; }
.highlight-box { background: #f3f4f6; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0; }
</style>
</head>
<body class="min-h-screen py-8 px-4">
<article class="magazine-page">
{{CONTENT}}
</article>
</body>
</html>
```

---

## 3. Tech Magazine

**Description**: Futuristic design with gradient accents and code-friendly typography.

**Color Palette**:
- Primary: `#0f172a` (Dark Navy)
- Secondary: `#64748b` (Slate)
- Background: `#f8fafc` (Light Gray)
- Accent: Gradient `#6366f1` to `#8b5cf6` (Indigo to Purple)

**Typography**:
- Headings: `'Space Grotesk', sans-serif`
- Body: `'IBM Plex Sans', sans-serif`
- Code: `'Fira Code', monospace`

**Template**:
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{TITLE}}</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=IBM+Plex+Sans:wght@300;400;500&family=Fira+Code:wght@400;500&family=Noto+Sans+SC:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>
/* ========== 智能分页控制 ========== */
@media print {
  h1, h2, h3 { page-break-after: avoid; break-after: avoid; }
  blockquote, .highlight-box, .code-block, figure { page-break-inside: avoid; break-inside: avoid; }
  p { orphans: 3; widows: 3; }
}
blockquote, .highlight-box, .code-block { page-break-inside: avoid; break-inside: avoid; }
h1, h2, h3 { page-break-after: avoid; break-after: avoid; }

/* ========== 主题样式 ========== */
body { font-family: 'IBM Plex Sans', 'Noto Sans SC', sans-serif; background: #e2e8f0; }
h1, h2, h3 { font-family: 'Space Grotesk', 'Noto Sans SC', sans-serif; }
code { font-family: 'Fira Code', monospace; }
.magazine-page {
  width: 100%;
  max-width: 800px;
  background: #f8fafc;
  padding: 60px 70px;
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.15);
  margin: 0 auto;
  position: relative;
}
.gradient-bar {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #6366f1, #8b5cf6, #a855f7);
}
h1 { font-size: 2.5rem; font-weight: 700; color: #0f172a; margin-bottom: 0.5rem; }
.tag {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  color: white;
  font-size: 0.75rem;
  font-weight: 500;
  border-radius: 9999px;
  margin-bottom: 1rem;
}
.content { line-height: 1.8; color: #334155; }
.content p { margin-bottom: 1.25rem; }
.code-block {
  background: #1e293b;
  color: #e2e8f0;
  padding: 1.5rem;
  border-radius: 0.75rem;
  margin: 1.5rem 0;
  font-family: 'Fira Code', monospace;
  font-size: 0.875rem;
  overflow-x: auto;
}
blockquote {
  border-left: 4px solid;
  border-image: linear-gradient(to bottom, #6366f1, #8b5cf6) 1;
  padding-left: 1.5rem;
  margin: 2rem 0;
  color: #475569;
}
.highlight-box {
  background: linear-gradient(135deg, rgba(99,102,241,0.1), rgba(139,92,246,0.1));
  padding: 1.5rem;
  border-radius: 0.75rem;
  margin: 1.5rem 0;
}
</style>
</head>
<body class="min-h-screen py-8 px-4">
<article class="magazine-page">
<div class="gradient-bar"></div>
{{CONTENT}}
</article>
</body>
</html>
```

---

## 4. Nature & Lifestyle

**Description**: Organic, earthy design with natural colors and flowing typography.

**Color Palette**:
- Primary: `#365314` (Forest Green)
- Secondary: `#78716c` (Stone)
- Background: `#fefce8` (Warm Cream)
- Accent: `#84cc16` (Lime)

**Template**:
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{TITLE}}</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@400;700&family=Nunito:wght@300;400;600&family=Caveat:wght@400;700&family=Noto+Serif+SC:wght@400;700&display=swap" rel="stylesheet">
<style>
/* ========== 智能分页控制 ========== */
@media print {
  h1, h2, h3 { page-break-after: avoid; break-after: avoid; }
  blockquote, .highlight-box, figure { page-break-inside: avoid; break-inside: avoid; }
  .nature-divider { page-break-after: avoid; break-after: avoid; }
  p { orphans: 3; widows: 3; }
}
blockquote, .highlight-box { page-break-inside: avoid; break-inside: avoid; }
h1, h2, h3 { page-break-after: avoid; break-after: avoid; }

/* ========== 主题样式 ========== */
body { font-family: 'Nunito', 'Noto Sans SC', sans-serif; background: #fefce8; }
h1, h2, h3 { font-family: 'Fraunces', 'Noto Serif SC', serif; color: #365314; }
.handwritten { font-family: 'Caveat', cursive; }
.magazine-page {
  width: 100%;
  max-width: 800px;
  background: linear-gradient(180deg, #fefce8 0%, #fef9c3 100%);
  padding: 60px 80px;
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.1);
  margin: 0 auto;
  border-radius: 0.5rem;
}
h1 { font-size: 2.75rem; font-weight: 700; line-height: 1.2; margin-bottom: 1rem; }
.subtitle { font-family: 'Caveat', cursive; font-size: 1.5rem; color: #84cc16; margin-bottom: 2rem; }
.content { line-height: 1.85; color: #44403c; }
.content p { margin-bottom: 1.5rem; }
.nature-divider {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 2.5rem 0;
  color: #84cc16;
  font-size: 1.5rem;
}
blockquote {
  background: rgba(132, 204, 22, 0.1);
  border-radius: 1rem;
  padding: 2rem;
  margin: 2rem 0;
  border-left: 4px solid #84cc16;
  color: #365314;
  font-style: italic;
}
.highlight { background: linear-gradient(180deg, transparent 60%, rgba(132,204,22,0.3) 60%); }
</style>
</head>
<body class="min-h-screen py-8 px-4">
<article class="magazine-page">
{{CONTENT}}
</article>
</body>
</html>
```

---

## 5. Bold Editorial

**Description**: High-contrast, impactful design with oversized typography.

**Color Palette**:
- Primary: `#000000` (Black)
- Secondary: `#525252` (Gray)
- Background: `#ffffff` (White)
- Accent: `#ef4444` (Red)

**Template**:
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{TITLE}}</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Roboto:wght@300;400;700&family=Oswald:wght@400;700&family=Noto+Sans+SC:wght@300;400;700&display=swap" rel="stylesheet">
<style>
/* ========== 智能分页控制 ========== */
@media print {
  h1, h2, h3, .section-header { page-break-after: avoid; break-after: avoid; }
  blockquote, .highlight-box, figure { page-break-inside: avoid; break-inside: avoid; }
  .red-line { page-break-after: avoid; break-after: avoid; }
  p { orphans: 3; widows: 3; }
}
blockquote, .highlight-box { page-break-inside: avoid; break-inside: avoid; }
h1, h2, h3, .section-header { page-break-after: avoid; break-after: avoid; }

/* ========== 主题样式 ========== */
body { font-family: 'Roboto', 'Noto Sans SC', sans-serif; background: #e5e5e5; }
h1 { font-family: 'Bebas Neue', 'Noto Sans SC', sans-serif; }
h2, h3 { font-family: 'Oswald', 'Noto Sans SC', sans-serif; }
.magazine-page {
  width: 100%;
  max-width: 800px;
  background: #ffffff;
  padding: 50px 60px;
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.2);
  margin: 0 auto;
}
h1 {
  font-size: 4rem;
  letter-spacing: 0.05em;
  line-height: 0.95;
  color: #000;
  margin-bottom: 1.5rem;
  text-transform: uppercase;
}
.red-line { width: 80px; height: 6px; background: #ef4444; margin-bottom: 2rem; }
.byline {
  font-family: 'Oswald', sans-serif;
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #525252;
  margin-bottom: 2rem;
}
.content { line-height: 1.7; color: #262626; font-weight: 300; }
.content p { margin-bottom: 1.25rem; }
blockquote {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 2.5rem;
  line-height: 1.1;
  color: #000;
  padding: 2rem 0;
  margin: 2rem 0;
  border-top: 4px solid #000;
  border-bottom: 4px solid #000;
}
.red-text { color: #ef4444; }
.section-header {
  font-family: 'Oswald', sans-serif;
  font-size: 1.25rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: #ef4444;
  margin: 2.5rem 0 1rem;
}
</style>
</head>
<body class="min-h-screen py-8 px-4">
<article class="magazine-page">
{{CONTENT}}
</article>
</body>
</html>
```

---

## 6. Vintage Retro

**Description**: Nostalgic design with sepia tones and ornate borders.

**Color Palette**:
- Primary: `#451a03` (Deep Brown)
- Secondary: `#92400e` (Amber)
- Background: `#fef3c7` (Parchment)
- Accent: `#b45309` (Burnt Orange)

**Template**:
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{TITLE}}</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Lora:wght@400;500;700&family=Special+Elite&family=Noto+Serif+SC:wght@400;700&display=swap" rel="stylesheet">
<style>
/* ========== 智能分页控制 ========== */
@media print {
  h1, h2 { page-break-after: avoid; break-after: avoid; }
  blockquote, .inner-border, figure { page-break-inside: avoid; break-inside: avoid; }
  .vintage-divider { page-break-after: avoid; break-after: avoid; }
  p { orphans: 3; widows: 3; }
}
blockquote { page-break-inside: avoid; break-inside: avoid; }
h1, h2 { page-break-after: avoid; break-after: avoid; }

/* ========== 主题样式 ========== */
body { font-family: 'Lora', 'Noto Serif SC', serif; background: #fde68a; }
h1, h2 { font-family: 'Abril Fatface', 'Noto Serif SC', serif; }
.typewriter { font-family: 'Special Elite', monospace; }
.magazine-page {
  width: 100%;
  max-width: 800px;
  background: #fef3c7;
  padding: 50px;
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.2);
  margin: 0 auto;
}
.inner-border { border: 2px solid #92400e; padding: 40px; }
h1 { font-size: 3rem; color: #451a03; text-align: center; margin-bottom: 0.5rem; }
.vintage-divider {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 1.5rem 0;
}
.vintage-divider::before, .vintage-divider::after { content: ''; flex: 1; height: 2px; background: #92400e; }
.vintage-divider span { padding: 0 1rem; color: #b45309; font-size: 1.25rem; }
.date-line {
  font-family: 'Special Elite', monospace;
  text-align: center;
  color: #92400e;
  letter-spacing: 0.2em;
  margin-bottom: 2rem;
}
.content { line-height: 1.8; color: #451a03; text-align: justify; }
.content p { margin-bottom: 1.25rem; text-indent: 2rem; }
blockquote {
  border: 1px solid #92400e;
  padding: 1.5rem;
  margin: 2rem 1rem;
  background: rgba(180, 83, 9, 0.05);
  font-style: italic;
}
.drop-cap::first-letter {
  float: left;
  font-family: 'Abril Fatface', serif;
  font-size: 4rem;
  line-height: 0.8;
  margin: 0.1em 0.1em 0 0;
  color: #b45309;
}
</style>
</head>
<body class="min-h-screen py-8 px-4">
<article class="magazine-page">
<div class="inner-border">
{{CONTENT}}
</div>
</article>
</body>
</html>
```

---

## 7. Corporate Professional

**Description**: Clean, professional design for business content.

**Color Palette**:
- Primary: `#1e3a5f` (Navy)
- Secondary: `#64748b` (Slate)
- Background: `#ffffff` (White)
- Accent: `#0ea5e9` (Sky Blue)

**Template**:
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{TITLE}}</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Open+Sans:wght@300;400;600&family=Roboto+Mono:wght@400;500&family=Noto+Sans+SC:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>
/* ========== 智能分页控制 ========== */
@media print {
  h1, h2, h3 { page-break-after: avoid; break-after: avoid; }
  blockquote, .key-point, .highlight-box, figure, table { page-break-inside: avoid; break-inside: avoid; }
  p { orphans: 3; widows: 3; }
}
blockquote, .key-point, .highlight-box { page-break-inside: avoid; break-inside: avoid; }
h1, h2, h3 { page-break-after: avoid; break-after: avoid; }

/* ========== 主题样式 ========== */
body { font-family: 'Open Sans', 'Noto Sans SC', sans-serif; background: #e2e8f0; }
h1, h2, h3 { font-family: 'Montserrat', 'Noto Sans SC', sans-serif; }
.mono { font-family: 'Roboto Mono', monospace; }
.magazine-page {
  width: 100%;
  max-width: 800px;
  background: #ffffff;
  padding: 60px 70px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.1);
  margin: 0 auto;
}
.header-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 1rem;
  border-bottom: 3px solid #1e3a5f;
  margin-bottom: 2rem;
}
h1 { font-size: 2rem; font-weight: 700; color: #1e3a5f; margin-bottom: 0.5rem; }
.subtitle { color: #64748b; font-size: 1rem; margin-bottom: 2rem; }
.content { line-height: 1.75; color: #334155; }
.content p { margin-bottom: 1.25rem; }
h2 { font-size: 1.25rem; font-weight: 600; color: #1e3a5f; margin: 2rem 0 1rem; padding-left: 1rem; border-left: 4px solid #0ea5e9; }
blockquote {
  background: #f1f5f9;
  padding: 1.5rem;
  border-radius: 0.5rem;
  margin: 1.5rem 0;
  border-left: 4px solid #0ea5e9;
}
.key-point {
  background: linear-gradient(135deg, #1e3a5f 0%, #0ea5e9 100%);
  color: white;
  padding: 1.5rem;
  border-radius: 0.5rem;
  margin: 1.5rem 0;
}
</style>
</head>
<body class="min-h-screen py-8 px-4">
<article class="magazine-page">
{{CONTENT}}
</article>
</body>
</html>
```

---

## 8. Creative Art

**Description**: Artistic design with asymmetric layouts and bold colors.

**Color Palette**:
- Primary: `#1f2937` (Charcoal)
- Accent: `#f59e0b` (Amber)
- Accent 2: `#ec4899` (Pink)

**Template**:
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{TITLE}}</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Righteous&family=Quicksand:wght@300;400;500;700&family=Permanent+Marker&family=Noto+Sans+SC:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>
/* ========== 智能分页控制 ========== */
@media print {
  h1, h2 { page-break-after: avoid; break-after: avoid; }
  blockquote, .highlight-box, figure { page-break-inside: avoid; break-inside: avoid; }
  .art-divider { page-break-after: avoid; break-after: avoid; }
  p { orphans: 3; widows: 3; }
}
blockquote, .highlight-box { page-break-inside: avoid; break-inside: avoid; }
h1, h2 { page-break-after: avoid; break-after: avoid; }

/* ========== 主题样式 ========== */
body { font-family: 'Quicksand', 'Noto Sans SC', sans-serif; background: #d1d5db; }
h1, h2 { font-family: 'Righteous', 'Noto Sans SC', sans-serif; }
.marker { font-family: 'Permanent Marker', cursive; }
.magazine-page {
  width: 100%;
  max-width: 800px;
  background: #f3f4f6;
  padding: 50px 60px;
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.15);
  margin: 0 auto;
  position: relative;
  overflow: hidden;
}
.color-block {
  position: absolute;
  top: -50px;
  right: -50px;
  width: 200px;
  height: 200px;
  background: #f59e0b;
  transform: rotate(15deg);
  opacity: 0.3;
}
h1 { font-size: 3.5rem; color: #1f2937; line-height: 1.1; margin-bottom: 1rem; position: relative; z-index: 1; }
.subtitle {
  font-family: 'Permanent Marker', cursive;
  color: #f59e0b;
  font-size: 1.25rem;
  margin-bottom: 2rem;
  transform: rotate(-2deg);
  display: inline-block;
}
.content { line-height: 1.8; color: #374151; position: relative; z-index: 1; }
.content p { margin-bottom: 1.5rem; }
blockquote {
  background: #1f2937;
  color: #f3f4f6;
  padding: 2rem;
  margin: 2rem -20px;
  transform: rotate(-1deg);
  font-size: 1.125rem;
}
.art-divider {
  height: 4px;
  background: linear-gradient(90deg, #f59e0b, #ec4899, #8b5cf6);
  margin: 2rem 0;
  border-radius: 2px;
}
</style>
</head>
<body class="min-h-screen py-8 px-4">
<article class="magazine-page">
<div class="color-block"></div>
{{CONTENT}}
</article>
</body>
</html>
```

---

## 9. Academic Journal

**Description**: Scholarly design with structured layouts for research content.

**Color Palette**:
- Primary: `#1e293b` (Dark Slate)
- Secondary: `#475569` (Slate)
- Accent: `#0369a1` (Blue)

**Template**:
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{TITLE}}</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Source+Sans+Pro:wght@300;400;600&family=Source+Serif+Pro:wght@400;600&family=Noto+Serif+SC:wght@400;700&family=Noto+Sans+SC:wght@300;400;600&display=swap" rel="stylesheet">
<style>
/* ========== 智能分页控制 ========== */
@media print {
  h1, h2, h3 { page-break-after: avoid; break-after: avoid; }
  blockquote, .abstract, figure, table { page-break-inside: avoid; break-inside: avoid; }
  .footnote { page-break-inside: avoid; break-inside: avoid; }
  p { orphans: 3; widows: 3; }
}
blockquote, .abstract { page-break-inside: avoid; break-inside: avoid; }
h1, h2, h3 { page-break-after: avoid; break-after: avoid; }

/* ========== 主题样式 ========== */
body { font-family: 'Source Sans Pro', 'Noto Sans SC', sans-serif; background: #e5e7eb; }
h1, h2, h3 { font-family: 'Merriweather', 'Noto Serif SC', serif; }
.magazine-page {
  width: 100%;
  max-width: 800px;
  background: #ffffff;
  padding: 50px 60px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  margin: 0 auto;
}
.journal-header { text-align: center; padding-bottom: 1.5rem; border-bottom: 1px solid #e2e8f0; margin-bottom: 2rem; }
.journal-name { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.2em; color: #64748b; margin-bottom: 1rem; }
h1 { font-size: 1.75rem; font-weight: 700; color: #1e293b; line-height: 1.3; margin-bottom: 1rem; }
.authors { color: #475569; font-size: 1rem; margin-bottom: 0.5rem; }
.abstract {
  background: #f8fafc;
  padding: 1.5rem;
  margin: 2rem 0;
  border-left: 3px solid #0369a1;
}
.abstract-title { font-weight: 600; color: #0369a1; margin-bottom: 0.5rem; text-transform: uppercase; font-size: 0.875rem; }
.abstract-text { font-family: 'Source Serif Pro', serif; line-height: 1.7; color: #334155; font-size: 0.95rem; }
.content { line-height: 1.7; color: #334155; }
.content p { margin-bottom: 1rem; text-align: justify; }
h2 { font-size: 1.25rem; color: #1e293b; margin: 2rem 0 1rem; }
.citation { color: #0369a1; }
.footnote { font-size: 0.8rem; color: #64748b; border-top: 1px solid #e2e8f0; margin-top: 2rem; padding-top: 1rem; }
</style>
</head>
<body class="min-h-screen py-8 px-4">
<article class="magazine-page">
{{CONTENT}}
</article>
</body>
</html>
```

---

## 10. Fashion Luxe

**Description**: Luxurious design with elegant typography and gold accents.

**Color Palette**:
- Primary: `#18181b` (Near Black)
- Secondary: `#71717a` (Zinc)
- Accent: `#d4af37` (Gold)

**Template**:
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{TITLE}}</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Raleway:wght@300;400;500&family=Italiana&family=Noto+Serif+SC:wght@400;700&family=Noto+Sans+SC:wght@300;400;500&display=swap" rel="stylesheet">
<style>
/* ========== 智能分页控制 ========== */
@media print {
  h1, h2 { page-break-after: avoid; break-after: avoid; }
  blockquote, figure { page-break-inside: avoid; break-inside: avoid; }
  .section-divider, .gold-line { page-break-after: avoid; break-after: avoid; }
  p { orphans: 3; widows: 3; }
}
blockquote { page-break-inside: avoid; break-inside: avoid; }
h1, h2 { page-break-after: avoid; break-after: avoid; }

/* ========== 主题样式 ========== */
body { font-family: 'Raleway', 'Noto Sans SC', sans-serif; background: #a1a1aa; }
h1, h2 { font-family: 'Cinzel', 'Noto Serif SC', serif; }
.italiana { font-family: 'Italiana', serif; }
.magazine-page {
  width: 100%;
  max-width: 800px;
  background: #fafafa;
  padding: 70px 80px;
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.15);
  margin: 0 auto;
}
.gold-line { width: 60px; height: 2px; background: #d4af37; margin: 0 auto 2rem; }
h1 {
  font-size: 2.5rem;
  font-weight: 400;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  text-align: center;
  color: #18181b;
  margin-bottom: 0.5rem;
}
.subtitle { font-family: 'Italiana', serif; font-size: 1.25rem; text-align: center; color: #71717a; margin-bottom: 1rem; }
.content { line-height: 1.9; color: #3f3f46; font-weight: 300; }
.content p { margin-bottom: 1.5rem; }
blockquote {
  text-align: center;
  padding: 3rem 2rem;
  margin: 2.5rem 0;
  position: relative;
}
blockquote::before {
  content: '"';
  font-family: 'Cinzel', serif;
  font-size: 4rem;
  color: #d4af37;
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
}
blockquote p { font-family: 'Italiana', serif; font-size: 1.5rem; color: #18181b; margin-top: 1rem; }
.section-divider {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 2.5rem 0;
}
.section-divider::before, .section-divider::after { content: ''; width: 100px; height: 1px; background: #d4d4d8; }
.section-divider span { width: 8px; height: 8px; background: #d4af37; transform: rotate(45deg); margin: 0 1rem; }
</style>
</head>
<body class="min-h-screen py-8 px-4">
<article class="magazine-page">
{{CONTENT}}
</article>
</body>
</html>
```

---

## 11. News & Report

**Description**: Newspaper-style layout with clear hierarchy.

**Color Palette**:
- Primary: `#171717` (Black)
- Secondary: `#525252` (Gray)
- Accent: `#dc2626` (Red)

**Template**:
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{TITLE}}</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=PT+Sans:wght@400;700&family=PT+Sans+Narrow:wght@400;700&family=Noto+Serif+SC:wght@400;700&family=Noto+Sans+SC:wght@400;700&display=swap" rel="stylesheet">
<style>
/* ========== 智能分页控制 ========== */
@media print {
  h1, h2 { page-break-after: avoid; break-after: avoid; }
  blockquote, .pull-quote, figure { page-break-inside: avoid; break-inside: avoid; }
  .masthead { page-break-after: avoid; break-after: avoid; }
  p { orphans: 3; widows: 3; }
}
blockquote, .pull-quote { page-break-inside: avoid; break-inside: avoid; }
h1, h2 { page-break-after: avoid; break-after: avoid; }

/* ========== 主题样式 ========== */
body { font-family: 'PT Sans', 'Noto Sans SC', sans-serif; background: #a8a29e; }
h1, h2 { font-family: 'Libre Baskerville', 'Noto Serif SC', serif; }
.narrow { font-family: 'PT Sans Narrow', sans-serif; }
.magazine-page {
  width: 100%;
  max-width: 800px;
  background: #fafaf9;
  padding: 40px 50px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  margin: 0 auto;
}
.masthead { text-align: center; padding-bottom: 0.75rem; border-bottom: 3px double #171717; margin-bottom: 1.5rem; }
.newspaper-name { font-family: 'Libre Baskerville', serif; font-size: 2rem; font-weight: 700; }
.breaking {
  background: #dc2626;
  color: white;
  padding: 0.25rem 0.75rem;
  font-family: 'PT Sans Narrow', sans-serif;
  font-weight: 700;
  text-transform: uppercase;
  font-size: 0.75rem;
  display: inline-block;
  margin-bottom: 1rem;
}
h1 { font-size: 2.25rem; font-weight: 700; line-height: 1.15; color: #171717; margin-bottom: 0.75rem; }
.lead { font-size: 1.125rem; color: #525252; line-height: 1.5; margin-bottom: 1rem; padding-bottom: 1rem; border-bottom: 1px solid #d6d3d1; }
.byline { font-family: 'PT Sans Narrow', sans-serif; font-size: 0.875rem; color: #525252; margin-bottom: 1.5rem; }
.content { line-height: 1.7; color: #292524; }
.content p { margin-bottom: 1rem; }
.pull-quote {
  float: right;
  width: 45%;
  margin: 0 0 1rem 1.5rem;
  padding: 1rem;
  border-top: 3px solid #dc2626;
  border-bottom: 3px solid #dc2626;
  font-family: 'Libre Baskerville', serif;
  font-size: 1.25rem;
  font-style: italic;
}
h2 { font-size: 1.25rem; margin: 1.5rem 0 0.75rem; color: #171717; }
</style>
</head>
<body class="min-h-screen py-8 px-4">
<article class="magazine-page">
{{CONTENT}}
</article>
</body>
</html>
```

---

## 12. Dark Mode Tech

**Description**: Dark-themed design for developer content.

**Color Palette**:
- Primary: `#f8fafc` (Light Text)
- Background: `#0f172a` (Dark Navy)
- Accent: `#22d3ee` (Cyan)
- Accent 2: `#a78bfa` (Purple)

**Template**:
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{TITLE}}</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Inter:wght@300;400;500;600&family=Fira+Code:wght@400;500&family=Noto+Sans+SC:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>
/* ========== 智能分页控制 ========== */
@media print {
  h1, h2, h3 { page-break-after: avoid; break-after: avoid; }
  blockquote, .code-block, .terminal, .highlight-box, figure { page-break-inside: avoid; break-inside: avoid; }
  .glow-line { page-break-after: avoid; break-after: avoid; }
  p { orphans: 3; widows: 3; }
}
blockquote, .code-block, .terminal, .highlight-box { page-break-inside: avoid; break-inside: avoid; }
h1, h2, h3 { page-break-after: avoid; break-after: avoid; }

/* ========== 主题样式 ========== */
body { font-family: 'Inter', 'Noto Sans SC', sans-serif; background: #1e293b; }
h1, h2, h3 { font-family: 'JetBrains Mono', 'Noto Sans SC', monospace; }
code { font-family: 'Fira Code', monospace; }
.magazine-page {
  width: 100%;
  max-width: 800px;
  background: #0f172a;
  padding: 60px 70px;
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);
  margin: 0 auto;
}
.glow-line {
  height: 2px;
  background: linear-gradient(90deg, #22d3ee, #a78bfa);
  box-shadow: 0 0 20px rgba(34, 211, 238, 0.5);
  margin-bottom: 2rem;
}
.tag {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  background: rgba(34, 211, 238, 0.1);
  border: 1px solid #22d3ee;
  color: #22d3ee;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  border-radius: 0.25rem;
  margin-bottom: 1rem;
}
h1 { font-size: 2.25rem; font-weight: 700; color: #f8fafc; margin-bottom: 0.75rem; line-height: 1.2; }
.subtitle { color: #94a3b8; font-size: 1.125rem; margin-bottom: 2rem; }
.content { line-height: 1.8; color: #cbd5e1; }
.content p { margin-bottom: 1.25rem; }
h2 { font-size: 1.25rem; color: #a78bfa; margin: 2rem 0 1rem; }
.code-block {
  background: #1e293b;
  padding: 1.5rem;
  border-radius: 0.5rem;
  margin: 1.5rem 0;
  border-left: 3px solid #22d3ee;
  font-family: 'Fira Code', monospace;
  font-size: 0.875rem;
  color: #e2e8f0;
  overflow-x: auto;
}
blockquote { border-left: 3px solid #a78bfa; padding-left: 1.5rem; margin: 1.5rem 0; color: #94a3b8; font-style: italic; }
.highlight { color: #22d3ee; }
.highlight-purple { color: #a78bfa; }
.terminal {
  background: #000;
  padding: 1rem 1.5rem;
  border-radius: 0.5rem;
  font-family: 'Fira Code', monospace;
  font-size: 0.875rem;
  color: #22d3ee;
  margin: 1.5rem 0;
}
.terminal::before { content: '$ '; color: #a78bfa; }
</style>
</head>
<body class="min-h-screen py-8 px-4">
<article class="magazine-page">
<div class="glow-line"></div>
{{CONTENT}}
</article>
</body>
</html>
```

---

## Style Selection Guide

| Style | Best For | Tone |
|-------|----------|------|
| Classic Elegance | Literature, essays, memoirs | Refined, thoughtful |
| Modern Minimalist | Tech blogs, modern essays | Clean, focused |
| Tech Magazine | Programming, technology | Technical, innovative |
| Nature & Lifestyle | Wellness, travel, food | Warm, organic |
| Bold Editorial | Opinion, commentary | Impactful, strong |
| Vintage Retro | History, nostalgia | Classic, timeless |
| Corporate Professional | Business, reports | Formal, trustworthy |
| Creative Art | Design, art, creativity | Expressive, dynamic |
| Academic Journal | Research, papers | Scholarly, precise |
| Fashion Luxe | Fashion, luxury brands | Elegant, sophisticated |
| News & Report | News, journalism | Informative, urgent |
| Dark Mode Tech | Developer content | Modern, technical |
