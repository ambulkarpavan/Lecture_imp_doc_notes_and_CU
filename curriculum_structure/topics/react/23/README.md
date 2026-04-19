# Pure/impure functions and side effects

Serial: 24
Made for: Beginner
Requirement: Must Have
Time in minutes: 25
Learning Objectives: effects and useEffect
doc-id: react-24

## Introduction :

The concepts of pure and impure functions, along with side effects, are very crucial for writing clean, maintainable, and predictable code. This lesson delves into what pure and impure functions are, explores the notion of side effects. 

## Detailed Explanation :

### Pure Functions :

1. **Definition**: A pure function is a function that, given the same input, will always return the same output and does not cause any observable side effects.
2. **Characteristics**:
    - **Deterministic**: For the same set of inputs, the function always produces the same output.
    - **No Side Effects**: The function doesn't alter any external state (e.g., global variables, I/O operations ).

### Impure Functions :

1. **Definition**: An impure function is one that may produce different outputs for the same input or causes side effects.
2. **Characteristics**:
    - **Non-Deterministic**: The output might vary even with the same inputs.
    - **Side Effects**: The function may modify some external state or depend on external variables.

### Side Effects :

- **Meaning**: A side effect is any application state change that is observable outside the called function other than its return value. Common side effects include modifying a global variable, writing to a database, or altering the DOM in a web page.
- **Implications**: While not inherently bad, side effects, if not managed well, can lead to issues like hard-to-track bugs and difficulties in understanding and maintaining code.

## Use-Case & Benefits :

- **Predictability**: Pure functions increase predictability in code. This makes it easier to debug and test functions.
- **Reusability**: Pure functions, by virtue of not depending on the external state, are more reusable across different parts of an application.
- **Concurrency**: Pure functions facilitate concurrent programming by avoiding issues like race conditions since they don’t alter external state.

## Real World Examples :

1. **Pure Function Example in JavaScript**:
    
    ```jsx
    function sum(a, b) {
      return a + b;
    }
    ```
    
    Here, `sum` is pure because it always returns the same result with the same inputs and does not modify any external state.
    
2. **Impure Function Example in JavaScript**:
    
    ```jsx
    let count = 0;
    function incrementCount() {
      count += 1;
      return count;
    }
    ```
    
    `incrementCount` is impure as it modifies the external variable `count`.
    

## Usage

- **In Web Development**: When developing web applications, especially with frameworks like React, understanding pure and impure functions is crucial. For instance, in React, components should ideally represent pure functions with respect to their props for predictable rendering behavior. We will discuss it in detailed fashion
- **Best Practices**: Aim to use pure functions whenever possible. When impure functions are necessary (e.g., for I/O operations), clearly isolate and manage them to minimize unintended side effects.

## Instructor Activity

- **Demonstration**: Show examples of pure and impure functions. Demonstrate how impure functions can lead to unpredictable behaviors.
- **Discussion**: Engage in a discussion on how pure functions can simplify unit testing and why functional programming paradigms value immutability and pure functions.

## Learners Activity

- **Exercises**:
    1. Write a pure function to calculate the area of a square.
    2. Modify an existing impure function to make it pure.
    3. Identify the side effects in a given piece of code.
- **Project**: Develop a small application or a component in React where the emphasis is on using pure functions and managing side effects effectively.

## Conclusion

Understanding pure and impure functions and the concept of side effects has practical implications, especially in React. Embracing these concepts leads to more robust, maintainable, and predictable code. Remember, the aim is not to avoid impure functions and side effects altogether but to understand and manage them effectively.