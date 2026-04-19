# ES6 [60 min] (1)

## Rest and Spread

[MDN- rest](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)

[MDN - spread](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

```jsx
// rest operator helps collect all the arguments in an array
function doSomething(first, second, ...rest) {
  console.log(first, second, rest); // rest is guaranteed to be an array
}

doSomething('one', 'two', 'three', 'four', 'five');
```

```jsx
// The spread operator explodes the array or objects in place
let arr = [1, 3, 5, 7, 9];
console.log(...arr); //-> 1 3 5 7 9

let user = {
  firstName: 'Vivek',
  lastName: 'Agarwal'
}

console.log({
  ...user,
  fullName: `${user.firstName} ${user.lastName}`
});
//-> {firstName: 'Vivek', lastName: 'Agarwal', fullName: 'Vivek Agarwal'}
```

## Destructuring Arrays and Objects

[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)

```jsx
const arr = [1, 3, 5, 7, 9];

const [first, second, ...rest] = arr;
console.log(first, second, rest);
```

```jsx
let user = {
  firstName: 'Vivek',
  lastName: 'Agarwal',
  age: 38,
  posts: [
    {title: 'Post 1', comments: 10},
    {title: 'Post 2', comments: 11}
  ]
}

const { firstName:first, lastName, age=40, ...rest } = user;
console.log(first, lastName, age, rest);

// only the deepest keys become variables
const { posts: [{ title }, {title: t2}] } = user;
console.log(title, t2);
```

```jsx
// a function that returns an array of a number and a function
function useState(num) {
  let count = num;
  let setCount = function () {
    console.log(`setting the count: ${count}`);
  }

  return [count, setCount]
}

// way 1
let resultArr = useState(20);
let resultCount = resultArr[0];
let resultSetFunction = resultArr[1];

resultSetFunction(); //-> setting the count: 20

// the destructuring way, super neat
let [count, setCount] = useState(30);

setCount(); //-> setting the count: 30
```

```jsx
// we know that the function will receive an object with keys firstName & lastName

function printFullName({ firstName, lastName }) {
  console.log(`${firstName} ${lastName}`);
}

printFullName({
  firstName: 'Vivek',
  lastName: 'Agarwal'
})

//-> Vivek Agarwal
```

```jsx
const user = {
  id: 339,
  name: 'John',
  age: 42,
  education: {
    degree: 'Masters'
  }
};

const  { name, education: {degree}}  = user;
```

```jsx
const user = {
  id: 339,
  name: 'John',
  age: 42,
  education: {
    degree: {
      name: 'BCA'
    }
  }
};

const {name:fname, education: {degree: {name:degreeName}}} = user;
```

```jsx
const user = {
  id: 339,
  name: 'John',
  age: 42,
  subjects: ['HTML', 'CSS', 'Javascript'],
  education: {
    degree: {
      name: 'BCA'
    }
  }
};

const {
  name:fname, 
  education: {degree: {name:degreeName}},
  subjects: [sub1,,sub3]
} = user;
```

## Object shorthand

If the name of the key matches the name of the variable that's going into that key, you can get rid of the value and just use the variable name

```jsx
const userData = (name, email) => ({
  name,
  email
})
```

## Arrow functions

[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

```jsx
// Regular function
function greet(greeting, name) {
  return `${greeting}, from ${name}`;
}

// Arrow function
let newGreet = (greeting, name) => {
  return `${greeting}, from ${name}`;
}
```

implicit return: If all you have is a single expression that returns a value, you can get rid of the braces and the return keyword. Its a very common usage.

```jsx
let newGreet = (greeting, name) => `${greeting}, from ${name}`
```

**Edge case:** To implicitly return an object, surround it with parentheses.

## Default Parameter in function:

```jsx

function Human(name,age,salary=500000){
	
	let obj ={
		name: name,
		age: age,
		salary: salary,
	}
return obj;
}
//here if we do not pass salary it will take 500000 as the default value
Human("Ankur", 25) 
//output is {name: "ankur", age: 25, salary:500000}
Human("Ankur", 25, 800000) 
//output is {name: "ankur", age: 25, salary:800000}
```

### Student Task

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
    
    console.log(mergeWithSeparator(" | ", [1, 2, 3], ["A", "B", "C"], ["x", "y"])); // Should log "1 | 2 | 3 | A | B | C | x | y".
    
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
    
    console.log(filterOddEvenLengthWords("apple", "banana", "cherry", "date", "fig")); // Should log an object with oddLengthWords and evenLengthWords arrays.
    ```
    
- code snippet 10
    
    Create a function **`combineArraysAndStrings`** that takes any number of strings and arrays as arguments and uses the rest operator to merge them into a single array. Return the combined array.
    
    ```jsx
    // Your code here
    
    console.log(combineArraysAndStrings("Hello", ["world", "!"], [1, 2, 3])); // Should log ["Hello", "world", "!", 1, 2, 3].
    
    ```