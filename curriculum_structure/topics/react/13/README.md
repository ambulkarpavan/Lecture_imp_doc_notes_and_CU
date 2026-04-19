# React - Controlled and uncontrolled components

Serial: 14
Made for: Beginner
Requirement: Good to Have
Time in minutes: 15
Learning Objectives: State Management, useState
doc-id: react-14

Let’s take this very simple example :

```jsx
function App() {
  const [message, setMessage] = React.useState("");

  const handleChange = (event) => {
    setMessage(event.target.value);
    // event --> change event;
    // event target --> input box;
    // event target value --> whatever is currently avail
  };

  return (
    <div>
      <p>
        Message : <strong>{message}</strong>
      </p>
      <input placeholder="Add your message here" onChange={handleChange} />
    </div>
  );
}

const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
reactRoot.render(<App />);
```

While the code seems to have worked. But that is not the common convention as React like to take more control and with the above code. It doesn’t have complete control over input element. 

Lemme try and explain it this way

Let's consider a scenario where you have a form reset button to clear the input field. We shall discuss this below

```jsx
function App() {
  const [message, setMessage] = React.useState("");

  const handleChange = (event) => {
    setMessage(event.target.value);
  };

  const handleReset = () => {
    setMessage("");
  };

  return (
    <div>
      <p>
        Message : <strong>{message}</strong>
      </p>
      <input placeholder="Add your message here" onChange={handleChange} />
      <button onClick={handleReset}>Reset</button>
    </div>
  );
}

const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
reactRoot.render(<App />);
```

Here’s how it could look with an uncontrolled input (without the `value` attribute) 

In this uncontrolled version, clicking the reset button will update the `message` state to an empty string, but it won't clear the input field. The DOM is managing the input field’s value independently of React.

```jsx
function App() {
  const [message, setMessage] = React.useState("");

  const handleChange = (event) => {
    setMessage(event.target.value);
  };

  const handleReset = () => {
    setMessage("");
  };

  return (
    <div>
      <p>
        Message : <strong>{message}</strong>
      </p>
      <input
        placeholder="Add your message here"
        onChange={handleChange}
        value={message}
      />
      <button onClick={handleReset}>Reset</button>
    </div>
  );
}

const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
reactRoot.render(<App />);
```

Now, let’s modify the code to have a controlled input (with the `value` attribute)

In this controlled version, clicking the reset button will clear both the `message` state and the input field. The input field's value is always in sync with the `message` state, making the reset functionality work as expected. This demonstrates a situation where a controlled component (second approach) maintains desired functionality, whereas an uncontrolled component (first approach) does not.