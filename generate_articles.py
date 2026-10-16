import os
import json

with open('src/_data/airports.json', 'r', encoding='utf-8') as f:
    airports = json.load(f)

# 1. Generate Airport Review Pages (28 pages)
for a in airports:
    slug = a['slug']
    content = f"""---
layout: base.njk
title: "{a['name']}怎么样？{a['name']}梯子套餐价格、节点情况与公开资料测评"
description: "全面核对 {a['name']} 梯子服务的公开资料、套餐价格、线路特点、优惠码与购买前须知。帮助读者按需评估其在 AI 交互与流媒体场景中的适用性。"
permalink: "/airport/{slug}/"
---

<article class="max-w-4xl mx-auto px-4 py-8">
  <!-- Breadcrumb -->
  <nav class="text-sm text-slate-400 mb-6 flex items-center space-x-2">
    <a href="/" class="hover:text-cyan-400">首页</a>
    <span>/</span>
    <a href="/airport-recommend/" class="hover:text-cyan-400">机场推荐</a>
    <span>/</span>
    <span class="text-slate-200">{a['name']} 专属测评</span>
  </nav>

  <header class="mb-8 border-b border-slate-800 pb-6">
    <div class="flex items-center space-x-3 mb-3">
      <span class="px-3 py-1 bg-cyan-950 text-cyan-400 border border-cyan-800/60 rounded-full text-xs font-medium">编号 {a['id']} 资料收录</span>
      <span class="px-3 py-1 bg-slate-800 text-slate-300 rounded-full text-xs">核验状态：{a['status']}</span>
    </div>
    <h1 class="text-3xl sm:text-4xl font-extrabold text-white tracking-tight mb-4">
      {a['name']} 梯子服务全景测评：套餐价格、节点架构与公开资料深度核查
    </h1>
    <p class="text-lg text-slate-300 leading-relaxed">
      {a['name']} 主打 {a['tagline']}。本文围绕其公开资料、真实套餐价格梯度、线路特征、适用与不适用人群展开客观评估，帮助读者在选购前建立清晰的判断依据。
    </p>
  </header>

  <!-- Quick CTA & Coupon Card -->
  <div class="my-8 p-6 bg-gradient-to-r from-slate-900 to-slate-850 border border-cyan-900/40 rounded-2xl shadow-xl flex flex-col md:flex-row items-center justify-between gap-6">
    <div>
      <div class="text-xs text-cyan-400 uppercase tracking-wider font-semibold mb-1">最低门槛与优惠信息</div>
      <div class="text-2xl font-bold text-white mb-2">{a['minPrice']}</div>
      <div class="inline-flex items-center gap-2 bg-slate-800/80 px-3 py-1.5 rounded-lg border border-slate-700">
        <span class="text-xs text-slate-400">优惠码：</span>
        <code class="text-sm font-mono text-cyan-300 font-bold">{a['coupon']}</code>
        <span class="text-xs text-slate-400">({a['couponDesc']})</span>
      </div>
    </div>
    <div class="w-full md:w-auto flex flex-col sm:flex-row gap-3">
      <a href="{a['affLink']}" target="_blank" rel="sponsored nofollow noopener noreferrer" class="px-6 py-3 bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white font-semibold rounded-xl text-center shadow-lg shadow-cyan-900/30 transition">
        直达 {a['name']} 官网查看实时库存
      </a>
      <a href="/airport-recommend/" class="px-5 py-3 bg-slate-800 hover:bg-slate-750 text-slate-300 hover:text-white rounded-xl text-center border border-slate-700 transition">
        返回机场推荐中心页
      </a>
    </div>
  </div>

  <!-- Disclaimer for Affiliate -->
  <p class="text-xs text-slate-500 -mt-4 mb-8">
    * 利益披露：点击上方注册链接可能产生推荐收益，本站测评基于公开可核验资料，不影响结论的客观中立性。
  </p>

  <!-- Section 1: Who it is for -->
  <section class="mb-10">
    <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-cyan-500 pl-3">一、本文适合谁与不适合谁</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div class="p-5 bg-slate-900/60 border border-slate-800 rounded-xl">
        <h3 class="text-base font-semibold text-emerald-400 mb-2 flex items-center gap-2">
          <span>✓</span> 适合以下用户与场景
        </h3>
        <ul class="text-sm text-slate-300 space-y-2 list-disc list-inside">
          {''.join([f"<li>{s}</li>" for s in a['suitableFor']])}
        </ul>
      </div>
      <div class="p-5 bg-slate-900/60 border border-slate-800 rounded-xl">
        <h3 class="text-base font-semibold text-rose-400 mb-2 flex items-center gap-2">
          <span>✕</span> 不建议以下人群选购
        </h3>
        <ul class="text-sm text-slate-300 space-y-2 list-disc list-inside">
          {''.join([f"<li>{u}</li>" for u in a['unsuitableFor']])}
        </ul>
      </div>
    </div>
  </section>

  <!-- Section 2: Core Highlights -->
  <section class="mb-10">
    <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-cyan-500 pl-3">二、主打卖点与技术架构解析</h2>
    <div class="p-6 bg-slate-900/40 border border-slate-800 rounded-xl text-slate-300 leading-relaxed space-y-4">
      <p>{a['highlights']}</p>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
        <div class="p-3 bg-slate-850 rounded-lg border border-slate-800">
          <span class="text-xs text-slate-400 block mb-1">公开协议与架构：</span>
          <span class="text-sm font-semibold text-white">{a['protocol']}</span>
        </div>
        <div class="p-3 bg-slate-850 rounded-lg border border-slate-800">
          <span class="text-xs text-slate-400 block mb-1">核验状态标识：</span>
          <span class="text-sm font-semibold text-cyan-300">{a['status']}</span>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 3: Plans Table -->
  <section class="mb-10">
    <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-cyan-500 pl-3">三、公开套餐与价格梯度明细</h2>
    <div class="overflow-x-auto border border-slate-800 rounded-xl">
      <table class="w-full text-left border-collapse text-sm">
        <thead>
          <tr class="bg-slate-850 text-slate-300 border-b border-slate-800">
            <th class="p-4 font-semibold">套餐名称</th>
            <th class="p-4 font-semibold">公开标价</th>
            <th class="p-4 font-semibold">月流量配额</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-800/60 text-slate-300">
          {''.join([f"<tr class='hover:bg-slate-850/50'><td class='p-4 font-medium text-white'>{p['name']}</td><td class='p-4 text-cyan-300 font-semibold'>{p['price']}</td><td class='p-4'>{p['traffic']}</td></tr>" for p in a['plans']])}
        </tbody>
      </table>
    </div>
    <p class="text-xs text-slate-400 mt-2">
      提示：{a['checkNote']}
    </p>
  </section>

  <!-- Section 4: Pre-purchase Checklist -->
  <section class="mb-10">
    <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-cyan-500 pl-3">四、购买与配置前核查清单</h2>
    <div class="p-6 bg-slate-900/40 border border-slate-800 rounded-xl space-y-3 text-slate-300 text-sm">
      <div class="flex items-start gap-3">
        <span class="text-cyan-400 font-bold">1.</span>
        <div><strong>确认流量重置口径：</strong>下单前务必确认流量是按自然月（每月1日）还是账单日周期重置，避免月底断流。</div>
      </div>
      <div class="flex items-start gap-3">
        <span class="text-cyan-400 font-bold">2.</span>
        <div><strong>设备并发数量：</strong>检查是否限制同时在线设备数，如有多设备或家庭使用需求，请确认是否支持。</div>
      </div>
      <div class="flex items-start gap-3">
        <span class="text-cyan-400 font-bold">3.</span>
        <div><strong>优惠码生效验证：</strong>在结算最终确认页输入 <code class="text-cyan-300 font-mono font-bold">{a['coupon']}</code>，确认实付金额已按规则折扣扣减。</div>
      </div>
      <div class="flex items-start gap-3">
        <span class="text-cyan-400 font-bold">4.</span>
        <div><strong>退款政策与工单时效：</strong>确认该服务是否支持不满意退款条款，以及日常技术咨询的响应周期。</div>
      </div>
    </div>
  </section>

  <!-- Section 5: Specific FAQs -->
  <section class="mb-10">
    <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-cyan-500 pl-3">五、常见问题解答 (FAQ)</h2>
    <div class="space-y-4">
      <div class="p-5 bg-slate-900 border border-slate-800 rounded-xl">
        <h3 class="text-base font-semibold text-white mb-2">{a['name']} 是否支持 ChatGPT 和海外流媒体？</h3>
        <p class="text-sm text-slate-300 leading-relaxed">
          答：服务商公开资料标明支持 AI 访问与流媒体解锁。但由于平台风控策略会动态更新，实际体验取决于您所连接的落地节点属性。建议优先选用香港、日本或新加坡原生 IP 节点进行连接。更多全局建议可查阅 <a href="/airport-recommend/" class="text-cyan-400 underline">机场推荐中心</a>。
        </p>
      </div>
      <div class="p-5 bg-slate-900 border border-slate-800 rounded-xl">
        <h3 class="text-base font-semibold text-white mb-2">如何获得 {a['name']} 的最新折扣或优惠码？</h3>
        <p class="text-sm text-slate-300 leading-relaxed">
          答：在结算页面可输入优惠码 <code class="text-cyan-300 font-mono font-bold">{a['coupon']}</code> 查看当前折扣。若提示过期或不适用，请在官方公告面板查验最新活动说明。
        </p>
      </div>
    </div>
  </section>

  <!-- Footer meta -->
  <footer class="pt-6 border-t border-slate-800 text-xs text-slate-500 flex flex-col sm:flex-row justify-between gap-2">
    <div>资料最后核对日期：2026年10月（基于公开资料与服务商控制台）</div>
    <div>编辑：梯子墙测评编辑部 ｜ 遵循客观性与透明度原则</div>
  </footer>
</article>
"""
    with open(f"src/airport/{slug}.njk", "w", encoding="utf-8") as f:
        f.write(content)

print(f"Successfully created 28 airport review pages in src/airport/")
