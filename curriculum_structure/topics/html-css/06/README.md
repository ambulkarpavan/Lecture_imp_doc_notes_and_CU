# Modern Dev Tools - Linters (Advanced) (15mins)

## Introduction to Linters for HTML & CSS

### Overview

Today, we delved into the world of linters, exploring their significance and benefits for coding, especially in HTML & CSS. This class note serves as a concise summary of our discussion and hands-on activities.

---

## 🔑  Can you find out some potential errors, inefficiencies or deviations from the following code:

### Example Code

index.html

```jsx
<html>
  <head> 
    <title>Linter Test Page</title>
  </head>
  <body>
    <div class = " container  ">

      <h1> Welcome to the Linter Test Page </h1>

      <p ID ="coding">
        This page has been intentionally designed with a few coding mistakes to
        test our linters.
      </p>

      <a class="btn">Click Me</a>

      <p id ="coding" class="error-text">This is a paragraph with a missing closing tag</p>

      <FOOTER>
          <p>&copy; 2023 Linter Test</p>
      </FOOTER>
    </div>
  </body>
</html>
```

.htmlhintrc (html hint runtime configuration)

```json
{
  "tagname-lowercase": true,
  "attr-lowercase": true,
  "attr-value-double-quotes": true,
  "doctype-first": true,
  "tag-pair": true,
  "spec-char-escape": true,
  "id-unique": true,
  "src-not-empty": true,
  "attr-no-duplication": true,
  "title-require": true,
  "html-lang-require": true,
  "tags-check": true,
  "tag-self-close": true,
  "attr-whitespace": true
}
```

[linters.zip](Modern%20Dev%20Tools%20-%20Linters%20(Advanced)%20(15mins)%20cc0f3786adc54233aa8c8ce51dad0510/linters.zip)

### 1. **What is a Linter?**

A linter is a software tool that scans code for potential errors, inefficiencies, or deviations from specified coding standards.

**Analogy**: Think of a linter as a grammar checker for your code. Just as word processing software might underline a misspelled word, linters highlight coding errors.

---

### 2. **Why Use a Linter?**

- **Catch Errors Early**: Before they lead to bigger problems when the code runs or is viewed in a browser.
- **Maintain Code Quality**: Ensures your code adheres to good practices, leading to readable and maintainable code.
- **Learn as You Code**: By pointing out mistakes and suggesting fixes, linters offer a form of real-time feedback, aiding the learning process.

---

## Linters in VSCode

VSCode, a widely-used code editor, supports integrating various linters for HTML & CSS. Linters assist developers by highlighting potential coding issues in real-time, ensuring code quality, and reinforcing best practices.

---

### 1. **HTML Linting with HTMLHint in VSCode**

### **a. What is HTMLHint?**

- HTMLHint is a linter specifically designed for HTML, offering the ability to catch common issues in HTML files.

### **b. Installation**:

1. Launch VSCode.
2. Navigate to Extensions (`Ctrl+Shift+X`).
3. Search for "HTMLHint" and click 'Install'.

### **c. Using HTMLHint**:

- Once installed, HTMLHint will automatically lint HTML files in VSCode.
- Issues will be highlighted. Hovering over the problematic code provides a tooltip with error/warning details.

### **d. Customizing HTMLHint**:

- HTMLHint's behavior can be tailored using a `.htmlhintrc` configuration file.
- Explore further configurations and rules at the [HTMLHint Rules documentation](https://htmlhint.com/docs/user-guide/list-rules).

---

### 2. **VSCode's Built-in CSS Linter**

### **a. Introduction**:

- By default, VSCode comes with a basic CSS linter that identifies common mistakes.

### **b. Using the Built-in CSS Linter**:

- When you open a CSS file, the linter is automatically active.
- It highlights code areas with potential issues. Tooltips provide error/warning explanations upon hovering.

### **c. Adjusting Linter Settings**:

1. Navigate to Settings (`Ctrl+,`).
2. Search for "CSS Lint".
3. Adjust the settings based on your preferences or project needs (e.g., disabling specific warnings).

---

### 3. **Advanced CSS Linting with Stylelint**

### **a. What is Stylelint?**

- Stylelint is a modern, powerful linter for CSS and its variants (SCSS, Less).

### **b. Installation**:

1. Ensure Stylelint is globally installed via npm: `npm install -g stylelint`.
2. In VSCode, go to Extensions and search for "Stylelint". Install the appropriate extension.

### **c. Using Stylelint**:

- Similar to HTMLHint, Stylelint activates automatically for relevant files.
- It flags code with potential issues, with error details accessible via hover tooltips.

### **d. Customizing Stylelint**:

- You can tailor Stylelint using a `.stylelintrc` configuration file.
- For beginners, starting with "stylelint-config-standard" as a base is recommended.
- Dive deeper into configurations using the [Stylelint documentation](https://stylelint.io/user-guide/configure).

---