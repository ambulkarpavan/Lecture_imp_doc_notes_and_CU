# Redux - Combine Reducer

### Project Structure

Create separate folders for each feature within the Redux folder.

```jsx
.
└── src
    ├── App.css
    ├── App.js
    ├── Components
    │   ├── Counter
    │   │   └── Counter.jsx
    │   └── Todo
    │       ├── Todo.jsx
    │       ├── TodoInput.jsx
    │       └── TodoItem.jsx
    ├── Redux
    │   ├── Counter
    │   │   ├── action.js
    │   │   ├── actionTypes.js
    │   │   └── reducer.js
    │   ├── Todo
    │   │   ├── action.js
    │   │   ├── actionTypes.js
    │   │   └── reducer.js
    │   └── store.js
    ├── index.css
    └── index.js
```

### src/Redux/Counter/actionTypes.js

```jsx
export const INCREMENT = "INCREMENT";
export const DECREMENT = "DECREMENT";
export const RESET_COUNT = "RESET_COUNT";

```

### src/Redux/Counter/action.js

```jsx
import { INCREMENT, DECREMENT, RESET_COUNT } from "./actionTypes";

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

### src/Redux/Counter/reducer.js

```jsx
import { INCREMENT, DECREMENT, RESET_COUNT } from "./actionTypes";

const initState = {
  count: 0,
};

export const counterReducer = (state = initState, action) => {
  switch (action.type) {
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

### src/Redux/Todo/actionTypes.js

```jsx
export const ADD_TODO = "ADD_TODO";
export const DELETE_TODO = "DELETE_TODO";
export const UPDATE_TODO = "UPDATE_TODO";

```

### src/Redux/Todo/action.js

```jsx
import { ADD_TODO, DELETE_TODO, UPDATE_TODO } from "./actionTypes";

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

```

### src/Redux/Todo/reducer.js

```jsx
import { ADD_TODO, DELETE_TODO, UPDATE_TODO } from "./actionTypes";

const initState = {
  todos: [],
};

export const todoReducer = (state = initState, action) => {
  switch (action.type) {
    case ADD_TODO:
      return {
        ...state,
        todos: [...state.todos, action.payload],
      };
    case DELETE_TODO:
      return {
        ...state,
        todos: state.todos.filter(todo => todo.id !== action.payload),
      };
    case UPDATE_TODO:
      return {
        ...state,
        todos: state.todos.map(todo =>
          todo.id === action.payload.id ? { ...todo, title: action.payload.title } : todo
        ),
      };
    default:
      return state;
  }
};

```

### src/Redux/store.js

```jsx
import { createStore, combineReducers } from "redux";
import { counterReducer } from "./Counter/reducer";
import { todoReducer } from "./Todo/reducer";

const rootReducer = combineReducers({
  counter: counterReducer,
  todos: todoReducer,
});

export const store = createStore(
  rootReducer
);

store.subscribe(() => {
  console.log("state got updated", store.getState());
});

```

### src/Components/Counter/Counter.jsx

```jsx
import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { increment, decrement, resetCount } from "../../Redux/Counter/action";

export const Counter = () => {
  const count = useSelector((state) => state.counter.count);
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

### src/Components/Todo/Todo.jsx

```jsx
import React from "react";
import { useSelector } from "react-redux";
import { TodoItem } from "./TodoItem";
import { TodoInput } from "./TodoInput";

export const Todo = () => {
  const todos = useSelector((state) => state.todos.todos);
  return (
    <>
      <TodoInput />
      <br />
      <br />
      <div>
        {todos.map((item) => (
          <TodoItem key={item.id} {...item} />
        ))}
      </div>
    </>
  );
};

```

With these changes, we've successfully refactored our code to separate our state management logic based on features, using `combineReducers` to create a root reducer. This makes our application more maintainable and scalable.