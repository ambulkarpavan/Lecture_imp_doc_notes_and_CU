# prototypical Inheritance using ES6 classes [120 min] (1)

Student task1: [solution](https://codepen.io/adarshakhatua/pen/yLGYLyx?editors=0010) 

Student task: [student tasks-1 es6 (codepen.io)](https://codepen.io/Adarsha-khatua/pen/yLQbaXr?editors=0010);

Class code : [ES6 class code (codepen.io)](https://codepen.io/Adarsha-khatua/pen/vYQmyjv?editors=0010);

- Quickly solve using constructor function: [https://codepen.io/drupalastic/pen/Baqjjwa?editors=0010](https://codepen.io/drupalastic/pen/Baqjjwa?editors=0010)
    - solution: [https://codepen.io/drupalastic/pen/poxggLR?editors=0012](https://codepen.io/drupalastic/pen/poxggLR?editors=0012)
- Discuss difference between attaching methods to `this` vs attaching methods to the functions prototype object
- convert the same problem into es6 classes syntax
    - Problem: [https://codepen.io/drupalastic/pen/OJBMMGy?editors=0012](https://codepen.io/drupalastic/pen/OJBMMGy?editors=0012)
        - solution
            
            ```jsx
            class Person {
              constructor(name, age) {
                this.name = name;
                this.age = age;
              }
            
              increaseAge() {
                this.age++;
              }
            
              sayName() {
                return `my name is ${this.name} & age is ${this.age}`;
              };
            }
            
            class Employee extends Person {
              constructor(name, age, salary) {
                super(name, age);
                this.salary = salary;
              }
            
              increaseSalary(amt) {
                this.salary += amt;
              }
            
              decreaseSalary(amt) {
                this.salary -= amt;
              }
            
              introduce() {
                return `my name is ${this.name}, I am ${this.age} years old & my salary is ${this.salary}`
              }
            }
            
            let e1 = new Employee('Chatur', 25, 100);
            console.log(e1)
            console.log(e1.sayName()) // my name is Chatur & age is 25
            e1.increaseAge()
            console.log(e1.sayName()) // my name is Chatur & age is 26
            
            console.log(e1.introduce());
            e1.decreaseSalary(20);
            console.log(e1.introduce());
            e1.increaseSalary(40);
            console.log(e1.introduce());
            ```
            

- Object creation - Student task 3 - ES6 classes [[problem](https://codepen.io/drupalastic/pen/YzjJodv?editors=0012)]
    - solution
        
        ```jsx
        // write a ES6 Class IPhone1 to create iPhone objects in bulk quantiy
        // iPhone1 takes in generation, ASIN, weight, OS, RAM, color, display, camera
        // the object it creates has the following
        // properties: generation, ASIN, weight, OS, RAM, color, display, camera
        // methods:
        // dial - console logs "tring.. tring..."
        // sendMessage - console logs "Sending message..."
        // cameraClick - "Camera clicked"
        // feel free to copy your constructor function solution and then make changes to them
        
        class IPhone1 {
          constructor(generation, ASIN, weight, OS, RAM, color, display, camera) {
            this.generation = generation;
            this.asin = ASIN;
            this.weight = weight;
            this.os = OS;
            this.ram = RAM;
            this.color = color;
            this.display = display;
            this.camera = camera;
          }
        
          dial() {
            console.log("tring.. tring...");
          }
        
          sendMessage() {
            console.log("Sending message...");
          }
        
          cameraClick() {
            console.log("Camera clicked");
          }
        }
        
        let i1 = new IPhone1(
          1,
          "B09X67JBQV",
          7.8,
          "IOS",
          "128mb",
          "Gray",
          "90mm",
          "2.0 MP"
        );
        
        i1.dial(); // "tring.. tring..."
        i1.sendMessage(); // "Sending message..."
        i1.cameraClick(); // "Camera clicked"
        ```
        

JavaScript ES6 classes provide a way to define objects with properties and methods. Classes are a syntactic sugar over JavaScript's existing prototype-based inheritance system, making it easier to write object-oriented code.

- Student task
    - Give a simple `class` task - for revision
    - Give a constructor function inheritance student task
- Convert it to `class`

Here's an example of a simple class in JavaScript:

```jsx
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  sayHello() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }
}

const john = new Person("John", 30);
john.sayHello(); // Hello, my name is John and I am 30 years old.
```

In the example above, we define a class called **`Person`** with a constructor method that takes two parameters: **`name`** and **`age`**. We also define a **`sayHello`** method that logs a message to the console. We then create a new instance of the **`Person`** class called **`john`** and call its **`sayHello`** method.

Here are some features of a class in JavaScript:

## Constructor Method

The constructor method is called when a new instance of the class is created. It's used to set the initial state of the object.

```jsx
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}
```

### **Properties**

Classes can have properties that are defined in the constructor method or outside of it.

```jsx
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  occupation = "Developer"; // Class property
}
```

### **Methods**

Classes can have methods that are defined inside the class body.

```jsx
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  sayHello() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }
}
```

## Inheritance Using ES6 Classes

```jsx
class Person {
  constructor(name){
    this.name = name;
  }

  sayHello() {
    console.log(this.name, 'says Hello');
  }
}

let person1 = new Person('Vivek');
person1.sayHello();

class Teacher extends Person{
  constructor(name, subject) {
    super(name);
    this.subject = subject;
  }

  teach() {
    console.log(this.name, 'is Teaching ', this.subject);
  }
}

let teacher1 = new Teacher('Akash', 'Science');
teacher1.sayHello();
teacher1.teach();
```

Under the hood exactly the same prototype chain is getting created: 

```jsx
console.log(teacher1);
console.log(teacher1.__proto__ === Teacher.prototype);
console.log(Teacher.prototype.__proto__ === Person.prototype);
```

## iPhone example using ES6 classes

*(copy paste code from constructor function to demo the similarities)*

```jsx
class IPhone1 {
    constructor(generation, ASIN, weight, OS, RAM, color, display, camera) {
      this.generation = generation;
      this.asin = ASIN;
      this.weight = weight;
      this.os = OS;
      this.ram = RAM;
      this.color = color;
      this.display = display;
      this.camera = camera;
    }

    dial() {
      console.log('tring.. tring...');
    }

    sendMessage() {
      console.log('Sending message...');
    }

    cameraClick() {
      console.log('Camera clicked')
    }
}

let i1 = new IPhone1(1,'B09X67JBQV',7.8,'IOS', '128mb','Gray','90mm','2.0 MP');

// --------------------------------
// bluetooth feature added
// 3g Internet feature added
// high resolution capture added
// -------------------------------- 

class IPhone2 extends IPhone1 {
    constructor(generation, ASIN, weight, OS, RAM, color, display, camera, bluetooth, internetType) {
      super(generation, ASIN, weight, OS, RAM, color, display, camera);
      this.bluetooth = '2.0';
      this.internet = '3g';
    }
    
    connectWithBlutoothDevice(){
      console.log('Connecting with bluetooth divice...')
    }
    
    connectWithInternet(){
      console.log('Connecting with 3g Internet...')
    }
    
    cameraClick(){
      console.log('Clicking a high resolution pic...')
    }
}

let i2 = new IPhone2();
```

## Summary: Classical vs Prototypical Inheritance

In Classical object-oriented programming, like in java & c++,  we have two constructs: **classes** and **objects**. **Classes** act as a blueprint (or a specification or a structure ) and **objects** are constructed using the structure provided by its Class. Inheritance in classical programming happens at the level of classes. Classes mostly cannot be modified at runtime.

Javascript internally does not have classes. Prototypical inheritance is all about objects **linked** to other objects. Instead of defining a structure through a class, In Javascript, you simply create an object. In order to access the properties and methods of another object, we simply need to set up a Proto-typical relationship of our object with that another object. Prototypical chains are very flexible and can be changed at runtime.

All the inheritance techniques of Javascript like 

- Object.create(),
- Object.setPrototypeOf(),
- the constructor functions (using the `new` keyword) and even
- the ES6 Classes

under the hood, they all do one thing, setting up of prototype chain.

# Miscellaneous

### **Static Methods**

Static methods are methods that are called on the class itself, rather than on an instance of the class.

```jsx
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  static greet() {
    console.log("Hello!");
  }
}

Person.greet(); // Hello!
```

### **Getters and Setters**

Getters and setters are special methods that allow you to access or modify the values of class properties.

```jsx
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
    this.salary = 5000;
  }

  // getter
  get fullName() {
    return `${this.name} Doe`;
  }

  // setter
  set fullName(name) {
    this.name = name.split(" ")[0];
  }
}

const john = new Person("John", 30);

// are we trying to get a value or set a value
console.log(john.fullName); // get

// are we trying to get a value or set a value
john.fullName = "Jane Smith"; // set

// get a value or are we trying to get a value
console.log(john.name);
```

In the example above, we define a **`fullName`** getter and setter that manipulate the **`name`** property.

### **Private Fields**

Private fields are class properties that are not accessible from outside the class.

```jsx
class Person {
  #age;

  constructor(name, age) {
    this.name = name;
    this.#age = age;
  }

  get age() {
    return this.#age;
  }
}

const john = new Person("John", 30);
console.log(john.age); // 30
console.log(john.#age); // SyntaxError: Private field '#age' must be declared in an enclosing class
```

In the example above, we define a private field called #age using the # symbol. We can only access the #age field through the age getter method.

Student task: [https://codepen.io/drupalastic/pen/WNgXVWJ?editors=0010](https://codepen.io/drupalastic/pen/WNgXVWJ?editors=0010) 

```jsx
// private property called balance
// public method called deposit(amount)
// public method called withdraw(amount)
// public method called displayBalance()
// on every deposit a private method called depositCharge() should be invoded which reduces the balance by 10

class Account {
  #balance;
  constructor(openingBalance) {
    this.#balance = openingBalance;
  } 

  #depositCharge() {
    this.#balance -=  10;
  }

  deposit(amount) {
    this.#balance += amount;
    this.#depositCharge();
  }

  withdraw(amount) {
    this.#balance -= amount;
  }

  displayBalance() {
    console.log(this.#balance)
  }
}

let a1 = new Account(5000)
a1.withdraw(1000)
a1.deposit(400)
a1.displayBalance();
```

**Getters and Setters with private fields**

Getters and setters are special methods that allow us to access and modify class properties.

```jsx
class Person {
  #age;

  constructor(name, age) {
    this.name = name;
    this.#age = age;
  }

  get age() {
    return this.#age;
  }

  set age(value) {
    if (value < 0) {
      throw new Error("Age must be a positive number");
    }
    this.#age = value;
  }
}

const john = new Person("John", 30);
console.log(john.age); // 30
john.age = 40;
console.log(john.age); // 40
john.age = -10; // Error: Age must be a positive number
```

In the example above, we define a getter method called age that returns the value of the private field #age, and a setter method called age that sets the value of #age if the value is greater than or equal to 0.

## Misc `class` concepts codepen:

- [https://codepen.io/drupalastic/pen/eYjbXew?editors=0012](https://codepen.io/drupalastic/pen/eYjbXew?editors=0012)
- [https://codepen.io/drupalastic/pen/MWBZxQd?editors=0011](https://codepen.io/drupalastic/pen/MWBZxQd?editors=0011)
- [https://codepen.io/drupalastic/pen/qByLvoN?editors=0012](https://codepen.io/drupalastic/pen/qByLvoN?editors=0012)
- [https://codepen.io/drupalastic/pen/poZqYKB?editors=0012](https://codepen.io/drupalastic/pen/poZqYKB?editors=0012)

## Optional:

## **The `constructor` property**

If the object is created using the `new` keyword, it returns the **constructor function** that was used to create the object. 

If the object was created using object literal, the default `Object()` that javascript uses to create objects is returned. The `Object()` is a built-in constructor function in javascript. 

Functions in javascript are `objects` built using the built-in `Function` constructor.  A function has methods and properties just like other `objects` in javascript.

In the above codepen, if I try to log `acc1.constructor` I'll get back something like this:

![Untitled](prototypical%20Inheritance%20using%20ES6%20classes%20%5B120%20mi%208939ac281f334a41959b93af5a233326/Untitled.png)

On the other hand, if I try to log the constructor property of an object literal I'll see something like this:

![Untitled](prototypical%20Inheritance%20using%20ES6%20classes%20%5B120%20mi%208939ac281f334a41959b93af5a233326/Untitled%201.png)

Every object has a constructor property and that references the function that was used to create that object.

## call(), apply() & bind()

**What is call() & apply() ?**

In Javascript `call()` & `apply()` executes the function and binds the `this` of the function to the first argument of the call().

**What is the difference between call() & apply();**

For arguments of the function, in `call()` we pass comma-separated values but in `apply()` we pass in an array of arguments.

**What is the difference between call/apply vs bind?**

in call/apply the this is bound and the function is **immediately called**. but in bind we bind the this keyword of the function and we get back a new function & it is not immediately executed.

Just like an object, a function in javascript has its properties and methods. Some of the common properties are `name`, `length`, `constructor` & Some common methods of a function are `call`, `bind`, `apply` etc.

Interesting fact: the constructor of a function is built in `Function()` constructor.

```jsx
function SayHello(favSubject, favFood) {
  console.log('Hello from ', this.name);
  console.log('I love ', favSubject, ' & ' , favFood);
}

SayHello.call({name: 'Vivek'}, 'Maths', 'Pizza');

SayHello.apply({name: 'Vivek'}, ['Maths', 'Pizza']);

const sayHelloToSwapnil =  SayHello.bind({name: 'Swapnil'});
sayHelloToSwapnil('Javascript', 'Sweets');
```

Use `.bind()` when you want that function to later be called with a certain context, useful in events. Use `.call()` or `.apply()` when you want to invoke the function immediately, and modify the context.

Call/apply call the function immediately, whereas `bind` returns a function that, when later executed, will have the correct context set for calling the original function.

**code-pen:** [https://codepen.io/drupalastic/pen/jOwBQgM?editors=0012](https://codepen.io/drupalastic/pen/jOwBQgM?editors=0012) 

Classnotes;

![Untitled](prototypical%20Inheritance%20using%20ES6%20classes%20%5B120%20mi%208939ac281f334a41959b93af5a233326/Untitled%202.png)

## Value vs Reference

**Value Types:** Number, String, Boolean, undefined, null, Symbol

**Reference Types:** Object, Function & Array

```jsx
let x = 10;
let y = x; // value copied by value

x = 20;

console.log('x: ', x); // 20
console.log('y: ', y); // 10

let a = {value: 10};
let b = a; // Object copied by reference

b.value = 20;

console.log('a: ', a); // {value: 20}
console.log('b: ', b); // {value: 20}
```

Primitives are copied by their value & Objects are copied by their reference.

**codepen:** [https://codepen.io/drupalastic/pen/KKqWbyX?editors=0012](https://codepen.io/drupalastic/pen/KKqWbyX?editors=0012)

## Methods of Object constructor function

`Object.keys` give us an array of all the properties of an object.

```jsx
console.log(Object.keys({x: 1, y:2})); // ["x","y"]
```

`Object.entries` gives us an array of key value array of an object

```jsx
console.log(Object.entries({x: 1, y:2})); 
//[['x', 1],['y', 2]]
```

Check if a property exists in an object using the `in` keyword

```jsx
if ('x' in {x: 1, y:2}) {
  console.log('yes x is a propery of the object')
}
```

Codepen: [https://codepen.io/drupalastic/pen/LYLWqGV?editors=0012](https://codepen.io/drupalastic/pen/LYLWqGV?editors=0012) 

`Object.assign` gives us a way to clone properties and members (properties & methods) of an object into another object.

```jsx
// Old way
// let clonedAccount = {};

// for (let key in account) {
//   clonedAccount[key] = account[key];
// }

// console.log(clonedAccount); // you may not see the method in codepen, open actual console.

let clonedAccount = Object.assign({}, account);
console.log(clonedAccount);
```

Cloning can also be done using the `...` spread operator:

```jsx
let clonedAccount = { ...account };
```

**codepen:** [https://codepen.io/drupalastic/pen/LYLWqGV?editors=0012](https://codepen.io/drupalastic/pen/LYLWqGV?editors=0012)

## Built-in Objects in Javascript

### Math

`Math` is a built-in object that has properties and methods for mathematical constants and functions. `Math` is not a constructor. All properties and methods of `Math` are static & we do not need to use the `new` keyword to use `Math`

```jsx
Math.floor( 45.95); //  45
console.log(Math.ceil(7.004)); // 8
console.log(Math.max(1, 3, 2)); // 3
console.log(Math.min(2, 3, 1)); // 1

function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1) + min); //The maximum is inclusive and the minimum is inclusive
}
```

Documentation: [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math) 

### String

The `String` object is used to represent and manipulate a sequence of characters. Strings can be created as primitives, from string literals, or as objects, using the `String()` **constructor**.

```jsx
const string1 = "A string primitive or literal";

const string4 = new String("A String object");
```

Javascript engine internally wraps a String primitive with a String object. String primitives and string objects can be used interchangeably in most situations.

 **Documentation:** [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) 

```jsx
string1.length;
string1[0];
string1.includes('or');
string1.startsWith('A string');
string1.endsWith('l');
string1.indexOf('or');
string1.replace('or','and');
string1.toUpperCase();
string1.toLowerCase();
string1.trim();
string1.split(' ');
```

Escape notation:

![Untitled](prototypical%20Inheritance%20using%20ES6%20classes%20%5B120%20mi%208939ac281f334a41959b93af5a233326/Untitled%203.png)

**Template literals:**

Benefits: Easy to add line breaks, single and double quotes, placeholders

```jsx
let name = "Vivek";
let balance = 100000;

// console.log('Hello \'Vivek\' \n' + 
//              'Your Balance is 100000'
//            );

console.log('Hello \'' + name +  '\' \n' + 
'Your Balance is ' + balance + '.');

console.log(`Hello '${name}'
Your Balance is ${balance}.`);
```

**codepen:** [https://codepen.io/drupalastic/pen/dyRvEOM?editors=0012](https://codepen.io/drupalastic/pen/dyRvEOM?editors=0012) 

### Date constructor

**MDN Date Documentation:** [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) 

**MDN Date constructor documentation:** [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date) 

**CSS Tricks:** [https://css-tricks.com/everything-you-need-to-know-about-date-in-javascript/](https://css-tricks.com/everything-you-need-to-know-about-date-in-javascript/)

**codepen:**  [https://codepen.io/drupalastic/pen/MWopNbE?editors=0012](https://codepen.io/drupalastic/pen/MWopNbE?editors=0012)

## Objects exercises

- logging all key,values of an object: [https://codepen.io/drupalastic/pen/rNwmNLe?editors=0012](https://codepen.io/drupalastic/pen/rNwmNLe?editors=0012)
- practice creating an object using Factory Function
- practice creating an object using Constructor Function

## Property descriptors

There' an another, advanced way to add members to an object using `Object.defineProperty`

`Object.defineProperty` takes in the `object` as the first argument, the member name as the second argument and an object of **Property descriptors** as the third argument.

By member we mean either property or method.

```jsx
let user = {
  name: 'Vivek',
  sayName: function () { console.log(greeting, "I'm " + this.name); },
}

Object.defineProperty(user, 'age', {
  writable: true, // we can change it
  enumerable: true, // it will showup in the for in loop & Object.keys
  configurable: true, // we can delete the age property
  value: 30
})

// the  default value for all three are true.

// we'll able to delete it only if the configurable is set to true
// delete user.age;

// we'll be albe to update it only if writable is true
// user.age = 40;

// it will be shown in Object.entries/keys or for .. in loop only it enumerable is true
console.log(Object.entries(user));
console.log(Object.keys(user));

for (let key in user) {
  console.log(key);
}
```

## Own vs Prototype members & `hasOwnProperty()`

```jsx
function User(name, age) {
  // own members
  this.name = name;
  this.age = age;
  this.sayName = function () { console.log("I'm " + this.name); };
}

// prototype member
User.prototype.sayAge = function () { console.log("My age is " + this.age); };

let user = new User('Vivek', 30);

// Only the own members will be shown in Object.entries/keys
console.log(Object.entries(user));
console.log(Object.keys(user));

// both own and prototype members are shown in for .. in loop 
for (let key in user) {
  console.log(key);
}

// we can use the hasOwnProperty() to check if the property is its own
console.log(user.hasOwnProperty('sayName')); // true
console.log(user.hasOwnProperty('sayAge')); // false
```

## Teaching with iPhone example

## Simple example Factory [v1]

```jsx
// manufacturing iphone1's in bulk quantity
// factory function to generate iPhone1

let sharedIphone1Functionalities = {};
sharedIphone1Functionalities.dial = function() {
  console.log('tring... tring...');
}

function iPhone1(generation, color) {
  let obj = {};
  Object.setPrototypeOf(obj, sharedIphone1Functionalities);

  obj.generation = generation;
  obj.color = color;

  return obj;
}

let i1 = iPhone1(1, 'grey');

// iphone 2 was released.
// every thing else were same. 
// property = blueTooth
// method = connectToABlueToothDevice

let sharedIphone2Functionalities = {};
sharedIphone2Functionalities.connectToABlueToothDevice = function() {
  console.log('Connected to the BT device.')
}

Object.setPrototypeOf(sharedIphone2Functionalities, sharedIphone1Functionalities);

function iPhone2(generation, color, bluetoothType) {
  let obj = {};
  Object.setPrototypeOf(obj, sharedIphone2Functionalities);

  obj.generation = generation;
  obj.color = color;
  obj.bluetoothType = bluetoothType;

  return obj;
}

let i2 = iPhone2(2, 'black', 'BT 5.0');
```

## [v2]

```jsx
// manufacturing iphone1's in bulk quantity
// factory function to generate iPhone1

iPhone1.prototype.dial = function() {
  console.log('tring... tring...');
}

function iPhone1(generation, color) {
  let obj = {};
  Object.setPrototypeOf(obj, iPhone1.prototype);

  obj.generation = generation;
  obj.color = color;

  return obj;
}

let i1 = iPhone1(1, 'grey');

// iphone 2 was released.
// every thing else were same. 
// property = blueTooth
// method = connectToABlueToothDevice

Object.setPrototypeOf(iPhone2.prototype, iPhone1.prototype);

iPhone2.prototype.connectToABlueToothDevice = function() {
  console.log('Connected to the BT device.')
}

function iPhone2(generation, color, bluetoothType) {
  let obj = {};
  Object.setPrototypeOf(obj, iPhone2.prototype);

  obj.generation = generation;
  obj.color = color;
  obj.bluetoothType = bluetoothType;

  return obj;
}

let i2 = iPhone2(2, 'black', 'BT 5.0');
```

## [v3]

```jsx
iPhone1.prototype.dial = function() {
  console.log('tring... tring...');
}

function iPhone1(o, generation, color) {
  let obj = o;
  Object.setPrototypeOf(obj, iPhone1.prototype);

  obj.generation = generation;
  obj.color = color;

  return obj;
}

let i1 = iPhone1({} ,1, 'grey');

// iphone 2 was released.
// every thing else were same. 
// property = blueTooth
// method = connectToABlueToothDevice

Object.setPrototypeOf(iPhone2.prototype, iPhone1.prototype);

iPhone2.prototype.connectToABlueToothDevice = function() {
  console.log('Connected to the BT device.')
}

function iPhone2(generation, color, bluetoothType) {
  let obj = {};

  iPhone1(obj, generation, color);

  Object.setPrototypeOf(obj, iPhone2.prototype);

  // obj.generation = generation;
  // obj.color = color;

  obj.bluetoothType = bluetoothType;

  return obj;
}

let i2 = iPhone2(2, 'black', 'BT 5.0');
```

## Simple iPhone constructor function [L2]

```jsx
IPhone1.prototype.dial = function() {
  console.log('tring... tring...');
}

function IPhone1(generation, color) {
  // let this = {}; #1
  // Object.setPrototypeOf(this, iPhone1.prototype); #3

  this.generation = generation;
  this.color = color;

  // return this; #2
}

let i1 = new IPhone1(1, 'grey');

Object.setPrototypeOf(IPhone2.prototype, IPhone1.prototype);

IPhone2.prototype.connectToABlueToothDevice = function() {
  console.log('Connected to the BT device.')
}

function IPhone2(generation, color, bluetoothType) {
  // let this = {}; #1
  // Object.setPrototypeOf(this, iPhone2.prototype); #3

  this.generation = generation;
  this.color = color;
  this.bluetoothType = bluetoothType;

  // return this; #2
}

let i2 = new IPhone2(2, 'black', 'BT 5.0');

// Any function that is intended to be called 
// with the `new` keyword is
// called a constructor function
```

Student task: [https://codepen.io/drupalastic/pen/WNKwbYO?editors=0012](https://codepen.io/drupalastic/pen/WNKwbYO?editors=0012) 

Student task: [https://codepen.io/drupalastic/pen/JjBXoba?editors=0010](https://codepen.io/drupalastic/pen/JjBXoba?editors=0010) [problem]

## Constructor function L3

```jsx
IPhone1.prototype.dial = function() {
  console.log('tring... tring...');
}

function IPhone1(generation, color) {
  // let this = {}; #1
  // Object.setPrototypeOf(this, iPhone1.prototype); #3

  this.generation = generation;
  this.color = color;

  // return this; #2
}

let i1 = new IPhone1(1, 'grey');

Object.setPrototypeOf(IPhone2.prototype, IPhone1.prototype);

IPhone2.prototype.connectToABlueToothDevice = function() {
  console.log('Connected to the BT device.')
}

function IPhone2(generation, color, bluetoothType) {
  // let this = {}; #1
  // Object.setPrototypeOf(this, iPhone2.prototype); #3

  // Fact 1. when invoking IPhone1, generation & color property will be attached to the this object.
  // Fact 2. when you invoke a function with the call(), you have power to send/set `this` object withing the function you are invoking.

  IPhone1.call(this, generation, color);

  // this.generation = generation;
  // this.color = color;

  this.bluetoothType = bluetoothType;

  // return this; #2
}

let i2 = new IPhone2(2, 'black', 'BT 5.0');

// Any function that is intended to be called 
// with the `new` keyword is
// called a constructor function
// convention - not a rule
```

[https://codepen.io/drupalastic/pen/WNKwbJj?editors=0012](https://codepen.io/drupalastic/pen/WNKwbJj?editors=0012) 

## ES6 Classes

```jsx
// ES6 classes
class IPhone1 {
  constructor(generation, color) {
    this.generation = generation;
    this.color = color;
  }

  dial() {
    console.log('tring... tring...')
  }
}

let i1 = new IPhone1(1, 'grey');

class IPhone2 extends IPhone1 {
  constructor(generation, color, bluetoothType) {
    super(generation, color);
    this.bluetoothType = bluetoothType;
  }

  connectToABlueToothDevice() {
    console.log('Connected to the BT device.')
  }

  connectToWifi() {
    console.log('Connected to the Wifi device.')
  }
}

let i2 = new IPhone2(2, 'black', 'BT 5.0');

// using es6 class syntax,
// create a class IPhone3 - should extend everything from iPhone1 & 2
// new property = siri <boolean> true
// function = respondToHeySiri() <log "Siri: how can I help you?">
```

Student task: [https://codepen.io/drupalastic/pen/OJwNVym?editors=0010](https://codepen.io/drupalastic/pen/OJwNVym?editors=0010)

![Untitled](prototypical%20Inheritance%20using%20ES6%20classes%20%5B120%20mi%208939ac281f334a41959b93af5a233326/Untitled%204.png)

## B24

```jsx
class Person {
  constructor(firstName, lastName, age) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
  }

  sleep() {
    console.log(`${this.firstName} is sleeping.`)
  }

  eat() {
    console.log(`${this.firstName} is eating.`)
  } 

  increaseAge() {
    this.age = this.age + 1;
    console.log(this.age);
  }

  introduceSelf() {
    console.log(this.firstName, this.lastName, this.age);
  }
}

class Employee extends Person {
  constructor(firstName, lastName, age, department, salary) {
    // Person.call(this,firstName, lastName, age)
    super(firstName, lastName, age)
    this.department = department;
    this.salary = salary;
  }

  work() {
    console.log(`${this.firstName} is working.`)
  }

  getSalary() {
    console.log(`${this.firstName} is getting Salary.`)
  }
}

let e1 = new Employee("John", "Doe", 25, "frontend", 200000);
console.log(e1);
e1.eat();
```

## Student task: [Implement 3 levels of inheritance using es6 classes]

[https://codepen.io/drupalastic/pen/jOvajYr?editors=0010](https://codepen.io/drupalastic/pen/jOvajYr?editors=0010) 

```jsx
class Creature {
  constructor(name) {
    this.name = name;
  }
  
  eat() {
    console.log(`${this.name} is eating...`);
  }
}

class Humans extends Creature {
  constructor(name) {
    super(name);
  }
  sleep() {
    console.log(`${this.name} is sleeping...`);
  }
}

class Employees extends Humans {
  constructor(name, salary) {
    super(name);
    this.salary = salary;
  }

  ChangeSalary(value) {
    this.salary = value;
  }

  displaySalary() {
    console.log(`${this.name}'s salary is    ${this.salary}`);
  }
}

let e1 = new Employees("Vivek", "500");
console.log(e1)
e1.displaySalary();
e1.ChangeSalary(1000);
e1.displaySalary();
```

[assignment ](prototypical%20Inheritance%20using%20ES6%20classes%20%5B120%20mi%208939ac281f334a41959b93af5a233326/assignment%202f7ce7dc6b4540eaa0778783a0fdad24.md)