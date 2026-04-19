# assignment

## Code Snippet 1:

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

## Code Snippet 2:

```jsx
const person = {
  name: "John",
  sayHello: function() {
    console.log("Hello, my name is " + this.name);
  },
  sayDelayedHello: function() {
    setTimeout(function() {
      console.log("Delayed Hello, my name is " + this.name);
    }, 1000);
  },
  sayArrowDelayedHello: function() {
    setTimeout(() => {
      console.log("Arrow Delayed Hello, my name is " + this.name);
    }, 1000);
  }
};

person.sayHello();              // Output: Hello, my name is John
person.sayDelayedHello();       // Output: Delayed Hello, my name is undefined
person.sayArrowDelayedHello();  // Output: Arrow Delayed Hello, my name is John
```

## Code Snippet 3:

```jsx
function Car(make, model) {
  this.make = make;
  this.model = model;
}

Car.prototype.startEngine = function() {
  console.log(this.make + " " + this.model + " engine started.");
};

Car.prototype.drive = function() {
  console.log("Driving the " + this.make + " " + this.model + ".");
};

const car1 = new Car("Toyota", "Corolla");
const car2 = new Car("Honda", "Civic");

car1.startEngine(); 
car2.startEngine();  

car1.drive();      
car2.drive();        
```

## Code Snippet 4:

```jsx
function greet() {
  console.log("Greetings! I am", this.name);
}

var person1 = {
  name: "Alice",
  age: 25,
  introduction: function() {
    console.log("Hello, my name is", this.name);
  },
  greet: greet
};

var person2 = {
  name: "Bob",
  age: 30,
  introduction: function() {
    console.log("Hello, my name is", this.name);
  },
  greet: greet
};

person1.introduction();
person1.greet();

person2.introduction();
person2.greet();
```

## Code Snippet 5:

```jsx
function printMessage() {
  console.log(this.message);
}

var obj1 = {
  message: "Hello from object 1",
  printMessage: printMessage
};

var obj2 = {
  message: "Hello from object 2",
  printMessage: printMessage
};

var obj3 = {
  message: "Hello from object 3",
  innerObj: {
    message: "Hello from inner object",
    printMessage: printMessage
  }
};

obj1.printMessage();
obj2.printMessage();
obj3.innerObj.printMessage();
```

## Code Snippet 6:

```jsx
function introduce() {
  console.log("I am", this.name, "and I am", this.age, "years old.");
}

var person1 = {
  name: "Alice",
  age: 25
};

var person2 = {
  name: "Bob",
  age: 30
};

introduce.call(person1);
introduce.call(person2);
```

## Code Snippet 7:

```jsx
function printName() {
  console.log("Name:", this.name);
}

function greet() {
  console.log("Hello, ", this.name);
}

var person = {
  name: "Alice",
  printName: printName,
  greet: greet
};

var friend = {
  name: "Bob",
  printName: printName,
  greet: greet
};

var stranger = {
  printName: printName,
  greet: greet
};

var boundPrintName = printName.bind(person);
boundPrintName();

var boundGreet = greet.bind(friend);
boundGreet();

person.printName.call(friend);
friend.greet.apply(stranger);
```

## Code Snippet 8:

```jsx
function Person(name) {
  this.name = name;
}

Person.prototype.sayHello = function() {
  console.log("Hello, my name is", this.name);
};

function createPerson() {
  var person = new Person("Alice");
  person.sayHello();
}

function sayHello() {
  console.log("Hello ", this);
}

sayHello();

createPerson();
```

## Code Snippet 9:

```jsx
var obj = {
  name: "John",
  func1: function() {
    console.log("Func1: Hello, my name is", this.name);
    var func2 = function() {
      console.log("Func2: Hello, my name is", this.name);
    };
    func2();
  }
};

obj.func1();
```

## Code Snippet 10:

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

## Code Snippet 11:

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

## Code Snippet 12:

```jsx
var person = {
  name: "Alice",
  age: 30,
  sayArrowHello: () => {
    console.log("Arrow Hello ", this);
  },
  sayRegularHello: function() {
    console.log("Regular Hello ", this);
  },
  sayRegularName: function() {
    console.log("My Regular name is ", this.name, this);
    this.sayRegularHello();
    this.sayArrowHello();
    var sayArrowGoodbye = () => {
      console.log("Arrow Goodbye ", this);
    };
    sayArrowGoodbye();
  }
};

person.sayRegularName();
```

## Code Snippet 13:

```jsx
function Car(make, model) {
  this.make = make;
  this.model = model;
  this.drive = function() {
    console.log("Driving the", this.make, this.model);
  };
}

var car1 = new Car("Toyota", "Corolla");
var car2 = new Car("Honda", "Civic");

function accelerate() {
  console.log("Accelerating the", this.make, this.model);
}

car1.accelerate = accelerate;
car2.accelerate = accelerate;

car1.drive();
car1.accelerate();

car2.drive();
car2.accelerate();
```