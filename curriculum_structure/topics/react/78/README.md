# Typescript React + useReducer

`useReducer` is a hook in React that is used for state management. It's an alternative to `useState` and is preferable when you have complex state logic that involves multiple sub-values or when the next state depends on the previous one. TypeScript can help ensure that the state transitions are predictable and that the state shape is well-defined.

Here’s an example of how you can use `useReducer` with TypeScript in a React component. We'll create a simple counter that increments, decrements, and resets the count.

### Step 1: Define the State and Action Types

First, define the types for your state and actions:

```tsx
type CounterState = {
  count: number;
};

type UpdateAction = {
  type: 'increment' | 'decrement';
  payload: number;
};

type ResetAction = {
  type: 'reset';
};

type CounterAction = UpdateAction | ResetAction;

```

In this code:

- `CounterState` represents the type of state used by the reducer (in this case, just a single `count` number).
- `CounterAction` is a union type for all actions that the reducer can handle. It can be an `UpdateAction` (increment or decrement by a payload value) or a `ResetAction` (reset the count to 0).

### Step 2: Create the Reducer

Next, define the reducer function. A reducer takes the current state and an action, and returns the new state:

```tsx
const counterReducer = (state: CounterState, action: CounterAction): CounterState => {
  switch (action.type) {
    case 'increment':
      return { count: state.count + action.payload };
    case 'decrement':
      return { count: state.count - action.payload };
    case 'reset':
      return { count: 0 };
    default:
      return state;
  }
};

```

### Step 3: Use the Reducer in a Component

Now you can use the `useReducer` hook in your component:

```tsx
import React, { useReducer } from 'react';

const Counter: React.FC = () => {
  const [state, dispatch] = useReducer(counterReducer, { count: 0 });

  return (
    <div>
      Count: {state.count}
      <button onClick={() => dispatch({ type: 'increment', payload: 1 })}>
        +
      </button>
      <button onClick={() => dispatch({ type: 'decrement', payload: 1 })}>
        -
      </button>
      <button onClick={() => dispatch({ type: 'reset' })}>
        Reset
      </button>
    </div>
  );
};

export default Counter;

```

In this component:

- `useReducer` is called with the `counterReducer` and an initial state.
- `dispatch` is used to dispatch actions to the reducer to update the state based on the action type and payload.

This example demonstrates how you can use `useReducer` with TypeScript in a React application, ensuring that both the state and actions are strongly typed for better predictability and maintainability of your code.