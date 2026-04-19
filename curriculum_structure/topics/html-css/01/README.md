# How Web Works (Basic) (15mins)

Backend vs Frontend

## BE example:

- [https://jsonplaceholder.typicode.com/](https://jsonplaceholder.typicode.com/)
- BE App returns something similar to this: [https://jsonplaceholder.typicode.com/photos?_start=0&_limit=5](https://jsonplaceholder.typicode.com/photos?_start=0&_limit=5)

## FE example:

- [https://codepen.io/drupalastic/pen/rNpXKxN?editors=1010](https://codepen.io/drupalastic/pen/rNpXKxN?editors=1010)

## 🔑 Student Activity

- Read the documentation - [https://jsonplaceholder.typicode.com/](https://jsonplaceholder.typicode.com/)
- Try to load all the users in your browser [simple JSON object - only the code that comes from the backend server]

![Untitled](How%20Web%20Works%20(Basic)%20(15mins)%2007e962a403e44658a125a90202c1f847/Untitled.png)

### The client requests a service

- we open a browser (client)
- we hit a url for example: [www.google.com](http://www.google.com) (Uniform Resource Location)
    - the client sends a message to the server asks for a resource
    - Resources can be - web pages, images, video files, fonts, stylesheets
    - This message is formatted based on a protocol called `HTTP`
    - In other words, HTTP (Hypertext transfer protocol) is a standard structure (or protocol) that clients and servers use to communicate over internet.
    - With an `HTTP request`, the client communicates to the server, what it is looking for

### The server provides the service

- The server listens to the message
- It figures out what the client is asking
- It sends a message back to the client
- This message is called an `HTTP response`

### The client gets back a message

- for example, the response can be an html page
    
    ```html
    <!DOCTYPE html>
    <html>
    ...
    	<link rel="stylesheet" href="styles.css">
    ...
      <img class="footer-sub__logo" src="https://unsplash.com/assets/core/logo-black-df2168ed0c378fa5506b1816e75eb379d06cfcd0af01e07a2eb813ae9b5d7405.svg">
    ...
    </html>
    ```
    
- browser constructs a DOM in case its an HTML document (Document Object Model)
- browser discovers references to other resources in the html document like images, stylesheets, font etc.
- For each resource the browser sends separate HTTP requests to same or other servers to fetch that resource
- These requests can be parallel
- Once the browser has all the necessary resources, it renders the HTML document (or displays it)

## Request and Response in Action

![Untitled](How%20Web%20Works%20(Basic)%20(15mins)%2007e962a403e44658a125a90202c1f847/Untitled%201.png)

![Untitled](How%20Web%20Works%20(Basic)%20(15mins)%2007e962a403e44658a125a90202c1f847/Untitled%202.png)

## 🔑 Student Activity

- Visit: [https://www.amazon.in/Apple-iPhone-15-Plus-256/dp/B0CHWV3L2R/ref=sr_1_10?crid=3IYIGCZNHLQ98](https://www.amazon.in/Apple-iPhone-15-Plus-256/dp/B0CHWV3L2R/ref=sr_1_10?crid=3IYIGCZNHLQ98)
- Inspect and change the price
- Where did you change the price - client or the server