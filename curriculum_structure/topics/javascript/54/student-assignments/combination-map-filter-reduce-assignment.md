# assignment

## **.reduce() Method**

**Question1 :**

Given an array of objects with a **`name`** and **`age`** property, use **`.reduce()`** to calculate the average age of all objects in the array.

```jsx
const people = [
  { name: "Alice", age: 25 },
  { name: "Bob", age: 32 },
  { name: "Charlie", age: 19 },
  { name: "David", age: 47 },
  { name: "Emily", age: 28 }
];
```

**Question2 :**

Write a function `ProductOfEven` that takes an array of numbers as input and returns the product of all even numbers in the array, using **`.reduce()`**.

**Question3:**

Given an array of objects with a **`name`** and **`score`** property, use **`.reduce()`** to find the object with the highest score.

```jsx
const players = [
  { name: "Alice", score: 95 },
  { name: "Bob", score: 80 },
  { name: "Charlie", score: 62 },
  { name: "David", score: 73 },
  { name: "Emily", score: 87 },
  { name: "Frank", score: 55 },
  { name: "Gina", score: 90 }
];
```

**Question4:**

Write a function `UniqueString` that takes an array of strings as input and returns an object with the count of each unique string in the array, using **`.reduce()`**.

```jsx
//input format
const strings = ["apple", "banana", "apple", "orange", "banana", "pear", "apple"];

//output format

{
  apple: 3,
  banana: 2,
  orange: 1,
  pear: 1
}
```

**Question5:**

Given an array of numbers, use **`.reduce()`** to find the sum of all numbers that are divisible by 3 or 5.

```jsx
const numbers = [7, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597];
```

## **.filter() Method**

**Question1:**

Given an array of strings, write a function that returns a new array containing only the strings that are palindromes (i.e., read the same backwards as forwards) using **`.filter()`**.

```jsx
const words = ["racecar", "hello", "deified", "world", "level", "programming", "radar", "civic", "javascript"];
```

**Question2:**

Given an array of objects representing products with a **`price`** property, write a function that returns a new array containing only the products with a price greater than the average price of all products, using **`.filter()`**.

```jsx
const products = [
  { name: "iPhone", price: 999 },
  { name: "MacBook", price: 1499 },
  { name: "iPad", price: 799 },
  { name: "Apple Watch", price: 399 },
  { name: "AirPods", price: 249 }
];
```

**Question3:**

Given an array of strings representing file paths, write a function that returns a new array containing only the file paths that have a **`.png`** or **`.jpg`** extension, using **`.filter()`**.

```jsx
const filePaths = [
  "/images/pic1.jpg",
  "/images/pic2.png",
  "/assets/img/background.jpg",
  "/assets/img/logo.png",
  "/downloads/document.pdf",
  "/downloads/image.png",
  "/downloads/image.jpg"
];
```

## **.map() Method**

**Question1:**

Given an array of strings, write a function that returns a new array where each string has its first and last letters swapped using **`.map()`**.

```jsx
const strings = ["Hello", "world", "this", "is", "an", "example", "array", "of", "strings"];
```

**Question2:**

Given an array of numbers, write a function that returns a new array where each number is replaced with its absolute value multiplied by 2 using **`.map()`**.

```jsx
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
```

**Question3:**

Given an array of objects representing students with **`name`** and **`grade`** properties, write a function that returns a new array of strings with the format "NAME received a GRADE" for each student, using **`.map()`**.

```jsx
const students = [
  { name: "John", grade: 80 },
  { name: "Mary", grade: 95 },
  { name: "Bob", grade: 70 },
  { name: "Alice", grade: 90 },
  { name: "Peter", grade: 85 }
];
```

## **.foreach() Method**

**Question1:**

Given an array of objects representing customers with a **`name`** property, write a function that logs a greeting message to the console for each customer using **`.forEach()`**.

```jsx
const customers = [
  { name: "John Doe" },
  { name: "Mary Smith" },
  { name: "Bob Johnson" },
  { name: "Alice Lee" },
  { name: "Peter Kim" }
];
```

**Question2:**

Given an array of numbers, write a function that logs the sum of all numbers to the console using **`.forEach()`**.

```jsx
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
```

**Question3:**

Given an array of strings representing sentences, write a function that logs the number of words in each sentence to the console using **`.forEach()`**.

