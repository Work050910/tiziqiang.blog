const fs = require('fs');
const path = require('path');
const matter = require('gray-matter');
const nunjucks = require('nunjucks');

// Configure Nunjucks
const env = new nunjucks.Environment(new nunjucks.FileSystemLoader(['src/_includes', 'src']), {
  autoescape: false
});
env.addFilter('dump', obj => JSON.stringify(obj));

// Load data
const airports = JSON.parse(fs.readFileSync('src/_data/airports.json', 'utf8'));
const faqs = JSON.parse(fs.readFileSync('src/_data/faqs.json', 'utf8'));
let search_index = [];
if (fs.existsSync('src/_data/search_index.json')) {
  search_index = JSON.parse(fs.readFileSync('src/_data/search_index.json', 'utf8'));
}

const baseLayout = fs.readFileSync('src/_includes/base.njk', 'utf8');

function ensureDir(p) {
  if (!fs.existsSync(p)) fs.mkdirSync(p, { recursive: true });
}

ensureDir('_site');
ensureDir('_site/css');

// Copy static assets
fs.copyFileSync('icon.svg', '_site/icon.svg');
fs.copyFileSync('preview-icon.png', '_site/preview-icon.png');
fs.copyFileSync('src/css/style.css', '_site/css/style.css');

// Walk src directory
const allPages = [];
function walk(dir) {
  const files = fs.readdirSync(dir);
  for (const f of files) {
    const full = path.join(dir, f);
    if (fs.statSync(full).isDirectory()) {
      if (f !== '_includes' && f !== '_data' && f !== 'css') {
        walk(full);
      }
    } else if (f.endsWith('.njk')) {
      allPages.push(full);
    }
  }
}
walk('src');

console.log(`Found ${allPages.length} templates to build.`);

const collectionsAll = [];

// First pass: extract frontmatter for collections
for (const pagePath of allPages) {
  const raw = fs.readFileSync(pagePath, 'utf8');
  const parsed = matter(raw);
  const data = parsed.data;
  let permalink = data.permalink;
  if (!permalink) {
    const rel = path.relative('src', pagePath).replace(/\\/g, '/');
    if (rel === 'index.njk') permalink = '/';
    else if (rel.endsWith('/index.njk')) permalink = '/' + rel.replace('/index.njk', '/') + '/';
    else permalink = '/' + rel.replace('.njk', '/') + '/';
  }
  if (!data.eleventyExcludeFromCollections) {
    collectionsAll.push({
      url: permalink,
      data: data
    });
  }
}

let count = 0;
// Second pass: render pages
for (const pagePath of allPages) {
  const raw = fs.readFileSync(pagePath, 'utf8');
  const parsed = matter(raw);
  const data = parsed.data;
  const tmplContent = parsed.content;

  let permalink = data.permalink;
  if (!permalink) {
    const rel = path.relative('src', pagePath).replace(/\\/g, '/');
    if (rel === 'index.njk') permalink = '/';
    else if (rel.endsWith('/index.njk')) permalink = '/' + rel.replace('/index.njk', '/') + '/';
    else permalink = '/' + rel.replace('.njk', '/') + '/';
  }

  const context = {
    ...data,
    permalink,
    airports,
    faqs,
    search_index,
    collections: {
      all: collectionsAll
    }
  };

  // Render template body
  let renderedBody = env.renderString(tmplContent, context);

  let finalHtml = renderedBody;
  if (data.layout === 'base.njk') {
    finalHtml = env.renderString(baseLayout, {
      ...context,
      content: renderedBody
    });
  }

  // Determine output path
  let outFilePath;
  if (permalink.endsWith('.xml') || permalink.endsWith('.txt')) {
    outFilePath = path.join('_site', permalink.replace(/^\//, ''));
  } else if (permalink.endsWith('/')) {
    outFilePath = path.join('_site', permalink.replace(/^\//, ''), 'index.html');
  } else {
    outFilePath = path.join('_site', permalink.replace(/^\//, '') + '.html');
  }

  ensureDir(path.dirname(outFilePath));
  fs.writeFileSync(outFilePath, finalHtml, 'utf8');
  count++;
}

console.log(`Successfully built ${count} pages into _site/!`);
