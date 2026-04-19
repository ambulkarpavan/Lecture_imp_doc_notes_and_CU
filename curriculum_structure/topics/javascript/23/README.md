# Inbuilt Methods [60 min] (1)

**Code 1: using toString vs Number()**

```jsx
var num1 = 12;
var num2 = 13;
num1 = num1.toString();
num2 = num2.toString();
console.log(num1, num2);
var x = "21";
x = Number(x);
console.log(typeof(x));
```

**Code 2: lastIndexOf**

```jsx
var animals = ['Dodo', 'Tiger', 'Penguin', 'Dodo'];
console.log(animals.lastIndexOf("Dodo"));
var people = ["jamna das", "pandu", "kalicharan", "elaichi", "oggy", "pandu"];
console.log(people.lastIndexOf("jerry"));
```

**Code 3: indexOf**

```jsx
var animals = ['Dodo', 'Tiger', 'Penguin', 'Dodo'];
console.log(animals.indexOf("Dodo"));
var people = ["jamna das", "pandu", "kalicharan", "elaichi", "oggy", "pandu"];
console.log(people.indexOf("jerry"));
```

**Code 4: shift**

```jsx
var people = [1,2,3];
var x = people.shift();
console.log(people);
console.log("removed",x);
```

**Code 5: unshift**

```jsx
var arr = [1,2,3];
arr.unshift(4,5,6,7);
console.log(arr);
```

**Code 6: join**

```jsx
// Part 1 : Using Bag
var arr = ["M","A","N"];
var bag="";
for(var i=0; i<arr.length; i++)
{
bag = bag + arr[i];
}
console.log(bag);
// Part 2 : Using Bag
var bag = arr.join();
console.log(bag);
```

**Code 7: custom join**

```jsx
function customJoin(arr, char)
{
if(char == undefined)
{
char = ",";
}
var bag="";
for(var i=0; i<arr.length; i++)
{
if(i != arr.length-1)
{
bag = bag + arr[i] + char;
}
else
{
bag = bag + arr[i];
}
}
return bag;
}
var arr = ["M","A","N"];
console.log(customJoin(arr));
```

**Code 8: Slice**

```jsx
var animals = ["cat", "dog", "rat", "lion"];
var x = animals.slice(1,3);
console.log(x);
console.log(animals);
var animals = ["cat", "dog", "rat", "lion"];
var manu = animals.splice(2);
console.log("Manu :",manu);
console.log("Original",animals);
```

**Code 9 : toLowerCase() vs toUpperCase()**

```jsx
var sentence = 'The quick brown fox jumps over the lazy dog.';
console.log(sentence.toLowerCase());
var sentence = 'The quick brown fox jumps over the lazy dog.';
console.log(sentence.toUpperCase());
```

**Code 10: indexOf**

```jsx
var paragraph = 'The quick brown fox jumps over the lazy dog. If the dog barked, was it really lazy?';
var searchTerm = 'dog';
var indexOfFirst = paragraph.indexOf(searchTerm);
console.log(indexOfFirst);
```

**Code 11: split()**

```jsx
str = 'The quick brown fox';
var x = str.split(" ");
console.log(x);
```

**Code 12: Custom split mySplit()**

```jsx
function mySplit(str)
{
var output = [];
var bag = "";
for(var i=0; i<str.length; i++)
{
if(str[i] != " ")
{
bag = bag + str[i];
}
else
{
if(bag != ""){
output.push(bag);
}
bag = "";
}
}
output.push(bag);
return output;
}
var str = "The quick brown fox";
console.log(mySplit(str));
```