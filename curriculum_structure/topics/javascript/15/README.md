# While Loop [60 min] (1)

![Untitled](While%20Loop%20%5B60%20min%5D%20(1)%20bcafc35e03bb45b68a072002ae1d0b64/Untitled.png)

### Song Library

![Untitled](While%20Loop%20%5B60%20min%5D%20(1)%20bcafc35e03bb45b68a072002ae1d0b64/Untitled%201.png)

On Internet, When we listen to a song. There is an option of listening to the song in
the loop, it will play the song again and again when it reaches to end.

### Guests

![Untitled](While%20Loop%20%5B60%20min%5D%20(1)%20bcafc35e03bb45b68a072002ae1d0b64/Untitled%202.png)

- There are 10 guests coming to my home, After 2-3 days they decided to leave their
home.
- They all have the train on the same day and at the same time.
- I need to drop them at the railway station but I have one bike which can only take
one person at a time.
- In this case, I need to drop each guest one by one.
- Taking the First guest to the railway station, dropping them off, and arriving back and
following the same procedure again and again till the end.

### While Loop

- The while loop begins with a condition and it is written similarly to an if statement. The
inner parenthesis is the condition.
- As long as the condition is true, it will continue to execute the statement(s).
- To stop the loop, the condition must eventually become false.
- A common condition is to have a variable be less than or greater than compared to
a number.
- Within the statements, that variable will be incremented or decremented depending
on the condition.
- Each time the loop is executed, the variable will change and eventually become
larger or less than the number in the condition, stopping the loop.

### Let's try to understand the Loop Variables: Marathon Analogy

![Untitled](While%20Loop%20%5B60%20min%5D%20(1)%20bcafc35e03bb45b68a072002ae1d0b64/Untitled%203.png)

**Case 1 : Given a track of 100 m, Hari trains himself for a long Marathon of 100
meter. Hari standing at the 0th position and he needs to cover a 100-meter distance.**

Hari will make 1-meter jump at a time.
Let's take Hari's position as position = 0
After 1st jump, Hari will be at position = 1 meter
After 2nd jump, Hari will be at position = 2 meter
............................................................
After the 100th jump, Hari will be at position = 100 meter

**Observation**

![Untitled](While%20Loop%20%5B60%20min%5D%20(1)%20bcafc35e03bb45b68a072002ae1d0b64/Untitled%204.png)

the value of position is going as follows position = 0,1,2,3......100

1. The initial value of position = 0
2. The loop is running till position ≤ 100
3. At every point, Hari is making a jump of 1

**For Loops, 3 things are important :**

1. **Starting Point:** position = 0
2. **How long jump:** Jump of 1 meter
3. **Till When:** position≤100 meter
Syntax of While Loop

**Syntax of While Loop**

![Untitled](While%20Loop%20%5B60%20min%5D%20(1)%20bcafc35e03bb45b68a072002ae1d0b64/Untitled%205.png)

```jsx
Starting Point
While ( Till When )
{
How long Jump at a time?
}
-------------------------------------------------------------------------
Initialization
While ( Condition )
{
Increment/Decrement
}
```

```jsx
var position = 0
while(position <= 100)
{
position = position + 1;
}
```

![Untitled](While%20Loop%20%5B60%20min%5D%20(1)%20bcafc35e03bb45b68a072002ae1d0b64/Untitled%206.png)

**Understanding DRY RUN**

```jsx
var i = 0;
while(i<=5)
{
console.log("hello");
i = i + 1;
}
```

![Untitled](While%20Loop%20%5B60%20min%5D%20(1)%20bcafc35e03bb45b68a072002ae1d0b64/Untitled%207.png)

### While Loop Examples

**Code 1: Loop from 1 to 100 [1-meter jump at a time**

```jsx
var position = 0;
while(position <= 100)
{
position = position + 1;
console.log("Current Position ",position);
}
```

![Untitled](While%20Loop%20%5B60%20min%5D%20(1)%20bcafc35e03bb45b68a072002ae1d0b64/Untitled%204.png)

**Code 2: Infinite Loop**

```jsx
while(true)
{
console.log("Hello Masai");
}
```

**Code 3: Loop from 1 to 100 [2-meter jump at a time ]**

```jsx
var position = 0;
while(position<100){
console.log("Current Position ",position);
position = position + 2;
}
```

![Untitled](While%20Loop%20%5B60%20min%5D%20(1)%20bcafc35e03bb45b68a072002ae1d0b64/Untitled%208.png)

### Student Task

**Code 4: Loop from 1 to 100 [15-meter jump at a time ]**

```jsx
var position = 0;
while(position<100){
console.log("Current Position",position);
position = position + 15;
}
```

**Note : `!=` and `<` behave differently**

**Code 5: Loop from 35 to 100 [ 3 units jump at a time ]**

```jsx
var position = 35;
while(position<100){
console.log("Current Position",position);
position = position + 3;
}
```

**Code 6: Reverse Loop from 100 to 0 [ 1 unit jump at a time ]**

```jsx
var position = 100;
while(position>=0){
console.log("Current Position",position);
position = position - 1;
}
```

### Sending Notice to 1000 Employees

![Untitled](While%20Loop%20%5B60%20min%5D%20(1)%20bcafc35e03bb45b68a072002ae1d0b64/Untitled%209.png)

### Break

**Guest Analogy**

- There are 10 guests coming to my home, After 2-3 days they decided to leave their
home.
- They all have the train on the same day and at the same time.
- I need to drop them at the railway station but I have one bike which can only take
one person at a time.
- In this case, I need to drop each guest one by one.
- Taking the First guest to the railway station, dropping them off, and arriving back and
following the same procedure again and again till the end.
Suppose I took the First Guest and dropped him to the Railway station and come
back.
- Again I took the Second Guest and followed the same.
- Next, I took the third guest to the Railway station and found that the Train had gone.

**So, Will I continue the above procedure or stop it?**

Obviously, I will stop it and wait for tomorrow.

**Code 7: Loop from 0 to 10 (using break)**

```jsx
var guest=0;
while(guest<=10)
{
console.log("Guest",guest);
if(guest == 3)
{
break;
}
guest++;
}
```

### Student Task

**Code 8: Predict the output**

```jsx
var count=0;
while(true)
{
console.log("Hello");
count++;
++count;
if(count>5)
{
break;
}
count--;
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

**Code 11: Loop from 0 to 10 (using continue)**

```jsx
var guest=0;
while(guest<=10)
{
console.log("Guest",guest);
if(guest == 3)
{
continue;
}
guest++;
}
```

**Code 12: Find a Sum of 1 to 10**

```jsx
**Problem** :
// Sum of 1 to 10
// 1 + 2 + 3....... + 10
var i = 1;
var sum = 0;
while(i<=10)
{
sum = sum+i;
i++;
}
console.log(sum);
```