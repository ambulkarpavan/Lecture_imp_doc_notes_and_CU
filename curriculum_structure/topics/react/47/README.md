# Routing - Query Params and useSearchParams hook

Serial: 47
Made for: Beginner
Requirement: Good to Have
Time in minutes: 20
Dependant on: Routing - Introduction, Installation & Setup,BrowserRouter, Routes, Route and Link (Routing%20-%20Introduction,%20Installation%20&%20Setup,Brows%202b38a28f30a34da596f1926ad5e7824f.md)
Learning Objectives: Routing Basics
doc-id: react-47

# Introduction :

Understanding how to manage query parameters in a React application is crucial for tasks like filtering, sorting, and sharing specific views or states of a page. React Router provides hooks like `useSearchParams` to efficiently handle query parameters. In this lesson, we'll delve into the difference between URL parameters and query parameters, and learn how to use the `useSearchParams` hook in a React application.

# URL Parameters vs. Query Parameters :

- **URL Parameters**: These are part of the URL path. For example, `https://localhost:3000/products/<someProductId>` uses a URL parameter to fetch a specific product by its ID.
- **Query Parameters**: These are additional key-value pairs attached to the URL. For instance, `https://localhost:3000/products?category=electronics` uses a query parameter to filter products by category.

# The `useSearchParams` Hook

- **Purpose**: This hook is used in React to retrieve and modify query parameters in the URL.
- **Advantage**: It simplifies the process of reading and updating the URL's query parameters, which is more complex to implement manually.

### Comparison with `useParams`

- `useParams` is used for fetching URL parameters, like in `https://localhost:3000/products/<someProductId>`.
- `useSearchParams`, on the other hand, is for handling query parameters, like in `https://localhost:3000/products?category=electronics`.

# Real-World Example | Code Example :

Implementing Pagination with `useSearchParams`

Let's apply this knowledge in a practical scenario involving pagination in a `Users` component.

### Phase 1: Basic Implementation

1. **Fetching Data Based on Page Number**: The `Users` component fetches user data from an API based on the current page number, which is stored in the component's state.
2. **Handling Page Changes**: The component includes buttons to navigate between pages, updating the page number in the state.

```jsx
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
  // 1. maintain state for page
  const [page, setPage] = useState(1);

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
    // 3. added page as a dependency here;
    fetchAndUpdateData(`https://reqres.in/api/users?page=${page}`);
  }, [page]);

  if (loading) return <LoadingIndicator />;
  if (error) return <ErrorIndicator />;

  return (
    <div>
      <h1>Users Page</h1>
      {/* 2. Buttons to update page state */}
      <div className="pagination">
        <button onClick={() => setPage(page - 1)}>Previous</button>
        <span>Page : {page}</span>
        <button onClick={() => setPage(page + 1)}>Next</button>
      </div>
      {users &&
        users.length > 0 &&
        users.map((user) => (
          <div className="user-card" key={user?.id}>
            <img src={user?.avatar} alt={user?.first_name} />
            <Link to={`/users/${user?.id}`}>Click to view user details</Link>
          </div>
        ))}
    </div>
  );
}

export default Users;
```

### Phase 2: Integrating Query Parameters

1. **Setting Page Number in URL**: Using `useSearchParams`, the component updates the URL's query parameter to reflect the current page number. This happens every time the page number in the state changes.
2. **Retrieving Page Number from URL**: The page number is retrieved from the URL's query parameter when the component mounts or when the URL changes.

```jsx
import { useState, useEffect } from "react";
import LoadingIndicator from "../components/LoadingIndicator";
import ErrorIndicator from "../components/ErrorIndicator";
import { Link, useSearchParams } from "react-router-dom";

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
  const [page, setPage] = useState(1);
  // 1 : useSearchParams hooks to get the search params
  const [searchParams, setSearchParams] = useSearchParams();

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
    fetchAndUpdateData(`https://reqres.in/api/users?page=${page}`);
  }, [page]);

  // 2. updating search params as soon as the component mounts
  useEffect(() => {
    setSearchParams({ page: page });
  }, [page]);

  if (loading) return <LoadingIndicator />;
  if (error) return <ErrorIndicator />;

  return (
    <div>
      <h1>Users Page</h1>
      <div className="pagination">
        <button onClick={() => setPage(page - 1)}>Previous</button>
        <span>Page : {page}</span>
        <button onClick={() => setPage(page + 1)}>Next</button>
      </div>
      {users &&
        users.length > 0 &&
        users.map((user) => (
          <div className="user-card" key={user?.id}>
            <img src={user?.avatar} alt={user?.first_name} />
            <Link to={`/users/${user?.id}`}>Click to view user details</Link>
          </div>
        ))}
    </div>
  );
}

