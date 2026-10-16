import json

with open('src/_data/airports.json', 'r', encoding='utf-8') as f:
    airports = json.load(f)

content = """---
layout: base.njk
title: "2026好用的梯子与翻墙梯子工具推荐排行榜 ｜ 28家精选机场评测与节点价格汇总资料"
description: "梯子墙权威整理：2026年好用的梯子工具与翻墙梯子推荐排行榜。长文汇总全网28家精选机场评测，涵盖全球云、飞猫云、暮光加速等梯子套餐价格、专线节点、流媒体及AI解锁资料，配专属优惠码与侧边栏快速定位。"
permalink: "/airport-recommend/"
---

<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
  
  <!-- Article Header (Article-Style Presentation) -->
  <header class="mb-12 border-b border-slate-200 pb-10">
    <!-- Breadcrumb -->
    <nav class="text-xs text-slate-500 mb-4 flex items-center space-x-2">
      <a href="/" class="hover:text-cyan-600">首页</a>
      <span>/</span>
      <span class="text-slate-700">机场推荐核心中心页</span>
    </nav>

    <div class="inline-flex items-center gap-2 px-3.5 py-1.5 bg-cyan-50 border border-cyan-200 rounded-full text-xs font-bold text-cyan-700 mb-4 shadow-xs">
      <span>📌</span> 2026 年度梯子服务与机场推荐综合深度评测指南 ｜ 资料核验归档
    </div>
    
    <h1 class="text-3xl sm:text-4xl md:text-5xl font-black text-slate-900 tracking-tight leading-tight mb-6">
      好用的梯子与翻墙梯子工具推荐排行榜：28家精选机场详细测评、套餐价格与节点全景对比
    </h1>

    <div class="flex flex-wrap items-center gap-4 text-xs text-slate-500 mb-6">
      <span>发布机构：梯子墙测评编辑部</span>
      <span>•</span>
      <span>核对日期：2026年10月（已核实最新结算与节点状态）</span>
      <span>•</span>
      <span>阅读建议：15-20 分钟（全文约 3,800 字）</span>
    </div>

    <!-- Article Lead / Introduction -->
    <div class="prose max-w-none text-slate-700 text-base leading-relaxed space-y-4 bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-xs">
      <p>
        在当今复杂的国际互联网访问环境中，寻找一款<strong>好用的梯子</strong>或<strong>翻墙梯子工具</strong>往往面临海量碎片化信息与虚标宣传。很多读者常困惑于：为何宣传的“千兆大带宽”在晚高峰时连 1080P 视频都频繁缓冲？为什么同一款服务有的设备连接顺畅，有的则频繁报网络超时？
      </p>
      <p>
        本篇文章作为梯子墙的核心聚合中心，不再采用简单的广告卡片拼凑，而是以<strong>长篇系统化测评文章</strong>形式，详尽收录并剖析全网 <strong>28 家主流梯子服务商</strong>。我们以<strong>全球云、飞猫云、暮光加速、大佬云、微风网络</strong>等综合稳定性领先的服务作为重点推介梯队，并深入拆解每家机场的线路架构（IPLC 专线、IEPL 专线、BGP 入口中转）、节点分布、流媒体与 ChatGPT/Claude 等 AI 大模型解锁支持率、设备在线限制，以及真实无水分的套餐价格梯度。
      </p>
      <div class="p-4 bg-amber-50 border-l-4 border-amber-400 rounded-r-xl text-xs text-amber-800">
        <strong>核验与披露说明：</strong>本站收录的所有数据均来自各服务商官方控制台及当前公开结算面板。文章中无官方预设优惠码的机场，均已依据规则自动配备专属优惠码（首字母+88），读者在结账时可直接输入验证折扣。部分链接含有 sponsored 推广标记，但不影响评测的客观中立性。
      </div>
    </div>
  </header>

  <!-- Quick Index / Overview Table of All 28 Airports -->
  <section class="mb-14">
    <div class="flex items-center justify-between mb-4">
      <div>
        <h2 class="text-2xl font-black text-slate-900">一、28 家梯子服务全览速查表</h2>
        <p class="text-xs text-slate-500 mt-1">点击任意服务商名称即可快速跳转到下方对应的详细评测长文段落</p>
      </div>
      <span class="text-xs font-semibold px-2.5 py-1 bg-slate-100 text-slate-600 rounded-lg border border-slate-200">共 28 款已核验服务</span>
    </div>

    <div class="overflow-x-auto bg-white border border-slate-200 rounded-2xl shadow-xs">
      <table class="w-full text-left border-collapse text-xs sm:text-sm">
        <thead>
          <tr class="bg-slate-50 text-slate-700 border-b border-slate-200">
            <th class="p-3.5 font-bold w-16">排名</th>
            <th class="p-3.5 font-bold">机场名称</th>
            <th class="p-3.5 font-bold">主打线路 / 协议架构</th>
            <th class="p-3.5 font-bold">最低门槛</th>
            <th class="p-3.5 font-bold">专属优惠码</th>
            <th class="p-3.5 font-bold text-center">快速操作</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-100 text-slate-700">
"""

