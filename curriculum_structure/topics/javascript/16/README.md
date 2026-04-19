# For Loop [60 min] (1)

![Untitled](For%20Loop%20%5B60%20min%5D%20(1)%209965d3b2d6d2425abaca816f3047d8f0/Untitled.png)

- Let’s say you want to display Masala Dosa one time then you will print the
console.log("Masala Dosa") one time.
- Similarly, If it is two then you will write console.log twice
- Let’s say you want to display it 100 times. Without some sort of loop in your code,
we would probably have to write the same line of code 100 times.

A for-loop can help us to do so by running the same code repeatedly under certain
conditions.

**Syntax**

![Untitled](For%20Loop%20%5B60%20min%5D%20(1)%209965d3b2d6d2425abaca816f3047d8f0/Untitled%201.png)

1. **Initialization:** Decides the starting point of a loop
2. **Condition:** Condition is checked before the execution of every iteration. If it
evaluates to true, the loop’s statement is executed. If it evaluates to false, the loop
stops.
3. **Iteration:** Iteration is used to affect your counter. It can be increment/decrement.
4. **Loop Body:** The loop body repeats the code as long as the condition part is TRUE.

### Three Ways of Writing For Loop

1. `for (initialize; condition; increment);`
2. `for (initialize; condition; increment) single statement;`
3. `for (initialize; condition; increment) { multiple; statements;}`

### Comparing For Loop Vs While Loop

![Untitled](For%20Loop%20%5B60%20min%5D%20(1)%209965d3b2d6d2425abaca816f3047d8f0/Untitled%202.png)

### The sequence of Execution of For Loop

![Untitled](For%20Loop%20%5B60%20min%5D%20(1)%209965d3b2d6d2425abaca816f3047d8f0/Untitled%203.png)

1. Initialization -> Condition -> Loop Body -> Iteration -> Condition -> Loop Body ->
Iteration and so one
2. Initialization is denoted as 1, Condition denoted as 2, Loop Body is denoted as 3,
Iteration denoted as 4.
3. Sequence of Execution will be : 1 -> 2 -> 3 -> 4 -> 2-> 3 -> 4 -> 2 -> 3 -> 4 and so
on

### Examples of For Loop with Dry Run

**Example 1: Print Hello 5 times.**

```jsx
for(var i=0; i<5; i++)
{
console.log("Hello");
}

```

![Untitled](For%20Loop%20%5B60%20min%5D%20(1)%209965d3b2d6d2425abaca816f3047d8f0/Untitled%204.png)

**Example 2: Print Values from 1 to 5**

```jsx
// Ist way : Output on new line
for(var i = 1; i<=5; i++){
console.log(i);
}
// IInd way: Output on a single line
var bag="";
for(var i = 1; i<=5; i++){
bag = bag + i + " ";
}
console.log(bag);
```

![Untitled](For%20Loop%20%5B60%20min%5D%20(1)%209965d3b2d6d2425abaca816f3047d8f0/Untitled%205.png)

**Example 3: Print multiple of 2 values from 1 to 10**

```jsx
// Ist way : Output on new line
for(var i = 1; i<=10; i=i*2){
console.log(i);
}
// IInd way : Output on single line
var bag="";
for(var i = 1; i<=10; i=i*2){
bag = bag + i + " ";
}
console.log(bag);
```

![Untitled](For%20Loop%20%5B60%20min%5D%20(1)%209965d3b2d6d2425abaca816f3047d8f0/Untitled%206.png)

**Example 4: Reverse Loop from 5 to 1**

```jsx
var bag = "";
for(var i = 5; i>0; i--){
bag = bag + i + " ";
}
console.log(bag);
```

![Untitled](For%20Loop%20%5B60%20min%5D%20(1)%209965d3b2d6d2425abaca816f3047d8f0/Untitled%207.png)

**Example 5: Factorial**

```jsx
var fact = 1;
for(var i=1; i<=5;i++)
{
fact = fact * i;
console.log(fact);
}
```

![Untitled](For%20Loop%20%5B60%20min%5D%20(1)%209965d3b2d6d2425abaca816f3047d8f0/Untitled%208.png)

**Example 6: Find Sum 1 to N**

```jsx
var N = 5;
var sum = 0;
for(var i = 1; i<=N; i++){
sum = sum + i;
}
console.log(sum);
```

![Untitled](For%20Loop%20%5B60%20min%5D%20(1)%209965d3b2d6d2425abaca816f3047d8f0/Untitled%209.png)

### Break

**Guest Analogy**

- There were 10 guests who came to my home, After 2-3 days they decided to leave.
- They all have the train on the same day and at the same time.
- I need to drop them at the railway station but I have one bike which can only take
one person at a time.
- In this case, I need to drop each guest one by one.
- Taking the First guest to the railway station, dropping them off, and arriving back and
following the same procedure again and again till the end.
- Suppose I took the First Guest and dropped him to the Railway station and come
back.
- Again I took the Second Guest and followed the same.
- Now, I took the third guest to the Railway station and found that the Train had gone.

**So, Will I continue the above procedure or stop it?**

Obviously, I will stop it and wait for tomorrow

**Code 7 : Loop from 1 to 10 (using break). Using console.log before break
statement**

```jsx
for(var guest=1; guest<=10; guest++)
{
console.log("guest ",guest,"got the train");
if(guest == 3){
break;
}
}
```

**Code 8 : Loop from 1 to 10 (using break). Using console.log after break statement**

```jsx
for(var guest=1; guest<=10; guest++)
{
if(guest == 3){
break;
}
console.log("guest ",guest,"got the train");
}
```

### Continue

**Guest Analogy**

- There are 10 guests coming to my home, After 2-3 days they decided to leave their
home.
- They all have the train on the same day and at the same time.
- I need to drop them at the railway station but I have one bike which can only take
one person at a time.
- In this case, I need to drop each guest one by one.
- Taking the First guest to the railway station, dropping them off, and arriving back and
following the same procedure again and again till the end.
- Suppose I took the First Guest and dropped him to the Railway station and come
back.
- Again I took the Second Guest and followed the same.
- Suppose the third guest is Sick, In that case, I will skip him.
- and I will continue with the fourth guest and follow the same procedure.

**Code 9: Loop from 1 to 10 (using Continue). Using console.log before continue
statement**

```jsx
for(var guest=1; guest<=10; guest++)
{
console.log("guest ",guest,"got the train");
if(guest == 3){
continue;
}
}
```

**Code 10: Loop from 1 to 10 (using Continue). Using console.log after continue
statement**

```jsx
for(var guest=1; guest<=10; guest++)
{
if(guest == 3){
continue;
}
console.log("guest ",guest,"got the train");
}
```

**Code 11: Predict the output.**

```jsx
var count = 1;
for(var i = 1; i<10; i++)
{
count++;
if(i==5){
continue;
}
}
console.log(count);
```

**Code 12: Predict the output.**

```jsx
var count = 1;
for(var i = 1; i<10; i++)
{
if(i==5){
continue;
}
count++;
}
console.log(count);
```