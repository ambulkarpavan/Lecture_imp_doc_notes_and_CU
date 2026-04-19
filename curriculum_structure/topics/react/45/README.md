# Routing - Navigate Component and useNavigate Hook

Serial: 45
Made for: Beginner
Requirement: Must Have
Time in minutes: 15
Dependant on: Routing - Introduction, Installation & Setup,BrowserRouter, Routes, Route and Link (Routing%20-%20Introduction,%20Installation%20&%20Setup,Brows%202b38a28f30a34da596f1926ad5e7824f.md)
Learning Objectives: Routing Basics
Related back to React: Routing - Custom private route component (Routing%20-%20Custom%20private%20route%20component%20607ae18615a849b68582493a754fceb1.md)
doc-id: react-45

# Introduction :

In this lesson, we extend our understanding of React's routing capabilities by exploring the `Navigate` component and `useNavigate` hook from the `react-router-dom` library. These tools allow for programmatic navigation, giving developers control over redirecting users under certain conditions.

# Detailed Explanation :

- **`Navigate` Component**: Used for immediate redirection. When rendered, it navigates to a specified route.
- **`useNavigate` Hook**: Provides a function that can be called to programmatically navigate the user.

# Use-case & Benefits :

- **Conditional Redirects**: Redirect users based on certain conditions (e.g., authentication status).
- **Event-Driven Navigation**: Navigate after certain actions like form submissions.
- **Enhanced User Experience**: Smoothly guide users through application flows.

# Real World Examples :

- Redirecting unauthenticated users to a login page.
- Navigating to a different page after a certain task is done or say a new resource is created.

# Usage :

1. **`Navigate` Component**: Use it in a component's render method for immediate redirection.
2. **`useNavigate` Hook**: Call the navigate function to redirect users in response to events.

# Simplified Explanation

This `Navigate` component or `useNavigate` hook is generally used to programatically navigate/move the user to a different location.  

But how is it different from `Link` component that we already have. Let’s try and understand

Now you as a developer will also have to navigate/move user to different pages. That is when this `Navigate` tool can be super helpful..

Well how is this different from `Link` ??

`Link` is when user wants to go to some page. He clicks on that particular link and goes there. ( User has the control. He chose to go to that page ) 

Now there are gonna be times wherein as a user it's not upto him but as a developer you navigate him to a different route. ( Developer controls this as in, You programatically navigates user to some other place )

Lemme give you an example

A user has not logged in ( is not authenticated ) and is trying to access the `home page`. As a developer, what you’d do in that case is navigate user to `login page`

```jsx

```

Reference : 

[Navigate v6.16.0](https://reactrouter.com/en/main/components/navigate)

[useNavigate v6.17.0](https://reactrouter.com/en/main/hooks/use-navigate)

# Code Example :

```jsx
// src/pages/Home.jsx
import { Navigate } from "react-router-dom";

function Home() {
  const isLoggedIn = false;

  if (!isLoggedIn) {
    return <Navigate to="/about" />;
  }

  return (
    <>
      <h1>Home Page</h1>
    </>
  );
}

export default Home;
```

```jsx
// src/pages/About.jsx
import { useNavigate } from "react-router-dom";

function About() {
  const navigate = useNavigate();

  const handleClick = () => {
    console.log(`button clicked and user is being navigated to contact page`);
    navigate(`/contact`);
  };

  return (
    <>
      <h1>About Page</h1>
      <button onClick={handleClick}>
        Navigate to contact page using useNavigate hook
      </button>
    </>
  );
}

export default About;
```

### Conclusion

Understanding the `Navigate` component and `useNavigate` hook is essential for controlling user navigation in a React application. These tools provide flexibility in managing user flows, enhancing both security and user experience.