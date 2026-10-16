import os
import json

with open('src/_data/airports.json', 'r', encoding='utf-8') as f:
    airports = json.load(f)

airport_map = {a['slug']: a for a in airports}

def normalize_airports(context_airports):
    # Always ensure quanqiuyun is first, pad to 5 unique airports (within 4-6 range)
    chosen = ['quanqiuyun']
    if context_airports:
        for s in context_airports:
            if s and s != 'quanqiuyun' and s in airport_map and s not in chosen:
                chosen.append(s)
    fallbacks = ['flycat', 'muguang', 'dalaoyun', 'breezenet', 'jilianyun', 'guangnianti', 'edgenova']
    for f in fallbacks:
        if len(chosen) >= 5:
            break
        if f in airport_map and f not in chosen:
            chosen.append(f)
    return chosen[:5]

def render_article_page(section, slug, title, meta_desc, contract, sections_html, context_airports, specific_faqs, related_links=None):
    # Context airports: strictly 4-6 airports, always starting with #01 全球云
    context_airports = normalize_airports(context_airports)
    cards_html = ""
    if context_airports:
        card_items = ""
        for s in context_airports:
            if s in airport_map:
                a = airport_map[s]
                card_items += f"""
        <div class="p-5 bg-white rounded-2xl border border-slate-200 hover:border-cyan-300 transition shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div class="flex items-start sm:items-center gap-4">
            <span class="text-base font-bold text-white bg-cyan-600 px-3 py-1.5 rounded-xl font-mono shrink-0">#{a['id']}</span>
            <div>
              <div class="flex items-center gap-2.5">
                <h4 class="font-bold text-slate-900 text-base">{a['name']}</h4>
                <span class="text-sm font-semibold text-slate-600">{a['minPrice']}</span>
              </div>
              <p class="text-sm sm:text-base text-slate-700 mt-1 leading-relaxed">{a['highlights']}</p>
            </div>
          </div>
          <div class="flex items-center gap-2.5 shrink-0 self-end sm:self-center">
            <code class="text-base font-mono font-bold bg-cyan-50 text-cyan-700 px-2.5 py-1 rounded-lg border border-cyan-200">{a['coupon']}</code>
            <a href="/airport/{a['slug']}/" class="text-base px-3.5 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold rounded-lg border border-slate-200 transition">详情评测</a>
            <a href="{a['affLink']}" target="_blank" rel="sponsored nofollow noopener noreferrer" class="text-base px-4 py-1.5 bg-cyan-600 hover:bg-cyan-700 text-white font-bold rounded-lg transition">官网</a>
          </div>
        </div>"""
        cards_html = f"""
    <!-- Contextually Relevant Airports Only (4-6 airports, #01 全球云首位) -->
    <div class="my-8 p-6 bg-slate-50 border border-slate-200 rounded-3xl">
      <div class="flex items-center justify-between mb-4">
        <h3 class="text-base sm:text-lg font-bold text-slate-900">本文相关重点服务参考（仅引用契合本篇议题的案例）</h3>
        <a href="/airport-recommend/" class="text-sm text-cyan-600 hover:underline font-semibold">全量 28 家完整榜单在推荐中心 →</a>
      </div>
      <div class="flex flex-col space-y-3.5">
        {card_items}
      </div>
    </div>"""

    faq_html = ""
    if specific_faqs:
        f_items = ""
        for q, a in specific_faqs:
            f_items += f"""
        <div class="p-5 bg-white border border-slate-200 rounded-2xl shadow-xs space-y-2">
          <h4 class="text-base font-bold text-slate-900 mb-1">{q}</h4>
          <p class="text-sm sm:text-base text-slate-700 leading-relaxed">{a}</p>
        </div>"""
        faq_html = f"""
    <section class="my-8">
      <h3 class="text-lg sm:text-xl font-black text-slate-900 mb-4 border-l-4 border-cyan-600 pl-3">本篇专属问题解答</h3>
      <div class="space-y-3.5">
        {f_items}
      </div>
      <div class="mt-4 text-right">
        <a href="/faq/" class="text-sm text-slate-500 hover:text-cyan-600 font-medium">通用问题请参阅全站 100 题 FAQ 知识库 →</a>
      </div>
    </section>"""

    rel_html = ""
    if related_links:
        r_items = ""
        for u, t in related_links:
            r_items += f"""
          <a href="{u}" class="p-4 bg-white border border-slate-200 hover:border-cyan-300 rounded-xl text-sm text-slate-800 hover:text-cyan-700 font-medium transition flex items-center justify-between">
            <span>{t}</span>
            <span class="text-slate-400">→</span>
          </a>"""
        rel_html = f"""
    <section class="my-8 p-6 bg-slate-50 rounded-2xl border border-slate-200">
      <h3 class="text-base font-bold text-slate-900 mb-3">延伸阅读与关联专题</h3>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
        {r_items}
      </div>
    </section>"""

    lead_html = f"""
    <div class="p-6 bg-slate-50 border border-slate-200 rounded-2xl text-slate-800 text-base sm:text-lg leading-relaxed mb-6 shadow-xs">
      <div class="font-bold text-cyan-800 text-xs sm:text-sm uppercase tracking-wider mb-2">【核心问题直接回答】</div>
      <p class="font-medium text-slate-800 leading-relaxed">{contract['direct_answer']}</p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5 text-sm mb-8">
      <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-xs">
        <span class="text-slate-500 block mb-1 text-xs">👤 目标读者处境：</span>
        <span class="font-bold text-slate-900 text-sm sm:text-base">{contract['target_situation']}</span>
      </div>
      <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-xs">
        <span class="text-slate-500 block mb-1 text-xs">🎯 读后行动目标：</span>
        <span class="font-bold text-cyan-700 text-sm sm:text-base">{contract['action_goal']}</span>
      </div>
    </div>"""

    content = f"""---
layout: base.njk
title: "{title} ｜ 梯子墙客观资料"
description: "{meta_desc}"
permalink: "/{section}/{slug}/"
---

<article class="max-w-4xl mx-auto px-4 sm:px-6 py-10">
  <!-- Breadcrumb -->
  <nav class="text-xs text-slate-500 mb-6 flex items-center space-x-2">
    <a href="/" class="hover:text-cyan-600">首页</a>
    <span>/</span>
    <a href="/{section}/" class="hover:text-cyan-600">专栏分类</a>
    <span>/</span>
    <span class="text-slate-700">正文</span>
  </nav>

  <header class="mb-8 border-b border-slate-200 pb-6">
    <div class="flex items-center space-x-3 mb-3 text-xs text-slate-400">
      <span class="px-2.5 py-0.5 bg-cyan-50 text-cyan-700 border border-cyan-200 rounded-full font-bold">专题深度分析</span>
      <span>核对日期：2026年10月</span>
    </div>
    <h1 class="text-2xl sm:text-3xl md:text-4xl font-black text-slate-900 tracking-tight mb-4 leading-tight">
      {title}
    </h1>
    {lead_html}
  </header>

  <!-- Body Content -->
  <div class="space-y-8 text-slate-800 leading-relaxed text-base sm:text-lg">
    {sections_html}
  </div>

  {cards_html}

  {faq_html}

  {rel_html}

  <!-- Footer link back -->
  <footer class="mt-12 pt-6 border-t border-slate-200 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-500">
    <div>资料来源：服务商公开控制台与官方文档 ｜ 编辑：梯子墙</div>
    <div class="flex gap-4">
      <a href="/airport-recommend/" class="text-cyan-600 hover:underline font-semibold">机场推荐长文中心</a>
      <a href="/faq/" class="text-slate-500 hover:underline">常见问题 FAQ</a>
    </div>
  </footer>
</article>
"""
    out_path = f"src/{section}/{slug}.njk"
    with open(out_path, 'w', encoding='utf-8') as fp:
        fp.write(content)

print("Framework loaded successfully.")
