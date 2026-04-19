# Higher Order Function [120 min] (1)

A function that takes another function as a parameter or returns a function is known as a higher-order function.

[A`rray.reduce()` (1)](Higher%20Order%20Function%20%5B120%20min%5D%20(1)%208d55da0a5d3f4f729fb055b5c29a742e/Array%20reduce()%20(1)%200ae42ce84d8d4950a750c088c2e56359.md)

## How does array.reduce works

```jsx
//It is an array method
// It takes in a callback function & an initial value
// The callback function is invoked array. length number of times
//In every iteration I can make changes to the accumulated value
//In every iteration I have access to the current item in the original array
//In the first iteration, the initial value in the accumulated value
//Whatever is returned from the previous iteration becomes the acc value for the next iteration
// whatever is returned from the last iteration becomes the accumulated value
// It is normally used when we need a different shape of output
```

## How does the array.filter method works

```jsx
// How array.filter works
// Its an array method
// It returns a new array
//The length of the the new array may be different from the original array
// it takes in a callback function 
// the callback function gets the current item in every iteration
// the callback function is invoked original array.length number of times
// if the cb function returns a truthy value the current item is added to the output array
// the the cb function returns a falsy value the current item is not added to the output array
```

## How does the [array.map](http://array.map) works

```jsx
// How does Array.prototype.map work?
//It is an array method
// It returns a new array
//The length of the output array is the same as the length of the input array
//It takes in a callback function
//The callback function is called for each item in the input array
//In every iteration we have access to the current item 
// whatever you return from the cb function becomes the item of the output array
```

## Array.prototype.sort

Imagine you have a group of your friends lined up to take a photo together. You want them to stand in order based on their height, so the shortest person is on the left and the tallest person is on the right. In real life, you'd ask your friends to move around and swap places until they're in the correct order.

Now, think of JavaScript arrays as a line of friends. Each friend represents an element in the array. The **`Array.prototype.sort()`** method helps you organize this line of friends based on certain criteria, just like organizing your friends by height.

Here's an example:

```jsx
let ages = [13, 15, 14, 12, 16];
ages.sort();
console.log(ages); // Output: [12, 13, 14, 15, 16]
```

In this example, the ages array represents a group of friends with different ages. Using the sort() method, you can organize them in ascending order, from the youngest to the oldest. By default, sort() converts the numbers to strings and sorts them in alphabetical order. In this case, the default behavior works fine because the ages are simple one or two-digit numbers.

Here's another example that sorts by color, and I'll explain how the **`sort()`**
 the method works in depth.

```jsx
let shapes = [
  {sides: 4, color: 'red'},
  {sides: 3, color: 'blue'},
  {sides: 4, color: 'blue'},
  {sides: 3, color: 'red'}
];

shapes.sort(function(a, b) {
  return a.color.localeCompare(b.color);
});

console.log(shapes);
// Output: [
//   {sides: 3, color: 'blue'},
//   {sides: 4, color: 'blue'},
//   {sides: 3, color: 'red'},
//   {sides: 4, color: 'red'}
// ]
```

In this example, we're only sorting the **`shapes`** array by the color property. The **`sort()`** method takes a custom function as a parameter, which we call a "compare function." This function is used to determine the order of the elements in the array. The compare function should return a negative, zero, or positive value, depending on the arguments, like:

- a negative value if **`a`** should be sorted before **`b`**
- a positive value if **`a`** should be sorted after **`b`**
- 0 if **`a`** and **`b`** are equal and their order doesn't matter

Here's how the **compare function** works in our example:

1. The **`sort()`** method starts comparing pairs of elements (in this case, objects) in the **`shapes`** array: **`a`** and **`b`**.
2. For each comparison, the compare function returns a value based on the **`color`** properties of **`a`** and **`b`**. We use the **`localeCompare()`** method, which compares two strings (colors) and returns a negative, positive, or zero value depending on the alphabetical order.
3. Based on the returned value, the **`sort()`** method rearranges the elements in the array until they're in the desired order.

The **`sort()`** method uses an algorithm to efficiently sort the array. While the exact algorithm may vary across JavaScript engines, it generally works as follows:

