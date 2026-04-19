# JS and DOM Vs React and ReactDOM ( Let’s talk syntax )

Serial: 2
Made for: Beginner
Requirement: Must Have
Time in minutes: 30
Learning Objectives: React Basics
doc-id: react-2

## JS and DOM :

The DOM that we have learned so far, we use  `document` API ( Which is a browser API ) 

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
			// 1. Create a DOM element using document.createElement method
      const element = document.createElement("p");
      element.textContent = "Carpe Diem";
      element.className = "quote";

			// 2. Catch hold of the root element directly in the DOM tree and append it to that;
      const rootElement = document.getElementById("root");
      rootElement.appendChild(element);
    </script>
  </body>
</html>
```

### **React and ReactDOM :**

React and ReactDOM

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Create UI with React API</title>
  </head>
  <body>
    <div id="root"></div>
    <!-- 1. Add React and ReactDOM Packages -->
    <script src="https://www.unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
    <script src="https://www.unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
    <script>
      // 2. Create a react element using React.createElement method.
      const element = React.createElement("p", {
        className: "quote",
        children: "Carpe Diem",
      });

      // 3. Define a location in your HTML (like a div with an ID of "root") where your React application will be attached. ( It's like you inform react that I want the entire react app to be within this div#root here )
      const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
      // 4. render method basically takes react element. Convert react element to actual DOM and attach it to root element in HTML
      reactRoot.render(element);
    </script>
  </body>
</html>
```

# Why **React ?**

React was born out of a need to make it easier for developers to build complex and interactive UIs. One of React's main goals is to minimize direct interactions with the actual DOM. Why? Well, directly manipulating the DOM is slow and expensive in terms of performance.

1. Add `React` and `ReactDOM` libraries to your webpage.
    
    ```html
    <script src="https://www.unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
    <script src="https://www.unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
    ```
    
2. **`React` and `React.createElement`** : In vanilla JavaScript, you'd interact directly with the DOM elements using the Document API. With React, you don't do that. Instead, you deal with **React elements**. We use `createElement` method from react to create React elements 
    
    ```jsx
    const element = React.createElement("div", {
            className: "quote",
            children: "Carpe Diem",
          })
    // Here, React.createElement is doing three main things:
    	  // 1. Specifies the type of element ("div")
    	 // 2. Adds any properties to that element (like className)
      // 3. Sets the children of that element ("Carpe Diem")
    ```
    
    Now what is the difference between element created using `document.createElement` and element created using `React.createElement`
    
    - **DOM Elements**: **`document.createElement`** directly creates and manipulates actual DOM elements,
    
    ```jsx
    const element = document.createElement("div")
    console.log(element)
    ```
    
    - When you use **`document.createElement('div')`**, for example, it creates a **`<div>`** element that can be added to your webpage.
    - After creating an element, you manually set its attributes, like **`id`**, **`class`**, etc., and then append it to the document. For example, you can add text to this **`div`**, style it, and then insert it into the DOM.
    - This approach involves directly changing the structure of your webpage's HTML through script
    
    - **React Elements**: **`React.createElement`** creates objects representing DOM elements which are later translated into actual DOM updates by React.
    
    ```jsx
    const element = React.createElement("div", {
            className: "quote",
            children: "Carpe Diem",
          })
    console.log(element)
    ```
    
    - When you use **`React.createElement('div',** { className: "quote", children: "Carpe Diem"}**)**`, it doesn’t create an actual DOM element right away. Instead, it creates a React element, which is a lightweight description of what the DOM element should look like.
    - This React element created is then given to `ReactDOM` ’s `render` method. which takes the responsibility of converting this React Element to Actual DOM element and display it to DOM. ( we will see this in the next point )
3. **`ReactDOM` and `ReactDOM.render` :** 
Now, what do you do with this React element? This is where **`ReactDOM`** comes into play.
**`ReactDOM`** is like a bridge between React elements and actual DOM elements. Its job is to take the React elements and turn them into real DOM elements that get rendered on the page.

Define a location in your HTML (like a div with an ID of "root") where your React application will be attached.
    
    ```jsx
    const reactRoot = ReactDOM.createRoot(document.getElementById("root"))
    reactRoot.render(element)
    ```
    
    Here, **`ReactDOM.createRoot()`** creates a root node where your React elements will live. **`reactRoot.render(element)`** then takes the React element and transforms it into a real DOM element, finally attaching it to the **`root`** div in your HTML.
    
    ```jsx
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <style>
          .quote {
            color: teal;
            font-size: 48px;
          }
        </style>
        <title>Create UI with React API</title>
      </head>
      <body>
        <div id="root"></div>
    			// 1. Add react and react-dom scripts
        <script src="https://www.unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
        <script src="https://www.unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
        <script>
    
    			// 2. **React and React.createElement**
          const element = React.createElement("div", {
            className: "quote",
            children: "Carpe Diem",
          })
    
    			// 3. **ReactDOM and ReactDOM.render**
          const reactRoot = ReactDOM.createRoot(document.getElementById("root"))
          reactRoot.render(element)
        </script>
      </body>
    </html>
    ```
    

**In a nutshell :** 

- **`React`** provides a powerful and flexible way to describe what the UI should look like.
- **`ReactDOM`** makes it easy to render and update the described UI in the actual DOM.
- You're still leveraging the power of the DOM, but in an optimized way. You avoid direct, costly manipulations to the DOM. ( We will talk about this in future in detail )

### Task ( 3 Minutes ) :

Your task is to create a p element with text "Seize the day" and display it to DOM using React and ReactDOM

```jsx
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
  <script>
	    // Your task is to create a p element with text "Seize the day" and display it to DOM using React and ReactDOM
  </script>
</html>
```

Solution : 

Ref : [https://github.com/abduljabbarpeer/fe-react/tree/main/react-4/example-1](https://github.com/abduljabbarpeer/fe-react/tree/main/react-4/example-1)

```jsx
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
  <script>
    // Your task is to create a p element with text "Seize the day" and display it to DOM using React and ReactDOM
    // React element created
    const element = React.createElement("p", {
      children: "Seize the day",
    });

    // React element rendered;
    const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
    reactRoot.render(element);
  </script>
</html>
```