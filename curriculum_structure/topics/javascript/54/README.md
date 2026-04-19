# Student Tasks

### Type-coercion

- Code Snippet 1
  ```jsx
  let x = 5;
  let y = "10";

  let result = x + y;

  console.log(result);

  //Guess the Output: __________
  //510
  ```
- Code Snippet 2
  ```jsx
  let num = 10;
  let str = "5";

  let result = num - str;

  console.log(result);

  //Guess the Output: __________
  //5
  ```
- Code Snippet 3
  ```jsx
  let a = 2;
  let b = "3";

  let result = a * b;

  console.log(result);

  //Guess the Output: __________
  //6
  ```
- Code Snippet 4
  ```jsx
  let value1 = "8";
  let value2 = "4";

  let result = value1 > value2;

  console.log(result);

  //Guess the Output: __________
  //true
  ```
- Code Snippet 5
  ```jsx
  let name = "John";
  let age = 25;

  let result = name + age;

  console.log(result);

  //Guess the Output: __________
  //John25
  ```
- Code Snippet 6
  ```jsx
  let isStudent = true;
  let isTeacher = false;

  let result = isStudent + isTeacher;

  console.log(result);

  //Guess the Output: __________
  //1
  ```
- Code Snippet 7
  ```jsx
  let num = 10;
  let str = "abc";

  let result = num * str;

  console.log(result);

  //Guess the Output: __________
  //NaN
  ```
- Code Snippet 8
  ```jsx
  let value1 = "15";
  let value2 = 10;

  let result = value1 - value2;

  console.log(result);

  //Guess the Output: __________
  //5
  ```

### Stored by Value VS Stored by Reference

- Stored by Value
  ```jsx
  let a = 10;
  let b = a;

  b = 20;

  console.log(a);
  console.log(b);

  //Guess the Output for **a** and **b**: __________
  ```
- Stored by Reference - Array
  ```jsx
  let arr1 = [1, 2, 3];
  let arr2 = arr1;

  arr2.push(4);

  console.log(arr1);
  console.log(arr2);

  //Guess the Output for **`arr1`** and **`arr2`**: __________
  ```
- Stored by Reference - Object
  ```jsx
  let obj1 = { name: "Alice", age: 25 };
  let obj2 = obj1;

  obj2.age = 30;

  console.log(obj1.age);
  console.log(obj2.age);

  //Guess the Output for **obj1.age** and **obj2.age**: __________
  ```
- Stored by Value-Function Arguments
  ```jsx
  function modifyValue(value) {
    value = "Modified";
  }

  let originalValue = "Original";
  modifyValue(originalValue);

  console.log(originalValue);

  //Guess the Output for **originalValue**: __________
  ```
- Stored by Reference - Function Arguments
  ```jsx
  function modifyArray(arr) {
    arr.push(4);
  }

  let myArray = [1, 2, 3];
  modifyArray(myArray);

  console.log(myArray);

  //Guess the Output for myArray: __________
  ```

### Function scope VS Block scope

- Hoisting with `'var'`
  ```jsx
  javascriptCopy code
  function hoistingVar() {
    console.log(x);
    var x = 10;
  }

  hoistingVar();

  //Guess the Output: __________
  ```
- Block Scope with `'var'`
  ```jsx
  function blockScopeVar() {
    if (true) {
      var y = 20;
    }
    console.log(y);
  }

  blockScopeVar();

  //Guess the Output: __________
  ```
- Re-declaration with `'let'`
  ```jsx
  javascriptCopy code
  let z = 30;
  {
    let z = 40;
    console.log(z);
  }
  console.log(z);

  //Guess the Output: __________
  ```
- Function Scope with `'const'`
  ```jsx
  javascriptCopy code
  function functionScopeConst() {
    if (true) {
      const a = 50;
    }
    // console.log(a); // Uncomment this line to check the result
  }

  functionScopeConst();

  //
  ```
- Global Scope
  ```jsx
  javascriptCopy code
  const b = 60;

  function globalScope() {
    console.log(b);
  }

  globalScope();

  //Guess the Output: __________
  ```
- IIFE (Immediately Invoked Function Expression)
  ```jsx
  javascriptCopy code
  const c = 70;
  (function () {
    const c = 80;
    console.log(c);
  })();
  console.log(c);

  //Guess the Output: __________
  ```
- Block Scope and for-loop with `'let'`
  ```jsx
  javascriptCopy code
  function blockScopeLoopLet() {
    for (let i = 0; i < 3; i++) {
      setTimeout(function () {
        console.log(i);
      }, 100);
    }
  }

  blockScopeLoopLet();

  //Guess the Output: __________
  ```
