# Routing - Custom private route component

Serial: 46
Made for: Beginner
Requirement: Good to Have
Time in minutes: 15
Dependant on: Routing - Navigate Component and useNavigate Hook (Routing%20-%20Navigate%20Component%20and%20useNavigate%20Hook%209db21d5564ad49f0b1321b433f4a6d2e.md)
Learning Objectives: Routing Basics
doc-id: react-46

# Introduction

Creating a custom Private Route component in React applications enhances security and user experience by controlling access to certain routes. This lesson will focus on implementing a `PrivateRoute` component using the `Navigate` component from the `react-router-dom` library, ensuring that only authenticated users can access specific pages.

# Detailed Explanation

### Concept of Private Routes

- **Purpose**: Private routes in React are used to restrict access to certain pages or components based on user authentication status.
- **Implementation**: This is typically achieved by creating a higher-order component that wraps around the desired routes.

### Using `Navigate` for Redirection

- **Functionality**: The `Navigate` component from `react-router-dom` is utilized to redirect unauthenticated users to a specified route, like a login page.
- **Integration**: It's integrated into the custom `PrivateRoute` component to handle redirection.

### Building `PrivateRoute.jsx`

- **Structure**: The component receives `children` (the components to be rendered) as props.
- **Authentication Check**: It includes a conditional statement checking if a user is authenticated (`isAuth`). If not authenticated, it renders the `Navigate` component to redirect to the login page.
- **Sample Code**:
    
    ```jsx
    import { Navigate } from "react-router-dom";
    
    function PrivateRoute({ children }) {
      const isAuth = true; // This should be replaced with actual authentication logic
    
      if (!isAuth) {
        return <Navigate to="/login" />;
      }
    
      return children;
    }
    
    export default PrivateRoute;
    
    ```
    

# Use-case & Benefits

- **DRY Principle**: Avoids code repetition across different routes that require authentication.
- **Scalability**: Makes the application more scalable, as adding new private routes becomes simpler.
- **Security**: Enhances security by centralizing the authentication logic for routes.

# Real World Examples

- **Member-Only Content**: Websites with exclusive content for registered or subscribed users, like online courses, premium articles, etc.
- **User Profile Pages**: Social media or e-commerce sites where user profiles or dashboards are accessible only after logging in.

# Usage

- **In `AllRoutes.jsx`**: The `PrivateRoute` component is used as a wrapper around the routes that should be private.
    
    ```jsx
    // src/components/AllRoutes.jsx
    import { Routes, Route } from "react-router-dom";
    import Home from "../pages/Home";
    import About from "../pages/About";
    import Contact from "../pages/Contact";
    import Users from "../pages/Users";
    import SingleUser from "../pages/SingleUser";
    import PrivateRoute from "./PrivateRoute";
    
    function AllRoutes() {
      return (
        <Routes>
          <Route path="/" element={<Home />} /> // Public Route
          <Route path="/about" element={<About />} /> // Public Route
          <Route path="/contact" element={<Contact />} /> // Public Route
          <Route 
            path="/users"
            element={
              <PrivateRoute>
                <Users />
              </PrivateRoute>
            }
          /> // Private Route
          <Route
            path="/users/:user_id"
            element={
              <PrivateRoute>
                <SingleUser />
              </PrivateRoute>
            }
          /> // Private Route
        </Routes>
      );
    }
    
    export default AllRoutes;
    ```
    
- **Flexibility**: This method allows easy modification of authentication logic without altering each route individually.

By understanding and implementing this concept, you can effectively manage user access in your React applications, adhering to best practices in web development.