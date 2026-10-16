import os
import json
import re

articles = []

# Scan src directories
walk_dirs = ['airport', 'good-ladder', 'ladder-guide', 'ladder-tools', 'how-to-choose', 'service', 'faq', 'airport-recommend', 'about']

for d in walk_dirs:
    dir_path = os.path.join('src', d)
    if not os.path.exists(dir_path):
        continue
    for fname in os.listdir(dir_path):
        if fname.endswith('.njk'):
            fpath = os.path.join(dir_path, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # extract frontmatter
            title_match = re.search(r'title:\s*"([^"]+)"', content)
            desc_match = re.search(r'description:\s*"([^"]+)"', content)
            perm_match = re.search(r'permalink:\s*"([^"]+)"', content)
            
            title = title_match.group(1) if title_match else ""
            desc = desc_match.group(1) if desc_match else ""
            url = perm_match.group(1) if perm_match else ""
            
            if title and url:
                articles.append({
                    "title": title,
                    "desc": desc,
                    "url": url,
                    "category": d
                })

# Add home
articles.append({
    "title": "梯子墙 ｜ 好用的梯子、梯子工具与梯子推荐资料",
    "desc": "梯子墙：按服务资料与需求查看好用的梯子和推荐信息。",
    "url": "/",
    "category": "home"
})

with open('src/_data/search_index.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)

print(f"Generated search index with {len(articles)} searchable items!")
