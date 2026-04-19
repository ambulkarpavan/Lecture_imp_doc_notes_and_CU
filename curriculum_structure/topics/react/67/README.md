# Redux - Middlewares

## Part 1: Middleware in Redux

Redux middleware acts as an intermediary layer between dispatching an action and the moment it reaches the reducer. It's used for logging, handling asynchronous actions, and more.

**Setting Up Middleware:**

In this example, we create a simple logger middleware to understand the middleware flow.

```jsx
// Middleware Setup
import { createStore, combineReducers, applyMiddleware } from "redux";
import { counterReducer } from "./Counter/reducer";
import { todoReducer } from "./Todo/reducer";

export const rootReducer = combineReducers({
  count: counterReducer,
  todos: todoReducer,
});

const loggerMiddleware = (store) => (next) => (action) => {
  console.log("Middleware triggered:", action);
  next(action);
};

export const store = createStore(
  rootReducer,
  applyMiddleware(loggerMiddleware)
);

store.subscribe(() => {
  console.log("Updated state:", store.getState());
});
```

## Full Code :

### Entire Project Structure:

```
project-root/
├── src/
│   ├── Components/
│   │   ├── Counter/
│   │   │   └── Counter.jsx
│   │   └── Todo/
│   │       ├── Todo.jsx
│   │       ├── TodoInput.jsx
│   │       └── TodoList.jsx
│   ├── Redux/
│   │   ├── Counter/
│   │   │   ├── actionTypes.js
│   │   │   ├── actions.js
│   │   │   └── reducer.js
│   │   ├── Todo/
│   │   │   ├── actionTypes.js
│   │   │   ├── actions.js
│   │   │   └── reducer.js
│   │   └── store.js
│   ├── App.js
│   └── index.js
├── package.json
└── db.json

```

### Part 1: Middleware in Redux

**Redux/Counter/actionTypes.js:**

```jsx
export const INCREMENT = "INCREMENT";
export const DECREMENT = "DECREMENT";
```

**Redux/Counter/actions.js:**

```jsx
import * as actionTypes from "./actionTypes";

export const increment = (payload) => ({
  type: actionTypes.INCREMENT,
  payload
});

export const decrement = (payload) => ({
  type: actionTypes.DECREMENT,
  payload
});
```

**Redux/Counter/reducer.js:**

```jsx
import * as actionTypes from "./actionTypes";

const initialState = {
  count: 0
};

export const counterReducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.INCREMENT:
      return { ...state, count: state.count + action.payload };
    case actionTypes.DECREMENT:
      return { ...state, count: state.count - action.payload };
    default:
      return state;
  }
};

```

**Redux/store.js:**

```jsx
import { createStore, combineReducers, applyMiddleware } from "redux";
import { counterReducer } from "./Counter/reducer";
import { todoReducer } from "./Todo/reducer";

export const rootReducer = combineReducers({
  count: counterReducer,
  todos: todoReducer,
});

const loggerMiddleware1 = (store) => (next) => (action) => {
  console.log("Entering Middleware 1");
  if (typeof action === "function") {
    return action(store.dispatch);
  }
  next(action);
  console.log("Exiting Middleware 1");
};

const loggerMiddleware2 = (store) => (next) => (action) => {
  console.log("Entering Middleware 2");
  next(action);
  console.log("Exiting Middleware 2");
};

export const store = createStore(
  rootReducer,
  applyMiddleware(loggerMiddleware1, loggerMiddleware2)
  // window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);

store.subscribe(() => {
  console.log("localStorage", localStorage.getItem("count"));
  console.log(store.getState());
});
```

## Part 2: Implementing Custom Thunk Middleware

Instead of using the Redux Thunk library, we'll create a custom thunk middleware to understand its inner workings.

**Custom Thunk Middleware:**

Our custom thunk middleware will check if the action is a function. If it is, it will call that function with `dispatch` as an argument.

