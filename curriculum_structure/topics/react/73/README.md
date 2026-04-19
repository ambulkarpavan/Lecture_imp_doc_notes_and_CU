# Typescript Introduction

### TypeScript: A Statically Typed Superset of JavaScript

TypeScript is a statically-typed language that compiles down to JavaScript. It provides type safety at compile-time, addressing the loose typing behavior of JavaScript.

### Why TypeScript?

1. **Catches Errors Early**: By knowing the types at compile-time, TypeScript can catch errors before the code is executed.
2. **Enhances Code Quality**: TypeScript's type system leads to more predictable and maintainable code.
3. **JavaScript Compatibility**: TypeScript is a superset of JavaScript, meaning any valid JavaScript code is also valid TypeScript code.

### Detailed Explanation

1. **Creating the Project**
    - Initialize a new Node.js project by running `npm init -y`. This command creates a `package.json` file with default values.
2. **Installing TypeScript**
    - Install TypeScript globally using the command `npm install typescript -g`. This allows you to use the TypeScript compiler in any project.
    - Verify the installation by using `tsc -v` (to check the TypeScript version) and `npm list -g` (to see all globally installed packages).
3. **Creating the TypeScript Configuration File**
    - To create a **`tsconfig.json`** file, navigate to your project's root directory in the terminal and run:
    
    ```jsx
    tsc --init # This command will generate a tsconfig.json file with default settings in your project's root directory. The generated file will include a set of default configurations that you can then customize based on your project's needs.
    ```
    
    `tsconfig.json`
    
    ```json
    {
        "include": ["src"],
        "exclude": ["node_modules"],
        "compilerOptions": {
            "module": "commonjs",
            "outDir": "build",
            "target": "es2017",
            "declaration": true,
            "sourceMap": true
        }
    }
    ```
    
    - The `include` key tells TypeScript to compile the `.ts` files inside the `src` folder.
    - The `compilerOptions` provide various settings that instruct the compiler how to compile the project.
4. **Updating the `package.json`**
    - Inside `package.json`, add a script to build your TypeScript project. This script uses the TypeScript compiler (`tsc`) to compile your project and watch for changes.
        
        ```json
        "scripts": {
            "build": "tsc --watch"
        }
        
        ```
        
5. **Creating Source Files**
    - Create a `src` folder to hold your TypeScript (`.ts`) files. Inside `src`, create an `index.ts` file as your entry point.
6. **Building the Project**
    - Run `npm run build` to start the TypeScript compiler in watch mode. It compiles your `.ts` files into `.js` files in the `build` directory and watches for any changes in your TypeScript files to recompile.
7. **Final Project Structure :**
    
    ```jsx
    project-root-directory/
    │
    ├── node_modules/                  # Folder for all the npm packages
    │
    ├── src/                           # Source folder for TypeScript files
    │   └── index.ts                   # Main TypeScript file
    │
    ├── build/                         # Compiled JavaScript files will be placed here by TypeScript
    │
    ├── package.json                   # NPM package configuration file, contains dependencies and scripts
    │
    ├── tsconfig.json                  # TypeScript compiler configuration file
    ```
    

- **Why Use TypeScript?**
    1. **JavaScript's Loose Behavior**: JavaScript allows operations that might be errors in other languages. For instance:
    TypeScript helps in catching such behaviors during development by providing static type checking.
        
        ```jsx
        console.log("2" + "2");  // Output: "22"
        console.log("2" - "2");  // Output: 0
        console.log(1 - !0);     // Output: 0
        
        ```
        
    2. **Runtime Errors**: In JavaScript, you only know about errors when you run the code. TypeScript provides compile-time error checking, which helps in identifying errors during development, not at runtime.
    3. When you define variables, TypeScript allows you to assign types to ensure the correctness of the data being used. For example:
        
        ```tsx
        let firstName: string = "Masai";
        let age: number = 26;
        let isActive: boolean = true;
        
        ```
        
    4. TypeScript allows defining complex structures like arrays, objects, and tuples with type safety.
    5. Advanced features like Generics, Enums, and Decorators are also used in large-scale applications to maintain a robust codebase.

### Usage

- **Working with TypeScript**
    - **Basic Types**: Define variables with specific types to avoid unintended type coercions.
        
        ```tsx
        let a: number = 5;
        let firstName: string = "Masai";
        let isActive: boolean = true;
        ```
        
    - **Arrays and Objects**: Define arrays with type annotations, and use interfaces or types to shape objects.
        
        ```tsx
        let numArray: number[] = [1, 2, 3, 4];
        type User = { id: number; name: string; };
        let user: User = { id: 1, name: "Masai" };
        ```
        
    - **Functions**: Provide type annotations for function parameters and return type.
        
        ```tsx
        function sum(a: number, b: number): number {
            return a + b;
        }
        ```
        

### Learner Activity

- **Exercise**: Convert the following JavaScript code into TypeScript by adding type annotations and ensuring it compiles without errors.
    
    ```jsx
    function greet(name, age) {
        console.log(`Hello, my name is ${name} and I am ${age} years old.`);
    }
    
    greet("Masai", 26);
    ```
    
- **Solution**:
    
    ```tsx
    function greet(name: string, age: number): void {
        console.log(`Hello, my name is ${name} and I am ${age} years old.`);
    }
    
    greet("Masai", 26);
    ```
    
    This lesson gives a comprehensive introduction to setting up and using TypeScript, starting from project creation, through TypeScript configuration, to writing and compiling TypeScript code. The practices and exercises included will help solidify the understanding of TypeScript's fundamental concepts and benefits.