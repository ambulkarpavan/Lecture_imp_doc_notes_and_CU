# asynchronous JS - web API, event-loop, callback Queue [120 min] (1)

## setTimeout()

The global **`setTimeout()`** method sets a timer that executes a function or specified piece of code once the timer expires.

The returned `timeoutID` is a positive integer value that identifies the timer created by the call to `setTimeout()`. This value can be passed to `[clearTimeout()](https://developer.mozilla.org/en-US/docs/Web/API/clearTimeout)` to cancel the timeout.

### Syntax:

```jsx
let id = setTimeout(function, delay);

//to  clear the timeout
clearTimeout(id);
```

## setInterval()

The **`setInterval()`** method, offered on the `[Window](https://developer.mozilla.org/en-US/docs/Web/API/Window)` and `[Worker](https://developer.mozilla.org/en-US/docs/Web/API/Worker)` interfaces, repeatedly calls a function or executes a code snippet, with a fixed time delay between each call.

This method returns an interval ID that uniquely identifies the interval, so you can remove it later by calling `[clearInterval()](https://developer.mozilla.org/en-US/docs/Web/API/clearInterval)`.

### Syntax:

```jsx
setInterval(function, delay);

//to  clear the time interval
clearInterval(id);
```

## Blocking Code VS Non-Blocking Code

As JS is a `synchronous` language, it executes code line by line. So if there is a block of code that will take some time, in that case, it will block the execution of the rest of the part till that duration.

```jsx
 console.log("hi");
for(let i =0;i<7000000000;i++){
	
}
console.log("Welcome to masai School.")

//In this code the console of "Welcome to masai School." is executed only after the completion of the loop.
```

But this kind of behavior is not always good for user experience. 

To overcome this issue JS takes the help of `browser API` to execute tasks ( that might take some time )asynchronously. 

```jsx
 console.log("hi");
setTimeout(function(){
for(let i =0;i<7000000000;i++){
	
}},0)
console.log("Welcome to masai School.")
```

Once JS encounters any `asynchronous` code it gives it to the `browser API` and it is registered along with a callback function to be executed when the task completes.

When the time is over, the code is moved to the callback queue or microtask queue based on the priority of that task. 

- **Microtask Queue:** Holds microtasks, such as Promise callbacks and Mutation Observer callbacks. These tasks have higher priority than regular tasks and are executed before regular tasks.
- **Callback Queue:** Holds tasks like timers, network responses, and user interaction events. These tasks are executed after microtasks.

## Event loop:

The event loop is a continuous loop that repeatedly checks the state of different queues and the call stack. It follows a specific sequence:

**a. Check the Microtask Queue:** Execute all pending microtasks in the order they were added.
**b. Check the Callback Queue:** If the call stack is empty, move a task from the callback queue to the call stack and execute it.
**c. Repeat:** The event loop keeps cycling through these steps, allowing asynchronous tasks to be executed while maintaining responsiveness.

![62c6fbddb12bb523df242285_event_loop_animation-gif.gif](asynchronous%20JS%20-%20web%20API,%20event-loop,%20callback%20Qu%2051ffdc0b72a341e5b13795047438db9a/62c6fbddb12bb523df242285_event_loop_animation-gif.gif)

### Guess the output

```jsx
console.log("sync 1");
console.log("sync 2");

Promise.resolve().then(()=>{console.log("promise resolve 1")});

Promise.resolve().then(
    ()=>{
    console.log("promise resolve 2");
    setTimeout(()=>{console.log("Inside timeout")},0);
    }
);

Promise.resolve().then(()=>{console.log("promise resolve 3")});

setTimeout(
    ()=>{
    console.log("set Timeout 1");
    setTimeout(()=>{console.log("inside timeout")},1000);
    }
,2000);

setTimeout(()=>{console.log("set time out 2")},1000);
setTimeout(()=>{console.log("set time out 3")},0);

 console.log("sync 3");
 console.log("sync 4");
```

```jsx
console.log("sync 1");
console.log("sync 2");

setTimeout(()=>{console.log("set time out 1")},0);

setTimeout(
    ()=>{
    console.log("set Timeout 2");
    Promise.resolve().then(()=>{console.log("inside promise resolve 1")});
    }
,0);

setTimeout(()=>{console.log("set time out 3")},0);

Promise.resolve().then(()=>{console.log("promise resolve 1")});

Promise.resolve().then(
    ()=>{
    console.log("promise resolve 2");
    setTimeout(()=>{console.log("Inside timeout 1")},0);
    }
);

Promise.resolve().then(()=>{console.log("promise resolve 3")});

 console.log("sync 3");
 console.log("sync 4");
```