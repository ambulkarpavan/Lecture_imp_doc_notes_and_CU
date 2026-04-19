# Data Type in JS [10 min] (1)

### What types of values can be assigned to variables?

[MDN- primitive](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)

**Primitives (value types)**

string

number

boolean

undefined

null

bigInt

symbol

**Non Primitives (reference types)**

object

array

function

![Untitled](Data%20Type%20in%20JS%20%5B10%20min%5D%20(1)%200b8ce8e5d76a433facc5417c2dcb56bf/Untitled.png)

- Strings
    
    The first type of data is a String. This is used to store a sequence of characters
    used to represent text.
    Example:
    
    ```jsx
    var name = "Masai School";  //using double quotes
    var subject = 'Coding';     // using single quotes
    var val =`Hi`;              //  using template literal
    ```
    
    Any data within  " " ( Double quotes) or  ' ' (Single quotes) or ` ` (Template literal) is a String in JavaScript.
    
- Numbers
    
    The second type of data we want to know is a Number, which is used to store any kind
    of numbers. We have already seen this type of data in the variables example. Numbers
    can store both Whole Numbers/Integers and Decimals.
    Example:
    
    ```jsx
    var num = 100
    var dec = 100.001
    ```
    
- Booleans
    
    This data type has only two values true and false.
    Example:
    
    ```jsx
    var x = true
    var y = false
    ```
    

### Checking the type of data:

Let's say you have some data but you don't know what type it
is. You can use the **typeof()** inbuilt code to find the type of the data.

Example:

```jsx
var name = "Masai School"
console.log(typeof(name)) //output => string
```