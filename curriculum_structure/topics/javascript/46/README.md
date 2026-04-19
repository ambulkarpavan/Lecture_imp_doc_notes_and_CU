# CRUD-DOM-2-Pagination [120 min] (1)

## Rendering buttons from an Array [Pagination task-1]

Problem: 

You’ve got the following data: 

```jsx
let primary_buttons = [
  {text: '1', 'data-id': 1},
  {text: '2', 'data-id': 2},
  {text: '3', 'data-id': 3},
  {text: '4', 'data-id': 4},
  {text: '5', 'data-id': 5},
  {text: '6', 'data-id': 6},
]
```

You need to render a list of buttons using the above data:

![Untitled](CRUD-DOM-2-Pagination%20%5B120%20min%5D%20(1)%20ef2ded3bbf63426a8abfd669c9127979/Untitled.png)

On click of every button, the data-id should be logged to the console.

Before you start coding: 

- Can you think of a use case where it can be practically used?
- Can you try to solve it in you mind first?

Problem code: [https://codepen.io/drupalastic/pen/zYLoENR?editors=1010](https://codepen.io/drupalastic/pen/zYLoENR?editors=1010) 

Solution code: [https://codepen.io/drupalastic/pen/VwGxvrz?editors=0011](https://codepen.io/drupalastic/pen/VwGxvrz?editors=0011)

**Json server documentation:** [https://github.com/typicode/json-server#paginate](https://github.com/typicode/json-server#paginate) 

## Making Paginated Query [Pagination task-2]

Problem: [https://codepen.io/drupalastic/pen/VwBmzMQ?editors=0010](https://codepen.io/drupalastic/pen/VwBmzMQ?editors=0010) 

![Untitled](CRUD-DOM-2-Pagination%20%5B120%20min%5D%20(1)%20ef2ded3bbf63426a8abfd669c9127979/Untitled%201.png)

[MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Layout_cookbook/Pagination)

The list of posts is really long. I just need get first 15 results from the server

URL: [https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts) 

Server API Documentation: [https://github.com/typicode/json-server](https://github.com/typicode/json-server)

## Get total number of Item in paginated query & count the number of pages

You need to console log the total number of items & the total number of pages

Problem: [https://codepen.io/drupalastic/pen/rNrWzrW](https://codepen.io/drupalastic/pen/rNrWzrW) 

Hint1 : Exploring the API in VSCode RestClient gives us a lot more meta information

Hint2: `res.headers.get("X-Total-Count")`

Solution: [https://codepen.io/drupalastic/pen/KKBNvxp?editors=0011](https://codepen.io/drupalastic/pen/KKBNvxp?editors=0011) 

Complete pagination example: [https://codesandbox.io/s/pagination-problem-sdrwu1?file=/src/index.js](https://codesandbox.io/s/pagination-problem-sdrwu1?file=/src/index.js) [problem]

---

---

Steps: 

- limit the results
- get total number of items
- calculate number of buttons required
- render list of buttons
- add event handlers to refresh the list