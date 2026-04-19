# asynchronous JS - Promise async await [120 min] (1)

There are limitations and challenges associated with handling asynchronous operations using callbacks. **Promises** were introduced in JavaScript to address this issue.

### What is Promise?

In JavaScript, a Promise is an object that represents the eventual completion or failure of an asynchronous operation and its resulting value. It provides a more structured and efficient way to handle asynchronous operations compared to using callback functions.

### Promises have three states:

1. **Pending:** The initial state when the Promise is created and the asynchronous operation is still in progress.
2. **Fulfilled:** The state when the asynchronous operation is successfully completed, and the Promise is resolved with a value.
3. **Rejected:** The state when the asynchronous operation encounters an error or failure, and the Promise is rejected with a reason or error object.

![Untitled.png](asynchronous%20JS%20-%20Promise%20async%20await%20%5B120%20min%5D%20(1%209d08c49f1a4746a3a25212153a71aaf6/Untitled.png)

**Synchronous Example:** 

- Fans ask for the release date of the next album and
- she gives them the **date** immediately

**Asynchronous Example:** 

- Fans ask for the **release date** of the next album
- She gives them back a **promise** {unfulfilled}
- The promise may **resolve** in the future with a date {fulfilled}
- The promise may **reject** in the future with an error {fulfilled}

## Consuming vs Producing a promise

This is a real-life analogy for things we often have in programming:

1. A “**producing** code” that does something and takes time. For instance, some code that loads the data over a network. That’s a “singer”.
2. A “**consuming** code” that wants the result of the “producing code” once it’s ready. Many functions may need that result. These are the “fans”.
3. A *promise* is a special JavaScript object that links the “producing code” and the “consuming code” together. In terms of our analogy: this is the “subscription list”. The “producing code” takes whatever time it needs to produce the promised result, and the “promise” makes that result available to all of the subscribed code when it’s ready.

The analogy isn’t terribly accurate, because JavaScript promises are more complex than a simple subscription list: they have additional features and limitations. But it’s fine, to begin with.

The constructor syntax for a promise object is:

```jsx
let promise = new Promise(function(resolve, reject) {
  // executor (the producing code, "singer")
});
```

The function passed to the `new Promise` is called the *executor*. When a `new Promise` is created, the executor runs automatically. It contains the producing code which should eventually produce the result. In terms of the analogy above: the executor is the “singer”.

Its arguments `resolve` and `reject` are callbacks provided by JavaScript itself. Our code is only inside the executor.

When the executor obtains the result, be it soon or late, doesn’t matter, it should call one of these callbacks:

- `resolve(value)` — if the job is finished successfully, with result `value`.
- `reject(error)` — if an error has occurred, the `error` is the error object.
- 

So to summarize: the executor runs automatically and attempts to perform a job. When it is finished with the attempt, it calls `resolve` if it was successful or `reject` if there was an error.

[Student task 1](https://codepen.io/adarshakhatua/pen/xxmVXxd?editors=0010)

### Producing a Promise:

```jsx
function getReleaseDate() {
  return new Promise((resolve, reject) => {
    // Simulating an asynchronous operation to get information about the album.
    setTimeout(() => {
      const data = { date: '31st October', Location: "Bangalore" };
      // Simulating a successful data retrieval
      if (data) {
        resolve(data); // Resolve the promise with the fetched data
      } else {
        reject(new Error('Albul release date postponed for time being.')); // Reject the promise with an error
      }
    }, 2000); // Simulating a delay of 2 seconds
  });
}
```

### Consuming a Promise:

```jsx
getReleaseDate()
  .then((data) => {
    console.log('Greetings! this is the release information:', data);
    // Additional actions or chaining of promises can be performed here
  })
  .catch((error) => {
    console.log('Error:', error.message);
  });
```

### Different Methods of Promise:

- **Promise.all**
    
    **`Promise.all`** is a method that takes an array (or any iterable) of Promise objects as input and returns a new Promise. This new Promise will be fulfilled when all the Promises in the input array have been fulfilled, and it will contain an array of the fulfilled values from the input Promises. If any of the Promises fail, the entire operation is considered failed, and the first rejection reason is provided.
    
- **Promise.allSettled**
    
    **`Promise.allSettled`** is a method that takes an array (or any iterable) of Promise objects as input and returns a new Promise. This new Promise will be fulfilled when all the Promises in the input array have settled (either fulfilled or rejected), and it will contain an array of objects representing the settled status of each Promise.
    
- **Promise.race**
    
    **`Promise.race`** is a method that takes an array (or any iterable) of Promise objects as input and returns a new Promise. This new Promise will settle (either fulfill or reject) as soon as the first Promise in the input array settles.
    
- **Promise.any**
    
    **`Promise.any`** is a method that takes an array (or any iterable) of Promise objects as input and returns a new Promise. This new Promise will fulfill with the value of the first Promise in the input array that fulfills successfully.
    

### Achieving Asynchronous action using Callback VS Promise:

- **Using Callback**
    
    ```jsx
    function asynchronous1(data, callback) {
      console.log("Task 1 started");
      setTimeout(() => {
        callback(data);
      }, 2000);
    }
    
    function asynchronous2(data, callback) {
      console.log("Task 2 started");
      data = data.map(i => i * 2);
      setTimeout(() => {
        callback(data);
      }, 2000);
    }
    
    function asynchronous3(data, callback) {
      console.log("Task 3 started");
      data = data.reduce((ac, i) => ac + i);
      setTimeout(() => {
        callback(data);
      }, 2000);
    }
    ```
    
    ```jsx
    const input = [1, 2, 3, 4, 5];
    
    asynchronous1(input, function (result1) {
      asynchronous2(result1, function (result2) {
        asynchronous3(result2, function (result3) {
          console.log("Final result:", result3);
        });
      });
    });
    ```
    
- **Using Promise**
    
    ```jsx
    function asynchronous1(data) {
      return new Promise((resolve) => {
        console.log("Task 1 started");
        setTimeout(() => {
          resolve(data);
        }, 2000);
      });
    }
    
    function asynchronous2(data) {
      return new Promise((resolve) => {
        console.log("Task 2 started");
        data = data.map(i => i * 2);
        setTimeout(() => {
          resolve(data);
        }, 2000);
      });
    }
    
    function asynchronous3(data) {
      return new Promise((resolve) => {
        console.log("Task 3 started");
        data = data.reduce((ac, i) => ac + i);
        setTimeout(() => {
          resolve(data);
        }, 2000);
      });
    }
    ```
    
    ```jsx
    const input = [1, 2, 3, 4, 5];
    
    asynchronous1(input)
      .then(asynchronous2)
      .then(asynchronous3)
      .then(result => {
        console.log("Final result:", result);
      })
      .catch(error => {
        console.error("An error occurred:", error);
      });
    ```
    

### What is Async/await?

Async/await is a syntactic feature introduced in JavaScript to simplify asynchronous programming. It provides a more synchronous-style coding approach while still allowing the non-blocking execution of asynchronous operations.

Async/await was introduced in JavaScript to make asynchronous code easier to read and write, especially when dealing with promises.

Before async/await, chaining promises using **`.then()`** could make the code harder to understand. It required nesting multiple callbacks, which could become confusing and messy.

Async/await simplifies this by allowing us to write asynchronous code in a more straightforward and sequential way, similar to regular synchronous code.

```jsx
const input = [1, 2, 3, 4, 5];

async function performTasks() {
  try {
    const result1 = await asynchronous1(input);
    const result2 = await asynchronous2(result1);
    const result3 = await asynchronous3(result2);
    console.log("Final result:", result3);
  } catch (error) {
    console.error("An error occurred:", error);
  }
}

performTasks();
```

### Benefits of async/await:

1. **Easier to understand**: Async/await makes the code easier to read and follow. It removes the need for complex **`.then()`** chains, so the code looks more like a step-by-step sequence.
2. **Simpler error handling**: Async/await makes it easier to handle errors. Instead of attaching **`.catch()`** at every step, we can use a single try-catch block to handle errors within the async function.
3. **Reduces callback complexity**: Async/await avoids excessive nesting of callbacks, which can make the code hard to follow. It allows for a flatter and more organized code structure.
4. **Simplifies debugging**: Debugging async/await code is easier because we can pause execution at each **`await`** statement, helping us see the flow of execution more clearly.

[assignment](asynchronous%20JS%20-%20Promise%20async%20await%20%5B120%20min%5D%20(1%209d08c49f1a4746a3a25212153a71aaf6/assignment%203a70e8bacbc741d08e8df18f325527e4.md)