```jsx
const sentences = [
  "The quick brown fox jumps over the lazy dog.",
  "She sells seashells by the seashore.",
  "I have a dream that one day this nation will rise up.",
  "To be or not to be, that is the question.",
  "In the beginning, God created the heavens and the earth."
];
```

## **Combination of all Methods**

**Question1:**

Given an array of objects representing employees with **`name`**, **`salary`**, and **`department`** properties, write a function `getTotalSalaryByDepartment` that returns the total salary of all employees in a given department using **`.filter()`** and **`.reduce()`**.

```jsx
const employees = [
  { name: "John", salary: 50000, department: "IT" },
  { name: "Mary", salary: 60000, department: "HR" },
  { name: "Bob", salary: 70000, department: "IT" },
  { name: "Alice", salary: 80000, department: "Sales" },
  { name: "Peter", salary: 90000, department: "Sales" }
];
```

**Question2:**

Given an array of numbers, write a function `sumOfSquaresOfOddNumbers` that returns the sum of the squares of all odd numbers using **`.map()`**, **`.filter()`**, and **`.reduce()`**.

```jsx
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
```

**Question3:**

The function `massageArray()` is expected to return an array of objects.

Parameter of `massageArray()`: `inputArray` of type array

### **Provided `typeOfCourse`:**

```jsx
let typeOfCourse = [
  { id: 1, name: "Developer" },
  { id: 2, name: "Tester" },
];
```

**Provided `categories`**

```jsx
let CourseDurationDirectory = {
  1: `6 month`,
  2: `1 year`,
  3: `2 year`,
};
```

**Example Input Array:**

```jsx
let exampleInputArray = [
  {
    courseName: "masai frontend web26",
    courseDuration: 2,
    Category: 3,
    type: 1,
    techTools: {
      1: "HTML",
      2: "CSS",
      3: "javaScript",
      4: "React",
      5: "Redux",
      6: "Node.js",
      7: "Express",
      8: "MongoDB",
      9: "Bootstrap",
      10: "",
      11: "",
      12: "",
      13: "",
      14: "",
      15: "",
      16: null,
      17: null,
      18: null,
      19: null,
      20: null,
    },
    techdetails: {
      1: "HTML is the standard markup language for Web pages.",
      2: "CSS is the language we use to style an HTML document. ",
      3: "JavaScript is the programming language of the Web. JavaScript is easy to learn.",
      4: "React is a JavaScript library for building user interfaces.",
      5: "Redux is an open-source JavaScript library for managing and centralizing application state.",
      6: "Node.js® is a JavaScript runtime built on Chrome's V8 JavaScript engine.",
      7: "Express is a minimal and flexible Node.js web application framework .",
      8: "MongoDB is a document database. It stores data in a type of JSON format called BSON.",
      9: "Bootstrap utilizes Sass for a modular and customizable architecture. ",
      10: "",
      11: "",
      12: "",
      13: "",
      14: "",
      15: "",
      16: null,
      17: null,
      18: null,
      19: null,
      20: null,
    },
  },
  {
    courseName: "foundation batch",
    courseDuration: 2,
    Category: 4,
    type: 2,
    techTools: {
      1: "aptitude",
      2: "GitHub",
      3: "C",
      4: "",
      5: "",
      6: "",
      7: "",
      8: "",
      9: "",
      10: "",
      11: "",
      12: "",
      13: "",
      14: "",
      15: "",
      16: null,
      17: null,
      18: null,
      19: null,
      20: null,
    },
    techdetails: {
      1: "1. a natural ability or skill: 2. a natural ability or skill:",
      2: "The open source community is the heart of GitHub and fundamental to how we build software today.",
      3: "C is a general-purpose programming language, developed in 1972",
      4: "",
      5: "",
      6: "",
      7: "",
      8: "",
      9: "",
      10: "",
      11: "",
      12: "",
      13: "",
      14: "",
      15: "",
      16: null,
      17: null,
      18: null,
      19: null,
      20: null,
    },
  },
  {
    courseName: "Java batch",
    courseDuration: 1,
    Category: 5,
    type: 1,
    techTools: {
      1: "ETL",
      2: "Perl",
      3: "C#",
      4: "Python",
      5: "PHP",
      6: "",
      7: "",
      8: "",
      9: "",
      10: "",
      11: "",
      12: "",
      13: "",
      14: "",
      15: "",
      16: null,
      17: null,
      18: null,
      19: null,
      20: null,
    },
    techdetails: {
      1: "ETL is used to replicate and auto sync data from various source databases to a cloud data warehouse",
      2: "Perl is a high-level scripting language",
      3: "C# was originally designed to be easy to learn and use",
      4: "Python is one of the most beginner-friendly programming languages out there.",
      5: "PHP is a scripting language running on the server side",
      6: "",
      7: "",
      8: "",
      9: "",
      10: "",
      11: "",
      12: "",
      13: "",
      14: "",
      15: "",
      16: null,
      17: null,
      18: null,
      19: null,
      20: null,
    },
  },
];
```

