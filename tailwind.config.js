/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html', // Include all HTML files in your templates directory
    './static/js/**/*.js',   // If you have custom JavaScript files, include this
    './static/css/**/*.css', // Include your Tailwind CSS files if dynamic classes are added
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};

