export default function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy({ "icon.svg": "icon.svg" });
  eleventyConfig.addPassthroughCopy({ "preview-icon.png": "preview-icon.png" });
  eleventyConfig.addPassthroughCopy({ "src/css/style.css": "css/style.css" });
  
  eleventyConfig.addFilter("dump", function(obj) {
    return JSON.stringify(obj);
  });

  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      data: "_data"
    },
    templateFormats: ["njk", "md", "html"],
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk"
  };
};
