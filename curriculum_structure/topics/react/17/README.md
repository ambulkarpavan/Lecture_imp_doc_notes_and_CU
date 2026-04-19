# State upliftment

Serial: 18
Made for: Beginner
Requirement: Must Have
Time in minutes: 20
Learning Objectives: State Management, useState
doc-id: react-18

# Independant component states

### Example 1: Independent Component States

Consider a scenario where you have a button component in React. Each time this component is used, it maintains its own state.

When you use this `MyButton` component multiple times in your `App` like this. Each button keeps track of its own clicks independently. That means if you click one button, it updates its count without affecting the other.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>react-10 | example-13</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://www.unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
    <script src="https://www.unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
    <script type="text/babel">
      function MyButton() {
        const [count, setCount] = React.useState(0); // State for counting clicks

        function handleClick() {
          setCount(count + 1); // Increment count on click
        }

        return <button onClick={handleClick}>Clicked {count} times</button>;
      }

      function App() {
        return (
          <>
            <h1>Counters that update separately</h1>
            <MyButton />
            <MyButton />
          </>
        );
      }

      const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
      reactRoot.render(<App />);
    </script>
  </body>
</html>
```

Notice how each button “remembers” its own `count` state and doesn’t affect other buttons.

![Screenshot 2023-04-06 at 10.40.43 AM.png](State%20upliftment%2045e74ff3abfd42b396219b1ef8e51a7a/Screenshot_2023-04-06_at_10.40.43_AM.png)

# Shared State Between Components

### Example 2: Shared State Between Components

Sometimes, you want multiple components to share the same data. For example, if you have two buttons and want them to display the same `count` that updates together, you need a shared state.

To achieve this, you "lift the state up" to a common parent component. Here's how you do it :

Step 1 : Move the state to the parent component, `App`

Step 2 : Modify the `MyButton` component to accept props

```html
function MyButton({ count, onClick }) {
  return <button onClick={onClick}>Clicked {count} times</button>;
}

function App() {
  const [count, setCount] = React.useState(0); // Shared state

  function handleClick() {
    setCount(count + 1); // Update shared state
  }

  // Pass state and handler to children
  return (
    <div>
      <h1>Counters that update together</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}

const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
reactRoot.render(<App />);
```

In this setup, `App` holds the state (`count`) and manages the click handler (`handleClick`). Both buttons receive the count and the handler as props. When a button is clicked, it uses the shared handler from `App`, updating the `count` for both buttons simultaneously.

![Screenshot 2023-04-06 at 10.40.57 AM.png](State%20upliftment%2045e74ff3abfd42b396219b1ef8e51a7a/Screenshot_2023-04-06_at_10.40.57_AM.png)

This kind of ***Lifting State Up***  technique or simply called ***State upliftment*** is a technique to share state between multiple components by moving it to their common parent.

Remember, each component should be responsible for its own state, but when you need to share data across components, lifting the state up is a clean and effective solution.