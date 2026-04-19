# SASS(Advanced) (40-45mins)

A preprocessor is a program or set of tools that processes the source code of a program before it is passed to the compiler. The primary purpose of a preprocessor is to perform tasks such as text replacement, file inclusion, and conditional compilation in order to prepare the code for the actual compilation process.

Sass (Syntactically Awesome Style Sheets) is a CSS preprocessor that gives your CSS superpowers.

It helps you stick to the DRY (Do Not Repeat Yourself) philosophy when writing CSS.

Sass provides a compiler that allows us to write stylesheets in two different syntaxes, indented and SCSS.

## Getting Started

1. **Install Sass:**

```jsx
npm install -g sass
```

1. **Create a Sass File:**

Save your Sass code in a file with a **`.scss`** extension. For example, you can name it **`styles.scss`**.

1. **Compile Sass to CSS (in terminal)**

```jsx
sass styles.scss styles.css
```

Once you run the above command, a CSS file will be generated called styles.css, link it to your HTML file. 

### **Indented syntax**

This is the older syntax that is indented, and gets rid of the curly braces and semi-colons. It has a file extension of `.sass`.

```sass
nav
  ul
    margin: 0
    padding: 0
    list-style: none

  li
    display: inline-block

  a
    display: block
    text-decoration: none
```

### **SCSS syntax**

This is the newer and more popular syntax. It is essentially a subset of the CSS3 syntax. This means that you can write regular CSS with some additional functionalities.

Due to its advanced features it is often termed as *Sassy CSS*. It has a file extension of `.scss`.

```scss
nav {
  ul {
    margin: 0;
    padding: 0;
    list-style: none;
  }
  li {
    display: inline-block;
  }

  a {
    display: block;
    text-decoration: none;
  }
}
```

Sass works in such a way that when you write your styles in a `.scss` file, it gets compiled into a regular CSS file. The CSS code is then loaded into the browser.

### **Variables in Sass**

You can declare variables in Sass. This is one of Sass's strengths since we can define variables for various properties and use them in any file.

The benefit here is that if that value changes, you simply need to update a single line of code.

This is done by naming a variable with a dollar symbol `$` and then referencing it elsewhere in your code.

```scss
$primary-color: #24a0ed;

.text {
  color: $primary-color;
}
button {
  color: $primary-color;
  border: 2px solid $primary-color;
}
```

## Nesting

When writing HTML you’ve probably noticed that it has a clear nested and visual hierarchy. CSS, on the other hand, doesn’t.

Sass will let you nest your CSS selectors in a way that follows the same visual hierarchy of your HTML. Be aware that overly nested rules will result in over-qualified CSS that could prove hard to maintain and is generally considered bad practice.

With that in mind, here’s an example of some typical styles for a site’s navigation:

![Untitled](SASS(Advanced)%20(40-45mins)%208b4b35d8717244e1b02cb8e4c8c73601/Untitled.png)

## Partials

You can create partial Sass files that contain little snippets of CSS that you can include in other Sass files. This is a great way to modularize your CSS and help keep things easier to maintain. A partial is a Sass file named with a leading underscore. You might name it something like `_partial.scss`. The underscore lets Sass know that the file is only a partial file and that it should not be generated into a CSS file. 

![Untitled](SASS(Advanced)%20(40-45mins)%208b4b35d8717244e1b02cb8e4c8c73601/Untitled%201.png)

In the main sheet; styles.scss we import the partials and use them.

```scss
@import "sheet1";
@import "sheet2";
@import "sheet3";
@import "buttons";
@import "form";
@import 'functions';
```

![2.png](SASS(Advanced)%20(40-45mins)%208b4b35d8717244e1b02cb8e4c8c73601/2.png)

## Mixins

Some things in CSS are a bit tedious to write, especially with CSS3 and the many vendor prefixes that exist. A mixin lets you make groups of CSS declarations that you want to reuse throughout your site. It helps keep your Sass very DRY. You can even pass in values to make your mixin more flexible. Here’s an example for `theme`.

![Untitled](SASS(Advanced)%20(40-45mins)%208b4b35d8717244e1b02cb8e4c8c73601/Untitled%202.png)

