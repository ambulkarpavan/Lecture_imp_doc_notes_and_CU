# CRUD-DOM-3 JWT authentication [120 min] (1)

## Token Systems in general

![Untitled](CRUD-DOM-3%20JWT%20authentication%20%5B120%20min%5D%20(1)%205a0e780a67c440f88a55dce9bab2623a/Untitled.png)

Steps involved: 

- You: pay money to the receptionist
- receptionist: smile & give us a token
- we will be having a token
- use that token to enquire about your order
- use the same token to get/access you order

## Token system for website authentication

![source: [https://betterprogramming.pub/jwt-ultimate-how-to-guide-with-best-practices-in-javascript-f7ba4c48dfbd](https://betterprogramming.pub/jwt-ultimate-how-to-guide-with-best-practices-in-javascript-f7ba4c48dfbd)](CRUD-DOM-3%20JWT%20authentication%20%5B120%20min%5D%20(1)%205a0e780a67c440f88a55dce9bab2623a/Untitled%201.png)

source: [https://betterprogramming.pub/jwt-ultimate-how-to-guide-with-best-practices-in-javascript-f7ba4c48dfbd](https://betterprogramming.pub/jwt-ultimate-how-to-guide-with-best-practices-in-javascript-f7ba4c48dfbd)

### Playing around with JWT in the rest-client

```jsx
### Sign up / create an account / register a user

POST http://127.0.0.1:9090/register
Content-Type: application/json

{
  "username": "babu",
  "firstname": "babu",
  "lastname": "bhai",
  "email": "babu@bhai.com",
  "password": "babu123",
  "avatar": "https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/762.jpg",
  "userLevel": 2
}

### Login / sign-in

POST http://127.0.0.1:9090/login
Content-Type: application/json

{
  "username": "babu",
  "password": "babu123" 
}

### Making authenticated requests / accessing protected routes

GET http://127.0.0.1:9090/todos
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImJhYnUiLCJwYXNzd29yZCI6IiQyYiQxMCRJc3NBLmJZaG5Qalh5cG9PNkF0VFVPbXdvRjQ2aWM4OFhUOE96MU50Y3pZVEl0WnF1WGg1ZSIsImVtYWlsIjoiYmFidUBiaGFpLmNvbSIsImZpcnN0bmFtZSI6ImJhYnUiLCJsYXN0bmFtZSI6ImJoYWkiLCJhdmF0YXIiOiJodHRwczovL2Nsb3VkZmxhcmUtaXBmcy5jb20vaXBmcy9RbWQzVzVEdWhnSGlyTEhHVml4aTZWNzZMaENrWlV6NnBuRnQ1QUpCaXl2SHllL2F2YXRhci83NjIuanBnIiwiY3JlYXRlZEF0IjoxNjc4OTUwMTk2ODQ5LCJpZCI6NTYsImlhdCI6MTY3ODk1MDI0NSwiZXhwIjoxNjc4OTYxMDQ1fQ.cXZsLFywHA5_J0HMwf7LZRl6Kazkts0qLdr7l9PibvE
```

### Implement them in code

```jsx
async function createData(){
  try {
    let res = await fetch(`http://localhost:9090/todos`, {
      method: 'POST',
      headers: { 
        'Content-type': 'application/json',
        'Authorization': `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsImZpcnN0bmFtZSI6IkFkIiwibGFzdG5hbWUiOiJNaW5pc3RlciIsImVtYWlsIjoiYWRtaW5AbWFpbC5jb20iLCJwYXNzd29yZCI6IiQyYiQxMCRsTG01THA0MHVCUjlDVXJabjU4Q2RPbDh5dTVHcDJ1bUFPLjZseS52V2NaMGEwdlVLc0hpQyIsImF2YXRhciI6Imh0dHBzOi8vY2xvdWRmbGFyZS1pcGZzLmNvbS9pcGZzL1FtZDNXNUR1aGdIaXJMSEdWaXhpNlY3NkxoQ2taVXo2cG5GdDVBSkJpeXZIeWUvYXZhdGFyLzc2Mi5qcGciLCJ1c2VyTGV2ZWwiOjQsImNyZWF0ZWRBdCI6MTY3MDE2NTk4MDYzOCwiaWF0IjoxNjcwNDg3NDMwLCJleHAiOjE2NzA1MDkwMzB9.VtoT7t0WMMtfBAgiB8WowRi43yQOSQ0hsOhuB2OJ5WQ`
      },
      body: JSON.stringify({
        userId: 48,
        title: "New loyal Minskin",
        completed: false
      })
    });
    if (res.ok) {
      let data = await res.json();
      return data;
    } else {
      return `server responded with a ${res.status} error.`
    }
  } catch (error) {
    return 'error';
  }
}

// createData().then(dat => console.log(dat));
```

Class Code: [JWT auth (codepen.io)](https://codepen.io/Adarsha-khatua/pen/zYMEZJe?editors=0010)

## Optional - Persisting JWT Authentication

*Just for your information - not mandatory; There are some shortcomings on storing JWT tokens in local-storage and its good to be aware of them.*

- [https://www.youtube.com/watch?v=occfnVaZOXI](https://www.youtube.com/watch?v=occfnVaZOXI)
- [https://betterprogramming.pub/jwt-ultimate-how-to-guide-with-best-practices-in-javascript-f7ba4c48dfbd](https://betterprogramming.pub/jwt-ultimate-how-to-guide-with-best-practices-in-javascript-f7ba4c48dfbd)