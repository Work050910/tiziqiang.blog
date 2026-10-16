console.log("Step 1: start");
const fs = require('fs');
console.log("Step 2: fs required");
try {
  const { Eleventy } = require('@11ty/eleventy');
  console.log("Step 3: Eleventy required successfully");
} catch (e) {
  console.log("Step 3: Require failed with error:", e.message);
}
