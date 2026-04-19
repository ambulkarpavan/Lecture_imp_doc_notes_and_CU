# Routing - Dynamic Links, Dynamic Routes and useParams hook

Serial: 44
Made for: Beginner
Requirement: Must Have
Time in minutes: 30
Dependant on: Routing - Introduction, Installation & Setup,BrowserRouter, Routes, Route and Link (Routing%20-%20Introduction,%20Installation%20&%20Setup,Brows%202b38a28f30a34da596f1926ad5e7824f.md)
Learning Objectives: Routing Basics
doc-id: react-44

# Introduction

In this lesson, we'll explore how to implement dynamic routing in a React application using the `react-router-dom` library, specifically focusing on the `useParams` hook. This is crucial for creating pages that display unique content based on URL parameters, like user profiles or product details.

# Detailed Explanation

Dynamic routing allows a single route to match multiple paths. For example, `/users/:id` can match `/users/1`, `/users/2`, etc. The `:id` part is a URL parameter, and `react-router-dom` provides the `useParams` hook to access these parameters within your components.

# Use-case & Benefits

- **User Experience**: Provides a cleaner, more organized URL structure.
- **Flexibility**: Easily create pages that display content based on URL parameters (like user details).
- **Scalability**: Simplifies adding new routes for new types of content.

# Real World Examples

- A user profile page where the URL `/users/123` fetches and displays details for user 123.
- An e-commerce site where `/products/xyz` shows details for product xyz.

# Code Example :

## Dynamic Links :

Let’s build users page. For this we will go to `/src/pages/Users` . This users page will fetch a list of users from an API call. and we will display this list of users onto UI. 

```jsx
// src/pages/Users.jsx
import { useState, useEffect } from "react";
import LoadingIndicator from "../components/LoadingIndicator";
import ErrorIndicator from "../components/ErrorIndicator";
import { Link } from "react-router-dom";

async function getData(url) {
  try {
    let response = await fetch(url);
    let finalResponse = await response.json();
    return finalResponse;
  } catch (error) {
    console.log(error);
  }
}

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  async function fetchAndUpdateData(url) {
    setLoading(true);
    try {
      const apiResponse = await getData(url);
      setUsers(apiResponse.data);
      setLoading(false);
    } catch (error) {
      setError(true);
      setLoading(false);
    }
  }

  useEffect(() => {
    fetchAndUpdateData(`https://reqres.in/api/users`);
  }, []);

  if (loading) return <LoadingIndicator />;
  if (error) return <ErrorIndicator />;

  return (
    <div>
      <h1>Users Page</h1>
      {/* Users listing here */}
      {users &&
        users.length > 0 &&
        users.map((user) => (
          <div className="user-card" key={user?.id}>
            <img src={user?.avatar} alt={user?.first_name} />
            <Link to={`/users/${user?.id}`}>Click to view user details</Link> // Dynamic Links
          </div>
        ))}
    </div>
  );
}

export default Users;
```

Now when user clicks on the link; You’ll see that the url in the address bar changes like this. ( Dynamic Links )

```jsx
/users/1
/users/2
/users/3
...
```

Typically when you visit any website; You’ll have listing page and details page like

```jsx
/lectures --> lectures listing page
/lectures/1 --> lecture detailed page with lecture having id 1 ( This page basically makes another API call to get details related to lecture with id 1 )

/products --> products listing page
/products/abc343nvkfnboiae --> product detailed page with product having id abc343nvkfnboiae( This page basically makes another API call to get details related to product with id abc343nvkfnboiae )
```

We want to emulate the same behaviour wherein when the customer visits `/users/4` page;  we make another API call to get details related to user with id 4 and display the same onto UI.

## Dynamic Routes :

```jsx
// src/components/AllRoutes.jsx
import { Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import About from "../pages/About";
import Contact from "../pages/Contact";
import Users from "../pages/Users";
import SingleUser from "../pages/SingleUser";

function AllRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/contact" element={<Contact />} />
      <Route path="/users" element={<Users />} />
      <Route path="/users/:user_id" element={<SingleUser />} /> // --> Dynamic Route 
			{/* Whenever react routes see a route with /users/anything --> it'd go to this route; */}
    </Routes>
  );
}

export default AllRoutes;
```

## useParams Hook :

Create a single user page. This page will be rendered whenever customer tries to access `/users/someId` 

```jsx
// src/pages/SingleUser.jsx
function SingleUser() {
  return (
    <>
      <h1>Single User Page</h1>
    </>
  );
}

export default SingleUser;
```

Everytime a customer visit a single user page. Here are the list of things that should happen

1. As soon as the component mounts, An API call should happen to get the details of specific user. ( e.g., `[api.com/users/1](http://api.com/users/1)` )
2. Display the same onto UI by storing it in internal state. Also maintain loading and error state. 

Problem 1 : To make this API call and get the data related to user with some id. First we need to get the id. How to retrive this id from url within our component ??

Solution : `useParams` hook from `react-router-dom` library.

```jsx
// src/pages/SingleUser.jsx
import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import LoadingIndicator from "../components/LoadingIndicator";
import ErrorIndicator from "../components/ErrorIndicator";

async function getData(url) {
  try {
    let response = await fetch(url);
    let finalResponse = await response.json();
    return finalResponse;
  } catch (error) {
    console.log(error);
  }
}

function SingleUser() {
  const [user, setUser] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const { user_id } = useParams();

  async function fetchAndUpdateData(url) {
    setLoading(true);
    try {
      const apiResponse = await getData(url);
      console.log(apiResponse);
      setUser(apiResponse.data);
      setLoading(false);
    } catch (error) {
      setError(true);
      setLoading(false);
    }
  }

  useEffect(() => {
    fetchAndUpdateData(`https://reqres.in/api/users/${user_id}`);
  }, [user_id]);

  if (loading) {
    return <LoadingIndicator />;
  }

  if (error) {
    return <ErrorIndicator />;
  }

  return (
    <>
      <h1>Single User Page</h1>
      {user && (
        <div style={{ margin: "25px", border: "1px solid black" }}>
          <img src={user?.avatar} alt={user?.first_name} />
          <h5>
            Name : {user?.first_name}
            {user?.last_name}
          </h5>
          <h5>Email : {user?.email}</h5>
        </div>
      )}
    </>
  );
}

export default SingleUser;
```

### Conclusion

Dynamic routing with `useParams` in React enhances your application's functionality, making it more interactive and user-friendly. It's a foundational concept for building sophisticated web applications with unique pages based on URL parameters.

@Abdul Jabbar Peer Todo - Add the github link to this example here.

Referece : 

[useParams v6.16.0](https://reactrouter.com/en/main/hooks/use-params)