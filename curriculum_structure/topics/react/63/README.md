# React - Redux

Let's understand Redux and React-Redux by building a Counter and TodoList.

### Introduction

***Redux*** is a standalone library for managing and centralizing application state. It's commonly used with React but isn't exclusive to it. ***React-Redux*** is an official library that binds Redux with React, offering hooks like `useSelector` and `useDispatch` to interact with the Redux store in a React component. In this lesson, we'll explore these concepts by building a counter and a todo list application.

### Detailed Explanation

### Redux Basics

1. **Store**: The global state of your application.
2. **Action**: A plain JavaScript object describing what happened and what needs to change in the state.
3. **Reducer**: A pure function that takes the current state and an action, and returns the new state.
4. **Dispatch**: The process of sending actions to the reducer to update the state.

### React-Redux

- **`useSelector`**: A hook that allows you to extract data from the Redux store state.
- **`useDispatch`**: A hook that gives you access to the `dispatch` function to send actions to the store.

### Project Structure

We'll be working with the following project structure:

```
.
└── src
    ├── Components
    │   ├── Counter
    │   │   └── Counter.jsx
    │   └── Todo
    │       ├── Todo.jsx
    │       ├── TodoInput.jsx
    │       └── TodoItem.jsx
    ├── Redux
    │   ├── actionTypes.js
    │   ├── action.js
    │   ├── reducer.js
    │   └── store.js
    ├── App.css
    ├── App.js
    └── index.js

```

### Use-case & Benefits

- **Counter Functionality**: Demonstrates basic actions like increment, decrement, and reset ( Primitive Datatype - Number ).
- **Todo List Functionality**: Showcases more complex state management including adding, updating, and deleting tasks ( Non Primitive Datatype - Array ).

### Real World Examples

In real-world applications, managing state across multiple components can become complex. Redux provides a global state container to manage this efficiently. For instance, user authentication status or a shopping cart in an e-commerce app are typically kept in a global state.

### Usage

### 1. Setting up Redux and React-Redux

Before diving into code, ensure that you have `redux`, `react-redux`, and `uuid` for unique key generation installed in your project.

### 2. Code Implementation

We'll start by defining our Redux actions, reducers, and store. Then we'll integrate these with our React components.

### Actions (`action.js`)

```jsx
import { ADD_TODO, DELETE_TODO, UPDATE_TODO, INCREMENT, DECREMENT, RESET_COUNT } from "./actionTypes";

export const addTodo = (data) => ({
  type: ADD_TODO,
  payload: data,
});

export const deleteTodo = (id) => ({
  type: DELETE_TODO,
  payload: id,
});

export const updateTodo = (data) => ({
  type: UPDATE_TODO,
  payload: data,
});

export const increment = (value) => ({
  type: INCREMENT,
  payload: value,
});

export const decrement = (value) => ({
  type: DECREMENT,
  payload: value,
});

export const resetCount = () => ({
  type: RESET_COUNT,
});
```

### Reducer (`reducer.js`)

```jsx
import { ADD_TODO, DELETE_TODO, UPDATE_TODO, INCREMENT, DECREMENT, RESET_COUNT } from "./actionTypes";

const initState = {
  count: 0,
  todos: [],
};

export const reducer = (state = initState, action) => {
  switch (action.type) {
    case ADD_TODO:
      return {
        ...state,
        todos: [...state.todos, action.payload],
      };
    case DELETE_TODO:
      return {
        ...state,
        todos: state.todos.filter((todo) => todo.id !== action.payload),
      };
    case UPDATE_TODO:
      return {
        ...state,
        todos: state.todos.map((todo) =>
          todo.id === action.payload.id ? { ...todo, title: action.payload.title } : todo
        ),
      };
    case INCREMENT:
      return {
        ...state,
        count: state.count + action.payload,
      };
    case DECREMENT:
      return {
        ...state,
        count: state.count - action.payload,
      };
    case RESET_COUNT:
      return {
        ...state,
        count: 0,
      };
    default:
      return state;
  }
};
```

