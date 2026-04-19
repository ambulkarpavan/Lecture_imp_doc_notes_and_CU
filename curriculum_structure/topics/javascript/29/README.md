# JS Execution context [60 min] (1)

## How JS executes code:

execution context, execution stack

## Stack:

Stack is an abstract data structure that follows LIFO (last in first out) principle; that means if we want to remove one element, the lastly added element will be removed first.

![Untitled](JS%20Execution%20context%20%5B60%20min%5D%20(1)%20bdcfa8a53c304187bf389ff320821dd4/Untitled.png)

# **JavaScript Execution of Synchronous Code**

## **Execution Phases**

JavaScript code execution occurs in two main phases:

### **1. Creation/Memory Phase**

- During this phase, JavaScript sets up the environment for code execution.
- Variables and functions are "hoisted" - memory space is allocated for them.
- Variable and function declarations are moved to the top of their respective scopes.
- The global object is created, and **`this`** is determined in the global context.

### **2. Execution Phase**

- In this phase, the code is actually executed.
- Execution starts from the top of the script or the function and proceeds line by line.
- Variables are assigned values, functions are called, and expressions are evaluated.

## **Execution Stack**

- JavaScript uses a data structure known as the "call stack" to manage the execution of code.
- It keeps track of the order in which functions are called and their respective execution contexts.

## **Global Execution Context**

- The global execution context is the top-level context for your code.
- It represents the environment in which your entire script is executed.
- It includes the global object (e.g., **`window`** in a web browser), and **`this`** refers to it.
- Variables and functions declared in the global scope are accessible globally.

## **Function Execution Context**

- When a function is invoked, a new execution context is created for that function.
- This execution context includes its own set of variables and a reference to the outer (enclosing) execution context.
- The function's parameters and local variables are stored within this context.
- When the function returns, its execution context is popped off the call stack.

### **Execution Context Creation**

1. **Creation Phase**:
    - The function's parameters and variables are allocated memory.
    - Variables are hoisted within the function's scope.
2. **Execution Phase**:
    - The function's code is executed.

### **Call Stack**

- As functions are called, their execution contexts are pushed onto the call stack.
- The function at the top of the stack is the one currently being executed.
- When a function completes, its context is removed from the stack, and control returns to the calling function.

## **Example**

```jsx
javascriptCopy code
var globalVar = 'I am global';

function exampleFunction() {
  var localVar = 'I am local';
  console.log(globalVar);
}

exampleFunction();

```

- **Global Execution Context**:
    - **`globalVar`** is declared in the global context.
    - **`exampleFunction`** is declared in the global context.
    - Execution starts with calling **`exampleFunction()`**.
- **Function Execution Context for `exampleFunction`**:
    - **`localVar`** is declared within this context.
    - The **`console.log(globalVar)`** statement is executed.
- **Call Stack**:
    - Initially, the global execution context is on the stack.
    - When **`exampleFunction()`** is called, its execution context is pushed onto the stack.
    - After **`exampleFunction()`** completes, its execution context is popped off the stack.

## Resources:

Slide: [https://docs.google.com/presentation/d/15S6aj3Jn5N8dlWRHscc3w3fASUCoCf7FxP18g6tX8Wg/edit?usp=sharing](https://docs.google.com/presentation/d/15S6aj3Jn5N8dlWRHscc3w3fASUCoCf7FxP18g6tX8Wg/edit?usp=sharing)

[JS-the-execution-context.pptx](JS%20Execution%20context%20%5B60%20min%5D%20(1)%20bdcfa8a53c304187bf389ff320821dd4/JS-the-execution-context.pptx)

[JS-the-execution-context.pdf](JS%20Execution%20context%20%5B60%20min%5D%20(1)%20bdcfa8a53c304187bf389ff320821dd4/JS-the-execution-context.pdf)