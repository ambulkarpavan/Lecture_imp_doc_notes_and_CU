# OOPs

Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications and computer programs.  It utilizes 4 key concepts:

- **Encapsulation**
- **Abstraction**
- **Inheritance**
- **Polymorphism**

## Encapsulation

Encapsulation in JavaScript is about bundling the data (properties) and the code (methods) that manipulates the data into a single unit, which is the object. In other words The process of **wrapping properties and functions** within a **single unit** is known as encapsulation.

![Untitled](OOPs%2068c2e1ad162148a69f4c986930252798/Untitled.png)

The localStore object has `length` property & methods like `getItem` and `setItem` to remove the items. 

In JavaScript, this is achieved by:

1. **Properties**: These are like the contents of the diary. They represent the state of the object. 
2. **Methods**: These are like the actions you can perform with the diary, such as adding a new note or reading an existing one. 

CoffeeMachine example:

```jsx
function CoffeeMachine() {
  this.coffeeBeans = 100;

  this.grindBeans = function () {
    console.log("Grinding beans...");
    this.coffeeBeans -= 10;
  };

  this.makeCoffee = function () {
    this.grindBeans();
    console.log("Making coffee...");
  };

  this.showBeans = function () {
    console.log(`Beans remaining: ${this.coffeeBeans}`);
  };
}

// Using the CoffeeMachine
let myMachine = new CoffeeMachine();
myMachine.makeCoffee(); // Grinding beans... Making coffee... 
myMachine.showBeans(); // Beans remaining: 90 

```

## Abstraction

Abstraction means displaying only essential information and hiding the details. Data abstraction refers to providing only essential information about the data to the outside world, hiding the background details or implementation or complexities.  Abstraction means hiding certain details that don't matter to the user and only showing essential features or functions.

For example, take a CoffeeMachine. We don't need to show details  like `coffeeBeans` , `grindBeans()`. Instead we provide essential features which matter to user like `makeCoffee()` & `showBeans()`.

This is normally communicated as we are abstracting away the complexities.

```jsx
function CoffeeMachine() {
    // Private Property: Only accessible within the function
    let coffeeBeans = 100;

    // Private Method
    function grindBeans() {
        console.log("Grinding beans...");
        coffeeBeans -= 10;
    }

    // Public Method
    this.makeCoffee = function() {
        grindBeans(); // using private method
        console.log("Making coffee...");
    };

    // Public Method: shows remaining beans
    this.showBeans = function() {
        console.log(`Beans remaining: ${coffeeBeans}`);
    };
}

// Using the CoffeeMachine
let myMachine = new CoffeeMachine();
myMachine.makeCoffee(); // Public: OK to call
myMachine.showBeans(); // Public: OK to call
// myMachine.grindBeans(); // This will throw an error, as it's a private method
```

## Inheritance

In Object-Oriented Programming, **inheritance** is a key principle that allows us to create a new class that is based on an existing class. The new class, known as a **subclass**, inherits attributes and methods from the existing class, which is referred to as the **superclass**.

To understand the impact of inheritance, especially in terms of reducing redundant code, let's consider the example of HTML elements. In web development, we work with various HTML elements like text boxes, drop-down lists, checkboxes, and so on. Despite their unique functionalities, these elements share several common properties and methods. For instance, most elements have properties like 'hidden' or 'innerHTML', and methods like 'click' and 'focus'.

In a scenario without inheritance, we would end up defining these common properties and methods for each HTML element separately. This approach leads to a significant amount of redundant code, making the codebase larger, more complex, and harder to maintain.

However, with the use of inheritance, we can define these shared properties and methods just once in a generic object, let's say, `HTMLElement`. This `HTMLElement` acts as a superclass. Then, specific element classes like `TextBox`, `DropDownList`, and `Checkbox` can inherit from `HTMLElement`. This way, all the shared properties and methods are available to the specific element classes without having to redefine them.

The benefit here is twofold: firstly, it significantly reduces the amount of code, as we avoid repeating the same code for each element. Secondly, it enhances maintainability. If we need to make a change to a common property or method, we only need to update it in the superclass, and the change automatically propagates to all subclasses. This makes our code more scalable and easier to manage.

In summary, inheritance is a powerful concept in OOP that promotes code reusability and maintainability by allowing classes to inherit properties and methods from other classes, thereby reducing redundant code."

