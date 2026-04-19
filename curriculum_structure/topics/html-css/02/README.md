# Introduction to HTML (Basic) (15mins)

## Is HTML a programming language?

HTML is not a programming language - it’s a markup language. Once we dive into a programming language like JavaScript, you will see that they write logic that can be executed, but writing HTML is more like formatting your essay, Giving it a structure & marking it with a marker.

[https://www.figma.com/file/4Y3aYyYlwvkkwu81RYwM9x/Understanding-Markups?type=whiteboard&node-id=0-1&t=TNmxEQXoXcTVzUm6-0](https://www.figma.com/file/4Y3aYyYlwvkkwu81RYwM9x/Understanding-Markups?type=whiteboard&node-id=0-1&t=TNmxEQXoXcTVzUm6-0) 

### So is HTML a programming language or not?

![HTML-and-CSS-Jokes-844x1024.jpeg](Introduction%20to%20HTML%20(Basic)%20(15mins)%2074ebd34d6b0f4f10b844fa02053325d4/HTML-and-CSS-Jokes-844x1024.jpeg)

- Think of it this way: you can’t compute the sum of 2 + 2 in HTML; that’s not what it’s for. This is because HTML is not a programming language. HTML means hypertext markup language.

What is markup language?

> ***A computer language that consists of easily understood keywords, names, or tags that help format the overall view of a page and the data it contains.***
> 

## HTML is not the only markup language

There are many other markup languages:

- XML
- Markdown
- BPML
- FpML
- XBRL
- … and many more

Markdown markup language is beautifully used by modern apps like WhatsApp.

![Untitled](Introduction%20to%20HTML%20(Basic)%20(15mins)%2074ebd34d6b0f4f10b844fa02053325d4/Untitled.png)

In markup languages, the emphasis is squarely on presentation. Think of the asterisks (*) and underscores () in Markdown as little magic wands that tell the text how to dress up. When you wrap a word or a group of words with asterisks, they get dressed in a **bold "outfit."** Use underscores, and your text dresses up into an italic style. These symbols `*` and `_`* are like fashion cues in the language of Markdown; they're **tags** that instruct how the text should appear on the screen.

Just like Markdown has its style cues, so does HTML, another markup language. Instead of using single characters like `*` or `_`, HTML uses more descriptive **tags** enclosed in angle brackets. For instance, to make text bold in HTML, you'd surround it with **`<strong>`** tags. If you want to italicize text, you'd use **`<em>`** tags.

So in essence, most markup languages — including HTML—operate on the same basic principle. They have their unique set of **tags** that ensures that what you see on the screen is dressed just the way you intended.

## Playing around with HTML

### Example codes

```html
  <!-- The h1 tag is used for main headings -->
  <h1>Introduction to HTML Tags</h1>

  <!-- The p tag is used for paragraphs -->
  <p>HTML tags are the building blocks of HTML pages. They define the structure and content of the document.</p>

  <!-- The em tag is used to emphasize text -->
  <p>This is a sentence with <em>emphasized</em> text.</p>

  <!-- The strong tag is used to indicate strong importance for its contents -->
  <p>This is a sentence with <strong>strongly emphasized</strong> text.</p>

```

- `<h1>`: Used for main headings. It's the highest level of the HTML headings and is usually the most prominent item on the page.
- `<p>`: Used for paragraphs. It organizes and groups sentences and text blocks.
- `<em>`: Emphasizes text, changing its meaning. Text inside an `<em>` element is typically displayed in italics.
- `<strong>`: Indicates strong emphasis. Text within a `<strong>` element is typically displayed in bold.

### Example Code

Codepen: 

- [https://codepen.io/drupalastic/pen/zYyqPdm?editors=1000](https://codepen.io/drupalastic/pen/zYyqPdm?editors=1000)
- [https://codepen.io/drupalastic/pen/abPNVLX?editors=1000](https://codepen.io/drupalastic/pen/abPNVLX?editors=1000)

## HTML vs CSS vs JavaScript

![Untitled](Introduction%20to%20HTML%20(Basic)%20(15mins)%2074ebd34d6b0f4f10b844fa02053325d4/Untitled%201.png)

Think of building a house as akin to creating a webpage. The fundamental architecture—the pillars that hold up the structure, the walls that divide rooms, and the roof that covers everything—is akin to HTML. These elements set the "bones" of the house, delineating spaces for living, sleeping, cooking, etc., just as HTML tags define where text, images, and links go on a web page.

Once the house is built, you're not going to leave it bare, right? That's where interior and exterior design come into play. The paint on the walls, the color scheme of the rooms, the curtains on the windows, and the decoration pieces on the coffee table—all these stylistic choices are like CSS. They add aesthetic flair and functionality to the basic structure, transforming it from a mere construction of brick and mortar into a cozy, visually appealing home.

Now think of JavaScript as the electricity that powers the lights, appliances, and heating or cooling systems, as well as the doorbell that rings when someone is at your front door. The electricity adds a functional layer to the house, allowing you to live comfortably and do tasks more easily. Similarly, the doorbell adds an interactive feature; when someone pushes the button, you're alerted to a visitor at your door. In the digital realm, JavaScript enables dynamic, interactive features like alert boxes, real-time updates, and more on a website.

## Example Code  ( Real Examples )

HTML: [https://codepen.io/drupalastic/pen/mdaPqry?editors=0010](https://codepen.io/drupalastic/pen/mdaPqry?editors=0010) 
HTML + CSS: [https://codepen.io/drupalastic/pen/MWZyOjr?editors=1100](https://codepen.io/drupalastic/pen/MWZyOjr?editors=1100) 
HTML + CSS + JS: [https://codepen.io/drupalastic/pen/XWodzKY?editors=1000](https://codepen.io/drupalastic/pen/XWodzKY?editors=1000) 

HTML + JS: [https://codepen.io/drupalastic/pen/mdaPqOy?editors=0100](https://codepen.io/drupalastic/pen/mdaPqOy?editors=0100) 

- Source Code
    
    ```jsx
    <div class="container">
      <h1>To-Do List</h1>
      <div class="input-container">
        <input type="text" id="taskInput" placeholder="Add a new task...">
        <button id="addTaskButton">Add Task</button>
      </div>
      <ul id="taskList">
        <li>Buy groceries</li>
        <li>Call mom</li>
      </ul>
    </div>
    ```
    
    ```jsx
    body {
      font-family: "Arial", sans-serif;
      background-color: #f4f4f4;
      margin: 0;
      padding: 0;
    }
    
    .container {
      max-width: 600px;
      margin: 50px auto;
      background-color: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    
    h1 {
      text-align: center;
      margin-bottom: 20px;
    }
    
    .input-container {
      display: flex;
      justify-content: space-between;
      margin-bottom: 20px;
    }
    
    input[type="text"] {
      width: 75%;
      padding: 10px;
      font-size: 18px;
      margin-right: 10px;
    }
    
    button {
      flex-grow: 1;
      padding: 10px;
      font-size: 18px;
      cursor: pointer;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
    }
    
    ul {
      list-style: none;
      padding: 0;
    }
    
    ul li {
      background-color: #f1f1f1;
      margin: 8px 0;
      padding: 10px;
      font-size: 18px;
      border-radius: 4px;
    }
    ```
    
    ```jsx
    document.addEventListener("DOMContentLoaded", function () {
      const taskInput = document.getElementById("taskInput");
      const addTaskButton = document.getElementById("addTaskButton");
      const taskList = document.getElementById("taskList");
    
      // Add click event to existing list items
      const existingItems = taskList.querySelectorAll("li");
      existingItems.forEach(function (item) {
        item.addEventListener("click", function () {
          this.classList.toggle("completed");
        });
      });
    
      addTaskButton.addEventListener("click", function () {
        const newTask = taskInput.value.trim();
    
        if (newTask === "") {
          return;
        }
    
        const listItem = document.createElement("li");
        listItem.textContent = newTask;
    
        listItem.addEventListener("click", function () {
          this.classList.toggle("completed");
        });
    
        taskList.appendChild(listItem);
        taskInput.value = "";
      });
    });
    ```
    

## Definition of HTML

"HTML, or Hypertext Markup Language, is the standard markup language used for creating web pages and web applications. It serves as the backbone of most websites and provides the structure for the content presented in web browsers. HTML is a tree-like structure of nested elements, defined using 'tags' enclosed in angle brackets. These tags label pieces of content like headings, paragraphs, links, images, lists, forms, and many others, instructing the browser on how to render them. While HTML sets the structure and presentation, it is commonly used in conjunction with CSS for styling and JavaScript for interactivity to create a fully integrated web experience.”

HTML is used to write content and give it semantic meaning;

## Markup Language VS Programming Language

HTML stands for Hypertext Markup Language, and it is often referred to as a markup language. While some may argue that HTML is a programming language, it is more accurately a markup language, which is a type of language that is used to describe the structure and presentation of digital documents.

A programming language, on the other hand, is a language that is used to write code that can be executed by a computer. HTML cannot be used to write code that can be executed by a computer, but it is used to describe the structure of a web page.

HTML is used to create the building blocks of a website, such as text, images, and links. It allows web developers to mark up the content of a web page, which can then be styled and presented using CSS. JavaScript is then used to add interactivity and dynamic functionality to the web page.

In summary, HTML is a markup language that is used to describe the structure and content of a web page, but it is not a programming language in the traditional sense.HTML is a markup language used to create web pages. It is not a programming language, but rather a language used to describe the structure and presentation of digital documents. While HTML cannot be used to write code that is executed by a computer, it enables web developers to mark up the content of a web page, which can then be styled and presented using CSS.

Furthermore, HTML is used to create the building blocks of a website, such as text, images, and links. This provides the foundation for a web page, which can then be enhanced with JavaScript to add interactivity and dynamic functionality.

In conclusion, while HTML is not a programming language, it is a crucial component of web development and is used to create the structure and content of a web page.