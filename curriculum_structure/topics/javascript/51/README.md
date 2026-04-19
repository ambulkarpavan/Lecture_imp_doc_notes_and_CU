# Function Currying [60 min] (1)

### **WHAT IS CURRYING IN JAVASCRIPT?**

Currying in JavaScript transforms a function with multiple arguments into a nested series of functions, each taking a single argument. Currying helps you avoid passing the same variable multiple times, and it helps you create a higher-order function.

**Note:** An American mathematician named **Haskell Curry** developed this technique, that’s why it is called currying.

### **Why is currying useful in JavaScript?**

- It helps us to avoid passing the same variable multiple times.
- It helps us to create a higher-order function.
- It is very useful in building modular and reusable code.
- It makes the code more readable.
- It reduces the chances of error in our function by dividing it into multiple smaller functions that can handle one responsibility.

### Problem 1.

- a function `a` returns function `b`
- the function `b` returns function `c`
- the function `c` returns a string `hello world`

how would you invoke the function `c` from the global scope?

```jsx
function a() {
    return function b() {
        return function c() {
            return 'hello world';
        }
    }
}

//
```

### Problem 2.

What will the following code return & Why: 

```jsx
function a() {
    let A = 'hello';
    return function b() {
        let B = 'world';
        return function c() {
            let C = 'from Vivek'
            return `${A} ${B} ${C}`
        }
    }
}

a()()();
```

1. “undefined undefined undefined”
2. “undefined undefined from Vivek”
3. “hello world from Vivek”

### Problem 3.

What will the following code return & why:

```jsx
function a(A) {
    return function b(B) {
        return function c(C) {
            return `${A} ${B} ${C}`
        }
    }
}

a('hello')('world')('from Vivek');
```

### Problem 4.

What will the following code return;

```jsx
function a(A) {
    return function b(B) {
        return function c(C) {
            return `${A} ${B} ${C}`
        }
    }
}

a('hello');
a('hello')('world');
```

### Problem 5.

Convert the following function into a currying function

```jsx
function a(A,B,C) {
    return A+B+C;
}

a(2,3,4) // should output 9
```

- solution
    
    ```jsx
    function a(A) {
        return function b(B) {
            return function c(C) {
                return A + B + C;
            }
        }
    }
    
    a(2)(3)(4); //> 9
    ```
    

