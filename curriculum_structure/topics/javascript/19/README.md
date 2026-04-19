# Arrays vs Strings [15 min] (1)

We can use an array to store the sequence of characters.

**Code 6: Store “Masai” in String and array.**

```jsx
var name1 = "Masai";
console.log(name1);
console.log(name1[0]);
var name2 = ["M","a","s","a","i"];
console.log(name2);
console.log(name2[0]);
```

**Strings are immutable**

Once the string is declared and initialized, it cannot be updated later.

**Code 7: Update Character in String**

```jsx
var name = "Masai";
name[0] = "N";
console.log(name); // Masai
```

Let’s use an array to update the string

**Code 8: Update Character in the array**

```jsx
var name = ["M","a","s","a","i"];
name[0] = "N";
console.log(name); // Nasai
```

We can conclude that strings are immutable. Once it is created, it cannot be updated
later but in the array it is possible.

### Update Strings

We already know that we can not update the string but we can update the array.

**Code 9: Update String using array and third variable. [First Method]**

```jsx
**I Way**
var name = "Masai";
var name2 = []
for(var i=0; i<name.length; i++)
{
name2.push(name[i]);
}
name2[0] = "N";
var bag = "";
for(var i=0; i<name2.length; i++)
{
bag = bag + name2[i];
}
console.log(bag);
```

**Code 10: Update String using array and third variable. [Second Method]**

```jsx
**II Way**
var name = "Masai";
var output = "";
for(var i=0; i<name.length; i++)
{
if(i==0)
{
output = output + "N";
}
else
{
output = output + name[i];
}
}
console.log(output); // Nasai
```

### Remove char in Strings:

loop in the given string and don’t add that character which you want to remove
otherwise add all.

**Code 11: Remove a char from String**

```jsx
var name = "Masai";
var output = "";
for(var i=0; i<name.length; i++)
{
if(name[i] != "s")
{
output = output + name[i];
}
}
console.log(output);
```

### **Problems in Strings:**

**Code 12: Count the names starting with N or n**

```jsx
var names = ["Nobita", "Naruto", "Noddy", "Shinchan", "Oswald"];
var count = 0;
for(var i=0; i<names.length; i++)
{
var name = names[i];
if(name[0] == "N" || name[0] == "n")
{
count++;
}
}
console.log(count);
```

### **Student Task:**

**Code 13: Count the names that contain A in them.**

```jsx
var names = [”Nobita”, “Naruto”, “Noddy”, “Shinchan”, “Oswald”];
var count = 0;
for(var i=0; i<names.length; i++)
{
var name = names[i];
for(var j = 0; j<name.length; j++)
{
if(name[j]=='a' || name[j]=='A')
{
count++;
break;
}
}
}
console.log(count);
```