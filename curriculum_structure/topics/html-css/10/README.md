# HTML Tags, Attributes (Advanced) (40mins)

## Working with Text

- Formatting Text: Paragraphs, Headings, Line Breaks, Horizontal Rules
- Text Formatting Tags: Mark, Cite, Dfn, Bdi, Bdo, Samp, Kbd, Var, I, B, Small, Del, Ins, Sub, Sup
- Lists: Ordered, Unordered, Definition
- Entities: line break, copyright, angle brackets, non breaking space,

| Tag | Description | Usecase |
| --- | --- | --- |
| p | Paragraph | Structure main content |
| h1-h6 | Headings (levels 1-6) | Page and section titles |
| br | Line Break | Create new lines within text |
| hr | Horizontal Rule | Separate content visually |
| mark | Highlight | Highlight parts of text |
| cite | Citation | Reference a title of a work |
| dfn | Definition | Define a term |
| bdi | Bi-directional Isolation | Text with a different direction |
| bdo | Bi-directional Override | Reverse text direction |
| samp | Sample Output | Show sample system output |
| kbd | Keyboard Input | Indicate keyboard input |
| var | Variable | Name a variable in math/programming |
| i | Italic | Emphasize text |
| b | Bold | Emphasize text strongly |
| small | Small Print | Display side comments/legalese |
| del | Deleted Text | Indicate deleted text |
| ins | Inserted Text | Indicate added text |
| sub | Subscript | Display text below the line |
| sup | Superscript | Display text above the line |
| ol | Ordered List | List items in numbered format |
| ul | Unordered List | List items in bulleted format |
| dl | Definition List | List terms with definitions |

> You do not need to remember all of these tags. You just need to know that 
- They exist
- Where to find them
- A rough idea of how to use them
> 

[https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started)  

## Mini Project

