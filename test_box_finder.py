import glob
import json
import re

with open('src/_data/airports.json', 'r', encoding='utf-8') as f:
    airports = json.load(f)
airport_map = {a['slug']: a for a in airports}

files = sorted(glob.glob('src/**/post-*.njk', recursive=True))

def find_box_bounds(content):
    # Find start
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
                # find the opening <section tag before this
                sec_idx = content.rfind('<section', 0, idx)
                if sec_idx != -1:
                    start_pos = sec_idx
            else:
                start_pos = idx
            break
            
    if start_pos == -1:
        return -1, -1

    # Find end: the next section or footer
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
            # If end marker is inside a section tag like '本篇专属问题解答', rewind to <section
            if end_marker in ['本篇专属问题解答', '关于本篇主题的常见问题解答', '延伸阅读与关联专题']:
                sec_idx = content.rfind('<section', start_pos, idx)
                if sec_idx != -1:
                    end_pos = sec_idx
                    break
            else:
                end_pos = idx
                break
                
    return start_pos, end_pos

success = 0
failed = []
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    s, e = find_box_bounds(c)
    if s != -1 and e != -1 and s < e:
        success += 1
    else:
        failed.append((f, s, e))

print(f'Total files: {len(files)}')
print(f'Successfully found bounds: {success}')
if failed:
    print('Failed:', failed)
