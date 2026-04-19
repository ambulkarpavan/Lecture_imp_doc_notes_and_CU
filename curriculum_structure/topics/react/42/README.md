# Routing - NavLink component

Serial: 42
Made for: Beginner
Requirement: Must Have
Time in minutes: 10
Dependant on: Routing - Introduction, Installation & Setup,BrowserRouter, Routes, Route and Link (Routing%20-%20Introduction,%20Installation%20&%20Setup,Brows%202b38a28f30a34da596f1926ad5e7824f.md), Routing - General Patterns and Conventions (Routing%20-%20General%20Patterns%20and%20Conventions%20dfd1fb8294804438ad6c12b15238eb12.md)
Learning Objectives: Routing Basics
doc-id: react-42

### NavLink :

Ref : 

[NavLink v6.16.0](https://reactrouter.com/en/main/components/nav-link)

`NavLink` basically is `Link` with additional features. In `Navlink` , you can style `Link` component differently based on whether it’s active link or not. This can be done either by using style prop or even by className.

Example : 

src/components/Navbar.jsx

```jsx
import { Link } from "react-router-dom";

const listOfLinks = [
  {
    to: "/",
    displayText: "Home",
 ...
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

src/components/Navbar.jsx

```jsx
// src/components/Navbar.jsx
import { NavLink } from "react-router-dom";

function Navbar() {
  const defaultStyle = {
    color: "black",
  };

  const activeStyle = {
    color: "red",
  };
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
      {listOfLinks.map((link) => (
        <NavLink
          style={({ isActive }) => {
            return isActive ? activeStyle : defaultStyle;
          }}
          key={link.to}
          to={link.to}
        >
          {link.displayText}
        </NavLink>
      ))}
    </div>
  );
}

export default Navbar;
```

The same can also be done for `classNames`

```jsx
 <NavLink
	key={link.to}
	to={link.to}
	className={({ isActive })=>{return isActive ? styles.active : styles.default }}
>
  {link.displayText}
 </NavLink>
```