### Store (`store.js`)

```jsx
import { createStore } from "redux";
import { reducer } from "./reducer";

export const store = createStore(reducer);

store.subscribe(() => {
  console.log("state got updated", store.getState());
});

```

### Integrating Redux with React Components

Let's integrate the Redux state with our React components.

### Counter Component (`Counter.jsx`)

```jsx
import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { increment, decrement, resetCount } from "../../Redux/action";

export const Counter = () => {
  const count = useSelector((state) => state.count);
  const dispatch = useDispatch();

  const handleIncrement = () => {
    dispatch(increment(1));
  };

  const handleDecrement = () => {
    dispatch(decrement(1));
  };

  const handleReset = () => {
    dispatch(resetCount());
  };

  return (
    <>
      <h1>Count is {count}</h1>
      <button onClick={handleIncrement}>INC</button>
      <button onClick={handleDecrement}>DEC</button>
      <button onClick={handleReset}>RESET</button>
    </>
  );
};
```

### Todo Components (`Todo.jsx`, `TodoInput.jsx`, `TodoItem.jsx`)

We've already defined `Todo.jsx`, `TodoInput.jsx`, and `TodoItem.jsx`. You can integrate the DELETE_TODO and UPDATE_TODO actions similarly to how ADD_TODO is integrated.

### Todo.jsx

```jsx
import React from "react";
import { useSelector } from "react-redux";
import { TodoItem } from "./TodoItem";
import { TodoInput } from "./TodoInput";

export const Todo = () => {
  const todos = useSelector((state) => state.todos);

  return (
    <>
      <TodoInput />
      <br />
      <br />
      <div>
        {todos.map((todo) => (
          <TodoItem key={todo.id} {...todo} />
        ))}
      </div>
    </>
  );
};
```

### TodoInput.jsx

```jsx
import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { addTodo } from "../../Redux/action";
import { v4 as uuidv4 } from 'uuid';

export const TodoInput = () => {
  const [title, setTitle] = useState("");
  const dispatch = useDispatch();

  const handleAdd = () => {
    const payload = {
      title,
      status: false,
      id: uuidv4(),
    };

    dispatch(addTodo(payload));
    setTitle(""); // Clear input field after adding
  };

  return (
    <>
      <input
        type="text"
        placeholder="Add Todo"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <button onClick={handleAdd}>ADD</button>
    </>
  );
};
```

### TodoItem.jsx

```jsx
import React from "react";
import { useDispatch } from "react-redux";
import { deleteTodo, updateTodo } from "../../Redux/action";

export const TodoItem = ({ id, title, status }) => {
  const dispatch = useDispatch();

  const handleDelete = () => {
    dispatch(deleteTodo(id));
  };

  const handleUpdate = () => {
    const updatedTitle = prompt("Update Todo Title:", title); // Simple prompt for the demo
    if (updatedTitle) {
      dispatch(updateTodo({
        id,
        title: updatedTitle
      }));
    }
  };

  return (
    <div>
      {title} {"-->"} {status ? "Completed" : "Not Completed"}
      <button onClick={handleDelete}>Delete</button>
      <button onClick={handleUpdate}>Update</button>
    </div>
  );
};
```

### Learner Activity

Try extending the application by:

1. Implementing the decrement and reset functionality for the counter.
2. Adding delete and update functionality for the todos.

### Learner Activity Solution

For the decrement and reset functionality in the counter, you'd create respective actions and update your reducer to handle these actions. Similarly, for delete and update functionality in todos, you'd create DELETE_TODO and UPDATE_TODO actions and update the reducer accordingly.

### Conclusion

In this lesson, we learned how Redux serves as a global state management tool and how React-Redux provides hooks to let your React components interact with the Redux store. We applied these concepts to build a counter and a todo list application, demonstrating both basic and complex state management. Remember, Redux is powerful for managing large-scale state but might be overkill for simple applications. Always assess your project's needs before choosing your state management strategy.