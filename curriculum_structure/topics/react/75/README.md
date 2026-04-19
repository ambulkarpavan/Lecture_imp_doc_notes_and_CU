# React + Typescript

Using TypeScript with React is a great choice as it brings the benefits of strong typing and helps catch errors early during the development phase. Here's how you can set up and use TypeScript in a React project:

### Step 1: Project Setup

### 1.1 Creating the Project

Create a new project using Vite and the React TypeScript template:

```bash
npm create vite@latest my-todo-app --template react-ts
cd my-todo-app
npm install
```

### 1.2 Installing Dependencies

Install the necessary packages, including `uuid` for unique ID generation:

```bash
npm install
npm install uuid

```

Step 2: Define TypeScript Types

**Using hooks with Typescript**

```jsx
import React, { useState } from 'react';

const Counter: React.FC = () => {
  const [count, setCount] = useState<number>(0); // `count` is inferred to be a number

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
};

export default Counter;
```

Or you can even have a separate file wherein you describe types. 

In out todo app,  `src/types.ts`, define the structure of a todo item:

```tsx
// src/types.ts
export interface Todo {
  id: string;
  title: string;
  isCompleted: boolean;
}
```

### Step 3: Building the Application

### Project Structure

```jsx
my-todo-app/
│
├── node_modules/                  # Folder for all of your project's dependencies
│
├── src/                           # Source files
│   ├── components/                # Folder for React components
│   │   ├── AddTodo.tsx            # Component to add new todos
│   │   └── TodoItem.tsx           # Component to display individual todo items
│   │
│   ├── types.ts                   # TypeScript type definitions for your project
│   ├── App.tsx                    # Main application component
│   └── main.tsx                   # Entry point for your application
├── index.html                     # Root HTML file where the React tree gets injected
├── package.json                   # Project manifest with metadata, dependencies, and scripts
├── tsconfig.json                  # Configuration for the TypeScript compiler
├── vite.config.ts                 # Configuration for Vite
└── README.md                      # README file with information about the project
```

### 3.1 Define State and Context in `App.tsx`

In `src/App.tsx`, set up the state and provide a context for the todo list. Use `uuid` to generate unique IDs for new todos:

```tsx
// src/App.tsx
import React, { useState } from 'react';
import { v4 as uuidv4 } from 'uuid';
import { Todo } from './types';
import TodoItem from './components/TodoItem';
import AddTodo from './components/AddTodo';

const App: React.FC = () => {
  const [todos, setTodos] = useState<Todo[]>([]);

  const addTodo = (title: string) => {
    const newTodo: Todo = {
      id: uuidv4(),
      title,
      isCompleted: false,
    };
    setTodos([...todos, newTodo]);
  };

  const toggleCompletion = (id: string) => {
    setTodos(
      todos.map(todo =>
        todo.id === id ? { ...todo, isCompleted: !todo.isCompleted } : todo,
      ),
    );
  };

  const deleteTodo = (id: string) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  return (
    <div className="App">
      <h1>Todo List</h1>
      <AddTodo addTodo={addTodo} />
      {todos.map(todo => (
        <TodoItem
          key={todo.id}
          todo={todo}
          toggleCompletion={toggleCompletion}
          deleteTodo={deleteTodo}
        />
      ))}
    </div>
  );
};

export default App;

```

### 3.2 Create the `TodoItem` Component

In `src/components/TodoItem.tsx`, create a component to display each todo. Note that the `id` is now of type `string`:

```tsx
// src/components/TodoItem.tsx
import React from 'react';
import { Todo } from '../types';

interface Props {
  todo: Todo;
  toggleCompletion: (id: string) => void;
  deleteTodo: (id: string) => void;
}

const TodoItem: React.FC<Props> = ({ todo, toggleCompletion, deleteTodo }) => (
  <div>
    <input
      type="checkbox"
      checked={todo.isCompleted}
      onChange={() => toggleCompletion(todo.id)}
    />
    <span style={{ textDecoration: todo.isCompleted ? 'line-through' : 'none' }}>
      {todo.title}
    </span>
    <button onClick={() => deleteTodo(todo.id)}>Delete</button>
  </div>
);

export default TodoItem;

```

### 3.3 Create the `AddTodo` Component

In `src/components/AddTodo.tsx`, create a component to add new todos. No changes are needed here from the previous version:

```tsx
// src/components/AddTodo.tsx
import React, { useState } from 'react';

interface Props {
  addTodo: (title: string) => void;
}

const AddTodo: React.FC<Props> = ({ addTodo }) => {
  const [title, setTitle] = useState('');

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!title.trim()) return;
    addTodo(title);
    setTitle('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={title}
        onChange={e => setTitle(e.target.value)}
        placeholder="Add a new task..."
      />
      <button type="submit">Add</button>
    </form>
  );
};

export default AddTodo;

```

### Step 4: Styling the Components

Add or update styles in `src/App.css`. Import the styles in `src/main.tsx` 

```css
/* src/App.css */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 20px;
  background-color: #f4f4f4;
}

.App {
  max-width: 600px;
  margin: 0 auto;
}

input[type="text"] {
  margin-right: 10px;
}

.todo-item {
  background-color: white;
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.todo-item input[type="checkbox"] {
  margin-right: 10px;
}

button {
  background-color: #ff6b6b;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  opacity: 0.9;
}
```

### Step 5: Run the Application

Run the application:

```bash
npm run dev
```