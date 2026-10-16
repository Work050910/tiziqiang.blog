import os
import re
import json

base_dirs = ['good-ladder', 'ladder-guide', 'ladder-tools', 'how-to-choose', 'service']
posts = []

for b in base_dirs:
    dir_path = os.path.join('src', b)
    if not os.path.exists(dir_path):
        continue
    for f in sorted(os.listdir(dir_path)):
        if f.endswith('.njk') and f.startswith('post-'):
            file_path = os.path.join(dir_path, f)
            with open(file_path, 'r', encoding='utf-8') as fp:
                content = fp.read()
            
            title_m = re.search(r'title:\s*"([^"]+)"', content)
            title = title_m.group(1) if title_m else ""
            
            # extract H2s
            h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', content, re.DOTALL)
            h2_cleaned = [re.sub(r'<[^>]+>', '', h).strip() for h in h2s]
            
            # extract lead paragraph
            lead_m = re.search(r'【针对标题问题的直接结论】</div>\s*<p>(.*?)</p>', content, re.DOTALL)
            lead = lead_m.group(1).strip() if lead_m else ""
            
            posts.append({
                "path": f"{b}/{f}",
                "url": f"/{b}/{f.replace('.njk', '')}/",
                "title": title,
                "h2s": h2_cleaned,
                "lead": lead[:80]
            })

print(f"Total analyzed posts: {len(posts)}")

# Check H2 overlap across sections
h2_patterns = {}
for p in posts:
    for h in p['h2s']:
        h2_patterns[h] = h2_patterns.get(h, 0) + 1

print("\n--- Overlapping H2 patterns (> 1 occurrences) ---")
for h, count in sorted(h2_patterns.items(), key=lambda x: x[1], reverse=True):
    if count > 1:
        print(f"[{count} times] {h}")

