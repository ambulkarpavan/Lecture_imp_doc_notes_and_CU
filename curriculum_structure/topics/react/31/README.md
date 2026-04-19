# Effects and useEffect III - Unmount phase

Serial: 32
Made for: Beginner
Requirement: Must Have
Time in minutes: 20
Dependant on: Closures and Stale Closure ( A quick revision ) (Closures%20and%20Stale%20Closure%20(%20A%20quick%20revision%20)%20a0fbb17dcb0f41f79e48db7b6e9c527a.md)
Learning Objectives: React Component Lifecycle, effects and useEffect
Related back to React: Cleanup functions during update phase (Cleanup%20functions%20during%20update%20phase%20588f0087b46449b7b7cbf98c3b41ddc6.md)
doc-id: react-32

- useEffect and Unmount Phase
    - Introduction

In React, understanding the lifecycle of components is crucial for efficient resource management. A key aspect of this lifecycle is the unmount phase, during which components are removed from the UI. We'll explore how `useEffect` and cleanup functions play a vital role in this phase to prevent memory leaks and maintain optimal application performance.

**Unmount Phase/Event :**

When a React component is removed from the user interface, it undergoes the "unmount phase."

### Why is it important to know unmount phase ?

Imagine you have a room full of gadgets. When you leave the room, you turn off the lights, the fan, and any other electronics. This is like the "unmount phase" in React. It's the moment when a component is removed from the screen, and you should "clean up" to save resources.

A classic example is toggling the visibility of a component in the UI, like in the provided `Timer` component.

**Problem Statement  :** 

1. Build a countdown timer that starts countdown as soon as the component mounts. Default value is 10 and it should go all the way till 0 and stop
2. When the component Timer is unmounted from UI, The timer should stop and not run in the background. 

### Code :

Things we are trying to explain with this below example

- Unmount Phase and why is it important to know unmount phase
- Cleanup function and how cleanups are performed during unmount phase and why is it important to know
- Alse explain why while using `setCount` we chose callback function syntax `setState(prevState => {} )` over `setState(value)` ( Hint : Stale state and how to avoid. Also you’ll find stale closure concept revision in dependancy sheet )

```jsx
// src/App.jsx
import { useState } from "react"
import "./App.css"
import Timer from "./components/Timer"

function App() {
  const [showComponent, setShowComponent] = useState(true)

  return (
    <>
      <button onClick={() => setShowComponent(!showComponent)}>
        TOGGLE COMPONENT
      </button>
      {showComponent ? <Timer /> : null}
    </>
  )
}

export default App
```

```jsx
// src/components/Timer.jsx
import { useEffect } from "react"

function Timer() {
  useEffect(() => {
    setInterval(() => {
      console.log(`this code runs every 1 second`, Date.now())
    }, 1000)
  }, [])
  return <h1>Timer</h1>
}

export default Timer
```

**Observation** : You can observe that though the component `Timer` is unmounted from UI. the timer is still running in the background and is eating up your computer's memory. This is known as a "memory leak."

**How to Fix This?**

You can use a cleanup function in `useEffect` to stop the timer when the component is removed. Either of the code are basically doing the same thing.

```jsx
useEffect(() => {
  const intervalId = setInterval(() => {
    console.log(`this code runs every 1 second`, Date.now())
  }, 1000)

	// Cleanup function
  return () => {
    clearInterval(intervalId);
  };
}, [])

```

```jsx
useEffect(() => {
  const intervalId = setInterval(() => {
    console.log(`this code runs every 1 second`, Date.now())
  }, 1000)

	// Cleanup function
	const cleanupFunction = () => {
    clearInterval(intervalId);
  };
  return cleanupFunction;
}, [])
```

This cleanup function will run when the component is about to be removed/unmounted, effectively stopping the timer and preventing memory leaks.

**In a nutshell :**

1. **Unmount Phase / Unmount Event** : When a component is removed from UI. ( Like you are leaving your room )
2. **Cleanup Function inside useEffect** : A function that cleans up ongoing processes in the component about to be removed/unmounted from UI to prevent memory leaks. ( Like how you’d turn off computer, fan, light etc when you leave your room )

By understanding these concepts, you can manage resources effectively and make your apps more efficient. 

Project Structure : 

```jsx
├── src
│   ├── App.jsx
│   ├── components
│   │   └── Timer.jsx
│   └── main.jsx
```

App.jsx :

```jsx
import { useState } from "react";
import Timer from "./components/Timer";

function App() {
  const [showComponent, setShowComponent] = useState(true);

  return (
    <>
      <button onClick={() => setShowComponent(!showComponent)}>
        TOGGLE COMPONENT
      </button>
      {showComponent ? <Timer /> : null}
    </>
  );
}

export default App;
```

Timer.jsx : 

```jsx
// src/components/Timer.jsx
import { useEffect, useState } from "react";

function Timer() {
  const [count, setCount] = useState(10);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setCount((prevCount) => {
        if (prevCount === 1) {
          clearInterval(intervalId);
        }
        return prevCount - 1;
      });
    }, 1000);

    const cleanupFunction = () => {
      clearInterval(intervalId);
    };
    return cleanupFunction;
  }, []);

  return (
    <div>
      <h3>Count : {count}</h3>
    </div>
  );
}

export default Timer;
```