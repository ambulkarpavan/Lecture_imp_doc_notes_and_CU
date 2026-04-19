# Custom Hooks

### Introduction to Custom Hooks in React

Custom hooks in React allow developers to extract component logic into reusable functions. This feature, introduced in React 16.8, has revolutionized state management and side effects in functional components, making them as powerful as class components.

### Understanding Custom Hooks

Custom hooks are JavaScript functions that start with `use` and can call other hooks. They enable you to create your reusable stateful logic and share it across multiple components. By using custom hooks, you encapsulate and abstract stateful logic, making your code more organized and manageable.

### How Custom Hooks Work

Custom hooks can use other built-in React hooks like `useState`, `useEffect`, and `useContext`. They allow for the encapsulation and abstraction of stateful logic into a reusable function. This logic can then be shared across different components, promoting code reusability and separation of concerns.

### Use-case & Benefits

1. **Reusability**: Custom hooks allow you to share logic across multiple components without the need for higher-order components or render props.
2. **Separation of Concerns**: Encapsulate specific functionality in each custom hook, leading to more organized and manageable code.
3. **Testability**: Isolated custom hooks are easier to test in isolation from the components that use them.

### Real-World Examples of Custom Hooks

1. **useForm**: Manages form input values, validation, and submission.
2. **useFetch**: Handles fetching data from an API, including managing loading and error states.

### Creating and Using Custom Hooks

### 1. Creating a Custom Hook

Declare a function that starts with `use`, for instance, `useCustomHook`. Inside your custom hook, utilize React’s built-in hooks to manage state, effects, and more. Return whatever stateful values or functions you want to expose from this hook.

### 2. Using Custom Hooks in Components

Import your custom hook into your component and call it as you would with built-in hooks. Access the values or functions returned by the custom hook and integrate them into your component's logic.

### Instructor Activity: Creating and Using a Custom `useFetch` Hook

### Code Example:

```jsx
// useFetch.js
import { useState, useEffect } from 'react';

function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(url);
        const result = await response.json();
        setData(result);
        setLoading(false);
      } catch (error) {
        setError(error);
        setLoading(false);
      }
    };

    fetchData();
  }, [url]);

  return { data, loading, error };
}

export default useFetch;
```

### Using `useFetch` in a Component:

```jsx
// MyComponent.js
import React from 'react';
import useFetch from './useFetch';

function MyComponent() {
  const { data, loading, error } = useFetch('<https://api.example.com/data>');

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      <h1>Data Fetched</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default MyComponent;
```

### Learner Activity: `useLocalStorage` Custom Hook

### Task:

Create a custom hook named `useLocalStorage` that persists and retrieves a value from the browser's local storage. It should accept a key and an initial value as parameters.

### Learner Activity Solution:

```jsx
// useLocalStorage.js
import { useState, useEffect } from 'react';

function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error('Error reading from localStorage', error);
      return initialValue;
    }
  });

  const setValue = (value) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error('Error writing to localStorage', error);
    }
  };

  useEffect(() => {
    setValue(storedValue);
  }, [key]);

  return [storedValue, setValue];
}

export default useLocalStorage;

```

### Using `useLocalStorage` in a Component:

```jsx
// MyComponent.js
import React from 'react';
import useLocalStorage from './useLocalStorage';

function MyComponent() {
  const [name, setName] = useLocalStorage('name', 'React');

  return (
    <div>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <p>Hello, {name}!</p>
    </div>
  );
}

export default MyComponent;

```

---

We've previously discussed the `useLocalStorage` hook. Now, let's expand our notes by examining additional custom hooks: `useTimer`, `useDebounce`, `useThrottle`, and `useMyReducer`. Each of these hooks serves a unique purpose and can be extremely useful in various scenarios.

### 1. useTimer Hook

**Purpose**: The `useTimer` hook is designed to change a value from `false` to `true` after a specified delay. This can be particularly useful for scenarios like showing a component after a certain period or triggering an action after a delay.

**How it Works**:

```jsx
export const useTimer = (delay) => {
  const [show, setShow] = useState(false);

  useEffect(() => {
    let id = setTimeout(() => {
      setShow(true);
    }, delay);

    return () => {
      clearTimeout(id);
    };
  }, [delay]);

  return show;
};

```

- **useState**: Initializes a state variable `show` with `false`.
- **useEffect**: Sets up a timeout that sets `show` to `true` after the specified `delay`. The cleanup function clears the timeout, preventing side effects if the component unmounts before the timeout completes.
- **Return Value**: Returns the current state of `show`, which components can use to determine if the timer has completed.

### 2. useDebounce Hook

**Purpose**: `useDebounce` is used to delay the execution of a function until after a certain amount of time has passed since the last time it was invoked. This is particularly useful for performance optimization, such as delaying a search operation until the user stops typing.

**How it Works**:

```jsx
export const useDebounce = (func, delay) => {
  let { current: id } = useRef();

  return () => {
    id && clearTimeout(id);
    id = setTimeout(() => {
      func();
    }, delay);
  };
};

```

- **useRef**: Stores the `timeoutId` across renders without causing re-renders itself.
- **Functionality**: Clears the previous timeout (if any) and sets a new one each time the returned function is called. The actual function `func` is only called after the specified `delay`.

### 3. useThrottle Hook

**Purpose**: `useThrottle` allows you to ensure that a function is not called more often than the time interval you specify. It's particularly useful for controlling the rate at which a function can fire, for instance, handling scroll or resize events.

**How it Works**:

```jsx
export const useThrottle = (func, delay) => {
  let { current: wait } = useRef(false);

  return () => {
    if (wait) return;

    func();
    wait = true;

    setTimeout(() => {
      wait = false;
    }, delay);
  };
};

```

- **useRef**: Holds a boolean flag `wait` across renders.
- **Functionality**: The function `func` is called immediately if `wait` is `false`, and then `wait` is set to `true`. `wait` is reset to `false` after the specified `delay`, allowing the function to be called again.

### 4. useMyReducer Hook

**Purpose**: `useMyReducer` mimics the behavior of the built-in `useReducer` hook, providing an alternative way to handle complex state logic in components.

**How it Works**:

```jsx
const useMyReducer = (reducer, initialState) => {
  const [state, setState] = useState(initialState);

  const dispatch = (action) => {
    const nextState = reducer(state, action);
    setState(nextState);
  }

  return [state, dispatch];
}

```

- **useState**: Sets up the state and state updater function.
- **dispatch Function**: Takes an action, computes the next state using the `reducer` function, and sets the new state.
- **Return Value**: Returns the current state and the `dispatch` function, which components can use to update the state based on actions.

### Summary

These custom hooks (`useTimer`, `useDebounce`, `useThrottle`, and `useMyReducer`) are powerful tools that abstract and encapsulate specific functionalities, making your codebase cleaner, more organized, and more reusable. Each serves a unique purpose and can be easily integrated into your React components to manage timing, rate-limiting of function executions, and complex state management in a more declarative and readable manner.