// .eslintrc.js
module.exports = {
  // Other ESLint configurations...
  parser: "vue-eslint-parser",
  parserOptions: {
    parser: "@typescript-eslint/parser",
  },
  plugins: ["@typescript-eslint", "vue"],

  rules: {
    "prettier/prettier": "off",
  },
};