• If `techTools` and `techdetails` values are null or "" avoid them in the output array.

**Expected output with the above input:**

```jsx
let eo1 = [
    {
      courseName: "masai frontend web26",
      courseDuration: "1 year",
      Category: "Fullstack",
      type: "Developer",
      techTools: [
        {
          language: "HTML",
          details: "HTML is the standard markup language for Web pages.",
        },
        {
          language: "CSS",
          details: "CSS is the language we use to style an HTML document. ",
        },
        {
          language: "javaScript",
          details:
            "JavaScript is the programming language of the Web. JavaScript is easy to learn.",
        },
        {
          language: "React",
          details: "React is a JavaScript library for building user interfaces.",
        },
        {
          language: "Redux",
          details:
            "Redux is an open-source JavaScript library for managing and centralizing application state.",
        },
        {
          language: "Node.js",
          details:
            "Node.js® is a JavaScript runtime built on Chrome's V8 JavaScript engine.",
        },
        {
          language: "Express",
          details:
            "Express is a minimal and flexible Node.js web application framework .",
        },
        {
          language: "MongoDB",
          details:
            "MongoDB is a document database. It stores data in a type of JSON format called BSON.",
        },
        {
          language: "Bootstrap",
          details:
            "Bootstrap utilizes Sass for a modular and customizable architecture. ",
        },
      ],
    },
    {
      courseName: "foundation batch",
      courseDuration: "1 year",
      Category: "manual tester",
      type: "Tester",
      techTools: [
        {
          language: "aptitude",
          details:
            "1. a natural ability or skill: 2. a natural ability or skill:",
        },
        {
          language: "GitHub",
          details:
            "The open source community is the heart of GitHub and fundamental to how we build software today.",
        },
        {
          language: "C",
          details:
            "C is a general-purpose programming language, developed in 1972",
        },
      ],
    },
    {
      courseName: "Java batch",
      courseDuration: "6 month",
      Category: "automation tester",
      type: "Developer",
      techTools: [
        {
          language: "ETL",
          details:
            "ETL is used to replicate and auto sync data from various source databases to a cloud data warehouse",
        },
        { language: "Perl", details: "Perl is a high-level scripting language" },
        {
          language: "C#",
          details: "C# was originally designed to be easy to learn and use",
        },
        {
          language: "Python",
          details:
            "Python is one of the most beginner-friendly programming languages out there.",
        },
        {
          language: "PHP",
          details: "PHP is a scripting language running on the server side",
        },
      ],
    },
  ]
```

### **Mapping of properties from input to expected output**

- *`courseName`* maps to courseName
- *`courseDuration`* maps to Category, but the id turns into the name
- *`Category`* maps to CourseDurationDirectory, but the id turns into the name
- *`type`* maps to typeOfCourse, but the id turns into the name
- finally, 20 key-value pair techTools object & 20 key-value pair techdetails object turns into a single entry of `techTools` which is an array of object. Each object of techTools contains a key called `language` and another key called `details`.

### Problem Statement: 1

```jsx
let users = [
{id: 1, name: "John"},
{id: 2, name: "Pete"},
{id: 3, name: "Mary"}
];

let newArr = /* your code here */

/*
Use the proper array method such that the newArr becomes:
{John: 1, Pete: 2, Mary: 3}

Note: the order does not matter here.

Problem Statement: you are expected to use of the array methods
to create a new object called newArr using the user's Array.

the keys of the new object (newArr) would be the name of the user
and the values would be the id of the user
*/
```

### Problem Statement: 2

```jsx
let users = [
  {age: 16},
  {age: 20},
  {age: 23},
  {age: 30}
];

/*
Problem Statement: 

Use the proper array method such that the newArr becomes: 
 [16,20,23,30]
 
The newArr is simply an array of numbers, in this problem the ages of the users. 
*/

console.log(newArr); // [16,20,23,30]

```

