# More about JSX - Interpolation, Props, Attributes, Events and More

Serial: 4
Made for: Beginner
Requirement: Must Have
Time in minutes: 30
Learning Objectives: Babel, JSX
doc-id: react-4

### More About JSX :

Two tools that can be very handy when you are starting out : 

1. Use [Babel Try It Out Page](https://babeljs.io/repl#?browsers=defaults%2C%20not%20ie%2011%2C%20not%20ie_mob%2011&build=&builtIns=false&corejs=3.21&spec=false&loose=false&code_lz=MYewdgzgLgBAtgTwCoFMAesC8MBEBhAQwCcAHFGAEQEsU4cBuAKFElhQBtaUwsYAeACZUAbgD4A3olQYAvnwD0QsfSA&debug=false&forceAllTransforms=false&modules=false&shippedProposals=false&circleciRepo=&evaluate=false&fileSize=false&timeTravel=false&sourceType=module&lineWrap=true&presets=env%2Creact&prettier=true&targets=&version=7.23.6&externalPlugins=&assumptions=%7B%7D) to see how JSX is converted to Non JSX Code ( JS Code ) that your browser can understand by using babel. 
2. This [HTML TO JSX tool](https://transform.tools/html-to-jsx) converts your HTML Code to JSX. 

1. You can add properties and attributes in JSX similar to how you’d add properties and attributes to HTML elements.   

```jsx
const element = (
        <p id="quote" className="message">
          Carpe Diem
        </p>
      );
```

```jsx
// The same code gets transpiled/converted by babel like this in browser
const element = React.createElement(
  "p",
  {
    id: "quote",
    className: "message"
  },
  "Carpe Diem"
);
```

1. **Interpolation** is your friend : 
    1.  ****You can add in any javascript variable directly into your JSX. For example 
        
        
        ```jsx
        const myText = "Carpe Diem";
        const element = <div>{myText}</div>;
        ```
        
        ```jsx
        // The same code gets transpiled/converted by babel like this in browser
        const myText = "Carpe Diem";
        const element = React.createElement("div", null, myText);
        ```
        
    2. Props Too ! : Want to make your HTML classes dynamic ? Here's how :
        
        
        ```jsx
        const myClassName = "message";
        const myText = "Carpe Diem";
        const element = <div className={myClassName}>{myText}</div>;
        ```
        
        ```jsx
        // The same code gets transpiled/converted by babel like this in browser
        const myClassName = "message";
        const myText = "Carpe Diem";
        const element = React.createElement(
          "div",
          {
            className: myClassName
          },
          myText
        );
        ```
        
2. Self-Closing Tags are also acceptable in JSX. In some cases it’s mandatory like for an img.
    
    
    ```jsx
    const element = (
            <img src="https://placehold.co/400" alt="some placeholder image" />
          );
    ```
    
    ```jsx
    const element = React.createElement("img", {
      src: "https://placehold.co/400",
      alt: "some placeholder image"
    });
    ```
    
3. **Event Handlers in JSX :** 
    
    
    ```jsx
    const alertFunc = () => {
      alert("Button Clicked!");
    };
    const element = <button onClick={alertFunc}>Click Me</button>;
    ```
    
    - The **`onClick`** attribute is an event handler. It tells React to listen for a click event on this button. When the button is clicked, the **`alertFunc`** function will be called.
    - **`alert("Button Clicked!")`** displays a pop-up message box with the text "Button Clicked!".
    - In React, we often define functions to handle events like clicks, mouse movements, form submissions, etc. These functions define what should happen when the event occurs. These functions are called event handlers. Remember you have similar thing in javascript `button.addEventListener('click', alertFunc)`
    
    ```jsx
    const alertFunc = () => {
      alert("Button Clicked!");
    };
    const element = React.createElement(
      "button",
      {
        onClick: alertFunc
      },
      "Click Me"
    );
    ```
    
4. **Properties/Attributes and Spread Operator** `{...}` :
This one's cool. Make an object with all the props you want, and then just spread 'em
    
    
    ```jsx
    const alertFunc = () => {
      alert("Button Clicked!");
    };
    const buttonClassName = "button";
    const buttonId = "click-button";
    
    const props = {
      className: buttonClassName,
      id: buttonId,
      onClick: alertFunc,
    };
    
    const element = <button {...props}>Click Me</button>;
    ```
    
    ```jsx
    const alertFunc = () => {
      alert("Button Clicked!");
    };
    const buttonClassName = "button";
    const buttonId = "click-button";
    const props = {
      className: buttonClassName,
      id: buttonId,
      onClick: alertFunc
    };
    const element = React.createElement("button", props, "Click Me");
    ```
    
5. Rendering Multiple elements in JSX : 
    
    Try this below code and see what happens. why you can't put two React elements next to each other like this ?
    
    ```jsx
      <body>
        <div id="root"></div>
        <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
        <script src="https://www.unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
        <script src="https://www.unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
        <script type="text/babel">
    
          const element = ( // why you can't put two React elements next to each other like this ?
              <span>Carpe</span>
              <span>Diem</span>
          )
    
          const reactRoot = ReactDOM.createRoot(document.getElementById("root"))
    
          reactRoot.render(element)
        </script>
      </body>
    </html>
    ```
    
    You usually have to wrap them inside another element like a `<div>` and then it’ll work
    
    ```jsx
     <body>
        <div id="root"></div>
        <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
        <script src="https://www.unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
        <script src="https://www.unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
        <script type="text/babel">
    
          const element = (
            <div>
              <span>Carpe</span>
              <span>Diem</span>
            </div>
          )
    
          const reactRoot = ReactDOM.createRoot(document.getElementById("root"))
    
          reactRoot.render(element)
        </script>
      </body>
    </html>
    ```
    

Try putting the code even in a babel try out page and you’ll encounter this error

![Screenshot 2023-12-21 at 12.52.08 PM.png](More%20about%20JSX%20-%20Interpolation,%20Props,%20Attributes,%2089c6132169594717b888d238513bdd5e/Screenshot_2023-12-21_at_12.52.08_PM.png)

This JSX basically boils down to `React.createElement` code so let’s go back to that.

a. **Making A Single Element**: Normally, you create React elements with `React.createElement`. But I need one main element to be rendered. reactRoot.render accepts one element.

```jsx
<script type="text/babel">
    const carpeElement = React.createElement('span', null, 'Carpe');
		const diemElement = React.createElement('span', null, 'Diem');

    const reactRoot = ReactDOM.createRoot(document.getElementById("root"))
    reactRoot.render( /********** I CAN ONLY KEEP ONE ELEMENT HERE ********/ )
</script>
```

b. **The Side-By-Side Issue**: With `React.createElement`, placing two elements side by side is tough. So you might end up creating a wrapper element with using a div or some other HTML tag

```jsx
 <script type="text/babel">
    const carpeElement = React.createElement('span', null, 'Carpe');
		const diemElement = React.createElement('span', null, 'Diem');

		const wrapperElement = React.createElement('div', null, carpeElement, diemElement)

    const reactRoot = ReactDOM.createRoot(document.getElementById("root"))
    reactRoot.render(wrapperElement) // this wrapper element has all the elements required inside it as children
</script>
```

c. The same above thing if you write in JSX

```jsx
const carpeElement = <span>Carpe</span>;
const diemElement = <span>Diem</span>;
const wrapperElement = (
  <div>
    {carpeElement}
    {diemElement}
  </div>
);
const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
reactRoot.render(wrapperElement);
```

d. **Introducing Fragments**: Enter React Fragments, a solution to keep things clean.

```jsx
const carpeElement = <span>Carpe</span>;
      const diemElement = <span>Diem</span>;

      const wrapperElement = (
        <React.Fragment>
          <span>Carpe</span>
          <span>Diem</span>
        </React.Fragment>
      );
      const reactRoot = ReactDOM.createRoot(document.getElementById("root"));

      reactRoot.render(wrapperElement);
```

```jsx
const carpeElement = React.createElement("span", null, "Carpe");
const diemElement = React.createElement("span", null, "Diem");

const wrapperElement = React.createElement(
  React.Fragment,
  null,
  carpeElement,
  diemElement
);
const reactRoot = ReactDOM.createRoot(document.getElementById("root"));

reactRoot.render(wrapperElement); // this wrapper element has all the elements required inside it as children
```

Think of a React Fragment as a container that doesn't mess with your DOM structure. With this you have the wrapper but at the same time no additional divs are created. This Same fragment can also be written as `<></>` in JSX

```jsx
const carpeElement = <span>Carpe</span>;
const diemElement = <span>Diem</span>;

const wrapperElement = (
  <> // This is React Fragment for lazy coders; Just as effective, but way simpler. 
    <span>Carpe</span>
    <span>Diem</span>
  </>
);
const reactRoot = ReactDOM.createRoot(document.getElementById("root"));

reactRoot.render(wrapperElement);
```

1. **Inline styling in React** : 
    
    React allows you to use a `style` attribute to add inline styles directly to your JSX elements.
    
    Here's how you can do it:
    
    ```jsx
    <div style={{ color: "red" }}>
    ```
    
    The `style` attribute accepts an object where the keys are camelCased versions of the CSS property names, and the values are CSS values as strings.
    
    Here’s a box styled completely inline as an example:
    
    ```jsx
    const carpeElement = <span>Carpe</span>;
    const diemElement = <span>Diem</span>;
    
    const element = (
      <div
        style={{
          margin: "20px",
          padding: "20px",
          border: "1px solid cyan",
          color: "darkcyan",
          backgroundColor: "lightcyan",
        }}
      >
        Here is a box with styling done using inline styling
      </div>
    );
    const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
    
    reactRoot.render(element);
    ```
    
    📌 **When to use Inline Styling?**
    
    - When you want to dynamically set styles.
    - For one-off unique styles that don't make sense to put in a CSS class.
    
    ---
    
    Task : Create a React element using JSX which has the following 
    
    - It should be wrapped using React Fragment
    - Inside this fragment; There should be
        - a `p` element with text “React is a javascript library”
        - a `div` element which should have class `“main”` . This `div` should contain the following
            - A `p` element which says “click the below button to alert `Hello`
            - A button with text “Alert Hello” . Clicking on which an alert pops up with the same message