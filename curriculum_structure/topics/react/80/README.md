# Cypress Testing

### Overview

Cypress is an end-to-end testing framework designed to provide a robust testing environment for web applications. Its unique features and user-friendly approach make testing a more manageable and efficient process. It's particularly well-suited for applications built with libraries like React, offering real-time reloads, consistent results, and a variety of tools to simulate user interactions.

### Installation

### Setting Up the React Application

Before integrating Cypress, ensure you have a React application. If you're starting from scratch, create a new React app:

```bash
npx create-react-app my-app
cd my-app
```

### Installing Cypress

To add Cypress to your React project, run the following command in your project directory:

```bash
npm install cypress --save-dev
```

After installation, open `package.json` and add the following script to simplify the Cypress running process:

```json
"scripts": {
  "cypress:open": "cypress open"
}
```

### Building Applications

### 1. Basic Counter Application

### Code Structure

- **`Counter.js`**: A simple counter component with increment and decrement functionality.

### Implementation

```jsx
// src/components/Counter.js
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h2 data-cy="counter-value">{count}</h2>
      <button data-cy="increment-btn" onClick={() => setCount(count + 1)}>Increment</button>
      <button data-cy="decrement-btn" onClick={() => setCount(count - 1)}>Decrement</button>
    </div>
  );
}

export default Counter;

```

### 2. TodoList Application

### Code Structure

- **`TodoList.js`**: A component that displays a list of todos and allows users to add new items.

### Implementation

```jsx
// src/components/TodoList.js
import React, { useState } from 'react';

function TodoList() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState('');

  const addTodo = () => {
    if (input) {
      setTodos([...todos, input]);
      setInput('');
    }
  };

  return (
    <div>
      <input data-cy="todo-input" value={input} onChange={(e) => setInput(e.target.value)} />
      <button data-cy="add-todo-btn" onClick={addTodo}>Add Todo</button>
      <ul>
        {todos.map((todo, index) => (
          <li key={index} data-cy={`todo-item-${index}`}>{todo}</li>
        ))}
      </ul>
    </div>
  );
}

export default TodoList;

```

### Testing with Cypress

### 1. Writing Tests for the Counter Application

Create a new test file under `cypress/integration/counter_spec.js` and add the following test:

```jsx
// cypress/integration/counter_spec.js
describe('Counter Tests', () => {
  beforeEach(() => {
    cy.visit('/')
  });

  it('increments the counter', () => {
    cy.get('[data-cy=counter-value]').should('contain', '0');
    cy.get('[data-cy=increment-btn]').click();
    cy.get('[data-cy=counter-value]').should('contain', '1');
  });

  it('decrements the counter', () => {
    cy.get('[data-cy=counter-value]').should('contain', '0');
    cy.get('[data-cy=decrement-btn]').click();
    cy.get('[data-cy=counter-value]').should('contain', '-1');
  });
});

```

### 2. Writing Tests for the TodoList Application

Create a new test file under `cypress/integration/todoList_spec.js` and add the following test:

```jsx
// cypress/integration/todoList_spec.js
describe('TodoList Tests', () => {
  beforeEach(() => {
    cy.visit('/')
  });

  it('adds a new todo item', () => {
    cy.get('[data-cy=todo-input]').type('Learn Cypress');
    cy.get('[data-cy=add-todo-btn]').click();
    cy.get('[data-cy=todo-item-0]').should('contain', 'Learn Cypress');
  });
});

```

### Running Tests

To run your Cypress tests, use the script you added to `package.json`:

```bash
npm run cypress:open
```

Cypress will open a testing window where you can see your test suite and interact with the tests as they run.

By following these steps, you can effectively integrate Cypress into your React applications.

---

Now we'll create a React component that fetches data from a mock API ([https://jsonplaceholder.typicode.com/todos](https://jsonplaceholder.typicode.com/todos)) and saves the response to the component's state. We will then write a test case using Cypress to verify that the component correctly fetches and displays the data.

### Building the TodoFetcher Component

### TodoFetcher Component Implementation

Create a file named `TodoFetcher.js` in your `src/components` directory and add the following code:

```jsx
// src/components/TodoFetcher.js
import React, { useState, useEffect } from 'react';

function TodoFetcher() {
  const [todos, setTodos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/todos')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setTodos(data);
        setLoading(false);
      })
      .catch(error => {
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <ul>
      {todos.map(todo => (
        <li key={todo.id} data-cy={`todo-item-${todo.id}`}>{todo.title}</li>
      ))}
    </ul>
  );
}

export default TodoFetcher;

```

This component fetches data from the provided API endpoint and renders a list of todos. It handles loading state and possible errors during the data fetching process.

### Testing the TodoFetcher Component with Cypress

### 1. Writing the Test

Create a new test file under `cypress/integration/todoFetcher_spec.js` and add the following test:

```jsx
// cypress/integration/todoFetcher_spec.js
describe('TodoFetcher Tests', () => {
  beforeEach(() => {
    cy.intercept('GET', 'https://jsonplaceholder.typicode.com/todos', { fixture: 'todos.json' }).as('getTodos');
    cy.visit('/');
  });

  it('fetches and displays todos', () => {
    cy.wait('@getTodos');
    cy.get('[data-cy^=todo-item-]').should('have.length', 5); // Assuming todos.json contains 5 items
  });
});

```

In this test, `cy.intercept` is used to intercept the network request to the API and respond with data from a fixture file (`todos.json`). The `cy.wait` command ensures that the request completes before making assertions about the DOM elements.

### 2. Adding Fixture

Create a file named `todos.json` in your `cypress/fixtures` directory. Add your mock todo data in the following format:

```json
// cypress/fixtures/todos.json
[
  { "id": 1, "title": "Todo 1" },
  { "id": 2, "title": "Todo 2" },
  { "id": 3, "title": "Todo 3" },
  { "id": 4, "title": "Todo 4" },
  { "id": 5, "title": "Todo 5" }
]

```

This JSON file will serve as the mock response for your API calls during testing.

### Running the Test

To run your Cypress tests, use the script you added to `package.json`:

```bash
npm run cypress:open
```

Cypress will open a testing window where you can see your test suite and interact with the tests as they run.

By following these steps, you've created a React component that fetches data from an API and displays it. You've also written a Cypress test to verify that the component behaves as expected, ensuring that your application functions correctly and is stable.