codepen problem: [https://codepen.io/drupalastic/pen/gOjWQXO?editors=0012](https://codepen.io/drupalastic/pen/gOjWQXO?editors=0012) 

 

Optional: Re-implement it using arrow function:

- Solution
    
    ```jsx
    let a = (A) => (B) => (C) => A+B+C;
    
    a(2)(3)(4); //> 9
    ```
    

### Problem 6.

Implement a currying function called `a`. Using `a` you should be able to create as many specific functions as you want as following: 

```jsx
let sumWith5 = a(5);
let sumWith3 = a(3);

sumWith5(2) // 7
sumWith3(2) // 5
```

- Breaking problem statement into smaller problems (thinking before inking)
    
    ![Untitled](Function%20Currying%20%5B60%20min%5D%20(1)%20a767919349dd4d50bdc5b08bcfb453c0/Untitled.png)
    
- Solution
    
    ```jsx
    function a(A) {
        return function a(B) {
            return A + B;
        }
    }
    ```
    

### Problem 7.

Explain the advantages of currying?

- Reusability
- It helps in avoiding the same variable again and again.
- It divides one function into multiple functions so that one handles one set of responsibilities. Easy debugging
- Detailed explanation
    
    Currying is a functional programming technique that involves transforming a function that takes multiple arguments into a series of functions that take a single argument. In JavaScript, the currying pattern can offer several benefits:
    
    **Partial function application:** Currying allows you to create a function that takes a subset of the original function's arguments and returns a new function that takes the remaining arguments. This can be useful for creating reusable functions that are tailored to specific use cases. For example:
    
    ```jsx
    function add(x) {
      return function(y) {
        return x + y;
      };
    }
    
    const addFive = add(5);
    console.log(addFive(3)); // 8
    console.log(addFive(7)); // 12
    ```
    
    In this example, **`add`** is a curried function that takes a single argument **`x`**
    and returns a new function that takes a single argument **`y`**. **`addFive`**
    is a partially applied function that takes **`y`**and returns **`x + y`**.
    
    **Composition:** Curried functions can be easily composed with other functions to create more complex functions. This can make it easier to reason about the behavior of a program and to separate concerns. For example:
    
    ```jsx
    function add(x) {
      return function(y) {
        return x + y;
      };
    }
    
    function multiply(x) {
      return function(y) {
        return x * y;
      };
    }
    
    const addFiveAndMultiplyByTen = (x) => multiply(10)(add(5)(x));
    console.log(addFiveAndMultiplyByTen(2)); // 70
    console.log(addFiveAndMultiplyByTen(4)); // 90
    ```
    
    In this example, **`addFiveAndMultiplyByTen`** is a function that first adds 5 to its argument and then multiplies the result by 10.
    
    **Easy to create variations:** Curried functions can be easily extended to create variations with different behavior. For example:
    
    ```jsx
    function add(x) {
      return function(y) {
        return x + y;
      };
    }
    
    const addOne = add(1);
    
    // create a subtract function based on add function
    function subtract(x) {
      return function(y) {
        return add(-x)(y);
      };
    }
    
    console.log(subtract(5)(3)); // 2
    
    ```
    
    In this example, the **`subtract`** function is created by extending the **`add`** function with a negated value of **`x`**. This is possible because **`add`** is a curried function that returns a function.
    
    **Flexibility in argument order:** Curried functions make it easy to change the order of arguments, which can be useful in some situations. For example:
    
    ```jsx
    function log(level) {
      return function(tag) {
        return function(message) {
          console.log(`[${level}] [${tag}] ${message}`);
        };
      };
    }
    
    const infoLog = log("INFO");
    const debugLog = log("DEBUG");
    
    infoLog("server")("starting"); // [INFO] [server] starting
    debugLog("database")("query"); // [DEBUG] [database] query
    ```
    
    In this example, the **`log`** function takes three arguments: **`level`**, **`tag`**, and **`message`**. By currying the function, we can create separate functions for different levels of logging and easily change the order of the arguments.
    

### Problem 8.

Implement a currying function `evaluate` such that they can be used as following:

```jsx
evaluate("mul")(3)(4); //> 12
```

- Thinking before inking
    
    ```jsx
    evaluate is function
    evaluate takes in an arg `operation` of type string
    evaluate returns a function
    
    it takes in an argument `a` of type number
    it returns a function
    
    it takes in an argument `b` of type number
    it returns a number (a value)
    calulation / operation happen here
    we may need `a`, `b`, `operation` all args here
    
    depending on `operation`, performs some calculation between `a` & `b` 
    and returns a number
    ```
    
- solution
    
    ```jsx
    function evaluate(operation) {
        return function (a) {
            return function (b) {
                if (operation == "sum") return a + b;
                if (operation == "mul") return a * b;
                if (operation == "div") return a / b;
                if (operation == "sub") return a - b;
                else return "Invalid operation";
            }
        }
    }
    ```
    
- additional use case
    
    ```jsx
     function evaluate(operation) {
        return function (a) {
            return function (b) {
                if (operation == "sum") return a + b;
                if (operation == "mul") return a * b;
                if (operation == "div") return a / b;
                if (operation == "sub") return a - b;
                else return "Invalid operation";
            }
        }
    }
    
    // evaluate("mul")(3)(4); //> 12
    
    let mul = evaluate("mul");
    mul(3)(4); //> 12
    ```
    

### Problem 9.

Implement infinite currying → `sum(1)(4)(2)....()`

Step 1.

```jsx
function sum (a) {
    return function (b) {
        return function () {
            return a + b;
        }
    }
}

sum(2)(3)(); //> 5
```

Step 2. (concept not code)

```jsx
sum(1)(3)(2)(1)() //> 7

sum(a=1) -> f(b=3)
	sum(a=4) -> f(b=2)
		sum(a=6) -> f(b=1)
			sum(a=7) -> f(b=undefined)
				if b==undefined return a
```

Final solution: 

```jsx
function sum(a) {
    return function (b) {
        if (b) return sum(a + b);
        return a;
    }
}

sum(1)(3)(2)(1)(); //> 7
```

Note: For recursive solutions, most of times, its best to write code first and then step through it

- step through
    
    ```jsx
    sum(1)(3)(2)(1)(); //> 7
    
    function sum(a) { // a = 1
        return function (b) { // b = 3
            if (b) return sum(a + b);
            return a;
        }
    }
    
    function sum(a) { // a = 4
        return function (b) { // b = 2
            if (b) return sum(a + b);
            return a;
        }
    }
    
    function sum(a) { // a = 6
        return function (b) { // b = 1
            if (b) return sum(a + b);
            return a;
        }
    }
    
    function sum(a) { // a = 7
        return function (b) { // b = undefined
            if (b) return sum(a + b);
            return a;
        }
    }
    
    sum(1)(3)(2)(1)(); //> 7
    ```