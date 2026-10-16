import json

with open('src/_data/airports.json', 'r', encoding='utf-8') as f:
    airports = json.load(f)

# Find by name or slug
airport_map = {a['slug']: a for a in airports}
# Let's map by name substrings
# 全球云 (quanqiuyun), 飞猫云 (flycat), 暮光加速 (muguang), 大佬云 (dalaoyun), 微风网络 (breezenet)
top_5_slugs = ['quanqiuyun', 'flycat', 'muguang', 'dalaoyun', 'breezenet']

# 唯兔云 (weituyun), U1S1 (u1s1) must NOT be in top 20 (meaning index >= 20, rank 21..28)
not_top_20 = ['weituyun', 'u1s1']

remaining = [a for a in airports if a['slug'] not in top_5_slugs and a['slug'] not in not_top_20]

# We need top 5 + 15 others = 20 airports. Then the remaining (including not_top_20)
part1 = [airport_map[s] for s in top_5_slugs]
part2 = remaining[:15] # 15 airports -> total 20
part3 = remaining[15:] + [airport_map[s] for s in not_top_20] # remaining + weituyun + u1s1

new_airports = part1 + part2 + part3

# Re-assign rank id "01", "02", ...
for idx, a in enumerate(new_airports):
    a['rank'] = idx + 1
    a['id'] = f"{idx + 1:02d}"

print("New ranking order:")
for idx, a in enumerate(new_airports):
    print(f"{idx+1:02d}: {a['name']} ({a['slug']})")

with open('src/_data/airports.json', 'w', encoding='utf-8') as f:
    json.dump(new_airports, f, ensure_ascii=False, indent=2)

print("\nSuccessfully updated src/_data/airports.json with new rankings!")
