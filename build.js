(async () => {
  try {
    const { Eleventy } = await import('@11ty/eleventy');
    let elev = new Eleventy("src", "_site");
    await elev.write();
    console.log("Eleventy build finished successfully!");
  } catch (e) {
    console.error("Build failed:", e);
  }
})();