[https://codepen.io/drupalastic/full/qBLazKM](https://codepen.io/drupalastic/full/qBLazKM)

### Formatting Text:

### 1. Paragraphs (`<p>`)

- **Usage**: Represents a paragraph of text.
- **Example**: Think of `<p>` like the paragraphs in a novel. Each time a character speaks or a new idea begins, there's often a new paragraph.
    
    ```html
    <p>This is a paragraph of text.</p>
    
    ```
    

### 2. Headings (`<h1>` to `<h6>`)

- **Usage**: Represents 6 levels of headings, with `<h1>` being the highest and most important.
- **Example**: Think of headings like the titles and subtitles in a textbook. The main title (e.g., "Biology") might be an `<h1>`, while chapter titles could be `<h2>`, and sub-chapters `<h3>`.
    
    ```html
    <h1>Main Title</h1>
    <h2>Sub-title or Chapter Title</h2>
    
    ```
    
    ### Instructor’s Code
    
    <h1>This is heading 1</h1>
    <h2>This is heading 2</h2>
    <h3>This is heading 3</h3>
    <h4>This is heading 4</h4>
    <h5>This is heading 5</h5>
    <h6>This is heading 6</h6>
    
    **Codepen** :  [Example-1](https://codepen.io/drupalastic/pen/PoXGGVO?editors=1010) [Example-2](https://codepen.io/drupalastic/pen/OJrRRdz)
    

### 3. Line Breaks (`<br>`)

- **Usage**: Inserts a line break.
- **Example**: It's like pressing the "Enter" key once in a word processor.
    
    ```html
    First line.<br>Second line.
    
    <p>This is a <br> paragraph with a line break.</p>
    
    ```
    

### 4. Horizontal Rules (`<hr>`)

- **Usage**: Produces a horizontal line, often used as a thematic break.
- **Example**: In novels, when there's a scene change within a chapter, there might be a small line or decorative element. That's like `<hr>`.
    
    ```html
    <hr>
    
    ```
    

---

### Text Formatting Tags:

### 5. Mark (`<mark>`)

- **Usage**: Represents text that has been marked or highlighted.
- **Analogy**: It's like using a highlighter on a physical document.
    
    ```html
    Do <mark>not</mark> touch the wet paint.
    
    ```
    

<aside>
💡 Conceptual Aside

</aside>

## A short introduction to accessibility

Let's think about buildings in the real world. Buildings are designed for people to use, but not everyone interacts with a building the same way. Some people walk up stairs, while others might use a wheelchair and need ramps. To make sure everyone can use the building, architects add features like ramps, tactile paving, or braille on signs. This practice of designing for everyone is similar to **accessibility** in web development.

When building websites, we want everyone, including people with disabilities, to have a good experience. This might mean making sure a website works well with screen readers (tools that read web content out loud for visually impaired users) or ensuring that all functions on a website can be used with just a keyboard (for those who can't use a mouse).

For now, remember that visually reading the content of a webpage is one of the ways of consuming the content. There are many friends of us, around the world, who use different assistive technologies like “screen reader” to navigate web page.

### 6. Cite (`<cite>`)

- **Usage**: Indicates the title of a creative work (book, film, etc.).
- **Example**:
    
    ```html
    My favorite book is <cite>The Compound Effect</cite> by Darren Hardy.
    ```
    
    ```jsx
    <p>More information can be found in <cite>[ISO-0000]</cite>.</p>
    ```
    
- Documentation: [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite)
- **Description**
    
    The `<cite>` element in HTML is used to reference the **title** of a creative work. This can be a book, a play, a movie, a painting, a sculpture, a song, or any other work that has a distinct title. 
    
    Here are some things to know about the `<cite>` element:
    
    1. **Purpose**: The main purpose of the `<cite>` tag is to provide a way to indicate the source or reference for a quotation or a claim made in the content.
    2. **Display**: By default, browsers usually render `<cite>` content in italics.
    3. **Attributes**: Like many HTML tags, the `<cite>` tag can have global attributes, but it doesn't have any specific attributes of its own.
    4. **Example of usage**:
        
        ```html
        <p>In <cite>The Catcher in the Rye</cite>, J.D. Salinger explores themes of identity, isolation, and connection.</p>
        
        ```
        
    5. **Not for URLs or authors**: The `<cite>` tag should be used to reference the **title** of works, not the authors of those works or the URLs where the works might be found. If you want to link to a source, you should use the `<a>` tag. If you want to mark up the author's name, a plain `<span>` or other contextual elements like `<p>` or `<address>` might be more appropriate.
    6. **Styling and customization**: You can style the `<cite>` element with CSS just like any other HTML element. For instance, if you wanted to override the default italics:
        
        ```css
        cite {
            font-style: normal;
        }
        
        ```
        
    7. **Semantic importance**: Using semantic elements like `<cite>` in your HTML helps make your content more understandable for search engines, assistive technologies (like screen readers for the visually impaired), and other machines or tools that parse web content. This can aid in accessibility and SEO (search engine optimization).
    8. **Parent and Child elements**: The `<cite>` element can be used as a child of any element that accepts phrasing content. This includes elements like `<p>`, `<div>`, `<article>`, and many more.
    9. **Compatibility**: The `<cite>` element is widely supported in all modern web browsers.
    
    It's always a good practice to use semantic tags like `<cite>` appropriately to convey the meaning and structure of your content accurately.
    

### 7. Dfn (`<dfn>`)

- **Usage**: Represents the defining instance of a term.
- **Example**:
    
    ```html
    A <dfn>computer</dfn> is a device that can be instructed to carry out sequences of arithmetic or logical operations automatically.
    
    ```
    
- Documentation: [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dfn)
- **Description**
    
    The `<dfn>` element in HTML stands for "definition" and is used to indicate the defining instance of a term. Here are some key details about the `<dfn>` element:
    
    1. **Purpose**: The `<dfn>` tag is used to highlight the introduction or first instance of a term in a context where it will be defined.
    2. **Display**: By default, most browsers render the `<dfn>` content in italics.
    3. **Attributes**:
        - **Global Attributes**: Like most HTML elements, `<dfn>` supports global attributes.
        - **`title` Attribute**: This attribute is commonly used with `<dfn>` to provide a brief definition of the term.
    4. **Example of usage**:
        
        ```html
        <p>The <dfn title="A mythical creature often depicted as a large, scaly, fire-breathing serpent.">dragon</dfn> is a common figure in medieval folklore.</p>
        
        ```
        
    5. **Use with `<abbr>`**: If the defining instance of a term is also an abbreviation, you can nest the `<abbr>` element inside the `<dfn>` element.
        
        ```html
        <p>The <dfn title="Hypertext Markup Language"><abbr title="Hypertext Markup Language">HTML</abbr></dfn> is the standard markup language for documents designed to be displayed in a web browser.</p>
        
        ```
        
    6. **Styling and customization**: You can style the `<dfn>` element with CSS like any other HTML element. For instance, if you want to override the default italics:
        
        ```css
        dfn {
            font-style: normal;
        }
        
        ```
        
    7. **Semantic importance**: Using semantic elements like `<dfn>` helps convey the meaning and structure of your content more clearly. This can benefit search engines, assistive technologies (like screen readers for the visually impaired), and other tools that parse and interpret web content.
    8. **Parent and Child elements**: The `<dfn>` element can be used as a child of any element that accepts phrasing content, such as `<p>`, `<div>`, `<article>`, and so on.
    9. **Compatibility**: The `<dfn>` element is widely supported in all modern web browsers.
    
    Using semantic tags like `<dfn>` properly helps enrich the content by making it more understandable and accessible. Always ensure to use it for the first occurrence of a term that's being defined within your content.
    
    The `<dfn>` element, as a semantic HTML element, plays a significant role in accessibility, especially for visually impaired users who rely on screen readers to interpret and narrate web content. Here's why `<dfn>` is important in that context:
    
    1. **Contextual Interpretation**: When a screen reader encounters the `<dfn>` tag, it understands that the enclosed term has special significance as a defined term within the context. This can trigger specific behaviors, such as pausing slightly before and after the term or providing a different tone, to indicate its importance.
    2. **Link to Definitions**: The `title` attribute often used with `<dfn>` provides a concise definition. Some advanced screen readers or browsing tools can use this to offer the user a quick explanation of the term without having to search for its definition in the surrounding text. It offers an immediate context, aiding comprehension.
    3. **Navigation and Emphasis**: Some screen readers provide a feature for users to navigate specifically between certain types of semantic elements. For instance, a user might want to jump from one heading to another or from one link to another. In the same way, if a user is particularly interested in understanding new terms in a document, they might navigate between `<dfn>` elements.
    4. **Enhanced User Experience**: By marking up terms with `<dfn>`, content creators are signaling that certain words or phrases are being defined or explained in the surrounding content. This is especially helpful for visually impaired users who can't quickly scan the text visually. They can get a cue from the screen reader's interpretation that a term is of particular significance.
    5. **Interactivity and Customization**: Advanced tools or custom scripts can be developed for visually impaired users to interact more deeply with content. For instance, when a `<dfn>` tag is detected, a tool might offer the user the option to save that term and its definition for later review, aiding in learning and content retention.
    6. **Consistency Across Web**: When web developers consistently use semantic elements like `<dfn>`, it creates a more predictable web browsing experience for visually impaired users. Predictability is crucial for accessibility, as users can apply learned behaviors and expectations from one site to another.
    
    In conclusion, while the `<dfn>` tag's impact on accessibility might seem subtle, its proper use contributes to a richer, more informative, and more navigable web experience for visually impaired users. By marking up content semantically, developers make it more understandable and navigable for everyone, especially those using assistive technologies.
    

<aside>
💡 Conceptual Aside

</aside>

## A short introduction to directionality of text: `ltr` & `rtl`

Imagine you're at a bookstore, and you pick up two books: one written in English and the other in Arabic.

When you open the English book, you naturally start reading from the top-left corner and move your eyes from the left to the right side of the page, then down to the next line, and repeat. This reading direction is what we call **LTR** (Left-To-Right).

On the other hand, if you open the Arabic book, you'll notice it seems to "start" at what you'd consider the "end" of the book. And as you try to read, you move your eyes from the top-right corner of the page and go towards the left. Once you reach the end of the line, you move down to the next line on the right and repeat. This direction is known as **RTL** (Right-To-Left).

In the world of web development and HTML, we often need to display content in different languages, just like our bookstore having books from all over the world. This means our websites should be able to "understand" and "adapt" to the reading direction of the content.

**For example**, let's consider two sentences:

1. "Hello, World!" (in English)
2. "مرحبا، العالم!" (which is "Hello, World!" in Arabic)

For the English sentence, the browser would display it starting from the left side of the screen, moving to the right, because English is an LTR language.

For the Arabic sentence, the browser should ideally start displaying it from the right side, moving to the left, respecting its RTL nature.

In HTML, we can specify these directions using the `dir` attribute:

```html
<p dir="ltr">Hello, World!</p>
<p dir="rtl">مرحبا، العالم!</p>

```

By setting the `dir` attribute, we're essentially guiding the browser, much like telling someone which way to hold and read a book. The browser will then adjust the layout, text alignment, and even things like bullet points or scrollbar position to match the specified direction.

**In Summary**:

- Think of **LTR** like reading an English book: starting from the top-left and moving towards the right.
- Consider **RTL** as reading an Arabic book: beginning from the top-right and heading towards the left.
- Just like how books come in different languages and reading directions, websites do too. In HTML, we use the `dir` attribute to tell the browser which way the "book" (or content) should be read.

## Introduction to HTML Attributes

Imagine you're celebrating the New Year and decide to send greeting cards to your friends. You buy 10 identical New Year cards to send to 10 different friends. Now, while the cards are the same, you know that you'd want to add a personal touch to each - writing their name, perhaps a custom message, or even sealing it with their favorite color.

This act of buying generic cards and then personalizing them is quite similar to how HTML tags and attributes work. The card itself represents a generic HTML tag, and the personal touches you add act as the attributes.

### Concrete Example:

**New Year Card (HTML Element)**: A beautifully designed card with a printed message, "Wishing you a Happy New Year!"

**Personal Touches (Attributes)**:

- **Friend's Name**: "John"
- **Custom Message**: "May this year bring you closer to all your dreams."
- **Sealing Sticker Color**: Blue

Transitioning this scenario into the world of web pages:

**HTML Element**: A paragraph that says "Hello, World!"

This is akin to our generic New Year card.

**Attributes**:

- **Direction to read**: Left-to-right for English or right-to-left for Arabic.

In HTML, this might be represented as:

For English:

```html
<p dir="ltr">Hello, World!</p>

```

For Arabic:

```html
<p dir="rtl">مرحبا، العالم!</p>

```

Here:

- The `<p>` tag is our New Year card, the main greeting.
- The `dir` attribute, whether it's `ltr` or `rtl`, is akin to adding a friend's name or a custom message to personalize the card. It provides additional context to the primary message, ensuring it's presented correctly and understood as intended.

In HTML, just as in life, while you may start with something generic, it's the personal touches (or attributes) that provide specificity, meaning, and clarity. Just as you'd customize a New Year card for each friend, in web design, attributes help customize and fine-tune generic HTML tags to fit the intended purpose.

… continuing with text related HTML tags

### 8. Bdi (`<bdi>`)

- **Usage**: Isolates a span of text that might be formatted in a different direction from other text outside it.
- **Example**: Useful for user-generated content where the text direction isn't known in advance.
    
    ```html
    User: <bdi>نص</bdi> has logged in.
    
    ```
    
- **Documentation**: [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdi)
- Description
    
    The `<bdi>` element in HTML stands for "Bi-Directional Isolation." It's a rather specialized element introduced in HTML5 to address the challenges of displaying bi-directional text, particularly when the direction is unknown or might change. Here's more information about the `<bdi>` element:
    
    1. **Purpose**: The main purpose of the `<bdi>` tag is to allow a piece of text to be isolated from its surrounding text, ensuring it's displayed in its intended direction even if it's different from the rest of the content. This is especially useful for user-generated content where the text direction isn't known in advance.
    2. **Usage Scenario**: Consider social media posts, comments, or usernames where users from different language backgrounds contribute content. Without `<bdi>`, a username in Arabic or Hebrew (which are right-to-left languages) might distort the layout of English content (which is left-to-right) or vice versa.
    3. **Attributes**:
        - **Global Attributes**: The `<bdi>` element supports all global attributes in HTML.
        - **`dir` Attribute**: While the `<bdi>` element isolates text directionally, you can still explicitly set the direction using the `dir` attribute if needed (e.g., `dir="rtl"` for right-to-left).
    4. **Example of usage**:
        
        Let's say you have a UI that displays usernames followed by the number of posts they've made:
        
        ```html
        <ul>
            <li><bdi>usernameInArabic</bdi>: 10 posts</li>
            <li><bdi>usernameInEnglish</bdi>: 5 posts</li>
        </ul>
        
        ```
        
        Without the `<bdi>` tag, the colon and number might be incorrectly placed for the Arabic username due to its right-to-left nature.
        
    5. **Styling and Customization**: The `<bdi>` element can be styled with CSS just like any other HTML element. However, its primary function is structural rather than presentational.
    6. **Semantic Importance**: While the `<bdi>` element's primary role is to handle the display of bi-directional content, it also imparts semantic meaning. It tells both browsers and developers that the enclosed text might have a direction different from its surrounding content.
    7. **Compatibility**: Modern browsers generally support the `<bdi>` element, but it's always good to test and ensure it functions as expected in your target browsers, especially if they're older versions.
    
    The introduction of the `<bdi>` tag was a response to the increasingly global nature of the internet, ensuring content from various languages and scripts can coexist harmoniously in the same context. It's a testament to the evolving nature of the web and the commitment to making it more inclusive and accessible for all users.
    

### 9. Bdo (`<bdo>`)

- **Usage**: Overrides the current text direction.
- **Example**:
    
    ```html
    This is a <bdo dir="rtl">reversed</bdo> text.
    ```
    
- **Documentation:** [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdo)
- Description
    
    The `<bdo>` element in HTML stands for "Bi-Directional Override." It's used to override the current directionality of text. Here's what you need to know about the `<bdo>` element:
    
    1. **Purpose**: The `<bdo>` tag allows developers to override the natural text direction, which is usually determined by the Unicode character properties of the text. It can force text to be rendered either left-to-right (LTR) or right-to-left (RTL), regardless of its normal directionality.
    2. **Attributes**:
        - **`dir` Attribute (Mandatory)**: The `<bdo>` element requires the `dir` attribute to specify the text direction. The possible values for this attribute are "ltr" for left-to-right and "rtl" for right-to-left.
        - **Global Attributes**: The `<bdo>` element also supports all global attributes in HTML.
    3. **Usage Scenario**: The `<bdo>` element can be handy when trying to display characters in a way that's against their natural or default directionality. For instance, if you have an Arabic word (which is inherently RTL) that you want to display in an LTR context for artistic or specific layout purposes.
    4. **Example of usage**:
        
        ```html
        <p>This is a normal LTR paragraph. But <bdo dir="rtl">This part is reversed</bdo> just for effect.</p>
        
        ```
        
        In this example, the text "This part is reversed" would be displayed from right to left, even though the rest of the sentence is left to right.
        
    5. **Difference from `<bdi>`**: While both `<bdo>` and `<bdi>` are related to bi-directional text, they serve different purposes. The `<bdi>` element isolates text, ensuring it takes on its inherent directionality without affecting surrounding content. The `<bdo>` element, on the other hand, overrides the natural directionality, forcing text to be displayed in the specified direction.
    6. **Styling and Customization**: The `<bdo>` element can be styled with CSS like any other HTML element, but its primary function is structural, affecting the layout and presentation of the content.
    7. **Semantic Importance**: The `<bdo>` element carries semantic information about the direction in which the text should be interpreted and displayed. It can be especially useful for assistive technologies, like screen readers, to understand and communicate the text's flow.
    8. **Compatibility**: The `<bdo>` element is supported in most modern browsers. However, as with all HTML elements, it's a good practice to test its rendering in your target browsers.
    
    In conclusion, while the `<bdo>` element might not be commonly used in everyday web development, it's an essential tool in the toolkit for web developers working with multi-lingual and global platforms, ensuring content can be presented precisely as intended.
    

### 10. Samp (`<samp>`)

- **Usage**: Displays sample output from a program or system.
- **Example**:
    
    ```html
    When you run the command, you should see: <samp>Execution successful</samp>.
    
    ```
    
- **Documentation**: [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/samp)
- Description:
    
    ### `<samp>`: The Sample Output Element
    
    The `<samp>` tag in HTML is used to represent sample output from computer programs. If you're writing a document or a tutorial that describes computer programming or command-line sequences, and you want to show the user what the output might look like, you'd use the `<samp>` element.
    
    ### Why Use It?
    
    In online documentation, articles, or tutorials that cover programming, scripting, or command-line tasks, it's essential to differentiate between the code, input, and output. By doing so, it helps the reader easily distinguish between what they're supposed to type or code versus what they can expect the system to return as a result.
    
    ### Basic Usage:
    
    Let's say you're writing a tutorial on how to use a command-line tool, and you want to showcase what the output might look like after a certain command is run. Here's an example:
    
    ```html
    <p>When you type the command <code>echo "Hello, World!"</code>, you should see:</p>
    <samp>Hello, World!</samp>
    
    ```
    
    In this example:
    
    - The `<code>` tag is used to represent a piece of computer code (`echo "Hello, World!"`).
    - The `<samp>` tag is then used to display the expected sample output from running that command (`Hello, World!`).
    
    ### Appearance:
    
    By default, how the `<samp>` tag displays in browsers can vary, but it's often rendered in a monospace font, which aligns with the typographical conventions of computer code and output. However, like all HTML elements, its appearance can be customized using CSS.
    
    ### In Summary:
    
    The `<samp>` tag in HTML provides a semantic way to represent sample outputs from computer programs or commands. By using it, content creators can offer clearer, more easily understandable tutorials and documentation for those learning or using programming and command-line tools.
    

### 11. Kbd (`<kbd>`)

- **Usage**: Represents user input (usually keyboard input).
- **Example**:
    
    ```html
    Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy.
    
    ```
    
- **Documentation**: [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd)
- Description
    
    ### `<kbd>`: The Keyboard Input Element
    
    The `<kbd>` tag in HTML is used to represent user input, usually from a keyboard, but it can also denote input from other devices if contextually appropriate. In documentation or web content that instructs users on what to type or which keys to press, the `<kbd>` element comes in handy.
    
    ### Why Use It?
    
    It's essential to clearly distinguish between regular text and specific keys or input sequences when you're guiding someone on what they should type or press. By using the `<kbd>` tag, you can provide clarity and enhance readability.
    
    ### Basic Usage:
    
    Let's say you're writing a guide on keyboard shortcuts. You might want to inform users about how to save a file using a keyboard combination:
    
    ```html
    <p>To save a file, press <kbd>Ctrl</kbd> + <kbd>S</kbd>.</p>
    
    ```
    
    In this example:
    
    - The `<kbd>` tag is used to represent each key in the shortcut combination (`Ctrl` and `S`).
    
    ### Appearance:
    
    By default, the `<kbd>` tag is often rendered in browsers as inline text within a border, usually appearing like a button or key on a keyboard. This visual representation reinforces its purpose — to signify keyboard or user input. However, this appearance can vary based on the browser and can be customized further using CSS.
    
    ### Nested Usage:
    
    Sometimes, for enhanced clarity, you'll see the `<kbd>` element nested. This can be particularly useful for multi-key sequences. For instance:
    
    ```html
    <p>To force a hard refresh, press <kbd><kbd>Ctrl</kbd> + <kbd>F5</kbd></kbd>.</p>
    
    ```
    
    Here, the outer `<kbd>` tags signify the entire key sequence, while the inner ones denote each specific key.
    
    ### In Summary:
    
    The `<kbd>` tag in HTML is a semantic way to denote keyboard keys or user input. It's especially useful in documentation, tutorials, or any content that guides users on interacting with software or devices through specific key presses or input. By using `<kbd>`, you ensure that such instructions are easily distinguishable from the surrounding text.
    

### 12. Var (`<var>`)

- **Usage**: Represents the name of a variable in programming or math.
- **Example**:
    
    ```html
    Solve for <var>x</var> in the equation.
    
    ```
    
- **Documentation**: [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/var)
- Description
    
    ### `<var>`: The Variable Element
    
    The `<var>` tag in HTML is used to represent the name of a variable in a mathematical expression or programming context. It's a way to semantically differentiate variable names or symbols from surrounding text, making them easily identifiable.
    
    ### Why Use It?
    
    When writing mathematical, scientific, or programming content, it's important to ensure that symbols or variable names stand out and are immediately recognizable as such. The `<var>` element serves this purpose by offering a semantic way to present these variables.
    
    ### Basic Usage:
    
    Let's say you're explaining a simple mathematical formula, or you're outlining a programming concept. Here's how you might use the `<var>` tag:
    
    1. **Mathematical Context**:
        
        ```html
        <p>Given the formula: <var>a</var>² + <var>b</var>² = <var>c</var>²</p>
        
        ```
        
        In this example, the names of the variables \(a\), \(b\), and \(c\) are enclosed in `<var>` tags.
        
    2. **Programming Context**:
        
        ```html
        <p>Let's declare a variable named <var>x</var> to store the user's age.</p>
        
        ```
        
        Here, the variable name `x` is wrapped in a `<var>` tag to differentiate it from the regular text.
        
    
    ### Appearance:
    
    By default, browsers usually render the `<var>` element in an italic font, emphasizing that it represents a variable name. This style can be altered with CSS, but the italic representation is a widely accepted convention for variables, especially in mathematical content.
    
    ### In Summary:
    
    The `<var>` tag in HTML offers a semantic way to represent variable names in both mathematical and programming contexts. By using it, content creators can ensure that variables are visually distinguishable from the surrounding text, thereby improving readability and clarity for readers or learners. Whether it's in academic articles, online lessons, or programming guides, `<var>` plays a crucial role in presenting variable names clearly and effectively.
    

### 13. I (`<i>`) and B (`<b>`)

- **Usage**: Represents text in italics (`<i>`) or bold (`<b>`). However, use with caution as `<strong>` and `<em>` are preferred for semantic emphasis.
- **Example**:
    
    ```html
    This is <i>italic</i> and this is <b>bold</b>.
    
    ```
    

Why you should not be using these two tags? Watch the video!

### 14. Small (`<small>`)

- **Usage**: Decreases the text size, often used for disclaimers or side notes.
- **Example**:
    
    ```html
    This is a statement. <small>*Terms and conditions apply.</small>
    
    ```
    
- Description
    
    Let's discuss the `<small>` element in HTML.
    
    ### `<small>`: The Small Text Element
    
    The `<small>` tag in HTML is used to display text in a smaller font size, indicating side comments, disclaimers, copyright information, or other fine print. It serves as a way to semantically and visually de-emphasize certain text relative to the main content.
    
    ### Why Use It?
    
    The main goal of using the `<small>` element is to differentiate particular portions of text that are less crucial or that act as supplementary information. By reducing the font size, it visually alerts readers that the information is secondary or less important compared to the main content.
    
    ### Basic Usage:
    
    1. **Disclaimer**:
        
        ```html
        <p>Buy one, get one free! <small>Offer valid until stock lasts. Terms and conditions apply.</small></p>
        
        ```
        
        In this example, the main message is about the promotion, but the `<small>` tag wraps around the terms and conditions, indicating they're supplemental details.
        
    2. **Copyright Notice**:
        
        ```html
        <footer>
            <p><small>© 2023 MyWebsite. All rights reserved.</small></p>
        </footer>
        
        ```
        
        Here, the `<small>` tag is used for a copyright notice, commonly found in website footers.
        
    
    ### Appearance:
    
    By default, text within a `<small>` element appears slightly smaller than the surrounding text. This size reduction helps in setting apart the content it wraps. However, the exact presentation can vary between browsers and can be further customized using CSS if desired.
    
    ### In Summary:
    
    The `<small>` tag in HTML serves a specific purpose: to de-emphasize or denote secondary information within a page. It's especially useful in scenarios where certain details need to be present but should not distract from the main content. By using `<small>`, web designers and content creators can ensure that such information is presented in a manner that's appropriately subtle yet still accessible to readers who seek it out.
    

### 15. Del (`<del>`) and Ins (`<ins>`)

- **Usage**: Represents deleted text (`<del>`) and inserted text (`<ins>`).
- **Example**:
    
    ```html
    Buy one get one <del>50%</del> <ins>free</ins>!
    
    ```
    
- Description
    
    Let's delve into the `<del>` and `<ins>` elements in HTML.
    
    ### `<del>`: The Deleted Text Element
    
    The `<del>` tag in HTML is used to represent text that has been deleted or removed from a document. It provides a way to visually indicate changes or edits made to content, typically by striking through the deleted text.
    
    ### `<ins>`: The Inserted Text Element
    
    The `<ins>` tag represents text that has been added or inserted into a document. It's the counterpart to the `<del>` tag, and the usual visual indication for inserted text is to underline it.
    
    ### Why Use Them?
    
    These tags are especially valuable in situations where you want to visually present the modifications made to content, like in version-controlled documents, editorial corrections, or any context where tracking changes is essential.
    
    ### Basic Usage:
    
    Imagine an article where a correction was made:
    
    Original text: "The event will take place on Tuesday."
    Revised text: "The event will take place on Wednesday."
    
    This correction could be represented in HTML as:
    
    ```html
    The event will take place on <del>Tuesday</del> <ins>Wednesday</ins>.
    ```
    
    In this representation:
    
    - The `<del>` tag surrounds "Tuesday" to indicate that it's the old or deleted information.
    - The `<ins>` tag wraps "Wednesday" to show it's the new or inserted information.
    
    ### Additional Attributes:
    
    Both the `<del>` and `<ins>` tags can be combined with the `datetime` attribute, which indicates when the change was made.
    
    Example:
    
    ```html
    <del datetime="2023-08-31">Tuesday</del> <ins datetime="2023-09-01">Wednesday</ins>
    ```
    
    ### Appearance:
    
    - By default, browsers usually render text within a `<del>` element as struck through.
    - Text within an `<ins>` element is typically rendered as underlined.
    
    However, these visual styles can be customized using CSS.
    
    ### In Summary:
    
    The `<del>` and `<ins>` tags in HTML provide a semantic way to represent changes in content. They offer clear visual cues to indicate what has been removed and what has been added. Especially valuable in editorial, legal, and version-controlled contexts, these tags ensure that modifications are transparent and easily traceable.
    

### 16. Sub (`<sub>`) and Sup (`<sup>`)

- **Usage**: Represents subscript (`<sub>`) and superscript (`<sup>`).
- **Example**:
    
    ```html
    The formula for water is H<sub>2</sub>O. E = mc<sup>2</sup>.
    
    ```
    
- Description
    
    Let's explore the `<sub>` and `<sup>` elements in HTML.
    
    ### `<sub>`: The Subscript Text Element
    
    The `<sub>` tag in HTML is used to represent subscript text. Subscript text appears slightly below the baseline of the normal text and is often used in scientific contexts to denote formulas or specific notations.
    
    ### `<sup>`: The Superscript Text Element
    
    The `<sup>` tag is used to represent superscript text. Superscript text appears slightly above the baseline of the normal text. It's frequently used to denote footnotes, mathematical exponents, or other specific notations.
    
    ### Why Use Them?
    
    Both subscript and superscript are essential for a variety of textual contexts, especially:
    
    1. **Mathematical and Scientific Notations**: To accurately represent formulas, chemical compounds, or mathematical exponents.
    2. **References and Footnotes**: To link a particular segment of text to a corresponding note or citation.
    
    ### Basic Usage:
    
    1. **Chemical Formula**:
        
        ```html
        <p>The chemical formula for water is H<sub>2</sub>O.</p>
        
        ```
        
        Here, the `<sub>` tag is used to correctly denote the subscript "2" in the water molecule notation.
        
    2. **Mathematical Exponentiation**:
        
        ```html
        <p>The square of 5 is represented as 5<sup>2</sup>.</p>
        
        ```
        
        In this instance, the `<sup>` tag is used to represent the squared exponent.
        
    3. **Footnote Reference**:
        
        ```html
        <p>This is a statement<sup>1</sup>.</p>
        <footer>
            <p><sup>1</sup> This is the corresponding footnote explaining the statement.</p>
        </footer>
        
        ```
        
        Here, the `<sup>` tag is used to link the statement to its corresponding footnote.
        
    
    ### Appearance:
    
    - Text within a `<sub>` element appears slightly lower than the baseline of the main text.
    - Text within a `<sup>` element appears slightly higher than the baseline.
    
    The exact positioning and size can vary slightly between browsers, but the relative positioning (higher for superscript and lower for subscript) remains consistent. If necessary, these default styles can be adjusted using CSS.
    
    ### In Summary:
    
    The `<sub>` and `<sup>` tags in HTML offer a semantic way to represent subscript and superscript text, respectively. They ensure that certain notations, references, and special characters are displayed accurately and meaningfully in various contexts, contributing to clear communication and correct representation of information.
    

## 🔑 Student Activity - working with simple text tags

![Untitled](HTML%20Tags,%20Attributes%20(Advanced)%20(40mins)%203c486c987aa04e79a786a659a3405ecd/Untitled.png)

Problem: [https://codepen.io/drupalastic/pen/abPROPK?editors=1000](https://codepen.io/drupalastic/pen/abPROPK?editors=1000) 

Solution: [https://codepen.io/drupalastic/pen/WNLavYG?editors=1000](https://codepen.io/drupalastic/pen/WNLavYG?editors=1000) 

## Working with lists

### 1. Ordered List (`<ol>`)

- **Usage**: Represents a list of items in which order does matter.
- **Example**:
    
    ```html
    <ol>
      <li>Wake up</li>
      <li>Brush teeth</li>
      <li>Have breakfast</li>
    </ol>
    
    ```
    
- Description
    
    Let's delve into the `<ol>` element in HTML.
    
    ### `<ol>`: The Ordered List Element
    
    The `<ol>` tag in HTML stands for "ordered list." As the name suggests, it is used to represent a list of items in a specific order. Each item in the list is wrapped with a `<li>` (list item) tag. The items in an ordered list are usually displayed with a number or letter preceding them, indicating their sequence.
    
    ### Why Use It?
    
    An ordered list is essential in situations where the sequence of the items matters, unlike an unordered list (`<ul>`), where the sequence is irrelevant. You'd typically use `<ol>` in contexts like step-by-step instructions, rankings, or any other scenario where the order is crucial.
    
    ### Real Example: Baking a Cake
    
    Let's say you're writing a recipe for baking a chocolate cake, and you want to provide step-by-step instructions. The order of the steps is critical; otherwise, you might end up with a culinary disaster!
    
    ```html
    <ol>
        <li>Preheat your oven to 350°F (175°C).</li>
        <li>In a large bowl, mix flour, cocoa powder, baking powder, and salt.</li>
        <li>In another bowl, beat together butter and sugar until light and fluffy.</li>
        <li>Add eggs one by one to the butter and sugar mixture, beating well after each addition.</li>
        <li>Gradually blend in the dry ingredients until fully combined.</li>
        <li>Pour the batter into a greased baking pan.</li>
        <li>Bake for 30-35 minutes or until a toothpick inserted into the center comes out clean.</li>
        <li>Allow the cake to cool in the pan for 10 minutes, then transfer to a wire rack to cool completely.</li>
    </ol>
    
    ```
    
    In this recipe, the order of the instructions is essential. For instance, you can't start by adding eggs if you haven't first combined your dry ingredients. The `<ol>` element ensures readers understand the sequence and follow the steps correctly.
    
    ### Additional Attributes:
    
    The `<ol>` tag can also use several attributes to adjust the type of markers or start the list from a different number:
    
    - `type`: Specifies the type of marker (like "1", "A", "a", "I", "i").
    - `start`: Specifies the starting number for the list.
    
    For instance, if you wanted your list to start from step 3 using Roman numerals:
    
    ```html
    <ol type="I" start="3">
        <li>Third step</li>
        <li>Fourth step</li>
    </ol>
    
    ```
    
    ### In Summary:
    
    The `<ol>` tag in HTML is a vital tool when representing ordered sequences or steps. Its primary function is to communicate the importance of order in the given context, ensuring that the audience understands the sequence in which the actions or items should be acknowledged or executed. Whether it's in recipes, instructional manuals, or rankings, `<ol>` plays a crucial role in presenting information clearly and effectively.
    

### 2. Unordered List (`<ul>`)

- **Usage**: Represents a list of items in which order doesn't matter.
- **Example**:
    
    ```html
    <ul>
      <li>Milk</li>
      <li>Eggs</li>
      <li>Bread</li>
    </ul>
    
    ```
    
- Description
    
    Let's explore the `<ul>` element in HTML.
    
    ### `<ul>`: The Unordered List Element
    
    The `<ul>` tag in HTML stands for "unordered list." It is used to represent a list of items where the order is not essential. Each item within the list is enclosed with a `<li>` (list item) tag. Typically, items in an unordered list are displayed with bullet points to indicate individual list entries.
    
    ### Why Use It?
    
    You would use the `<ul>` element in situations where you want to list items, but their sequence isn't crucial. Unlike the ordered list (`<ol>`), where the order matters, the `<ul>` is perfect for displaying collections of items without implying any particular sequence or hierarchy.
    
    ### Real Example: Grocery Shopping List
    
    Imagine you're jotting down a quick grocery shopping list. For most people, the order in which the items are written doesn't necessarily dictate the order in which they must be picked up. Here's how such a list might look in HTML:
    
    ```html
    <ul>
        <li>Milk</li>
        <li>Bread</li>
        <li>Eggs</li>
        <li>Tomatoes</li>
        <li>Orange juice</li>
    </ul>
    
    ```
    
    In this grocery list, it doesn't matter if you pick up eggs before bread or tomatoes before milk. The main point is to remember to buy all these items. The `<ul>` element is perfect for representing such lists.
    
    ### Appearance:
    
    By default:
    
    - The `<ul>` element displays its items with bullet points in most web browsers.
    - Items are usually presented with a vertical stack layout, with each item appearing below the previous one.
    
    However, the default appearance of the `<ul>` can be customized using CSS, allowing you to change the bullet point style, layout, and other visual properties.
    
    ### Nested Lists:
    
    Unordered lists can be nested within each other to represent sub-items or sub-categories. Here's an example of a nested list, perhaps for categorizing groceries:
    
    ```html
    <ul>
        <li>Dairy
            <ul>
                <li>Milk</li>
                <li>Butter</li>
            </ul>
        </li>
        <li>Bakery
            <ul>
                <li>Bread</li>
                <li>Pastries</li>
            </ul>
        </li>
    </ul>
    
    ```
    
    In this nested list, "Dairy" and "Bakery" are top-level items, and beneath each, we have a sub-list specifying related grocery items.
    
    ### In Summary:
    
    The `<ul>` tag in HTML is invaluable when you need to represent a collection of items without a specific order. Be it a simple list of tasks, categories on a website, or features of a product, the unordered list provides a structured yet flexible way to display information. It's a staple in web content creation, ensuring that various types of lists are presented clearly and effectively to users.
    

### 3. Definition List (`<dl>`)

- **Usage**: Represents a list of terms followed by one or more descriptions.
- **Example**:
    
    ```html
    <dl>
      <dt>HTML</dt>
      <dd>HyperText Markup Language</dd>
      <dt>CSS</dt>
      <dd>Cascading Style Sheets</dd>
    </dl>
    
    ```
    
- Description
    
    Of course! Let's explore the `<dl>` element in HTML.
    
    ### `<dl>`: The Description List Element
    
    The `<dl>` tag stands for "description list" in HTML. A description list is a collection of terms and their corresponding descriptions. The `<dl>` element is typically used alongside two other elements:
    
    - `<dt>`: Stands for "description term." This is the term or name being defined.
    - `<dd>`: Represents "description definition." It provides the definition, description, or value for the term specified by the preceding `<dt>`.
    
    ### Why Use It?
    
    A description list is useful in contexts where you want to pair items with their definitions or descriptions. It's a semantic way to connect related pieces of information, like terms and definitions, metadata fields and values, or any set of paired items.
    
    ### Real Example: A Glossary of Terms
    
    Imagine you're creating a glossary section on a website to define technical terms:
    
    ```html
    <dl>
        <dt>HTML</dt>
        <dd>HyperText Markup Language: The standard markup language for creating web pages.</dd>
    
        <dt>URL</dt>
        <dd>Uniform Resource Locator: A reference or address used to access resources on the Internet.</dd>
    
        <dt>HTTP</dt>
        <dd>HyperText Transfer Protocol: The foundation of data communication for the World Wide Web.</dd>
    </dl>
    
    ```
    
    In this glossary:
    
    - Each term (`<dt>`) is followed by its definition (`<dd>`).
    - The `<dl>` element wraps the entire list, providing context.
    
    ### More Complex Usage: Multiple Descriptions
    
    A single term might have multiple descriptions or definitions:
    
    ```html
    <dl>
        <dt>Browser</dt>
        <dd>A software application used to access and view websites.</dd>
        <dd>A person who looks over or glances through something without a methodical examination.</dd>
    </dl>
    
    ```
    
    ### Appearance:
    
    By default:
    
    - The `<dt>` (term) is bold and placed on its line.
    - The `<dd>` (definition) is placed on the next line, usually with a margin or indentation to set it apart from the term.
    
    Again, as with other HTML elements, these default appearances can be customized with CSS.
    
    ### Other Common Use Cases:
    
    1. **Metadata Presentation**: If you're displaying metadata (like for an image or document), you might use a `<dl>` to pair metadata fields with their values.
    2. **Question and Answer Format**: For FAQ sections, where a question can be considered a term and its answer a description.
    
    ### In Summary:
    
    The `<dl>` element provides a semantic way to create lists of paired terms and definitions in HTML. Its flexibility means it can be used in a variety of contexts beyond just traditional glossaries, such as FAQs or metadata displays. In content that requires clear associations between related items, the description list is an invaluable tool.
    

## Working with links

In the vast world of the internet, imagine every website as an island. These islands are unique, rich with content, and offer different experiences. But what if these islands were isolated? How would you travel between them? This is where the HTML `<a>` tag, commonly known as the anchor element, comes into play. Think of it as the bridge that connects these islands.

### 1. Basics of the Anchor Element:

The `<a>` tag is used to create links, allowing users to navigate from one page to another, be it within the same website or to a completely different one.

```html
<a href="<https://www.example.com/>">Visit Example</a>

```

In this, "Visit Example" is the visible text and the `href` attribute is the destination address, much like a bridge's starting point and its destination.

### 2. Understanding URLs:

**a) Absolute URL**:
It's a full web address. If you think of it as an address, it's similar to giving someone your full home address including your city, state, and country.

```html
<a href="<https://www.example.com/gallery>">Go to Gallery</a>

```

**b) Relative URLs**:
These are partial addresses that are relative to the current page. Imagine giving someone directions to your kitchen, while they're already in your living room.

- **Folder Down** (Navigating deeper into the site's structure):
    
    ```html
    <a href="images/pic.jpg">See the picture</a>
    
    ```
    
- **Folder Up** (Going back in the site's structure):
    
    ```html
    <a href="../about.html">About Us</a>
    
    ```
    

### 3. More Than Just Web Pages:

Links can point to various resources:

- Images: `<a href="images/sunset.jpg">View Sunset Image</a>`
- PDFs: `<a href="files/report.pdf">Download Report</a>`

You can even prompt a user to download a resource directly:

```html
<a href="images/sunset.jpg" download>Click to download the sunset image</a>

```

### 4. Navigating Within a Page:

**a) Fragments**: Let's say a webpage is a multi-story building. If you want to guide someone to a specific floor or room, you'd use fragments.

```html
<h2 id="summary">Summary</h2>
...
<a href="#summary">Jump to Summary</a>

```

**b) Jump to Top Link**: If you're at the base of this building and want a quick elevator to the top, you'd use:

```html
<a href="#">Back to Top</a>

```

### 5. Difference Between Link and Hyperlink:

All hyperlinks are links, but not all links are hyperlinks. Confused? Think of fruits. All apples are fruits, but not all fruits are apples.

A "link" is a more general term that can refer to anything that connects two things. In the web context, it often means a URL or an address. A "hyperlink," on the other hand, is interactive and clickable, usually taking you from one web page to another. In HTML, hyperlinks are created using the `<a>` tag.

### 6. Extra Tips for Enhancing User Experience:

- **Opening Links in a New Tab**: To let users keep your page open while visiting another site:
    
    ```html
    <a href="<https://www.example.com/>" target="_blank">Open Example in a new tab</a>
    
    ```
    
- **Mailto Links**: Want your users to send you an email directly by clicking a link? Here you go:
    
    ```html
    <a href="mailto:example@example.com">Send us an email</a>
    
    ```
    
- **Title Attribute**: Provide a brief tooltip description when hovering over the link:
    
    ```html
    <a href="<https://www.example.com/>" title="Go to Example's homepage">Example</a>
    
    ```
    

## The `target` attribute

The `target` attribute of the `<a>` (anchor) tag in HTML specifies where a new page will be displayed when the link is clicked. This is especially important when you're working with hyperlinks that lead to external websites, documents, or when working with frames and iframes.

Here are the possible values for the `target` attribute:

1. **`_blank`**: Opens the linked document in a new window or tab. This is commonly used for external links to ensure that the user doesn't navigate away from the current page.
    
    ```html
    <a href="<https://www.example.com>" target="_blank">Visit Example</a>
    
    ```
    
2. **`_self`**: Opens the linked document in the same frame or window. This is the default behavior if no target attribute is specified.
    
    ```html
    <a href="page2.html" target="_self">Go to Page 2</a>
    
    ```
    
3. **`_parent`**: Opens the linked document in the parent frame (used in the context of frames or iframes). If there's no parent frame, this behaves the same as `_self`.
    
    ```html
    <a href="page3.html" target="_parent">Go to Page 3 in parent frame</a>
    
    ```
    
4. **`_top`**: Opens the linked document in the full body of the current window, essentially breaking out of any frame. This can be handy if your site is being embedded elsewhere and you want a link to break out of the embed.
    
    ```html
    <a href="page4.html" target="_top">Go to Page 4, breaking out of any frames</a>
    
    ```
    
5. **framename**: If you're using frames (which are less common in modern web design), you can also specify the name of the frame you want the link to open in. This requires the target frame to have a `name` attribute set.
    
    ```html
    <!-- Frame Definition -->
    <frameset cols="50%,50%">
        <frame src="page1.html" name="leftFrame">
        <frame src="page2.html" name="rightFrame">
    </frameset>
    
    <!-- Inside page1.html -->
    <a href="page3.html" target="rightFrame">Load Page 3 in the right frame</a>
    
    ```
    

**Important Note**: Using `target="_blank"` without additional security precautions can expose your site to vulnerabilities (like reverse tabnabbing). To mitigate this, it's good practice to add the `rel="noopener noreferrer"` attribute to such links:

```html
<a href="<https://www.example.com>" target="_blank" rel="noopener noreferrer">Visit Example</a>

```

This ensures that the new page cannot access your page via the `window.opener` object, potentially protecting your users from phishing attacks.

## Example Code

1. **Home Page**: Introduction and links to other pages.
2. **Books Page**: Displaying a list of books.
3. **Contact Page**: A page with contact information

### **1. Home Page (`index.html`)**:

```html
<html>
  <head>
    <title>Bookstore Home</title>
  </head>
  <body>
    <h1>Welcome to Our Online Bookstore</h1>

    <ul>
      <li><a href="index.html">Home</a></li>
      <li><a href="books.html">Books</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul>

    <p>
      Discover a wide range of books in various genres. Dive into the world of
      literature with us.
    </p>
  </body>
</html>
```

### **2. Books Page (`books.html`)**:

```html
<html>
  <head>
    <title>Our Books</title>
  </head>
  <body>
    <h1>Our Books</h1>

    <ul>
      <li><a href="index.html">Home</a></li>
      <li><a href="books.html">Books</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul>

    <ul>
      <li>"The Great Gatsby" by F. Scott Fitzgerald</li>
      <li>"Pride and Prejudice" by Jane Austen</li>
      <li>"To Kill a Mockingbird" by Harper Lee</li>
    </ul>
  </body>
</html>
```

### **3. Contact Page (`contact.html`)**:

```html
<html>
  <head>
    <title>Contact Us</title>
  </head>
  <body>
    <h1>Contact Information</h1>
    <ul>
      <li><a href="index.html">Home</a></li>
      <li><a href="books.html">Books</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul>

    <p>Email: <a href="mailto:info@bookstore.com">info@bookstore.com</a></p>
    <p>Phone: +123 456 7890</p>
  </body>
</html>
```

With this structure, users can navigate between the three pages using the links provided. The `index.html` acts as the central or main page, with `books.html` and `contact.html` as sub-pages. The relative URLs (`href` values) indicate the path to other HTML files, making it easy to navigate between them.

## Example 2.

```jsx
<html>
  <head>
    <title>Contact Us</title>
  </head>
  <body>
    <h1>The History of Coffee</h1>

    <h3>Table of Contents:</h3>
    <ul>
      <li><a href="#origin">Origin of Coffee</a></li>
      <li><a href="#spread">Spread to Europe</a></li>
      <li><a href="#modern-times">Modern Times</a></li>
    </ul>

    <hr />

    <h2 id="origin">Origin of Coffee</h2>
    <p>
      Coffee is believed to have originated in the Ethiopian region. According
      to legend, a 9th-century Ethiopian goat herder discovered coffee by
      accident when he noticed how crazy the beans were making his goats. He
      tried the beans himself and had a similar reaction. After trying the
      beans, the goat herder took them to a local monastery, where they were
      used to create a drink that kept the monks awake during extended hours of
      prayer.
    </p>

    <p>
      Lorem, ipsum dolor sit amet consectetur adipisicing elit. Suscipit
      veritatis esse maxime necessitatibus impedit explicabo delectus, aut
      praesentium sed dolores minus quasi, eveniet rerum. Neque harum molestias
      ea sunt nostrum.
    </p>

    <p>
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Earum harum,
      suscipit voluptates quidem optio odit numquam eos expedita, minus nam
      deserunt consectetur vitae dicta, debitis deleniti voluptatibus doloribus
      hic illo?
    </p>

    <p>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Consequuntur
      nesciunt odio consectetur voluptatibus sequi veritatis, cum harum tenetur
      assumenda optio dolorum quae dicta repellat minus enim maiores cupiditate
      atque, ut magnam quidem consequatur? Veniam aut autem est facilis
      mollitia. Ratione aliquid accusamus ipsum pariatur, necessitatibus maxime
      officia unde mollitia accusantium.
    </p>

    <p>
      Lorem ipsum dolor sit, amet consectetur adipisicing elit. Atque magnam
      rerum aspernatur? Non iure sapiente quo magni. Sunt necessitatibus odio
      corrupti molestiae veniam et qui quasi voluptatem illum excepturi pariatur
      ab, cumque non commodi accusantium quibusdam quas expedita. Aliquid
      mollitia consectetur dicta nihil illo fuga impedit ratione sapiente nemo
      id rem pariatur, eius necessitatibus harum eum tenetur quaerat
      perspiciatis similique! Iste velit tempore aliquam voluptatibus, explicabo
      voluptate! Sunt reprehenderit repellendus omnis voluptatibus vitae illum
      itaque esse quis, beatae libero! Est quas ducimus ut fugit sunt. Illo
      commodi rerum quisquam repudiandae aliquam saepe, delectus explicabo, et
      incidunt atque animi, quae amet?
    </p>

    <p>
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum
      quibusdam eligendi dignissimos hic corporis reprehenderit corrupti iure
      eos maxime est laboriosam possimus vero perferendis iusto odio, quia
      pariatur nobis minima in assumenda. Delectus ut error quos natus
      distinctio a! Nobis facilis omnis ea, praesentium libero quos labore
      obcaecati commodi. Libero ex repudiandae rerum labore consequuntur sit
      dolores tempora. Architecto unde odit, placeat autem sed minima expedita
      laboriosam laborum nemo? Iste cupiditate, aliquam repellendus non,
      recusandae et, eum deserunt doloremque voluptate molestias libero itaque
      similique earum pariatur! Fuga voluptatem cupiditate totam, vero dolore
      eos, tempore nostrum consequatur quaerat possimus error? Nihil, culpa
      deleniti provident explicabo expedita sapiente architecto quis dolor sunt
      hic atque, totam ea officiis saepe nesciunt quod minus eligendi qui a
      accusamus ab eius. Nam eveniet repellat porro possimus ducimus incidunt
      ratione ipsum. Beatae itaque harum, voluptatibus incidunt, facere
      perspiciatis tempora mollitia ab rerum quisquam aliquam impedit, voluptate
      praesentium.
    </p>

    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla illum,
      aspernatur aut molestias dignissimos temporibus qui saepe accusamus dicta!
      Numquam ex optio laudantium voluptatum laborum doloribus non culpa! Vero
      iste modi alias sapiente architecto explicabo veniam exercitationem
      debitis eveniet placeat molestias ex, ipsum voluptate, dolorum voluptatum
      eum minus nesciunt id aliquam. Quos aliquid sed beatae soluta ipsam minus
      delectus iste reiciendis vitae eos sapiente quam, magni hic ea velit nemo
      architecto voluptates libero officiis quia? Dignissimos, iure culpa. Ex
      modi velit libero, quo tempora eaque accusantium expedita praesentium,
      quidem excepturi fugiat ad nemo ut molestias voluptate, ratione laudantium
      exercitationem atque?
    </p>

    <p>
      The story of how coffee grew in popularity in the Arab world is equally
      interesting. It's said that coffee was first roasted and brewed in a
      similar way to how it's prepared today in Yemen. From Yemen, it spread to
      Mecca and then to the entire Arab world.
    </p>

    <p>
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum
      quibusdam eligendi dignissimos hic corporis reprehenderit corrupti iure
      eos maxime est laboriosam possimus vero perferendis iusto odio, quia
      pariatur nobis minima in assumenda. Delectus ut error quos natus
      distinctio a! Nobis facilis omnis ea, praesentium libero quos labore
      obcaecati commodi. Libero ex repudiandae rerum labore consequuntur sit
      dolores tempora. Architecto unde odit, placeat autem sed minima expedita
      laboriosam laborum nemo? Iste cupiditate, aliquam repellendus non,
      recusandae et, eum deserunt doloremque voluptate molestias libero itaque
      similique earum pariatur! Fuga voluptatem cupiditate totam, vero dolore
      eos, tempore nostrum consequatur quaerat possimus error? Nihil, culpa
      deleniti provident explicabo expedita sapiente architecto quis dolor sunt
      hic atque, totam ea officiis saepe nesciunt quod minus eligendi qui a
      accusamus ab eius. Nam eveniet repellat porro possimus ducimus incidunt
      ratione ipsum. Beatae itaque harum, voluptatibus incidunt, facere
      perspiciatis tempora mollitia ab rerum quisquam aliquam impedit, voluptate
      praesentium.
    </p>

    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla illum,
      aspernatur aut molestias dignissimos temporibus qui saepe accusamus dicta!
      Numquam ex optio laudantium voluptatum laborum doloribus non culpa! Vero
      iste modi alias sapiente architecto explicabo veniam exercitationem
      debitis eveniet placeat molestias ex, ipsum voluptate, dolorum voluptatum
      eum minus nesciunt id aliquam. Quos aliquid sed beatae soluta ipsam minus
      delectus iste reiciendis vitae eos sapiente quam, magni hic ea velit nemo
      architecto voluptates libero officiis quia? Dignissimos, iure culpa. Ex
      modi velit libero, quo tempora eaque accusantium expedita praesentium,
      quidem excepturi fugiat ad nemo ut molestias voluptate, ratione laudantium
      exercitationem atque?
    </p>

    <p>
      The story of how coffee grew in popularity in the Arab world is equally
      interesting. It's said that coffee was first roasted and brewed in a
      similar way to how it's prepared today in Yemen. From Yemen, it spread to
      Mecca and then to the entire Arab world.
    </p>

    <h2 id="spread">Spread to Europe</h2>
    <p>
      Coffee first came to Europe through the port of Venice. The first coffee
      shop in Venice opened in 1645. Coffee's popularity grew in Europe during
      the 17th century, and coffee houses opened in major cities across the
      continent. These weren't just places to drink coffee, but places where
      people came to chat, read, write, and conduct business.
    </p>

    <p>
      By the mid-17th century, there were over 300 coffee houses in London. They
      became known as 'penny universities' because for the price of a penny one
      could purchase a coffee and engage in stimulating conversation.
    </p>

    <p>
      Lorem, ipsum dolor sit amet consectetur adipisicing elit. Suscipit
      veritatis esse maxime necessitatibus impedit explicabo delectus, aut
      praesentium sed dolores minus quasi, eveniet rerum. Neque harum molestias
      ea sunt nostrum.
    </p>

    <p>
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Earum harum,
      suscipit voluptates quidem optio odit numquam eos expedita, minus nam
      deserunt consectetur vitae dicta, debitis deleniti voluptatibus doloribus
      hic illo?
    </p>

    <p>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Consequuntur
      nesciunt odio consectetur voluptatibus sequi veritatis, cum harum tenetur
      assumenda optio dolorum quae dicta repellat minus enim maiores cupiditate
      atque, ut magnam quidem consequatur? Veniam aut autem est facilis
      mollitia. Ratione aliquid accusamus ipsum pariatur, necessitatibus maxime
      officia unde mollitia accusantium.
    </p>

    <p>
      Lorem ipsum dolor sit, amet consectetur adipisicing elit. Atque magnam
      rerum aspernatur? Non iure sapiente quo magni. Sunt necessitatibus odio
      corrupti molestiae veniam et qui quasi voluptatem illum excepturi pariatur
      ab, cumque non commodi accusantium quibusdam quas expedita. Aliquid
      mollitia consectetur dicta nihil illo fuga impedit ratione sapiente nemo
      id rem pariatur, eius necessitatibus harum eum tenetur quaerat
      perspiciatis similique! Iste velit tempore aliquam voluptatibus, explicabo
      voluptate! Sunt reprehenderit repellendus omnis voluptatibus vitae illum
      itaque esse quis, beatae libero! Est quas ducimus ut fugit sunt. Illo
      commodi rerum quisquam repudiandae aliquam saepe, delectus explicabo, et
      incidunt atque animi, quae amet?
    </p>

    <p>
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum
      quibusdam eligendi dignissimos hic corporis reprehenderit corrupti iure
      eos maxime est laboriosam possimus vero perferendis iusto odio, quia
      pariatur nobis minima in assumenda. Delectus ut error quos natus
      distinctio a! Nobis facilis omnis ea, praesentium libero quos labore
      obcaecati commodi. Libero ex repudiandae rerum labore consequuntur sit
      dolores tempora. Architecto unde odit, placeat autem sed minima expedita
      laboriosam laborum nemo? Iste cupiditate, aliquam repellendus non,
      recusandae et, eum deserunt doloremque voluptate molestias libero itaque
      similique earum pariatur! Fuga voluptatem cupiditate totam, vero dolore
      eos, tempore nostrum consequatur quaerat possimus error? Nihil, culpa
      deleniti provident explicabo expedita sapiente architecto quis dolor sunt
      hic atque, totam ea officiis saepe nesciunt quod minus eligendi qui a
      accusamus ab eius. Nam eveniet repellat porro possimus ducimus incidunt
      ratione ipsum. Beatae itaque harum, voluptatibus incidunt, facere
      perspiciatis tempora mollitia ab rerum quisquam aliquam impedit, voluptate
      praesentium.
    </p>

    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla illum,
      aspernatur aut molestias dignissimos temporibus qui saepe accusamus dicta!
      Numquam ex optio laudantium voluptatum laborum doloribus non culpa! Vero
      iste modi alias sapiente architecto explicabo veniam exercitationem
      debitis eveniet placeat molestias ex, ipsum voluptate, dolorum voluptatum
      eum minus nesciunt id aliquam. Quos aliquid sed beatae soluta ipsam minus
      delectus iste reiciendis vitae eos sapiente quam, magni hic ea velit nemo
      architecto voluptates libero officiis quia? Dignissimos, iure culpa. Ex
      modi velit libero, quo tempora eaque accusantium expedita praesentium,
      quidem excepturi fugiat ad nemo ut molestias voluptate, ratione laudantium
      exercitationem atque?
    </p>

    <p>
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum
      quibusdam eligendi dignissimos hic corporis reprehenderit corrupti iure
      eos maxime est laboriosam possimus vero perferendis iusto odio, quia
      pariatur nobis minima in assumenda. Delectus ut error quos natus
      distinctio a! Nobis facilis omnis ea, praesentium libero quos labore
      obcaecati commodi. Libero ex repudiandae rerum labore consequuntur sit
      dolores tempora. Architecto unde odit, placeat autem sed minima expedita
      laboriosam laborum nemo? Iste cupiditate, aliquam repellendus non,
      recusandae et, eum deserunt doloremque voluptate molestias libero itaque
      similique earum pariatur! Fuga voluptatem cupiditate totam, vero dolore
      eos, tempore nostrum consequatur quaerat possimus error? Nihil, culpa
      deleniti provident explicabo expedita sapiente architecto quis dolor sunt
      hic atque, totam ea officiis saepe nesciunt quod minus eligendi qui a
      accusamus ab eius. Nam eveniet repellat porro possimus ducimus incidunt
      ratione ipsum. Beatae itaque harum, voluptatibus incidunt, facere
      perspiciatis tempora mollitia ab rerum quisquam aliquam impedit, voluptate
      praesentium.
    </p>

    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla illum,
      aspernatur aut molestias dignissimos temporibus qui saepe accusamus dicta!
      Numquam ex optio laudantium voluptatum laborum doloribus non culpa! Vero
      iste modi alias sapiente architecto explicabo veniam exercitationem
      debitis eveniet placeat molestias ex, ipsum voluptate, dolorum voluptatum
      eum minus nesciunt id aliquam. Quos aliquid sed beatae soluta ipsam minus
      delectus iste reiciendis vitae eos sapiente quam, magni hic ea velit nemo
      architecto voluptates libero officiis quia? Dignissimos, iure culpa. Ex
      modi velit libero, quo tempora eaque accusantium expedita praesentium,
      quidem excepturi fugiat ad nemo ut molestias voluptate, ratione laudantium
      exercitationem atque?
    </p>

    <p>
      The story of how coffee grew in popularity in the Arab world is equally
      interesting. It's said that coffee was first roasted and brewed in a
      similar way to how it's prepared today in Yemen. From Yemen, it spread to
      Mecca and then to the entire Arab world.
    </p>

    <p>
      The story of how coffee grew in popularity in the Arab world is equally
      interesting. It's said that coffee was first roasted and brewed in a
      similar way to how it's prepared today in Yemen. From Yemen, it spread to
      Mecca and then to the entire Arab world.
    </p>

    <h2 id="modern-times">Modern Times</h2>
    <p>
      The way we drink coffee has evolved over time. From the simple brewing
      methods of the past to the more sophisticated machines we have today,
      coffee has seen a lot of change. One of the most significant advancements
      in coffee was the invention of the espresso machine in the early 20th
      century.
    </p>

    <p>
      Today, coffee is enjoyed worldwide, and the culture around it is richer
      than ever. With specialty coffee shops and a vast array of preparation
      methods, coffee isn't just a drink; it's an experience.
    </p>

    <p>
      Lorem, ipsum dolor sit amet consectetur adipisicing elit. Suscipit
      veritatis esse maxime necessitatibus impedit explicabo delectus, aut
      praesentium sed dolores minus quasi, eveniet rerum. Neque harum molestias
      ea sunt nostrum.
    </p>

    <p>
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Earum harum,
      suscipit voluptates quidem optio odit numquam eos expedita, minus nam
      deserunt consectetur vitae dicta, debitis deleniti voluptatibus doloribus
      hic illo?
    </p>

    <p>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Consequuntur
      nesciunt odio consectetur voluptatibus sequi veritatis, cum harum tenetur
      assumenda optio dolorum quae dicta repellat minus enim maiores cupiditate
      atque, ut magnam quidem consequatur? Veniam aut autem est facilis
      mollitia. Ratione aliquid accusamus ipsum pariatur, necessitatibus maxime
      officia unde mollitia accusantium.
    </p>

    <p>
      Lorem ipsum dolor sit, amet consectetur adipisicing elit. Atque magnam
      rerum aspernatur? Non iure sapiente quo magni. Sunt necessitatibus odio
      corrupti molestiae veniam et qui quasi voluptatem illum excepturi pariatur
      ab, cumque non commodi accusantium quibusdam quas expedita. Aliquid
      mollitia consectetur dicta nihil illo fuga impedit ratione sapiente nemo
      id rem pariatur, eius necessitatibus harum eum tenetur quaerat
      perspiciatis similique! Iste velit tempore aliquam voluptatibus, explicabo
      voluptate! Sunt reprehenderit repellendus omnis voluptatibus vitae illum
      itaque esse quis, beatae libero! Est quas ducimus ut fugit sunt. Illo
      commodi rerum quisquam repudiandae aliquam saepe, delectus explicabo, et
      incidunt atque animi, quae amet?
    </p>

    <p>
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum
      quibusdam eligendi dignissimos hic corporis reprehenderit corrupti iure
      eos maxime est laboriosam possimus vero perferendis iusto odio, quia
      pariatur nobis minima in assumenda. Delectus ut error quos natus
      distinctio a! Nobis facilis omnis ea, praesentium libero quos labore
      obcaecati commodi. Libero ex repudiandae rerum labore consequuntur sit
      dolores tempora. Architecto unde odit, placeat autem sed minima expedita
      laboriosam laborum nemo? Iste cupiditate, aliquam repellendus non,
      recusandae et, eum deserunt doloremque voluptate molestias libero itaque
      similique earum pariatur! Fuga voluptatem cupiditate totam, vero dolore
      eos, tempore nostrum consequatur quaerat possimus error? Nihil, culpa
      deleniti provident explicabo expedita sapiente architecto quis dolor sunt
      hic atque, totam ea officiis saepe nesciunt quod minus eligendi qui a
      accusamus ab eius. Nam eveniet repellat porro possimus ducimus incidunt
      ratione ipsum. Beatae itaque harum, voluptatibus incidunt, facere
      perspiciatis tempora mollitia ab rerum quisquam aliquam impedit, voluptate
      praesentium.
    </p>

    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla illum,
      aspernatur aut molestias dignissimos temporibus qui saepe accusamus dicta!
      Numquam ex optio laudantium voluptatum laborum doloribus non culpa! Vero
      iste modi alias sapiente architecto explicabo veniam exercitationem
      debitis eveniet placeat molestias ex, ipsum voluptate, dolorum voluptatum
      eum minus nesciunt id aliquam. Quos aliquid sed beatae soluta ipsam minus
      delectus iste reiciendis vitae eos sapiente quam, magni hic ea velit nemo
      architecto voluptates libero officiis quia? Dignissimos, iure culpa. Ex
      modi velit libero, quo tempora eaque accusantium expedita praesentium,
      quidem excepturi fugiat ad nemo ut molestias voluptate, ratione laudantium
      exercitationem atque?
    </p>

    <p>
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum
      quibusdam eligendi dignissimos hic corporis reprehenderit corrupti iure
      eos maxime est laboriosam possimus vero perferendis iusto odio, quia
      pariatur nobis minima in assumenda. Delectus ut error quos natus
      distinctio a! Nobis facilis omnis ea, praesentium libero quos labore
      obcaecati commodi. Libero ex repudiandae rerum labore consequuntur sit
      dolores tempora. Architecto unde odit, placeat autem sed minima expedita
      laboriosam laborum nemo? Iste cupiditate, aliquam repellendus non,
      recusandae et, eum deserunt doloremque voluptate molestias libero itaque
      similique earum pariatur! Fuga voluptatem cupiditate totam, vero dolore
      eos, tempore nostrum consequatur quaerat possimus error? Nihil, culpa
      deleniti provident explicabo expedita sapiente architecto quis dolor sunt
      hic atque, totam ea officiis saepe nesciunt quod minus eligendi qui a
      accusamus ab eius. Nam eveniet repellat porro possimus ducimus incidunt
      ratione ipsum. Beatae itaque harum, voluptatibus incidunt, facere
      perspiciatis tempora mollitia ab rerum quisquam aliquam impedit, voluptate
      praesentium.
    </p>

    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla illum,
      aspernatur aut molestias dignissimos temporibus qui saepe accusamus dicta!
      Numquam ex optio laudantium voluptatum laborum doloribus non culpa! Vero
      iste modi alias sapiente architecto explicabo veniam exercitationem
      debitis eveniet placeat molestias ex, ipsum voluptate, dolorum voluptatum
      eum minus nesciunt id aliquam. Quos aliquid sed beatae soluta ipsam minus
      delectus iste reiciendis vitae eos sapiente quam, magni hic ea velit nemo
      architecto voluptates libero officiis quia? Dignissimos, iure culpa. Ex
      modi velit libero, quo tempora eaque accusantium expedita praesentium,
      quidem excepturi fugiat ad nemo ut molestias voluptate, ratione laudantium
      exercitationem atque?
    </p>

    <p>
      The story of how coffee grew in popularity in the Arab world is equally
      interesting. It's said that coffee was first roasted and brewed in a
      similar way to how it's prepared today in Yemen. From Yemen, it spread to
      Mecca and then to the entire Arab world.
    </p>

    <p>
      The story of how coffee grew in popularity in the Arab world is equally
      interesting. It's said that coffee was first roasted and brewed in a
      similar way to how it's prepared today in Yemen. From Yemen, it spread to
      Mecca and then to the entire Arab world.
    </p>

    <a href="#">Back to Top</a>
  </body>
</html>
```

## Live Server URL

If you're using the "Live Server" extension in Visual Studio Code (VSCode), it provides you with a way to serve your static (HTML, CSS, and JavaScript) files to a local development server, allowing you to preview your changes in real time in a web browser. This is particularly useful when you're building and testing websites.

When you start "Live Server", it creates a URL that usually looks something like this:

```
<http://127.0.0.1:5500/path-to-your-file.html>

```

Let's break down this URL:

1. **`http://`**: This is the protocol. In web URLs, you'll typically see `http` or `https` (the latter is a secure version). For local development, `http` is just fine.
2. **`127.0.0.1`**: This is an IP address, specifically the loopback address. It always refers to the current device used to access it, meaning your own computer in this case. In the context of web development, it's a way to say "this computer" or "localhost". You might also see `localhost` used in place of `127.0.0.1`, and they mean the same thing in this context.
3. **`:5500`**: This is the port number. A port can be thought of as a specific "door" through which data can be sent or received on a computer. The Live Server extension in VSCode defaults to port 5500, but if that port is already in use, it may choose another one like 5501.
4. **`/path-to-your-file.html`**: This is the path to the specific file you're serving. If you started the live server on an `index.html` file inside a folder called `mywebsite`, this part might look like `/mywebsite/index.html`.

So, when you access this URL in your browser, you're essentially telling it to connect to your own computer (via `127.0.0.1` or `localhost`), on port `5500`, and retrieve the specific file mentioned in the path.

One more thing to note: since this server is local (it runs on your computer), only you can access this URL. If someone else tries to access this URL from their computer, they won't be able to see your website because `127.0.0.1` will point to their own computer, not yours.

### In Summary:

The HTML `<a>` tag is the bridge of the internet world, connecting myriad pages and providing smooth navigation. Whether you're guiding visitors to another part of your website, letting them download a file, or even enabling them to send you an email, the anchor element is your go-to tool. Use it wisely and enhance the browsing experience for everyone venturing onto your island in the vast ocean of the web.

## Images & Media

- Inserting Images: Img and Picture Tags
- Image Maps
- Adding Audio and Video with fallbacks using links. Support for all browsers.
- Vector Graphics & Illustrations (SVG & Figma)

`img` `picture` `audio` 

## `img` tag

The `<img>` tag in HTML is used to embed images in a webpage. It's an empty (self-closing) tag, which means it doesn't have a closing tag like `</img>`.

**Attributes of the `<img>` tag:**

1. **src** (required): Specifies the path to the image. This can be an absolute URL, a relative URL, or even a data URL.
    
    Example:
    
    ```html
    <img src="path/to/image.jpg" alt="Description of Image">
    
    ```
    
2. **alt** (recommended): Provides alternative text for the image if the image cannot be displayed. It's also important for accessibility.
    
    Example:
    
    ```html
    <img src="path/to/image.jpg" alt="A scenic view of a mountain">
    
    ```
    
3. **width** & **height**: Define the width and height of the image in pixels. If you only define one of these (e.g., only width), the browser will automatically scale the other dimension to maintain the image's original aspect ratio. It's often a good idea to specify these dimensions to prevent page reflows as images load.
    
    Example:
    
    ```html
    <img src="path/to/image.jpg" alt="Description" width="300" height="200">
    
    ```
    
4. **usemap**: Specifies an image map to use with the image. An image map allows different parts of an image to become clickable, each linking to a different URL.
5. **ismap**: Specifies that the image is part of a server-side image map (less common in modern web development).
6. **crossorigin**: This attribute deals with how the element handles CORS (Cross-Origin Resource Sharing) requests. The two potential values are `anonymous` and `use-credentials`.
7. **loading**: This is a newer attribute that can be set to `lazy` or `eager`. If set to `lazy`, it indicates to the browser that the image can be loaded lazily (e.g., when it's near the viewport). This can be very useful for performance, especially with large images below the fold.
    
    Example:
    
    ```html
    <img src="path/to/image.jpg" alt="Description" loading="lazy">
    
    ```
    
8. **decoding**: Provides a hint to the browser on how to decode the image. Can be set to `sync`, `async`, or `auto`.

**Best Practices:**

1. **Always provide alt text:** It's essential for accessibility. Screen readers will read the alt text to describe the image to users who can't see it.
2. **Responsive Images:** You can use the `srcset` attribute and `<picture>` element to serve different images based on device capabilities, such as viewport size or screen density.
3. **Avoid using the `<img>` tag for decorative images:** For images that are purely decorative and add no content value, consider using CSS background images or the `aria-hidden="true"` attribute to hide them from screen readers.

**Examples:**

1. **Basic Image Embedding:**
    
    ```html
    <img src="path/to/image.jpg" alt="A beautiful sunset">
    
    ```
    
2. **Responsive Image with srcset:**
    
    ```html
    <img srcset="image-320w.jpg 320w,
                 image-480w.jpg 480w,
                 image-800w.jpg 800w"
         sizes="(max-width: 320px) 280px,
                (max-width: 480px) 440px,
                800px"
         src="image-800w.jpg"
         alt="A responsive image">
    
    ```
    
3. **Using the `<picture>` element for art direction:**
    
    ```html
    <picture>
        <source media="(max-width: 799px)" srcset="image-mobile.jpg">
        <source media="(min-width: 800px)" srcset="image-desktop.jpg">
        <img src="image-desktop.jpg" alt="A picture element example">
    </picture>
    
    ```
    

## Image Maps

Image maps in HTML allow you to create clickable regions within an image. This can be useful for scenarios like a geographical map where you want different areas to link to different content, or an interactive graphic with multiple clickable elements.

An image map comprises two main parts:

1. The `<map>` element, which contains a set of `<area>` elements.
2. The `<img>` element that uses the map, specified via its `usemap` attribute.

**Attributes for the `<map>` element:**

- **name**: Specifies a unique name for the map.

**Attributes for the `<area>` element:**

1. **shape**: Defines the shape of the clickable area. Possible values are:
    - `rect` (rectangle)
    - `circle`
    - `poly` (polygon)
    - `default` (the entire area of the image if no other shape is specified)
2. **coords**: Defines the coordinates of the clickable area. The way you specify coordinates depends on the shape:
    - `rect`: top-left x, top-left y, bottom-right x, bottom-right y
    - `circle`: center x, center y, radius
    - `poly`: x1, y1, x2, y2, ..., xn, yn (for a polygon with n points)
3. **href**: Specifies the link where the user will be taken when the area is clicked.
4. **alt**: A short description of the clickable area. Useful for accessibility.
5. **target**: Specifies where to open the linked document. Common values are `_blank` (a new tab or window) and `_self` (the current window).

**Example:**

Let's say you have an image (`map.jpg`) of a simple map with two regions you want to make clickable: a circular lake and a rectangular forest.

HTML:

```html
<img src="map.jpg" alt="Clickable map" usemap="#mymap">

<map name="mymap">
    <!-- Define a circular area for the lake -->
    <area shape="circle" coords="120,180,60" href="lake.html" alt="Lake" target="_blank">

    <!-- Define a rectangular area for the forest -->
    <area shape="rect" coords="260,120,400,220" href="forest.html" alt="Forest">
</map>

```

In the above example:

- The `usemap="#mymap"` attribute in the `<img>` tag links the image to the map named `mymap`.
- The lake, represented as a circle, is defined with its center at coordinates (120,180) and a radius of 60 pixels. When clicked, it opens `lake.html` in a new tab.
- The forest, represented as a rectangle, starts at coordinates (260,120) for its top-left corner and ends at (400,220) for its bottom-right corner. Clicking on it will navigate the user to `forest.html` in the same window.

**Things to Remember:**

1. Image maps can be less accessible than other navigational methods. Always provide alternative methods of navigation for those using screen readers or keyboards.
2. Image maps might not scale properly on responsive websites. If your image scales with the viewport, the coordinates for your clickable areas will be off. Some JavaScript libraries can help address this issue.
3. Image maps are less common in modern web design. Before implementing them, consider if there are more contemporary, accessible, and responsive-friendly solutions that would meet your needs.

If you decide to use image maps, always test on various devices and browsers to ensure your clickable regions are accurate and provide the desired functionality.

## `picture` tag

The `<picture>` element is a container used to specify multiple `<source>` elements for a specific `<img>` contained within it, to allow developers to serve the appropriate image to users depending on various conditions, like viewport size and screen resolution. This is particularly useful for responsive web design and improving page load times on mobile devices.

**Attributes of the `<source>` element within `<picture>`:**

1. **srcset**: Specifies the path or paths to the image(s). This can be a comma-separated list of URLs, each followed by a width descriptor (e.g., `600w`) or a pixel density descriptor (e.g., `1.5x`).
2. **sizes**: Defines a set of media conditions (like screen widths) and indicates what image size would be best to choose, when multiple sizes are available in `srcset`.
3. **media**: Similar to CSS media queries, this attribute allows you to test and apply different images based on the outcome.
4. **type**: Specifies the MIME type of the image (like `image/jpeg` or `image/webp`). This is particularly useful when you want to serve newer image formats to browsers that support them, while falling back to more widely-supported formats for other browsers.

**Usage:**

1. **Art Direction**: Sometimes, it's not just about scaling an image. At different viewport sizes, you might want to serve entirely different images. This is where art direction comes into play.
    
    ```html
    <picture>
        <source media="(max-width: 699px)" srcset="small.jpg">
        <source media="(min-width: 700px)" srcset="large.jpg">
        <img src="default.jpg" alt="Description of the image">
    </picture>
    
    ```
    
    If the viewport is 699 pixels wide or smaller, `small.jpg` will be used. If it's 700 pixels wide or larger, `large.jpg` will be used. If the browser doesn't support the `<picture>` element, `default.jpg` will be loaded.
    
2. **Different Image Formats**: You can serve modern image formats like WebP to browsers that support it, and fall back to JPEG or PNG for browsers that don't.
    
    ```html
    <picture>
        <source type="image/webp" srcset="image.webp">
        <img src="image.jpg" alt="Description of the image">
    </picture>
    
    ```
    
    Browsers that support WebP will load `image.webp`, while others will fall back to `image.jpg`.
    
3. **Resolution Switching**: Serve different resolution images based on the screen's pixel density.
    
    ```html
    <picture>
        <source srcset="low-res.jpg 1x, high-res.jpg 2x">
        <img src="default.jpg" alt="Description of the image">
    </picture>
    
    ```
    
    Devices with standard displays (1x) will load `low-res.jpg`, while devices with high-resolution (like Retina displays, 2x) will load `high-res.jpg`.
    

**Things to remember:**

- The `<img>` element inside the `<picture>` container is always required. It serves as a fallback for browsers that don't support the `<picture>` element.
- The browser will evaluate the `<source>` elements in order, so always place your preferred or most modern formats/conditions first.
- The `alt` attribute for the image should always be placed in the `<img>` tag, not in the `<source>` tags.
- While `<picture>` and `<source>` give a lot of power for responsive images, always test across various devices and browsers to ensure your images load as expected.

The `<picture>` element is a step forward in making web content more responsive and faster-loading, offering better user experiences across various devices and conditions.

## Audio & Video

The introduction of the `<audio>` and `<video>` elements in HTML5 was a significant move towards standardizing media playback across the web, reducing the need for plugins like Flash. Let's delve into each element:

## `<audio>`

The `<audio>` element is used to embed sound content in documents.

### Attributes:

- **src**: The URL of the audio to embed.
- **controls**: If present, the browser will offer playback controls.
- **autoplay**: The audio will start playing as soon as it's ready.
- **loop**: The audio will start over again every time it finishes.
- **muted**: Specifies that the audio output should be muted.
- **preload**: Hints to the browser about how the audio should be loaded when the page loads (`none`, `metadata`, or `auto`).

### Example:

```html
<audio controls>
  <source src="sound.mp3" type="audio/mpeg">
  <source src="sound.ogg" type="audio/ogg">
  Your browser does not support the audio element.
</audio>

```

Here, we provide both an MP3 and an Ogg file for the audio to ensure it plays on as many browsers as possible. The message "Your browser does not support the audio element." serves as a fallback for browsers that don't support the `<audio>` element.

## `<video>`

The `<video>` element is used to embed video content.

### Attributes (most are similar to `<audio>`):

- **src**: The URL of the video to embed.
- **controls**: If present, the browser will offer playback controls.
- **autoplay**: The video will start playing as soon as it's ready.
- **loop**: The video will start over again, every time it finishes.
- **muted**: Specifies that the audio output of the video should be muted.
- **preload**: Hints to the browser about how the video should be loaded when the page loads.
- **poster**: An image to show as a placeholder before the video plays.
- **width** and **height**: Set the size of the video player.

### Example:

```html
<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
  Your browser does not support the video tag.
</video>

```

Like with the `<audio>` example, we provide both MP4 and Ogg file formats to accommodate different browsers. The fallback message "Your browser does not support the video tag." is shown for unsupported browsers.

## Fallbacks & Support:

1. **Multiple Formats**: Always provide multiple formats for your media to accommodate different browsers. For example, MP3 and Ogg for audio, MP4 and Ogg for video.
2. **Text Fallback**: Inside the `<audio>` or `<video>` tag, include a message for browsers that don't support these tags.
3. **JavaScript Fallback**: For more advanced fallbacks, you can use JavaScript to detect whether the browser supports certain media formats and react accordingly.
4. **Content Delivery Networks (CDNs)**: Some CDNs and services offer video players that come with fallbacks built-in, automatically serving the right format based on the user's browser.
5. **Subtitles and Captions**: The `<track>` element can be used within the `<video>` tag to add subtitles or captions.

### Browser Support:

As of my last update in 2021:

- **`<audio>` and `<video>`**: Supported in all modern browsers, including the latest versions of Chrome, Firefox, Safari, Edge, and Opera.
- **MP4**: Supported by Chrome, Firefox, Safari, Edge, and Opera.
- **Ogg**: Supported by Chrome, Firefox, and Opera.
- **WebM**: Supported by Chrome, Firefox, Edge, and Opera.

However, always check updated compatibility tables and test in various browsers to ensure broad support.

## SVG

SVG, which stands for Scalable Vector Graphics, is an XML-based image format used to display vector images on the web. Unlike raster images (like JPG, PNG, etc.), which are composed of pixels, SVG images are made up of paths, shapes, and fills, allowing them to be scaled indefinitely without any loss of quality.

**Advantages of SVGs:**

1. **Scalability**: Can be resized without loss of quality.
2. **File Size**: Often smaller than their raster counterparts, especially for simpler images or icons.
3. **Stylable**: You can style them with CSS and add interactivity with JavaScript.
4. **Accessibility**: Since SVG is XML-based, it can be more accessible than raster images.
5. **Resolution Independence**: Looks crisp on Retina and other high-density displays.

## Basic Structure

An SVG has a root `<svg>` element, within which various shapes and paths are defined.

```html
<svg width="100" height="100" xmlns="<http://www.w3.org/2000/svg>">
    <!-- Rectangle -->
    <rect x="10" y="10" width="30" height="30" fill="blue" />
    <!-- Circle -->
    <circle cx="70" cy="70" r="15" fill="red" />
</svg>

```

This SVG draws a blue rectangle and a red circle.

## Key SVG Elements:

1. **`<rect>`**: Draws rectangles. Key attributes include `x`, `y`, `width`, `height`, `fill`, `stroke`, and `stroke-width`.
2. **`<circle>`**: Draws circles. Important attributes: `cx`, `cy` (center coordinates), and `r` (radius).
3. **`<ellipse>`**: Draws ellipses. Attributes: `cx`, `cy`, `rx` (x-axis radius), `ry` (y-axis radius).
4. **`<line>`**: Draws straight lines. Attributes: `x1`, `y1` (start point), `x2`, `y2` (end point).
5. **`<polyline>`**: Draws a series of connected lines. The `points` attribute defines the list of points.
6. **`<polygon>`**: Like `<polyline>`, but the start and end points are connected.
7. **`<path>`**: Most flexible and commonly used. `d` attribute contains path data and commands.

Example of a simple path:

```html
<path d="M10 10 L90 10 L50 90z" fill="green" />

```

This draws a green triangle using the `M` (move to), `L` (line to), and `z` (close path) commands.

1. **`<text>`**: To display text. Attributes include `x`, `y`, and standard font styling attributes.

```html
<text x="10" y="40" font-family="Arial" font-size="20" fill="black">Hello SVG</text>

```

## Styling and Interactivity

SVGs can be styled using CSS and can have interactivity added with JavaScript. You can include class or ID attributes to SVG elements and then target them in your stylesheets or scripts.

## SVG Inclusion Methods:

1. **Inline**: Directly embed SVG markup in HTML.
2. **Image Tag**: `<img src="image.svg" alt="Description">`
3. **CSS Background**: `background-image: url('image.svg');`
4. **Object or iFrame**: Embed using the `<object>` or `<iframe>` tags.
5. **SVG Sprites**: Combining multiple SVGs into one and then displaying parts as needed.

## Fallback for SVG:

Not all browsers, especially older ones, support SVG. You can provide a fallback using the `<img>` tag's `onerror` attribute:

```html
<img src="image.svg" alt="Description" onerror="this.onerror=null; this.src='image.png'">

```

If the SVG fails to load, the PNG version will be loaded as a fallback.

## Tips:

1. **Optimization**: Tools like [SVGOMG](https://jakearchibald.github.io/svgomg/) can help in optimizing SVGs for the web.
2. **Creating SVG**: Many graphic design software options, such as Adobe Illustrator or Inkscape, can export graphics as SVG.

## Conclusion:

SVG offers a flexible, resolution-independent method for displaying graphics on the web. With advantages in scalability, styling, and interactivity, it's a powerful tool in the web developer's toolkit. However, it's essential to be mindful of browser support and ensure that your graphics are accessible to all users.