# 5Why 因果链可视化报告模板

本文件定义 5Why 分析结束后生成的因果链可视化 HTML 报告模板。

---

## 报告生成时机

在第四阶段（根本对策）完成后，询问用户：

> 是否需要我为您生成一份 5Why 因果链可视化报告？
>
> 报告将包含：问题陈述、完整因果链流程图、根本原因标注、对策行动计划。

---

## 数据准备

生成报告前，整理以下数据：

| 字段 | 说明 |
|------|------|
| `problem` | 第一阶段确认的问题陈述 |
| `whys` | 每一层 Why 的问题和用户回答（数组） |
| `root_cause` | 第三阶段验证通过的根本原因 |
| `countermeasures` | 第四阶段的对策行动计划（数组） |
| `date` | 分析日期 |

---

## HTML 报告模板

### 基础样式

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>5Why 溯源分析报告 - [问题关键词]</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700&family=Noto+Sans+SC:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>
body { font-family: 'Noto Sans SC', sans-serif; font-weight: 300; }
h1, h2, h3, blockquote { font-family: 'Noto Serif SC', serif; }
.report-page {
    width: 800px;
    min-height: 1100px;
    background: linear-gradient(135deg, #fefefe 0%, #f8f9fa 100%);
    overflow: hidden;
}
.breathing-space { letter-spacing: 0.03em; line-height: 1.9; }

/* 因果链流程图样式 */
.chain-node {
    position: relative;
    padding: 1.25rem 1.5rem;
    border-radius: 0.75rem;
    transition: transform 0.2s;
}
.chain-node:hover { transform: translateX(4px); }
.chain-connector {
    width: 3px;
    height: 2.5rem;
    margin-left: 2rem;
    background: linear-gradient(180deg, currentColor 0%, currentColor 60%, transparent 100%);
}
.chain-why-label {
    position: absolute;
    left: -3.5rem;
    top: 50%;
    transform: translateY(-50%);
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

/* 节点层级色彩 - 从浅到深，越接近根因颜色越深 */
.node-problem {
    background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
    border-left: 4px solid #f59e0b;
    color: #92400e;
}
.node-why {
    background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
    border-left: 4px solid #3b82f6;
    color: #1e3a5f;
}
.node-deep {
    background: linear-gradient(135deg, #e0e7ff 0%, #c7d2fe 100%);
    border-left: 4px solid #6366f1;
    color: #312e81;
}
.node-root {
    background: linear-gradient(135deg, #fce7f3 0%, #fbcfe8 100%);
    border-left: 4px solid #ec4899;
    color: #831843;
    box-shadow: 0 4px 15px rgba(236, 72, 153, 0.15);
}

/* 对策卡片 */
.countermeasure-card {
    background: linear-gradient(145deg, #ecfdf5 0%, #d1fae5 100%);
    border-left: 4px solid #10b981;
    border-radius: 0.75rem;
    padding: 1rem 1.5rem;
}

/* 分隔线 */
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
<article class="report-page shadow-2xl mx-auto mb-12 relative overflow-hidden">
    <!-- 装饰性背景 -->
    <div class="absolute top-0 right-0 w-64 h-64 bg-gradient-to-br from-amber-50 to-pink-50 rounded-full -translate-y-32 translate-x-32 opacity-60"></div>
    <div class="absolute bottom-0 left-0 w-48 h-48 bg-gradient-to-tr from-blue-50 to-indigo-50 rounded-full translate-y-24 -translate-x-24 opacity-60"></div>

    <div class="relative z-10 p-16 h-full flex flex-col">
        <!-- 头部标识 -->
        <header class="flex justify-between items-start mb-16">
            <div>
                <span class="text-xs tracking-widest text-gray-400 uppercase">5Why Root Cause Analysis</span>
                <div class="text-sm text-gray-500 mt-1">[日期]</div>
            </div>
            <div class="text-right">
                <span class="text-xs text-gray-400">溯源分析报告</span>
            </div>
        </header>

        <!-- 主标题 -->
        <div class="flex-1 flex flex-col justify-center">
            <h1 class="text-4xl font-bold text-gray-900 leading-tight mb-6">
                [问题关键词]
            </h1>
            <div class="section-divider my-8"></div>
            <p class="text-lg text-gray-600 breathing-space max-w-lg">
                [完整问题陈述]
            </p>
        </div>

        <!-- 底部摘要 -->
        <footer class="flex justify-between items-end text-sm text-gray-500">
            <div>
                <div class="font-medium text-gray-700">追问层数</div>
                <div class="text-2xl font-bold text-indigo-600">[N] 层</div>
            </div>
            <div class="text-right">
                <div class="font-medium text-gray-700">根本原因</div>
                <div class="text-pink-600 font-medium">[根因关键词]</div>
            </div>
        </footer>
    </div>
</article>
```

### 因果链流程图页

```html
<!-- 因果链页 -->
<article class="report-page shadow-2xl mx-auto mb-12 relative overflow-hidden">
    <div class="p-16">
        <h2 class="text-2xl font-bold text-gray-900 mb-2">因果链溯源</h2>
        <p class="text-sm text-gray-500 mb-10">从问题表象到根本原因的完整追问路径</p>

        <!-- 因果链流程图 -->
        <div class="space-y-0">
            <!-- 问题节点 -->
            <div class="chain-node node-problem">
                <div class="chain-why-label text-amber-600">问题</div>
                <div class="text-sm font-medium">[问题陈述]</div>
            </div>
            <div class="chain-connector text-amber-400"></div>

            <!-- Why 1 -->
            <div class="chain-node node-why">
                <div class="chain-why-label text-blue-600">Why 1</div>
                <div class="text-xs text-blue-400 mb-1">为什么 [问题]？</div>
                <div class="text-sm font-medium">[用户回答1]</div>
            </div>
            <div class="chain-connector text-blue-400"></div>

            <!-- Why 2 -->
            <div class="chain-node node-why">
                <div class="chain-why-label text-blue-600">Why 2</div>
                <div class="text-xs text-blue-400 mb-1">为什么 [回答1]？</div>
                <div class="text-sm font-medium">[用户回答2]</div>
            </div>
            <div class="chain-connector text-blue-400"></div>

            <!-- Why 3+ (根据实际层数重复，越深用 node-deep) -->
            <div class="chain-node node-deep">
                <div class="chain-why-label text-indigo-600">Why 3</div>
                <div class="text-xs text-indigo-400 mb-1">为什么 [回答2]？</div>
                <div class="text-sm font-medium">[用户回答3]</div>
            </div>
            <div class="chain-connector text-indigo-400"></div>

            <!-- 根本原因节点 -->
            <div class="chain-node node-root">
                <div class="chain-why-label text-pink-600">根因</div>
                <div class="text-xs text-pink-400 mb-1">为什么 [回答N-1]？</div>
                <div class="text-sm font-bold">[根本原因]</div>
            </div>
        </div>

        <!-- 逻辑验证 -->
        <div class="mt-12 p-6 bg-gray-50 rounded-xl border border-gray-200">
            <h3 class="text-sm font-bold text-gray-700 mb-3">逆向逻辑验证</h3>
            <p class="text-sm text-gray-600 breathing-space">
                因为"[根本原因]"，所以"[第N-1层]"，所以"[第N-2层]"，……所以最终导致了"[问题]"。
            </p>
            <div class="mt-3 text-xs text-green-600 font-medium">✓ 逻辑链验证通过</div>
        </div>
    </div>
</article>
```

### 对策行动计划页

```html
<!-- 对策页 -->
<article class="report-page shadow-2xl mx-auto mb-12 relative overflow-hidden">
    <div class="p-16">
        <h2 class="text-2xl font-bold text-gray-900 mb-2">根本对策</h2>
        <p class="text-sm text-gray-500 mb-4">
            针对根因：<span class="text-pink-600 font-medium">"[根本原因]"</span>
        </p>
        <div class="section-divider my-8"></div>

        <!-- 对策列表 -->
        <div class="space-y-6">
            <!-- 对策 1 -->
            <div class="countermeasure-card">
                <div class="flex justify-between items-start mb-2">
                    <h3 class="text-base font-bold text-gray-800">对策 1：[措施名称]</h3>
                    <span class="text-xs bg-green-100 text-green-700 px-2 py-1 rounded-full">[优先级]</span>
                </div>
                <p class="text-sm text-gray-600 mb-3">[具体措施描述]</p>
                <div class="flex gap-6 text-xs text-gray-500">
                    <div><span class="font-medium text-gray-700">责任人：</span>[谁]</div>
                    <div><span class="font-medium text-gray-700">时间：</span>[何时完成]</div>
                    <div><span class="font-medium text-gray-700">验证标准：</span>[怎么判断有效]</div>
                </div>
            </div>

            <!-- 对策 2（根据实际数量重复） -->
            <div class="countermeasure-card">
                <div class="flex justify-between items-start mb-2">
                    <h3 class="text-base font-bold text-gray-800">对策 2：[措施名称]</h3>
                    <span class="text-xs bg-green-100 text-green-700 px-2 py-1 rounded-full">[优先级]</span>
                </div>
                <p class="text-sm text-gray-600 mb-3">[具体措施描述]</p>
                <div class="flex gap-6 text-xs text-gray-500">
                    <div><span class="font-medium text-gray-700">责任人：</span>[谁]</div>
                    <div><span class="font-medium text-gray-700">时间：</span>[何时完成]</div>
                    <div><span class="font-medium text-gray-700">验证标准：</span>[怎么判断有效]</div>
                </div>
            </div>
        </div>

        <!-- 底部提示 -->
        <div class="mt-12 p-4 bg-indigo-50 rounded-lg border border-indigo-100">
            <p class="text-xs text-indigo-600">
                <span class="font-bold">下一步建议：</span>
                可使用「第一性原理」Skill 进一步审视对策的本质——是否有更高效的方式实现同样的目标？
            </p>
        </div>
    </div>
</article>

</body>
</html>
```

---

## 模板使用说明

1. **动态填充**：将方括号 `[...]` 中的占位符替换为实际分析数据
2. **层数自适应**：因果链节点数量根据实际追问层数增减
   - Why 1-2 使用 `node-why` 样式
   - Why 3+ 使用 `node-deep` 样式
   - 最后一层始终使用 `node-root` 样式
3. **对策数量灵活**：根据实际对策数量增减卡片
4. **保持呼吸感**：遵循"少即是多"的设计哲学，内容不溢出页面边界
