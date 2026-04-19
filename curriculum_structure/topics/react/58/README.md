# MVC, Flux and Redux

### Introduction

In the journey of web application development, understanding the evolution of architectural patterns is pivotal. MVC, Flux, and Redux represent milestones in managing application states and data flow. This lesson will not only delve into each architecture but also discuss the challenges faced with MVC that led to the development of Flux by Facebook, and how Redux further refined the concepts introduced by Flux.

### 1. MVC (Model-View-Controller) Architecture and Its Challenges

![Screenshot 2022-12-22 at 9.09.51 PM.png](MVC,%20Flux%20and%20Redux%20c264f9eb27d2441e905796d4b9f899c8/Screenshot_2022-12-22_at_9.09.51_PM.png)

### Detailed Explanation

**Model-View-Controller (MVC)** is a software design pattern that separates the application into three main logical components: Model, View, and Controller, each with distinct responsibilities. However, as applications grew more complex, the bidirectional data flow of MVC made it difficult to debug and understand, especially with multiple views affecting the model and vice versa.

### Problem Encountered by Facebook

Facebook encountered significant challenges with MVC as their application scaled. The main issue was the "spaghetti" of callbacks due to the intricate web of models and views affecting each other. This complexity made the application unpredictable and hard to maintain, as a change in one part of the application could have unexpected effects in other parts.

### 2. Flux Architecture: Facebook's Solution

### Detailed Explanation

To address the shortcomings of MVC, Facebook introduced **Flux**. Flux maintains a unidirectional data flow which makes the application more predictable and easier to understand. It introduced a new component, the Dispatcher, as a central hub for all data flow in the application, thus eliminating the cascade of updates prevalent in MVC.

### Use-case & Benefits

- **Use-case**: Flux is ideal for complex applications with multiple dynamic user interfaces and data sources.
- **Benefits**:
    - More predictable data flow and easier debugging.
    - Decoupled components that are easier to maintain and test.

### 3. Redux Architecture: Refinement over Flux

### Detailed Explanation

**Redux** is a predictable state container for JavaScript applications, inspired by Flux but with significant improvements:

- **Single Source of Truth**: Redux uses a single store for the entire application's state, making state management more predictable.
- **Immutability**: State is immutable, preventing unpredictable mutations and ensuring pure functions in reducers.

### Comparison with Flux & Its Advantages

- **Simplicity**: Redux simplifies the dispatcher-store relationship by using a single store and a strict reducer pattern, making it easier to reason about the application state.
- **Middleware**: Redux supports middleware, allowing for more flexible and powerful handling of side effects.
- **Ecosystem and Tooling**: Redux has a rich ecosystem and powerful development tools like Redux DevTools.

### Did Redux Replace Flux?

Redux offered a more refined approach to state management, leading to its popularity. While it didn't replace Flux entirely (as some projects may still use Flux for specific reasons), it became the more favored choice for state management in the React ecosystem due to its simplicity and powerful features.

### Demonstrating MVC, Flux, and Redux with an Example

Let's take a simple example of a counter application and see how it is implemented in MVC, Flux, and Redux.

- **Example**: A counter application where a user can increment or decrement the count.

### MVC Implementation:

```jsx
// Model
let count = 0;

// View
function render() {
    document.getElementById('counter').innerText = count;
}

// Controller
document.getElementById('increment').addEventListener('click', () => {
    count++;
    render();
});
document.getElementById('decrement').addEventListener('click', () => {
    count--;
    render();
});

render();

```

### Flux Implementation:

```jsx
// Dispatcher
const dispatcher = new Flux.Dispatcher();

// Store
const counterStore = {
  count: 0,
  getCount: function() {
    return this.count;
  },
  dispatcherIndex: dispatcher.register(function(payload) {
    if (payload.actionType === 'INCREMENT') {
      counterStore.count++;
      render();
    } else if (payload.actionType === 'DECREMENT') {
      counterStore.count--;
      render();
    }
    return true; // No errors. Needed by promise in Dispatcher.
  }),
};

// View & Controller
function render() {
    document.getElementById('counter').innerText = counterStore.getCount();
    document.getElementById('increment').onclick = () =>
        dispatcher.dispatch({ actionType: 'INCREMENT' });
    document.getElementById('decrement').onclick = () =>
        dispatcher.dispatch({ actionType: 'DECREMENT' });
}

render();

```

### Redux Implementation:

```jsx
// Reducer
function counter(state = 0, action) {
  switch (action.type) {
    case 'INCREMENT':
      return state + 1;
    case 'DECREMENT':
      return state - 1;
    default:
      return state;
  }
}

// Store
const { createStore } = Redux;
const store = createStore(counter);

// View & Controller
const render = () => {
  document.getElementById('counter').innerText = store.getState();
};

store.subscribe(render);
render();

document.getElementById('increment').addEventListener('click', () => {
    store.dispatch({ type: 'INCREMENT' });
});
document.getElementById('decrement').addEventListener('click', () => {
    store.dispatch({ type: 'DECREMENT' });
});

```

In this lesson, we've explored the intricacies of MVC, Flux, and Redux, understanding their evolution, advantages, and use cases. We also saw how each architecture could be implemented in a simple counter application, highlighting the differences in their approaches to managing state and data flow.