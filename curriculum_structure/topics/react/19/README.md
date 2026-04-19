# Vite

Serial: 20
Made for: Beginner
Requirement: Must Have
Time in minutes: 20
Learning Objectives: State Management, useState
doc-id: react-20

# Vite :

Vite is a modern, fast build tool for web projects, including React applications. It serves as an alternative to older tools like Webpack. The main advantage of Vite is its speed, primarily because it leverages modern JavaScript features and avoids unnecessary work during development.

# Why Use Vite for React ?

1. **Speed**: Vite significantly speeds up the development process. It uses ES Modules, which allows your browser to understand your JavaScript code directly without extensive processing.
2. **Hot Module Replacement (HMR)**: Vite offers a faster HMR, which means you can see your changes in real-time without refreshing the entire page or losing the current state.
3. **Simplicity**: Setting up a React project with Vite is straightforward, requiring minimal configuration.
4. **Modern JavaScript**: It's built to work with the latest JavaScript features, making your development process smoother.

# Getting Started with Vite for a React Application

### Step-by-Step Guide :

1. **Install Node.js**: Ensure you have `Node.js` and `npm` installed on your computer. You can check your current `node` and `npm` version by
    
    ```jsx
    node -v
    ```
    
    ```jsx
    npm -v
    ```
    
2. **Create a New Project**: Open your terminal and run:
    
    ```jsx
    npm create vite@latest <name-of-project> -- --template react
    ```
    
    This command creates a new directory with whatever name you have given to your project in the above command with a basic React setup using Vite.
    
3. **Navigate to Your Project**:
    
    ```bash
    cd <name-of-project>
    ```
    
4. **Install Dependencies**:
    
    ```bash
    npm install
    ```
    
    This command installs all the necessary dependencies for your project.
    
5. **Start the Development Server**:
    
    ```bash
    npm run dev
    ```
    
    This command starts a local development server. You can view your app by going to `http://localhost:3000` in your browser.
    

# Understanding the Project Structure

After creating your project, you'll notice several files and folders:

- `node_modules/`: Contains all the packages and dependencies your project needs.
- `public/`: Stores static assets like images.
- `src/`: This is where you'll spend most of your time. It contains your React components.
    - `App.jsx`: The main React component.
    - `main.jsx`: The entry point for your application, where React is rendered into the DOM.
- `index.html`: The base HTML file.
- `vite.config.js`: The configuration file for Vite, typically requiring little to no changes for basic projects.
- `package.json`: Lists your project dependencies and scripts.

# Building a Counter with State in Vite

Let's create a simple counter application:

1. **Modify `App.jsx`**:
Open `src/App.jsx` and replace its content with:
    
    ```jsx
    import React from "react";
    
    function App() {
      const [count, setCount] = React.useState(0);
    
      function increment() {
        setCount(count + 1);
      }
    
      function decrement() {
        setCount(count - 1);
      }
    
      return (
        <div>
          <h1>Counter: {count}</h1>
          <button onClick={increment}>Increase</button>
          <button onClick={decrement}>Decrease</button>
        </div>
      );
    }
    
    export default App;
    ```
    
    Here, you're using the `useState` hook to manage the state of your counter.
    
2. **View Your Application**:
If your development server is running, you should see the counter in your browser. Click the buttons to increase or decrease the count.

# Conclusion

That's a basic introduction to using Vite with React. Vite simplifies the setup process, offers faster development experiences, and allows you to focus on building your React application efficiently. As you progress, you'll find Vite to be a powerful tool in your React development toolkit.