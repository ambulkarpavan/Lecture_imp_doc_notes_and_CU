# Why state management ?

Serial: 10
Made for: Beginner
Requirement: Must Have
Time in minutes: 30
Learning Objectives: State Management, useState
doc-id: react-10

# Event Handling in React :

React allows you to handle events like clicks, change, hover, form submissions, etc., in a way similar to handling events in regular JavaScript. However, in React, you work with a virtual DOM and use JSX syntax.

Let’s take a simple example to understand Event Handling in React by taking two different events.

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Event Handling</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://www.unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
    <script src="https://www.unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
    <script type="text/babel">
      function App() {
        // A simple function to handle click events
        function handleClick() {
          alert("Button clicked!");
        }

        // A simple function to handle input change events
        function handleInputChange(event) {
          console.log("input value is being changed", event.target.value);
        }

        // JSX returns a button with an event handler
        return (
          <>
            <button onClick={handleClick}>Click me</button>
            <input
              type="text"
              placeholder="Type here"
              onChange={handleInputChange}
            />
          </>
        );
      }

      // Render the App component into the root div
      const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
      reactRoot.render(<App />);
    </script>
  </body>
</html>
```

- App component has a button. An onClick event handler `handleClick` is attached to this button meaning whenever user clicks on this button. `handleClick` function will be invoked.
    - Event - Click Event ( `onClick`) . We use camelCasing like `onClick` , `onChange` etc here unlike HTML
    - Event Handler - `handleClick` function
- App component has an input box. An onClick event handler `handleChange` is attached to this input meaning whenever user changes something on this input box. `handleChange` function will be invoked.
    - Event - Change Event ( `onChange`) . We use camelCasing like `onClick` , `onChange` etc here unlike HTML
    - Event Handler - `handleInputChange` function
    

---

Now that you understand event handling in react. Let’s take a look at this very simple example. 
Agenda : We are trying to maintain a variable called `count` which will be displayed onto UI. Clicking on the button should increase the value of `count` and this updated value should be reflected onto DOM

TODO : Update an image explaining the behaviour of counter app we are trying to build. 

 

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Event Handling</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://www.unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
    <script src="https://www.unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
    <script type="text/babel">
      function App() {
        let count = 0;

        function handleClick() {
          count += 1;
          console.log(`Clicked ${count} times`);
        }

        return (
          <div>
            <p>You clicked {count} times</p>
            <button onClick={handleClick}>Click me</button>
          </div>
        );
      }

      // Render the App component into the root div
      const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
      reactRoot.render(<App />);
    </script>
  </body>
</html>
```

- When the `App` component first renders, `count` is set to `0`. The UI shows "You clicked 0 times".
- When you click the button, `handleClick` is called. It increments `count` and logs the new value. However, the UI still shows "You clicked 0 times".

**Expectation vs. Reality :** 

As a developer, you might expect that changing `count` would update the UI. However, these changes are not being reflected. 

Why Doesn't the UI Update ?

A simple answer - REACT doesn’t know. React has no way of knowing that `count` has changed and that it needs to update the UI. 

Let’s make some changes to the above code and see if we can fix this. 

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Managing a variable across re-renders</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://www.unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
    <script src="https://www.unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
    <script type="text/babel">
      // Initialize variable
      const state = { count: 0 };

      // Custom function to update state and re-render
      function setState(newState) {
        Object.assign(state, newState);
        renderApp();
      }

      function App() {
        function handleClick() {
          setState({ count: state.count + 1 });
          console.log(`Clicked ${state.count} times`);
        }

        return (
          <div>
            <p>You clicked {state.count} times</p>
            <button onClick={handleClick}>Click me</button>
          </div>
        );
      }

      // Render the App component into the root div
      const reactRoot = ReactDOM.createRoot(document.getElementById("root"));

      function renderApp() {
        reactRoot.render(<App />);
      }
      renderApp();
    </script>
  </body>
</html>
```

Some new variables and functions that you see here 

- `state` : Here we store the value of count in a javascript object and let’s call this object state. Now why state ? Because this information in “state” describes the current state/condition of your UI.
- `renderApp` : The `renderApp` function is responsible for rendering the `App` component. We are gonna call this function
    - Initially : It’s called inital render wherein App component is initially rendered to UI
    - `state` value changes : We will also call this function `renderApp` each time `state` value is updated.
- `setState` :  This function updates the state and then calls `renderApp` to re-render the UI with the new state.

In React, "state" refers to data or properties that need to be tracked in an application. So is there a way we can handle this “state” variable in better way . 

The answer is “Yes”. Using a hook from react called `useState` but that’s a different topic and will be discussed next. 

---

### Additional Example :

We have further modified the above example to include “input” value and manage state of input box as well.

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Managing a variable across re-renders</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://www.unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
    <script src="https://www.unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
    <script type="text/babel">
      // Initialize variable
      const state = { count: 0, message: "" };

      // Custom function to update state and re-render
      function setState(newState) {
        Object.assign(state, newState);
        renderApp();
      }

      function App() {
        function handleClick() {
          setState({ count: state.count + 1 });
          console.log(`Clicked ${state.count} times`);
        }

        const handleChange = (event) => {
          setState({ message: event.target.value });
        };

        return (
          <div>
            <p>You clicked {state.count} times</p>
            <button onClick={handleClick}>Click me</button>
            <hr />
            <input
              placeholder="Enter the message here"
              onChange={handleChange}
            />
          </div>
        );
      }

      // Render the App component into the root div
      const reactRoot = ReactDOM.createRoot(document.getElementById("root"));

      function renderApp() {
        reactRoot.render(<App />);
      }
      renderApp();
    </script>
  </body>
</html>
```