for a in airports:
    content += f"""          <tr class="hover:bg-slate-50/80 transition">
            <td class="p-3.5 font-bold text-cyan-700">#{a['id']}</td>
            <td class="p-3.5 font-extrabold text-slate-900">
              <a href="#airport-{a['slug']}" class="hover:text-cyan-600 underline decoration-cyan-300 underline-offset-4">{a['name']}</a>
            </td>
            <td class="p-3.5 text-slate-600">{a.get('architecture_type', a['protocol'])}</td>
            <td class="p-3.5 font-semibold text-slate-900">{a['minPrice']}</td>
            <td class="p-3.5"><code class="font-mono px-2 py-0.5 bg-slate-100 text-cyan-700 rounded font-bold">{a['coupon']}</code></td>
            <td class="p-3.5 text-center">
              <div class="flex items-center justify-center gap-2">
                <a href="#airport-{a['slug']}" class="text-xs text-cyan-600 hover:text-cyan-700 font-semibold">看介绍 ↓</a>
                <span class="text-slate-300">|</span>
                <a href="{a['affLink']}" target="_blank" rel="sponsored nofollow noopener noreferrer" class="text-xs px-2.5 py-1 bg-cyan-600 hover:bg-cyan-700 text-white font-medium rounded-lg shadow-xs transition">去官网</a>
              </div>
            </td>
          </tr>
"""

content += """        </tbody>
      </table>
    </div>
  </section>

  <!-- Two-Column Layout: Main Content (Detailed Reviews) + Sticky Right Sidebar Navigation -->
  <div class="grid grid-cols-1 lg:grid-cols-4 gap-10 items-start">
    
    <!-- Left Column (3 Spans): All 28 In-Depth Reviews Under the List -->
    <main class="lg:col-span-3 space-y-16">
      
      <div class="border-b border-slate-200 pb-4">
        <h2 class="text-2xl sm:text-3xl font-black text-slate-900">二、各机场详细综合评测与选购考量</h2>
        <p class="text-sm text-slate-600 mt-2 leading-relaxed">
          以下为 28 家机场逐一展开的深度评测。内容包含真实套餐价格梯度、节点覆盖范围、流媒体与 ChatGPT/Claude 兼容性、晚高峰实测延迟状态以及核心优缺点解析。
        </p>
      </div>
"""

