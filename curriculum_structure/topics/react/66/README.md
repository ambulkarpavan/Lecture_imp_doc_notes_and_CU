# Redux - Saving API Responses

In this section, we'll explore how to handle API responses by integrating them with the Redux store. We'll use a simple Todo application that interacts with a JSON server backend, demonstrating how to manage and synchronize state with server data.

### 1. Setting Up the Backend (JSON Server)

First, create a backend to serve our data using JSON server, a tool for setting up a fake REST API.

- **`db.json`**: This file will act as our mock database.
    
    ```json
    {
      "todos": [
        {
          "title": "Eat",
          "status": false,
          "id": 1
        },
        {
          "title": "Code",
          "status": true,
          "id": 2
        }
      ]
    }
    
    ```
    
- **Starting JSON Server**:
Run `json-server --watch db.json --port 3001` in your terminal.

### 2. Frontend Setup

Structure the React project as follows:

- `src/`
    - `redux/`
        - `action.js`
        - `reducer.js`
        - `store.js`
    - `components/`
        - `Todo.jsx`
        - `TodoInput.jsx`
        - `TodoItem.jsx`
    - `utils/`
        - `index.js`
    - `index.js`
    - `App.jsx`

### Code Implementation

**index.js**

```jsx
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { Provider } from "react-redux";
import { store } from "./redux/store";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <Provider store={store}>
    <App />
  </Provider>
);

```

**App.jsx**

```jsx
import React from "react";
import { Todo } from "./components/Todo";

function App() {
  return <Todo />;
}

export default App;

```

**Todo.jsx**

```jsx
import React, { useEffect } from "react";
import { TodoInput } from "./TodoInput";
import { useSelector, useDispatch } from "react-redux";
import { getLatestTodos } from "../redux/action";
import { TodoItem } from "./TodoItem";
import { getTodos } from "../utils";

export const Todo = () => {
  const todos = useSelector((state) => state.todos);
  const dispatch = useDispatch();

  useEffect(() => {
    getTodos("http://localhost:3001/todos")
      .then((res) => {
        dispatch(getLatestTodos(res));
      });
  }, [dispatch]);

  return (
    <>
      <TodoInput />
      {todos.map((el) => (
        <TodoItem key={el.id} {...el} />
      ))}
    </>
  );
};

```

**TodoItem.jsx**

```jsx
import React from "react";
import { useDispatch } from "react-redux";
import { getLatestTodos } from "../redux/action";
import { getTodos } from "../utils";

export const TodoItem = ({ id, title, status }) => {
  const dispatch = useDispatch();

  const fetchAndUpdateTodos = () => {
    getTodos("<http://localhost:3001/todos>")
      .then((res) => {
        dispatch(getLatestTodos(res));
      });
  };

  const handleDelete = () => {
    fetch(`http://localhost:3001/todos/${id}`, { method: "DELETE" })
      .then(fetchAndUpdateTodos);
  };

  const handleToggle = () => {
    fetch(`http://localhost:3001/todos/${id}`, {
      method: "PATCH",
      body: JSON.stringify({ status: !status }),
      headers: { "Content-Type": "application/json" }
    }).then(fetchAndUpdateTodos);
  };

  return (
    <div style={{ display: "flex" }}>
      <p>
        {title} - {status ? "Completed" : "Not Completed"}
      </p>
      <button onClick={handleDelete}>DELETE</button>
      <button onClick={handleToggle}>TOGGLE</button>
    </div>
  );
};

```

**TodoInput.jsx**

```jsx
import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { getLatestTodos } from "../redux/action";
import { getTodos } from "../utils";

export const TodoInput = () => {
  const [title, setTitle] = useState("");
  const dispatch = useDispatch();

  const fetchAndUpdateTodos = () => {
    getTodos("<http://localhost:3001/todos>")
      .then((res) => dispatch(getLatestTodos(res)));
  };

  const handleAdd = () => {
    const payload = { title, status: false };

    fetch("<http://localhost:3001/todos>", {
      method: "POST",
      body: JSON.stringify(payload),
      headers: { "Content-Type": "application/json" }
    }).then(fetchAndUpdateTodos);

    setTitle(""); // Clear the input after adding
  };

  return (
    <>
      <input
        type="text"
        placeholder="Add todo"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <button onClick={handleAdd}>ADD</button>
    </>
  );
};

```

**action.js**

```jsx
export const GET_LATEST_TODOS = "GET_LATEST_TODOS";

export const getLatestTodos = (payload) => ({
  type: GET_LATEST_TODOS,
  payload
});

```

**reducer.js**

```jsx
import { GET_LATEST_TODOS } from "./action";

const reducer = (store = { todos: [] }, { type, payload }) => {
  switch (type) {
    case GET_LATEST_TODOS:
      return { ...store, todos: payload };
    default:
      return store;
  }
};

export { reducer };
```

**store.js**

```jsx
import { legacy_createStore as createStore } from "redux";
import { reducer } from "./reducer";

export const store = createStore(
  reducer,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);
```

**utils/index.js**

```jsx
export const getTodos = (url) => {
  return fetch(url).then((res) => res.json());
};

```

### Conclusion

This tutorial demonstrated how to manage API responses using Redux by integrating a fake JSON server backend. By fetching data from the server and updating the Redux store accordingly, we've created a seamless synchronization between server data and application state, making our Todo application more robust and maintainable.