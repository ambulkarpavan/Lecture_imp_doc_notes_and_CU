# Mastering “this” keyword [120 min] (1)

- Mastering the this keyword - WHY
    - Regular vs Arrow functions
    - Mastering the `this` keyword

## Master the `this` keyword

The following are commonly asked Javascript interview questions. Please attempt to identify where the `this` keyword points in the following examples:

- **These questions are commonly asked in tech interviews**
    - Job Interview Challenge #1
        
        ```jsx
        function sayGoodbye() {
          console.log("Good bye! ", this);
        }
        
        function sayHello() {
          console.log("Helloo! ", this);
          sayGoodbye();
        }
        
        sayHello();
        
        ```
        
    - Job Interview Challenge #2
        
        ```jsx
        function sayHello() {
          console.log("Hello! from ", this.name);
        }
        
        var john = {
          name: "John Doe",
          age: 30,
          sayName: function () {
            // this.age = 35;
            console.log("My name is ", this.name);
          },
          sayHello: sayHello
        };
        
        var james = {
          name: "James Bond",
          age: 27,
          sayName: function () {
            console.log("My name is ", this.name);
          },
          sayHello: sayHello
        };
        
        john.sayName();
        john.sayHello();
        
        james.sayName();
        james.sayHello();
        
        ```
        
    - Job Interview Challenge #3
        
        ```jsx
        function sayHello() {
          console.log("Hello! ", this);
        }
        
        var john = {
          name: "John Doe",
          age: 30
        };
        
        var james = {
          name: "James Bond",
          age: 30
        };
        
        sayHello.call(james);
        sayHello.call(john);
        
        ```
        
    - Job Interview Challenge #4
        
        ```jsx
        var sayArrowHello = () => {
          console.log("Arrow Hello ", this);
        };
        
        sayArrowHello();
        
        function sayRegularHello() {
          console.log("Regular Hello ", this);
        }
        
        sayRegularHello();
        
        ```
        
    - Job Interview Challenge #5
        
        ```jsx
        var john = { name: "John Doe", age: 25 };
        
        var sayArrowHello = () => {
          console.log("Arrow Hello ", this);
        };
        
        function sayRegularHello() {
          console.log("Regular Hello ", this);
        }
        
        function sayRegularName() {
          console.log("My Regular name is ", this.name, this);
          sayRegularHello();
          sayArrowHello();
          var sayArrowGoodBye = () => {
            console.log("Arrow GoodBye ", this);
          };
          sayArrowGoodBye();
        }
        
        sayRegularName.call(john);
        
        ```
        

## Understand Regular function vs Arrow function

### Regular functions:

```jsx
//function declaration
function myDelaredFunction(number) {
  return number * 2;
}

//function expression
var myExpressionFunction = function (number) {
  return number * 2;
};

console.log(myDelaredFunction(3));
console.log(myExpressionFunction(5));

```

### Arrow functions:

```jsx
var myArrowFunction = (number) => number * 2;

console.log(myArrowFunction(10));

```

## understand `Call`, `Apply` vs `Bind`

```jsx
// call, apply & bind 
// .call & .apply are used to invoke a function & set the value of the this keyword 
// inside of the function

// .bind is used to create a function & set the value of the this keyword 
// inside of the newly created function

function greet(greeting, year, receiver) {
  return `${greeting} ${year} to ${receiver} from ${this.name}.`
}

// while invoking greet() we need to set the value of this keyword inside 
// of the greet function

// .call()
// takes in the value of this keyword as the first argument
// rest of the arguments to the function can be sent as comma separated values
// let g =  greet.call({name: 'Vivek'}, 'Happy new year', '2023', 'JS201 Batch')

// .apply()
// takes in the value of this keyword as the first argument
// rest of the arguments to the function can be sent a an array of values

// let args = [];
// args.push('Happy new year');
// args.push('2023');
// args.push('JS201 Batch');

// let g =  greet.apply({name: 'Vivek'}, args)

// .bind()
// bind gives you a new function 
// in which the this keyword is pre-set for you
// let greetFromVivek = greet.bind({name: 'Vivek'});
// let g = greetFromVivek('Happy new year', '2023', 'JS201 Batch')

console.log(g)
```

## Core underlying concept:

> Javascript gives us a very powerful and flexible keyword called **`this`** & For **regular functions**, what will the keyword **`this`** point to, is determined entirely by ***HOW & WHERE** THE FUNCTION WAS CALLED!!*
> 

## Rule #1

