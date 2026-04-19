# Structural elements [non-semantic] (Basic) (10mins)

In HTML, while many elements carry semantic meaning (e.g., `<header>`, `<article>`, `<nav>`), some elements are primarily used for structuring and styling content without adding specific meaning. Two of the most common non-semantic elements are `<div>` and `<span>`.

### `<div>` (Division Element):

1. **Description:** The `<div>` is a block-level container element. It's often used to group content or other elements together for styling (with CSS) or scripting (with JavaScript) purposes.
2. **Use Cases:**
    - Wrapping sections of a page for styling: For instance, centering a block of content or applying a background color to a specific section.
    - As a container for layout purposes: For instance, creating columns or grid layouts using CSS.
    - JavaScript interaction: It's often easier to manipulate or animate a group of elements if they're contained within a `<div>`.

### Example Code

```html
<div class="content-section">
    <h1>Title</h1>
    <p>Some text here.</p>
</div>

```

```jsx

<div class="image-gallery">
    <img src="image1.jpg" alt="Image 1">
    <p>Caption for Image 1</p>
    <img src="image2.jpg" alt="Image 2">
    <p>Caption for Image 2</p>
</div>
```

```jsx
<div id="header">
    <h1>My Website</h1>
    <p>Welcome to my website.</p>
</div>

<div id="main-content">
    <h2>About Me</h2>
    <p>I am a web developer...</p>
</div>
```

### `<span>` (Span Element):

1. **Description:** The `<span>` is an inline-level container element. It is used to target inline content or elements for styling or scripting without interrupting the flow of the content.
2. **Use Cases:**
    - Styling specific parts of text: For instance, changing the color or background of specific words within a paragraph.
    - JavaScript interaction: Such as adding tooltips to specific pieces of text.
    - Wrapping text for specific behaviors: Such as preventing line breaks in a specific span of text.
3. **Example:**
    
    ```html
    <p>This is <span class="highlighted-text">highlighted</span> text.</p>
    
    ```
    

### Key Differences:

1. **Display Value:** By default, `<div>` has a display value of `block`, which means it takes up the full width of its parent container and starts on a new line in the flow of content. `<span>`, on the other hand, has a display value of `inline`, so it does not start on a new line and only takes up as much width as necessary.
2. **Typical Use:** `<div>` is typically used for grouping larger blocks of content or elements, while `<span>` is used for smaller, inline elements or pieces of text.

### Importance of Using Them Appropriately:

While `<div>` and `<span>` are non-semantic and don't provide inherent meaning by themselves, using them judiciously is essential:

1. **Accessibility:** Over-reliance on non-semantic elements can make a webpage less accessible. Screen readers and assistive technologies rely on the semantic meaning of elements to provide a better experience. Always prefer semantic elements when possible.
2. **Maintainability:** Structured, well-organized code is easier to read, update, and maintain. Using non-semantic elements indiscriminately can result in "div soup" or "span spaghetti", making the code harder to understand.
3. **Styling & Behavior:** Both `<div>` and `<span>` are immensely useful when semantic elements don't fit the need. They offer flexibility in applying styles and behaviors where semantic tags might not be appropriate or available.

In conclusion, while `<div>` and `<span>` are non-semantic, they are invaluable tools in web design and development. It's essential to balance their use with semantic elements to create accessible, maintainable, and functional web content.

## 🔑 Student Activity

End Result: 

![Untitled](Structural%20elements%20%5Bnon-semantic%5D%20(Basic)%20(10mins%20e34b4563b16147dca35850c8f87459bf/Untitled.png)

Problem: [https://codepen.io/drupalastic/pen/VwqEqPm?editors=1000](https://codepen.io/drupalastic/pen/VwqEqPm?editors=1000)