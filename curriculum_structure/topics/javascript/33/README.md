# DOM-2 (1)

## Forms in Javascript:

- Forms will generally contain input tags.
- Take an example of any application form online, it consists of many input tags.
- So, whenever you are using some kind of input tags, where you want to take input from user, use forms.
- There are certain steps needs to be followed while using forms

## Steps:

1. Wrap your input tags inside form tag.
2. Instead of button tag you should use `<input type="submit"/>`
3. Add eventListener to `form` tag.
4. Event name should be `submit` 
    
    ```jsx
    addEventListener("submit", myFunction)
    ```
    
5. Forms by default tries to send data to backend when you click on submit, to stop default behaviour use `event.preventDefault()`

- Let’s see the difference between onClick and addEventListener by looking into following example

### Without using form tag

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
    <input id="name" type="text" placeholder="enter name" />
    <input id="mail" type="email" placeholder="Enter email address" />
    <button onClick="getData()">Submit</button>
    <h1 id="nameDisplay">display name here</h1>
    <h2 id="emailDisplay">display email here</h2>
  </body>
</html>

<script>
  function getData() {
    var username = document.getElementById("name").value;
    var email = document.getElementById("mail").value;
    document.getElementById("nameDisplay").innerText = username;
    document.getElementById("emailDisplay").innerText = email;
  }
</script>
```

Live code : [Codepen](https://codepen.io/vchandu111/pen/LYQQzJL)

### With Form tag

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
    <form>
      <input id="name" type="text" placeholder="enter name" />
      <input id="mail" type="email" placeholder="Enter email address" />
      **<input type="submit" />**
    </form>
    <h1 id="nameDisplay">display name here</h1>
    <h2 id="emailDisplay">display email here</h2>
  </body>
</html>

<script>
  **document.querySelector("form").addEventListener("submit", getData);**
  function getData() {
****    var username = document.getElementById("name").value;
    var email = document.getElementById("mail").value;
    document.getElementById("nameDisplay").innerText = username;
    document.getElementById("emailDisplay").innerText = email;
  }
</script>
```

