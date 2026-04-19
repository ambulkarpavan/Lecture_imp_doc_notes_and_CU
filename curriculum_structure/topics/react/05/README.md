# Components and Props - Basics

Serial: 5
Made for: Beginner
Requirement: Must Have
Time in minutes: 25
Learning Objectives: Components
doc-id: react-5

- Components
- Props
    - Passing different data types like string, number, arrays, objects, functions as props
    - children props ( Passing JSX )

# Components :

React is a JavaScript library for rendering user interfaces (UI). UI is built from small units like buttons, text, and images. React lets you combine them into reusable, nestable components.  From web sites to phone apps, everything on the screen can be broken down into components.

React applications are built from isolated pieces of UI called *components*. A React component is a JavaScript function that you can sprinkle with markup. Components can be as small as a button, or as large as an entire page. 

Okay; Let’s say you have to prepare a birthday card element which display “Happy Birthday” Message multiple times. 

**The Traditional Method**: Let's say you want to display the same message twice on a page. You might do this:

```jsx
const element = (
  <>
    <p>Happy Birthday!</p>
    <p>Happy Birthday!</p>
  </>
);
const reactRoot = ReactDOM.createRoot(document.getElementById("root"));

reactRoot.render(element);
```

**With a Constant**: To make it a tad cleaner, you could store the message in a constant:

```jsx
const message = <p>Happy Birthday!</p>
const element = (
  <>
    {message}
    {message}
  </>
);
```

### Use Functions for Flexibility

Okay, so far so good. But what if you want two different messages, huh?

Let’s say, greeting text can be a variable; name can be another variable.

**Using Functions**: Functions are your friends here. Check this out:

```jsx
function greet({ text, name }) {
  return (
    <p>
      {text}, {name}
    </p>
  );
}

const element = (
  <div className="container">
    {greet({ text: "Happy Birthday", name: "Bruce" })}
    {greet({ text: "Good Morning", name: "Rachel" })}
  </div>
);

const reactRoot = ReactDOM.createRoot(document.getElementById("root"));

reactRoot.render(element);
```

This is how it’ll look when you inspect it using devtools. 

![Screenshot 2023-12-21 at 3.23.50 PM.png](Components%20and%20Props%20-%20Basics%2092efc18921cf4d0d85e14edf1b0ed1fd/Screenshot_2023-12-21_at_3.23.50_PM.png)

This very same thing can be written in a more cleaner syntax like the one below. Notice how `Greet` is written with Capital Letter

```jsx
function Greet({ text, name }) { // First Change
  return (
    <p>
      {text}, {name}
    </p>
  );
}

const element = (
  <div className="container">
    <Greet text="Happy Birthday" name="Bruce" /> // Second Change; Props are discussed in detail below 
    <Greet text="Good Morning" name="Rachel" />
  </div>
);
const reactRoot = ReactDOM.createRoot(document.getElementById("root"));

reactRoot.render(element);
```

- So now this `Greet` is a component. It’s a reusable piece of UI meaning it can be used multiple time as and when required ( Pretty similar to how a function works and that is exactly what a component is; A function which maintains a piece of UI including styling, functionality etc ). Essentially you entire react is nothing but a bunch of components.

and if you check console now ( Does look like a react component )

![Screenshot 2023-12-21 at 3.30.14 PM.png](Components%20and%20Props%20-%20Basics%2092efc18921cf4d0d85e14edf1b0ed1fd/Screenshot_2023-12-21_at_3.30.14_PM.png)

---

Some important pointer wrt components : 

1. In React, Components are basically reusable piece of code that serve the same purpose as JavaScript functions, They work in isolation and return HTML via a render function. For example, The above function `Greet` is a component. Wherever you put `<Greet text="Happy Birthday" name="Bruce" />` ; It displays that message with that name. 
2. Why components ? 
    
    They let you split the UI into independent, reusable pieces to think about each piece in isolation. They make our code cleaner and easier to understand. Plus, you can use them again and again.
    
3. **Name Matters**: Capitalize your component names. It's not just good manners; it's how React knows you're creating a component.
4. **Nesting Components** : Components can be used inside other components. In the below code, you can see the component `App` has two components `Greet` inside
    
    ```jsx
    function Greet({ text, name }) {
      return (
        <p>
          {text}, {name}
        </p>
      );
    }
    
    function App() {
      return (
        <div className="container">
          <Greet text="Happy Birthday" name="Bruce" />
          <Greet text="Good Morning" name="Rachel" />
        </div>
      );
    }
    const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
    
    reactRoot.render(<App />);
    ```
    

# Props :

**Intro :**

- **Props** stand for "properties."
- They are a way of passing data from one component (usually a parent) to another (usually a child).
- Think of props like arguments you pass to a function. They let components communicate with each other.

**How Do They Work?**

1. **Passing Data**: You can pass different types of data, such as numbers, strings, arrays, objects, or even functions, as props.
2. **Read-Only**: Props are read-only. This means the component receiving props cannot modify them. Instead, it treats them like a 'constant' or an unchangeable value.
3. **One-Way Data Flow**: Props flow down from parent to child components. This makes the data flow predictable and easier to understand.

In the above example : 

- `Greet` component receives props
- `App` component is the parent, and `Greet` is the child.
- `text="Happy Birthday"` and ``name="Bruce"`` is the prop being passed to `Greet`.
- Inside `Greet`, we access the name using `[props.name](http://props.name)` or it can be directly destructured as we have done above

These props make your components flexible and maintainable. As you dive deeper into React, you'll see how props play a critical role in component interaction and data flow.

---