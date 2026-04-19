# Problem:

## Title
JSON Server CRUD Operations with Filter and Sort

## Level
Intermediate

## Time to solve the problem
3 hours

## Overview
This problem focuses on creating a web application that performs CRUD (Create, Read, Update, Delete) operations on a set of products stored in a JSON Server. Additionally, the application should include functionality for filtering and sorting the product data.

## Detailed Explanation

### Topics
- JSON Server
- CRUD Operations
- Filtering
- Sorting
- Frontend Development
- User Interface Design

### Setup Guidelines and Instructions
1. Set up your own JSON Server. You can use tools like `json-server` to create a RESTful API.
- [json server doc](https://www.npmjs.com/package/json-server)
2. Create and db.json filter for the data of books. the sample is provided.
3. Implement a web application that interacts with your JSON Server to perform CRUD operations on the product data.
4. Include features for filtering products based on categories and sorting products based on price or name.
5. Develop a user-friendly interface that allows users to view, add, edit, and delete products.

### Problem Statement

db.json

```
{
  "books": [
    {
      "id": 1,
      "title": "Harry Potter and the Philosopher's Stone",
      "author": "J.K. Rowling",
      "category": "Fantasy",
      "image": "https://user-images.githubusercontent.com/101581634/234347858-680f0add-e33b-4bb0-afc4-3afd1409a766.jpg",
      "price": 1089
    },
    {
      "id": 2,
      "title": "The Adventures of Huckleberry Finn",
      "author": "Mark Twain",
      "category": "Classic",
      "image": "https://user-images.githubusercontent.com/101581634/234347869-af3cc4fa-6e67-4abf-a20b-75410105721d.jpg",
      "price": "17535"
    },
    {
      "id": 3,
      "title": "To Kill a Mockingbird",
      "author": "Harper Lee",
      "category": "Classic",
      "image": "https://user-images.githubusercontent.com/101581634/234347837-8ab1d54d-74e1-48c3-8b2d-fbcc2e4c060c.jpg",
      "price": 6652
    },
    {
      "id": 4,
      "title": "The Odyssey",
      "author": "Homer",
      "category": "Epic poem",
      "image": "https://user-images.githubusercontent.com/101581634/234347820-e51d5678-4633-4779-89fc-00c63b34457b.jpg",
      "price": 785
    },
    {
      "id": 5,
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "category": "Classic",
      "image": "https://user-images.githubusercontent.com/101581634/234347792-2e36e823-95bb-4a8f-9189-0b894d74b2d8.jpg",
      "price": 2895
    },
    {
      "id": 6,
      "title": "Pride and Prejudice",
      "author": "Jane Austen",
      "category": "Romance",
      "image": "https://user-images.githubusercontent.com/101581634/234347864-8c6acce9-e900-49c1-b6ab-2a2ee00ee804.jpg",
      "price": 3641
    },
    {
      "id": 7,
      "title": "The Catcher in the Rye",
      "author": "J.D. Salinger",
      "category": "Coming of age",
      "image": "https://user-images.githubusercontent.com/101581634/234347874-148612ae-7123-4b5c-a571-e3032305c115.jpg",
      "price": 856
    },
    {
      "id": 8,
      "title": "The Lord of the Rings",
      "author": "J.R.R. Tolkien",
      "category": "Fantasy",
      "image": "https://user-images.githubusercontent.com/101581634/234347813-6471cf73-d97f-475d-b39a-ae78664809e8.jpg",
      "price": 542
    },
    {
      "id": 9,
      "title": "Animal Farm",
      "author": "George Orwell",
      "category": "Political satire",
      "image": "https://user-images.githubusercontent.com/101581634/234347848-b77080cc-8ff6-4106-a9a9-85c9dd417412.jpg",
      "price": 4177
    },
    {
      "id": 10,
      "title": "The Hobbit",
      "author": "J.R.R. Tolkien",
      "category": "Fantasy",
      "image": "https://user-images.githubusercontent.com/101581634/234347807-eb036bad-42b3-4d03-a230-1a2e404cb961.jpg",
      "price": 6981
    }
  ]
}
```

### Problem 1: List of books on page load


On page load, a list of all books should be shown in the `div#data-list-wrapper`.

Expected markup (Book card list):

```html
<!-- The div.card is a card appended to the div with div.card-list where all such cards are appended. -->
<div class="card-list">
  <!-- Example single card div inside card-list div -->
  <div class="card" data-id="{id of div}">
    <!-- div.card-image in this image of the book is present. -->
    <div class="card-image">
      <!-- Image of the book -->
    </div>
    <!-- div.card-body in this -->
    <div class="card-body">
      <h4 class="card-title">Title of the book</h4>
      <p class="card-author">Author of the book</p>
      <p class="card-category">Category of the book</p>
      <p class="card-price">Price of the book</p>
      <a href="#" class="card-link" data-id="{id of the book}">Edit</a>
      <button class="card-button" data-id="{id of the book}">Delete</button>
    </div>
  </div>
</div>

```

Data mapping:

- The data should be fetched from **`${baseServerURL}/books`**
- baseServerURL - your json server url
- The books should be shown on page load

### **Problem 2: Ability to add new Books **

Make a 'POST' request at **`${baseServerURL}/books`**. The page must not reload; the list must update.

### **Problem 3: Ability to delete a Book **

In each book card, add a button "Delete" with **`button.card-button`**. On clicking this button, the particular book must be removed from DOM as well as **`db.json`**. Make a 'DELETE' request at **`${baseServerURL}/books/{bookId}`**. The page must not reload; the list must update.

### **Problem 4: Ability to update all the fields of a book **

Able to populate the following input on the "Edit" link click.

- Add an event listener with a click to the anchor tag with class **`.card-link`**. Use preventDefault.
- The page should not reload on the click of the "Edit" link **`.card-link`**.
- To update all fields:
    - **`#update-book-id`** should be populated with the id of the book.
    - **`#update-book-title`** should be populated with the title of the book.
    - **`#update-book-image`** should be populated with the image URL of the book.
    - **`#update-book-author`** should be populated with the author of the book.
    - **`#update-book-category`** should be populated with the category of the book.
    - **`#update-book-price`** should be populated with the price of the book.
- Make a 'PATCH' request at **`${baseServerURL}/books/${bookId}`** to update title, image, author, category, and price. The page must not reload; the list must update.


### **Problem 5: Sorting Books Based on Price **

Sorting for Low to High UI:

- With the click of the button **`#sort-low-to-high`**, the book list should be sorted in ascending order based on their price.
- With the click of the button **`#sort-high-to-low`**, the book list should be sorted in descending order based on their price.

### **Problem 6: Filtering Books based on the category **

You have to create three types of filters as:

- Classic
- Fantasy
- Mystery
Filtering for Fantasy UI:
- When the button **`#filter-Classic`** is clicked, the book list is expected to be filtered. It should only show the books whose category is Classic.
- When the button **`#filter-Fantasy`** is clicked, the book list is expected to be filtered. It should only show the books whose category is Fantasy.
- When the button **`#filter-Mystery`** is clicked, the book list is expected to be filtered. It should only show the books whose category is Mystery.



**Note:** Get the updated data from API after POST, PATCH, or DELETE request is done.



### Submission Guidelines

- Save your work and push the code to your GitHub repository. Submit the GitHub repo link.
- Ensure your code is well-commented, explaining the purpose of major sections and key lines.
- Test your application thoroughly, making sure that all CRUD operations, filtering, and sorting functionalities work as expected.
- Submit your file by the deadline provided by your instructor or course platform

# Solution
