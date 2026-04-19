# Routing - Introduction, Installation & Setup,BrowserRouter, Routes, Route and Link

Serial: 40
Made for: Beginner
Requirement: Must Have
Time in minutes: 30
Learning Objectives: Routing Basics
Related back to React: Routing - General Patterns and Conventions (Routing%20-%20General%20Patterns%20and%20Conventions%20dfd1fb8294804438ad6c12b15238eb12.md), Routing - NavLink component (Routing%20-%20NavLink%20component%2017bd68a3f09f4e28b80c748ad15aa0e9.md), Routing - NotFound Page (Routing%20-%20NotFound%20Page%20695f7c439fec4bdab80d556f9550a7e4.md), Routing - Dynamic Links, Dynamic Routes and useParams hook (Routing%20-%20Dynamic%20Links,%20Dynamic%20Routes%20and%20usePar%2051820b240ab24085841ed08599b62b54.md), Routing - Navigate Component and useNavigate Hook (Routing%20-%20Navigate%20Component%20and%20useNavigate%20Hook%209db21d5564ad49f0b1321b433f4a6d2e.md), Routing - Query Params and useSearchParams hook (Routing%20-%20Query%20Params%20and%20useSearchParams%20hook%20242172add56d48febdb58849f0d89fab.md)
doc-id: react-40

# Introduction :

Routing basically means you navigate between different pages of your application.

# Introduction to Routing in React with `react-router-dom` :

Routing in React enables navigation between different components in an application, simulating the experience of moving between pages in a multi-page web application. `react-router-dom` is a popular library that facilitates routing in React applications.

# A quick overview of steps we are gonna follow to build an application using `react-router-dom` library

**Step 1 - Installation:**
To use `react-router-dom`, first, install it in your React project. If you're using Vite, create a new project and install `react-router-dom`:

```jsx
npm init vite@latest <application-name> -- --template react
npm install react-router-dom
```

**Step 2 - `BrowserRouter`:**`BrowserRouter` is a router implementation that uses the HTML5 history API to keep your UI in sync with the URL.

**Step 3 - `Routes` and `Route` Component:**`Routes` replaces the older `Switch` component and is used to declare routes in your application. `Route` components inside `Routes` define individual routes.

**Step 4 - `Link` Component:**`Link` is used for navigation within your app. It's similar to HTML's `<a>` tag but is designed for React Router.

**Step 5 - Dynamic Routes and `useParams` Hook:**
Dynamic routing is achieved using route parameters. `useParams` is a hook that allows you to access these parameters.

**Step 6 - `Navigate` Component and `useNavigate` Hook:**`Navigate` is a component used for redirecting to another route. `useNavigate` is a hook that programmatically navigates users around.

# Use-case & Benefits

React Router enhances user experience by enabling smooth navigation in React applications without full page reloads, which is crucial for single-page applications (SPAs). It also helps in organizing the structure of an application by defining routes in a centralized location.

# Real World Examples

- A blog website where users can navigate between home, about, and article pages.
- An e-commerce site with product listings, product detail pages, and a shopping cart.

# Detailed Explanation

### Step 1 - Installation

Create a react project using vite

```jsx
npm init vite@latest <application-name> -- --template react
```

Install `react-router-dom` library

```jsx
npm install react-router-dom
```

### **Step 2** : BrowserRouter

Ref : 

[BrowserRouter v6.17.0](https://reactrouter.com/en/main/router-components/browser-router)

Open `src/main.jsx` and set `BrowserRouter` component.

src/main.jsx

```jsx
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import { BrowserRouter } from "react-router-dom";

ReactDOM.createRoot(document.getElementById("root")).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
```

`BrowserRouter` is a provider component from react-router-dom library. All routing logic should be wrapped inside it. So only by wrapping your application ( App ) with BrowserRouter, you'll be able to use lot of tools that `react-router-dom` gives 

![browser-router-tree.png](Routing%20-%20Introduction,%20Installation%20&%20Setup,Brows%202b38a28f30a34da596f1926ad5e7824f/browser-router-tree.png)

### **Step 3** : `Routes` and `Route` component :

`Routes` replaces the older `Switch` component and is used to declare routes in your application. `Route` components inside `Routes` define individual routes.

Ref : 

[Routes v6.17.0](https://reactrouter.com/en/main/components/routes)

[Route v6.16.0](https://reactrouter.com/en/main/route/route)

Before we begin, create multiple pages in your application like `Home` `About` `Contact` `Users` . A better convention would be to maintain a folder with `src` folder called `pages`

Project Structure :

```jsx
├── src
│   ├── App.css
│   ├── App.jsx
│   ├── index.css
│   ├── main.jsx
│   └── pages
│       ├── About.jsx
│       ├── Contact.jsx
│       ├── Home.jsx
│       └── Users.jsx
```

src/pages/Home.jsx

```jsx
 function Home() {
  return (
    <>
      <h1>Home Page</h1>
    </>
  );
}

export default Home;
```

src/pages/About.jsx

```jsx
function About() {
  return (
    <>
      <h1>About Page</h1>
    </>
  );
}

export default About;
```

src/pages/Contact.jsx

```jsx
function Contact() {
  return (
    <>
      <h1>Contact Page</h1>
    </>
  );
}

export default Contact;
```

src/pages/Users.jsx

```jsx
function Users() {
  return (
    <>
      <h1>Users Page</h1>
    </>
  );
}

export default Users;
```

- Elaborated Explanation
    
    `Routes` - Wrapper component for Route component
    
    `Route` - This component from `react-router-dom` takes two props.
    
    1. **path** - On which path ?? . 
    It’s like “when the typed in url in the address bar has the endpoint
     `“/”` , `“/contact”` 
    2. **element** - What to render ?? 
    Which particular component to render when the path is `"/"` `"/contact"` … 
    `<Home/>` , `<Contact/>`

```jsx
// src/App.jsx
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import About from "./pages/About";
import Contact from "./pages/Contact";
import Users from "./pages/Users";

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/users" element={<Users />} />
      </Routes>
    </>
  );
}

export default App;
```

### **Step 4** : `Link` component :

`Link` is used for navigation within your app. It's similar to HTML's `<a>` tag but is designed for React Router.

Ref :

[Link v6.17.0](https://reactrouter.com/en/main/components/link)

Remember anchor `a` element. The `Link` component here works in similar manner. 

| a | Link |
| --- | --- |
| href | to |

```jsx
import { Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import About from "./pages/About";
import Contact from "./pages/Contact";
import Users from "./pages/Users";

function App() {
  return (
    <>
      <Link to="/">Home</Link>
      <Link to="/about">About</Link>
      <Link to="/contact">Contact</Link>
      <Link to="/users">Users</Link>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/users" element={<Users />} />
      </Routes>
    </>
  );
}

export default App;
```

- Elaborated explanation
    
    Remember `e.preventDefault` . So it's just the same thing implemented internally wherein `a` tag default behaviour is prevented and some other is applied ( It makes use of browser history stack and kind of mutates it ). 
    
    Why can’t I just use `a` tag ???
    
    you may use `a` tag but that will reload all the resources on every component changes that happens on route change ( that will defeat the purpose of having `react-router-dom` as it's similar to loading page every-time); but if you use Link that `react-router-dom` provides you wouldn't encounter that issue;
    

![tree-structure.png](Routing%20-%20Introduction,%20Installation%20&%20Setup,Brows%202b38a28f30a34da596f1926ad5e7824f/tree-structure.png)