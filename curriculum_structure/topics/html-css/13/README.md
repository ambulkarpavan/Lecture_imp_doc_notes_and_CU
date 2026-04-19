# Structural elements (Basic) (15mins)

Semantic HTML elements are those that introduce meaning to web content. Unlike non-semantic elements like `<div>` and `<span>`, which don't convey specific meanings on their own, semantic elements clearly define their content for both the browser and the developer.

Using semantic elements not only makes the code more readable and maintainable but also benefits accessibility tools like screen readers and search engine optimization (SEO) efforts.

Here are some commonly used semantic HTML structural elements:

### 1. `<header>`

- **Description:** Represents a container for introductory content or navigation links. Often contains the website logo, website's title, and main navigation.
- **Example:**
    
    ```html
    <header>
      <h1>Website Name</h1>
      <nav>
        <!-- navigation links -->
      </nav>
    </header>
    
    ```
    

### 2. `<nav>`

- **Description:** Denotes a section with navigation links, either within the current document or to other documents.
- **Example:**
    
    ```html
    <nav>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
      </ul>
    </nav>
    
    ```
    

### 3. `<main>`

- **Description:** Represents the main content of a document. There should be only one `<main>` per page, and it should be unique from content that is repeated across a set of documents such as site navigation, header, or footer.
- **Example:**
    
    ```html
    <main>
      <article>
        <!-- main content -->
      </article>
    </main>
    
    ```
    

### 4. `<article>`

- **Description:** Represents self-contained content that makes sense on its own and can be independently distributed or syndicated.
- **Example:**
    
    ```html
    <article>
      <h2>Blog Post Title</h2>
      <p>Blog post content...</p>
    </article>
    
    ```
    

ChatGPT Chat: [https://chat.openai.com/share/e154d280-ce3f-48cb-9710-2689e2512af2](https://chat.openai.com/share/e154d280-ce3f-48cb-9710-2689e2512af2) 

### 5. `<section>`

- **Description:** Represents a standalone section of a document, like tabs of content or a set of content grouped under a theme.
- **Example:**
    
    ```html
    <section>
      <h2>Section Title</h2>
      <p>Section content...</p>
    </section>
    
    ```
    

### 6. `<aside>`

- **Description:** Used for content that is tangentially related to the main content and can be considered separate. Often seen as sidebars in a design.
- **Example:**
    
    ```html
    <aside>
      <h3>Related Links</h3>
      <ul>
        <!-- list of links -->
      </ul>
    </aside>
    
    ```
    

### 7. `<footer>`

- **Description:** Represents the footer of a document or a section, typically containing information about the author, copyright information, or related documents.
- **Example:**
    
    ```html
    <footer>
      <p>Copyright © 2023</p>
    </footer>
    
    ```
    

### Benefits of Using Semantic HTML:

1. **Accessibility:** Semantic elements are crucial for screen readers and other assistive technologies. They convey the structure and role of the content, helping users navigate and understand it better.
2. **SEO:** Search engines reward well-structured content, and semantic elements make it easier for search engines to identify and index the content properly.
3. **Maintainability:** Semantic elements convey meaning, making it easier for developers to understand the structure and purpose of content in a document.
4. **Styling:** CSS frameworks and browser defaults often provide styles tailored to semantic elements, giving you a head start in designing.

In conclusion, using semantic HTML elements enhances the clarity, accessibility, and discoverability of web content. Developers should aim to use these elements appropriately to create well-structured and meaningful web documents.

## 🔑 Activity - Non semantic to semantic

Problem: [https://codepen.io/drupalastic/pen/abPRPyv?editors=1000](https://codepen.io/drupalastic/pen/abPRPyv?editors=1000) 

![Untitled](Structural%20elements%20(Basic)%20(15mins)%2065ca4347daee4c929f689bcade3f234f/Untitled.png)