Let's use the `CoffeeMachine` example to explain inheritance in Object-Oriented Programming. Imagine we have a basic `CoffeeMachine` class as you've described, and we want to extend its functionality with inheritance.

Your `CoffeeMachine` class has private members like `coffeeBeans`, a private method `grindBeans()`, and public methods `makeCoffee()` and `showBeans()`. The private members and methods are only accessible within the class, while the public methods can be called from outside.

Now, suppose we want to create a `SpecialCoffeeMachine` that has additional features, like making a cappuccino or an espresso. Instead of writing a completely new class from scratch, we can inherit from the `CoffeeMachine` class and extend its functionality.

```jsx
function SpecialCoffeeMachine() {
    CoffeeMachine.call(this); // Inherit properties and methods from CoffeeMachine

    // New method specific to SpecialCoffeeMachine
    this.makeCappuccino = function() {
        this.makeCoffee(); // Using inherited method
        console.log("Adding milk foam for cappuccino...");
    };

    this.makeEspresso = function() {
        this.makeCoffee(); // Using inherited method
        console.log("Making a strong espresso...");
    };
}

// Set up inheritance
SpecialCoffeeMachine.prototype = Object.create(CoffeeMachine.prototype);
SpecialCoffeeMachine.prototype.constructor = SpecialCoffeeMachine;

// Using SpecialCoffeeMachine
let mySpecialMachine = new SpecialCoffeeMachine();
mySpecialMachine.makeCappuccino(); // Uses both inherited and new methods
mySpecialMachine.showBeans(); // Inherited method

```

1. **Inheritance**: `SpecialCoffeeMachine` inherits from `CoffeeMachine`. This means it gets all the properties and methods of `CoffeeMachine`.
2. **Extended Functionality**: `SpecialCoffeeMachine` adds its own methods like `makeCappuccino` and `makeEspresso`, which use the inherited `makeCoffee` method as part of their process.
3. **Reusability and Maintenance**: By using inheritance, we avoid rewriting the logic for making coffee or managing beans. Any changes in the `CoffeeMachine` class will automatically be reflected in the `SpecialCoffeeMachine`, making maintenance easier.
4. **Encapsulation**: The private members and methods of `CoffeeMachine` (like `grindBeans` and `coffeeBeans`) remain inaccessible directly from `SpecialCoffeeMachine`, maintaining encapsulation.

In this example, inheritance allows the `SpecialCoffeeMachine` to build upon the existing functionality of `CoffeeMachine` without duplicating code. This demonstrates how inheritance promotes reusability and maintainability in software development, a key advantage of object-oriented programming.

## Polymorphism

Polymorphism in object-oriented programming (OOP) refers to the ability of different objects to respond in their own way to the same message or method call. The term "polymorphism" comes from Greek, where "poly" means "many" and "morph" means "form." Thus, polymorphism means "many forms."

In the context of the provided description, polymorphism allows objects to implement the same method in different ways. This is particularly useful when dealing with a hierarchy of objects where each subclass can have its own specific behavior for a common method. In your example, the focus is on rendering HTML elements. Each HTML element (like a button, textbox, image, etc.) has a common operation, such as rendering, but the way they render on a page is different for each element type.

To illustrate this with the CoffeeMachine example, let's extend it to demonstrate polymorphism. We will create different types of coffee machines, each with a unique way of making coffee.

First, we have the basic `CoffeeMachine`:

```jsx
function CoffeeMachine() {
    let coffeeBeans = 100;

    function grindBeans() {
        console.log("Grinding beans...");
        coffeeBeans -= 10;
    }

    this.makeCoffee = function() {
        grindBeans();
        console.log("Making standard coffee...");
    };

    this.showBeans = function() {
        console.log(`Beans remaining: ${coffeeBeans}`);
    };
}

```

Now, let's create a `SpecialCoffeeMachine` that extends `CoffeeMachine` and overrides the `makeCoffee` method:

```jsx
function SpecialCoffeeMachine() {
    CoffeeMachine.call(this); // Inherit from CoffeeMachine

    let originalMakeCoffee = this.makeCoffee;
    // method overriding
    this.makeCoffee = function() {
        originalMakeCoffee.call(this); // Call the original method
        console.log("Adding special ingredients for special coffee...");
    };
}

```

