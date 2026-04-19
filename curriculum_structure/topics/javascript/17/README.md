# Array [60 min] (1)

### How do we store information?

We use variables to store the data.
For Example: If I want to store the name of a student, In that case, I will use a
variable

```jsx
var name = "Varun";
```

But What if, I want to store the names of 5 students

```jsx
var name1 = "Prateek";
var name2 = "Nrupul";
var name3 = "Yogesh";
var name4 = "Aman";
var name5 = "Albert";
```

To store 5 names, we need to declare 5 variables.
Isn’t possible that one variable will contain all names?
Yes, It is possible with the array.

### Arrays

The array is a contiguous chunk of memory that can store multiple values.
Declaration of an array

```jsx
var arr = [];
```

If I want to store all 5 names in a single variable, then it is possible through an array

```jsx
var arr = ["Prateek", "Nrupul","Yogesh","Aman","Albert"];
```

Each value is stored at some index.

the array index starts from 0.

**Code 1: Declare and print 3 students names using variables**

```jsx
var name1 = "Rahul";
var name2 = "Shubham";
var name3 = "Rishabh";
console.log(name1);
console.log(name2);
console.log(name3);
```

**Code 2: Declare and Print 3 students names using an array**

```jsx
var names = ["Rahul", "Shubham", "Rishabh"];
console.log(names[0]);
console.log(names[1]);
console.log(names[2]);
```

**Code 3: Perform the following tasks :**

1. **Create an array of vegetables**
2. **Store 3 vegetables**
3. **Print all the vegetable**

```jsx
var vegetables = ["Tomato", "Beans", "Onion"];
console.log(vegetables[0]);
console.log(vegetables[1]);
console.log(vegetables[2]);
```

**Note:** Don’t write `vegetables[3]` that will give `undefined`.

### **How to find the length of an array?**

- It means How many elements are present in the array.
- Use the length function to calculate the length.

**Code 4: Find the length of the vegetable array.**

```jsx
var vegetables = ["Tomato", "Beans", "Onion"];
console.log(vegetables.length);
```

**Code 5: Perform the following tasks :**

1. **Create an array price.**
2. **Store the prices of 3 products in the array**
3. **Print the price of the last product.**

Not a generic code :

```jsx
var prices = [45, 71, 29];
console.log(prices[2]);
```

Generic Code :

```jsx
var prices = [45, 71, 29];
last_index = prices.length-1;
console.log(prices[last_index]);
```

### **How to add elements in an array?**

push() function helps to insert the elements in an array.
push() always inserts at the last.

**Code 6: Insert 3 movie names in the arrays.**

```jsx
var items2 = [];
items2.push("Bahuballi");
items2.push("Avengers");
items2.push("Spider Man");
```

### **Students Task**

**Code 7: Perform the following tasks :**

1. **Create an array of superheroes**
2. and **push 3 superheroes into the array**
3. **Print the array**

```jsx
var superheroes = [];
superheroes.push("batman");
superheroes.push("superman");
superheroes.push("ironman");
console.log(superheroes);
```

### **How to update the array?**

Suppose I want to change the first index value.

```jsx
superheroes[0] = "Thor";
```

### How to print all elements using Loop?

Write a for loop from starting `i = 0` to the length of array - 1.
print all the elements using a loop.

**Code 8: print all the elements of the array using a loop.**

```jsx
var movies = [];
movies.push("batman");
movies.push("superman");
movies.push("ironman”);
for(var i = 0; i<movies.length; i++)
{
console.log(movies[i]);
}

```

**Note:** Don't run the loop till `movies.length`, It will show `undefined` for the last index
because last index doesn't exist for movies.

**Code 9: Perform the following tasks :**

1. **Create an array of movies and actors**
2. **Print all the movie names with the actors**

```jsx
var movies = ["bahuballi", "Spider Man", "Iron Man", "Super Man"];
var actors = ["Prabhas", "Tom holland", "Robert Downey", "Henry Cavil"];
for(var i=0; i<movies.length; i++){
console.log(movies[i]," - ",actors[i]);
}
```

**Note:** The length of both arrays should be the same.

### How to remove elements from an array?

To remove elements, we have a `pop()` function
`pop()` function that will remove elements from the last.

**Code 10: pop the last 2 elements from an array**

```jsx
var movies = [];
movies.push("batman");
movies.push("superman");
movies.push("ironman");
movies.pop();
movies.pop();
console.log(movies);
```