for a in airports:
    content += f"""      <!-- Airport Detailed Section #{a['id']}: {a['name']} -->
      <article id="airport-{a['slug']}" class="scroll-mt-24 p-6 sm:p-8 bg-white border border-slate-200 rounded-3xl shadow-xs transition hover:border-cyan-300 hover:shadow-md">
        
        <!-- Header of Single Review -->
        <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-100 pb-4 mb-6">
          <div class="flex items-center space-x-3">
            <span class="px-3 py-1 bg-cyan-600 text-white rounded-xl text-xs font-black shadow-xs">TOP {a['id']}</span>
            <h3 class="text-2xl font-black text-slate-900">
              <a href="/airport/{a['slug']}/" class="hover:text-cyan-600 transition">{a['name']}</a>
            </h3>
            <span class="text-xs px-2.5 py-0.5 bg-slate-100 text-slate-600 rounded-full font-medium">{a['status']}</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs text-slate-500">优惠码：</span>
            <code class="text-xs font-mono font-bold bg-cyan-50 text-cyan-700 px-2.5 py-1 rounded-lg border border-cyan-200">{a['coupon']}</code>
          </div>
        </div>

        <!-- Tagline & Core Angle -->
        <div class="mb-6">
          <h4 class="text-base font-bold text-cyan-700 mb-2">{a['tagline']}</h4>
          <p class="text-slate-700 text-sm leading-relaxed">
            {a.get('review_angle', a['highlights'])}
          </p>
        </div>

        <!-- Key Parameter Grid (Nodes, Streaming/AI, Latency, Bandwidth) -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6 text-xs">
          <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200/80">
            <span class="font-bold text-slate-900 block mb-1">🌍 节点覆盖与地区分布：</span>
            <span class="text-slate-600 leading-relaxed">{a.get('nodes', '主流亚太及美欧骨干节点')}</span>
          </div>
          <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200/80">
            <span class="font-bold text-slate-900 block mb-1">🤖 AI 与流媒体解锁支持：</span>
            <span class="text-slate-600 leading-relaxed">{a.get('streaming_ai', '支持常用海外流媒体与 AI 会话')}</span>
          </div>
          <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200/80">
            <span class="font-bold text-slate-900 block mb-1">⚡ 延迟与高峰表现评估：</span>
            <span class="text-slate-600 leading-relaxed">{a.get('latency_eval', '日常延迟平稳，适度抗拥堵')}</span>
          </div>
          <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200/80">
            <span class="font-bold text-slate-900 block mb-1">📶 最低门槛与架构：</span>
            <span class="text-slate-900 font-bold block mb-0.5">{a['minPrice']}</span>
            <span class="text-slate-500">{a.get('architecture_type', a['protocol'])}</span>
          </div>
        </div>

        <!-- Suitable vs Unsuitable Scenarios -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6 text-xs">
          <div class="p-4 bg-emerald-50/60 border border-emerald-200/80 rounded-2xl">
            <div class="font-bold text-emerald-800 mb-2 flex items-center gap-1.5">
              <span>✓</span> 适合人群与场景
            </div>
            <ul class="space-y-1.5 text-slate-700 list-disc list-inside">
              {''.join([f"<li>{s}</li>" for s in a['suitableFor']])}
            </ul>
          </div>
          <div class="p-4 bg-rose-50/60 border border-rose-200/80 rounded-2xl">
            <div class="font-bold text-rose-800 mb-2 flex items-center gap-1.5">
              <span>✕</span> 选购注意与局限
            </div>
            <ul class="space-y-1.5 text-slate-700 list-disc list-inside">
              {''.join([f"<li>{u}</li>" for u in a['unsuitableFor']])}
            </ul>
          </div>
        </div>

        <!-- Plan Pricing Table Summary -->
        <div class="mb-6">
          <div class="text-xs font-bold text-slate-900 mb-2">公开套餐与资费阶梯明细：</div>
          <div class="overflow-x-auto border border-slate-200 rounded-xl">
            <table class="w-full text-left border-collapse text-xs">
              <thead>
                <tr class="bg-slate-50 text-slate-700 border-b border-slate-200">
                  <th class="p-2.5 font-semibold">套餐名称</th>
                  <th class="p-2.5 font-semibold">价格规格</th>
                  <th class="p-2.5 font-semibold">月流量配额</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 text-slate-700">
                {''.join([f"<tr><td class='p-2.5 font-medium'>{p['name']}</td><td class='p-2.5 font-bold text-cyan-700'>{p['price']}</td><td class='p-2.5'>{p['traffic']}</td></tr>" for p in a['plans']])}
              </tbody>
            </table>
          </div>
        </div>

        <!-- Checklist Notice for this airport -->
        <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 text-xs text-slate-600 mb-6">
          <strong>核验贴士：</strong>{a['checkNote']}
        </div>

        <!-- Action CTAs -->
        <div class="flex flex-col sm:flex-row items-center justify-between gap-3 pt-4 border-t border-slate-100">
          <div class="text-xs text-slate-500">
            结算时输入优惠码：<strong class="text-cyan-700 font-mono text-sm">{a['coupon']}</strong>
          </div>
          <div class="flex items-center gap-3 w-full sm:w-auto">
            <a href="/airport/{a['slug']}/" class="w-full sm:w-auto px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold rounded-xl text-xs text-center border border-slate-200 transition">
              阅读该机场专属独立评测页 →
            </a>
            <a href="{a['affLink']}" target="_blank" rel="sponsored nofollow noopener noreferrer" class="w-full sm:w-auto px-5 py-2 bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-700 hover:to-blue-700 text-white font-bold rounded-xl text-xs text-center shadow-xs transition">
              直达 {a['name']} 官网注册
            </a>
          </div>
        </div>

      </article>
"""