By default, the **`this`** keyword points at the **`global`** object. if we “simply execute” a regular function (without explicitly, implicity or hard binding the `this` to any object) then `this` points to the `global` object, which in the browser is the `window` object.

```
function sayGoodbye() {
  console.log("Good bye! ", this); // Window
}

function sayHello() {
  console.log("Helloo! ", this); // Window
  sayGoodbye();
}

sayHello();

```

## Rule #2 - **the implicit binding of 𝑡𝒽𝑖𝓈**

When a **method** is ***called*** as a property of an object, then the `this` implicity refers to the parent object. If a function attached to an object is called by `objectname.methodname()` syntax, the `this` points to the object to which the function is attached.

```jsx
function sayHello() {
  console.log("Hello! from ", this.name);
}

var john = {
  name: "John Doe",
  age: 30,
  sayName: function () {
    // this.age = 35;
    console.log("My name is ", this.name);
  },
  sayHello: sayHello
};

var james = {
  name: "James Bond",
  age: 27,
  sayName: function () {
    console.log("My name is ", this.name);
  },
  sayHello: sayHello
};

john.sayName();
john.sayHello();

james.sayName();
james.sayHello();

```

When a function/class is called with the `new` operator, it gives us a brand new `object` & the `this` refers to the newly created `object`.

```jsx
function Person(name) {
  this.name = name;

  this.sayHello = function () {
    console.log("Hello! ", this, this.name);
  };
}

var james = new Person("James Bond");
var john = new Person("John Doe");

john.sayHello();
james.sayHello();

```

## Rule #3 - The explicit binding of 𝑡𝒽𝑖𝓈 using call/apply

When a function is called using the `call` or `apply` methods, then `this` refers to the value passed as the first argument of the `call` or `apply` function.

```
function sayHello() {
  console.log("Hello! ", this);
}

var john = {
  name: "John Doe",
  age: 30
};

var james = {
  name: "James Bond",
  age: 30
};

sayHello.call(james);
sayHello.call(john);

```

## Rule #4 - **the hard binding of 𝑡𝒽𝑖𝓈 using `bind`**

**`bind`** creates a new function hard bound to the object that we have specified.

```
function sayHello() {
  console.log("Hello! ", this, this.name);
}

var John = {
  name: "John Doe",
  age: 30
};

var johnSayHello = sayHello.bind(John);

johnSayHello();

```

## Rule #5 - **Arrow Functions does not bind 𝑡𝒽𝑖𝓈 at all**

- In an arrow function, the **`this`** keyword behaves like any other variable, the **`this`** gets lexically resolved from one of its parent's scope (Just like any other variable).
- if its a regular function, how the function is invoked matters to determine **`this`**!! - if it's an arrow function, where the function sits (lexically) matters to determine **`this`**, no matter how it was invoked!!
- when you want the **`this`** keyword to resolve lexically from one of its parent's scope, use the arrow function - when you want the **`this`** keyword to resolve dynamically at the call site, use the regular functions.

```
var john = { name: "John Doe", age: 25 };

var sayArrowHello = () => {
  console.log("Arrow Hello ", this);
};

function sayRegularHello() {
  console.log("Regular Hello ", this);
}

function sayRegularName() {
  console.log("My Regular name is ", this.name, this); // points to john because of line no.42
  sayRegularHello();
  sayArrowHello();
  var sayArrowGoodBye = () => {
    console.log("Arrow GoodBye ", this); // lexically resolves to john
  };
  sayArrowGoodBye();
}

sayRegularName.call(john);

```

## Gentle introduction to Poly-filling

Let’s do some Hacking 🏴‍☠️

Take it lightly as fun..

```jsx
Array.prototype.map = function(cb){
  return ['Mugambo', 'Khush', 'Huva'];
}

let arr = ["A", "O", "Suno", "lo", "ha", "na"];

let newArr =  arr.map(item => item + ' ji')
console.log(newArr)

let newArr3 = [1,2,3,4,5].map(item => item+1);
console.log(newArr3);

console.dir(Array);
```

Student task 1: [https://codepen.io/drupalastic/pen/OJwNzGR?editors=0012](https://codepen.io/drupalastic/pen/OJwNzGR?editors=0012) 

Student task 2: [https://codepen.io/drupalastic/pen/ExpKQxr?editors=0012](https://codepen.io/drupalastic/pen/ExpKQxr?editors=0012) 

[assignment](Mastering%20%E2%80%9Cthis%E2%80%9D%20keyword%20%5B120%20min%5D%20(1)%20eb11ef1f50b84dad9493b1a29bc00d0f/assignment%20a9fb931aa2ed401385e5ebd1dc67f198.md)