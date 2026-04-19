# Introduction to Redux ( No React )

In this lesson, we will explore the Redux library, a predictable state container for JavaScript applications. We'll start from creating a Redux-like setup using vanilla JavaScript to implementing Redux itself. This approach will help you understand that Redux is a standalone library and can be used with plain JavaScript before integrating it with frameworks like React.

![Introduction%20to%20Redux%20(%20No%20React%20)%2087a702f5fdee4aa6b61b2306fb39e6e8/flux-simple-f8-diagram-with-client-action-1300w.png](Introduction%20to%20Redux%20(%20No%20React%20)%2087a702f5fdee4aa6b61b2306fb39e6e8/flux-simple-f8-diagram-with-client-action-1300w.png)

### Key Concepts of Redux

1. **Actions:**
Actions in Redux are plain JavaScript objects that represent an intention to change the state. They have a `type` field to describe the action and may have a `payload` to carry any information that should be processed.
    
    ```jsx
    {
      type: "INC_COUNT", // The type of action
      payload: 1 // Data needed for the update
    }
    
    ```
    
2. **Store:**
The store is the object that brings actions and reducers together. It holds the application state, allows access to the state via `getState()`, allows state to be updated via `dispatch(action)`, and registers listeners via `subscribe(listener)`.
    
    ```jsx
    { counter: 0, todos: [] }
    ```
    
3. **Dispatch:**
Dispatch is a function that you call with an action object. The store's reducing function will be called with the current `getState()` result and the given `action` synchronously. Its return value will be considered the next state.
    
    ```jsx
    dispatch({ type: "ADD_COUNT", payload: 1 })
    ```
    
4. **View:**
The view is the presentation part, usually UI components that display the data.

### Building Our Own Redux-like Implementation

We'll first create our own mini-version of Redux to understand its internals. This will involve creating our own `reducer`, `store`, and `dispatch` mechanism.

1. **Reducer Function:**
The reducer is a pure function that takes the current state and an action, and returns the next state.
    
    ```jsx
    const reducer = (store, action) => {
      switch (action.type) {
        case "INC_COUNT":
          return { ...store, count: store.count + action.payload };
        case "DEC_COUNT":
          return { ...store, count: store.count - action.payload };
        case "ADD_TODO":
          return { ...store, todos: [...store.todos, action.payload] };
        default:
          return store;
      }
    };
    
    ```
    
2. **Store Class:**
Our store will be a simple class that keeps the state and the reducer.
    
    ```jsx
    class Store {
      constructor(reducer, initialState) {
        this.reducer = reducer;
        this.state = initialState;
      }
    
      getState() {
        return this.state;
      }
    
      dispatch(action) {
        this.state = this.reducer(this.state, action);
      }
    }
    ```
    
3. **Using Our Store:**
We create an instance of our `Store` class, pass in the reducer and the initial state, and then test dispatching some actions.
    
    ```jsx
    const initState = { count: 0, todos: [] };
    const store = new Store(reducer, initState);
    console.log(store.getState());
    store.dispatch({ type: "INC_COUNT", payload: 1 });
    console.log(store.getState());
    
    ```
    

### Complete Code :

Before Restructure : 

index.js

```jsx
import { createStore } from "redux";

const reducer = (store, action) => {
  switch (action.type) {
    case "INC_COUNT":
      return { ...store, count: store.count + action.payload };
    case "DEC_COUNT":
      return { ...store, count: store.count - action.payload };
    case "ADD_TODO":
      return { ...store, todos: [...store.todos, action.payload] };
    default:
      return store;
  }
};

class Store {
  constructor(reducer, initialState) {
    this.reducer = reducer;
    this.state = initialState;
  }

  getState() {
    return this.state;
  }

  dispatch(action) {
    this.state = this.reducer(this.state, action);
  }
}

const initState = { count: 0, todos: [] };

const store = createStore(reducer, initState); 

console.log(store.getState()); // { count: 0, todos: [] }

store.dispatch({ type: "INC_COUNT", payload: 1 });
store.dispatch({ type: "INC_COUNT", payload: 1 });
store.dispatch({ type: "INC_COUNT", payload: 1 });
store.dispatch({ type: "INC_COUNT", payload: 1 });
console.log(store.getState()); // { count: 4, todos: [] }
store.dispatch({ type: "DEC_COUNT", payload: 1 });
console.log(store.getState()); // { count: 3, todos: [] }
store.dispatch({ type: "ADD_TODO", payload: { title: "Eat", status: false } });
console.log(store.getState()); // { count: 3, todos: [ { title: 'Eat', status: false } ] }
store.dispatch({
  type: "ADD_TODO",
  payload: { title: "Sleep", status: false },
});
console.log(store.getState()); /* {
  count: 3,
  todos: [
    { title: 'Eat', status: false },
    { title: 'Sleep', status: false }
  ]
}
*/
```

