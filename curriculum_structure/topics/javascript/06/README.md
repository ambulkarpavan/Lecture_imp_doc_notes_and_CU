# Dynamic Typing [15 min] (1)

JS is a dynamically typed language. a dynamically typed language is a programming language in which the type of a variable is determined at runtime, not at compile time. 

In dynamic type languages, you can change the type of a variable during the program's execution. This is in contrast to statically typed languages where variable types are explicitly declared and checked at compile time.

```jsx
var x = 5; // x is now of type number
x = "Hello, World!"; // x is now of type string
x = [1, 2, 3]; // x is now an array
```

## Type coercion:

as JS is a dynamic type language it can convert one primitive data type to another primitive data type based on requirements. This implicit conversion of datatypes is known as type coercion. 

[https://www.canva.com/design/DAFyEN6oEOw/D65VxCvfMUaQfypVHgEotw/edit?utm_content=DAFyEN6oEOw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton](https://www.canva.com/design/DAFyEN6oEOw/D65VxCvfMUaQfypVHgEotw/edit?utm_content=DAFyEN6oEOw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

### Student task

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