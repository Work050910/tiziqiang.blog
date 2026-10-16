import os
import re
import json

with open('src/_includes/base.njk', 'r', encoding='utf-8') as f:
    base_template = f.read()

count = 0
for root, dirs, files in os.walk('src'):
    if '_data' in root or '_includes' in root or 'src/css' in root:
        continue
    for file in sorted(files):
        if not file.endswith('.njk'):
            continue
        file_path = os.path.join(root, file)
        print(f"Processing {file_path}...")
        with open(file_path, 'r', encoding='utf-8') as fp:
            raw = fp.read()
        fm_match = re.search(r'^---\n(.*?)\n---\n(.*)$', raw, re.DOTALL)
        if not fm_match:
            print(f"No FM in {file_path}")
            continue
        count += 1

print(f"Tested {count} files successfully!")