### Problem Statement: 3

```jsx
let data = [
  { name: "John", subject: "Javascript" },
  { name: "John", subject: "HTML" },
  { name: "John", subject: "CSS" },
  { name: "Pete", subject: "Java" },
  { name: "Pete", subject: "English" },
  { name: "Pete", subject: "Maths" },
  { name: "Mary", subject: "Rust" },
  { name: "Mary", subject: "Elm" },
]

console.log(subjectHash);
/*
Expected output:
{
  John: ["Javascript", "HTML", "CSS"],
  Pete: ["Java", "English", "Maths"],
  Mary: ["Rust", "Elm"]
}
*/

/*
 - Use proper array methods to create an object from the data array.
 - from the data, the name would become the key of the new object.
 - keys must be unique, one key per user.
 - the value would be an array of their subjects.
*/
```

### Problem Statement: 4

```jsx
let john = { name: "John", surname: "Smith", id: 1 };
let pete = { name: "Pete", surname: "Hunt", id: 2 };
let mary = { name: "Mary", surname: "Key", id: 3 };

let users = [ john, pete, mary ];

let usersMapped = /* ... your code ... */

/* 
end result/sample output: 
usersMapped = [
  { fullName: "John Smith", id: 1 },
  { fullName: "Pete Hunt", id: 2 },
  { fullName: "Mary Key", id: 3 }
]
*/

console.log(usersMapped);    
console.log(usersMapped[0].id) // 1
console.log(usersMapped[0].fullName) // John Smith

/*
 form a new array using the users array
 the new array is expected to have objects with the following properties:
  - fullName: <name><space><surname> 
  - id: <id>
 check the end result / sample output in the comment above. 
*/
```

### Problem Statement: 5

```jsx
function getGreeting(firstName, lastName) {
  return `Hi from ${firstName} ${lastName}.`
}

let john = { name: "John", surname: "Smith", id: 1 };
let pete = { name: "Pete", surname: "Hunt", id: 2 };
let mary = { name: "Mary", surname: "Key", id: 3 };

let users = [ john, pete, mary ];

let usersGreetings = /* your code here */  

console.log(usersGreetings) // ["Hi from John Smith.", "Hi from Pete Hunt.","Hi from Mary Key."]

/*
  Use of the array functions to manipulate the users array. We need a new array called usersGreetings.
  usersGreetings will be an array of strings: ["Hi from John Smith.", "Hi from Pete Hunt.","Hi from Mary Key."]
  You are expected to use the getGreeting function inside the callback of the array method that you choose to use.
*/
```

### Problem Statement: 6

```jsx
let subjectsHash = {
  1: 'Javascript',
  2: 'HTML',
  3: 'CSS',
  4: 'Java',
  5: 'Rust',
}

let students = [
  {id: 1, name: 'Prateek', subjectID: 5},
  {id: 2, name: 'Yogesh', subjectID: 2},
  {id: 3, name: 'Nrupul', subjectID: 4},
  {id: 4, name: 'Prateek', subjectID: 1},
]

let newObj = /* your code here */

console.log(newObj);

/* 
----------------------------------
create a new object called `newObj` using the `students` array &  
the `subjectsHash` object.
----------------------------------

Expected Output of `newObj`: 
{
  Prateek: ["Rust", "Javascript"],
  Yogesh: ["HTML"],
  Nrupul: ["Java"],
}
*/
```

### Problem Statement: 7

```jsx
let subjectsData = [
  {id: 1, name: 'Javascript'},
  {id: 2, name: 'HTML'},
  {id: 3, name: 'CSS'},
  {id: 4, name: 'Java'},
  {id: 5, name: 'Rust'},
]

// code your key-value object for subjects here

let students = [
  {id: 1, name: 'Prateek', subjectID: 5},
  {id: 2, name: 'Yogesh', subjectID: 2},
  {id: 3, name: 'Nrupul', subjectID: 4},
  {id: 4, name: 'Prateek', subjectID: 1},
]

let newObj = /* your array method here */ 

console.log(newObj);

/* 
----------------------------------
create a new object called `newObj` using the `students` array &  
the `subjectsData` array.

Hint: consider creating an extra key-value object for quickly accessing subject names
----------------------------------

Expected Output of `newObj`: 
{
  Prateek: ["Rust", "Javascript"],
  Yogesh: ["HTML"],
  Nrupul: ["Java"],
}
*/
```