### Students Task

**Code 11: Perform the following tasks :**

**1. Create an array of 6 numbers
2. print the numbers array
3. delete the last 3 numbers from that array
4. print the numbers array**

```jsx
First Way
var numbers = [2,3,4,5,6,7];
console.log(numbers);
numbers.pop();
numbers.pop();
numbers.pop();
console.log(numbers);
```

```jsx
Second Way
var numbers = [2,3,4,5,6,7];
console.log(numbers);
for(var i=1; i<=3; i++)
{
numbers.pop();
}
console.log(numbers);
```

### **Arrays with Loop and Break**

**Code 12: Print the first 3 items in the array using a loop.**

```jsx
First Way
var movies = ["bahuballi", "SpiderMan", "IronMan", "SuperMan"];
for(var i = 1; i<=3; i++)
{
console.log(movies[i]);
}
```

```jsx
Second Way [ Using Break ]
var movies = ["bahuballi", "SpiderMan", "IronMan", "SuperMan"];
for(var i = 0; i<movies.length; i++)
{
if(i==3)
{
break;
}
console.log(movies[i]);
}
```

### **Arrays with Loop and Continue**

**Code 12: Print all movies except the third movie.**

```jsx
var movies = ["bahuballi", "SpiderMan", "IronMan", "SuperMan"];
for(var i = 0; i<movies.length; i++)
{
if(i==2)
{
continue;
}
console.log(movies[i]);
}
```

**Code 13: Print all movies except the third and fifth movies.**

```jsx
var movies = ["bahuballi", "SpiderMan", "IronMan", "SuperMan","hulk","thor"];
for(var i = 0; i<movies.length; i++)
{
if(i==2 || i==4)
{
continue;
}
console.log(movies[i]);
}
```

**Code 14: Print the last 3 items of an product array**

```jsx
**Approach 1:**
var products = ["earphone", "headphones", "mic", "ipad", "cell phone", "laptop"];
var start = products.length - 3;
for(var i=start; i<products.length; i++)
{
console.log(products[i]);
}
```

Above Approach 1 will fail, if suppose the products array is
`var products = ["earphone", "headphones"]`;

```jsx
**Approach 2:**
var products = ["earphone", "headphones", "mic", "ipad", "cell phone", "laptop"];
var start = 0;
if(products.length>3)
{
start = products.length - 3;
}
for(var i=start; i<products.length; i++)
{
console.log(products[i]);
}
```

**Code 15: For Even Array, print the second half of the array**

```jsx
var names = ["A","B","C","D","E","F","G","H"];
var start = Math.floor(names.length/2);
for(var i=start; i<names.length; i++)
{
console.log(names[i]);
}
```

**Code 16: For Even or Odd Array, print the second half of the array**

```jsx
var names = ["A","B","C","D","E","F","G","H","K"];
var start=0;
// Handle Even Array
if(names.length % 2 == 0)
{
start = names.length/2;
}
// Handle Odd Array
else
{
start = Math.floor(names.length/2);
}
for(var i=start; i<names.length; i++)
{
console.log(names[i]);
}
```

**Code 17: For Even or Odd Array, print the first half of the array**

```jsx
var names = ["A","B","C","D","E","F","G","H","K"];
var start=0;
if(names.length % 2 == 0)
{
end = names.length/2;
}
else
{
end = Math.floor(names.length/2);
}
for(var i=0; i<end; i++)
{
console.log(names[i]);
}
```

**Code 18: Given marks, find the total marks**

```jsx
var marks = [10, 15, 19, 20, 21];
var sum=0;
for(var i = 0; i<marks.length; i++)
{
sum = sum+marks[i];
}
console.log(sum);
```

**Code 19: Find the sum of all subject marks and average also.**

```jsx
var subject_marks = [10, 15, 19, 20, 21];
var sum_marks = 0;
for(var i=0; i<subject_marks.length; i++)
{
sum_marks = sum_marks + subject_marks[i];
}
var average = Math.floor(sum_marks/subject_marks.length);
console.log("Total sum is ",sum_marks);
console.log("Average is ",average);
```

**Code 20: Given marks, find the maximum marks**

```jsx
var marks = [10, 15, 19, 20, 21,45, 31, 18];
var max = -Infinity;
for(var i = 0; i<marks.length; i++)
{
if(max<marks[i])
{
max = marks[i];
}
}
console.log(max);
```