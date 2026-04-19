# State Mangement II - Handling multiple states in a component

Serial: 12
Made for: Beginner
Requirement: Must Have
Time in minutes: 10
Learning Objectives: State Management, useState
doc-id: react-12

# Handling Multiple States :

You can use multiple `useState` calls to manage different state variables within the same component.

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>react-10 | example-2</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://www.unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
    <script src="https://www.unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
    <script type="text/babel">
      function App() {
        const [count1, setCount1] = React.useState(0);
        const [count2, setCount2] = React.useState(0);

        const incrementCount1 = () => {
          setCount1(count1 + 1);
        };

        const incrementCount2 = () => {
          setCount2(count2 + 1);
        };

        return (
          <div>
            <p>Button 1 is clicked {count1} times</p>
            <button onClick={incrementCount1}>Button 1</button>
            <p>Button 2 is clicked {count2} times</p>
            <button onClick={incrementCount2}>Button 2</button>
          </div>
        );
      }

      const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
      reactRoot.render(<App />);
    </script>
  </body>
</html>
```

- Two state variables `count1` and `count2`are being maintained here.
- `setCount1` is the state updater function for `count1`
- `setCount2` is the state updater function for `count2`
- You can observer we can maintain multiple instances of count using `useState` hook and each of this count will not have an impact on the other one