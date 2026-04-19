# Module CSS

Serial: 23
Made for: Beginner
Requirement: Must Have
Time in minutes: 20
Learning Objectives: Styling in React
doc-id: react-23

### The Problem with Global CSS

In a typical React app, you might have a global CSS file that styles your components. The issue here is that CSS is, well, global. If you use the same class name in different components, the styles can clash, causing unexpected behavior.

**Example with Global CSS :**

In this example, both `App.css` and `Greetings.css` have a `.title` class. The `Greetings` component's `.title` class will override the `.title` class in `App.css`, causing a conflict.

```jsx
.
├── README.md
├── index.html
├── src
│   ├── App.css
│   ├── App.jsx
│   ├── components
│   │   ├── Greetings.css
│   │   └── Greetings.jsx
```

```jsx
// App.jsx
import "./App.css"
import Greetings from "./components/Greetings"

export default function App() {
  return (
    <div>
      <p className="title"> Some other text in app component</p>
      <Greetings />
    </div>
  )
}
```

```jsx
// App.css
.title {
  color: green;
  font-size: 48px;
}
```

```jsx
// src/components/Greetings.jsx
import "./Greetings.css"

function Greetings() {
  return (
    <div>
      <p>Some other lorem ipsum text in greetings component</p>
      <p className="title">Hello People</p>
    </div>
  )
}

export default Greetings
```

```jsx
// src/components/Greetings.css
.title {
  color: blue;
  font-size: 24px;
}
```

---

### The Solution: Module CSS

Module CSS scopes your CSS to the component level. This means the styles you define in a `module.css` file will only apply to the component that imports it.

**Example with Module CSS :** In this example, the `.title` class in `Greetings.module.css` is scoped to the `Greetings` component. It won't interfere with the `.title` class in `App.css`.

1. **Rename your CSS file**: Change the extension to `.module.css`. For example, `Greetings.css` becomes `Greetings.module.css`.
2. **Import with a specific syntax**:
    
    ```jsx
    import styles from './Greetings.module.css';
    
    ```
    
    This `styles` object now holds all your class names as properties.
    
3. **Use it in JSX**:
    
    ```jsx
    <p className={styles.title}>Hello People</p>
    
    ```
    
    Here, `styles.title` refers to the `.title` class in `Greetings.module.css`.
    

### Why is this Awesome?

1. **No More Clashes**: Each component has its own scope, so no more worrying about overriding styles.
2. **Code Splitting**: Since the styles are scoped to the component, they can be loaded on demand, making your app faster.
3. **Better Maintainability**: It's easier to know which styles apply to which component, making your codebase easier to understand and maintain.

```jsx
.
├── README.md
├── index.html
├── src
│   ├── App.css
│   ├── App.jsx
│   ├── components
│   │   ├── Greetings.module.css
│   │   └── Greetings.jsx
```

```jsx
import "./App.css"
import Greetings from "./components/Greetings"

export default function App() {
  return (
    <div>
      <p className="title"> Some other text in app component</p>
      <Greetings />
    </div>
  )
}
```

```jsx
.title {
  color: green;
  font-size: 48px;
}
```

```jsx
import styles from "./Greetings.module.css"

function Greetings() {
  return (
    <div>
      <p>Some other lorem ipsum text in greetings component</p>
      <p className={styles.title}>Hello People</p>
    </div>
  )
}

export default Greetings
```

```jsx
.title {
  color: blue;
  font-size: 24px;
}
```

**In a nutshell :**

- Global CSS is, well, global. It can cause clashes.
- Module CSS scopes your styles to the component, preventing these clashes.
- To use Module CSS, rename your file to `.module.css`, import it using a specific syntax, and then use it in your JSX.