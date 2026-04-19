# callback function-error handling with callback [120 min] (1)

### What is CallBack Function?

a callback function is a function that is passed as an argument to another function and is intended to be executed or "called back" at a certain point in the execution of that function. 

The primary purpose of using callback functions is to ensure that certain code is executed only after the completion of a specific operation or task.

### Example:

```jsx
function doSomething(callback) {
  // Perform some operation or task
  
  // Once the operation is complete, call the callback function
  callback();
}

function callbackFunction() {
  console.log('Callback function called!');
}

// Pass the callback function as an argument to doSomething()
doSomething(callbackFunction);
```

### Importance of Callback functions :

- **Asynchronous Operations**
    
    JavaScript is often used for asynchronous programming, where certain operations take time to complete, such as making API calls, fetching data from a database, or reading files. Callback functions allow you to define what should happen after the asynchronous operation is finished. 
    
    ```jsx
    function fetchData(callback) {
      // Simulate an asynchronous operation
      setTimeout(function() {
        const data = { name: 'John', age: 30 };
        callback(data);
      }, 2000);
    }
    
    function handleData(data) {
      console.log('Data received:', data);
    }
    
    fetchData(handleData);
    ```
    
- **Event Handling**
    
    Callback functions are commonly used to handle events in JavaScript, such as button clicks, form submissions, or mouse movements. When an event occurs, the associated callback function is called to respond to that event. This allows you to define custom behavior or actions to be performed when specific events occur.
    
    ```jsx
    document.getElementById('myButton').addEventListener('click', function() {
      console.log('Button clicked!');
    });
    ```
    
- **Modularity and Reusability**
    
    Callback functions promote modularity and reusability in your code. By passing a callback function as an argument to a higher-order function, you can separate concerns and define different behaviors for the same function depending on the context. This allows you to reuse the same function with different callbacks, making your code more flexible and maintainable.
    
    ```jsx
    function calculate(a,b,callback) {
      let result = callback(a,b);
    	console.log(`The result is ${result}.`)
    }
    
    //To add two numbers
    function adder(a,b) {
      return a + b;
    }
    
    //To multiply two numbers
    function multiplier(a,b) {
      return a * b;
    }
    
    calculate(2,4,adder);//The result is 6.
    calculate(2,4,multiplier);//The result is 8.
    
    //Here the same function calculate is used to add to numbers and 
    //is also used to multiply numbers
    
    ```
    
- **Error Handling**
    
    Callback functions allow you to handle errors effectively. By passing an error object as a parameter to the callback function, you can handle and propagate errors appropriately. This helps in providing meaningful error messages and taking necessary actions based on the outcome of an operation.
    
    ```jsx
    function performOperation(callback) {
      // Simulate an operation that encounters an error
      const success = false;
    
      if (success) {
        callback(null, 'Operation successful!');
      } else {
        const error = new Error('Operation failed!');
        callback(error, null);
      }
    }
    
    function handleResult(error, result) {
      if (error) {
        console.log('Error:', error.message);
      } else {
        console.log('Result:', result);
      }
    }
    
    performOperation(handleResult);
    ```
    

### Drawbacks of Callback functions :

- **Callback Hell or Pyramid of Doom**
    
    When multiple asynchronous operations are nested within each other, it leads to deeply nested callback functions, also known as **callback hell** or the **pyramid of doom**(as it seems like a pyramid). This can make code difficult to follow, leading to lower readability and maintainability.
    
    ```jsx
    asyncOperation1(function (result1) {
      asyncOperation2(result1, function (result2) {
        asyncOperation3(result2, function (result3) {
          // More nested callbacks...
        });
      });
    });
    ```
    
- **Lack of Synchronous Error Handling**
    
    In traditional callback-style programming, synchronous errors can be caught using try-catch blocks, while asynchronous errors require separate error callbacks or error-handling functions. This inconsistency in error handling can make the code harder to understand and reason about.
    
    ```jsx
    try {
      syncOperation();
    } catch (error) {
      console.error('An error occurred:', error);
    }
    
    asyncOperation(function (error, result) {
      if (error) {
        console.error('An error occurred:', error);
        return;
      }
      // Process result
    });
    ```
    
    In this case, synchronous errors are caught using try-catch, while asynchronous errors are handled within the callback.
    

There are limitations and challenges associated with handling asynchronous operations using callbacks. **Promises** were introduced in JavaScript to address this issue.

[assignment ](callback%20function-error%20handling%20with%20callback%20%5B12%20cf4e97b75a5342cc88d0b972fc9c3498/assignment%20e1a289cf7a4444a98fc687befdccd73d.md)