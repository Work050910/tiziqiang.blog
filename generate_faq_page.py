import json

with open('src/_data/faqs.json', 'r', encoding='utf-8') as f:
    faqs = json.load(f)

content = """---
layout: base.njk
title: "梯子推荐常见问题 ｜ 2026年100个好用的梯子与梯子工具使用知识库全景解答"
description: "AI精选并人工核验的100个梯子常见问题FAQ。全面覆盖好用的梯子、翻墙梯子、梯子工具推荐标准、套餐价格、流量倍率、退款与设备并发规则。"
permalink: "/faq/"
---

<div class="max-w-4xl mx-auto px-4 sm:px-6 py-10">
  <header class="mb-10 text-center">
    <div class="inline-flex items-center gap-2 px-3 py-1 bg-cyan-50 border border-cyan-200 rounded-full text-xs font-bold text-cyan-800 mb-3 shadow-xs">
      知识库与疑问检索 ｜ 覆盖 100 题
    </div>
    <h1 class="text-3xl sm:text-4xl font-black text-slate-900 tracking-tight mb-4 leading-tight">
      常见问题解答 (FAQ 100 题全景库)
    </h1>
    <p class="text-slate-600 max-w-2xl mx-auto text-sm sm:text-base leading-relaxed">
      围绕<strong>好用的梯子、翻墙梯子、梯子工具与梯子推荐</strong>，全面覆盖推荐标准、预算套餐、流量倍率、订阅说明与合规常识。每题均采用“直接结论—需核对的条件—下一步行动”结构。
    </p>
    <div class="mt-6">
      <a href="/airport-recommend/" class="px-5 py-2.5 bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-700 hover:to-blue-700 text-white font-bold rounded-xl text-xs sm:text-sm shadow-xs transition">
        查看已收录的 28 款梯子服务详细资料长文 →
      </a>
    </div>
  </header>

  <!-- Filter & FAQ List -->
  <div class="space-y-4">
"""

for item in faqs:
    content += f"""    <details class="group p-5 bg-white border border-slate-200 rounded-2xl hover:border-cyan-300 transition shadow-xs">
      <summary class="flex justify-between items-center cursor-pointer list-none">
        <h2 class="text-sm sm:text-base font-bold text-slate-900 group-open:text-cyan-600 transition pr-4">
          {item['question']}
        </h2>
        <span class="text-cyan-600 font-bold transition transform group-open:rotate-180 text-xs">▼</span>
      </summary>
      <div class="pt-4 mt-4 border-t border-slate-100 text-xs sm:text-sm text-slate-600 leading-relaxed space-y-3">
        <p>{item['answer']}</p>
        <div class="pt-2 flex items-center justify-between text-[11px] text-slate-400">
          <span>关键词归属：{item['keyword']}</span>
          <a href="/airport-recommend/" class="text-cyan-600 hover:underline font-semibold">内链回梯子推荐中心 →</a>
        </div>
      </div>
    </details>
"""

content += """  </div>

  <div class="mt-12 p-8 bg-white border border-slate-200 rounded-3xl text-center shadow-xs">
    <h3 class="text-lg font-black text-slate-900 mb-2">仍有未解决的疑问？</h3>
    <p class="text-xs sm:text-sm text-slate-500 mb-4 max-w-xl mx-auto">
      建议前往机场推荐中心长文，直接按套餐价格、线路类型与优惠码查看各家服务商的控制台公开说明。
    </p>
    <a href="/airport-recommend/" class="inline-block px-6 py-2.5 bg-cyan-600 hover:bg-cyan-700 text-white text-xs sm:text-sm font-bold rounded-xl transition shadow-xs">
      浏览梯子推荐中心长文
    </a>
  </div>
</div>
"""

with open("src/faq/index.njk", "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully regenerated src/faq/index.njk in light theme!")
