# Typescript - Enums, Tuples, Generic Functions, Interfaces, and Classes

### Introduction

TypeScript extends JavaScript by adding types to the language. It speeds up your development by catching errors and providing fixes before you even run your code. TypeScript’s type system allows you to define complex, reusable types. In this lesson, we'll delve into some of the advanced types and features TypeScript offers, like Enums, Tuples, Generic Functions, Interfaces, and Classes.

### Detailed Explanation

### 1. Enums

Enums are a way to organize a collection of related values. They can be numeric or string-based.

### Numeric Enums

- Automatically incrementing. If you set the first value, TypeScript will increment the rest automatically.
    
    ```tsx
    enum Direction {
      Up = 1,
      Down,
      Left,
      Right,
    }
    
    ```
    
- If you don't initialize any value, TypeScript will set them starting from 0.
    
    ```tsx
    enum Direction {
      Up,
      Down,
      Left,
      Right,
    }
    
    ```
    

### String Enums

- Each value must be a string literal, or another string enum.
    
    ```tsx
    enum Direction {
      Up = "UP",
      Down = "DOWN",
      Left = "LEFT",
      Right = "RIGHT",
    }
    
    ```
    

### 2. Tuple

Tuples are like arrays but with a fixed number of elements whose types are known at compile time.

```tsx
let tuple: [number, string, boolean] = [7, "hello", true];

```

### 3. Generic Functions

Generic functions allow you to write a function that can work with any data type.

- Define a generic function with `<Type>` syntax.
    
    ```tsx
    function getIdentity<Type>(arg: Type): Type{
        return arg;
    }
    
    ```
    
- Examples of using generic functions:
    
    ```tsx
    getIdentity<number>(1);
    getIdentity<string>("Masai");
    
    ```
    

### 4. Interface

Interfaces define a contract for classes and objects, ensuring they adhere to a specific structure.

```tsx
interface Person {
  id: number;
  firstName: string;
  lastName: string;
}

```

### 5. Classes

TypeScript supports object-oriented programming features like classes, which are a blueprint for creating objects.

- Define a class with the `class` keyword.
    
    ```tsx
    class Car {
        name: string;
        constructor(name: string) {
            this.name = name;
        }
    }
    
    ```
    
- Classes can inherit from other classes, sharing or overriding properties and methods.
    
    ```tsx
    class Safari extends Car {
        // additional properties and constructor
    }
    
    ```
    

### Use-case & Benefits

- **Enums** provide a clear, defined set of values which can make your code more readable and less error-prone.
- **Tuples** are useful when you want to return multiple values from a function or when you want to ensure your array always has a specific structure.
- **Generic Functions** are great for creating reusable and flexible functions that work with any data type.
- **Interfaces** help in defining the structure of objects, making your code more predictable and easier to understand.
- **Classes** offer a way to encapsulate and organize your code, promoting reusability and maintainability.

### Real World Examples

- **Enums** can be used to define sets of named constants, like directions, days of the week, or specific states of a process.
- **Tuples** might be used to return a status code and message from a function, like `[200, "OK"]`.
- **Generic Functions** could be used in a sorting algorithm where the function can sort numbers, strings, or any other type.
- **Interfaces** might be used to define the structure of a user object in an authentication system.
- **Classes** can represent models in an application, like a `User` class in a social network app.

### Usage

- Enums are declared with `enum` keyword.
- Tuples are declared with square brackets and have a fixed number of elements.
- Generic Functions are declared with a generic type `<Type>` and used with specific types.
- Interfaces are declared with `interface` keyword and can extend other interfaces.
- Classes are declared with `class` keyword and can implement interfaces and extend other classes.

### Instructor Activity with Code Examples

The instructor should demonstrate each concept with the examples provided, showing how to define and use Enums, Tuples, Generic Functions, Interfaces, and Classes in TypeScript.

### Learner Activity

1. **Enums**: Define an enum for vehicle types (Car, Truck, Motorcycle, etc.).
2. **Tuples**: Create a tuple type for a database record (id as number, name as string, isActive as boolean).
3. **Generic Functions**: Write a generic function to return the last element in an array.
4. **Interfaces**: Define an interface for a `Vehicle` with properties `make`, `model`, and `year`.
5. **Classes**: Create a class `Bike` that extends the `Vehicle` class and adds a `type` property.

### Learner Activity Solution

1. **Enums**:
    
    ```tsx
    enum VehicleType {
        Car,
        Truck,
        Motorcycle
    }
    
    ```
    
2. **Tuples**:
    
    ```tsx
    let dbRecord: [number, string, boolean] = [1, "John Doe", true];
    
    ```
    
3. **Generic Functions**:
    
    ```tsx
    function getLastElement<T>(arr: T[]): T {
        return arr[arr.length - 1];
    }
    
    ```
    
4. **Interfaces**:
    
    ```tsx
    interface Vehicle {
        make: string;
        model: string;
        year: number;
    }
    
    ```
    
5. **Classes**:
    
    ```tsx
    class Bike extends Vehicle {
        type: string;
        constructor(make: string, model: string, year: number, type: string) {
            super(make, model, year);
            this.type = type;
        }
    }
    
    ```
    

This lesson provides a comprehensive understanding of advanced TypeScript concepts, empowering learners to write more robust, maintainable, and scalable code.