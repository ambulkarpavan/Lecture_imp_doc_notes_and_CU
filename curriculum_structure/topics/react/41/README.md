# Routing - General Patterns and Conventions

Serial: 41
Made for: Beginner
Requirement: Must Have
Time in minutes: 10
Dependant on: Routing - Introduction, Installation & Setup,BrowserRouter, Routes, Route and Link (Routing%20-%20Introduction,%20Installation%20&%20Setup,Brows%202b38a28f30a34da596f1926ad5e7824f.md)
Learning Objectives: Routing Basics
Related back to React: Routing - NavLink component (Routing%20-%20NavLink%20component%2017bd68a3f09f4e28b80c748ad15aa0e9.md)
doc-id: react-41

**Some Refactors :**

# **Refactor 1** :

- Style your navbar and make it a separate component
- Routing logic can also be moved to separate component

**Project Structure** :

```jsx
.
├── README.md
├── index.html
├── package-lock.json
├── package.json
├── src
│   ├── App.jsx
│   ├── components
│   │   ├── AllRoutes.jsx
│   │   └── Navbar.jsx
│   ├── main.jsx
│   └── pages
│       ├── About.jsx
│       ├── Contact.jsx
│       ├── Home.jsx
│       └── Users.jsx
```

```jsx
// src/components/Navbar.jsx
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "space-around",
        background: "lightgray",
        padding: "10px",
      }}
    >
      <Link to="/">Home</Link>
      <Link to="/about">About</Link>
      <Link to="/contact">Contact</Link>
      <Link to="/users">Users</Link>
    </div>
  );
}

export default Navbar;
```

```jsx
// src/components/AllRoutes.jsx
import { Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import About from "../pages/About";
import Contact from "../pages/Contact";
import Users from "../pages/Users";

function AllRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/contact" element={<Contact />} />
      <Route path="/users" element={<Users />} />
    </Routes>
  );
}

export default AllRoutes;
```

```jsx
// src/App.jsx
import AllRoutes from "./components/AllRoutes";
import Navbar from "./components/Navbar";

function App() {
  return (
    <>
      <Navbar />
      <AllRoutes />
    </>
  );
}

export default App;
```

# **Refactor 2** :

`Navbar` can also have array of links

```jsx
import { Link } from "react-router-dom";

const listOfLinks = [
  {
    to: "/",
    displayText: "Home",
  },
  {
    to: "/about",
    displayText: "About",
  },
  {
    to: "/contact",
    displayText: "Contact",
  },
  {
    to: "/users",
    displayText: "Users",
  },
];

function Navbar() {
  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "space-around",
        width: "80%",
        margin: "auto",
      }}
    >
      {listOfLinks.map((link) => (
        <Link key={link.to} to={link.to}>
          {link.displayText}
        </Link>
      ))}
    </div>
  );
}

export default Navbar;
```

@Abdul Jabbar Peer  Todo - Add github link here for the code.