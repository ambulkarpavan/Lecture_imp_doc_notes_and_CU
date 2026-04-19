# Objects [60 min] (1)

### Array vs Objects(Key-Value Pairs)

**Array**

```jsx
var subjects = ["maths", "sciene", "english", "Hindi"];
var marks = [40, 50, 80, 20];
```

here, I have two arrays one contains the subjects and the other contains the marks
of that respective subject.

- Suppose I want to find the marks in English, Then I need to search first in the
subjects array to find the subject index and then using that index I can directly
access the marks in the marks array.
- To access the information, the process is complex.

**Objects**

- It is a data structure that stores the data in a key-value manner.
- It is similar to any other forms that we have to fill in our daily lives,
one side is known as a key, which is telling what information you want to
store and the other side acts as a value representing the value of that information.

**Storing Information in Arrays vs Objects**

**Code 1: Declaring Arrays vs Objects**

```jsx
// Arrays
var user1 = ["Rahul", 25, "male", "Bangalore", "coding"];
// Objects
var user2 = {
name : "Rahul",
age : 25,
gender: "male",
city : "Bangalore",
hobbies: "coding"
};
console.log(user2);
```

**Note:** The key should be unique.

### Accessing information in Arrays vs Objects

**Code 2: Accessing the information gender in arrays vs objects**

```jsx
// Arrays
var user1 = ["Rahul", 25, "male", "Bangalore", "coding"];
console.log(user1[2];
// Objects
var user2 = {
name : "Rahul",
age : 25,
gender: "male",
city : "Bangalore",
hobbies: "coding",
marks : [25, 100, 80, 90, 80]
};
// 1. Bracket Notation
console.log(user["gender"]);
console.log(user["marks"]);
console.log(user["marks"][2]);
console.log(user["marks"].length);
// 2. Dot Notation
console.log(user.gender);
console.log(user.marks);
console.log(user.marks)[2]);
console.log(user.marks.length);
```

In Objects, we can access the information in two ways

1. **Bracket Notation :**
For Ex : `object["key"]`
2. **Dot Notation**
For Ex: `object.key`

**Adding information in Objects**

There are two ways to add information to an object

- **Bracket Notation :** `object["key"] = value`
- **Dot Notation:** `object.key = value`

**Code 3: Add the date of birth field in the given object.**

```jsx
// Objects
var user2 = {
name : "Rahul",
age : 25,
gender: "male",
city : "Bangalore",
hobbies: "coding",
marks : [25, 100, 80, 90, 80]
};
// Ist Way
user2['Date_of_Birth'] = "02-Oct-1984";
// IInd Way
user2.Date_of_Birth = "02-Oct-1984";
console.log(user2);
```

### Delete Information in Objects

to delete information use the keyword `delete`
`delete object[’key’] ;`
`delete object.key;`

```jsx
// Objects
var user2 = {
Objects 5
name : "Rahul",
age : 25,
gender: "male",
city : "Bangalore",
hobbies: "coding",
marks : [25, 100, 80, 90, 80]
};
// Ist way
delete user2["gender"];
// IInd way
delete user2["gender"]
console.log(user2);
```

### Object inside Object

- We can also store objects inside objects. Suppose I want to add information i.e
Address and Address will contain other subfields i.e State, Country, District,
Pincode, etc.
- To access the information, we can use either bracket or dot notation.

```jsx
// Objects
var user2 = {
name : "Rahul",
age : 25,
gender: "male",
city : "Bangalore",
hobbies: "coding",
marks : [25, 100, 80, 90, 80],
address : {
state : "Uttarakhand",
country : "india",
district : "Dehradun",
pincode : "249201"
}
};
//Bracket Notation
console.log(user["address"];
console.log(user["address"]["country"]);
console.log(user["address"]["pincode"]);
// Dot Notation
console.log(user.address);
console.log(user.address.country);
console.log(user.address.pincode);
```

### Loops in Objects:

- We have a special loop to iterate in objects.
- This special loop is known as, a `for-in loop`.

```jsx
var data2 = {
name : "Kaleen Bhaiyya",
age : 45,
gender : "male",
city : "Mirzapur",
hobbies : ["Making Guns"]
};
for(var key in data2)
{
console.log(key," --- ",data2[key]);
}
```

### IW Assignment:

**Problem 1 :**

Given an array find the unique items in the array

```jsx
// IW Problem1
var arr = ["Ramesh", "Suresh", "Ramesh", "Kamlesh", "Suresh", "Rupak"];
var party = [];
var present = false;
for(var i = 0; i<arr.length; i++)
{
Objects 7
for(var j=0; j<party.length; j++)
{
if(arr[i] == party[j])
{
present= true;
break;
}
}
if(present == false)
{
party.push(arr[i]);
}
else
{
present = false;
}
}
console.log(party);
```