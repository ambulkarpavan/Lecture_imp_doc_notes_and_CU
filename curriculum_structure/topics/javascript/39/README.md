# prototypical inheritance using a constructor function [120 min] (1)

## Random topics (which will be useful when we learn the inheritance using `new`)

## Understanding & using `.call()`

```jsx
function f1(a) {
  // trying to access property name in `this`
  console.log(this.name)

  // trying to attach `age` property to `this`
  this.age = a;
}

// how can you invoke f1() in a way that you can set 
// where this points to within the `f1`?
```

By default the `this` keyword in javascript points to the global `window` object. But there are many ways to tell javascript, where `this` should point to, and of of them is invoking the function that uses `this` with the `call`() method.

The `call()` method calls the function with a given this value and arguments provided individually.

The syntax of the `call()` method is:

```
func.call(thisArg, arg1, ... argN)
```

- `thisArg` - The `thisArg` is the object that the `this` object should reference inside the function `func`.
- `arg1, ... argN` (optional) - Arguments for the function `func`.

![Untitled](prototypical%20inheritance%20using%20a%20constructor%20funct%20a3604d31b48d471db220b296ced56888/Untitled.png)

**Problem:** 

What magic does the `new` keyword do? Convert the following factory function to a constructor function that is intended to be called with the `new` keyword?

