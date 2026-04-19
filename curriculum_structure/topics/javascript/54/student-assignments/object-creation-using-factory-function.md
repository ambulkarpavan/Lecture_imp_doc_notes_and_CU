# assignment

[Object creation - Student task 1 - factory functions [Problem] (codepen.io)](https://codepen.io/drupalastic/pen/xxJyozr?editors=0012)

[Student Task - Creating objects in Bulk using factory function [problem] (codepen.io)](https://codepen.io/drupalastic/pen/wvEdeMr?editors=0010)

[Object construction using constructor functions (codepen.io)](https://codepen.io/drupalastic/pen/KKxmqvG?editors=0012)

[Object construction using ES6 Classes (codepen.io)](https://codepen.io/drupalastic/pen/ZEMKyZz?editors=0012)

**Question 1:**

```jsx
// write a "factory function iPhone1 to create iPhone objects in bulk quantity
// iPhone1 takes in ASIN, color, display, camera
// the object it creates has the following 
// properties: ASIN, color, display, camera
// methods: 
// dial - console logs "tring.. tring..."
// sendMessage - console logs "Sending message..."
// cameraClick - "Camera clicked"

function iPhone1(ASIN, color, display, camera) {
  let obj = {};
  
  // Your code here
  
  return obj;
}

// Example invocation: 
let i1 = iPhone1(1,'B09X67JBQV',7.8,'IOS', '128mb','Gray','90mm','2.0 MP')
i1.dial(); // "tring.. tring..."
i1.sendMessage(); // "Sending message..."
i1.cameraClick(); // "Camera clicked"
```

```jsx
// write a "factory function iPhone2 to create iPhone objects in bulk quantity
// iPhone1 takes in ASIN, color, display, camera,bluetooth
// the object it creates has the following 
// properties: ASIN, color, display, camera,bluetooth
// methods: 
// dial - console logs "tring.. tring..."
// sendMessage - console logs "Sending message..."
// cameraClick - "Camera clicked"
//connectBluetooth - "Bluetooth connected successfully..."

function iPhone2(ASIN, color, display, camera,bluetooth) {
  let obj = {};
  
  // Your code here
  
  return obj;
}

// Example invocation: 
let i1 = iPhone2(1,'B09X67JBQV',7.8,'IOS', '128mb','Gray','90mm','2.0 MP', "5.1")
i1.dial(); // "tring.. tring..."
i1.sendMessage(); // "Sending message..."
i1.cameraClick(); // "Camera clicked"
i1.connectBluetooth(); //"Bluetooth connected successfully..."
    
```

- now use the constructor function and ES6 class to write the same code.
- use .call()/.apply() to avoid repetition.

**Question 2:**

```jsx
// Animal
//     ├── noOfLegs <number>
//     ├── vegetarian <boolean>
//     └── eat() <function that logs `eating...` >

// Write a factory function that can be used to create animal objects in bulk quantity. 

//Every animal object must have 2 properties: noOfLegs, vegetarian
//Every animal must have 2 methods
// eat() // console.log(`eating...`)
// greet() // console.log(`Hi, I have <noOfLegs> legs.`)

function animal(noOfLegs, vegetarian) {
  
}

// Example invocation
let a1 = animal(4,true);
// a1.eat() // eating...
// a1.greet() // Hi, I have 4 legs.
```

**Question 3:**

```jsx
//Convert the following factory function to a constructor function
function animal(noOfLegs, vegetarian) {
  let obj = {};

  obj.noOfLegs = noOfLegs;
  obj.vegetarian = vegetarian;

  obj.eat = function() {
    console.log('eating...')
  }

  obj.greet = function() {
    console.log(`Hi, I have ${obj.noOfLegs} legs.`)
  }

  return obj;
}

// Example invocation
let a1 = animal(4,true);
console.log(a1)
a1.eat() // eating...
a1.greet() // Hi, I have 4 legs.
```

**Question 4:**

```jsx
//Convert the following factory function to an ES6 class
function animal(noOfLegs, vegetarian) {
  let obj = {};

  obj.noOfLegs = noOfLegs;
  obj.vegetarian = vegetarian;

  obj.eat = function() {
    console.log('eating...')
  }

  obj.greet = function() {
    console.log(`Hi, I have ${obj.noOfLegs} legs.`)
  }

  return obj;
}

// Example invocation
let a1 = new animal(4,true);
console.log(a1)
a1.eat() // eating...
a1.greet() // Hi, I have 4 legs.
```