```scss
@mixin circle ($width,$height,$color,$radius) {
    width: $width;
    height: $height;
    background: $color;
    border-radius: $radius;
}
.box{
    @include circle (100px,100px,pink,50%);
}
```

## Placeholder selector & Extend

Placeholder selector defines a set of styles that can be reused in other selectors using the **`@extend`** directive. When a selector extends a placeholder selector, it inherits the styles defined within the placeholder.

```jsx
%message-shared {
  border: 1px solid #ccc;
  padding: 10px;
  color: #333;
}

.message {
  @extend %message-shared;
  background-color: #f0f0f0;
}

.another-message {
  @extend %message-shared;
  font-weight: bold;
}
```

## Difference between placeholder selector and mixin

Placeholder selectors (**`%selector`**) and mixins (**`@mixin`**) are both tools in Sass that allow you to write reusable pieces of code, but they serve different purposes and have different use cases.

  **Mixin:**

- A mixin is a reusable block of styles that can be included in other selectors using the **`@include`** directive.
- Mixins can take arguments, allowing them to generate different styles based on input.
- They are used for creating reusable sets of styles that may vary based on certain conditions.

**Placeholder Selector:**

- A placeholder selector is defined using **`%`** at the beginning of its name (e.g., **`%selector`**).
- It is a style definition that is not output to CSS unless it is extended using the **`@extend`** directive.
- **It is used for creating reusable styles that should only be included in the final CSS if explicitly extended.**

![Variables.png](SASS(Advanced)%20(40-45mins)%208b4b35d8717244e1b02cb8e4c8c73601/Variables.png)

### Functions

```scss
// _functions.scss
@function calculate-width($columns, $column-width) {
    @return $columns * $column-width;
  }

.container {
  width: calculate-width(3, 300px); 
  height: 100px;
  background-color: #069c54;
}
```

### Conditions

```scss
// Define your variables
$light-bg: #ffffff;
$dark-bg: #000000;

// Define the mixin
@mixin body-theme($theme) {
  @if $theme == "light" {
    background-color: $light-bg;
  } @else {
    background-color: $dark-bg;
  }
}

.some-other-selector {
  @include body-theme("dark");
}
```

### Loops

```scss
@for $i from 1 through 3 {
    .item-#{$i} {
      width: 100px * $i;
      height: 100px;
      border: 1px solid red;
    }
  }

<div class="item-1">Item 1</div>
  <div class="item-2">Item 2</div>
  <div class="item-3">Item 3</div>
```

```scss
$colors: "red", "green", "blue";

@each $i in $colors {
  .bg-#{$i} {
    background-color: $i;
  }
}
<div class="bg-red">Red Background</div>
  <div class="bg-green">Green Background</div>
  <div class="bg-blue">Blue Background</div>
```

```scss
$i: 1;

@while $i < 5 {
  .element-#{$i} {
    width: 50px * $i;
    border: 1px solid white;
  }
  $i: $i + 1;
}

<div class="element-1">Blue Background</div>
  <div class="element-2">Blue Background</div>
  <div class="element-3">Blue Background</div>
  <div class="element-4">Blue Background</div>
  <div class="element-5">Blue Background</div>
```

## Student activity

Create a Sass stylesheet for a navigation bar with the following specifications:

- Set the background color to a variable named **`$nav-bg-color`**.
- Set the text color to a variable named **`$nav-text-color`**.
- Nest the styling for the **`<ul>`** and **`<li>`** elements.
- Use the variables for background and text color within the nested rules.

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="styles.css"> <!-- Replace with the actual path to your Sass-compiled CSS file -->
  <title>Navigation Bar Example</title>
</head>
<body>

<nav>
  <ul>
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Services</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>

</body>
</html>
```

1. Implement a responsive layout for a webpage. Define breakpoints using variables and apply different styles for various screen sizes using media queries.

1. Create a mixin named box that takes parameters for the color and width, height. Use the mixin to apply box with different width, heights and colours to multiple elements.
2. Create a variable named color1 and give it a value orange. Use this inside your mixin.