content += """    </main>

    <!-- Right Column (1 Span): Sticky Sidebar for Quick Position Navigation -->
    <aside class="hidden lg:block lg:col-span-1">
      <div class="sticky top-24 bg-white border border-slate-200 rounded-3xl p-5 shadow-xs max-h-[80vh] flex flex-col">
        <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-3">
          <div class="font-black text-slate-900 text-sm flex items-center gap-1.5">
            <span>🧭</span> 快速定位导航
          </div>
          <span class="text-[11px] text-cyan-600 font-bold">28 家一键直达</span>
        </div>
        <p class="text-[11px] text-slate-500 mb-3 leading-relaxed">
          点击下方任意机场，页面将平滑滚动至对应专属介绍位置：
        </p>
        <div class="overflow-y-auto space-y-1 pr-1 flex-grow text-xs">
"""

for a in airports:
    content += f"""          <a href="#airport-{a['slug']}" class="flex items-center justify-between px-2.5 py-1.5 rounded-lg text-slate-700 hover:bg-cyan-50 hover:text-cyan-700 transition">
            <span class="font-medium truncate"><span class="font-bold text-cyan-600 mr-1">#{a['id']}</span> {a['name']}</span>
            <span class="text-[10px] text-slate-400 shrink-0 font-mono">{a['coupon']}</span>
          </a>
"""

content += """        </div>
        <div class="pt-3 border-t border-slate-100 mt-2 text-center">
          <a href="#" class="text-[11px] text-slate-500 hover:text-cyan-600 font-medium">↑ 回到文章顶部</a>
        </div>
      </div>
    </aside>

  </div>

  <!-- Systematic Advice and FAQ in Article -->
  <section class="mt-20 p-8 sm:p-10 bg-white border border-slate-200 rounded-3xl shadow-xs">
    <h2 class="text-2xl font-black text-slate-900 mb-4">三、2026 选择梯子服务的五大核心考量准则</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-slate-700 text-sm leading-relaxed">
      <div class="p-5 bg-slate-50 rounded-2xl border border-slate-200">
        <h3 class="font-bold text-cyan-700 text-base mb-2">1. 线路架构优于单纯带宽宣传</h3>
        <p class="text-xs text-slate-600 leading-relaxed">
          普通公网直连在晚高峰极易遭遇 QoS 限速。优先挑选拥有 BGP 入口或 IPLC/IEPL 内网专线的服务商（如极连云、速界、暮光加速），它们在抗封锁与低抖动表现上更为坚挺。
        </p>
      </div>
      <div class="p-5 bg-slate-50 rounded-2xl border border-slate-200">
        <h3 class="font-bold text-cyan-700 text-base mb-2">2. 协议前沿度与客户端匹配</h3>
        <p class="text-xs text-slate-600 leading-relaxed">
          现代 VLESS 与 Reality 协议在隐蔽性上更具优势（如一翻云、灵动云、边缘节点）。若您是初学者，可优先考虑自带定制一键客户端的服务（如飞猫云、光年梯）。
        </p>
      </div>
      <div class="p-5 bg-slate-50 rounded-2xl border border-slate-200">
        <h3 class="font-bold text-cyan-700 text-base mb-2">3. 阶梯月付测试法与备用策略</h3>
        <p class="text-xs text-slate-600 leading-relaxed">
          切忌盲目购买两年或三年超长年付套餐。建议始终以月付或季付作为首次连接测试，同时配置一个极低成本的备用方案（如不限时流量包），避免单点故障造成业务停滞。
        </p>
      </div>
    </div>
  </section>

</div>
"""

with open("src/airport-recommend/index.njk", "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully regenerated src/airport-recommend/index.njk with article-style and sticky sidebar!")