### Problem Statement: 8

```jsx
let prateekMarksData = {
  name: "Prateek",
  subject1: "Javascript",
  subject2: "HTML",
  subject3: "CSS",
  subject4: null,
  subject5: null,
  marks1: 90, 
  marks2: 81,
  marks3: 80,
  marks4: null,
  marks5: null,
}

let nrupulMarksData = {
  name: "Nrupul",
  subject1: "Java",
  subject2: "Pyton",
  subject3: null,
  subject4: null,
  subject5: null,
  marks1: 95, 
  marks2: 85,
  marks3: null,
  marks4: null,
  marks5: null,
}

let allStudentsMarksData = [prateekMarksData, nrupulMarksData];

let massagedData = allStudentsMarksData.reduce((acc, item)=>{
  
},[])

console.log(massagedData);

/*
 ------------------------------------------------
 massage the `allStudentsMarksData` to get a new 
 array called `massagedData`

 Instead of separate enties for 5 subjects and their marks,
 in the new array, we just have one entry called marks. 
 marks is an array of objects. the objects of marks
 contains subject and score.
 ------------------------------------------------

  Expected output from `massagedData`

  [
     {
       name: "Prateek", 
       marks: [
         {subject: 'Javascript', score: 90},
         {subject: 'HTML', score: 81},
         {subject: 'CSS', score: 80}
       ]
     },
     {
       name: "Nrupul", 
       marks: [
         {subject: 'Java', score: 95},
         {subject: 'Python', score: 85}
       ]
     },

  ]

*/
```

### Problem Statement: 9

```jsx
const wishlist = [
  { title: "Tesla Model S", price: 90000 },
  { title: "4 carat diamond ring", price: 45000 },
  { title: "Fancy hacky Sack", price: 5 },
  { title: "Gold fidgit spinner", price: 2000 },
  { title: "A second Tesla Model S", price: 90000 }
];

// Given an array of all your wishlist items, figure out how much it would cost to just buy everything at once: 227005
```

### Problem Statement: 10

```jsx
const voters = [
  {name:'Bob' , age: 30, voted: true},
  {name:'Jake' , age: 32, voted: true},
  {name:'Kate' , age: 25, voted: false},
  {name:'Sam' , age: 20, voted: false},
  {name:'Phil' , age: 21, voted: true},
  {name:'Ed' , age:55, voted:true},
  {name:'Tami' , age: 54, voted:true},
  {name: 'Mary', age: 31, voted: false},
  {name: 'Becky', age: 43, voted: false},
  {name: 'Joey', age: 41, voted: true},
  {name: 'Jeff', age: 30, voted: true},
  {name: 'Zack', age: 19, voted: false}
];

/*
{ numYoungVotes: 1,
  numYoungPeople: 4,
  numMidVotesPeople: 3,
  numMidsPeople: 4,
  numOldVotesPeople: 3,
  numOldsPeople: 4
}
*/
```

### Problem Statement: 11

```jsx
const data = [
  { name: 'Superman', favoriteIceCreams: ['Strawberry', 'Vanilla', 'Chocolate', 'Cookies & Cream'] },
  { name: 'Batman', favoriteIceCreams: ['Cookies & Cream', 'Mint Chocolate Chip', 'Chocolate', 'Vanilla'] },
  { name: 'Flash', favoriteIceCreams: ['Chocolate', 'Rocky Road', 'Pistachio', 'Banana'] },
  { name: 'Aquaman', favoriteIceCreams: ['Vanilla', 'Chocolate', 'Mint Chocolate Chip'] },
  { name: 'Green Lantern', favoriteIceCreams: ['Vanilla', 'French Vanilla', 'Vanilla Bean', 'Strawberry'] },
  { name: 'Robin', favoriteIceCreams: ['Strawberry', 'Chocolate', 'Mint Chocolate Chip'] }
];

/*
{
  Strawberry: 3,
  Vanilla: 4,
  Chocolate: 5,
  'Cookies & Cream': 2,
  'Mint Chocolate Chip': 3,
  'Rocky Road': 1,
  Pistachio: 1,
  Banana: 1,
  'French Vanilla': 1,
  'Vanilla Bean': 1
}
*/
```