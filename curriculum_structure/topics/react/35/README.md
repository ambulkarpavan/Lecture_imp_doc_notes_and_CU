# useRef - I ( Basics )

Serial: 35
Made for: Beginner
Requirement: Must Have
Time in minutes: 30
Learning Objectives: ref and useRef
Related back to React: useRef - II ( Intermediate ) (useRef%20-%20II%20(%20Intermediate%20)%20e862c25b7d024f419c6dc46e4cee3dd7.md)
doc-id: react-35

# Introduction :

### What is `useRef`?

`useRef` is a React Hook that allows you to reference a value that doesn't trigger a re-render when changed. Think of it as a "box" where you can keep a value safe and sound, and you can peek into it whenever you want without causing any commotion in your component.

### Basic Syntax

Here's how you declare a ref :

```jsx
const myRef = useRef(initialValue); 
// This useRef returns { current: initialValue }
```

### Parameters

`initialValue`: The value you want the ref object’s current property to be initially. It can be a value of any type. This argument is ignored after the initial render.

### Returns

- `useRef` returns an object with a single property:
- `current` : Initially, it’s set to the initialValue you have passed. You can later set it to something else. If you pass the ref object to React as a ref attribute to a JSX node, React will set its current property.

On the next renders, useRef will return the same object. You can change its current property to store information and read it later. This might remind you of state, but there is an important difference. This is discussed in the next section. 

# useRef Vs useState :

### Why not just use `useState`?

Great question! The main difference between `useState` and `useRef` is that `useState` will cause your component to re-render when the state changes. `useRef` doesn't do that. It's like a silent ninja, keeping your value safe without making a fuss.

Let’s understand with simpler example the working of `useRef` along with `useState`

```jsx
import { useState } from "react";

// useState remembers value though re-renders but
// but it triggers re-renders

const ButtonWithUseState = () => {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(count + 1);
  };

  console.log("ButtonWithUseState rendering...");
  return (
    <div>
      <h1>Count : {count}</h1>
      <button onClick={handleClick}>BUTTON WITH USE STATE</button>
    </div>
  );
};

export default ButtonWithUseState;
```

```jsx
import { useState, useRef } from "react";

// useRef also remembers value through re-renders;
// but does not trigger re-renders

const ButtonWithUseRef = () => {
  let ref = useRef(0);
  const [flag, setFlag] = useState(false);

  const handleClick = () => {
    ref.current = ref.current + 1;
    console.log(ref);
  };

  console.log("ButtonWithUseRef rendering...");
  return (
    <div>
      <h1>Count : {ref.current}</h1>
      <button onClick={handleClick}>BUTTON WITH USEREF</button>
      <br />
      <br />
      <button onClick={() => setFlag(!flag)}>{flag ? "TRUE" : "FALSE"}</button>
    </div>
  );
};

export default ButtonWithUseRef;
```

In this example, `ref.current` holds the count value. When you click the button, `handleClick` updates `ref.current`, but it doesn't cause a re-render. This is useful when you want to keep track of a value without affecting the component's performance.

**Some Observations :** 

| useState | useRef |
| --- | --- |
| Value persists through re-renders | Value persists through re-renders |
| Changing the value triggers a re-render | Changing the value does not trigger a re-render |
| Perfect for storing information that is required for UI

Example : Say you want to display count or some data. Storing that data in useState makes more sense. Reason being when this value changes, the component re-renders and in browser you’ll the latest value being updated | Perfect for storing information that is not required directly for UI

Example : Maybe some intervalId you have to store . or some subscriptionId or some other id you want to store. This value persists through re-renders and you might be needing to cleanup stuff during unmount/updates.  |
| Syntax  :  

Initial Declaration : let someRef = useRef( initialValue )

Return value someRef : { current: initialValue }
It returns an object with key “current” and value will be the initialValue that you passed inside ref
 | Syntax :

Initial Declaration : let someState = useState( initialValue )

Return value someState : [ state, setState ]
It returns an array with two values. state whose value will be the initalValue and setState which is a function which updates state value
 |
