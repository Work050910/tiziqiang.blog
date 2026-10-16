import os
import json

with open('src/_data/airports.json', 'r', encoding='utf-8') as f:
    airports = json.load(f)

# Helper to build article content strictly adhering to:
# 1. 80-150 words direct answer opening (首段直答)
# 2. Distinct Target Audience & Phase (目标读者与阶段)
# 3. Dedicated H2/H3 addressing ONLY the main question
# 4. Contextual checklist
# 5. Non-template specific FAQs
# 6. Distinct airport context cards (flex-col vertical stack 并列单列)
# 7. Internal link back to /airport-recommend/

def build_post(section, slug, title, core_q, audience, phase, conclusion, dims, sections, faqs, recom_indices):
    a1 = airports[recom_indices[0]]
    a2 = airports[recom_indices[1]]
    a3 = airports[recom_indices[2]]

    sec_html = ""
    for sec_idx, (h2_title, paragraphs) in enumerate(sections):
        p_html = "".join([f"<p>{p}</p>" for p in paragraphs])
        sec_html += f"""
    <section id="section-{sec_idx+1}" class="mb-10">
      <h2 class="text-xl sm:text-2xl font-black text-slate-900 mb-4 border-l-4 border-cyan-600 pl-3">
        {h2_title}
      </h2>
      <div class="text-slate-700 leading-relaxed space-y-4 text-sm sm:text-base bg-white p-6 rounded-2xl border border-slate-200 shadow-xs">
        {p_html}
      </div>
    </section>"""

    faq_html = ""
    for q_item, a_item in faqs:
        faq_html += f"""
        <div class="p-5 bg-white border border-slate-200 rounded-2xl shadow-xs">
          <h3 class="text-sm sm:text-base font-bold text-slate-900 mb-2">{q_item}</h3>
          <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">{a_item}</p>
        </div>"""

    content = f"""---
layout: base.njk
title: "{title} ｜ 梯子墙深度评测与选型指南"
description: "{conclusion[:120]} 本文围绕核心问题展开深入资料核验，提供客观判断依据。"
permalink: "/{section}/{slug}/"
---

<article class="max-w-4xl mx-auto px-4 sm:px-6 py-10">
  <!-- Breadcrumb -->
  <nav class="text-xs text-slate-500 mb-6 flex items-center space-x-2">
    <a href="/" class="hover:text-cyan-600">首页</a>
    <span>/</span>
    <a href="/{section}/" class="hover:text-cyan-600">专栏文章</a>
    <span>/</span>
    <span class="text-slate-700">正文详情</span>
  </nav>

  <header class="mb-8 border-b border-slate-200 pb-6">
    <div class="flex items-center space-x-3 mb-3">
      <span class="px-3 py-1 bg-cyan-50 text-cyan-700 border border-cyan-200 rounded-full text-xs font-bold">深度专题研究</span>
      <span class="text-xs text-slate-400">最后核验日期：2026年10月</span>
    </div>
    <h1 class="text-2xl sm:text-3xl md:text-4xl font-black text-slate-900 tracking-tight mb-4 leading-tight">
      {title}
    </h1>
    
    <!-- 80-150 words Direct Answer Lead Paragraph -->
    <div class="p-6 bg-slate-50 border border-slate-200 rounded-2xl text-slate-800 text-sm sm:text-base leading-relaxed mb-4">
      <div class="font-bold text-cyan-800 text-xs uppercase tracking-wider mb-1">【针对标题问题的直接结论】</div>
      <p>
        {conclusion}
      </p>
    </div>

    <!-- Audience & Decision Phase Card -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
      <div class="p-3.5 bg-white border border-slate-200 rounded-xl shadow-xs">
        <span class="text-slate-500 block mb-0.5">🎯 本文适合读者：</span>
        <span class="font-bold text-slate-900">{audience}</span>
      </div>
      <div class="p-3.5 bg-white border border-slate-200 rounded-xl shadow-xs">
        <span class="text-slate-500 block mb-0.5">⏱️ 决策所处阶段：</span>
        <span class="font-bold text-cyan-700">{phase}</span>
      </div>
    </div>
  </header>

  <!-- Notice linking to Airport Recommend -->
  <div class="my-8 p-6 bg-gradient-to-r from-cyan-50/70 via-sky-50/50 to-blue-50/60 border border-cyan-200 rounded-2xl flex flex-col sm:flex-row items-center justify-between gap-4 shadow-xs">
    <div>
      <div class="text-sm font-black text-slate-900 mb-1">需要核对全网 28 家梯子服务的最新套餐与节点参数？</div>
      <div class="text-xs text-slate-600">本站已在机场推荐中心长文汇总全部已收录服务的详细横向评测、节点架构与专属优惠码。</div>
    </div>
    <a href="/airport-recommend/" class="px-5 py-2.5 bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-700 hover:to-blue-700 text-white text-xs font-bold rounded-xl shrink-0 shadow-xs transition">
      查看 28 家机场推荐长文 →
    </a>
  </div>

  <!-- Key Dimensions List -->
  <div class="my-6 p-5 bg-white border border-slate-200 rounded-2xl shadow-xs">
    <div class="text-xs font-bold text-slate-900 uppercase tracking-wider mb-2">本文核心评判维度</div>
    <div class="flex flex-wrap gap-2 text-xs">
      {''.join([f'<span class="px-2.5 py-1 bg-slate-100 text-slate-700 rounded-lg border border-slate-200 font-medium">{d}</span>' for d in dims])}
    </div>
  </div>

  <!-- Main Body Sections -->
  {sec_html}

  <!-- Section 4: Relevant Airports Context (并列单列纵向排列) -->
  <section class="mb-10">
    <h2 class="text-xl sm:text-2xl font-black text-slate-900 mb-4 border-l-4 border-cyan-600 pl-3">
      符合本篇评判逻辑的代表性梯子服务参考
    </h2>
    <p class="text-slate-600 text-xs sm:text-sm mb-4">
      依据上述讨论的核心标准，以下 3 款服务在套餐定价、专线优化或特定场景支持上，展现出高契合度的交付质量：
    </p>
    <div class="flex flex-col space-y-4">
      <!-- Airport 1 -->
      <div class="p-5 bg-white rounded-2xl border border-slate-200 hover:border-cyan-300 transition shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div class="flex items-start sm:items-center gap-4">
          <span class="text-xs font-bold text-white bg-cyan-600 px-3 py-1.5 rounded-xl font-mono shrink-0">#{a1['id']}</span>
          <div>
            <div class="flex items-center gap-3">
              <h3 class="font-bold text-slate-900 text-base">{a1['name']}</h3>
              <span class="text-xs text-slate-500 font-semibold">{a1['minPrice']}</span>
            </div>
            <p class="text-xs text-slate-600 mt-1 leading-relaxed">{a1['highlights']}</p>
          </div>
        </div>
        <div class="flex items-center gap-3 shrink-0 self-end sm:self-center">
          <code class="text-xs font-mono font-bold bg-cyan-50 text-cyan-700 px-2.5 py-1 rounded-lg border border-cyan-200">{a1['coupon']}</code>
          <a href="/airport/{a1['slug']}/" class="text-xs px-3.5 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold rounded-lg border border-slate-200 transition">查看测评</a>
          <a href="{a1['affLink']}" target="_blank" rel="sponsored nofollow noopener noreferrer" class="text-xs px-4 py-1.5 bg-cyan-600 hover:bg-cyan-700 text-white font-bold rounded-lg transition">官网直达</a>
        </div>
      </div>

      <!-- Airport 2 -->
      <div class="p-5 bg-white rounded-2xl border border-slate-200 hover:border-cyan-300 transition shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div class="flex items-start sm:items-center gap-4">
          <span class="text-xs font-bold text-white bg-cyan-600 px-3 py-1.5 rounded-xl font-mono shrink-0">#{a2['id']}</span>
          <div>
            <div class="flex items-center gap-3">
              <h3 class="font-bold text-slate-900 text-base">{a2['name']}</h3>
              <span class="text-xs text-slate-500 font-semibold">{a2['minPrice']}</span>
            </div>
            <p class="text-xs text-slate-600 mt-1 leading-relaxed">{a2['highlights']}</p>
          </div>
        </div>
        <div class="flex items-center gap-3 shrink-0 self-end sm:self-center">
          <code class="text-xs font-mono font-bold bg-cyan-50 text-cyan-700 px-2.5 py-1 rounded-lg border border-cyan-200">{a2['coupon']}</code>
          <a href="/airport/{a2['slug']}/" class="text-xs px-3.5 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold rounded-lg border border-slate-200 transition">查看测评</a>
          <a href="{a2['affLink']}" target="_blank" rel="sponsored nofollow noopener noreferrer" class="text-xs px-4 py-1.5 bg-cyan-600 hover:bg-cyan-700 text-white font-bold rounded-lg transition">官网直达</a>
        </div>
      </div>

      <!-- Airport 3 -->
      <div class="p-5 bg-white rounded-2xl border border-slate-200 hover:border-cyan-300 transition shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div class="flex items-start sm:items-center gap-4">
          <span class="text-xs font-bold text-white bg-cyan-600 px-3 py-1.5 rounded-xl font-mono shrink-0">#{a3['id']}</span>
          <div>
            <div class="flex items-center gap-3">
              <h3 class="font-bold text-slate-900 text-base">{a3['name']}</h3>
              <span class="text-xs text-slate-500 font-semibold">{a3['minPrice']}</span>
            </div>
            <p class="text-xs text-slate-600 mt-1 leading-relaxed">{a3['highlights']}</p>
          </div>
        </div>
        <div class="flex items-center gap-3 shrink-0 self-end sm:self-center">
          <code class="text-xs font-mono font-bold bg-cyan-50 text-cyan-700 px-2.5 py-1 rounded-lg border border-cyan-200">{a3['coupon']}</code>
          <a href="/airport/{a3['slug']}/" class="text-xs px-3.5 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold rounded-lg border border-slate-200 transition">查看测评</a>
          <a href="{a3['affLink']}" target="_blank" rel="sponsored nofollow noopener noreferrer" class="text-xs px-4 py-1.5 bg-cyan-600 hover:bg-cyan-700 text-white font-bold rounded-lg transition">官网直达</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Specific FAQs for this topic -->
  <section class="mb-10">
    <h2 class="text-xl sm:text-2xl font-black text-slate-900 mb-4 border-l-4 border-cyan-600 pl-3">
      关于本篇主题的常见问题解答 (FAQ)
    </h2>
    <div class="space-y-4">
      {faq_html}
    </div>
  </section>

  <!-- Internal Link to Hub -->
  <section class="mb-10 p-6 bg-white rounded-2xl border border-slate-200 shadow-xs flex flex-col sm:flex-row items-center justify-between gap-4">
    <div>
      <div class="font-black text-slate-900 text-sm sm:text-base">返回机场推荐中心查看全景长文排行</div>
      <div class="text-xs text-slate-500 mt-1">包含全球云、飞猫云、暮光加速、大佬云等全部 28 家服务商的套餐详情与最新参数。</div>
    </div>
    <a href="/airport-recommend/" class="px-5 py-2.5 bg-cyan-600 hover:bg-cyan-700 text-white font-bold rounded-xl text-xs sm:text-sm shrink-0 transition shadow-xs">
      直达机场推荐中心 →
    </a>
  </section>

  <footer class="pt-6 border-t border-slate-200 text-xs text-slate-400 flex flex-col sm:flex-row justify-between gap-2">
    <div>发布于：梯子墙 (tiziqiang.blog) ｜ 资料核查归档</div>
    <div>免责声明：本站仅作公开资料整理与技术探讨，不提供直接代理服务</div>
  </footer>
</article>
"""
    file_path = f"src/{section}/{slug}.njk"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Helper function build_post defined successfully!")