```jsx
// Custom Thunk Middleware
const customThunk = (store) => (next) => (action) => {
  console.log("Entering Custom Thunk Middleware");
  if (typeof action === "function") {
    return action(store.dispatch);
  }
  next(action);
  console.log("Exiting Custom Thunk Middleware");
};

export const store = createStore(
  rootReducer,
  applyMiddleware(customThunk)
);

store.subscribe(() => {
  console.log("Updated state:", store.getState());
});

```

### Example Usage of Custom Thunk:

**Redux Actions:**

We'll define actions for loading, success, and error states for an asynchronous operation.

```jsx
// Redux/Todo/action.js
export const GET_TODOS = "GET_TODOS";
export const GET_TODOS_LOADING = "GET_TODOS_LOADING";
export const GET_TODOS_ERROR = "GET_TODOS_ERROR";

export const getTodos = (payload) => ({
  type: GET_TODOS,
  payload
});
export const getTodosLoading = () => ({
  type: GET_TODOS_LOADING
});
export const getTodosError = () => ({
  type: GET_TODOS_ERROR
});

export const getTodosData = () => (dispatch) => {
  dispatch(getTodosLoading());
  fetch(`http://localhost:3001/todos`)
    .then((res) => res.json())
    .then((res) => {
      dispatch(getTodos(res));
    })
    .catch(() => {
      dispatch(getTodosError());
    });
};

```

**Redux Reducer:**

The reducer will handle the various states based on the actions dispatched.

```jsx
// Redux/Todo/reducer.js
import { GET_TODOS_LOADING, GET_TODOS, GET_TODOS_ERROR } from "./action";

const initState = {
  loading: false,
  error: false,
  todos: []
};

const todoReducer = (store = initState, { type, payload }) => {
  switch (type) {
    case GET_TODOS_LOADING:
      return { ...store, loading: true };
    case GET_TODOS:
      return { ...store, todos: payload, loading: false, error: false };
    case GET_TODOS_ERROR:
      return { ...store, loading: false, error: true };
    default:
      return store;
  }
};

export { todoReducer };

```

### Using Custom Thunk in Components:

Now, we use the `getTodosData` action in our component, demonstrating how the custom thunk handles asynchronous actions.

```jsx
// Components/TodoList.jsx
import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getTodosData } from "../../Redux/Todo/action";

export const TodoList = () => {
  const { todos, loading, error } = useSelector((state) => state.todos);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getTodosData());
  }, [dispatch]);

  // Handle delete and toggle operations
  // Render loading, error, and todo list based on the state
};

```

In this tutorial, we explored how Redux middleware operates and implemented a custom thunk middleware. This custom implementation helps to understand the concept of thunks in Redux, particularly useful for handling complex asynchronous operations.

Full Code : 

**Redux/Todo/actionTypes.js:**

```jsx
export const GET_TODOS = "GET_TODOS";
export const GET_TODOS_LOADING = "GET_TODOS_LOADING";
export const GET_TODOS_ERROR = "GET_TODOS_ERROR";
```

**Redux/Todo/actions.js:**

```jsx
import * as actionTypes from "./actionTypes";

export const getTodos = (payload) => ({
  type: actionTypes.GET_TODOS,
  payload
});
export const getTodosLoading = () => ({
  type: actionTypes.GET_TODOS_LOADING
});
export const getTodosError = () => ({
  type: actionTypes.GET_TODOS_ERROR
});

export const getTodosData = () => (dispatch) => {
  dispatch(getTodosLoading());
  fetch(`http://localhost:3001/todos`)
    .then((res) => res.json())
    .then((res) => {
      dispatch(getTodos(res));
    })
    .catch(() => {
      dispatch(getTodosError());
    });
};

```

**Redux/Todo/reducer.js:**

```jsx
import * as actionTypes from "./actionTypes";

const initialState = {
  loading: false,
  error: false,
  todos: []
};

