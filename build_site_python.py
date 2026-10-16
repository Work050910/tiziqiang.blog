import os
import re
import json
import shutil

print("Starting Fast Python-powered site compiler...")

# 1. Load base template
with open('src/_includes/base.njk', 'r', encoding='utf-8') as f:
    base_template = f.read()

os.makedirs('_site', exist_ok=True)
os.makedirs('_site/css', exist_ok=True)

# Copy static assets
shutil.copy('icon.svg', '_site/icon.svg')
shutil.copy('preview-icon.png', '_site/preview-icon.png')
shutil.copy('src/css/style.css', '_site/css/style.css')

nav_tags = [
    ('/', "{% if permalink == '/' %}text-cyan-600 font-bold{% endif %}"),
    ('/good-ladder/', "{% if '/good-ladder/' in permalink %}text-cyan-600 font-bold{% endif %}"),
    ('/ladder-guide/', "{% if '/ladder-guide/' in permalink %}text-cyan-600 font-bold{% endif %}"),
    ('/ladder-tools/', "{% if '/ladder-tools/' in permalink %}text-cyan-600 font-bold{% endif %}"),
    ('/how-to-choose/', "{% if '/how-to-choose/' in permalink %}text-cyan-600 font-bold{% endif %}"),
    ('/service/', "{% if '/service/' in permalink %}text-cyan-600 font-bold{% endif %}"),
    ('/faq/', "{% if '/faq/' in permalink %}text-cyan-600 font-bold{% endif %}"),
    ('/about/', "{% if '/about/' in permalink %}text-cyan-600 font-bold{% endif %}"),
]

def wrap_in_base(body_content, title, description, permalink):
    res = base_template
    res = res.replace('{{ title }}', title)
    res = res.replace('{{ description }}', description)
    res = res.replace('{{ permalink }}', permalink)
    
    for href, tag in nav_tags:
        if (href == '/' and permalink == '/') or (href != '/' and href in permalink):
            res = res.replace(tag, 'text-cyan-600 font-bold')
        else:
            res = res.replace(tag, '')
            
    res = res.replace('{{ content | safe }}', body_content)
    return res

compiled_count = 0
sitemap_urls = []

for root, dirs, files in os.walk('src'):
    if '_data' in root or '_includes' in root or 'src/css' in root:
        continue
    for file in sorted(files):
        if not file.endswith('.njk'):
            continue
        file_path = os.path.join(root, file)
        with open(file_path, 'r', encoding='utf-8') as fp:
            raw = fp.read()
            
        if raw.startswith('---'):
            parts = raw.split('---', 2)
            if len(parts) >= 3:
                fm_text = parts[1]
                body = parts[2]
            else:
                continue
        else:
            continue
        
        title_m = re.search(r'title:\s*"([^"]+)"', fm_text)
        desc_m = re.search(r'description:\s*"([^"]+)"', fm_text)
        perm_m = re.search(r'permalink:\s*"([^"]+)"', fm_text)
        layout_m = re.search(r'layout:\s*([^\n\r]+)', fm_text)
        exclude_m = re.search(r'eleventyExcludeFromCollections:\s*true', fm_text)
        
        title = title_m.group(1) if title_m else "梯子墙"
        desc = desc_m.group(1) if desc_m else ""
        perm = perm_m.group(1) if perm_m else ""
        layout = layout_m.group(1).strip() if layout_m else ""
        
        if not perm:
            rel = os.path.relpath(file_path, 'src')
            if rel == 'index.njk':
                perm = '/'
            elif rel.endswith('/index.njk'):
                perm = '/' + rel.replace('/index.njk', '/') + '/'
            else:
                perm = '/' + rel.replace('.njk', '/') + '/'
                
        if not exclude_m:
            sitemap_urls.append(perm)
            
        if 'base.njk' in layout:
            final_content = wrap_in_base(body, title, desc, perm)
        else:
            final_content = body
            
        if perm.endswith('.xml') or perm.endswith('.txt'):
            out_file = os.path.join('_site', perm.lstrip('/'))
        elif perm.endswith('/'):
            out_file = os.path.join('_site', perm.lstrip('/'), 'index.html')
        else:
            out_file = os.path.join('_site', perm.lstrip('/') + '.html')
            
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        with open(out_file, 'w', encoding='utf-8') as out_fp:
            out_fp.write(final_content)
        compiled_count += 1
        if compiled_count % 20 == 0:
            print(f"Compiled {compiled_count} pages...", flush=True)

# Generate sitemap.xml
sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in sorted(set(sitemap_urls)):
    sitemap_xml.append(f"""  <url>
    <loc>https://tiziqiang.blog{u}</loc>
    <lastmod>2026-10-13</lastmod>
    <changefreq>weekly</changefreq>
  </url>""")
sitemap_xml.append('</urlset>')
with open('_site/sitemap.xml', 'w', encoding='utf-8') as fp:
    fp.write('\n'.join(sitemap_xml))

# Generate robots.txt
robots_txt = """User-agent: *
Allow: /

Sitemap: https://tiziqiang.blog/sitemap.xml
"""
with open('_site/robots.txt', 'w', encoding='utf-8') as fp:
    fp.write(robots_txt)

# Sync to both _site and site for full Cloudflare Pages directory compatibility
shutil.copytree('_site', 'site', dirs_exist_ok=True)

print(f"Compilation Complete! Built {compiled_count} pages and generated sitemap.xml with {len(sitemap_urls)} URLs.")
