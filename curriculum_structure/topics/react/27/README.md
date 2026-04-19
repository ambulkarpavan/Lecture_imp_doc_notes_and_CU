# Effects and useEffect II - Update phase

Serial: 29
Made for: Beginner
Requirement: Must Have
Time in minutes: 30
Dependant on: Effects and useEffect I - Mount phase (Effects%20and%20useEffect%20I%20-%20Mount%20phase%20a7c8ad7722e34cc4a163c1b374ca1b45.md)
Learning Objectives: React Component Lifecycle, effects and useEffect
Related back to React: Effects and useEffect II - Update phase extended (Effects%20and%20useEffect%20II%20-%20Update%20phase%20extended%20291b136f104241e29db33959f697d129.md)
doc-id: react-29

- Handling side effects during update phase using useEffect hook
    - Basic Example
    - Advance Example
- 

# Handling side effects during update phase using useEffect hook :

Remember this example we have done in the effects and useEffect. 

```jsx
function App() {
  const [count, setCount] = useState(0)

  useEffect(() => {
    console.log("callback function inside useEffect is called")
    document.title = "Counter Application"
  }, [])

  return (
    <div>
      <h1>Count : {count}</h1>
      <button onClick={() => setCount(count + 1)}>INCREASE COUNT</button>
    </div>
  )
}
```

Let’s make some modifications to the above code :

We have added another state variable called `flag` here

```jsx
function App() {
  const [count, setCount] = useState(0)
  const [flag, setFlag] = useState(false) // Added some state value flag which can be updated by some button click

  console.log("line no 8")
  useEffect(() => {
    console.log("callback function inside useEffect is called")
    document.title = `count is ${count}`
  }, [])

  console.log("line no 15")

  return (
    <div>
      <h1>Count : {count}</h1>
      <button onClick={() => setCount(count + 1)}>INCREASE COUNT</button>
      <br />
      <button onClick={() => setFlag(!flag)}>{flag.toString()}</button> // This button can modify state `flag`
    </div>
  )
}
```

Here are some observations : 

| If i do not pass dependancy array | If i pass empty dependancy array |
| --- | --- |
| The callback inside useEffect is called after initial render ( mount phase )  | The callback inside useEffect is called after initial render ( mount phase )  |
| The callback inside useEffect is called Whenever the count values or even when flag value changes. So basically anytime the component renders or re-render. The callback inside useEffect is called  | callback inside useEffect will not be called when the count value changes or flag value changes  |

We also know that the dependency array in `useEffect` controls when the effect should run.

- An empty array `[]` means the effect runs once after the initial render
- No dependancy array means the effect runs after every render
- If we include variables in dependancy array then it'll run when those variables change. The variables are basically any `state` or `prop` value

So If I further modify the above code to

We have added `count` as dependency to useEffect hook.

```jsx
function App() {
  const [count, setCount] = useState(0)
  const [flag, setFlag] = useState(false)

  console.log("line no 8")
  useEffect(() => {
    console.log("callback function inside useEffect is called")
    document.title = `count is ${count}`
  }, [count])

  console.log("line no 15")

  return (
    <div>
      <h1>Count : {count}</h1>
      <button onClick={() => setCount(count + 1)}>INCREASE COUNT</button>
      <br />
      <button onClick={() => setFlag(!flag)}>{flag.toString()}</button>
    </div>
  )
}
```

Some of the observations here

| If I do not pass dependancy array | If I pass empty dependancy array | If I pass some variable in dependancy array |
| --- | --- | --- |
| The callback inside useEffect is called after initial render ( mount phase )  | The callback inside useEffect is called after initial render ( mount phase )  | The callback inside useEffect is called whenever the value of that variable changes. The variable can be any state or prop value |
| The callback inside useEffect is called Whenever the count values or even when flag value changes. So basically anytime the component renders or re-render. The callback inside useEffect is called  | callback inside useEffect will not be called when the count value changes or flag value changes  | The callback inside useEffect is not called whenever the value of flag changes. Though the component re-renders. Since the callback function inside useEffect is only dependant on count value now |

**A Quick Recap of useEffect :** 

1. I want to perform some side effect during the initial render ( as soon as the component mount ) or also called mount phase/event.
    
    ```jsx
    // This will run the callback function inside useEffect 
    	// 1. During the mount phase ( initial render )
    useEffect(() => {
       // Called during the mount phase
      }, []) // You'd keep the dependancy array empty
    ```
    

1. I want to perform some side effect during the update phase
    
    
    ```jsx
    // This will run the callback function inside useEffect 
    	// 1. During the mount phase ( inital render )
    	// 2. During the update phase ( whenever the component re-renders due to change in any variable ). Not so ideal
    
    useEffect(() => {
        // called everytime
      }) // No dependancy array is passed here
    ```
    
    ```jsx
    // This will run the callback function inside useEffect 
    	// 1. During the mount phase ( inital render )
    	// 2. During the update phase. whenever the variable inside dependancy array is updated 
    useEffect(() => {
       // called during mount phase and when dependancyVariable changes
      },[dependancyVariable]) // dependancy array with dependancyVariable is passed here
    ```
    

## Practical Examples of using `useEffect` during update phase :

The dependency array in `useEffect` controls when the effect should run. An empty array `[]` means the effect runs once after the initial render, while including variables ( Any state or prop value typically ) means it'll run when those variables change.

Using this concept; Let’s see how we generally use something like by applying it to some real world example. 

### Here’s some code we have done so far

Project Structure

```jsx
├── src
│   ├── App.jsx
│   ├── components
│   │   └── PostItem.jsx
│   └── main.jsx
```

App.jsx

```jsx
import { useState, useEffect } from "react";
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

  useEffect(() => {
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

**Here’s the problem statement  :**

- I want to implement pagination. Whenever page value changes, the UI should also get updated with the relevant data

### Understanding the API

**Resource** : 

[https://github.com/typicode/json-server](https://github.com/typicode/json-server)

[JSONPlaceholder - Free Fake REST API](https://jsonplaceholder.typicode.com/)

```jsx
https://jsonplaceholder.typicode.com/posts// Result : All posts
```

```jsx
https://jsonplaceholder.typicode.com/posts?_limit=10 // Result : limits the post result to 10; defaults to first 10 posts
```

```jsx
https://jsonplaceholder.typicode.com/posts?_limit=10&_page=3 // Result : 10 per page and third page result
```

Let’s make some changes to the above code

- Pagination implemented
- Whenever page value changes; UI is updated with the latest data.
- Basically effect is being called
    - During the mount phase
    - Whenever the page value changes ( update phase )

```jsx
import { useState, useEffect } from "react";
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
  // Step 1 : Implement pagination
  const [page, setPage] = useState(1);

  // Step 2 : add page as dependancy and update url accordingly;
  useEffect(() => {
    fetchAndUpdateData(page);
  }, [page]);

  const fetchAndUpdateData = async () => {
    setLoading(true);
    try {
      let data = await getData(
        `https://jsonplaceholder.typicode.com/posts?_limit=10&_page=${page}`
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
      <h1>
        Get posts on mount phase and Update posts whenever page number changes
      </h1>
      {/* Step 3 : Buttons to update page number */}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <button onClick={() => setPage(page - 1)}>PREVIOUS</button>
        <p style={{ padding: "20px", fontWeight: "bolder" }}>{page}</p>
        <button onClick={() => setPage(page + 1)}>NEXT</button>
      </div>
      {posts.map((post) => (
        <PostItem key={post.id} id={post.id} title={post.title} />
      ))}
    </>
  );
}

export default App;
```