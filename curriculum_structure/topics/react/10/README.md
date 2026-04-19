# State management - The useState hook

Serial: 11
Made for: Beginner
Requirement: Must Have
Time in minutes: 15
Learning Objectives: State Management, useState
doc-id: react-11

# Introduction **:**

Modern user interfaces are interactive and responsive to user actions like clicking a button or entering text. In React, the concept of "state" is crucial for managing this interactivity. State refers to the data that changes over time in your application. React provides a powerful tool called "hooks" for managing this state, with the `useState` hook being the most fundamental.

# The `useState` Hook :

`useState` is a built-in React hook that allows you to add React state to function components. It lets you initialize a state variable and provides a function to update this state. When the state changes, React re-renders the component to reflect the update.

# Building a Counter App using `useState` hook :

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>State Management and useState</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://www.unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
    <script src="https://www.unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
    <script type="text/babel">
      function App() {
        const stateArray = React.useState(0);
        const count = stateArray[0];
        const setCount = stateArray[1];

        const handleClick = () => {
          setCount(count + 1);
        };

        return (
          <div>
            <p>Button is clicked {count} times</p>
            <button onClick={handleClick}>Click Me</button>
          </div>
        );
      }

      const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
      reactRoot.render(<App />);
    </script>
  </body>
</html>
```

Destructuring the array returned from `useState` hook directly. 

```jsx
function App() {
  const [count, setCount] = React.useState(0);

  const handleClick = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <p>Button is clicked {count} times</p>
      <button onClick={handleClick}>Click Me</button>
    </div>
  );
}

const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
reactRoot.render(<App />);
```

1. `count` is our state variable
2. `setCount` is a function which will update the value of `count`; Whenever `setCount` function is called and the updated value of `count` is passed inside `setCount`. Two things happen
    1. The value of `count` changes
    2. The `App` component re-renders.
3. The value that you are passing inside `useState` is the initial value of `count`

In this code you can observe that `useState` returns a stateArray which has

1. `count` in index 0
2. `setCount` in index 1

Generally speaking this same array can be destructed and be rewriiten as

```jsx
const stateArray = React.useState(0);
const count = stateArray[0];
const setCount = stateArray[1];
```

```jsx
const [count, setCount] = React.useState(0);
```