[https://codepen.io/drupalastic/pen/KKxmqvG?editors=0012](https://codepen.io/drupalastic/pen/KKxmqvG?editors=0012) [problem]

- Solution
    
    ```jsx
    
    ```
    

## Function attaching properties to an object

**Guess the output?**

```jsx
function f1(o, name, age) {
  o.name = name;
  o.age = age;
}

function f2(name, age) {
  let obj = {subject: 'Javascript'}

  f1(obj, name, age)

  return obj;
}

let c = f2("chatur", 20);
console.log(c)
```

- Answer
    
    ```jsx
    // expected cosole log:
    // {
    //   "subject": "Javascript",
    //   "name": "chatur",
    //   "age": 20
    // }
    ```
    

**Problem :** 

[https://codepen.io/drupalastic/pen/qBJOmKO?editors=0010](https://codepen.io/drupalastic/pen/qBJOmKO?editors=0010) [a function attaching properties to an object]

**Problem** : [https://codepen.io/drupalastic/pen/BaOmLBQ?editors=0012](https://codepen.io/drupalastic/pen/BaOmLBQ?editors=0012) [a function attaching properties to `this` using `.call`]

- Solution
    
    ```jsx
    function f1(name, age) {
      this.name = name;
      this.age = age;
    }
    
    function f2(n, a) {
      // hint: we are invoking f2 with the new keyword
      // attach name & age to this without changing anything in f1
      // use .call
      f1.call(this, n,a);
    }
    
    let j = new f2('John', 20);
    console.log(j)
    ```
    

- Identify all the prototype chains in the example
    - code
        
        ```jsx
        iPhone1.prototype.dial = function(){
          console.log('tring.. tring...');
        }
        
        iPhone1.prototype.sendMessage = function() {
          console.log('Sending message...');
        }
        
        iPhone1.prototype.cameraClick = function() {
          console.log('Camera clicked')
        }
        
        // factory function to create iPhone1
        function iPhone1(ASIN, RAM, color) {
          let obj = {};
          Object.setPrototypeOf(obj, iPhone1.prototype);
        
          obj.asin = ASIN;
          obj.ram = RAM;
          obj.color = color;
          
          return obj;  
        }
        
        // factory function to create iPhone2
        Object.setPrototypeOf(iPhone2.prototype, iPhone1.prototype);
        
        iPhone2.prototype.connectToBT = function() {
          console.log('Bluetooh connected')
        }
        
        iPhone2.prototype.disConnectFromBT = function() {
          console.log('Bluetooh disconnected')
        }
        
        function iPhone2(ASIN, RAM, color, bluetooth) {
          let obj = iPhone1(ASIN,RAM, color )
        
          Object.setPrototypeOf(obj, iPhone2.prototype)
          obj.bluetooth = bluetooth;
        
          return obj;
        }
        
        let i1 = iPhone2(1,'128mb','Gray', '1.4');
        ```
        
- Start with a factory function, discuss what changes if the `new` keyword in used, solve one of the same inheritance problem with the `new` keyword (Constructor functions)
    - code
        
        ```jsx
        iPhone1.prototype.dial = function(){
          console.log('tring.. tring...');
        }
        
        iPhone1.prototype.sendMessage = function() {
          console.log('Sending message...');
        }
        
        iPhone1.prototype.cameraClick = function() {
          console.log('Camera clicked')
        }
        
        // factory function to create iPhone1
        function iPhone1(ASIN, RAM, color) {
          let obj = {};
          Object.setPrototypeOf(obj, iPhone1.prototype);
        
          obj.asin = ASIN;
          obj.ram = RAM;
          obj.color = color;
          
          return obj;  
        }
        
        // factory function to create iPhone2
        Object.setPrototypeOf(iPhone2.prototype, iPhone1.prototype);
        
        iPhone2.prototype.connectToBT = function() {
          console.log('Bluetooh connected')
        }
        
        iPhone2.prototype.disConnectFromBT = function() {
          console.log('Bluetooh disconnected')
        }
        
        function iPhone2(ASIN, RAM, color, bluetooth) {
          let obj = iPhone1(ASIN,RAM, color )
        
          Object.setPrototypeOf(obj, iPhone2.prototype)
          obj.bluetooth = bluetooth;
        
          return obj;
        }
        
        let i1 = iPhone2(1,'128mb','Gray', '1.4');
        ```
        
- Solve the exact problem using the constructor function
    - solution
        
        ```jsx
        // write a constructor function IPhone1 to create iPhone objects in bulk quantiy
        // iPhone1 takes in generation, ASIN, weight, OS, RAM, color, display, camera
        // the object it creates has the following 
        // properties: generation, ASIN, weight, OS, RAM, color, display, camera
        // methods: 
        // dial - console logs "tring.. tring..."
        // sendMessage - console logs "Sending message..."
        // cameraClick - "Camera clicked"
        // feel free to copy your factory function solution and then make changes to them
        
        function IPhone1(generation, ASIN, weight, OS, RAM, color, display, camera) {   
          this.generation = generation;
          this.asin = ASIN;
          this.weight = weight;
          this.os = OS;
          this.ram = RAM;
          this.color = color;
          this.display = display;
          this.camera = camera
          
          this.dial = function(){
            console.log('tring.. tring...');
          }
          
          this.sendMessage = function() {
            console.log('Sending message...');
          }
          
          this.cameraClick = function() {
            console.log('Camera clicked')
          } 
        }
        
        let i1 = new IPhone1(1,'B09X67JBQV',7.8,'IOS', '128mb','Gray','90mm','2.0 MP')
        i1.dial(); // "tring.. tring..."
        i1.sendMessage(); // "Sending message..."
        i1.cameraClick(); // "Camera clicked"
        ```
        

## Revise inheritance using factory function to begin with

**Problem**: Implement the following hierarchy with factory functions. The methods like `eat()` & `meow()` should remain in the prototype chain and should not be copied to each object.

```jsx
Animal
    ├── noOfLegs <number>
    ├── vegetarian <boolean>
    └── eat() <function that logs `eating...` >

Cat extends all properties and methods of an Animal
    ├── color <string>
    └── meow() <function that logs `meowing...`>
```

## Solve the above problem

- solution
    
    ```jsx
    animal.prototype.eat = function() {
      console.log(`eating...`)
    }
    
    function animal(noOfLegs, vegetarian) {
      let obj = {};
      Object.setPrototypeOf(obj, animal.prototype)
    
      obj.noOfLegs = noOfLegs;
      obj.vegetarian = vegetarian;
    
      return obj;
    }
    
    Object.setPrototypeOf(cat.prototype, animal.prototype)
    
    cat.prototype.meow = function() {
      console.log('Meow....')
    }
    
    function cat(noOfLegs, vegetarian, color) {
      let obj = animal(noOfLegs, vegetarian);
      Object.setPrototypeOf(obj, cat.prototype);
    
      obj.color = color;
    
      return obj;
    }
    
    let c1 = cat(4, false, 'Black');
    
    console.log(c1)
    
    c1.meow()
    c1.eat()
    ```
    

## Convert the above problem using constructor function

```jsx
// Convert this factory function to a constructor function
// convention: PascalCase

Animal.prototype.eat = function() {
  console.log(`eating...`)
}

function Animal(noOfLegs, vegetarian) {
  // let this = {}; # 1
  // Object.setPrototypeOf(obj, Animal.prototype) #3

  this.noOfLegs = noOfLegs;
  this.vegetarian = vegetarian;

  // return this; #2
}

let a1 = new Animal(4, true);
console.log(a1);
a1.eat();

Object.setPrototypeOf(Cat.prototype, Animal.prototype)

Cat.prototype.meow = function() {
  console.log('Meow....')
}

function Cat(noOfLegs, vegetarian, color) {
  // #1. a this obj was created 
  // #3. a prototype chain was created between the new obj and the functions
  // prototype object
  Animal.call(this, noOfLegs, vegetarian)
  this.color = color;
  // #2. the this obj was returned
}

let c1 = new Cat(4, false, 'Brown');
console.log(c1);
c1.eat();
c1.meow();
```

## Transform Factory function to Constructor Function

```jsx
// Factory function
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

**Problem:** [https://codepen.io/drupalastic/pen/qBMVaRW?editors=0010](https://codepen.io/drupalastic/pen/qBMVaRW?editors=0010) 

- Solution
    
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
      this.firstName = firstName;
      this.lastName = lastName;
      this.age = age;
    }
    
    Object.setPrototypeOf(Employee.prototype, Person.prototype)
    
    Employee.prototype.work = function() {
      console.log(`${this.firstName} is working.`)
    }
    
    Employee.prototype.getSalary = function() {
      console.log(`${this.firstName} is getting Salary.`)
    }
    
    function Employee(firstName, lastName, age, department, salary) {
      Person.call(this,firstName, lastName, age);
      this.department = department;
      this.salary = salary;
    }
    
    let e1 = new Employee("John", "Doe", 25, "frontend", 200000);
    console.log(e1);
    e1.eat();
    ```
    

**A complete inheritance example using constructor function:**

```jsx
function Person(name) {
  this.name = name;
};

Person.prototype.sayHello = function () {
  console.log(this.name, ' hello!');
}

let p1 = new Person('Vivek');
p1.sayHello();

function Teacher(name, subject) {
  // we know that Teacher will be called with the new keyword
  // so assume it already has an empty object called `this` which will be 
  // returned at the end of the function

  // the objects created with the Teacher function must 
  // have a property called `subject`
  this.subject = subject;

  // notice that we are not calling Person() with the new keyword
  // we are using it as a simple function
  // Using call, we are passing it our new `this` object and
  // the `Person()` function will stick the `name` property to `this` object
  Person.call(this, name);

  // a new object with `subject` and `name` poperty will be returned
  // if the `Teacher()` function is called using the `new` keyword
}

// linking the prototype of Teacher to Person so that the 
// teacher has access to all the methods of a Person
Object.setPrototypeOf(Teacher.prototype, Person.prototype);

// Adding more methods to the `prototype` property of `Teacher()`
// all teachers need to teach. 
Teacher.prototype.teach = function () {
  console.log(this.name, 'Teaching');
}

// creating a new teacher
let t1 = new Teacher('Monika', 'Glopo');
t1.sayHello()
t1.teach()

console.log(t1);

// teacher object's `__proto__` should be linked to `Teacher.prototype`
console.log(t1.__proto__ === Teacher.prototype);

// teacher's constructor should be Teacher()
console.dir(t1.constructor);

// Teacher.prototype's __proto should be linked to Person.prototype
console.log(Teacher.prototype.__proto__ === Person.prototype);
```

![Untitled](prototypical%20inheritance%20using%20a%20constructor%20funct%20a3604d31b48d471db220b296ced56888/Untitled%201.png)

MDN Inheritance example using constructor functions: [https://github.com/mdn/learning-area/blob/master/javascript/oojs/advanced/oojs-class-inheritance-student.html](https://github.com/mdn/learning-area/blob/master/javascript/oojs/advanced/oojs-class-inheritance-student.html) 

One more thing to remember about the constructor functions is that we assume that they are going to be called with the `new` keyword. What the `new` keyword does is, that it provides us a local variable called `this` . `this` is an empty Javascript object to begin with. The `__proto__` of `this` is linked to the `prototype` of the constructor function constructing it. Finally, if nothing is returned, the `this` object is implicitly returned.  This is internally how JS constructs and returns an object when called with the `new` keyword.

The objects created using this function with the `new` keyword is linked to this `prototype` property via the objects `__proto__` property.

![Untitled](prototypical%20inheritance%20using%20a%20constructor%20funct%20a3604d31b48d471db220b296ced56888/Untitled%202.png)

 In other words, a functions `prototype` is what gets linked to the  `__proto__` value object when the `new` keyword is used against the function.

Please note that when we create a new object, say `emp1`, using `Employee()`, we will expect `emp1.constructor` to point to the `Employee()` function.  

`emp1` Object by itself does not have any `constructor` property. Because of prototypical lookup, it will try to find it in `Employee.prototype`, which does have a `constructor` property. So, it's almost always a good idea to ensure that a function's `prototype.constructor` should point back to the function itself.

Let's take the example of a built-in constructor function `Array()` before we move ahead and create our own constructor functions.

![Untitled](prototypical%20inheritance%20using%20a%20constructor%20funct%20a3604d31b48d471db220b296ced56888/Untitled%203.png)

Lets create an array in Javascript.

```jsx
let arr = new Array(); // equivalent to let arr = []
```

The `__proto__` property of the newly created `arr` is lined to `Array.prototype`. This can be verified: 

```jsx
console.log(arr.__proto__ === Array.prototype);
```

`arr.constructor` , by the means of prototypical lookup, points at the `Array()` function. Which makes sense.

### student tasks to copy properties when invoked with the this keyword

problem: [https://codepen.io/drupalastic/pen/wvxQvoY?editors=0011](https://codepen.io/drupalastic/pen/wvxQvoY?editors=0011) 

solution: [https://codepen.io/drupalastic/pen/QWBJWre?editors=0012](https://codepen.io/drupalastic/pen/QWBJWre?editors=0012) 

# Miscellaneous

### **Static Methods in Constructor Functions**

In constructor functions, static methods can be defined as properties of the constructor function itself, rather than on the prototype object.

```jsx
function Calculator() {}

Calculator.add = function(a, b) {
  return a + b;
};

Calculator.subtract = function(a, b) {
  return a - b;
};

console.log(Calculator.add(2, 3)); // 5
console.log(Calculator.subtract(5, 3)); // 2
```

In the example above, we define two static methods, add() and subtract(), as properties of the Calculator constructor function.

### **Private Members in Constructor Functions [Optional]**

In constructor functions, private members can be implemented using closure, where a function that creates the object returns an object that has access to variables in the outer function.

```jsx
function Person(name, age) {
  let _age = age;

  return {
    get name() {
      return name;
    },

    get age() {
      return _age;
    },

    set age(value) {
      if (value < 0) {
        throw new Error("Age must be a positive number");
      }
      _age = value;
    },
  };
}

const john = Person("John", 30);
console.log(john.name); // John
console.log(john.age); // 30
john.age = 40;
console.log(john.age); // 40
john.age = -10; // Error: Age must be a positive number
```

In the example above, we define a Person() constructor function that returns an object with getter and setter methods for name and _age. The variable _age is defined in the outer function, and is accessible only to the getter and setter methods of the returned object.

## iPhone example with Constructor Function

```jsx
// just a made up example to demonstrate object creation & inheritance.

function IPhone1(generation, ASIN, weight, OS, RAM, color, display, camera) {
  this.generation = generation;
  this.asin = ASIN;
  this.weight = weight;
  this.os = OS;
  this.ram = RAM;
  this.color = color;
  this.display = display;
  this.camera = camera;
}

IPhone1.prototype.dial = function(){
  console.log('tring.. tring...');
}

IPhone1.prototype.sendMessage = function() {
  console.log('Sending message...');
}

IPhone1.prototype.cameraClick = function() {
  console.log('Camera clicked')
}

let i1 = new IPhone1(1,'B09X67JBQV',7.8,'IOS', '128mb','Gray','90mm','2.0 MP');

// --------------------------------
// bluetooth feature added
// 3g Internet feature added
// high resolution capture added
// -------------------------------- 
function IPhone2(generation, ASIN, weight, OS, RAM, color, display, camera, bluetooth, internetType){
  IPhone1.call(this,generation,ASIN,weight,OS, RAM,color,display,camera);
  this.bluetooth = bluetooth;
  this.internet = internetType;
}

IPhone2.prototype.connectWithBlutoothDevice = function(){
  console.log('Connecting with bluetooth divice...')
}

IPhone2.prototype.connectWithInternet = function(){
  console.log('Connecting with 3g Internet...')
}

IPhone2.prototype.cameraClick = function(){
  console.log('Clicking a high resolution pic...')
}

Object.setPrototypeOf(IPhone2.prototype, IPhone1.prototype);

let i2 = new IPhone2(2,'B09X67JBQw',8.8,'IOS 2', '256mb','Black','100mm','4.0 MP','2.0', '3g');
```

[assignment ](prototypical%20inheritance%20using%20a%20constructor%20funct%20a3604d31b48d471db220b296ced56888/assignment%207d7e4212a658401597f6c10ea84d7164.md)