# prefix & postfix [10 min] (1)

### **Increment & Decrement**

The increment and decrement operators in JavaScript will add one (+1) or subtract
one (-1).

| Increment | Decrement |
| --- | --- |
| var a = 5; a = a + 1;
console.log(a); | var a = 5; a = a - 1;
console.log(a); |

Javascript provides another way of incrementing and decrementing the variable i.e
`++`/`--`.

**Using ++/-- After the Operand**

- When you use the increment/decrement operator after the operand, the value will
be returned before the operand is increased/decreased.
- In simple terms, Postpone the operation for later instead of it first printing it.
- This is known as Postfix Increment/Decrement.

| Increment | Decrement |
| --- | --- |
| var a = 1 console.log(a++); console.log(a). | var a = 1;
console.log(a--); console.log(a); |

**Using ++/-- Before the Operand**

- When you use the increment/decrement operator after the operand, the value will
be increased/decreased returned before the operand is returned.
- Preponing the operation.
- This is known as Prefix Increment and decrement.

| Increment | Decrement |
| --- | --- |
| var a = 1; console.log(++a); console.log(a). | var a = 1; 
console.log(--a); console.log(a); |

### Examples of Prefix and Postfix

|  | Prefix | Postfix |
| --- | --- | --- |
| Increment | var a = 1; 
console.log(++a); console.log(a).
 | var a = 1; 
console.log(a++); 
console.log(a); |
| Decrement | var a = 1; 
console.log(--a); console.log(a). | var a = 1; 
console.log(a--); 
console.log(a); |

### Student Task

**Code 1: Predict the output**

```jsx
var a = 10;
++a;
var b = 10;
b++;
console.log(a)
console.log(b);
```

**Code 2: Predict the output**

```jsx
var a = 10;
var b = 10;
++a;
b++;
console.log(a);
console.log(b);
```