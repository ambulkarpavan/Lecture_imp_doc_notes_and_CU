# React with Redux ( react-redux package used )

### Introduction

In this tutorial, we'll explore how to integrate Redux with React using the `react-redux` package. We'll refactor our previous counter application, removing the custom context-based approach in favor of `react-redux`'s `Provider` component and hooks like `useSelector` and `useDispatch`. This will showcase the streamlined process of state management in a React-Redux application.

### Project Structure

The revised project structure will be simplified:

```
- src
  - redux
    - action.js
    - actionTypes.js
    - reducer.js
    - store.js
- App.jsx
- index.js
```

### Redux Setup

### Actions (`action.js` and `actionTypes.js`)

Actions are JavaScript objects that convey information from your application to the Redux store. They are the only source of information for the store.

- **Action Types (`actionTypes.js`)**: Defines constants to help prevent typos and string mismatches in action types.
    
    ```jsx
    export const INC_COUNT = "INC_COUNT";
    export const DEC_COUNT = "DEC_COUNT";
    ```
    
- **Action Creators (`action.js`)**: Functions that create actions. It's a good practice to define action creators to decouple the creation of actions from the components.
    
    ```jsx
    export const incCount = (data) => ({
      type: INC_COUNT,
      payload: data
    });
    
    export const decCount = (data) => ({
      type: DEC_COUNT,
      payload: data
    });
    
    ```
    

### Reducer (`reducer.js`)

Reducers define how the state changes in response to actions sent to the store. They are pure functions that take the previous state and an action, and return the next state.

- **Reducer (`reducer.js`)**: Handles state transitions based on the received action types.
    
    ```jsx
    const initState = {
      value: 0
    };
    
    const reducer = (state = initState, action) => {
      switch (action.type) {
        case INC_COUNT:
          return { value: state.value + 1 };
        case DEC_COUNT:
          return { value: state.value - 1 };
        default:
          return state;
      }
    };
    
    export default reducer;
    ```
    

### Store (`store.js`)

The store brings actions and reducers together. It holds the application state and allows for state to be updated based on actions.

- **Store (`store.js`)**: Creates the Redux store by passing in the reducer.
    
    ```jsx
    import { createStore } from "redux";
    import reducer from "./reducer";
    
    const store = createStore(reducer);
    
    export { store };
    ```
    

### Integration with React using `react-redux`

### Root Component (`index.js`)

We wrap our application with `react-redux`'s `Provider` component, passing the store as a prop. This makes the Redux store available to any nested components that need to access the Redux store.

```jsx
import { createRoot } from 'react-dom/client';
import { Provider } from 'react-redux';
import { store } from './redux/store';
import App from './App';

const rootElement = document.getElementById('root');
const root = createRoot(rootElement);

root.render(
  <Provider store={store}>
    <App />
  </Provider>
);

```

### App Component (`App.jsx`)

Instead of using context, we'll use `react-redux`'s `useSelector` to read from the Redux store and `useDispatch` to dispatch actions.

```jsx
import { useSelector, useDispatch } from 'react-redux';
import { incCount, decCount } from './redux/action';
import './styles.css';

function App() {
  const value = useSelector((state) => state.value);
  const dispatch = useDispatch();

  return (
    <div className="App">
      <header className="App-header">
        <p>
          count is: {value}
          <button type="button" onClick={() => dispatch(incCount(1))}>
            INC
          </button>
          <button type="button" onClick={() => dispatch(decCount(1))}>
            DEC
          </button>
        </p>
      </header>
    </div>
  );
}

export default App;

```

### Benefits of Using `react-redux`

1. **Improved Performance:** `react-redux` optimizes performance by preventing unnecessary renders. Components only re-render when the data they need from the Redux store has changed.
2. **Simplified Code:** The `Provider` component makes the Redux store available to all nested components, and hooks like `useSelector` and `useDispatch` make it easy to interact with the Redux store without manually setting up context or subscriptions.
3. **Maintainability:** `react-redux` abstracts away the complex bindings between Redux and React, leading to cleaner, more maintainable code.

### Conclusion

In this tutorial, we refactored a counter application to use `react-redux`, illustrating the streamlined process and benefits of this integration. By using `react-redux`, we're able to write more readable and maintainable code, with the added benefits of optimized performance.