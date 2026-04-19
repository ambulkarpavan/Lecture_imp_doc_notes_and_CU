# useReducer

Serial: 51

# Introduction

In this lesson, we explore the `useReducer` hook in React, focusing on its syntax, flow, and advantages over `useState`, especially in complex state management scenarios.

# Detailed Explanation

### Understanding `useReducer`

- **What It Is:** `useReducer` is a React hook that manages state in a more structured way compared to `useState`. It's particularly useful for complex state logic.
- **How It Works:** It uses a reducer function to determine state changes based on actions, offering a predictable and organized way to handle state transitions.

### `useReducer` vs `useState`

- **`useState`**: Simple and direct, suitable for straightforward state updates.
- **`useReducer`**: Offers more control and is better suited for complex scenarios where state updates depend on previous states or when managing multiple sub-values.

# Use-case & Benefits

- **Complex State Logic:** Ideal for situations where state logic is complex or involves multiple sub-values.
- **Predictable State Transitions:** The dispatch-action pattern provides clear and predictable state updates.
- **Scalable State Management:** As application complexity grows, `useReducer` keeps state management manageable and organized.

# Real World Examples

### Example 1: Counter Application

1. **Counter with `useState`**:
    
    ```jsx
    import { useState } from "react";
    
    function Counter1() {
      const [count, setCount] = useState(0);
    
      const handleIncrement = () => setCount(count + 1);
      const handleDecrement = () => setCount(count - 1);
    
      return (
        <>
          <h1>Counter: {count}</h1>
          <button onClick={handleIncrement}>INCREMENT</button>
          <button onClick={handleDecrement}>DECREMENT</button>
        </>
      );
    }
    
    export { Counter1 };
    
    ```
    
2. **Counter with `useReducer`**:
    
    ```jsx
    import { useReducer } from "react";
    
    const reducer = (state, action) => {
      switch (action.type) {
        case "INCREMENT_COUNT":
          return state + 1;
        case "DECREMENT_COUNT":
          return state - 1;
        default:
          throw new Error(`Action type is invalid`);
      }
    };
    
    function Counter2() {
      const [state, dispatch] = useReducer(reducer, 0);
    
      const handleIncrement = () => dispatch({ type: "INCREMENT_COUNT" });
      const handleDecrement = () => dispatch({ type: "DECREMENT_COUNT" });
    
      return (
        <>
          <h1>Counter: {state}</h1>
          <button onClick={handleIncrement}>INCREMENT</button>
          <button onClick={handleDecrement}>DECREMENT</button>
        </>
      );
    }
    
    export { Counter2 };
    
    ```
    

### Example 2: Todo Application

1. **Todo with `useState`**:
    
    ```jsx
    // src/components/AddTodo.jsx
    import { useState } from "react";
    
    function AddTodo({ handleAdd }) {
      const [text, setText] = useState("");
    
      const handleClick = () => {
        const taskObject = {
          id: Math.random() + text + Date.now(),
          title: text,
          status: false
        };
        handleAdd(taskObject);
        setText("");
      };
    
      return (
        <>
          <label>
            ADD TODO :
            <input value={text} onChange={(e) => setText(e.target.value)} />
            <button onClick={handleClick}>ADD</button>
          </label>
        </>
      );
    }
    
    export default AddTodo;
    
    // src/components/TodoItem.jsx
    function TodoItem({ id, title, status, handleDelete, handleToggle }) {
      return (
        <div style={{ border: "1px solid black", margin: "10px" }}>
          <p>{title}</p>
          <p>STATUS : {status ? "DONE" : "NOT DONE"}</p>
          <button onClick={() => handleToggle(id)}>TOGGLE</button>
          <button onClick={() => handleDelete(id)}>DELETE</button>
        </div>
      );
    }
    
    export default TodoItem;
    
    // src/components/Todo.jsx
    import { useState } from "react";
    import AddTodo from "./AddTodo";
    import TodoItem from "./TodoItem";
    
    const initState = [
      { id: 1, title: "Learn HTML", status: false },
      { id: 2, title: "Learn JS", status: true },
      { id: 3, title: "Learn React", status: false }
    ];
    
    function Todo() {
      const [state, setState] = useState(initState);
    
      const handleAdd = (task) => {
        setState([...state, task]);
      };
    
      const handleDelete = (id) => {
        const todosAfterDeletion = state.filter(todo => todo.id !== id);
        setState(todosAfterDeletion);
      };
    
      const handleToggle = (id) => {
        const todosAfterToggle = state.map(todo =>
          todo.id === id ? { ...todo, status: !todo.status } : todo
        );
        setState(todosAfterToggle);
      };
    
      return (
        <>
          <AddTodo handleAdd={handleAdd} />
          {state.map(todo => (
            <TodoItem
              key={todo.id}
              {...todo}
              handleDelete={handleDelete}
              handleToggle={handleToggle}
            />
          ))}
        </>
      );
    }
    
    export default Todo;
    ```
    