1. It starts by comparing the first two elements (a and b) using the compare function.
2. If the compare function returns a **negative** value, it means **`a`** should be **before** **`b`**, and they remain in the same order.
3. If the compare function returns a **positive** value, it means **`a`** should be **after** **`b`**, and their positions are swapped.
4. The algorithm continues comparing elements, sometimes splitting the array into smaller parts and sorting them individually, then combining the sorted parts (this is called "merge sort").

The process continues until the whole array is sorted. Keep in mind that the **`sort()`** method modifies the original array, so if you want to keep the original array unchanged, you should create a copy before sorting.

```jsx
shapes.sort(function(a, b) {
  console.log(a.color, b.color)
  // iteration: 1
  // a: {sides: 1, color: 'blue'}
  // b: {sides: 4, color: 'red'}

   if (a.sides < b.sides) {
    return -1
   } 

   if (a.sides > b.sides) {
    return 1
   }

   return 0;

  // the logic can return 
  // 0 : a and b are of equal order
  // -1 : a should come before b 
  // 1 : a should come after b
});

console.log(shapes);
```

```jsx
let shapes = [
  {sides: 4, color: 'âred'},
  {sides: 1, color: 'blue'},
  {sides: 3, color: 'crange'},
  {sides: 2, color: 'dreen'}
];

// output: 
// sorted by the color.

shapes.sort(function(a, b) {
  console.log(a.color, b.color)
  // iteration: 1
  // a: {sides: 1, color: 'blue'}
  // b: {sides: 4, color: 'âred'}

   if (a.color.localeCompare(b.color) === -1) {
    return -1
   } 

   if (a.color.localeCompare(b.color) === 1) {
    return 1
   }

   return 0;

  // the logic can return 
  // 0 : a and b are of equal order
  // -1 : a should come before b 
  // 1 : a should come after b
});

console.log(shapes);

// How does array.prototype.sort works in javascript
// its an array method
// it mutates the input array (in place)
// it takes in a callback function
// the callback function gets two items of the input array usually stored as a , b
// the callback function is expected to return either 0, a -ve number or a +ve number
// if the callback returns a -ve number this means that a should come before b;
// if the callback returns a +ve number this means that a should come after b;
// if the callback returns 0, this means, no change in order is required
```

```jsx
let a = 'clue'
let b = 'brange'
let c = 'aaaa'
let d = 'âaaa'

console.log(a.localeCompare(b));    
console.log(a.localeCompare(b));
```

MDN: [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare) 

### Student tasks :

