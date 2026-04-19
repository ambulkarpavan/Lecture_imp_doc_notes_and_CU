# Variables [10 min] (1)

**Definition:** A variable is a container for storing data in JavaScript.

**Declaration:** Variables are declared using the **`var`** keyword.

**Naming Rules:** Variable names should start with a letter or underscore, followed by letters, numbers, or underscores.

We use programming languages like JavaScript to store and manipulate information.
Variables in JavaScript are used to store different kinds of data. Think of a variable
like a bottle. We use bottles to store water, in much the same way we use variables to
store various forms of data in JavaScript.

```jsx
var age = 25;    //Declaring a variable named 'age' with a value of 25
```

  

**Syntax:** You can also declare multiple variables in one statement as seen in the syntax
below.

**Multiple Variables Example:**

```jsx
var a = 100, b = 200, c = 300;
```

The data inside variables is not constant. This means the data inside a variable can
be changed.

**Example:**

```jsx
var a = 200
a = 100
```

In the above example, the variable called a first contained the value 200 but a = 100
means that a now contains the value 100.

**NOTE:** You can name variables whatever you want but try to give them good/descriptive
names that tell the reader what the variable is used for

### Declaration, Declaration with Initialisation, Assignment, Reassignment

```jsx
//declare or define a variable called firstName
let firstName; 

// initialize or assign value to a variable
firstName = 'John'

// declare & initialize | define a variable and assign a value
let lastName = 'Smith';

// re-assign value to a variable
firstName = 'Will'

// Access or showing or logging or looking up the variable content
console.log(firstName, lastName)
```