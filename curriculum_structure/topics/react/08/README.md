# How React updates the DOM efficiently ( Virtual DOM )

Serial: 9
Made for: Beginner
Requirement: Must Have
Time in minutes: 25
Learning Objectives: React Basics, Virtual DOM
doc-id: react-9

To appreciate the efficiency of React in updating the DOM, let's compare building a digital clock application using vanilla JavaScript and React.

Clock built with Vanilla Javascript

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Clock with JS / DOM</title>
  </head>
  <body>
    <div id="root"></div>
    <script>
      let rootElement = document.getElementById("root")

      function tick() {
        const time = new Date().toLocaleTimeString()
        rootElement.innerHTML = `
          <h1>Digital Clock With vanilla javascript</h1>
          <h2>${time}</h2>
        `
      }

      // Let's update the clock every 1 second!
      setInterval(tick, 1000)
    </script>
  </body>
</html>
```

Clock with react

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <style>
      .container {
        margin: 10px;
        color: teal;
      }
    </style>
    <title>Clock using React</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://www.unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
    <script src="https://www.unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
    <script type="text/babel">
      const rootElement = document.getElementById("root")
      const reactRoot = ReactDOM.createRoot(rootElement)

      function tick() {
        const time = new Date().toLocaleTimeString()
        const element = (
          <>
            <h1>Digital Clock With React</h1>
            <h2>{time}</h2>
          </>
        )
        reactRoot.render(element)
      }

      // Let's update the clock every 1 second!
      setInterval(tick, 1000)
    </script>
  </body>
</html>
```

**Observation** : 

1. **Vanilla JavaScript Approach**: Every second, the entire HTML content within the **`rootElement`** is replaced, even if only a small part, like the time, changes. 
2. **React Approach**: React updates only the necessary parts of the DOM. For instance, it only changes the time string without re-rendering the entire clock component.

Let’s make one another change to these above examples to understand how it impacts user experience.you’d notice that in vanilla javascript piece, any focused input will lose its focus every second, which is super annoying. React is smarter; it only updates what's necessary, keeping all your interactions intact.

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Clock with JS / DOM</title>
  </head>
  <body>
    <div id="root"></div>
    <script>
      let rootElement = document.getElementById("root")

      function tick() {
        const time = new Date().toLocaleTimeString()
        rootElement.innerHTML = `
          <h1>Digital Clock With vanilla javascript</h1>
          <input type="text" value="focus on this input" />
          <h2>${time}</h2>
        `
      }

      // Let's update the clock every 1 second!
      setInterval(tick, 1000)
    </script>
  </body>
</html>
```

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <style>
      .container {
        margin: 10px;
        color: teal;
      }
    </style>
    <title>Clock using React</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://www.unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
    <script src="https://www.unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
    <script type="text/babel">
      const rootElement = document.getElementById("root")
      const reactRoot = ReactDOM.createRoot(rootElement)

      function tick() {
        const time = new Date().toLocaleTimeString()
        const element = (
          <>
            <h1>Digital Clock With React</h1>
            <input type="text" value="focus on this input" />
            <h2>{time}</h2>
          </>
        )
        reactRoot.render(element)
      }

      // Let's update the clock every 1 second!
      setInterval(tick, 1000)
    </script>
  </body>
</html>
```

1. **Vanilla JavaScript Approach**: : Every second, the entire HTML content within the **`rootElement`** is replaced, even if only a small part, like the time, changes. This can disrupt user interactions, such as losing focus on an input field.
2. **React Approach**: React updates only the necessary parts of the DOM. For instance, it only changes the time string without re-rendering the entire clock component. Hence the input focus remained intact

# **Virtual DOM :**

React's efficiency stems from its use of the Virtual DOM. Here's how it works:

**What is the Virtual DOM?** 
The Virtual DOM is a lightweight copy of the actual DOM. It's a virtual representation of the UI components.

**How Does React Use the Virtual DOM?** 
When there's a change in the UI, React first updates the Virtual DOM. Then, it compares (or "diffs") the updated Virtual DOM with a snapshot taken right before the update. This process is known as "reconciliation."

**Efficient Updates**: 
React identifies what exactly changed in the Virtual DOM. It then updates only those specific parts in the actual DOM. This selective updating avoids unnecessary re-renders, enhancing performance.

**The Benefits:**

1. **Performance**: React reduces the workload on the browser by avoiding needless DOM manipulations, resulting in faster applications.
2. **User Experience**: React's targeted updates improve accessibility and user experience, such as maintaining focus on an input field, as shown in our clock example.

**Conclusion:**

React's smart DOM update mechanism, powered by the Virtual DOM, makes it a powerful tool for developing efficient and user-friendly web applications.

---