- Block Scope and for-loop with `'var'`
  ```jsx
  javascriptCopy code
  function blockScopeLoopVar() {
    for (var j = 0; j < 3; j++) {
      setTimeout(function () {
        console.log(j);
      }, 100);
    }
  }

  blockScopeLoopVar();

  //Guess the Output: __________
  ```

### Destructuring

- Codepens
  [PT-Unit-5-S1-D1-Student task (codepen.io)](https://codepen.io/Adarsha-khatua/pen/dywyNyz?editors=0010)
- code snippet 1
  Using the provided **`data`** object and multilevel destructuring, extract the teacher counts for the departments "math," "science," and "economics." Store these counts in the following variables: **`mathTeacherCount`**, **`scienceTeacherCount`**, and **`economicsTeacherCount`**.
  ```jsx
  javascriptCopy code
  let data = {
    score: [
      { name: "Prakash", marks: 67 },
      { name: "santhi", marks: 78 },
      { name: "Tanisha", marks: 68 }
    ],
    department: ["math", "science", "arts", "economics", "computer science"],
    stat: [
      { sub: "math", student: 100, teacher: 10 },
      { sub: "science", student: 120, teacher: 12 },
      { sub: "economics", student: 90, teacher: 6 }
    ]
  }

  // Your code here

  console.log(mathTeacherCount); // Should log the teacher count for the "math" department.
  console.log(scienceTeacherCount); // Should log the teacher count for the "science" department.
  console.log(economicsTeacherCount); // Should log the teacher count for the "economics" department.

  ```
  **Note:** You should use destructuring to access the teacher counts directly from the **`data`** object and store them in the respective variables as specified.
- code snippet 2
  ### **Extract Student Count for "Arts"**
  **Data Object:**
  ```jsx
  javascriptCopy code
  let data2 = {
    department: ["math", "science", "arts", "economics", "computer science"],
    stat: [
      { sub: "math", student: 100, teacher: 10 },
      { sub: "science", student: 120, teacher: 12 },
      { sub: "arts", student: 80, teacher: 8 },
      { sub: "economics", student: 90, teacher: 6 },
      { sub: "computer science", student: 150, teacher: 15 }
    ]
  }

  // Your code here

  ```
- code snippet 3
  ### **Extract Student Names and Marks**
  **Data Object:**
  ```jsx
  javascriptCopy code
  let data3 = {
    score: [
      { name: "Alice", marks: 92 },
      { name: "Bob", marks: 85 },
      { name: "Charlie", marks: 78 }
    ]
  }

  // Your code here

  ```
- code snippet 4
  ### **Extract Subject Names**
  **Data Object:**
  ```jsx
  javascriptCopy code
  let data4 = {
    stat: [
      { sub: "math", student: 100, teacher: 10 },
      { sub: "science", student: 120, teacher: 12 },
      { sub: "economics", student: 90, teacher: 6 }
    ]
  }

  // Your code here

  ```
- code snippet 5
  ### **Extract All Teacher Counts**
  **Data Object:**
  ```jsx
  javascriptCopy code
  let data5 = {
    department: ["math", "science", "arts", "economics", "computer science"],
    stat: [
      { sub: "math", student: 100, teacher: 10 },
      { sub: "science", student: 120, teacher: 12 },
      { sub: "arts", student: 80, teacher: 8 },
      { sub: "economics", student: 90, teacher: 6 },
      { sub: "computer science", student: 150, teacher: 15 }
    ]
  }

  // Your code here

  ```
- code snippet 6
  ### **Extract Student and Teacher Counts for "Computer Science"**
  **Data Object:**
  ```jsx
  javascriptCopy code
  let data6 = {
    department: ["math", "science", "arts", "economics", "computer science"],
    stat: [
      { sub: "math", student: 100, teacher: 10 },
      { sub: "science", student: 120, teacher: 12 },
      { sub: "arts", student: 80, teacher: 8 },
      { sub: "economics", student: 90, teacher: 6 },
      { sub: "computer science", student: 150, teacher: 15 }
    ]
  }

  // Your code here

  ```
- code snippet 7
  ### **Extract Student Count for "Arts"**
  **Data Object:**
  ```jsx
  javascriptCopy code
  let data2 = {
    department: ["math", "science", "arts", "economics", "computer science"],
    stat: [
      { sub: "math", student: 100, teacher: 10 },
      { sub: "science", student: 120, teacher: 12 },
      { sub: "arts", student: 80, teacher: 8 },
      { sub: "economics", student: 90, teacher: 6 },
      { sub: "computer science", student: 150, teacher: 15 }
    ]
  }

  // Your code here

  ```
- code snippet 8
  ### **Extract Student Names and Marks**
  **Data Object:**
  ```jsx
  javascriptCopy code
  let data3 = {
    students: [
      { name: "Alice", grades: { math: 92, science: 87 } },
      { name: "Bob", grades: { math: 85, science: 88 } },
      { name: "Charlie", grades: { math: 78, science: 79 } }
    ]
  }

  // Your code here

  ```
- code snippet 9
  ### **Extract All Teacher Counts**
  **Data Object:**
  ```jsx
  javascriptCopy code
  let data5 = {
    departments: ["math", "science", "arts", "economics", "computer science"],
    departmentStats: {
      math: { students: 100, teacher: 10 },
      science: { students: 120, teacher: 12 },
      arts: { students: 80, teacher: 8 },
      economics: { students: 90, teacher: 6 },
      computerScience: { students: 150, teacher: 15 }
    }
  }

  // Your code here

  ```
- code snippet 10
  ### **Extract Student and Teacher Counts for "Computer Science"**
  **Data Object:**
  ```jsx
  javascriptCopy code
  let data6 = {
    departments: ["math", "science", "arts", "economics", "computer science"],
    departmentStats: {
      math: { students: 100, teacher: 10 },
      science: { students: 120, teacher: 12 },
      arts: { students: 80, teacher: 8 },
      economics: { students: 90, teacher: 6 },
      computerScience: { students: 150, teacher: 15 }
    }
  }

  // Your code here

  ```

### Spread operator

- code snippet 1
  Given two arrays, **`arr1`** and **`arr2`**, use the spread operator to create a new array, **`combinedArray`**, that contains all the elements from both **`arr1`** and **`arr2`**.
  ```jsx
  javascriptCopy code
  const arr1 = [1, 2, 3];
  const arr2 = [4, 5, 6];

  // Your code here

  console.log(combinedArray); // Should log [1, 2, 3, 4, 5, 6].

  ```
- code snippet 2
  Given an object **`originalObj`**, use the spread operator to create a new object, **`clonedObj`**, that is a deep clone of **`originalObj`**.
  ```jsx
  javascriptCopy code
  const originalObj = {
    name: "John",
    age: 30,
    address: {
      city: "New York",
      zip: "10001"
    }
  };

  // Your code here

  console.log(clonedObj); // Should log an object identical to originalObj.

  ```
- code snippet 3
  Practice using the spread operator to merge multiple objects.
  **Instructions:** Given three objects, **`obj1`**, **`obj2`**, and **`obj3`**, use the spread operator to merge them into a new object, **`mergedObj`**.
  ```jsx
  javascriptCopy code
  const obj1 = { a: 1, b: 2 };
  const obj2 = { c: 3, d: 4 };
  const obj3 = { e: 5, f: 6 };

  // Your code here

  console.log(mergedObj); // Should log an object containing all key-value pairs from obj1, obj2, and obj3.

  ```
- code snippet 4
  ### **Copy Array and Add Elements**
  **Objective:** Practice using the spread operator to copy an array and add elements.
  **Instructions:** Given an array **`originalArray`**, use the spread operator to create a new array, **`copiedArray`**, that is a copy of the original array, and then add a new element, **`7`**, to the end of the copied array.
  ```jsx
  javascriptCopy code
  const originalArray = [1, 2, 3, 4, 5];

  // Your code here

  console.log(copiedArray); // Should log [1, 2, 3, 4, 5, 7].

  ```
- code snippet 5
  ### **Extract and Reorder Array Elements**
  **Objective:** Practice using the spread operator to extract and reorder array elements.
  **Instructions:** Given an array **`sourceArray`**, use the spread operator to create a new array, **`reorderedArray`**, that contains elements in the order: 3rd, 1st, 2nd.
  ```jsx
  javascriptCopy code
  const sourceArray = [10, 20, 30];

  // Your code here

  console.log(reorderedArray); // Should log [30, 10, 20].

  ```
- code snippet 6
  Given an object **`user`**, use the spread operator to create a new object, **`userWithoutEmail`**, that omits the **`email`** property.
  ```jsx
  javascriptCopy code
  const user = {
    name: "Alice",
    email: "alice@example.com",
    age: 28
  };

  // Your code here

  console.log(userWithoutEmail); // Should log an object without the "email" property.

  ```
- code snippet 7
  Given two objects, **`defaultSettings`** and **`userSettings`**, merge them into a new object, **`mergedSettings`**. If a property exists in both objects, the value from **`userSettings`** should override the value from **`defaultSettings`**.
  ```jsx
  javascriptCopy code
  const defaultSettings = {
    theme: "light",
    fontSize: 14,
    showNotifications: true
  };

  const userSettings = {
    fontSize: 16,
    showNotifications: false
  };

  // Your code here

  console.log(mergedSettings); // Should log an object with merged and overridden properties.

  ```
- code snippet 8
  Given an array **`originalArray`**, use the spread operator to create a new array, **`modifiedArray`**, that is a copy of the original array, and then insert the elements **`7`** and **`8`** at the 2nd and 4th positions respectively.
  ```jsx
  javascriptCopy code
  const originalArray = [1, 2, 3, 4, 5];

  // Your code here

  console.log(modifiedArray); // Should log [1, 7, 2, 3, 8, 4, 5].

  ```
- code snippet 9
  Given an object **`originalObject`** with nested objects, use the spread operator to create a new object, **`clonedObject`**, that is a deep clone of the original object.
  ```jsx
  javascriptCopy code
  const originalObject = {
    name: "John",
    address: {
      street: "123 Main St",
      city: "New York"
    }
  };

  // Your code here

  console.log(clonedObject); // Should log a deep clone of the original object.

  ```
- code snippet 10
  Given an array **`originalArray`**, use the spread operator to create a new array, **`expandedArray`**, that includes the elements **`0`** at the beginning and **`6`** at the end.
  ```jsx
  javascriptCopy code
  const originalArray = [1, 2, 3, 4, 5];

  // Your code here

  console.log(expandedArray); // Should log [0, 1, 2, 3, 4, 5, 6].

  ```

### REST operator

- code snippet 1
  Create a function **`calculateSum`** that takes any number of arguments and uses the rest operator to calculate and return the sum of all the numbers passed as arguments.
  ```jsx
  // Your code here

  console.log(calculateSum(1, 2, 3, 4, 5)); // Should log 15.
  ```
- code snippet 2
  Create a function **`filterOddEven`** that takes any number of arguments and uses the rest operator to separate the odd and even numbers into two arrays, **`oddNumbers`** and **`evenNumbers`**. Return an object containing both arrays.
  ```jsx
  // Your code here

  console.log(filterOddEven(1, 2, 3, 4, 5, 6)); // Should log an object with oddNumbers and evenNumbers arrays.
  ```
- code snippet 3
  Create a function **`removeFirstElement`** that takes an array as an argument and uses the rest operator to return a new array with the first element removed.
  ```jsx
  // Your code here

  console.log(removeFirstElement([1, 2, 3, 4, 5])); // Should log [2, 3, 4, 5].
  ```
- code snippet 4
  Create a function **`mergeWithSeparator`** that takes a separator and any number of arrays as arguments. Use the rest operator to merge the arrays with the specified separator and return a single string.
  ```jsx
  // Your code here

  console.log(
    mergeWithSeparator(" | ", [1, 2, 3], ["A", "B", "C"], ["x", "y"])
  ); // Should log "1 | 2 | 3 | A | B | C | x | y".
  ```
- code snippet 5
  Create a function **`extractFirstLast`** that takes an array as an argument and uses the rest operator to return an array containing the first and last elements.
  ```jsx
  // Your code here

  console.log(extractFirstLast([1, 2, 3, 4, 5])); // Should log [1, 5].
  ```
- code snippet 6
  Create a function **`concatenateStrings`** that takes any number of strings as arguments and uses the rest operator to concatenate them into a single string. Return the concatenated string.
  ```jsx
  // Your code here

  console.log(concatenateStrings("Hello", " ", "world", "!")); // Should log "Hello world!".
  ```
- code snippet 7
  Create a function **`findLongestWord`** that takes any number of words as arguments and uses the rest operator to find and return the longest word.
  ```jsx
  // Your code here

  console.log(findLongestWord("apple", "banana", "strawberry", "blueberry")); // Should log "strawberry".
  ```
- code snippet 8
  Create a function **`capitalizeFirstLetters`** that takes a sentence as an argument and uses the rest operator to capitalize the first letter of each word in the sentence. Return the modified sentence.
  ```jsx
  // Your code here

  console.log(capitalizeFirstLetters("this is a test sentence.")); // Should log "This Is A Test Sentence."
  ```
- code snippet 9
  Create a function **`filterOddEvenLengthWords`** that takes any number of words as arguments and uses the rest operator to separate the words into two arrays: **`oddLengthWords`** and **`evenLengthWords`**. Words with odd and even lengths should be placed in their respective arrays. Return an object containing both arrays.// Your code here
  console.log(filterOddEvenLengthWords("apple", "banana", "cherry", "date", "fig")); // Should log an object with oddLengthWords and evenLengthWords arrays.
  ```jsx
  // Your code here

  console.log(
    filterOddEvenLengthWords("apple", "banana", "cherry", "date", "fig")
  ); // Should log an object with oddLengthWords and evenLengthWords arrays.
  ```
- code snippet 10
  Create a function **`combineArraysAndStrings`** that takes any number of strings and arrays as arguments and uses the rest operator to merge them into a single array. Return the combined array.
  ```jsx
  // Your code here

  console.log(combineArraysAndStrings("Hello", ["world", "!"], [1, 2, 3])); // Should log ["Hello", "world", "!", 1, 2, 3].
  ```

### Map

- code snippet 1
  Create a function **`calculateAverageGrades`** that takes an array of student objects, where each object contains the student's name and an array of their grades. Use the **`map`** function to calculate the average grade for each student and return a new array of objects with each student's name and their average grade.
  ```jsx
  const students = [
    { name: "Alice", grades: [90, 85, 88] },
    { name: "Bob", grades: [78, 92, 87] },
    { name: "Charlie", grades: [85, 89, 92] },
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
    { name: "Charlie", grade: "A" },
  ];

  console.log(filterStudentsByGrade(students)); // Should log an array of students with grade "A."
  ```
- code snippet 5
  Create a function **`filterEvenLengthWords`** that takes an array of words as an argument and uses the **`filter`** method to return a new array containing only the words with even lengths.
  ```jsx
  // Your code here

  console.log(
    filterEvenLengthWords(["apple", "banana", "cherry", "date", "fig"])
  ); // Should log an array of words with even lengths.
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
    { name: "Charlie", age: 26 },
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
    { title: "Neuromancer", genre: "Science Fiction" },
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

  console.log(
    countWordOccurrences([
      "Hello world!",
      "This is a world of wonders.",
      "Hello, world!",
    ])
  ); // Should log an object with word counts.
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
    "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
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
    {
      category: "Technology",
      content: "JavaScript is a programming language used for web development.",
    },
    {
      category: "Travel",
      content: "Exploring new places and experiencing different cultures.",
    },
    {
      category: "Technology",
      content:
        "Web development requires knowledge of HTML, CSS, and JavaScript.",
    },
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
    {
      title: "To Kill a Mockingbird",
      author: "Harper Lee",
      category: "Fiction",
    },
    {
      title: "Neuromancer",
      author: "William Gibson",
      category: "Science Fiction",
    },
    {
      title: "Pride and Prejudice",
      author: "Jane Austen",
      category: "Fiction",
    },
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

[assignment](<Student%20Tasks%20(1)%20d6836b0a7ca24a6a9e43a5ecbac23c5f/assignment%20b478a0f5f7204d09a0d619fed0ff045f.md>)

### Object creation using the Factory function

[assignment](<Student%20Tasks%20(1)%20d6836b0a7ca24a6a9e43a5ecbac23c5f/assignment%2042c9cdb4554b499bbb65ccf2a6ea9f4f.md>)

### Prototypical inheritance using a Factory function

[assignment](<Student%20Tasks%20(1)%20d6836b0a7ca24a6a9e43a5ecbac23c5f/assignment%20606714558f1f416abf7dfb4bb9b3d0ef.md>)

### Prototypical inheritance using the Constructor function

[assignment](<Student%20Tasks%20(1)%20d6836b0a7ca24a6a9e43a5ecbac23c5f/assignment%20d21de9d5a4d44d8aa816260b4e558664.md>)

### Prototypical inheritance using the ES6 class

[assignment](<Student%20Tasks%20(1)%20d6836b0a7ca24a6a9e43a5ecbac23c5f/assignment%20309e2e60c0e3418c9084992aa504c47e.md>)

### Mastering this keyword

[assignment](<Student%20Tasks%20(1)%20d6836b0a7ca24a6a9e43a5ecbac23c5f/assignment%2051ab788ad281454eb2517f10a69ff081.md>)

### Asynchronous JS - callback

[assignment](<Student%20Tasks%20(1)%20d6836b0a7ca24a6a9e43a5ecbac23c5f/assignment%20c9ae6f5b51524b5b827c6bf8102eb64e.md>)

### Asynchronous JS - Promises

[assignment](<Student%20Tasks%20(1)%20d6836b0a7ca24a6a9e43a5ecbac23c5f/assignment%20abbd9bd87040400298b8b75b82247a8c.md>)
