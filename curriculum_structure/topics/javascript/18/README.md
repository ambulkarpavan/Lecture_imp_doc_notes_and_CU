# Strings [15 min] (1)

- The string is a group of characters
- It can include a-z, A-z, 0-9, and also all special characters like #,@,$, etc
- Each character has an index, Starting from 0 to the length of the string.

### Need of Strings:

- Lots of information we stored, is actually stored as a string
- For Example, The name of the product, Pincode, and mobile number also, Since we
will not perform any mathematical operation on mobile numbers that's why we
considered it as a string.

### How to declare a String?

```jsx
String s = "Masai School"
There is a total of 12 characters in this string.
```

**Code 1: Declare a string variable and print it.**

```jsx
var name = "Masai";
console.log(name);
console.log(name[0]); // M
console.log(name[1]); // a
console.log(name[2]); // s
console.log(name[3]); // a
console.log(name[4]); // i
console.log(name[5]); // undefined
```

**Code 2: Find the length of the String.**

```jsx
var name = "Jantar Mantar";
console.log(name.length); // 13
```

### Real-world use of String:

**Code 3: Find whether the user enters a valid length password of
at least 6 characters.**

```jsx
var password = "vb";
if(password.length < 6)
{
console.log("Invalid : Your Password must be atleast 6 characters long");
}
else
{
console.log("Valid Password");
}
```

### **Loop in Strings:**

**Code 4: Run loop and print each character of String.**

```jsx
var name = "Masai School";
for(var i = 0; i<name.length; i++)
{
console.log(name[i]);
}
```

**Code 5: Run a loop on the string add each character to the third
variable and print that variable**.

```jsx
var name = "Masai School";
var bag = "";
for(var i = 0; i<name.length; i++)
{
bag = bag + name[i];
}
console.log(bag);
```