| Immutable - one must use the state setting function to modify state variable | Mutable : you can modify the current property manually |

# useRef - use cases :

1. **Accessing DOM Elements**: You can use it to directly interact with DOM elements in a React way.
2. **Storing Instance Variables**: For example, if you're building a timer, you can store the interval ID in a ref.

## Accessing DOM elements :

To perform imperative actions on DOM nodes, React provides a way to get a reference to them via refs. All you have to do is to assign a `ref` property to a node with a ref object like this :

Well you can say that the same can be done like this

```jsx
  const addTodo = (e) => {
    e.preventDefault();
    setTask("");
		document.querySelector('input').current.focus()
  };
```

Something like this. But then you are going out of scope of react and interacting with browser API. React doesn’t have much control there and that is not `react way of doing things`

### Example 1 :

App.jsx

```jsx
import "./styles.css";
import { useRef } from "react";

export default function App() {
  const inputRef = useRef(null);
  // {current : input}

  const handleClick = () => {
    inputRef.current.focus();
  };

  return (
    <div className="App">
      <input id="inp" ref={inputRef} />
      <button onClick={handleClick}>FOCUS ON THE INPUT</button>
    </div>
  );
}
```

---

## **Storing Instance Variables :**

It can be super helpful if we need to store id of Timer ( Something which we have built previously ). It can be done this way ( Since the value of ref persists across re-renders )

```jsx
function startTimer(){
	ref.current = setInterval(()=>{
		// do something
	})
} 
```

```jsx
function stopTimer(){
	clearInterval(ref.current)
	ref.current = null
} 

```

Code :

```jsx
import { useEffect, useState, useRef } from "react";

function Timer() {
  const [count, setCount] = useState(10);
  const intervalRef = useRef(null);

  useEffect(() => {
    const cleanup = () => {
      stopTimer();
    };
    return cleanup;
  }, []);

  const startTimer = () => {
    if (intervalRef.current !== null) {
      console.log(`timer is already running`);
      return;
    }
    intervalRef.current = setInterval(() => {
      console.log(`timer running`, Date.now());
      setCount((prevCount) => {
        if (prevCount <= 1) {
          clearInterval(intervalRef.current);
        }
        return prevCount - 1;
      });
    }, 1000);
  };

  const stopTimer = () => {
    console.log(`timer stopped`);
    clearInterval(intervalRef.current);
    intervalRef.current = null;
  };

  const resetTimer = () => {
    stopTimer();
    setCount(10);
  };

  return (
    <div>
      <h6>{count} </h6>
      <button onClick={startTimer}>START</button>
      <button onClick={stopTimer}>STOP</button>
      <button onClick={resetTimer}>RESET</button>
    </div>
  );
}

export default Timer;
```

### A Quick Recap :

`useRef` allows you to create a mutable object that keeps the same reference between component renders. This object has a property called `current`.

**Key Characteristics**

1. **Persistence**: The value inside `useRef` persists throughout the component's lifecycle.
2. **Not Triggering Rerenders**: Unlike `useState`, changing a `useRef` does not cause the component to rerender.

**Why useRef :** 

1. **Accessing DOM Elements**: Directly manipulate DOM elements for focus management, measurements, etc.
2. **Storing Previous State**: You can use `useRef` to store the previous state or props. Useful for comparison with current state or props.
3. **Storing Values** : It could be any values like values derived from complex calculations to storing a basic interval id .

**Real World Examples :**

1. **Form Input Focus**: Automatically focus a text input when a component loads.
2. **Animation**: Keep track of animation frames in a component.
3. **Comparing Props**: Compare current props with previous ones to decide on rendering logic.
4. Building Custom Element say a custom video player and managing it
5. Storing interval ids and persist across re-renders
6. Building custom components like Pin Component above

**Syntax :**

Here's how to use `useRef`:

1. **Importing useRef**: `import { useRef } from 'react';`
2. **Initialization**: `const myRef = useRef(initialValue);`
3. **Accessing Ref**: Use `myRef.current` to access the stored value.