# CRUD-DOM-1 [120 min] (1)

Fetch analogy:  [https://www.canva.com/design/DAFnskZ65Jc/-mM86FytMXZHEGEVFnHjFQ/edit?utm_content=DAFnskZ65Jc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton](https://www.canva.com/design/DAFnskZ65Jc/-mM86FytMXZHEGEVFnHjFQ/edit?utm_content=DAFnskZ65Jc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## Client / Server model - Quick refresher

![Untitled](CRUD-DOM-1%20%5B120%20min%5D%20(1)%20f2873829c100496a9b4cc5ded3baa0ca/Untitled.png)

Explore the network tab of the dev tools by browsing 

- [https://www.google.com/](https://www.google.com/)
- [https://jsonplaceholder.typicode.com/users](https://jsonplaceholder.typicode.com/users)
- [https://reqres.in/api/users?page=2](https://reqres.in/api/users?page=2)

## Self study

- Status Codes
    
    ![Untitled](CRUD-DOM-1%20%5B120%20min%5D%20(1)%20f2873829c100496a9b4cc5ded3baa0ca/Untitled%201.png)
    

## What is this `GET` ?

![Untitled](CRUD-DOM-1%20%5B120%20min%5D%20(1)%20f2873829c100496a9b4cc5ded3baa0ca/Untitled%202.png)

HTTP (Hypertext Transfer Protocol) specifies a collection of **request methods** to specify what action is to be performed on a particular resource. The most commonly used HTTP request methods are GET, POST, PUT, PATCH, and DELETE. These are equivalent to the CRUD operations (create, read, update, and delete). These HTTP methods help to standardize how web browsers and servers communicate with each other, making it easier for developers to build web applications and services.

## Use cases of HTTP Methods?

### GET

![Untitled](CRUD-DOM-1%20%5B120%20min%5D%20(1)%20f2873829c100496a9b4cc5ded3baa0ca/Untitled%203.png)

`GET` is like asking the server to give us something. Its like asking for a piece of toy from the toy shelf. This method requests a specific resource from a server, such as a webpage or an image. It's the most commonly used method and is used to retrieve data from the server.

[MDN link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)

### POST

![Untitled](CRUD-DOM-1%20%5B120%20min%5D%20(1)%20f2873829c100496a9b4cc5ded3baa0ca/Untitled%204.png)

`POST` is like giving something to the server. It’s like giving a new toy to the toy shelf. This method submits data to a server to create a new resource, such as a new user account or a blog post. It's also commonly used for forms, where users enter data and submit it to a server for processing.

[MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)

### PUT

![Untitled](CRUD-DOM-1%20%5B120%20min%5D%20(1)%20f2873829c100496a9b4cc5ded3baa0ca/Untitled%205.png)

`PUT` is like giving something to server to replace an existing item completely. Its like replacing the number-blocks in the toy shelf with a new one. This method is used to update an existing resource on a server. For example, a user may use this method to change entire profile information.

[MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT)

### PATCH

![Untitled](CRUD-DOM-1%20%5B120%20min%5D%20(1)%20f2873829c100496a9b4cc5ded3baa0ca/Untitled%206.png)

`PATCH` is like telling server to change only a part of something. Its like changing just a number in the number-block. This method is similar to the PUT method, but it's used to update only part of a resource. For example, a user may use this method to change only their email address or their profile picture, without changing the rest of their profile.

[MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH)

### DELETE

![Untitled](CRUD-DOM-1%20%5B120%20min%5D%20(1)%20f2873829c100496a9b4cc5ded3baa0ca/Untitled%207.png)

`DELETE` is like telling server to get rid of something. Its like throwing away number-block from the toy shelf. This method is used to delete a resource from a server, such as a file or a record in a database.

[MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE)

## Trying out different HTTP Methods

Example server: [https://640f55c04ed25579dc4c7a34.mockapi.io/employees](https://640f55c04ed25579dc4c7a34.mockapi.io/employees) 

Server docs: [https://github.com/mockapi-io/docs/wiki](https://github.com/mockapi-io/docs/wiki) 

- Rest Client
    
    ![Untitled](CRUD-DOM-1%20%5B120%20min%5D%20(1)%20f2873829c100496a9b4cc5ded3baa0ca/Untitled%208.png)
    
    [https://marketplace.visualstudio.com/items?itemName=humao.rest-client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
    

```jsx
GET https://640f55c04ed25579dc4c7a34.mockapi.io/employees

###

GET https://640f55c04ed25579dc4c7a34.mockapi.io/employees/11

###

POST https://640f55c04ed25579dc4c7a34.mockapi.io/employees
Content-Type: application/json

{
  "name": "Jone DOE",
  "avatar": "https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/986.jpg"
}

###

PATCH https://640f55c04ed25579dc4c7a34.mockapi.io/employees/11
Content-Type: application/json

{
  "name": "JANEY"
}

###
DELETE https://640f55c04ed25579dc4c7a34.mockapi.io/employees/11
```

## Can you identify some of problems that can happen if all of try to do CRUD operations together in one of the online API’s

- We may quickly hit their free limits
- We may step on each other’s experiments
- etc.

## Whats a feasible solution?

- May be our own local server (Back end system running in our computer)

## Introduction to our new CP setup for DOM

- It is very different from the old setup. We must get familiar with it before the evaluations
- Towards the end of the class we will see how Masaischool has tried to solve this problem for us

## Could you explain the different types of HTTP responses to a request?

## Student task 1.

**Problem Statement:**

- On the click of `load-data` button, a GET request should be made to [`https://reqres.in/api/users`](https://reqres.in/api/users)
- The users should be rendered/displayed as the following screen-shot
    
    ![Untitled](CRUD-DOM-1%20%5B120%20min%5D%20(1)%20f2873829c100496a9b4cc5ded3baa0ca/Untitled%209.png)
    
- CSS styles have been written for you
- The Markup of the DOM Should exactly match the following screenshot
    
    ![Untitled](CRUD-DOM-1%20%5B120%20min%5D%20(1)%20f2873829c100496a9b4cc5ded3baa0ca/Untitled%2010.png)
    

Problem: [https://codepen.io/drupalastic/pen/gOjqKLY](https://codepen.io/drupalastic/pen/gOjqKLY) 

**1. Check the solution and make sure that you understand every bit of it**

Solution: [https://codepen.io/drupalastic/pen/zYLeazW?editors=0010](https://codepen.io/drupalastic/pen/zYLeazW?editors=0010) 

**2. Can you make the code cleaner?**

## Minor improvements in the way we have been working with DOM

**Why clean-code?**

![Untitled](CRUD-DOM-1%20%5B120%20min%5D%20(1)%20f2873829c100496a9b4cc5ded3baa0ca/Untitled%2011.png)

- Refactoring the code
- Creating card component
- Re-using card component

**Strategy**

- one function call to a function called `fetchAndRenderUsers()` inside of the event listener
- a reusable function to create a card called `getCard()`
- a reusable function to create the list called `getCardList()`

Solution:  [https://codepen.io/drupalastic/pen/XWBOBgQ?editors=0011](https://codepen.io/drupalastic/pen/XWBOBgQ?editors=0011) [Refactored]

## GET, filter, sort in the CP Setup

Additional parameters in Fetch

So far we have learned that the fetch function takes in a url and returns a promise object. The url that it takes is its first argument, it may also take an optional second argument, the type of which is a javascript object. We will be needing this object to POST some data to the server

```jsx
{
  method: 'POST'
}
```

Data in JSON format can be sent via body property

```jsx
{
  method: 'POST',
  body: 'json data here'
}
```

When we are sending some data, we need to tell the server that we are sending some JSON data (type) to it

```jsx
{
      method: 'POST',
      headers: { 
        'Content-type': 'application/json'
      },
      body: 'json data here'
    });
```

Headers are normally used for meta-data (some data about the data). 

- GET
    
    ```jsx
    // --- do not touch  ↓↓↓↓↓↓↓↓↓↓↓↓ ----------
    const baseServerURL = `http://localhost:${
      import.meta.env.REACT_APP_JSON_SERVER_PORT
    }`;
    // --- do not touch  ↑↑↑↑↑↑↑↑↑↑↑↑ ----------
    
    // ***** Constants / Variables ***** //
    const employeeURL = `${baseServerURL}/employees`;
    const userRegisterURL = `${baseServerURL}/register`;
    
    // Append div to main section
    let mainSection = document.getElementById("data-list-wrapper");
    
    //  add employees
    let empNameInput = document.getElementById("employee-name");
    let empImgInput = document.getElementById("employee-image");
    let empDeptInput = document.getElementById("employee-dept");
    let empSalaryInput = document.getElementById("employee-salary");
    let empCreateBtn = document.getElementById("add-employee");
    
    //Sorting 
    let sortAtoZBtn = document.getElementById("sort-low-to-high");
    let sortZtoABtn = document.getElementById("sort-high-to-low");
    
    //Filter 
    let filterLessThan1LBtn = document.getElementById("filter-less-than-1L");
    let filterMoreThanEqualLBtn = document.getElementById(
      "filter-more-than-equal-1L"
    );
    
    // Update employees
    let updateEmpIdInput = document.getElementById("update-employee-id");
    let updateEmpNameInput = document.getElementById("update-employee-name");
    let updateEmpImageInput = document.getElementById("update-employee-image");
    let updateEmpDeptInput = document.getElementById("update-employee-dept");
    let updateEmpSalaryInput = document.getElementById("update-employee-salary");
    let updateEmpUpdateBtn = document.getElementById("update-employee");
    
    //Update Salary
    let updateScoreEmpId = document.getElementById("update-score-employee-id");
    let updateScoreEmpSalary = document.getElementById(
      "update-score-employee-salary"
    );
    let updateScoreEmpSalaryButton = document.getElementById(
      "update-score-employee"
    );
    
    //Employee Data
    let employeesData = [];
    
    window.addEventListener("load", () => {
      fetchAndRenderUsers() 
    });
    
    // Fetch & render users
    function fetchAndRenderUsers() {
      fetch(`${baseServerURL}/employees`)
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          mainSection.innerHTML = null;
    
          const cardList = getCardList(data);
          mainSection.append(cardList);
        });
    }
    
    function getCardList(data) {
      const cardList = document.createElement("div");
      cardList.classList.add("card-list");
    
      data.forEach((item) => {
        let card = getCard(
          item.id,
          item.name,
          item.salary,
          `${baseServerURL}/${item.image}`
        );
    
        cardList.append(card);
      });
    
      return cardList;
    }
    
    function getCard(userId, fullName, email, imageUrl) {
    
      const card = document.createElement("div");
      card.classList.add("card");
      card.setAttribute("data-id", userId);
    
      const cardImage = document.createElement("div");
      cardImage.classList.add("card-img");
    
      const img = document.createElement("img");
      img.src = imageUrl;
      img.setAttribute("alt", "employee");
    
      cardImage.append(img);
    
      const cardBody = document.createElement("div");
      cardBody.classList.add("card-body");
    
      const cardTitle = document.createElement("div");
      cardTitle.classList.add("card-item");
      cardTitle.classList.add("card-title");
      cardTitle.innerText = fullName;
    
      const cardDescription = document.createElement("div");
      cardDescription.classList.add("card-item");
      cardDescription.classList.add("card-description");
      cardDescription.classList.add("card-salary");
      cardDescription.innerText = email;
    
      const cardEdit = document.createElement("a");
      cardEdit.setAttribute("href", "#");
      cardEdit.setAttribute("data-id", userId);
      cardEdit.setAttribute("data-name", fullName);
      cardEdit.setAttribute("class", "card-item card-link");
      cardEdit.innerText = "EDIT";
    
      cardBody.append(cardTitle);
      cardBody.append(cardDescription);
      cardBody.append(cardEdit);
      
      card.append(cardImage);
      card.append(cardBody);
    
      return card;
    }
    ```
    
- POST
    
    ```jsx
    // --- do not touch  ↓↓↓↓↓↓↓↓↓↓↓↓ ----------
    const baseServerURL = `http://localhost:${
      import.meta.env.REACT_APP_JSON_SERVER_PORT
    }`;
    // --- do not touch  ↑↑↑↑↑↑↑↑↑↑↑↑ ----------
    
    // ***** Constants / Variables ***** //
    const employeeURL = `${baseServerURL}/employees`;
    const userRegisterURL = `${baseServerURL}/register`;
    
    // Append div to main section
    let mainSection = document.getElementById("data-list-wrapper");
    
    //  add employees
    let empNameInput = document.getElementById("employee-name");
    let empImgInput = document.getElementById("employee-image");
    let empDeptInput = document.getElementById("employee-dept");
    let empSalaryInput = document.getElementById("employee-salary");
    let empCreateBtn = document.getElementById("add-employee");
    
    //Sorting 
    let sortAtoZBtn = document.getElementById("sort-low-to-high");
    let sortZtoABtn = document.getElementById("sort-high-to-low");
    
    //Filter 
    let filterLessThan1LBtn = document.getElementById("filter-less-than-1L");
    let filterMoreThanEqualLBtn = document.getElementById(
      "filter-more-than-equal-1L"
    );
    
    // Update employees
    let updateEmpIdInput = document.getElementById("update-employee-id");
    let updateEmpNameInput = document.getElementById("update-employee-name");
    let updateEmpImageInput = document.getElementById("update-employee-image");
    let updateEmpDeptInput = document.getElementById("update-employee-dept");
    let updateEmpSalaryInput = document.getElementById("update-employee-salary");
    let updateEmpUpdateBtn = document.getElementById("update-employee");
    
    //Update Salary
    let updateScoreEmpId = document.getElementById("update-score-employee-id");
    let updateScoreEmpSalary = document.getElementById(
      "update-score-employee-salary"
    );
    let updateScoreEmpSalaryButton = document.getElementById(
      "update-score-employee"
    );
    
    //Employee Data
    let employeesData = [];
    
    window.addEventListener("load", async () => {
      fetchAndRenderUsers() 
    });
    
    empCreateBtn.addEventListener("click", () => {
      // we need the data that was filled in
      let empName = empNameInput.value;
      let empImage = empImgInput.value;
      let empDept = empDeptInput.value;
      let empSalary = empSalaryInput.value;
    
      console.log(empName, empImage, empDept, empSalary)
    
      let newEmpObj = {
        name: empName,
        image: empImage,
        department: empDept,
        salary: empSalary
      }
    
      console.log(newEmpObj)
    
      fetch(`${baseServerURL}/employees`, {
        method: 'POST',
        body: JSON.stringify(newEmpObj),
        headers: { 
          'Content-type': 'application/json'
        },
      })
      .then((res) => res.json())
      .then((data) => {
        fetchAndRenderUsers();
      })
    })
    
    // Fetch & render users
    function fetchAndRenderUsers() {
      fetch(`${baseServerURL}/employees`)
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          mainSection.innerHTML = null;
    
          const cardList = getCardList(data);
          mainSection.append(cardList);
        });
    }
    
    function getCardList(data) {
      const cardList = document.createElement("div");
      cardList.classList.add("card-list");
    
      data.forEach((item) => {
        let card = getCard(
          item.id,
          item.name,
          item.salary,
          `${baseServerURL}/${item.image}`
        );
    
        cardList.append(card);
      });
    
      return cardList;
    }
    
    function getCard(userId, fullName, email, imageUrl) {
    
      const card = document.createElement("div");
      card.classList.add("card");
      card.setAttribute("data-id", userId);
    
      const cardImage = document.createElement("div");
      cardImage.classList.add("card-img");
    
      const img = document.createElement("img");
      img.src = imageUrl;
      img.setAttribute("alt", "employee");
    
      cardImage.append(img);
    
      const cardBody = document.createElement("div");
      cardBody.classList.add("card-body");
    
      const cardTitle = document.createElement("div");
      cardTitle.classList.add("card-item");
      cardTitle.classList.add("card-title");
      cardTitle.innerText = fullName;
    
      const cardDescription = document.createElement("div");
      cardDescription.classList.add("card-item");
      cardDescription.classList.add("card-description");
      cardDescription.classList.add("card-salary");
      cardDescription.innerText = email;
    
      const cardEdit = document.createElement("a");
      cardEdit.setAttribute("href", "#");
      cardEdit.setAttribute("data-id", userId);
      cardEdit.setAttribute("data-name", fullName);
      cardEdit.setAttribute("class", "card-item card-link");
      cardEdit.innerText = "EDIT";
    
      cardBody.append(cardTitle);
      cardBody.append(cardDescription);
      cardBody.append(cardEdit);
      
      card.append(cardImage);
      card.append(cardBody);
    
      return card;
    }
    ```