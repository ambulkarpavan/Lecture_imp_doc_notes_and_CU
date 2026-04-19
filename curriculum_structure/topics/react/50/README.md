# Axios

Serial: 52

## Introduction to Axios

Axios is a popular JavaScript library used to make HTTP requests. It can be used in both browser and Node.js environments and offers a wide range of features to handle requests and responses.

## Setting Up a React Project with VITE

1. **Create a VITE React Project**:
    
    ```bash
    npm create vite@latest my-axios-app -- --template react
    cd my-axios-app
    npm install
    ```
    
2. **Install Axios**:
    
    ```bash
    npm install axios
    ```
    

## Basic Axios Methods

Axios provides methods corresponding to HTTP methods:

- `axios.get(url[, config])`: For GET requests.
- `axios.post(url, data[, config])`: For POST requests.
- `axios.put(url, data[, config])`: For PUT requests.
- `axios.patch(url, data[, config])`: For PATCH requests.
- `axios.delete(url[, config])`: For DELETE requests.

### The Config Object

The `config` object in Axios allows you to configure your request with headers, query parameters, timeout settings, etc.

## Setting Up JSON-Server for a Fake Backend

1. **Install JSON-Server**:
    
    ```bash
    npm install -g json-server
    
    ```
    
2. **Create a Fake Database**:
Create a file named `db.json` in your project root with the following content:
    
    ```json
    {
      "posts": [
        { "id": 1, "title": "Post 1", "description": "Description of post 1" },
        { "id": 2, "title": "Post 2", "description": "Description of post 2" }
      ]
    }
    
    ```
    
3. **Start JSON-Server**:
    
    ```bash
    json-server --watch db.json --port 3001
    
    ```
    

## Making Requests to JSON-Server

### 1. GET Request

Fetch all posts:

```jsx
import axios from 'axios';

function fetchPosts() {
  axios.get('<http://localhost:3001/posts>')
    .then(response => {
      console.log(response.data);
    })
    .catch(error => console.error('Error fetching posts:', error));
}

```

### 2. POST Request

Add a new post:

```jsx
function addPost() {
  const newPost = {
    title: "New Post",
    description: "Description of new post"
  };

  axios.post('<http://localhost:3001/posts>', newPost)
    .then(response => console.log(response.data))
    .catch(error => console.error('Error adding a post:', error));
}

```

### 3. PUT Request

Update an entire post:

```jsx
function updatePost(id, updatedPost) {
  axios.put(`http://localhost:3001/posts/${id}`, updatedPost)
    .then(response => console.log(response.data))
    .catch(error => console.error('Error updating post:', error));
}

```

### 4. PATCH Request

Update part of a post:

```jsx
function patchPost(id, patchData) {
  axios.patch(`http://localhost:3001/posts/${id}`, patchData)
    .then(response => console.log(response.data))
    .catch(error => console.error('Error patching post:', error));
}

```

### 5. DELETE Request

Delete a post:

```jsx
function deletePost(id) {
  axios.delete(`http://localhost:3001/posts/${id}`)
    .then(() => console.log('Post deleted'))
    .catch(error => console.error('Error deleting post:', error));
}

```

## Assignments for Practice

1. **Build a Blog Interface**:
    - Use Axios to fetch and display posts from your JSON-Server backend.
    - Implement functionality to add, update, and delete posts.
2. **Create a To-Do App**:
    - Set up a `todos` endpoint in your fake backend.
    - Use Axios to interact with the `todos` endpoint, implementing CRUD operations.
3. **User Registration Form**:
    - Create a form for user registration.
    - Use Axios to POST the form data to the JSON-Server.

Through these exercises, you'll gain hands-on experience with Axios and understand how to work with HTTP requests in a React application using VITE. This knowledge is crucial for interacting with APIs and building full-fledged web applications.