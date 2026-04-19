# Scope [20 min] (1)

## Lexical Scope

[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)

There are three scopes. Look at the screenshot and try to make a sense of it.

![Untitled](Scope%20%5B20%20min%5D%20(1)%2082c285f56ab34ff2b53d2dbe0529be18/Untitled.png)

Javascript is a **two-pass** system. The code is processed (or compiled or parsed) first. In this first phase, the scopes are set up and the grammar of your code is validated. Then in the second phase, the code is executed. 

Javascript organizes scopes with **functions** and **blocks**. In the processing phase, the scope for every identifier (variable) is set.

In a lexically scoped language (which Javascript is), all of the identifiers & scopes that we dealing with, are determined in the first pass (compile-time). The decisions that I make about scope are author time decisions. When I write a function & put a variable there, it means that the variable is always gonna be scoped to that function. The place where the variable "**sits**" physically in your code and the variables that **"surrounds"** it physically are **important**. 

Another, important thing about lexical scopes is that if the compiler cannot find a variable's declaration within the scope, it looks up to its parent's and ancestor's scope.

In a non-strict environment, if a variable is used and never declared, JS auto-declares it in the global scope. it's a bad part of JS. We should always operate in strict mode.

## IIFE - Immediately invoked function expression

[MDN](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)

We keep our code inside a function, in order to prevent pollution of the global scope. We execute it immediately to make sure that our code actually runs.

```jsx
(function () {
  // our code here
})();
```

*Very important note: Make sure that the statement above it ends with a semicolon else javascript engine might teat it as a continuation of that statement and throw weird errors.*

### Student Task

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