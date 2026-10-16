import os
import re

print("Starting sitewide typography upgrade...")

# 1. Update rewrite_cluster_b_c_d_e.py with enlarged typography
with open("rewrite_cluster_b_c_d_e.py", "r", encoding="utf-8") as f:
    cluster_b = f.read()

# Replace tiny font classes in cluster_b
cluster_b = cluster_b.replace('table class="w-full text-left border-collapse text-xs"', 'table class="w-full text-left border-collapse text-sm sm:text-base"')
cluster_b = cluster_b.replace('ul class="text-xs sm:text-sm space-y-2 list-disc list-inside text-slate-600"', 'ul class="text-base space-y-2.5 list-disc list-inside text-slate-700"')
cluster_b = cluster_b.replace('ol class="text-xs sm:text-sm space-y-2 list-decimal list-inside text-slate-600"', 'ol class="text-base space-y-2.5 list-decimal list-inside text-slate-700"')
cluster_b = cluster_b.replace('p class="text-xs text-slate-500 pt-2 border-t border-slate-100">结论：', 'div class="p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm sm:text-base font-semibold text-slate-800 mt-4">结论：')
cluster_b = cluster_b.replace('</p>\n      </div>\n    </section>\n    """,\n    context_airports=["quanqiuyun"', '</div>\n      </div>\n    </section>\n    """,\n    context_airports=["quanqiuyun"')
cluster_b = cluster_b.replace('p class="text-xs text-slate-500', 'p class="text-sm text-slate-600 font-medium')
cluster_b = cluster_b.replace('text-xs text-slate-600', 'text-sm sm:text-base text-slate-700')
cluster_b = cluster_b.replace('text-xs font-semibold', 'text-sm font-semibold')
cluster_b = cluster_b.replace('text-xs sm:text-sm', 'text-base')

with open("rewrite_cluster_b_c_d_e.py", "w", encoding="utf-8") as f:
    f.write(cluster_b)

# 2. Update rewrite_cluster_a_b.py with enlarged typography
with open("rewrite_cluster_a_b.py", "r", encoding="utf-8") as f:
    cluster_a = f.read()

cluster_a = cluster_a.replace('table class="w-full text-left border-collapse text-xs sm:text-sm"', 'table class="w-full text-left border-collapse text-sm sm:text-base"')
cluster_a = cluster_a.replace('table class="w-full text-left border-collapse text-xs"', 'table class="w-full text-left border-collapse text-sm sm:text-base"')
cluster_a = cluster_a.replace('ul class="text-xs sm:text-sm space-y-2 list-disc list-inside text-slate-600"', 'ul class="text-base space-y-2.5 list-disc list-inside text-slate-700"')
cluster_a = cluster_a.replace('ol class="text-xs sm:text-sm space-y-2 list-decimal list-inside text-slate-600"', 'ol class="text-base space-y-2.5 list-decimal list-inside text-slate-700"')
cluster_a = cluster_a.replace('text-xs text-slate-600', 'text-sm sm:text-base text-slate-700')
cluster_a = cluster_a.replace('text-xs sm:text-sm', 'text-base')

with open("rewrite_cluster_a_b.py", "w", encoding="utf-8") as f:
    f.write(cluster_a)

# 3. Update rewrite_cluster_c_d_e.py with enlarged typography
with open("rewrite_cluster_c_d_e.py", "r", encoding="utf-8") as f:
    cluster_c = f.read()

cluster_c = cluster_c.replace('table class="w-full text-left border-collapse text-xs"', 'table class="w-full text-left border-collapse text-sm sm:text-base"')
cluster_c = cluster_c.replace('ul class="text-xs sm:text-sm space-y-2 list-disc list-inside text-slate-600"', 'ul class="text-base space-y-2.5 list-disc list-inside text-slate-700"')
cluster_c = cluster_c.replace('ol class="text-xs sm:text-sm space-y-2 list-decimal list-inside text-slate-600"', 'ol class="text-base space-y-2.5 list-decimal list-inside text-slate-700"')
cluster_c = cluster_c.replace('text-xs text-slate-600', 'text-sm sm:text-base text-slate-700')
cluster_c = cluster_c.replace('text-xs text-slate-500', 'text-sm text-slate-600')
cluster_c = cluster_c.replace('text-xs sm:text-sm font-mono', 'text-sm sm:text-base font-mono')
cluster_c = cluster_c.replace('text-xs sm:text-sm', 'text-base')

