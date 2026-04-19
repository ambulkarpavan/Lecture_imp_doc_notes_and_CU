# Effects and useEffect I - Mount phase

Serial: 28
Made for: Beginner
Requirement: Must Have
Time in minutes: 30
Dependant on: Network Requests from React Component (Network%20Requests%20from%20React%20Component%2029188d5d298b4cd18ace95779ea2f28a.md), Side Effects or Effects (Side%20Effects%20or%20Effects%2079f91849db4e4ac3a9392ec960307cc7.md)
Learning Objectives: React Component Lifecycle, effects and useEffect
Related back to React: Effects and useEffect II - Update phase (Effects%20and%20useEffect%20II%20-%20Update%20phase%20096a46870ac34db1bbf92d4c148e1b92.md)
doc-id: react-28

- useEffect
    - Introduction
    - Syntax
    - Order of execution
- Handling side effects during mount phase using useEffect hook
    - Basic Example
    - Advance Example

# useEffect :

React provides the `useEffect` hook to handle side effects in React components. The `useEffect` hook runs after render thereby you don’t endup blocking the rendering process. 

**useEffect Syntax :**

```jsx
useEffect( callbackFunction, dependancyArray )
useEffect(()=>{
	
},[])
```

So the above code will be updated to something like this

```jsx
import { useState, useEffect } from "react"
// Step 1: import useEffect
import "./App.css"

function App() {
  const [count, setCount] = useState(0)

  // Step 2 : call useEffect and pass callback function inside it;
  useEffect(() => {
    console.log("callback function inside useEffect is called")
    document.title = "Counter Application"
  })

  return (
    <div>
      <h1>Count : {count}</h1>
      <button onClick={() => setCount(count + 1)}>INCREASE COUNT</button>
    </div>
  )
}

export default App
```

### Order of execution of callback inside `useEffect` :

Check this one out

```jsx
import { useState, useEffect } from "react"
import "./App.css"

function App() {
  const [count, setCount] = useState(0)

  console.log("line no 8") // Order of execution --> 1
  useEffect(() => {
    // Order of execution --> 4
    console.log("callback function inside useEffect is called")
    document.title = "Counter Application"
  })

  console.log("line no 15") // Order of execution --> 2

  return (
    // // Order of execution --> 3
    <div>
      <h1>Count : {count}</h1>
      <button onClick={() => setCount(count + 1)}>INCREASE COUNT</button>
    </div>
  )
}

export default App
```

With this above approach, Now instead of performing side effects during the render process which is not ideal. We perform side effects after the rendering is completed as the callback inside useEffect is called after the rendering is completed.

Since this methods allows us to run side effect after render. It is also called “after-render” methods.

That is how side effects are handled in react. 

# Handling side effects during mount phase using useEffect hook :

The callback inside `useEffect` gets called after initial render, and also after every re-render. What if I want the callback to be called only during the inital render ( “***as soon as the component mounts”*** ). 

**Solution :**

The dependency array in `useEffect` controls when the effect should run. An empty array `[]` means the effect runs once after the initial render ( Mount phase )

```jsx
function App() {
  const [count, setCount] = useState(0)

  console.log("line no 8")
  useEffect(() => {
    console.log("callback function inside useEffect is called")
    document.title = "Counter Application"
  }, [])

  console.log("line no 15")

  return (
    <div>
      <h1>Count : {count}</h1>
      <button onClick={() => setCount(count + 1)}>INCREASE COUNT</button>
    </div>
  )
}
```

## Practical Examples of using `useEffect` during mount phase :

Using `useEffect`, we can fetch data from APIs after the component mounts 

### Remember this example from Network Requests from React Component

Let’s take this example of a simple API request whenever a user clicks a button ( on click event )

```jsx
├── src
│   ├── App.jsx
│   ├── components
│   │   └── PostItem.jsx
│   └── main.jsx
```

App.jsx

```jsx
import { useState } from "react";
import PostItem from "./components/PostItem";

const getData = async (url) => {
  try {
    let res = await fetch(url);
    let data = await res.json();
    return data;
  } catch (error) {
    throw new Error(error);
  }
};

function App() {
  const [loading, setLoading] = useState(false);
  const [posts, setPosts] = useState([]);
  const [err, setErr] = useState(false);

  const fetchAndUpdateData = async () => {
    setLoading(true);
    try {
      let data = await getData(
        `https://jsonplaceholder.typicode.com/posts?_limit=10`
      );
      setPosts(data);
      setLoading(false);
    } catch (error) {
      setErr(true);
      setLoading(false);
    }
  };

  if (loading) {
    return <h1>Loading...</h1>;
  }

  if (err) {
    return <h1>Something went wrong.. please refresh</h1>;
  }

  return (
    <>
      <h1>Click on the below button to get posts</h1>
      <button onClick={fetchAndUpdateData}>GET POSTS</button>
      {posts.map((post) => (
        <PostItem key={post.id} id={post.id} title={post.title} />
      ))}
    </>
  );
}

