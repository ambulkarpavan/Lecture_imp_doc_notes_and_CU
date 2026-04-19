# assignment

### Guidelines:

- create one `.js file` in the `Masai repo` and solve it.
- after solving the assignment push your code to `GitHub`.
- share the `GitHub Link` in the assignment.

### Question 1:

Create a class named **`Person`** with a constructor that takes **`name`** and **`age`** as parameters. Add a static method called **`greet`** that logs a greeting message. Create an instance of **`Person`** and call the **`greet`** static method.

add method to the prototype called `canSleep` that will return `<name> is sleeping...`

### Question 2:

Create a class named **`Employee`** that inherits from **`Person`**. Add a private property called **`_salary`** and create a getter and setter for it. The getter should return the salary, and the setter should validate that the salary is a positive number. Create an instance of **`Employee`** and set the salary to a negative value to test the setter.

add one method to the prototype called `working` that returns `<name> is working…`

### Question 3:

Create a class named **`Manager`** that inherits from **`Employee`**. Add a static method called **`getRole`** that returns the role of "Manager". Create an instance of **`Manager`** and call the **`getRole`** static method.

add one method to the prototype called `managing` that returns `<name> is managing…`

### Question 4:

Create a class named **`Executive`** that inherits from **`Manager`**. Add a private property called **`_bonus`** and create a getter and setter for it. The getter should return the bonus, and the setter should validate that the bonus is a positive number. Create an instance of **`Executive`** and set the bonus to a negative value to test the setter.

### Question 5:

Create a class named **`CEO`** that inherits from **`Executive`**. Add a static method called **`getRole`** that returns the role of "CEO". Create an instance of **`CEO`** and call the **`getRole`** static method.

add one method to the prototype called `fundRaise` that returns `<name> is raising fund…`

### Question 6:

Create a class hierarchy for a banking system. The hierarchy should include three classes: **`Bank`**, **`Account`**, and **`SavingsAccount`**. The **`Account`** class should inherit from the **`Bank`** class, and the **`SavingsAccount`** class should inherit from the **`Account`** class. Each class should have its own private properties, getter, setter, and a static method.

Your task is to implement the classes and demonstrate the inheritance chain by creating instances of each class and accessing their properties and methods.

Hints:

- The **`Bank`** class should have a private property called **`_name`**.
- The **`Account`** class should have a private property called **`_balance`** and a static method called **`getBankName()`** that returns the bank name.
- The **`SavingsAccount`** class should have a private property called **`_interestRate`** and a setter for it.

### Question 7:

**hierarchy chain**

```jsx
           Animal
              |
        -------------
        |           |
      Mammal       Bird
        |           |
   ------------   -------
   |          |   |     |
  Lion      Cow  Eagle  Sparrow
 
```

The **`Animal`** class should have two subclasses: **`Mammal`** and **`Bird`**. The **`Mammal`** subclass should have a private property called **`type`** and a public getter and setter for it. The **`Bird`** subclass should have a private property called **`wingspan`** and a public getter and setter for it.

In addition, create two more subclasses for the **`Mammal`** class: **`Lion`** and **`Cow`**. The **`Lion`** subclass should have a private property called **`maneColor`** and a public getter and setter for it. The **`Cow`** subclass should have a private property called **`milkProduction`** and a public getter and setter for it.

The **`Bird`** subclass should include **`Eagle`** and **`Sparrow`**. Each of these subclasses should have a unique private property and a public getter and setter for that property.

Create instances of each subclass, set their respective properties using the setters, and demonstrate the use of the getters to retrieve the property values. Also, call the **`getType`** static method on the **`Animal`** class and display the result.