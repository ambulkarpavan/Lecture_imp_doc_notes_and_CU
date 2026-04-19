# Controlled components in React

Serial: 13
Made for: Beginner
Requirement: Must Have
Time in minutes: 10
Learning Objectives: State Management, useState
doc-id: react-13

Controlled components are React components that control the form elements within them. The form data is handled by the state within the component.

Here's an example of a controlled input field :

```jsx
function App() {
  const [message, setMessage] = React.useState(""); // State for input value

  const handleChange = (event) => {
    setMessage(event.target.value); // Update state based on input
  };

  return (
    <div>
      <input
        value={message}
        onChange={handleChange}
        placeholder="Type a message"
      />
      <p>Your message: {message}</p>
    </div>
  );
}

```