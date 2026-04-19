# Labels and Inputs for inputs

Serial: 16
Made for: Beginner
Requirement: Good to Have
Time in minutes: 10
Learning Objectives: State Management, useState
doc-id: react-16

It’s recommended that you always tie your input with label for better accessibility. It’s done with `htmlFor` on label and `id` on input.

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>State Management and useState : Controlled component</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://www.unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
    <script src="https://www.unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
    <script type="text/babel">
      const rootElement = document.getElementById("root")
      const reactRoot = ReactDOM.createRoot(rootElement)

      function App() {
        const [message, setMessage] = React.useState("")

        const handleChange = (event) => {
          setMessage(event.target.value)
        }

        const handleReset = () => {
          setMessage("")
        }

        return (
          <div>
            <p>
              Message : <strong>{message}</strong>
            </p>
            <label htmlFor="message-input"></label>
            <input
              id="message-input"
              placeholder="Add your message here"
              onChange={handleChange}
              value={message}
            />
            <br />
            <button onClick={handleReset}>Reset</button>
          </div>
        )
      }

      reactRoot.render(<App />)
    </script>
  </body>
</html>
```