export default Users;
```

### Phase 3: Persistence Across Refreshes

1. **Maintaining Page State**: When the page is refreshed, the page number is retrieved from the URL's query parameter, ensuring that the user remains on the same page they were viewing.
2. **Handling Multiple Query Parameters**: The component can handle multiple query parameters, like a search query along with the page number.

```jsx
import { useState, useEffect } from "react";
import LoadingIndicator from "../components/LoadingIndicator";
import ErrorIndicator from "../components/ErrorIndicator";
import { Link, useSearchParams } from "react-router-dom";

async function getData(url) {
  try {
    let response = await fetch(url);
    let finalResponse = await response.json();
    return finalResponse;
  } catch (error) {
    console.log(error);
  }
}

function getPageNumberFromParams(pageParam) {
  pageParam = Number(pageParam);

  if (Number.isNaN(pageParam)) {
    return 1;
  }
  if (!pageParam) {
    return 1;
  }
  if (pageParam < 1) {
    return 1;
  }
  return pageParam;
}

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  // 1 Moving searchParams line before page state so as to utilize the searchParams to get the param from URL so that I can use the same in the below line
  const [searchParams, setSearchParams] = useSearchParams();
  // 2. getting the page param from URL
  const [page, setPage] = useState(
    getPageNumberFromParams(searchParams.get("page"))
  );
  // 3. can handle multiple query params
  const [searchText, setSearchText] = useState(searchParams.get("q") || "");

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
    fetchAndUpdateData(`https://reqres.in/api/users?page=${page}`);
  }, [page]);

  useEffect(() => {
    const finalParams = {};
    finalParams.page = page;
    if (searchText) {
      finalParams.q = searchText;
    }

    setSearchParams(finalParams);
  }, [page, searchText]);

  if (loading) return <LoadingIndicator />;
  if (error) return <ErrorIndicator />;

  return (
    <div>
      <h1>Users Page</h1>
      <input
        type="text"
        placeholder="set search text"
        onChange={(e) => setSearchText(e.target.value)}
        value={searchText}
      />
      <div className="pagination">
        <button onClick={() => setPage(page - 1)}>Previous</button>
        <span>Page : {page}</span>
        <button onClick={() => setPage(page + 1)}>Next</button>
      </div>
      {users &&
        users.length > 0 &&
        users.map((user) => (
          <div className="user-card" key={user?.id}>
            <img src={user?.avatar} alt={user?.first_name} />
            <Link to={`/users/${user?.id}`}>Click to view user details</Link>
          </div>
        ))}
    </div>
  );
}

export default Users;
```

### Use-case & Benefits

- **Consistent User Experience**: Retaining the state (like page number or filters) in the URL ensures a consistent experience even after page reloads.
- **Shareability**: URLs with query parameters can be shared to present the same view or state of the application to others.
- **Flexibility**: `useSearchParams` allows for dynamic and flexible manipulation of the URL's query parameters without complex logic.

### Instructor Activity

Demonstrate creating the `Users` component, focusing on integrating `useSearchParams` to handle pagination. Show how the URL changes with page navigation and how the state persists across page reloads.

### Learners Activity

1. **Implement `useSearchParams`**: Have learners modify a component to use `useSearchParams` for handling pagination or filtering.
2. **Explore & Discuss**: Encourage exploration of different use cases for `useSearchParams`, such as filtering products in an e-commerce site. Discuss the benefits and potential challenges of managing state through URL query parameters.

By mastering `useSearchParams`, developers can efficiently manage application state through the URL, enhancing user experience and shareability in React applications.