Here, `SpecialCoffeeMachine` has a different implementation of `makeCoffee`. It first calls the original method from `CoffeeMachine` to make standard coffee and then adds its special ingredients.

When we use these objects, polymorphism becomes evident:

```jsx
let myMachine = new CoffeeMachine();
myMachine.makeCoffee(); // Outputs: Grinding beans... Making standard coffee...

let mySpecialMachine = new SpecialCoffeeMachine();
mySpecialMachine.makeCoffee(); // Outputs: Grinding beans... Making standard coffee... Adding special ingredients for special coffee...

```

In this way, both `CoffeeMachine` and `SpecialCoffeeMachine` have a `makeCoffee` method, but the implementation differs based on the object's type. This is polymorphism – the same method name (`makeCoffee`), but different behaviors depending on the object.

By using polymorphism, you can write code that is more flexible and easier to maintain, as it allows you to treat different objects uniformly while leveraging their specific behaviors.

```jsx
// function overloading
greet(a) {
// count the number of args
// Array.isArray(a) {

} else {

}

}

greet([1,3,4])
greet (1,3)
```

## Benefits of OOPs

### Encapsulation

- **Benefit**: Encapsulation bundles data (properties) and code (methods) into a single unit, providing better organization and structure to the code. It helps in maintaining data integrity and prevents direct access to the internal implementation details of an object.

### Abstraction

- **Benefit**: Abstraction allows developers to focus on essential features or functions while hiding unnecessary details. It simplifies the complexity of code by providing a high-level view of objects and their interactions. This enhances code readability, reusability, and maintainability.

### Inheritance

- **Benefit**: Inheritance promotes code reusability and reduces redundancy by allowing subclasses to inherit properties and methods from a superclass. It enables the creation of a hierarchy of objects, where subclasses can add their own specific behaviors while inheriting the common functionalities. This makes the codebase more scalable, manageable, and easier to maintain.

### Polymorphism

- **Benefit**: Polymorphism enables objects of different types to respond to the same method or message in their own specific ways. It allows for dynamic binding, where the appropriate method implementation is determined at runtime based on the actual object type. Polymorphism enhances code flexibility, extensibility, and promotes the principle of "write once, use anywhere."

## How is OOPs different in Javascript as compared to other classical programming languages like Java

Object-Oriented Programming (OOP) in JavaScript differs from other classical programming languages like Java in several ways:

1. **Prototypal Inheritance**: JavaScript uses prototypal inheritance instead of classical inheritance. In classical languages like Java, classes are used to create objects, and objects are instances of these classes. In JavaScript, objects can directly inherit properties and methods from other objects, known as prototypes. This allows for more flexible and dynamic object creation.
2. **Dynamic Typing**: JavaScript is dynamically typed, meaning that the type of a variable is determined at runtime. In contrast, classical languages like Java are statically typed, where variables must have a declared type at compile time. This flexibility in JavaScript allows for more fluid and adaptable coding.
3. **First-class Functions**: Functions in JavaScript are considered first-class citizens, meaning they can be assigned to variables, passed as arguments to other functions, and returned as values from functions. This enables powerful functional programming capabilities and makes JavaScript a versatile language for various programming paradigms.
4. **No Class Declarations**: JavaScript does not have traditional class declarations like Java. Instead, it uses constructor functions and the `class` keyword (introduced in ECMAScript 2015) to create objects and define their properties and methods. This provides a more lightweight and flexible approach to object creation.
5. **Flexible Object Structure**: In JavaScript, objects can have dynamic properties and methods. Unlike in Java, where classes define a fixed structure for objects, JavaScript allows objects to have properties and methods added or modified at runtime. This dynamic nature provides a lot of flexibility in object design.
6. **Prototype Chain**: JavaScript uses a prototype chain to resolve property and method lookups. When a property or method is accessed on an object, JavaScript first checks if it exists directly on the object. If not, it looks up the prototype chain until it finds the property or method. This allows for easy inheritance and method sharing between objects.

## Difference between compile time and runtime polymorphism

**Compile Time Polymorphism in general:**