- [https://codepen.io/adarshakhatua/pen/VwEdQqW?editors=0010](https://codepen.io/adarshakhatua/pen/VwEdQqW?editors=0010)
- [https://codepen.io/adarshakhatua/pen/MWZQaBo?editors=0010](https://codepen.io/adarshakhatua/pen/MWZQaBo?editors=0010)

### Map

- code snippet 1
    
    Create a function **`calculateAverageGrades`** that takes an array of student objects, where each object contains the student's name and an array of their grades. Use the **`map`** function to calculate the average grade for each student and return a new array of objects with each student's name and their average grade.
    
    ```jsx
    const students = [
      { name: "Alice", grades: [90, 85, 88] },
      { name: "Bob", grades: [78, 92, 87] },
      { name: "Charlie", grades: [85, 89, 92] }
    ];
    
    // Your code here
    
    console.log(calculateAverageGrades(students)); // Should log an array of objects with student names and their average grades.
    
    ```
    
- code snippet 2
    
    Create a function **`convertTemperatureUnits`** that takes an array of weather objects, where each object contains the city name, temperature in Celsius, and weather conditions. Use the **`map`** function to convert the temperature to Fahrenheit and return a new array of weather objects with the city name, temperature in Fahrenheit, and weather conditions.
    
    ```jsx
    javascriptCopy code
    const weatherData = [
      { city: "New York", temperatureC: 22, conditions: "Sunny" },
      { city: "Los Angeles", temperatureC: 30, conditions: "Partly Cloudy" },
      { city: "Chicago", temperatureC: 18, conditions: "Rainy" }
    ];
    
    // Your code here
    
    console.log(convertTemperatureUnits(weatherData)); // Should log an array of weather objects with temperatures in Fahrenheit.
    
    ```
    
- code snippet 3
    
    Create a function **`calculateFinalScores`** that takes an array of student objects, where each object contains the student's name and an array of test scores. Use the **`map`** function to calculate the final score for each student by averaging their test scores and return a new array of objects with the student names and their final scores.
    
    ```jsx
    javascriptCopy code
    const students = [
      { name: "Alice", testScores: [90, 85, 88] },
      { name: "Bob", testScores: [78, 92, 87] },
      { name: "Charlie", testScores: [85, 89, 92] }
    ];
    
    // Your code here
    
    console.log(calculateFinalScores(students)); // Should log an array of objects with student names and their final scores.
    
    ```
    
- code snippet 4
    
    Create a function **`findLongestWords`** that takes an array of sentences and uses the **`map`** function to find and return an array of the longest words from each sentence.
    
    ```jsx
    javascriptCopy code
    const sentences = [
      "The quick brown fox jumps over the lazy dog",
      "She sells seashells by the seashore",
      "How much wood would a woodchuck chuck"
    ];
    
    // Your code here
    
    console.log(findLongestWords(sentences)); // Should log an array of the longest words from each sentence.
    
    ```
    
- code snippet 5
    
    Create a function **`doubleNumbers`** that takes an array of numbers as an argument and uses the **`map`** function to return a new array where each number is doubled.
    
    ```jsx
    javascriptCopy code
    // Your code here
    
    console.log(doubleNumbers([1, 2, 3, 4, 5])); // Should log [2, 4, 6, 8, 10].
    
    ```
    
- code snippet 6
    
    Create a function **`squareRoots`** that takes an array of numbers as an argument and uses the **`map`** function to return a new array where each number is replaced with its square root.
    
    ```jsx
    javascriptCopy code
    // Your code here
    
    console.log(squareRoots([1, 4, 9, 16, 25])); // Should log [1, 2, 3, 4, 5].
    
    ```
    
- code snippet 7
    
    Create a function **`capitalizeWords`** that takes an array of words as an argument and uses the **`map`** function to return a new array where each word is in uppercase.
    
    ```jsx
    javascriptCopy code
    // Your code here
    
    console.log(capitalizeWords(["apple", "banana", "cherry"])); // Should log ["APPLE", "BANANA", "CHERRY"].
    
    ```
    
- code snippet 8
    
    Create a function **`reverseStrings`** that takes an array of strings as an argument and uses the **`map`** function to return a new array where each string is reversed.
    
    ```jsx
    javascriptCopy code
    // Your code here
    
    console.log(reverseStrings(["hello", "world", "javascript"])); // Should log ["olleh", "dlrow", "tpircsavaj"].
    
    ```
    
- code snippet 9
    
    Create a function **`celsiusToFahrenheit`** that takes an array of temperatures in Celsius as an argument and uses the **`map`** function to return a new array where each temperature is converted to Fahrenheit using the formula **`(C * 9/5) + 32`**.
    
    ```jsx
    javascriptCopy code
    // Your code here
    
    console.log(celsiusToFahrenheit([0, 20, 37, -10, 100])); // Should log [32, 68, 98.6, 14, 212].
    
    ```
    
- code snippet 10
    
    Create a function **`extractNames`** that takes an array of objects representing people and uses the **`map`** function to return a new array containing just their names.
    
    ```jsx
    javascriptCopy code
    const people = [
      { name: "Alice", age: 28 },
      { name: "Bob", age: 35 },
      { name: "Charlie", age: 42 }
    ];
    
    // Your code here
    
    console.log(extractNames(people)); // Should log ["Alice", "Bob", "Charlie"].
    
    ```
    
- code snippet 11
    
    Create a function **`calculateAges`** that takes an array of objects representing people and uses the **`map`** function to return a new array of objects with an additional property **`birthYear`** calculated based on the current year and their age.
    
    ```jsx
    javascriptCopy code
    const people = [
      { name: "Alice", age: 28 },
      { name: "Bob", age: 35 },
      { name: "Charlie", age: 42 }
    ];
    
    // Your code here
    
    console.log(calculateAges(people)); // Should log an array of objects with "birthYear" properties added.
    
    ```
    
- code snippet 12
    
    Create a function **`convertTemperatures`** that takes an array of objects representing cities with temperatures in Celsius and uses the **`map`** function to return a new array of objects where the temperatures are converted to Fahrenheit.
    
    ```jsx
    javascriptCopy code
    const cities = [
      { name: "New York", temperatureC: 22 },
      { name: "Los Angeles", temperatureC: 30 },
      { name: "Chicago", temperatureC: 18 }
    ];
    
    // Your code here
    
    console.log(convertTemperatures(cities)); // Should log an array of objects with temperat
    
    ```
    
- code snippet 13
    
    Create a function **`modifyPrices`** that takes an array of product objects and uses the **`map`** function to return a new array of objects where the prices are increased by 10%.
    
    ```jsx
    javascriptCopy code
    const products = [
      { name: "Laptop", price: 1000 },
      { name: "Phone", price: 500 },
      { name: "Tablet", price: 300 }
    ];
    
    // Your code here
    
    console.log(modifyPrices(products)); // Should log an array of objects with modified prices.
    
    ```
    

### Filter

- code snippet 1
    
    Create a function **`filterOddNumbers`** that takes an array of numbers as an argument and uses the **`filter`** method to return a new array containing only the even numbers.
    
    ```jsx
    // Your code here
    
    console.log(filterOddNumbers([1, 2, 3, 4, 5, 6])); // Should log an array of even numbers.
    
    ```
    
- code snippet 2
    
    Create a function **`filterShortWords`** that takes an array of words as an argument and uses the **`filter`** method to return a new array containing only the words that have a length of 5 or more characters.
    
    ```jsx
    // Your code here
    
    console.log(filterShortWords(["apple", "banana", "cherry", "date", "fig"])); // Should log an array of words with length 5 or more.
    
    ```
    
- code snippet 3
    
    Create a function **`filterPositiveNumbers`** that takes an array of numbers as an argument and uses the **`filter`** method to return a new array containing only the positive numbers.
    
    ```jsx
    // Your code here
    
    console.log(filterPositiveNumbers([-1, 2, -3, 4, -5, 6])); // Should log an array of positive numbers.
    
    ```
    
- code snippet 4
    
    Create a function **`filterStudentsByGrade`** that takes an array of student objects, where each object contains the student's name and grade. Use the **`filter`** method to return a new array of objects containing only the students with a grade of "A."
    
    ```jsx
    // Your code here
    
    const students = [
      { name: "Alice", grade: "B" },
      { name: "Bob", grade: "A" },
      { name: "Charlie", grade: "A" }
    ];
    
    console.log(filterStudentsByGrade(students)); // Should log an array of students with grade "A."
    
    ```
    
- code snippet 5
    
    Create a function **`filterEvenLengthWords`** that takes an array of words as an argument and uses the **`filter`** method to return a new array containing only the words with even lengths.
    
    ```jsx
    // Your code here
    
    console.log(filterEvenLengthWords(["apple", "banana", "cherry", "date", "fig"])); // Should log an array of words with even lengths.
    
    ```
    
- code snippet 6
    
    Create a function **`filterPrimeNumbers`** that takes an array of integers as an argument and uses the **`filter`** method to return a new array containing only the prime numbers.
    
    ```jsx
    // Your code here
    
    console.log(filterPrimeNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])); // Should log an array of prime numbers.
    
    ```
    
- code snippet 7
    
    Create a function **`filterStudentsByAge`** that takes an array of student objects, where each object contains the student's name and age. Use the **`filter`** method to return a new array of objects containing only the students who are 25 years old or older.
    
    ```jsx
    // Your code here
    
    const students = [
      { name: "Alice", age: 22 },
      { name: "Bob", age: 28 },
      { name: "Charlie", age: 26 }
    ];
    
    console.log(filterStudentsByAge(students)); // Should log an array of students aged 25 or older.
    
    ```
    
- code snippet 8
    
    Create a function **`filterBooksByGenre`** that takes an array of book objects, where each object contains the book's title and genre. Use the **`filter`** method to return a new array of objects containing only the books that belong to the "Science Fiction" genre.
    
    ```jsx
    // Your code here
    
    const books = [
      { title: "Dune", genre: "Science Fiction" },
      { title: "To Kill a Mockingbird", genre: "Fiction" },
      { title: "Neuromancer", genre: "Science Fiction" }
    ];
    
    console.log(filterBooksByGenre(books)); // Should log an array of "Science Fiction" books.
    
    ```
    
- code snippet 9
    
    Create a function **`filterUniqueValues`** that takes an array of values and uses the **`filter`** method to return a new array containing only the unique values (values that occur only once in the original array).
    
    ```jsx
    // Your code here
    
    console.log(filterUniqueValues([1, 2, 3, 2, 4, 5, 4, 6, 7, 8, 7])); // Should log an array of unique values.
    
    ```
    

### Reduce

- code snippet 1
    
    Create a function **`sumNumbers`** that takes an array of numbers as an argument and uses the **`reduce`** method to calculate and return the sum of all the numbers in the array.
    
    ```jsx
    // Your code here
    
    console.log(sumNumbers([1, 2, 3, 4, 5])); // Should log the sum of numbers.
    
    ```
    
- code snippet 2
    
    Create a function **`findMaxNumber`** that takes an array of numbers as an argument and uses the **`reduce`** method to find and return the maximum number in the array.
    
    ```jsx
    // Your code here
    
    console.log(findMaxNumber([13, 27, 8, 21, 42, 18])); // Should log the maximum number.
    
    ```
    
- code snippet 3
    
    Create a function **`calculateProduct`** that takes an array of numbers as an argument and uses the **`reduce`** method to calculate and return the product of all the numbers in the array.
    
    ```jsx
    // Your code here
    
    console.log(calculateProduct([2, 3, 4, 5])); // Should log the product of numbers.
    
    ```
    
- code snippet 4
    
    Create a function **`concatenateStrings`** that takes an array of strings as an argument and uses the **`reduce`** method to concatenate and return a single string containing all the strings from the array.
    
    ```jsx
    // Your code here
    
    console.log(concatenateStrings(["Hello", " ", "world", "!"])); // Should log the concatenated string.
    
    ```
    
- code snippet 5
    
    Create a function **`countWordOccurrences`** that takes an array of sentences and uses the **`reduce`** method to count the occurrences of each word. Return an object where the keys are words and the values are the counts.
    
    ```jsx
    // Your code here
    
    console.log(countWordOccurrences(["Hello world!", "This is a world of wonders.", "Hello, world!"])); // Should log an object with word counts.
    
    ```
    
- code snippet 6
    
    Create a function **`calculateTotalExpenses`** that takes an array of expense objects, where each object contains a description and an amount. Use the **`reduce`** method to calculate and return the total expenses.
    
    ```jsx
    // Your code here
    
    const expenses = [
      { description: "Groceries", amount: 50 },
      { description: "Rent", amount: 1000 },
      { description: "Utilities", amount: 200 },
    ];
    
    console.log(calculateTotalExpenses(expenses)); // Should log the total expenses.
    
    ```
    
- code snippet 7
    
    Create a function **`groupStudentsByDepartment`** that takes an array of student objects, where each object contains a name and a department. Use the **`reduce`** method to group the students by department and return an object where the keys are department names and the values are arrays of students in each department.
    
    ```jsx
    // Your code here
    
    const students = [
      { name: "Alice", department: "Math" },
      { name: "Bob", department: "Science" },
      { name: "Charlie", department: "Math" },
      { name: "David", department: "Computer Science" },
    ];
    
    console.log(groupStudentsByDepartment(students)); // Should log an object with students grouped by department.
    
    ```
    
- code snippet 8
    
    Create a function **`calculateTotalSalesByCategory`** that takes an array of sales objects, where each object contains a category and a sale amount. Use the **`reduce`** method to calculate and return an object where the keys are category names and the values are the total sales for each category.
    
    ```jsx
    // Your code here
    
    const sales = [
      { category: "Electronics", amount: 5000 },
      { category: "Clothing", amount: 3000 },
      { category: "Electronics", amount: 2500 },
      { category: "Furniture", amount: 1500 },
    ];
    
    console.log(calculateTotalSalesByCategory(sales)); // Should log an object with total sales by category.
    
    ```
    
- code snippet 9
    
    Create a function **`findMostCommonWord`** that takes an array of sentences and uses the **`reduce`** method to find and return the most common word in the sentences. Break ties by returning the word that appears first.
    
    ```jsx
    // Your code here
    
    const sentences = [
      "The quick brown fox jumps over the lazy dog.",
      "She sells seashells by the seashore.",
      "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
    ];
    
    console.log(findMostCommonWord(sentences)); // Should log the most common word.
    
    ```
    

### Combination of Map, filter, and reduce method

- code snippet 1
    
    Create a function **`calculateTotalSalesForElectronics`** that takes an array of sales objects, where each object contains a category and a sale amount. Use the **`filter`** method to filter out sales for the "Electronics" category and then use the **`reduce`** method to calculate and return the total sales for "Electronics."
    
    ```jsx
    javascriptCopy code
    // Your code here
    
    const sales = [
      { category: "Electronics", amount: 5000 },
      { category: "Clothing", amount: 3000 },
      { category: "Electronics", amount: 2500 },
      { category: "Furniture", amount: 1500 },
    ];
    
    console.log(calculateTotalSalesForElectronics(sales)); // Should log the total sales for "Electronics."
    
    ```
    
- code snippet 2
    
    Create a function **`calculateAverageGradeForDepartments`** that takes an array of student objects, where each object contains a name, department, and grade. Use the **`filter`** method to filter students by department, the **`map`** method to extract the grades, and the **`reduce`** method to calculate the average grade for each department. Return an object where the keys are department names and the values are the average grades for each department.
    
    ```jsx
    // Your code here
    
    const students = [
      { name: "Alice", department: "Math", grade: 85 },
      { name: "Bob", department: "Science", grade: 78 },
      { name: "Charlie", department: "Math", grade: 92 },
      { name: "David", department: "Science", grade: 85 },
    ];
    
    console.log(calculateAverageGradeForDepartments(students)); // Should log an object with average grades for each department.
    ```
    
- code snippet 3
    
    Create a function **`findMostExpensiveElectronicsProduct`** that takes an array of product objects, where each object contains a name, category, and price. Use the **`filter`** method to filter products in the "Electronics" category, and then use the **`reduce`** method to find and return the most expensive product in that category.
    
    ```jsx
    // Your code here
    
    const products = [
      { name: "Smartphone", category: "Electronics", price: 800 },
      { name: "Laptop", category: "Electronics", price: 1200 },
      { name: "Shirt", category: "Clothing", price: 25 },
      { name: "TV", category: "Electronics", price: 1000 },
    ];
    
    console.log(findMostExpensiveElectronicsProduct(products)); // Should log the most expensive "Electronics" product.
    
    ```
    
- code snippet 4
    
    Create a function **`calculateStudentRankings`** that takes an array of student objects, where each object contains a name and grade. Use the **`filter`** method to filter out students with a grade of 90 or above, the **`map`** method to extract their names, and the **`reduce`** method to rank them by average grade. Return an array of student names ranked from highest to lowest grade.
    
    ```jsx
    // Your code here
    
    const students = [
      { name: "Alice", grade: 85 },
      { name: "Bob", grade: 92 },
      { name: "Charlie", grade: 88 },
      { name: "David", grade: 95 },
    ];
    
    console.log(calculateStudentRankings(students)); // Should log an array of student names ranked by grade.
    
    ```
    
- code snippet 5
    
    Create a function **`findMostCommonWordByCategory`** that takes an array of blog post objects, where each object contains a category and text content. Use the **`filter`** method to filter blog posts by category, the **`map`** method to extract words from the text content, and the **`reduce`** method to find and return the most common word for each category. Return an object where the keys are category names and the values are the most common words in each category.
    
    ```jsx
    // Your code here
    
    const blogPosts = [
      { category: "Technology", content: "JavaScript is a programming language used for web development." },
      { category: "Travel", content: "Exploring new places and experiencing different cultures." },
      { category: "Technology", content: "Web development requires knowledge of HTML, CSS, and JavaScript." },
    ];
    
    console.log(findMostCommonWordByCategory(blogPosts)); // Should log an object with the most common words by category.
    
    ```
    
- code snippet 6
    
    Create a function **`calculateTotalSalesPerMonth`** that takes an array of sales objects, where each object contains a date, category, and sale amount. Use the **`map`** method to extract the month from the date, the **`filter`** method to filter sales by category, and the **`reduce`** method to calculate and return an object where the keys are months and the values are the total sales for each month.
    
    ```jsx
    // Your code here
    
    const sales = [
      { date: "2023-01-15", category: "Electronics", amount: 5000 },
      { date: "2023-01-20", category: "Clothing", amount: 3000 },
      { date: "2023-02-10", category: "Electronics", amount: 2500 },
      { date: "2023-02-25", category: "Electronics", amount: 3500 },
    ];
    
    console.log(calculateTotalSalesPerMonth(sales)); // Should log an object with total sales per month.
    
    ```
    
- code snippet 7
    
    Create a function **`groupStudentsAndCalculateAverageGrades`** that takes an array of student objects, where each object contains a name, department, and grade. Use the **`reduce`** method to group students by department and calculate the average grade for each department. Return an object where the keys are department names, and the values are arrays of student names within each department and their average grade.
    
    ```jsx
    // Your code here
    
    const students = [
      { name: "Alice", department: "Math", grade: 85 },
      { name: "Bob", department: "Science", grade: 78 },
      { name: "Charlie", department: "Math", grade: 92 },
      { name: "David", department: "Science", grade: 85 },
    ];
    
    console.log(groupStudentsAndCalculateAverageGrades(students));
    // Should log an object with department names as keys and arrays of student
    
    ```
    
- code snippet 8
    
    Create a function **`groupProductsAndCalculateTotalPrices`** that takes an array of product objects, where each object contains a name, category, and price. Use the **`reduce`** method to group products by category and calculate the total price for each category. Return an object where the keys are category names, and the values are arrays of product names within each category and their total prices.
    
    ```jsx
    // Your code here
    
    const products = [
      { name: "Smartphone", category: "Electronics", price: 800 },
      { name: "Laptop", category: "Electronics", price: 1200 },
      { name: "Shirt", category: "Clothing", price: 25 },
      { name: "TV", category: "Electronics", price: 1000 },
    ];
    
    console.log(groupProductsAndCalculateTotalPrices(products));
    // Should log an object with category names as keys and arrays of product names and their total prices as values.
    
    ```
    
- code snippet 9
    
    Create a function **`filterBooksAndCreateReadingList`** that takes an array of book objects, where each object contains a title, author, and category. Use the **`filter`** method to filter books by a specific category, the **`map`** method to extract their titles, and the **`reduce`** method to create a reading list with categories as keys and arrays of book titles as values.
    
    ```jsx
    // Your code here
    
    const books = [
      { title: "Dune", author: "Frank Herbert", category: "Science Fiction" },
      { title: "To Kill a Mockingbird", author: "Harper Lee", category: "Fiction" },
      { title: "Neuromancer", author: "William Gibson", category: "Science Fiction" },
      { title: "Pride and Prejudice", author: "Jane Austen", category: "Fiction" },
    ];
    
    console.log(filterBooksAndCreateReadingList(books, "Science Fiction"));
    // Should log an object with a specific category as the key and an array of book titles in that category as the value.
    
    ```
    
- code snippet 10
    
    Create a function **`filterAndRankMoviesByGenre`** that takes an array of movie objects, where each object contains a title, genre, and rating. Use the **`filter`** method to filter movies by a specific genre, the **`map`** method to extract their titles, and the **`reduce`** method to rank them by rating. Return an array of movie titles ranked from highest to lowest rating.
    
    ```jsx
    // Your code here
    
    const movies = [
      { title: "Inception", genre: "Science Fiction", rating: 8.8 },
      { title: "The Godfather", genre: "Crime", rating: 9.2 },
      { title: "Interstellar", genre: "Science Fiction", rating: 8.6 },
      { title: "Pulp Fiction", genre: "Crime", rating: 8.9 },
    ];
    
    console.log(filterAndRankMoviesByGenre(movies, "Science Fiction"));
    // Should log an array of movie titles ranked by rating for a specific genre.
    
    ```
    

**CP Assignment Link:**

| JS-array-hoc-map-reduce | https://cp.masaischool.com/problems/1344/view#basicDetails | https://github.com/masai-problems/JS201-A3-array-reduce-map | Published |
| --- | --- | --- | --- |
| JS-Array-HOC | https://cp.masaischool.com/problems/534/view#basicDetails | https://github.com/masai-problems/JS201-b21-Array-HOC | Tested |
| JS201-S1-D4--array-hoc-methods | https://cp.masaischool.com/problems/1592/view#basicDetails | https://github.com/masai-problems/JS201-A4-array-hoc-methods | Published |