After Restructure : 

Project Structure : 

```jsx
- index.js
- redux
	- action.js
	- actionTypes.js
	- ownReduxStore.js
	- reducer.js
	- store.js
```

action.js

```jsx
import { INC_COUNT, DEC_COUNT, ADD_TODO } from "./actionTypes.js";

export const incCount = (data) => ({ type: INC_COUNT, payload: data });

export const decCount = (data) => ({ type: DEC_COUNT, payload: data });

export const addTodo = (data) => ({ type: ADD_TODO, payload: data });
```

actionTypes.js

```jsx
export const INC_COUNT = "INC_COUNT";
export const DEC_COUNT = "DEC_COUNT";
export const ADD_TODO = "ADD_TODO";
```

ownReduxStore.js

```jsx
export class Store {
  constructor(reducer, initialState) {
    this.reducer = reducer;
    this.state = initialState;
  }

  getState() {
    return this.state;
  }

  dispatch(action) {
    this.state = this.reducer(this.state, action);
  }
}
```

reducer.js

```jsx
import { INC_COUNT, DEC_COUNT, ADD_TODO } from "./actionTypes.js";

export const reducer = (store, action) => {
  switch (action.type) {
    case INC_COUNT:
      return { ...store, count: store.count + action.payload };
    case DEC_COUNT:
      return { ...store, count: store.count - action.payload };
    case ADD_TODO:
      return { ...store, todos: [...store.todos, action.payload] };
    default:
      return store;
  }
};
```

store.js

```jsx
import { Store } from "./ownRedux.js";
import { reducer } from "./reducer.js";

const initState = { count: 0, todos: [] };

const store = new Store(reducer, initState);

export { store };
```

index.js

```jsx
import { addTodo, incCount, decCount } from "./redux/action.js";
import { store } from "./redux/store.js";

console.log(store.getState());

store.dispatch(incCount(1));
store.dispatch(incCount(1));
store.dispatch(incCount(1));
store.dispatch(incCount(1));

console.log(store.getState());

store.dispatch(decCount(1));
store.dispatch(decCount(1));
console.log(store.getState());
store.dispatch(addTodo({ title: "Eat", status: false }));
console.log(store.getState());
store.dispatch(addTodo({ title: "Sleep", status: false }));
console.log(store.getState());
```

---

### Transitioning to Redux

Once we understand how our mini-version works, we transition to using the actual Redux library. This involves:

1. Installing Redux:
    
    ```bash
    npm init -y
    npm install redux;
    ```
    
2. Using `createStore` from Redux:
    
    ```jsx
    import { createStore } from "redux";
    const store = createStore(reducer, initState);
    ```
    
3. Dispatching actions and viewing the updated state:
    
    ```jsx
    store.dispatch({ type: "INC_COUNT", payload: 1 });
    console.log(store.getState());
    ```
    

store.js

```jsx
import { legacy_createStore as createStore } from "redux";
import { reducer } from "./reducer.js";

const initState = { count: 0, todos: [] };

const store = createStore(reducer, initState);

export { store };
```

### Structuring the Redux Application

Finally, we structure our application by separating action creators, action types, reducers, and the store into different files and directories, promoting modularity and maintainability.

```
.
├── index.js
├── redux
│   ├── action.js
│   ├── actionTypes.js
│   ├── reducer.js
│   └── store.js
├── package.json
└── package-lock.json

```

This structured approach not only makes the codebase cleaner but also prepares you for larger, more complex applications where such organization is essential.

In conclusion, this lesson provides a thorough understanding of Redux, its core principles, how to implement a Redux-like system from scratch, and how to transition to using Redux in a structured manner. This solid foundation will be beneficial as you move on to integrate Redux with UI frameworks like React.