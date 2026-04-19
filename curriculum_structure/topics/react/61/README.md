# React with Redux ( react-redux package not used )

This React application is managing state using Redux without the `react-redux` package. Instead, it employs a combination of React Context and Redux to share state across components. Let's break down the lesson with this approach in mind, focusing on the importance of the `react-redux` package by highlighting what it abstracts away and why it's commonly used.

### Introduction

In this lesson, we delve into a unique approach to state management in a React application. We explore how Redux is paired with React Context to manage and distribute application state without utilizing the `react-redux` package. This method illuminates the foundational concepts of Redux and the additional conveniences provided by `react-redux`.

### Detailed Explanation

### Redux Architecture without `react-redux`

Redux is a state management library that provides a predictable way to structure and update the state in a JavaScript application. It is often used with React but doesn't depend on it.

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
    

### React Context as a Store Connector (`CounterContext.jsx`)

Instead of using `react-redux` for connecting the Redux store to React components, this application uses the React Context API to pass down the store and dispatch function.

- **CounterContext (`CounterContext.jsx`)**: Provides a way for React components to subscribe to Redux store updates and dispatch actions.
    
    ```jsx
    import React from "react";
    
    export const CounterContext = React.createContext();
    
    export const CounterContextProvider = ({ children, store }) => {
      const { dispatch, getState, subscribe } = store;
      const [flag, setFlag] = React.useState(true);
    
      const forceUpdate = () => setFlag((prev) => !prev);
    
      subscribe(forceUpdate);
    
      return (
        <CounterContext.Provider value={{ dispatch, getState }}>
          {children}
        </CounterContext.Provider>
      );
    };
    
    ```
    

The code snippet `const [flag, setFlag] = React.useState(true);` along with the `forceUpdate` function in the `CounterContext.jsx` file is a creative workaround to force a React component to re-render whenever the Redux store state changes.

Here's a breakdown of what's happening:

1. **State Declaration with `useState`:**
    - `const [flag, setFlag] = React.useState(true);` is using React's `useState` hook to declare a piece of state named `flag`. This is a common pattern, but in this context, the actual value of `flag` is not important. The purpose is not to track some meaningful data for the component but rather to have a state variable that we can toggle to force the component to re-render.
2. **Force Update Function:**
    - `const forceUpdate = () => setFlag((prev) => !prev);` defines a function that toggles the value of `flag`. By calling `setFlag` and changing the state, it causes the component to re-render. This is a trick to force a component to update itself because React components naturally re-render when their state changes.
3. **Subscribing to Store Changes:**
    - `subscribe(forceUpdate);` is calling the `subscribe` method from the Redux store. The `subscribe` method is used to add a change listener. It will run every time an action is dispatched, and the Redux store state has potentially changed.
    - By passing `forceUpdate` to `subscribe`, you're telling Redux to execute `forceUpdate` (which toggles the `flag` state) whenever an action is dispatched and the store's state might have been updated. This ensures that the component re-renders in response to state changes in the Redux store.
4. **Providing Context:**
    - The `CounterContext.Provider` is used to provide the `dispatch` and `getState` functions from the Redux store to any child components. They can use these to dispatch actions and access the current state.

### Why is this necessary?

In a typical setup with `react-redux`, the `connect` function or the `useSelector` hook automatically ensures that your component re-renders when the Redux store state changes. However, in this custom setup where `react-redux` is not being used, such automatic re-rendering doesn't happen. The `flag` state and `forceUpdate` function are used as a manual way to ensure that the component re-renders in response to Redux state changes.

This method is less efficient and more cumbersome than using `react-redux`, which is designed to handle these updates optimally. It's a clear demonstration of the additional complexities you have to manage when not using `react-redux` and a testament to the convenience and performance optimizations `react-redux` provides.

### Use-case & Benefits

Understanding Redux without `react-redux` can deepen your understanding of the core principles of Redux. It also highlights the convenience and additional features provided by `react-redux`, such as the `connect` function and `useSelector`, and `useDispatch` hooks, which abstract away the context usage and provide performance optimizations.

### Integration in React (`App.jsx` and `index.js`)

React components interact with the Redux store. Normally, this would be through the `connect` function from `react-redux` or hooks like `useSelector` and `useDispatch`. In this case, the interaction is direct through the context.

- **Root Component (`index.js`)**: Wraps the `App` component with `CounterContextProvider` to provide the Redux store context.
    
    ```jsx
    import { createRoot } from "react-dom/client";
    import { CounterContextProvider } from "./context/CounterContext";
    import App from "./App";
    
    const rootElement = document.getElementById("root");
    const root = createRoot(rootElement);
    
    root.render(
      <CounterContextProvider store={store}>
        <App />
      </CounterContextProvider>
    );
    
    ```
    
- **App Component (`App.jsx`)**: Consumes the `CounterContext` and dispatches actions based on user interactions.
    
    ```jsx
    import { useContext } from "react";
    import { CounterContext } from "./context/CounterContext";
    import { incCount, decCount } from "./redux/action";
    
    function App() {
      const { getState, dispatch } = useContext(CounterContext);
      return (
        <div className="App">
          <header className="App-header">
            <p>
              count is: {getState().value}
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
    

### Usage

In this setup, components interact with the Redux store by consuming the React Context (`CounterContext`) instead of using `react-redux`. It requires manually subscribing to the store and forcing component updates, which `react-redux` would handle more efficiently.

### Instructor Activity with Code Examples

In this section, we would demonstrate how to add a new action and modify the state, focusing on how to bind the action to a component event.

### Learner Activity

Learners could be tasked with adding a new feature, such as resetting the counter, requiring them to understand and interact with the Redux store and React context.

### Learner Activity Solution

We would provide a detailed walkthrough of implementing the new feature, showcasing the necessary changes in actions, reducers, and components.

This lesson outlines the architecture and integration of Redux in a React application without using the `react-redux` package, emphasizing the foundational concepts and appreciating the benefits that `react-redux` introduces.