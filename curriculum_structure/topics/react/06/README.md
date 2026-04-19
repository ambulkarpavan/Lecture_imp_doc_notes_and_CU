# Components and Props - Let’s visualise

Serial: 6
Made for: Beginner
Requirement: Must Have
Time in minutes: 20
Learning Objectives: Components, Props
doc-id: react-6

A React application is fundamentally just a **component** - which is made up of other **components** - which is made up of other **components** and so on and so forth, to great depth. Let’s say we start with basic code for understanding. Your web application `App()` is made of different parts like `Navbar` `Sidebar` `Main` `Footer` and all of these are component including the `App()` itself. 

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <style>
      * {
        margin: 0;
      }
      .navbar {
        background-color: lightgray;
      }
      .sidebar {
        background-color: lightsalmon;
        flex: 1;
      }
      .main {
        background-color: lightpink;
        flex: 3;
      }
      .middle-section {
        display: flex;
      }
      .footer {
        background-color: lightsteelblue;
      }
    </style>
    <title>react-5 | example-4</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="https://unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
    <script src="https://unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script type="text/babel">
      function Navbar() {
        return <div className="navbar">NAVBAR</div>;
      }
      function Sidebar() {
        return <div className="sidebar">SIDEBAR</div>;
      }
      function Main() {
        return <div className="main">MAIN</div>;
      }
      function Footer() {
        return <div className="footer">FOOTER</div>;
      }

      function App() {
        return (
          <>
            <Navbar />
            <div className="middle-section">
              <Sidebar />
              <Main />
            </div>
            <Footer />
          </>
        );
      }
      const reactRoot = ReactDOM.createRoot(document.getElementById("root"));

      reactRoot.render(<App />);
    </script>
  </body>
</html>
```

![Screenshot 2023-12-21 at 4.07.01 PM.png](Components%20and%20Props%20-%20Let%E2%80%99s%20visualise%20119c51a72da7423f9defc17ad6c1a4ed/Screenshot_2023-12-21_at_4.07.01_PM.png)

If you could go through Twitter’s homepage, there's the level of depth. It's a lot of components making up of other components. 

Think of the entire page as an App component

![1.png](Components%20and%20Props%20-%20Let%E2%80%99s%20visualise%20119c51a72da7423f9defc17ad6c1a4ed/1.png)

The App is made up of several components - Animated preview

![2.gif](Components%20and%20Props%20-%20Let%E2%80%99s%20visualise%20119c51a72da7423f9defc17ad6c1a4ed/2.gif)

Individual component

![3.png](Components%20and%20Props%20-%20Let%E2%80%99s%20visualise%20119c51a72da7423f9defc17ad6c1a4ed/3.png)

![4.png](Components%20and%20Props%20-%20Let%E2%80%99s%20visualise%20119c51a72da7423f9defc17ad6c1a4ed/4.png)

![5.png](Components%20and%20Props%20-%20Let%E2%80%99s%20visualise%20119c51a72da7423f9defc17ad6c1a4ed/5.png)

![6.png](Components%20and%20Props%20-%20Let%E2%80%99s%20visualise%20119c51a72da7423f9defc17ad6c1a4ed/6.png)

![7.png](Components%20and%20Props%20-%20Let%E2%80%99s%20visualise%20119c51a72da7423f9defc17ad6c1a4ed/7.png)

If we zoom into the feed component it is again made up of a list of tweet component

![Untitled](Components%20and%20Props%20-%20Let%E2%80%99s%20visualise%20119c51a72da7423f9defc17ad6c1a4ed/Untitled.png)

If we zoom into the feed component, it is again composed of several components

![Intro-to-React-animation-2.gif](Components%20and%20Props%20-%20Let%E2%80%99s%20visualise%20119c51a72da7423f9defc17ad6c1a4ed/Intro-to-React-animation-2.gif)

![Untitled](Components%20and%20Props%20-%20Let%E2%80%99s%20visualise%20119c51a72da7423f9defc17ad6c1a4ed/Untitled%201.png)

- Neat and clean codebase - every component is usually kept in its own file
- Reusable - can be used anywhere in the App
- components are composed to make complex UIs

An high level overview of the components that makes up a Twitter App

![Untitled](Components%20and%20Props%20-%20Let%E2%80%99s%20visualise%20119c51a72da7423f9defc17ad6c1a4ed/Untitled%202.png)

Component Tree Representation

![Untitled](Components%20and%20Props%20-%20Let%E2%80%99s%20visualise%20119c51a72da7423f9defc17ad6c1a4ed/Untitled%203.png)

## React encourages component driven development

While developing a React app, we basically develop lots of components. The components are further composed together to form complex UI’s.