export const todoReducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.GET_TODOS_LOADING:
      return { ...state, loading: true };
    case actionTypes.GET_TODOS:
      return { ...state, todos: action.payload, loading: false, error: false };
    case actionTypes.GET_TODOS_ERROR:
      return { ...state, loading: false, error: true };
    default:
      return state;
  }
};
```

**Redux/store.js:**

```jsx
import { createStore, combineReducers, applyMiddleware } from "redux";
import { counterReducer } from "./Counter/reducer";
import { todoReducer } from "./Todo/reducer";

const customThunk = (store) => (next) => (action) => {
  if (typeof action === "function") {
    return action(store.dispatch);
  }
  next(action);
};

export const rootReducer = combineReducers({
  count: counterReducer,
  todos: todoReducer,
});

export const store = createStore(
  rootReducer,
  applyMiddleware(customThunk)
);

store.subscribe(() => {
  console.log("localStorage", localStorage.getItem("count"));
  console.log("Updated state:", store.getState());
});

```

---

In this final part of the tutorial, we will replace the custom thunk middleware with the actual Redux Thunk library. Redux Thunk is a middleware that allows you to write action creators that return a function instead of an action. This is particularly useful for handling asynchronous operations such as API requests.

### Step 1: Install Redux Thunk

If you haven't already installed Redux Thunk, you can do so by running the following command in your project directory:

```bash
npm install redux-thunk
```

### Step 2: Set Up Redux Thunk in the Store

Now, let's integrate Redux Thunk into our store. Replace the custom thunk middleware with Redux Thunk in your `store.js` file.

**Redux/store.js:**

```jsx
import { legacy_createStore as createStore, combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { counterReducer } from "./Counter/reducer";
import { todoReducer } from "./Todo/reducer";

export const rootReducer = combineReducers({
  count: counterReducer,
  todos: todoReducer,
});

export const store = createStore(rootReducer, applyMiddleware(thunk));
```

In the code above, we've imported the `thunk` middleware from the `redux-thunk` package and applied it to our store using `applyMiddleware`. This enables our action creators to return functions (thunks) that have access to the `dispatch` and `getState` methods of the Redux store.

### Step 3: Write Asynchronous Action Creators

With Redux Thunk, you can now write action creators that handle asynchronous logic. Here's an example of how you might fetch data from an API and update your Redux store based on the response.

**Redux/Todo/actions.js:**

```jsx
import * as actionTypes from "./actionTypes";

// Synchronous action creators
export const getTodos = (payload) => ({
  type: actionTypes.GET_TODOS,
  payload
});
export const getTodosLoading = () => ({
  type: actionTypes.GET_TODOS_LOADING
});
export const getTodosError = () => ({
  type: actionTypes.GET_TODOS_ERROR
});

// Asynchronous action creator using Redux Thunk
export const getTodosData = () => (dispatch) => {
  dispatch(getTodosLoading());
  fetch(`http://localhost:3001/todos`)
    .then((res) => res.json())
    .then((res) => {
      dispatch(getTodos(res));
    })
    .catch(() => {
      dispatch(getTodosError());
    });
};

```

In the code above, `getTodosData` is an asynchronous action creator. When it's dispatched, Redux Thunk intercepts it and provides the `dispatch` function, allowing you to perform asynchronous operations and dispatch other actions based on the result.

### Step 4: Dispatch Asynchronous Actions in Components

In your React components, you can dispatch the asynchronous actions just like you would with synchronous actions.

**Components/TodoList.jsx:**

```jsx
import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getTodosData } from "../../Redux/Todo/action";

export const TodoList = () => {
  const { todos, loading, error } = useSelector((state) => state.todos);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getTodosData());
  }, [dispatch]);

  // Render your component based on the state (loading, error, todos)
};

```

In the component above, we use `useEffect` to dispatch `getTodosData` when the component mounts. This fetches the todo data from the server and updates the Redux store.

### Conclusion

By integrating Redux Thunk, we've enhanced our application's ability to handle asynchronous operations. Actions can now encapsulate asynchronous logic, making our components simpler and our code more maintainable. Redux Thunk provides a robust solution for managing complex state changes, particularly those involving asynchronous processes like API calls.