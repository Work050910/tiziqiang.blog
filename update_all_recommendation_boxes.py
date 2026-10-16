import glob
import json
import re

with open('src/_data/airports.json', 'r', encoding='utf-8') as f:
    airports = json.load(f)
airport_map = {a['slug']: a for a in airports}

def make_card(a):
    return f"""        <div class="p-5 bg-white rounded-2xl border border-slate-200 hover:border-cyan-300 transition shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div class="flex items-start sm:items-center gap-4">
            <span class="text-base font-bold text-white bg-cyan-600 px-3 py-1.5 rounded-xl font-mono shrink-0">#{a['id']}</span>
            <div>
              <div class="flex items-center gap-2.5">
                <h3 class="font-bold text-slate-900 text-base">{a['name']}</h3>
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

def find_box_bounds(content):
    start_pos = -1
    for marker in [
        '<!-- Contextually Relevant Airports',
        '<!-- Section 4: Relevant Airports',
        '<!-- Section: Relevant Airports',
        '符合本篇评判逻辑的代表性梯子服务参考'
    ]:
        idx = content.find(marker)
        if idx != -1:
            if marker == '符合本篇评判逻辑的代表性梯子服务参考':
                sec_idx = content.rfind('<section', 0, idx)
                if sec_idx != -1:
                    start_pos = sec_idx
            else:
                start_pos = idx
            break
            
    if start_pos == -1:
        return -1, -1

    end_pos = -1
    for end_marker in [
        '<!-- Specific FAQs',
        '<!-- Section 5: Specific FAQs',
        '本篇专属问题解答',
        '关于本篇主题的常见问题解答',
        '延伸阅读与关联专题',
        '<!-- Footer',
        '<footer'
    ]:
        idx = content.find(end_marker, start_pos)
        if idx != -1:
            if end_marker in ['本篇专属问题解答', '关于本篇主题的常见问题解答', '延伸阅读与关联专题']:
                sec_idx = content.rfind('<section', start_pos, idx)
                if sec_idx != -1:
                    end_pos = sec_idx
                    break
            else:
                end_pos = idx
                break
                
    return start_pos, end_pos

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    s, e = find_box_bounds(content)
    if s == -1 or e == -1 or s >= e:
        print(f"FAILED to find bounds for {file_path}")
        return False

    box_snippet = content[s:e]
    existing_slugs = re.findall(r'/airport/([a-z0-9-]+)/', box_snippet)

    # 1. quanqiuyun MUST be first
    chosen = ['quanqiuyun']
    # 2. Add other unique slugs from the existing box
    for sl in existing_slugs:
        if sl != 'quanqiuyun' and sl in airport_map and sl not in chosen:
            chosen.append(sl)
    # 3. Fallbacks to ensure exactly 5 airports
    fallbacks = ['flycat', 'muguang', 'dalaoyun', 'breezenet', 'jilianyun', 'guangnianti', 'edgenova']
    for fb in fallbacks:
        if len(chosen) >= 5:
            break
        if fb in airport_map and fb not in chosen:
            chosen.append(fb)
    chosen = chosen[:5]

    cards_html = [make_card(airport_map[sl]) for sl in chosen]
    cards_joined = "\n".join(cards_html)

    new_box = f"""  <!-- Section: Relevant Airports Context (5 家推荐栏，#01 全球云首位，单列并列纵向排列) -->
  <section class="my-10 p-6 bg-slate-50 border border-slate-200 rounded-3xl">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between mb-4 gap-2">
      <div>
        <h2 class="text-xl sm:text-2xl font-black text-slate-900 border-l-4 border-cyan-600 pl-3">
          符合本篇评判逻辑的代表性梯子服务参考
        </h2>
        <p class="text-xs sm:text-sm text-slate-500 mt-1 pl-4">（按线路架构、晚高峰抗拥堵与服务资费核查综合推荐）</p>
      </div>
      <a href="/airport-recommend/" class="text-sm text-cyan-600 hover:underline font-semibold shrink-0">
        全量 28 家完整榜单在推荐中心 →
      </a>
    </div>
    <div class="flex flex-col space-y-3.5">
{cards_joined}
    </div>
  </section>

  """

    new_content = content[:s] + new_box + content[e:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True

files = sorted(glob.glob('src/**/post-*.njk', recursive=True))
success_count = 0
for f in files:
    if process_file(f):
        success_count += 1

print(f"Updated {success_count} / {len(files)} files successfully!")
