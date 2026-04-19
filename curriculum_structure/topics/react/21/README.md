# List and keys in React

Serial: 22
Made for: Beginner
Requirement: Must Have
Time in minutes: 45
Learning Objectives: List and Keys, State Management, useState
doc-id: react-22

### Key Concepts :

1. Updating arrays in state
2. List and keys and the importance of keys in lists

1. **Create Your React Project**:
    - Run `npm create vite@latest my-todo-app -- --template react` in your terminal to create a new project.
    - Enter the project directory: `cd my-todo-app`.
    - Install necessary dependencies: `npm install`.
    - Start your development server: `npm run dev`.

2. Building the Todo List Application

**App.jsx**:

```jsx
function App() {
  const [taskList, setTaskList] = useState([]);

  const addItem = (newTask) => {
    const updatedTaskList = [...taskList, newTask];
    setTaskList(updatedTaskList);
  };

  const deleteItem = (taskId) => {
    const updatedTaskList = taskList.filter((task) => task.id !== taskId);
    setTaskList(updatedTaskList);
  };

  const toggleItem = (taskId) => {
    const updatedTaskList = taskList.map((task) =>
      task.id === taskId ? { ...task, status: !task.status } : task
    );
    setTaskList(updatedTaskList);
  };

  return (
    <>
      <AddTodo addItem={addItem} />
      <div>
        <h5>List of tasks</h5>
        {taskList.map((task) => (
          <TaskItem
            key={task.id}
            {...task}
            deleteItem={deleteItem}
            toggleItem={toggleItem}
          />
        ))}
      </div>
    </>
  );
}
```

**AddTodo.jsx**:

```jsx
const AddTodo = ({ addItem }) => {
  const [taskName, setTaskName] = React.useState("");

  const handleAddButtonClick = () => {
    const newTask = {
      id: Date.now() + Math.random(),
      title: taskName,
      status: false,
    };
    addItem(newTask);
    setTaskName('');
  };

  return (
    <div className="add-todo">
      <input
        placeholder="Add your task here"
        onChange={(e) => setTaskName(e.target.value)}
        value={taskName}
      />
      <button onClick={handleAddButtonClick}>Add Todo</button>
    </div>
  );
};

```

**TaskItem.jsx**:

```jsx
const TaskItem = ({ id, title, status, deleteItem, toggleItem }) => {
  return (
    <div className="task-item">
      <p>{title}</p>
      <p>{status ? "Completed" : "Not Completed"}</p>
      <button onClick={() => deleteItem(id)}>Delete</button>
      <button onClick={() => toggleItem(id)}>Toggle Status</button>
    </div>
  );
};

```

**App Component**: 

Central component to manage state and render other components.

**State Management and Prop Passing**:

- The `App` component will handle the list of tasks using React's state.
- The `addItem`, `deleteItem`, and `toggleItem` functions will be passed down as props for respective actions on tasks.

### **Immutable State Updates** :

**Why Treat Arrays as Immutable in React?**

1. **JavaScript Arrays and Mutability**:
    - In JavaScript, arrays are mutable, meaning you can change their content directly.
    - However, when it comes to React state, this direct modification approach should be avoided.
2. **React's State and Immutability**:
    - React's state should be treated as immutable. Immutability in state management means not altering the state directly but rather creating a new version of it whenever changes are needed.
    - This approach ensures React can track changes efficiently and update the UI in a predictable manner.
    
    But Why ?
    
    **The Problems with Mutable Updates**
    
    1. **Direct Mutation Leads to Bugs**:
        - Directly mutating state (like using `push`, `pop`, or modifying `arr[0] = 'newValue'`) can lead to unexpected behaviors and bugs.
        - React may not detect these mutations, leading to the UI not re-rendering in response to state changes.
    2. **Reference Type Nature of Arrays**:
        - Arrays are reference types in JavaScript. Modifying an array directly alters the array in its original memory location, affecting every other part of your code that references it.
    
    **Correct Way to Update Arrays in State**
    
    1. **Creating New Arrays for Updates**:
        - To update an array in React state, always create a new array.
        - Utilize non-mutating methods like `map`, `filter` or spread syntax (`[...arr]`).
    2. **Reference Table for Array Operations in React**:
        
        
        | Avoid (Mutates the Array) | Prefer (Returns a New Array) |
        | --- | --- |
        | Adding: push, unshift | concat, [...arr, newItem] |
        | Removing: pop, shift, splice | filter, slice |
        | Replacing: splice, arr[i] = ... | map |
        | Sorting: reverse, sort | Copy the array first, then sort |
        - **Example for Adding**: Instead of `arr.push(newItem)`, use `[...arr, newItem]`.
        - **Example for Removing**: Replace `arr.splice(index, 1)` with `arr.filter((item, idx) => idx !== index)`.
        - **Example for Replacing**: Use `arr.map((item, idx) => idx === index ? newValue : item)` instead of `arr[index] = newValue`.
        - **Example for Sorting**: Copy the array using `[...arr]` before applying `sort()`.
        
    
    ### The Importance of Keys in Lists :
    
    1. **Key Prop in Rendering Lists**:
        - Assign a unique `key` prop to each item in a list for efficient rendering.
        - The `key` helps React identify and track each list item.
    2. **Performance Considerations**:
        - Proper key usage enhances performance by allowing React to reuse components and manage state effectively.

Summary : 

- Understanding state immutability, key usage, and component interaction are key takeaways.
- Treating arrays in state as immutable leads to better performance, fewer bugs, and more predictable UI updates.
- Understanding and applying these principles will help in building robust and efficient React applications.