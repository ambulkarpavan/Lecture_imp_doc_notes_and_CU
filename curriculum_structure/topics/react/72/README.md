# Static vs Dynamic Typed Languages

In programming, the terms "statically typed" and "dynamically typed" refer to when and how a programming language assigns data types. This classification has significant implications on how the code is written, tested, and executed.

### Static Typed Languages

Statically-typed languages require each variable and expression type to be explicitly declared or known at compile-time. Common statically-typed languages include Java, C, and C++.

```java
// Java example of static typing
int number = 5; // The variable 'number' is explicitly declared as an integer
```

**Characteristics:**

- **Compile-time Type Checking**: Errors and mismatches are caught early.
- **Performance**: Generally, faster execution after compilation.
- **Explicit Declarations**: Variables need explicitly assigned types.

### Dynamic Typed Languages

Dynamically-typed languages determine the type of a variable at runtime. This allows more flexibility but can lead to unexpected errors during execution. Examples include JavaScript, Python, PHP, and Ruby.

```python
# Python example of dynamic typing
number = 5 # The variable 'number' can hold any type of data
number = "five" # Now it holds a string
```

**Characteristics:**

- **Runtime Type Checking**: The type is inferred during execution.
- **Flexibility**: Easier to write but can lead to type-related runtime errors.
- **No Explicit Declarations**: Variables do not need types explicitly declared.