2. **Todo with `useReducer`**:
    
    ```jsx
    import { useReducer } from "react";
    
    // src/reducer.js
    const reducer = (state, action) => {
      switch (action.type) {
        case "ADD_TASK":
          return [...state, action.payload];
        case "DELETE_TASK":
          const todosAfterDeletion = state.filter(todo => todo.id !== action.payload);
          return todosAfterDeletion;
        case "UPDATE_TASK":
          const todosAfterUpdation = state.map(todo =>
            todo.id === action.payload.id ? { ...todo, status: !todo.status } : todo
          );
          return todosAfterUpdation;
        default:
          throw new Error(`Unknown action type: ${action.type}`);
      }
    };
    
    export default reducer;
    
    ---
    
    // src/components/Todo.jsx
    import { useReducer } from "react";
    import AddTodo from "./AddTodo";
    import TodoItem from "./TodoItem";
    import reducer from "../reducer";
    
    const initState = [
      { id: 1, title: "Learn HTML", status: false },
      { id: 2, title: "Learn JS", status: true },
      { id: 3, title: "Learn React", status: false }
    ];
    
    function Todo() {
      const [state, dispatch] = useReducer(reducer, initState);
    
      const handleAdd = (task) => {
        dispatch({
          type: "ADD_TASK",
          payload: task
        });
      };
    
      const handleDelete = (id) => {
        dispatch({
          type: "DELETE_TASK",
          payload: id
        });
      };
    
      const handleToggle = (id) => {
        dispatch({
          type: "UPDATE_TASK",
          payload: { id }
        });
      };
    
      return (
        <>
          <AddTodo handleAdd={handleAdd} />
          {state.map(todo => (
            <TodoItem
              key={todo.id}
              {...todo}
              handleDelete={handleDelete}
              handleToggle={handleToggle}
            />
          ))}
        </>
      );
    }
    
    export default Todo;
    ---
    
    ```
    

# Usage

### Implementing `useReducer`

1. **Defining the Reducer:** Create a reducer function that dictates how the state updates based on different actions.
2. **Setting up `useReducer`:** Replace `useState` with `useReducer`, providing the reducer function and the initial state.
3. **Dispatching Actions:** Use the dispatch function to update the state based on user interactions.

# Instructor Activity

- **Interactive Coding:** Live-code the transition from `useState` to `useReducer` using the Counter example. Highlight the differences in handling state.
- **Analyzing Todo Example:** Walk through the Todo application code, explaining how `useReducer` simplifies state management in complex applications.

# Learners Activity

- **Refactoring Exercise:** Have learners convert a simple application from `useState` to `useReducer`.
- **Building a Todo App:** Task learners with creating a Todo application using `useReducer` to manage various actions like adding, deleting, and updating tasks.

These examples, derived from your notes, illustrate the practical application and benefits of `useReducer` in different scenarios, enhancing the understanding of its usage and advantages over `useState`.