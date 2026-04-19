# Network Requests from React Component

Serial: 25
Made for: Beginner
Requirement: Must Have
Time in minutes: 20
Learning Objectives: Event Management, Fetch API calls , useState
Related back to React: Effects and useEffect I - Mount phase (Effects%20and%20useEffect%20I%20-%20Mount%20phase%20a7c8ad7722e34cc4a163c1b374ca1b45.md)
doc-id: react-25

Network Requests from React Component

In this lesson, We will talk about how one can build a react component wherein a network request can be made on button click ( click event )

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