# Object creation in bulk quantity(factory /constructor function/ES6 class) [120 min] (1)

**Contain properties (key-value pairs). Value can be of any type including primitives, objects, functions and arrays.**

## Why Objects?

#1 **Grouping related variables** 

```jsx
// grouping related variables
let account = {
  name: 'Vivek',
  type: 'Simple Saving',
  balance: 100000,
  active: true,
}
```

#2 **Adding & Removing Properties and Methods after creating an object [Dynamic objects]**

```jsx
account.reference = 'Some one';
account['new_property'] = 'Yet some value';
console.log(account);

delete account.reference;
console.log(account);
```

#3 **Passing into a function as an Argument**

```jsx
// can be passes to a function as an argument
function printAccountDetails(obj) {
  console.log('Name: ', obj.name, 'Type: ' ,obj.type, 'Active: ' , obj.active, 'Bal: ' , obj.balance);
}

printAccountDetails(account);
```

#4 **Related functions can be a part of the object itself, so wherever we have this object we have access to its functions (methods). In other words, Objects can store functions with their associated data.**

```jsx
let account = {
  name: 'Vivek',
  type: 'Preffered Savings',
  balance: 100000,
  active: true,
  print: function () {
    console.log('Name: ', this.name, 'Type: ', this.type, 'Active: ', this.active, 'Bal: ', this.balance);
  }
};

account.print()
```

**As our application grows, we need different ways to create Objects. How to create multiple accounts? for example.**

## Creating Objects

What is the total population of the world (2021 data) : Around 784 Crores (8 Billion) Human beings are present in this planet earth!!

Who is the creator?

Imagine you are the one & you have to create 8 Billion human beings. Would you think for each one of them - where the heart should be, where should be their stomach, where should be the brain? Is it feasible for you to design the properties & methods of each human one by one? is that scalable? 

You will basically create a process - a system - a function - that would take in some arguments and give you a human being!!

Another example: 

What if you need to draw this exact same drawing in 1,00,000 documents?

You would probably create a system - a process - a stamp maybe?

![Untitled](Object%20creation%20in%20bulk%20quantity(factory%20construct%20ee054347d9b444d3bb0d7fa608710c7a/Untitled.png)

> **If we need to create similar kind of a thing in quantity - its good to have a system - a structure - a process**
> 

Can you think of more real world examples? 

- Molds (sancha) for clay toys / utensils

“**Creating objects in Bulk Quantity”**

          vs

**“Inheritance”**

This the concept of creating or manufacturing an object in bulk quantity. Creation of object is different of inheritance. 

If you need to manufacture 1,00,000 iPhone 1st Gen in 2007 -  we understand that we need a process to manufacture them… create them… only the serial number of the device would change, rest all properties & methods remains the same…

The all have some common properties & methods

![Untitled](Object%20creation%20in%20bulk%20quantity(factory%20construct%20ee054347d9b444d3bb0d7fa608710c7a/Untitled%201.png)

Now when iPhone-2 (3G) was planned for 2008, obviously - first thing is that we need a system/structure/process/blueprint

But wait can we inherit/reuse of the properties from the older version of the phone.

Do you see the difference between creating & inheriting

## iPhone example

Problem: [https://codepen.io/drupalastic/pen/xxJyozr?editors=0012](https://codepen.io/drupalastic/pen/xxJyozr?editors=0012)

Solution: 

```jsx
// write a factory function iPhone1 to create iPhone objects in bulk quantiy
// iPhone1 takes in ASIN, color, display, camera
// the object it creates has the following 
// properties: ASIN, color, display, camera
// methods: 
// dial - console logs "tring.. tring..."
// sendMessage - console logs "Sending message..."
// cameraClick - "Camera clicked"

function iPhone1(ASIN, color, display, camera) {
  let obj = {};
  
  obj.ASIN = ASIN;
  obj.color = color;
  obj.display = display;
  obj.camera = camera;
  
  obj.dial = function() {
    console.log("tring.. tring...")
  }
  
  obj.sendMessage = function() {
    console.log("Sending message...")
  }
  
  obj.cameraClick = function() {
    console.log("Camera clicked")
  }
  
  return obj;
}

let i1 = iPhone1(1,'B09X67JBQV',7.8,'IOS', '128mb','Gray','90mm','2.0 MP')
i1.dial(); // "tring.. tring..."
i1.sendMessage(); // "Sending message..."
i1.cameraClick(); // "Camera clicked"
```

Student Tasks: [https://codepen.io/drupalastic/pen/wvEdeMr?editors=0010](https://codepen.io/drupalastic/pen/wvEdeMr?editors=0010) [problem - create animal factory function]

- Solution
    
    ```jsx
    
    ```
    

Student Tasks: [https://codepen.io/drupalastic/pen/KKxmqvG?editors=0012](https://codepen.io/drupalastic/pen/KKxmqvG?editors=0012) [problem - create animal using constructor function]

- Solution
    
    ```jsx
    
    ```
    

Student Tasks: [https://codepen.io/drupalastic/pen/ZEMKyZz?editors=0012](https://codepen.io/drupalastic/pen/ZEMKyZz?editors=0012) [problem - create animal using ES6 classes]

- Solution
    
    ```jsx
    
    ```
    

**how to teach constructor() in ES6 classes?**

- if we think of a class body as the body of a constructor function
- whenever it is invoked with a new keyword, a `this` object is formed
- what can you do to add a few properties to it - a method, stick them to this & then invoke the method
- constructor plays the same role, it sticks properties + the constructor method is automatically called by javascript every time an object is created

Home (Practice )Tasks: 

Try to construct `vehicles` using all three ways: 

```jsx
Vehicle
    ├── brand <string>
    ├── tyres <number>
    ├── doors <number>
    ├── driver <string>
    ├── accelerate <function that logs `accelerating`>
    └── honking <function that logs `honking`>
```

Try to construct `creatures` using all three ways:

```jsx
Creature
    ├── name <string>
    └── eat <function that logs <name> is eating>
```

## B27 Live session

Student Tasks: [https://codepen.io/drupalastic/pen/wvEdeMr?editors=0010](https://codepen.io/drupalastic/pen/wvEdeMr?editors=0010) [problem - create animal factory function]

- Solution
    
    ```jsx
    
    ```
    

Student Tasks: [https://codepen.io/drupalastic/pen/KKxmqvG?editors=0012](https://codepen.io/drupalastic/pen/KKxmqvG?editors=0012) [problem - create animal using constructor function]

- Solution
    
    ```jsx
    
    ```
    

Student Tasks: [https://codepen.io/drupalastic/pen/ZEMKyZz?editors=0012](https://codepen.io/drupalastic/pen/ZEMKyZz?editors=0012) [problem - create animal using ES6 classes]

- Solution

[assignment ](Object%20creation%20in%20bulk%20quantity(factory%20construct%20ee054347d9b444d3bb0d7fa608710c7a/assignment%2036b595eaa3f949dba5ed17345d4652de.md)