# Declarative Vs Imperative Programming

Serial: 1
Made for: Beginner
Requirement: Must Have
Time in minutes: 20
Learning Objectives: React Basics
doc-id: react-1

## **HTML and CSS :**

Back in the day, most websites were static and "read-only." Like a flyer/document which is used to share information and the person can look at it but not interact much. It started with HTML pages, CSS was then introduced to add some styling to page.

## **Javascript :**

JavaScript makes the webpage interactive, enabling it to respond to user actions like clicks and typing. For example : In masai school’s website, When you as a user clicks on `Apply Now` button. That acted as a trigger and the page responds by redirecting you to sign up. This was possible because of javascript.

First question : Can a developer build a website with just HTML, CSS, Javascript - The answer is “Yes”.

Then why React ?

Because React offers a more efficient, powerful, and scalable way to build modern web applications. We will talk about this in detailed fashion in future but for now let’s get some handson coding done on React and familiarise ourselves with it.

## React :

Two points before I begin :

1. React is basically a javascript library. That means it’s not a new language but just a technology built on top of javascript. That means when you are coding in react, you are basically coding in HTML, CSS and Javascript. There is no new language that you will be learning
2. I can start with more and more theory like “What is React”, “What is javascript library”.. Etc But I am not and it’s intentional. The idea of taking today’s session is
   1. To understand the purpose of react.
   2. To understand the way of writing code in react ( Though most of the code looks familiar. The mental-model/mindset you’d need here will be different )

With that said, let’s begin

### Task 1 ( 3 Minutes ) :

Observe the following piece of code. Better try it out in your computers.

How do we write code in javascript

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Create UI with DOM & JS</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="text/javascript">
      const element = document.createElement("p");
      element.textContent = "Carpe Diem";
      element.className = "quote";

      const rootElement = document.getElementById("root");
      rootElement.appendChild(element);
    </script>
  </body>
</html>
```

Ref :

[](https://github.com/abduljabbarpeer/fe-react/blob/main/session-1/example-1/index.html)

Observe the way in which we are talking to javascript here

- Hey Javascript, Create an `p` element and store it in a variable called `element`
- Set the `textContent` property of the `element` to be “Carpe Diem”
- Add className `quote` to `element`
- `append` `element` to the `root`

This is imperative way of writing code. In the imperative way of coding, we give a step-by-step instruction to the engine. We tell - **“How to do something”**

How do we write code in React

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Create UI With React API</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
  <script
    crossorigin
    src="https://unpkg.com/react@18/umd/react.development.js"
  ></script>
  <script
    crossorigin
    src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"
  ></script>
  <script src="https://unpkg.com/@babel/standalone@7.8.3/babel.js"></script>
  <script type="text/babel">
    const root = ReactDOM.createRoot(document.getElementById("root"));
    root.render(<p className="quote">Carpe Diem</p>);
  </script>
</html>
```

Ref :

[](https://github.com/abduljabbarpeer/fe-react/blob/main/session-1/example-2/index.html)

Observe the way in which we are talking to react here

- Hey React, Display a `p` tag inside `root` which has `className` `quote` and has text `“Carpe Diem”` in it.

This is declarative way of writing code. In declarative way of coding, we simply tell - **“What to do”**

Quick Summary : Working with DOM directly using Javascript is an **imperative** way of programming, whereas Working with React is a **declarative** way of programming.