Whenever an object is bound with its functionality at the compile time, this is known as the compile-time polymorphism. At compile-time, java knows which method to call by checking the method signatures. So this is called compile-time polymorphism or static or early binding. Compile-time polymorphism is achieved through [**method overloading](https://www.geeksforgeeks.org/overloading-in-java/).** Method Overloading says you can have more than one function with the same name in one class having a different prototype. Function overloading is one of the ways to achieve polymorphism but it depends on technology and which type of polymorphism we adopt. In java, we achieve function overloading at compile-Time. The following is an example where compile-time polymorphism can be observed.

greet(x) {

Array.isArray(x) {

} else {

}

}

greet(10)

greet([1,2,3])

**Run-Time Polymorphism in general:**

Whenever an object is bound with the functionality at run time, this is known as runtime polymorphism. The runtime polymorphism can be achieved by **[method overriding.](https://www.geeksforgeeks.org/overriding-in-java/) [Java virtual machine](https://www.geeksforgeeks.org/jvm-works-jvm-architecture/)** determines the proper method to call at the runtime, not at the compile time. It is also called dynamic or late binding. Method overriding says the child class has the same method as declared in the parent class. It means if the child class provides the specific implementation of the method that has been provided by one of its parent classes then it is known as method overriding.

**In JavaScript, both method overloading and method overriding are determined at “runtime” due to its dynamic nature.**

JavaScript, being a dynamically typed and interpreted language, doesn't have compile-time polymorphism in the same way as statically typed, compiled languages.

**Function Overloading (Simulated in JavaScript)**: While traditionally considered an example of compile-time polymorphism in statically typed languages, in JavaScript, what we refer to as "function overloading" is also a form of runtime polymorphism. This is because the decision of which function logic to execute, based on the arguments, happens at runtime.

**Example**:

```jsx
function add(a, b) {
    if (typeof b === 'undefined') {
        return a + a; // Decided at runtime based on arguments
    }
    return a + b;
}

console.log(add(5));    // Output: 10
console.log(add(5, 10)); // Output: 15

```

**Prototypal Inheritance (Method Overriding)**: This is a more clear-cut example of runtime polymorphism in JavaScript. When a method is overridden in a child class (or constructor function), the JavaScript engine determines which method to call at runtime based on the object's prototype chain.

**Example**:

```jsx
function Animal(name) {
    this.name = name;
}

Animal.prototype.speak = function() {
    console.log(`${this.name} makes a noise.`);
}

function Dog(name) {
    Animal.call(this, name);
}

Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

Dog.prototype.speak = function() {
    console.log(`${this.name} barks.`);
};

let pet = new Dog('Rex');
pet.speak(); // Output: Rex barks.

```

In JavaScript, most polymorphic behaviors are determined at runtime due to its dynamic nature. This contrasts with languages like Java or C++, where compile-time polymorphism (like method overloading and template specialization) is a significant feature.

## S.O.L.I.D. Design principles

### Single Responsibility Principle

The "S" in the SOLID design principles stands for the **Single Responsibility Principle (SRP)**. This principle states that a class or module should have one, and only one, reason to change. In simpler terms, it means that a class should only have one job or responsibility.

### Explanation

- **Single Responsibility**: Each class or module should focus on a single part of the functionality provided by the software. This makes the class or module more robust, easier to understand, easier to test, and easier to maintain.
- **Reason to Change**: The principle suggests that if a class has more than one responsibility, then there are more reasons for it to change. Multiple responsibilities can lead to a higher chance of bugs since a change in one responsibility might affect the other one inadvertently.

### Bad Code Example (Violating SRP)

In JavaScript, a bad example of SRP would be a class that handles both user data management and user interface logic:

```jsx
class User {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    saveUser() {
        // Code to save user data to a database
    }

    displayUser() {
        // Code to display user data on the screen
    }
}

```

Here, the `User` class has two responsibilities: managing user data and handling the user interface. This is not ideal, as changes in the user interface logic might affect the data management logic, or vice versa.

### Good Code Example (Following SRP)

A better approach would be to separate these concerns into two classes:

```jsx
class UserDataManager {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    saveUser() {
        // Code to save user data to a database
    }
}

class UserInterface {
    constructor(user) {
        this.user = user;
    }

    displayUser() {
        // Code to display user data on the screen
    }
}

```

In this improved version, we have:

- `UserDataManager`: Responsible for managing the user's data.
- `UserInterface`: Responsible for displaying user data on the UI.

This separation makes each class easier to maintain and less prone to bugs related to unrelated functionalities. It also makes it easier to modify or extend the functionalities of either user data management or user interface without affecting the other.

### **Open/Closed Principle**

The "O" in the SOLID design principles stands for the **Open/Closed Principle (OCP)**. This principle states that software entities (like classes, modules, functions, etc.) should be open for **extension** but closed for **modification**. In simpler terms, it means that you should be able to add new functionality without changing existing code.

### Explanation

- **Open for Extension**: You should be able to add new features or components to the application without breaking existing code.
- **Closed for Modification**: The existing code should not need to be modified to accommodate new features. If you find yourself frequently modifying existing code to add new features, you're probably not adhering to this principle.

### Bad Code Example (Violating OCP)

In JavaScript, a violation of the OCP might look like a class that you have to modify every time you want to add a new feature:

```jsx
class Shape {
    constructor(name) {
        this.name = name;
    }
}

class AreaCalculator {
    calculateArea(shapes) {
        let area = 0;
        for (let shape of shapes) {
            if (shape.name === 'circle') {
                // calculate area of circle
                area += Math.PI * 4; // simplified for example
            } else if (shape.name === 'square') {
                // calculate area of square
                area += 4; // simplified for example
            }
            // for every new shape, we have to modify this class
        }
        return area;
    }
}

```

Here, every time you add a new shape, you have to modify the `AreaCalculator` class. This is not ideal as it makes the class harder to maintain and more prone to bugs.

### Good Code Example (Following OCP)

A better approach would be to design the classes in such a way that adding new shapes doesn't require changing the existing `AreaCalculator` class:

```jsx
class Shape {
    getArea() {
        throw new Error('This method should be implemented by subclasses');
    }
}

class Circle extends Shape {
    constructor(radius) {
        super();
        this.radius = radius;
    }

    getArea() {
        return Math.PI * this.radius * this.radius;
    }
}

class Square extends Shape {
    constructor(length) {
        super();
        this.length = length;
    }

    getArea() {
        return this.length * this.length;
    }
}

class AreaCalculator {
    calculateArea(shapes) {
        return shapes.reduce((area, shape) => area + shape.getArea(), 0);
    }
}

```

In this improved version:

- Each shape class (`Circle`, `Square`, etc.) extends `Shape` and implements the `getArea` method.
- `AreaCalculator` now works with any shape that conforms to the `Shape` interface, making it open for extension but closed for modification. You can add new shapes without changing the `AreaCalculator`'s code.

This design adheres to the Open/Closed Principle, making the codebase more robust, easier to maintain, and open to extension without requiring changes to the existing code.

### **Liskov Substitution Principle**

The "L" in the SOLID design principles stands for the **Liskov Substitution Principle (LSP)**. This principle, named after Barbara Liskov, states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program. In simpler terms, it means that subclasses should extend the parent classes in such a way that they can be used interchangeably without causing issues.

### **Explanation**

- **Subtype Replaceability**: If class **`B`** is a subtype of class **`A`**, then objects of class **`A`** may be replaced with objects of class **`B`** without altering any desirable properties of the program (e.g., correctness).
- **Design Implication**: It guides us to design our inheritance structures so that the derived classes only extend the base classes without changing their behavior.

LSP states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program. This means subclasses should be able to perform the same actions as their superclass without error or altered behavior.

### Bad Code Example (Violating LSP)

In this example, we'll create a situation where a subclass (`Penguin`) cannot be used interchangeably with its superclass (`Bird`), particularly in the context of a method `fly()` that is not applicable to all birds.

```jsx
class Bird {
    eat() {
        return "I can eat!";
    }

    fly() {
        return "I can fly!";
    }
}

class Duck extends Bird {
    // Duck can eat and fly
}

class Penguin extends Bird {
    // Penguin can eat, but can't fly; overrides fly() with an error
    fly() {
        throw new Error("Cannot fly");
    }
}

function makeBirdFly(bird) {
    return bird.fly();
}

// This will throw an error for Penguin, violating LSP
try {
    makeBirdFly(new Penguin());
} catch (e) {
    console.error(e.message); // Outputs: "Cannot fly"
}

```

In this bad example:

- All birds have an `eat()` method, but the `fly()` method in the `Bird` class isn't applicable to all birds like `Penguin`.
- When a `Penguin` instance is used where a `Bird` is expected, it results in an error, violating LSP.

### Good Code Example (Following LSP)

Now, let's refactor the code to adhere to LSP, ensuring all subclasses can be used in place of their superclass.

```jsx
class Bird {
    eat() {
        return "I can eat!";
    }
}

class FlyingBird extends Bird {
    fly() {
        return "I can fly!";
    }
}

class Duck extends FlyingBird {
    // Duck can eat and fly
}

class Penguin extends Bird {
    // Penguin can eat but doesn't inherit fly()
    swim() {
        return "I can swim!";
    }
}

function makeBirdFly(bird) {
    if (!(bird instanceof FlyingBird)) {
        throw new Error("This bird can't fly");
    }
    return bird.fly();
}

// This will not throw an error, as Penguin doesn't have the fly() method
try {
    makeBirdFly(new Duck()); // Works fine
    makeBirdFly(new Penguin()); // Correctly throws an error
} catch (e) {
    console.error(e.message); // Outputs: "This bird can't fly"
}

```

In the good example:

- The `Bird` class only includes behaviors common to all birds, like `eat()`.
- `FlyingBird`, a subclass of `Bird`, introduces the `fly()` method, applicable to birds that can fly.
- `Duck` is a `FlyingBird` and inherits both `eat()` and `fly()`.
- `Penguin` is a `Bird` but not a `FlyingBird`, so it doesn't have a `fly()` method, avoiding the violation of LSP.
- The `makeBirdFly` function checks if the bird is an instance of `FlyingBird` before attempting to call `fly()`, adhering to LSP.

By structuring the classes this way, we ensure that any subclass of `Bird` can be used in place of a `Bird` without unexpected behavior or errors, fulfilling the requirements of the Liskov Substitution Principle.

### **Interface Segregation Principle**

The "I" in the SOLID design principles stands for the **Interface Segregation Principle (ISP)**. This principle suggests that no client should be forced to depend on methods it does not use. In simpler terms, it means creating smaller, more specific interfaces rather than having one large, general-purpose interface.

### Explanation

- **Small, Specific Interfaces**: Instead of one large interface, multiple smaller interfaces are preferred. Each of these smaller interfaces should cater to a specific subset of functionalities.
- **Avoid Overburdening**: An interface should not force the implementing classes to use methods that they don't need. This helps in reducing the side-effects of changes and makes the codebase more maintainable.

### Bad Code Example (Violating ISP)

In JavaScript, an example of violating the ISP would be creating a large, all-encompassing interface (or in JavaScript terms, a class with many methods), which forces implementing classes to have methods they don't use.

```jsx
class Worker {
    work() {
        // work implementation
    }

    eat() {
        // eat implementation
    }

    sleep() {
        // sleep implementation
    }

    play() {
        // play implementation
    }
}

class HumanWorker extends Worker {
    // Human worker uses all methods
}

class RobotWorker extends Worker {
    // Robot worker doesn't need eat or sleep, but it's still forced to have them
}

```

Here, `RobotWorker` is forced to have `eat` and `sleep` methods, even though it doesn’t need them, violating the ISP.

### Good Code Example (Following ISP)

A better approach is to break down the `Worker` into smaller, more specific interfaces:

```jsx
class Workable {
    work() {
        // work implementation
    }
}

class Eatable {
    eat() {
        // eat implementation
    }
}

class Sleepable {
    sleep() {
        // sleep implementation
    }
}

class Playable {
    play() {
        // play implementation
    }
}

class HumanWorker extends Workable {
    constructor() {
        super();
        Object.assign(this, new Eatable(), new Sleepable(), new Playable());
    }
    // Human worker uses all functionalities
}

class RobotWorker extends Workable {
    // Robot worker only uses work functionality
}

```

In this improved version:

- The functionalities are broken down into smaller classes (`Workable`, `Eatable`, `Sleepable`, `Playable`).
- `HumanWorker` can mix in all these functionalities as needed.
- `RobotWorker` only implements the `Workable` interface, adhering to its requirements and not being forced to implement unnecessary methods.

This design adheres to the Interface Segregation Principle by ensuring that classes only implement the methods that are necessary for their functionality, making the codebase more flexible and maintainable.

# Dependency Inversion

[https://www.youtube.com/watch?v=9oHY5TllWaU](https://www.youtube.com/watch?v=9oHY5TllWaU)