# 私董会报告排版模板

本文件定义私董会结束后生成的精美杂志风格报告模板。

---

## 报告生成时机

在私董会完成所有8个步骤后，询问案主是否需要生成精美的会议报告：

> 私董会已圆满结束。是否需要我为您生成一份精美的杂志风格会议报告？
>
> 报告将包含：问题摘要、关键洞察、幕僚建议汇总、您的行动计划等。

---

## HTML 报告模板

### 基础样式

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>私董会报告 - [案主问题关键词]</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700&family=Noto+Sans+SC:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>
body { font-family: 'Noto Sans SC', sans-serif; font-weight: 300; }
h1, h2, h3, blockquote { font-family: 'Noto Serif SC', serif; }
.magazine-page {
    width: 800px;
    min-height: 1100px;
    background: linear-gradient(135deg, #fefefe 0%, #f8f9fa 100%);
    overflow: hidden;
}
.drop-cap::first-letter {
    float: left;
    font-size: 4em;
    line-height: 0.8;
    margin: 0.1em 0.15em 0 0;
    font-weight: 700;
    font-family: 'Noto Serif SC', serif;
    color: #1f2937;
}
.breathing-space { letter-spacing: 0.03em; line-height: 1.9; }
.advisor-card {
    background: linear-gradient(145deg, #ffffff 0%, #f3f4f6 100%);
    border-left: 4px solid;
}
.advisor-buffett { border-color: #059669; }
.advisor-gates { border-color: #2563eb; }
.advisor-musk { border-color: #dc2626; }
.advisor-jobs { border-color: #7c3aed; }
.section-divider {
    background: linear-gradient(90deg, transparent 0%, #d1d5db 50%, transparent 100%);
    height: 1px;
}
</style>
</head>
<body class="bg-gray-100 py-12">
```

### 封面页

```html
<!-- 封面页 -->
<article class="magazine-page shadow-2xl mx-auto mb-12 relative overflow-hidden">
    <!-- 装饰性背景 -->
    <div class="absolute top-0 right-0 w-64 h-64 bg-gradient-to-br from-blue-50 to-purple-50 rounded-full -translate-y-32 translate-x-32 opacity-60"></div>
    <div class="absolute bottom-0 left-0 w-48 h-48 bg-gradient-to-tr from-green-50 to-blue-50 rounded-full translate-y-24 -translate-x-24 opacity-60"></div>

    <div class="relative z-10 p-16 h-full flex flex-col">
        <!-- 头部标识 -->
        <header class="flex justify-between items-start mb-16">
            <div>
                <span class="text-xs tracking-widest text-gray-400 uppercase">Peers Advisory Group</span>
                <div class="text-sm text-gray-500 mt-1">[日期]</div>
            </div>
            <div class="text-right">
                <span class="text-xs tracking-widest text-gray-400">私董会纪要</span>
                <div class="text-sm text-gray-500 mt-1">第 [N] 期</div>
            </div>
        </header>

        <!-- 主标题区 -->
        <div class="flex-1 flex flex-col justify-center">
            <h1 class="text-5xl font-bold leading-tight mb-8 text-gray-800">
                [案主问题的精炼标题]
            </h1>
            <p class="text-xl text-gray-600 font-light leading-relaxed max-w-lg">
                [问题的一句话概述]
            </p>
        </div>

        <!-- 幕僚阵容 -->
        <footer class="mt-auto pt-12 border-t border-gray-200">
            <p class="text-xs text-gray-400 mb-4 tracking-wide">本期幕僚</p>
            <div class="flex gap-6">
                <div class="flex items-center gap-2">
                    <div class="w-2 h-2 rounded-full bg-green-600"></div>
                    <span class="text-sm text-gray-600">巴菲特</span>
                </div>
                <div class="flex items-center gap-2">
                    <div class="w-2 h-2 rounded-full bg-blue-600"></div>
                    <span class="text-sm text-gray-600">比尔·盖茨</span>
                </div>
                <div class="flex items-center gap-2">
                    <div class="w-2 h-2 rounded-full bg-red-600"></div>
                    <span class="text-sm text-gray-600">马斯克</span>
                </div>
                <div class="flex items-center gap-2">
                    <div class="w-2 h-2 rounded-full bg-purple-600"></div>
                    <span class="text-sm text-gray-600">乔布斯</span>
                </div>
            </div>
        </footer>
    </div>
</article>
```

### 问题概述页

```html
<!-- 问题概述页 -->
<article class="magazine-page shadow-2xl mx-auto mb-12 p-16">
    <header class="mb-12">
        <span class="text-xs tracking-widest text-gray-400 uppercase">Chapter 01</span>
        <h2 class="text-3xl font-bold mt-2 text-gray-800">问题概述</h2>
    </header>

    <!-- 核心问题引言 -->
    <blockquote class="border-l-4 border-gray-800 pl-8 my-12">
        <p class="text-2xl font-light italic leading-relaxed text-gray-700">
            "[案主原话中最关键的一句]"
        </p>
    </blockquote>

    <!-- 背景描述 -->
    <div class="prose prose-lg max-w-none breathing-space text-gray-600">
        <p class="drop-cap mb-6">
            [案主问题背景的第一段，使用首字下沉效果]
        </p>
        <p class="mb-6">
            [问题的详细描述]
        </p>
    </div>

    <!-- 期望目标 -->
    <div class="mt-12 p-6 bg-gray-50 rounded-lg">
        <h3 class="text-lg font-semibold text-gray-700 mb-4">期望目标</h3>
        <ul class="space-y-2 text-gray-600">
            <li class="flex items-start gap-3">
                <span class="text-green-600 mt-1">◆</span>
                <span>[目标1]</span>
            </li>
            <li class="flex items-start gap-3">
                <span class="text-green-600 mt-1">◆</span>
                <span>[目标2]</span>
            </li>
        </ul>
    </div>
</article>
```

### 关键洞察页

```html
<!-- 关键洞察页 -->
<article class="magazine-page shadow-2xl mx-auto mb-12 p-16">
    <header class="mb-12">
        <span class="text-xs tracking-widest text-gray-400 uppercase">Chapter 02</span>
        <h2 class="text-3xl font-bold mt-2 text-gray-800">关键洞察</h2>
        <p class="text-gray-500 mt-2">来自三轮深度提问的发现</p>
    </header>

    <!-- 洞察卡片 -->
    <div class="space-y-8">
        <div class="p-6 bg-white rounded-lg shadow-sm border border-gray-100">
            <div class="flex items-center gap-3 mb-4">
                <span class="text-2xl">💡</span>
                <h3 class="text-lg font-semibold text-gray-800">洞察一</h3>
            </div>
            <p class="text-gray-600 breathing-space">[关键洞察内容]</p>
        </div>

        <div class="p-6 bg-white rounded-lg shadow-sm border border-gray-100">
            <div class="flex items-center gap-3 mb-4">
                <span class="text-2xl">🔍</span>
                <h3 class="text-lg font-semibold text-gray-800">洞察二</h3>
            </div>
            <p class="text-gray-600 breathing-space">[关键洞察内容]</p>
        </div>

        <div class="p-6 bg-white rounded-lg shadow-sm border border-gray-100">
            <div class="flex items-center gap-3 mb-4">
                <span class="text-2xl">⚡</span>
                <h3 class="text-lg font-semibold text-gray-800">洞察三</h3>
            </div>
            <p class="text-gray-600 breathing-space">[关键洞察内容]</p>
        </div>
    </div>
</article>
```

### 幕僚建议页（每位幕僚一页）

```html
<!-- 幕僚建议页 - 巴菲特 -->
<article class="magazine-page shadow-2xl mx-auto mb-12 p-16">
    <header class="mb-8 pb-6 border-b-2 border-green-600">
        <div class="flex items-center gap-4">
            <div class="w-12 h-12 rounded-full bg-green-100 flex items-center justify-center">
                <span class="text-2xl">🎩</span>
            </div>
            <div>
                <h2 class="text-2xl font-bold text-gray-800">沃伦·巴菲特</h2>
                <p class="text-sm text-gray-500">奥马哈的先知 · 价值投资之父</p>
            </div>
        </div>
    </header>

    <!-- 名言金句 -->
    <blockquote class="border-l-4 border-green-600 pl-6 my-8 bg-green-50 py-4 rounded-r-lg">
        <p class="text-xl font-medium italic text-gray-700">
            「[巴菲特的名言金句]」
        </p>
    </blockquote>

    <!-- 问题定性 -->
    <div class="my-8">
        <h3 class="text-lg font-semibold text-gray-700 mb-3 flex items-center gap-2">
            <span class="text-green-600">◎</span> 问题定性
        </h3>
        <p class="text-gray-600 breathing-space pl-6">
            [巴菲特对案主真正问题的判断]
        </p>
    </div>

    <!-- 经历分享 -->
    <div class="my-8 p-6 bg-gray-50 rounded-lg">
        <h3 class="text-lg font-semibold text-gray-700 mb-3">📖 经历分享</h3>
        <p class="text-gray-600 breathing-space">
            [巴菲特分享的相关经历或故事]
        </p>
    </div>

    <!-- 具体建议 -->
    <div class="my-8">
        <h3 class="text-lg font-semibold text-gray-700 mb-4 flex items-center gap-2">
            <span class="text-green-600">◎</span> 具体建议
        </h3>
        <div class="space-y-3 pl-6">
            <div class="flex items-start gap-3">
                <span class="bg-green-600 text-white text-xs px-2 py-1 rounded font-medium">1</span>
                <p class="text-gray-600">[具体建议1]</p>
            </div>
            <div class="flex items-start gap-3">
                <span class="bg-green-600 text-white text-xs px-2 py-1 rounded font-medium">2</span>
                <p class="text-gray-600">[具体建议2]</p>
            </div>
            <div class="flex items-start gap-3">
                <span class="bg-green-600 text-white text-xs px-2 py-1 rounded font-medium">3</span>
                <p class="text-gray-600">[具体建议3]</p>
            </div>
        </div>
    </div>
</article>
```

### 行动计划页

```html
<!-- 行动计划页 -->
<article class="magazine-page shadow-2xl mx-auto mb-12 p-16">
    <header class="mb-12">
        <span class="text-xs tracking-widest text-gray-400 uppercase">Action Plan</span>
        <h2 class="text-3xl font-bold mt-2 text-gray-800">行动计划</h2>
        <p class="text-gray-500 mt-2">您的承诺与下一步</p>
    </header>

    <!-- 核心收获 -->
    <div class="mb-10">
        <h3 class="text-lg font-semibold text-gray-700 mb-4">✨ 核心收获</h3>
        <div class="p-6 bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg">
            <p class="text-gray-700 breathing-space">[案主总结的最大收获]</p>
        </div>
    </div>

    <!-- 行动事项 -->
    <div class="mb-10">
        <h3 class="text-lg font-semibold text-gray-700 mb-4">📋 行动事项</h3>
        <div class="space-y-4">
            <div class="flex items-center gap-4 p-4 bg-white rounded-lg border border-gray-200">
                <div class="w-6 h-6 rounded border-2 border-gray-300"></div>
                <div class="flex-1">
                    <p class="text-gray-700 font-medium">[行动事项1]</p>
                    <p class="text-sm text-gray-500">截止日期：[日期]</p>
                </div>
            </div>
            <div class="flex items-center gap-4 p-4 bg-white rounded-lg border border-gray-200">
                <div class="w-6 h-6 rounded border-2 border-gray-300"></div>
                <div class="flex-1">
                    <p class="text-gray-700 font-medium">[行动事项2]</p>
                    <p class="text-sm text-gray-500">截止日期：[日期]</p>
                </div>
            </div>
            <div class="flex items-center gap-4 p-4 bg-white rounded-lg border border-gray-200">
                <div class="w-6 h-6 rounded border-2 border-gray-300"></div>
                <div class="flex-1">
                    <p class="text-gray-700 font-medium">[行动事项3]</p>
                    <p class="text-sm text-gray-500">截止日期：[日期]</p>
                </div>
            </div>
        </div>
    </div>

    <!-- 承诺签名 -->
    <div class="mt-auto pt-12 border-t border-gray-200">
        <div class="flex justify-between items-end">
            <div>
                <p class="text-sm text-gray-500 mb-2">案主签名</p>
                <div class="text-2xl font-serif text-gray-700">[案主称呼]</div>
            </div>
            <div class="text-right">
                <p class="text-sm text-gray-500 mb-2">日期</p>
                <div class="text-gray-700">[日期]</div>
            </div>
        </div>
    </div>
</article>
```

### 结尾页

```html
<!-- 结尾页 -->
<article class="magazine-page shadow-2xl mx-auto p-16 flex flex-col">
    <div class="flex-1 flex flex-col justify-center items-center text-center">
        <div class="mb-8">
            <span class="text-6xl">🎯</span>
        </div>
        <h2 class="text-3xl font-bold text-gray-800 mb-4">感谢参与私董会</h2>
        <p class="text-xl text-gray-600 font-light max-w-md">
            愿今天的洞察与建议，成为您前行路上的明灯
        </p>

        <div class="mt-16 p-8 bg-gray-50 rounded-lg max-w-lg">
            <p class="text-gray-600 italic breathing-space">
                "最好的投资是投资自己。最好的决策是深思熟虑后的决策。"
            </p>
            <p class="text-sm text-gray-400 mt-4">— 私董会寄语</p>
        </div>
    </div>

    <footer class="text-center text-sm text-gray-400 pt-8 border-t border-gray-200">
        <p>Peers Advisory Group</p>
        <p class="mt-1">[日期] · 第 [N] 期</p>
    </footer>
</article>

</body>
</html>
```

---

## 报告生成规则

1. **内容完整性**：报告必须包含私董会全过程的关键信息
2. **忠于原文**：不得修改案主的原话和观点
3. **视觉一致性**：每页保持统一的设计风格
4. **空间控制**：每页内容不得溢出，必要时分页
5. **幕僚色彩编码**：
   - 巴菲特：绿色 (#059669)
   - 比尔·盖茨：蓝色 (#2563eb)
   - 马斯克：红色 (#dc2626)
   - 乔布斯：紫色 (#7c3aed)

---

## 幕僚图标参考

| 幕僚 | 图标 | 备选 |
|------|------|------|
| 巴菲特 | 🎩 | 💰 📊 |
| 比尔·盖茨 | 💻 | 🔬 📈 |
| 马斯克 | 🚀 | ⚡ 🔥 |
| 乔布斯 | 🍎 | ✨ 💡 |
