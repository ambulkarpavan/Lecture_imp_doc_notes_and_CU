# Prototypical inheritance using a factory function [120 min] (1)

## **Learning Objectives**

- Understand the concept of inheritance and how it enables code reuse in object-oriented programming.
- Understand how prototypes work in JavaScript and how they enable inheritance.
- Understand the concept of the prototype chain and how it allows objects to inherit properties and methods from other objects.
- Know how to create prototype chains using **`Object.setPrototypeOf()`** and **`Object.create()`**.
- Understand how functions are linked to objects in JavaScript through the **`prototype`** property.

## Before moving to inheritance we need to solve these three simple problems as a quick revision

Slides: [https://www.canva.com/design/DAFfxpClzqE/F2oao3rVUk7apTd6K8GagA/edit?utm_content=DAFfxpClzqE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton](https://www.canva.com/design/DAFfxpClzqE/F2oao3rVUk7apTd6K8GagA/edit?utm_content=DAFfxpClzqE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

Class codes: [class codes (codepen.io)](https://codepen.io/Adarsha-khatua/pen/VwVPqWr?editors=1010)

- Object creation - Student task 1 - factory functions [[problem](https://codepen.io/drupalastic/pen/xxJyozr?editors=0012)]
    - solution
        
        ```jsx
        // write a factory function iPhone1 to create iPhone objects in bulk quantiy
        // iPhone1 takes in generation, ASIN, weight, OS, RAM, color, display, camera
        // the object it creates has the following 
        // properties: generation, ASIN, weight, OS, RAM, color, display, camera
        // methods: 
        // dial - console logs "tring.. tring..."
        // sendMessage - console logs "Sending message..."
        // cameraClick - "Camera clicked"
        
        function iPhone1(generation, ASIN, weight, OS, RAM, color, display, camera) {
          let obj = {};
            
          obj.generation = generation;
          obj.asin = ASIN;
          obj.weight = weight;
          obj.os = OS;
          obj.ram = RAM;
          obj.color = color;
          obj.display = display;
          obj.camera = camera
          
          obj.dial = function(){
            console.log('tring.. tring...');
          }
          
          obj.sendMessage = function() {
            console.log('Sending message...');
          }
          
          obj.cameraClick = function() {
            console.log('Camera clicked')
          }
          
          return obj;  
        }
        
        let i1 = iPhone1(1,'B09X67JBQV',7.8,'IOS', '128mb','Gray','90mm','2.0 MP')
        i1.dial(); // "tring.. tring..."
        i1.sendMessage(); // "Sending message..."
        i1.cameraClick(); // "Camera clicked"
        ```
        
- Object creation - Student task 2 - factory functions [[problem](https://codepen.io/Adarsha-khatua/pen/KKraGpM?editors=0010)]
    - solution
- Objects - student task 3 - attach simple properties from one object to another [[problem](https://codepen.io/drupalastic/pen/xxJZgQW)]
    - solution
        
        ```jsx
        
        ```
        
- Objects - student task 4 - attach simple properties from one object to another with args [[problem](https://codepen.io/drupalastic/pen/BaqNvoy?editors=0010)]
    - solution
        
        ```jsx
        
        ```
        

## Inheritance

Inheritance is one of the core concepts of object-oriented programming that enables an object to take on the properties and methods of another object. This makes it easy to reuse code in different parts of an application.

Unlike classical languages like C# and Java, JavaScript does not have a true class. It utilizes linking objects together in order to inherit properties. Every single object that you create, unless specified not to, is automatically linked to the corresponding global object prototype.

When you think of inheritance, you might think about classes, and object-oriented languages like C# and Java, and how these languages use classes to create inheritance by instantiating classes, extending them to inherit and pass these properties and methods to child classes.

JavaScript does not have a true class. It uses prototypes, is just an object. These objects are automatically linked together for us by JavaScript engines so that we can access properties and methods.

## Classical Inheritance

![Untitled](Prototypical%20inheritance%20using%20a%20factory%20function%20%20b20fe13d68e74b2f91b8e8900172c04b/Untitled.png)

[https://www.figma.com/file/n9WHBIq5I4CXqAMmKQXdj1/Untitled?node-id=0%3A1](https://www.figma.com/file/n9WHBIq5I4CXqAMmKQXdj1/Untitled?node-id=0%3A1)

## What is a prototype chain?

When it comes to inheritance, Javascript only has one construct: **objects**.  Each object has a private property (`__proto__`) that holds a link to another object (`prototype`) . That prototype object has a `__proto__` of its own, and so on, until an object is reached with `null` as its prototype.

Nearly all objects in Javascript are instances of Object that sits on the top of a prototype chain. 

The ECMAScript likes to represent this hidden property as  `[[Prototype]]` but many browsers like to represent it as `__proto__`. For our discussion, we will be using `__proto__` notation to refer to the private property if the object responsible for chaining.

Note: These days, even some browsers represent `__proto__` as `[[Prototype]]`.   

```jsx
let obj = {
  name: 'vivek',
  sayHello: function () {
    console.log('Hello');
  }
}
```

![Untitled](Prototypical%20inheritance%20using%20a%20factory%20function%20%20b20fe13d68e74b2f91b8e8900172c04b/Untitled%201.png)

In the browser console, if you try, you can of course get access to `name` and `sayHello` by typing `.` after `obj`. 

But along with the two properties that we have defined, we also see a lot of other properties like `hasOwnProperty`, `toString()` and many more. Where are they stored & how do we get access to them in our `obj`

They are stored in the built-in `Object` constructor function. The object constructor function has a property called `prototype`. `Object.prototype` is an object. All these extra properties that we see in our `obj` are actually properties of `Object.prototype`.

Our `obj` is linked to `Object.prototype` via the hidden property called `__proto__` 

The way developers communicate the above chain is as follows:

 communication: `Object()` is the **prototype** of `obj`

technical: obj's __proto__ is linked to Object's prototype

We can validate if `obj.__proto__` is equal to `Object.prototype` by logging `obj.__proto__ === Object.prototype` 

Let's move one step ahead with the example of an array. Consider the following array

```jsx
let arr = ['one', 'two', 'three'];
```

Again with our `arr` we see so many properties attached. Where are they stored? How do we see them as a property of our `arr` 

![Untitled](Prototypical%20inheritance%20using%20a%20factory%20function%20%20b20fe13d68e74b2f91b8e8900172c04b/Untitled%202.png)

The `__proto__` property of `Array.prototype` is linked to `Object.prototype` and in that way, it has access to all of the properties & methods of `Object.prototype`

The `__proto__` property of the `arr` object is linked to `Array.prototype` & in that way `arr` has access to all the properties and methods of `Array.prototype` and `Object.prototype` 

We can verify this relationship by logging these:

```jsx
console.log(arr.__proto__ === Array.prototype) // true
console.log(Array.prototype.__proto__ === Object.prototype); // true
console.log(Object.prototype.__proto__ === null); // true
```

Now let's check the prototype chain of a function. consider the following simple function:

```jsx
function fun() {
  
}
```

We'll see that our `fun` has access to several functions related properties & methods like `call()`, `bind()` , `arguments`, `length` etc... and also it has access to properties and methods of objects. 

![Untitled](Prototypical%20inheritance%20using%20a%20factory%20function%20%20b20fe13d68e74b2f91b8e8900172c04b/Untitled%203.png)

This prototype chain must be obvious to you by now.

This chain can be verified by running the following command:

```jsx
console.log(fun.__proto__ === Function.prototype);
console.log(fun.__proto__.__proto__ == Object.prototype);  // or
console.log(Function.prototype.__proto__ == Object.prototype);
```

## Creating our own Prototype chains

using `Object.setPrototypeOf()` 

```jsx
let obj = {
  name: 'vivek',
  sayHello: function () {
    console.log('Hello');
  }
}

let obj2 = {
  salary: 100000,
  work: function () {
    console.log('Working');
  }
}

Object.setPrototypeOf(obj2, obj);

obj2.sayHello();

console.log(obj2);
```

![Untitled](Prototypical%20inheritance%20using%20a%20factory%20function%20%20b20fe13d68e74b2f91b8e8900172c04b/Untitled%204.png)

The `Object.setPrototypeOf()` method sets the prototype (i.e., the internal `__proto__` property) of a specified object to another object

Documentation: [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf)

![Untitled](Prototypical%20inheritance%20using%20a%20factory%20function%20%20b20fe13d68e74b2f91b8e8900172c04b/Untitled%205.png)

```jsx
obj2.__proto__ === obj // true
```

The same task can also be performed using `Object.create()`

```jsx
let obj = {
  name: 'vivek',
  sayHello: function () {
    console.log('Hello');
  }
}

let obj2 = Object.create(obj);
obj2.salary = 100000;
obj2.work = function () {
  console.log('Working');
}

Object.setPrototypeOf(obj2, obj);

obj2.sayHello();

console.log(obj2);
```

The `Object.create()` method creates a new object, using an existing object as the prototype of the newly created object.

Documentation: [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create) 

💡What is the difference between `Object.assign` and `Object.setPrototypeOf` / `Object.create`

`Object.setPrototypeOf()` / `Object.create()`  sets up a prototype chain between the source object and the target object. But, `Object.assign()` method only copies enumerable and own properties from a source object to a target object.

```jsx
let obj = {
  name: 'vivek',
  sayHello: function () {
    console.log('Hello');
  }
}

let obj2 = {};

Object.assign(obj2, obj); // doesnot create a chain

console.log(obj2);
```

![Untitled](Prototypical%20inheritance%20using%20a%20factory%20function%20%20b20fe13d68e74b2f91b8e8900172c04b/Untitled%206.png)

`Object.assign` does not create a prototype chain.

```jsx
Object.setPrototypeOf(obj2, obj);
console.log(obj2);
```

`Object.setPtototypeOf()` & `Object.create()` does create a prototype chain.

![Untitled](Prototypical%20inheritance%20using%20a%20factory%20function%20%20b20fe13d68e74b2f91b8e8900172c04b/Untitled%207.png)

Example:

```jsx
let obj = {
  name: 'vivek',
  sayHello: function () {
    console.log('Hello');
  }
}

let obj2 = {
  salary: 100000,
  work: function () {
    console.log('Working');
  }
}

Object.setPrototypeOf(obj2, obj);

let obj3 = {
  subject: 'Javascript',
  teach: function () {
    console.log('Teaching');
  }
}

Object.assign(obj3, obj2);
console.log(obj3);
```

![Untitled](Prototypical%20inheritance%20using%20a%20factory%20function%20%20b20fe13d68e74b2f91b8e8900172c04b/Untitled%208.png)

## How are functions linked to objects in Javascript?

Okay, now we understand that every object has a `__proto__` property which is used to link it to another object. But what about functions? How is prototypal inheritance handled in objects created by constructor functions via `new` keyword?

Functions are first-class objects in JavaScript which means they can have their own properties and methods like any other plain object could.

This `prototype` property of a function itself is not used in the prototype chain look-up. The `.prototype` property object lives in every function except arrow functions. 

## Identifying problems with our existing approach

- Let students discover
    - Although the methods remain the same, but they are copied to all the objects

## Solving the problem using the functions prototype object & linking our objects to it

```jsx
Person.prototype.increaseAge = function() {
  this.age = this.age + 1;
  console.log(this.age);
}

Person.prototype.sleep = function() {
  console.log(`${this.firstName} is sleeping.`)
}

Person.prototype.eat = function() {
  console.log(`${this.firstName} is eating.`)
} 

Person.prototype.introduceSelf = function() {
  console.log(this.firstName, this.lastName, this.age);
}

function Person(firstName, lastName, age) {
  let obj = {};
  Object.setPrototypeOf(obj, Person.prototype);

  obj.firstName = firstName;
  obj.lastName = lastName;
  obj.age = age;

  return obj;
}

Object.setPrototypeOf(Employee.prototype, Person.prototype)

Employee.prototype.work = function() {
  console.log(`${this.firstName} is working.`)
}

Employee.prototype.getSalary = function() {
  console.log(`${this.firstName} is getting Salary.`)
}

function Employee(firstName, lastName, age, department, salary) {
  let obj = Person(firstName, lastName, age);
  Object.setPrototypeOf(obj, Employee.prototype);

  obj.department = department;
  obj.salary = salary;

  return obj;
}

let e1 = Employee("John", "Doe", 25, "frontend", 200000);
console.log(e1.eat())
```

![Untitled](Prototypical%20inheritance%20using%20a%20factory%20function%20%20b20fe13d68e74b2f91b8e8900172c04b/Untitled%209.png)

## iPhone example with Factory Method

*just a made up example to demonstrate object creation & inheritance. [this can be d5 assignment in the future]*

Student Task 1: [https://codepen.io/drupalastic/pen/xxJZgQW?editors=0010](https://codepen.io/drupalastic/pen/xxJZgQW?editors=0010) 

*(attach properties from one object to another)*

Student Task 2: [https://codepen.io/drupalastic/pen/XWBXZer?editors=0010](https://codepen.io/drupalastic/pen/XWBXZer?editors=0010) 

Student Task 3: [https://codepen.io/drupalastic/pen/XWBXpoz](https://codepen.io/drupalastic/pen/XWBXpoz) 

*(with arguments)*

### Version 1:

```jsx
let sharedIphone1Functionalities = {};

sharedIphone1Functionalities.dial = function(){
  console.log('tring.. tring...');
}

sharedIphone1Functionalities.sendMessage = function() {
  console.log('Sending message...');
}

sharedIphone1Functionalities.cameraClick = function() {
  console.log('Camera clicked')
}

function iPhone1(generation, ASIN, weight, OS, RAM, color, display, camera) {
  let obj = {};
  Object.setPrototypeOf(obj, sharedIphone1Functionalities);  
    
  obj.generation = generation;
  obj.asin = ASIN;
  obj.weight = weight;
  obj.os = OS;
  obj.ram = RAM;
  obj.color = color;
  obj.display = display;
  obj.camera = camera

  return obj;  
}

let i1 = iPhone1(1,'B09X67JBQV',7.8,'IOS', '128mb','Gray','90mm','2.0 MP');

// --------------------------------
// bluetooth feature added
// 3g Internet feature added
// high resolution capture added
// -------------------------------- 

let sharedIphone2Functionalities = {};
Object.setPrototypeOf(sharedIphone2Functionalities, sharedIphone1Functionalities)

sharedIphone2Functionalities.connectWithBlutoothDevice = function(){
  console.log('Connecting with bluetooth divice...')
}

sharedIphone2Functionalities.connectWithInternet = function(){
  console.log('Connecting with 3g Internet...')
}

sharedIphone2Functionalities.cameraClick = function(){
  console.log('Clicking a high resolution pic...')
}

function iPhone2(generation, ASIN, weight, OS, RAM, color, display, camera, bluetooth, internetType){
  let obj = {};
  Object.setPrototypeOf(obj, sharedIphone2Functionalities); 
    
  obj.generation = generation;
  obj.asin = ASIN;
  obj.weight = weight;
  obj.os = OS;
  obj.ram = RAM;
  obj.color = color;
  obj.display = display;
  obj.camera = camera;
    
  obj.bluetooth = bluetooth;
  obj.internet = internetType;

  return obj;  
}

let i2 = iPhone2(2,'B09dfgsgQV',9.8,'IOS 2', '256mb','Gray','99mm','4.0 MP', '2.0', '3g');
```

Possible improvements:

- use the built in `prototype` object of the function
- can you think of a way to copy all the properties from `iPhone1` to `iPhone2`

### Version 2. [using functions prototype object]

- attach iPhone1 methods to `iPhone1.prototype` object
- set prototype chain in between the newly created obj and the `iPhone1.prototype` object
- set prototype chain in between `iPhone2.prototype` and `iPhone1.prototype`
- attach iPhone2 methods to `iPhone2.prototype` object
- set prototype chain in between the newly created obj and the `iPhone2.prototype` object

```jsx
// just a made up example to demonstrate object creation & inheritance.

iPhone1.prototype.dial = function(){
  console.log('tring.. tring...');
}

iPhone1.prototype.sendMessage = function() {
  console.log('Sending message...');
}

iPhone1.prototype.cameraClick = function() {
  console.log('Camera clicked')
}

function iPhone1(generation, ASIN, weight, OS, RAM, color, display, camera) {
  let obj = {};
  Object.setPrototypeOf(obj, iPhone1.prototype);  
    
  obj.generation = generation;
  obj.asin = ASIN;
  obj.weight = weight;
  obj.os = OS;
  obj.ram = RAM;
  obj.color = color;
  obj.display = display;
  obj.camera = camera

  return obj;  
}

let i1 = iPhone1(1,'B09X67JBQV',7.8,'IOS', '128mb','Gray','90mm','2.0 MP');

// --------------------------------
// bluetooth feature added
// 3g Internet feature added
// high resolution capture added
// -------------------------------- 

Object.setPrototypeOf(iPhone2.prototype, iPhone1.prototype)

iPhone2.prototype.connectWithBlutoothDevice = function(){
  console.log('Connecting with bluetooth divice...')
}

iPhone2.prototype.connectWithInternet = function(){
  console.log('Connecting with 3g Internet...')
}

iPhone2.prototype.cameraClick = function(){
  console.log('Clicking a high resolution pic...')
}

function iPhone2(generation, ASIN, weight, OS, RAM, color, display, camera, bluetooth, internetType){
  let obj = {};
  Object.setPrototypeOf(obj, iPhone2.prototype); 
    
  obj.generation = generation;
  obj.asin = ASIN;
  obj.weight = weight;
  obj.os = OS;
  obj.ram = RAM;
  obj.color = color;
  obj.display = display;
  obj.camera = camera;
    
  obj.bluetooth = bluetooth;
  obj.internet = internetType;

  return obj;  
}

let i2 = iPhone2(2,'B09dfgsgQV',9.8,'IOS 2', '256mb','Gray','99mm','4.0 MP', '2.0', '3g');
```

### Version 2. [attaching properties in iPhone1 to iPhone2]

- pass an object as first argument to `iPhone1`
- attach all properties to that object
- pass an empty object while invoking iPhone1
- in iPhone2, immediately after creating obj, invoke iPhone1 with obj
- comment out or delete the Dirty code

```jsx
// just a made up example to demonstrate object creation & inheritance.

iPhone1.prototype.dial = function(){
  console.log('tring.. tring...');
}

iPhone1.prototype.sendMessage = function() {
  console.log('Sending message...');
}

iPhone1.prototype.cameraClick = function() {
  console.log('Camera clicked')
}

function iPhone1(o ,generation, ASIN, weight, OS, RAM, color, display, camera) {
  // student task: refactor using Object.create
  let obj = o;
  Object.setPrototypeOf(obj, iPhone1.prototype);  
    
  obj.generation = generation;
  obj.asin = ASIN;
  obj.weight = weight;
  obj.os = OS;
  obj.ram = RAM;
  obj.color = color;
  obj.display = display;
  obj.camera = camera

  return obj;  
}

let i1 = iPhone1({}, 1,'B09X67JBQV',7.8,'IOS', '128mb','Gray','90mm','2.0 MP');

// --------------------------------
// bluetooth feature added
// 3g Internet feature added
// high resolution capture added
// -------------------------------- 

Object.setPrototypeOf(iPhone2.prototype, iPhone1.prototype)

iPhone2.prototype.connectWithBlutoothDevice = function(){
  console.log('Connecting with bluetooth divice...')
}

iPhone2.prototype.connectWithInternet = function(){
  console.log('Connecting with 3g Internet...')
}

iPhone2.prototype.cameraClick = function(){
  console.log('Clicking a high resolution pic...')
}

function iPhone2(generation, ASIN, weight, OS, RAM, color, display, camera, bluetooth, internetType){
  let obj = {};
  iPhone1(obj, generation, ASIN, weight, OS, RAM, color, display, camera) 

  Object.setPrototypeOf(obj, iPhone2.prototype); 
        
  obj.bluetooth = bluetooth;
  obj.internet = internetType;

  return obj;  
}

let i2 = iPhone2(2,'B09dfgsgQV',9.8,'IOS 2', '256mb','Gray','99mm','4.0 MP', '2.0', '3g');
```

[assignment ](Prototypical%20inheritance%20using%20a%20factory%20function%20%20b20fe13d68e74b2f91b8e8900172c04b/assignment%20fd7468bd8a6f4f3eb745d0794651eb7e.md)