Live code : [Codepen](https://codepen.io/vchandu111/pen/eYVVGPp)

> What is happening here? You can see the data for a sec and it is disapperaing right? Why?
> 

> Because everytime we submit a form, the default behaviour of form is to send data to the backend. Since there is no backend here, it is disappearing. So, what should we do in order to prevent this default behaviour of the submit event in form?
> 

There is a method called preventDefault in event. Let’s see how to use it.

```jsx
**event.preventDefault();**
```

## **preventDefault()**

- The preventDefault() method cancels the event if it is cancelable, meaning that the default action that belongs to the event will not occur.
- For example, this can be useful when:
    - Clicking on a "Submit" button, prevent it from submitting a form.
    - Clicking on a link, prevent the link from following the URL.

> ***Till now for displaying data, what did we do? We created tags in html before only and just added innerText, right? But how will we do it in case of tables. Let’s say, we need to store the data in a table from JS. We can create table tag, thead and tbody in html. But what about the tr and td tags inside the tbody? So, we need to create elements or tags in script tag itself, right?***
> 

# **Document createElement()**

- The `createElement()` function in JavaScript is used to programatically add elements to the DOM.

## Syntax

```jsx
document.createElement(*type*)
```

- It has one required argument, the type of element to create, like `'div'` or `'img'`.
- Let’s see how we generally create an element using HTML.
- For Example I want to create a <h1> tag with innertext of Masai School

```html
<html lang="en">
<head>
  <title>Document</title>
</head>
<body>
  <h1>Masai School</h1>
</body>
</html>
```

- What are the steps we followed here?
    1. We have created `<h1>` tag - `<h1> </h1>`
    2. We have added innerText to it - `<h1>Masai School</h1>`
- Now let’s try to create same h1 tag using javascript by following same steps

```jsx
<html lang="en">
<head>
  <title>Document</title>
</head>
<body>
</body>
</html>

<script>
  // Step1: Creating h1 tag
  let heading = document.createElement("h1");
  // Step2: Adding innerText 
  heading.innerText = "Masai School";
</script>
```

Live code : [Codepen](https://codepen.io/vchandu111/pen/abqqLrJ)

> ***Now that we’ve created the h1 tag, is this fine? Will it add h1 and give us the required output?***
> 

Why won’t we see?

Because any tag which we see on our browser should be inside the body tag , right? We’ve created a h1 tag but did we keep it inside body? So, let’s see how to keep the h1 tag we created in the script tag to be kept inside the body tag.

3. We have added(appended) `h1` tag to `body` tag in order to display it on browser.

```jsx
  // Step3: Appending to body
  document.querySelector("body").append(heading)
```

If I want to add a heading 2 and heading 3 also.

```jsx
<html lang="en">
<head>
  <title>Document</title>
</head>
<body>
</body>
</html>

<script>
  let heading = document.createElement("h1");
  heading.innerText = "Masai School";
	document.querySelector("body").append(heading)

	let head2 = document.createElement("h2");
	 head2.innerText = "Part Time";
	let head3. = document.createElement("h3");
	 head3.innerText = "Batch 5";
  document.querySelector("body").append(head2,head3)
</script>
```

Similarly, how do we create and add a button?

```jsx
var btn = document.createElement("button");
```

For this button, if we add an event listener, how should we do it?

```jsx
btn.addEventListener("click",someFunction);
```

> ***Whenever we add an event to any element, an event object will be formed which provides us with some additional properties of event.***
> 

## Event Object:

### Where can we see or access this event object that is being created?

> ***We can access this event object inside the function parameter.***
> 

Let’s create a new file to see what all we can explore from the event object.

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>Masai school</h1>
    <div>
      <button>Click me</button>
    </div>
  </body>
</html>

<script>
  document.querySelector("h1").addEventListener("click", h1Fun);

  function h1Fun() {
    console.log(event.target);
    console.log(event.target.innerText);
    console.log(event.target.parentNode);
  }

  document.querySelector("button").addEventListener("click", btnFun);

  function btnFun() {
    console.log(event.target);
    console.log(event.target.innerText);
    console.log(event.target.parentNode);
  }
</script>
```

- When the event occurs, an event object is passed to the function as the first parameter. The type of the event object depends on the specified event. For example, the "click" event belongs to the MouseEvent object.

> ***Let’s see what is present in the field called target for both button and h1.***
> 

So, what is [event.target](http://event.target) giving us?

> [***Event.target](http://Event.target) is giving us the reference to the element upon which the event was fired, i.e, it is giving us the tag we are clicking to trigger that event.***
> 

## **What is event.target in JavaScript?**

- `target`, is a property of an event which is a reference to the element upon which the event was fired. Just as 'target' means 'aiming at something', it's used to 'aim' at that particular element.
- This property gives us access to the properties of that element.
- Since the target property has given us access to the element, we could then read some of the properties (which are the attributes) and also display them somewhere else.

### **Syntax**

The `target` property can only be obtained if the event of an `element` is being listened to.

> ***We can also access event without giving it as a parameter but we’ve use the whole name `event`. If we want to use e, we’ve to write e as a parameter inside the  function.***
> 

```jsx
element.addEventListener("click",myFunction)

function myFunction(){
	console.log(event) // //event.target is now accessible
}
```

### **Importance of event.target**

It is necessary to have the `target` property when an event is fired. We can do the following with the `target` property of the event.

- Get the `element` that fired the event.
- Access the properties of the `element`.
- Modify some properties of the `element`, such as the CSS, the attributes, etc.

# How do we create separate HTML, CSS and JS?

Till now, we’ve worked on a single file and created all the html, css and js components in the same file. But is that a good practice?

> ***If we create separate files for CSS, JS and HTML, then our code will look clean and we can debug easily because each file will be less in no of lines when compared to all the components in the same file.***
> 

```jsx
//linking CSS inside head
<link rel="stylesheet" href="file.css">

//linking JS
<script src="file.js"></script>
```

> ***Let’s separate the css and JS files now.***
> 

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="style.css">

	<style>
		background-color:yellow
	</style>

</head>
<body>
  
</body>
</html>

<script>
  console.log("Connected JS")
</script>
```

# Assignment Guidelines :

- Question will be in template form, template will consists of
    - HTML,CSS,JS file
- Don’t create your own files, just use given template.
- Don’t change any ID’s or classes given in template.
- Most of the cases HTML files will be given to you, no need to write any html tags, you need to just fill in JS and CSS files.

> ***Solve the question now and after solving, talk about the points below.***
> 
- After coding in JS files, you need to deploy it on netlify with logged in account (not free account)
    - Note: if you deploy on free account, your link will get expired
- You need to submit netlify link in submission section.

## Question to solve :

Deployed Link : [https://fluffy-souffle-6e0105.netlify.app/](https://fluffy-souffle-6e0105.netlify.app/)

[https://course.masaischool.com/problems/26355](https://course.masaischool.com/problems/26355)

Solution 

```jsx
document.querySelector("form").addEventListener("submit", myTodo);

function myTodo() {
  event.preventDefault();
  var task = document.querySelector("#task").value;
  var priority = document.querySelector("#priority").value;

  var tr = document.createElement("tr");
  var td1 = document.createElement("td");
  td1.innerText = task;

  var td2 = document.createElement("td");
  td2.innerText = priority;

  if (priority == "High") {
    td2.style.backgroundColor = "red";
  } else {
    td2.style.backgroundColor = "green";
  }

  var td3 = document.createElement("td");
  td3.innerText = "Delete";
  td3.addEventListener("click", deleteRow);
  td3.style.color = "red";
  tr.append(td1, td2, td3);
  document.querySelector("tbody").append(tr);
}

function deleteRow() {
  event.target.parentNode.remove();
	}
```

---

---

***don’t tell set attribute***

## **Element setAttribute()**

- The `setAttribute()` method sets a new value to an attribute.
- Here attributes can be any of the following
    - id
    - class
    - href
    - src, etc

# Syntax

```jsx
*element*.setAttribute(attributeN*ame*, attributeV*alue*)
```

**Example:**

```jsx
<html>
  <body>
    <div id="new">
      <p>Masai School</p>
    </div>
  </body>
</html>
<script>
      var newPara = document.createElement("p");
      newPara.innerText = "The Coding School that cares about you";
			// Setting class of "para" to p tag
			newPara.setAttribute("class","para")
			// Setting id of "container" to p tag
			newPara.setAttribute("id","container")
      document.getElementById("new").append(newPara);
</script>
```

- Now whatever styles we write for that class “para” or id “container” will be applied to that <p> tag

```jsx
<html>
<style>
.para {
	font-size:40px
}
</style>
  <body>
    <div id="new">
      <p>Masai School</p>
    </div>
  </body>
</html>
<script>
      var newPara = document.createElement("p");
      newPara.innerText = "The Coding School that cares about you";

			// Setting class of "para" to p tag
			newPara.setAttribute("class","para")

			// Setting id of "container" to p tag
			newPara.setAttribute("id","container")

      document.getElementById("new").append(newPara);
</script>
```

Live code : [Codepen](https://codepen.io/vchandu111/pen/RwQQxNw)

- Add a href attribute to an <a> element:

```jsx
myAnchor.setAttribute("href", "https://www.google.com");
```