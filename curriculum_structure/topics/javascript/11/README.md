# Conditional Statements [20 min] (1)

- Conditional statements are used to decide the flow of execution based on different
conditions. If a condition is true, you can perform one action and if the condition is
false, you can perform another action.
- Through Conditional Statements, we can control which code needs to run or which
code will not run.
- Code runs based on certain conditions.
For Ex: let's understand with the analogy, that the traffic light controls the flow of
vehicles on the road. Depending upon the color of the light, the actions happened.
If the light is green, then it is a signal to move whereas if the light is red then it is a
signal to move.
- Based on the comparison, if the comparison is true then it will execute the one
block of code otherwise another block of code.

### Different Types of Conditional Statements

There are mainly three main types of conditional statements in JavaScript.

1. If statement
2. If…Else statement
3. If…Else If…Else statement

### **if Statement:**

It is to specify a block of JavaScript code to be executed if a condition is true.

**Syntax:**
condition
block of code to be executed if the condition is true

- `if()`
It takes a Boolean Value or the expression that will give a Boolean value.
- `if() { }`
`{ }` is known as a code block.

**a) If with Boolean Value**

```jsx
console.log("Code Start")
if(true) {
console.log("Inside Code")
}
console.log("Code End")
```

**b) If with Expression**

The decision is based on the value of Expression

For Example :

```jsx
if(5>3){
console.log("Inside Code");
}
```

**c) If with Variables**

The decision is based on the value of Expression

For Example :

```jsx
var name1 = "rahul";
var name2 = "rahul";
var check = (name1==name2);
if(check){
console.log("Both Names are same");
}
```

**Code 1: Check Whether two numbers are equal**

```jsx
var a = 2;
var b = 3;
var c = (a==b);
if(c)
{
console.log("a and b are equal");
}
```

### if/else Statement:

The `if...else` is a type of conditional statement that will execute a block of code
when the condition in the `if` statement is `truthy`. If the condition is `falsy`, then
the `else` the block will be executed.

Here is a list of  falsy  values:

- `false`
- `0` (zero)
- `0` (negative zero)
- `0n` (BigInt zero)
- `""` ,  `''` ,  ````  (empty string)
- `null`
- `undefined`
- `NaN` (not a number)

If the condition is true, then one block of code executes.
Otherwise, another block of code executes.

**Syntax:**
condition
block of code to be executed if the condition is true
block of code to be executed if the condition is false

**Code 2: Check which number is greater**

```jsx
var a = 3;
var b = 20;
if(a>b)
{
console.log("a is greater");
}
else
{
console.log("a is not greater");
}
```

**Code 3: Check Whether two names are equal or not**

```jsx
var name1 = "suraj";
var name2 = "suraj";
if(name1==name2)
{
console.log("Names are Equal");
}
else
{
console.log("Names are not equal");
}
```

**Hotel Bill Discount:**

**Code 4 :**

**Given total_bill, discount_start_price if you satisfy the condition Print Discount
Availaible Otherwise print No Discount**

```jsx
var total_bill = 699;
var discount_start_price = 500;
if(total_bill>=discount_start_price){
console.log("Discount Available");
}
else{
console.log("No discount");
}
```

### Else-if Statement:

- There will be times when you want to test multiple conditions. That is where
the `else if` the block comes in.
- When the `if` statement is `false`, the computer will move on to the `else
if` statement. If that is also `false`, then it will move onto the `else` block.

**Syntax:**

**condition1**
block of code to be executed if condition1 is `true`
**condition2**
block of code to be executed if condition1 is `false` and condition2 is `true`
block of code to be executed if condition1 is `false` and condition2 is `false`

**Bill and Discount**
Problem Statement: According to the total_bill, the discount will be applied.

| Total Bill   | Discount Applied |
| --- | --- |
| Greater Than 500 | 10% |
| Greater Than 1000 | 20% |
| Others | No Discount |

**Code 5 :**

 **For a Restaurant, write the program for the following total_bill > 500
Then print 10% discount total_bill > 1000 Then print 20% discount Otherwise No
discount**

```jsx
var total_bill = 799;
if(total_bill > 1000)
{
console.log("20 % discount");
}
else if(total_bill > 500)
{
console.log("10 % discount");
}
else
{
console.log("No discount");
}
```

### `If-Else-If` vs `if-if-if` :

**Code 6: If-Else-If**

- My mother told me to get any one of the things from the market
1. `If` Rice is available then print Buy rice
2. `Else If` wheat is available then print buy wheat
3. `Else If` Apple is available then print buy apple

```jsx
var rice_availaible = false ;
var wheat_availaible = true;
var apple_availaible = true;
if(rice_availaible)
{
Conditional Statements 7
console.log("Buy rice");
}
else if(wheat_availaible)
{
console.log("Buy Wheat");
}
else if(apple_availaible)
{
console.log("Buy apple");
}
else
{
console.log("Nothing is availaible");
}
```

**Code 7: If - If - If**

- My mother told me to get all of the things if available from the market
1. `If` Rice is available then print Buy rice
2. `If` wheat is available then print buy wheat
3. `If` Apple is available then print buy apple

```jsx
var rice_availaible = true ;
var wheat_availaible = true;
var apple_availaible = false;
if(rice_availaible)
{
console.log("Buy rice");
}
if(wheat_availaible)
{
console.log("Buy Wheat");
}
if(apple_availaible)
{
console.log("Buy apple");
}
```

**Code 8 :** 

**Solve the Marriage Problem Legal Age in India Males ----> 21 Females ----> 18**

```jsx
var gender = "female";
var age = 21;
if(gender == "male")
{
if(age>=21)
{
console.log("Males : get marry");
}
else
{
console.log("Males : Can't get marry");
}
}
else
{
if(age>=18){
console.log("Females : get marry");
}
else{
console.log("Females : Can't get marry");
}
}
```

**Code 9 :**

**Given a char, you need to print whether the char is a vowel or not
vowels: a, e, i, o, u**

```jsx
var char = "z"
if(char == "a")
{
console.log("vowel");
}
else if(char == "e")
{
console.log("vowel");
}
else if(char == "i")
Conditional Statements 9
{
console.log("vowel");
}
else if(char == "o")
{
console.log("vowel");
}
else if(char == "u")
{
console.log("vowel");
}
else{
console.log("Not a vowel");
}
```

### Not Operator:

On applying to a boolean value, the not operator turns true to false and false to true.