export default App;
```

PostItem.jsx

```jsx
const PostItem = ({ id, title }) => {
  return (
    <div style={{ border: "1px solid black", margin: "20px", padding: "10px" }}>
      <p>{id}</p>
      <p>{title}</p>
    </div>
  );
};

export default PostItem;
```

If you observe the above example :

1. `**click**` is the event ( Button Click )
2. `**fetchAndUpdateData**` is the event handler

### Making an API call during the mount phase :

**Here’s the problem statement  :**

I do not want to make an API call on `click` event but I want to make API call on `mount` event. Because that is how any website work right ? As soon as the page loads/ component is mounted onto UI, You make an API call, you get the data and you display the same onto UI. 

So till now the trigger to make an API call was button click ( `click` event ) . But now the trigger to make this API call is as soon as the *“component mounts”*. So trigger is `mount` event.

Okay.. But how ? How can I make an API call as soon as the component mounts ?

Can we do something like this wherein we remove button and `click` event and instead invoke `fetchAndUpdateData` directly during the rendering of component ?

```jsx
import { useState } from "react";
import PostItem from "./components/PostItem";

const getData = async (url) => {
  try {
    let res = await fetch(url);
    let data = await res.json();
    return data;
  } catch (error) {
    throw new Error(error);
  }
};

function App() {
  const [loading, setLoading] = useState(false);
  const [posts, setPosts] = useState([]);
  const [err, setErr] = useState(false);

  const fetchAndUpdateData = async () => {
    setLoading(true);
    try {
      let data = await getData(
        `https://jsonplaceholder.typicode.com/posts?_limit=10`
      );
      setPosts(data);
      setLoading(false);
    } catch (error) {
      setErr(true);
      setLoading(false);
    }
  };

	// fetchAndUpdateData is invoked/called during the rendering of component

  fetchAndUpdateData();

  if (loading) {
    return <h1>Loading...</h1>;
  }

  if (err) {
    return <h1>Something went wrong.. please refresh</h1>;
  }

  return (
    <>
      <h1>Get posts as soon as the component renders</h1>
      {posts.map((post) => (
        <PostItem key={post.id} id={post.id} title={post.title} />
      ))}
    </>
  );
}

export default App;
```

**The problem with the above approach** : Typically whenever there are “side-effects” or “effects” in our component. They shouldn’t be called during the rendering of the component since these are unpredictable. We can’t block the rendering of component till the API call is completed. Not a good user experience. 
Also you might see too manys re-renders error in your console ( a rather not-so-recommended thing to try but do check it out and think why ?? )

So the above code will be updated to something like this. 

```jsx
import { useState, useEffect } from "react";
// Step 1 : Import useEffect from react library similar to how you have imported useState hook;
import PostItem from "./components/PostItem";

const getData = async (url) => {
  try {
    let res = await fetch(url);
    let data = await res.json();
    return data;
  } catch (error) {
    throw new Error(error);
  }
};

function App() {
  const [loading, setLoading] = useState(false);
  const [posts, setPosts] = useState([]);
  const [err, setErr] = useState(false);

  const fetchAndUpdateData = async () => {
    setLoading(true);
    try {
      let data = await getData(
        `https://jsonplaceholder.typicode.com/posts?_limit=10`
      );
      setPosts(data);
      setLoading(false);
    } catch (error) {
      setErr(true);
      setLoading(false);
    }
  };

  // Step 2 : Invoke/call useEffect and pass a callback function inside it;
  useEffect(() => {
    // Step 3 : Perform side effects here; basically meaning you can call fetchAndUpdateData here;
    // Step 4 : add an empty dependency array as second argument;
    fetchAndUpdateData();
  }, []);

  if (loading) {
    return <h1>Loading...</h1>;
  }

  if (err) {
    return <h1>Something went wrong.. please refresh</h1>;
  }

  return (
    <>
      <h1>Get posts as soon as the component renders</h1>
      {posts.map((post) => (
        <PostItem key={post.id} id={post.id} title={post.title} />
      ))}
    </>
  );
}

export default App;
```

With this above approach, Now instead of performing side effects during the render process which is not ideal. We perform side effects after the rendering is completed as the callback inside useEffect is called after the rendering is completed.

And this is how `useEffect` hook from react allows side effects to be handled after render, ensuring they don't block the rendering process.