with open("rewrite_cluster_c_d_e.py", "w", encoding="utf-8") as f:
    f.write(cluster_c)

print("Updated generator scripts with enlarged typography!")

# Re-run cluster generator scripts
import subprocess
subprocess.run(["python3", "rewrite_cluster_a_b.py"], check=True)
subprocess.run(["python3", "rewrite_cluster_b_c_d_e.py"], check=True)
subprocess.run(["python3", "rewrite_cluster_c_d_e.py"], check=True)
print("Regenerated Cluster A, B, C, D, E posts with enlarged typography!")

# 4. Scan and upgrade remaining files in src/
target_dirs = ['good-ladder', 'ladder-guide', 'ladder-tools', 'how-to-choose', 'service', 'airport', 'about', 'faq']
updated_count = 0

for d in target_dirs:
    dir_path = os.path.join('src', d)
    if not os.path.exists(dir_path):
        continue
    for fname in os.listdir(dir_path):
        if not fname.endswith('.njk'):
            continue
        fpath = os.path.join(dir_path, fname)
        with open(fpath, 'r', encoding='utf-8') as fp:
            txt = fp.read()
            
        orig = txt
        
        # Upgrade article body container
        txt = txt.replace('text-slate-700 leading-relaxed text-sm sm:text-base', 'text-slate-800 leading-relaxed text-base sm:text-lg')
        txt = txt.replace('text-slate-700 leading-relaxed space-y-4 text-sm sm:text-base', 'text-slate-800 leading-relaxed space-y-4 text-base sm:text-lg')
        txt = txt.replace('text-slate-700 leading-relaxed space-y-4 text-sm', 'text-slate-800 leading-relaxed space-y-4 text-base')
        
        # Upgrade bullet lists and ol
        txt = re.sub(r'class="([^"]*?)text-xs sm:text-sm([^"]*?)"', r'class="\1text-base\2"', txt)
        txt = re.sub(r'class="text-xs text-slate-600 space-y-2 list-disc list-inside"', r'class="text-base text-slate-700 space-y-2.5 list-disc list-inside"', txt)
        
        # Upgrade table text
        txt = txt.replace('border-collapse text-xs', 'border-collapse text-sm sm:text-base')
        
        # Upgrade cards descriptions in articles
        txt = txt.replace('text-xs text-slate-600 mt-1 leading-relaxed', 'text-sm sm:text-base text-slate-700 mt-1 leading-relaxed')
        txt = txt.replace('text-xs text-slate-600 mt-0.5 line-clamp-1', 'text-sm text-slate-700 mt-1 leading-relaxed')
        txt = txt.replace('text-slate-600 text-xs sm:text-sm mb-4', 'text-slate-700 text-sm sm:text-base mb-4')
        
        # Upgrade FAQs inside articles
        txt = txt.replace('h3 class="text-sm sm:text-base font-bold text-slate-900 mb-2"', 'h3 class="text-base sm:text-lg font-bold text-slate-900 mb-2"')
        txt = txt.replace('p class="text-xs sm:text-sm text-slate-600 leading-relaxed"', 'p class="text-base text-slate-700 leading-relaxed"')
        
        # Upgrade airport review single pages (grid parameter boxes & pros/cons)
        txt = txt.replace('grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2 text-xs', 'grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2 text-sm')
        txt = txt.replace('grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6 text-xs', 'grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6 text-sm')
        txt = txt.replace('grid grid-cols-1 md:grid-cols-2 gap-4 mb-6 text-xs', 'grid grid-cols-1 md:grid-cols-2 gap-4 mb-6 text-sm')
        txt = txt.replace('text-xs sm:text-sm text-slate-600', 'text-base text-slate-700')
        txt = txt.replace('text-xs text-slate-500 font-semibold', 'text-sm text-slate-600 font-semibold')
        txt = txt.replace('text-xs text-slate-500', 'text-sm text-slate-500')
        
        if txt != orig:
            with open(fpath, 'w', encoding='utf-8') as out_fp:
                out_fp.write(txt)
            updated_count += 1

print(f"Updated typography in {updated_count} templates across src/!")
