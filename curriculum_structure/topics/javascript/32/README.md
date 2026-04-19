# DOM-1 (1)

> Till now, we’ve built static web pages. That means our webpage did not interact with the user, right? Let’s see an alalogy of what a DOM is.
> 

## **What is DOM?**

- Imagine this🤔 you are watching TV and you don't like the show that's being streamed, and you want to change it and you also want to increase its volume. To do that, there has to be a way for you to interact with your television. So how do you control your tv now?
- By using `remote`

![Screenshot 2022-05-11 at 3.51.28 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_3.51.28_PM.png)

- The remote serves as the **bridge** which allows you interact with your television.
- In the same way, JavaScript helps you to interact with the HTML page via **DOM.**
- For example, say that you want a button to change colours when it gets clicked or you want text to be changed. First, you need to reference those elements from your JavaScript.
- The DOM is a tree-like representation of the web page that gets loaded into the browser.
- Whenever html document is loaded on browser, corresponding to that document another representation of document is created which is known as DOM.
- Let’s suppose you have this code

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Text</title>
  </head>
  <body>
    <h1>My Header</h1>
    <p>My Paragraph</p>
  </body>
</html>
```

The Document Object Model (DOM) is an interface for web documents. It represents the page so that programs can change the document structure, style, and content. The DOM represents the document as nodes and objects; that way, programming languages can interact with the page.

A web page is a document that can be either displayed in the browser window or as the HTML source in our vs code, right?. In both cases, it is the same document but the DOM representation of this document allows it to be manipulated as an object-oriented representation.  Now that it is an object-orinted representation, it can be modified with a scripting language such as JavaScript.

- If you open this in browser, the web browser creates a DOM of the webpage when the page is loaded. The DOM model is created as a tree of objects like this

![javascript8_1.webp](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/javascript8_1.webp)

## HTML meets 🤝 JS

![Screenshot 2022-05-11 at 3.33.08 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_3.33.08_PM.png)

## How to add JS inside HTML

```html
<html>
<head>
  <title>Connecting JS</title>
</head>
<body>
</body>
</html>

<script>
	function doSomething(){
		 // Your Code Goes Here
	}
</script>
```

- Inside script tag you can write your js code

## Console.log():

- console.log() in javascript is your best friend life long

![Screenshot 2022-05-11 at 4.53.33 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_4.53.33_PM.png)

### Where to find your best friend ?

- As you already know, you should use console inside your js code, so I am writing console.log() in script tag

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Text</title>
  </head>
  <body>
    <h1>My Header</h1>
    <p>My Paragraph</p>
  </body>
</html>
<script>
	console.log("Oh my Friend")
</script>
```

- Now, where can I find my best friend

> Till now, if it is a .js extension, we can run it in our vs code only using `node filename` .But, this is a .html extension and we know we can open html extension in our browser, then where can we see this console from browser.
> 
- Step-1: Run HTML file on browser.
- Step-2: Right click and click on inspect.
- Step-3: You can see console beside Elements
    
    ![Screenshot 2022-05-11 at 5.03.05 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_5.03.05_PM.png)
    

- Now with help of your friend let’s see what is hiding in our window and document.
    
    

![Screenshot 2022-05-25 at 11.14.53 AM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-25_at_11.14.53_AM.png)

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Text</title>
  </head>
  <body>
    <h1>My Header</h1>
    <p>My Paragraph</p>
  </body>
</html>
<script>
	console.log(window)
</script>
```

> ***Show window object and document object from here and show the difference of how DOM is creating the objects and nodes representation of the html file.***
> 

**Output**

![Screenshot 2022-05-11 at 5.07.37 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_5.07.37_PM.png)

Similar to how we access keys in our object, we can access keys of our document also. Then what will be the output of 

```jsx
// URL of a page
console.log(document.URL)
// title of a page
console.log(document.title)
// domain
console.log(document.domain)
// doctype
console.log(document.doctype)
// head
console.log(document.head)
// body
console.log(document.body)
// all elements
console.log(document.all)
// forms
console.log(document.forms)
// links
console.log(document.links)
// images
console.log(document.images)

```

Similar to how the channel can change using the remote of our TV, or the vol decreases or increases by using the remote. In the similar manner, let’s see how we can create some buttons and make them interactive.

Example:

```jsx
<html>
<head>
      <title>OnClick</title>
</head>
<body>
      <button onClick="likeMe()">Like👍</button>
</body>
</html>
```

Now what should we do with a button, we will click on the button, right?

So, what is this on click, it is some action that the user is doing right? The actions that a user can do or the actions that will interact with the user or the browser are called events. So, onClick is an event. 

Now that we have seen what an event is, how do we describe what should happen on clicking that button? We are writing a function, right?

We know how to access functions in JS and write some logic there. So, we have to define the function in JS, i.e, script tag. 

- Now we need to define this function in javascript to make it work

```jsx
<script>
      function likeMe() {
            console.log("Someone liked me")
      }
</script>
```

## [onClick Event:](https://www.w3schools.com/jsref/event_onclick.asp)

![poke-poking.gif](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/poke-poking.gif)

- The `onclick` event occurs when the user clicks on an element.
- The `onclick`event executes a certain functionality when a button/element is clicked.

[OEAO.mp4](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/OEAO.mp4)

**Basic `onclick` syntax:**

```jsx
<element onclick="functionToExecute()">Click</element>
```

- Now when we click on “Like” button, we will get `“Someone liked me”` in console

![Screenshot 2022-05-11 at 5.44.25 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_5.44.25_PM.png)

- Let’s dry run it

![Screenshot 2022-05-11 at 5.59.43 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_5.59.43_PM.png)

## [Alert():](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert)

- The **alert()** method in JavaScript is used to display a virtual alert box.
- It is mostly used to give a warning message to the users. It displays an alert dialog box that consists of some specified message (which is optional) and an OK button.
- When the dialog box pops up, we have to click "OK" to proceed.

![Show_an_alert_dialog_in_JavaScript_Example.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Show_an_alert_dialog_in_JavaScript_Example.png)

### Syntax

```jsx
alert(message)
```

- In the above example instead of console, we will try to keep alert

```jsx
<html>
<head>
      <title>OnClick</title>
</head>
<body>
      <button onClick="likeMe()">Like👍</button>
</body>
</html>

<script>
      function likeMe() {
            alert("Someone liked me")
      }
</script>
```

**Output**

![Screenshot 2022-05-11 at 6.06.02 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_6.06.02_PM.png)

***You might have seen some websites ask for location access when you are opening it using alert boxes, right?***

## **[Document.getElementById()](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById#syntax)**

We’ve seen how we can apply styles to our html elements in style tag by giving ids, classes and selectors, combinators, right?

We can do the same without style tag and using Javascript as well. But first let us see how we can access these html elements in javascript.

**Example:**

```jsx
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
      <p id="para">I am paragraph</p> 
      <div id="box">I am box</div>
      <h1 id="head-1">I am heading 1</h1> 
  </body>
</html>

<script>
      console.log(document.getElementById("para"))
      console.log(document.getElementById("box"))
      console.log(document.getElementById("head-1"))

</script>
```

**Output**:

![Screenshot 2022-05-11 at 6.19.04 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_6.19.04_PM.png)

## Syntax

```jsx
document.getElementById(id_Name)
```

### Parameters

- `id`The ID of the element to locate. The ID is case-sensitive string which is unique within the document; only one element may have any given ID.

### Return value

- An `[Element](https://developer.mozilla.org/en-US/docs/Web/API/Element)` object describing the DOM element object matching the specified ID, or `null` if no matching element was found in the document.
- The `[Document](https://developer.mozilla.org/en-US/docs/Web/API/Document)` method **`getElementById()`** returns an `[Element](https://developer.mozilla.org/en-US/docs/Web/API/Element)` object representing the element whose `[id](https://developer.mozilla.org/en-US/docs/Web/API/Element/id)` property matches the specified string.

## innerText (or) textContent:

- Do you remember in our first class we have discussed about `HTML elements`

![a.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/a.png)

- The content inside opening and closing tag is called as `innerText` also called as `textContent`
- The `innerText` property sets or returns the text content of an element.

## Syntax

```jsx
*element*.innerText
```

**Example:**

Let’s take previous example and try to get innerText of tags

```jsx
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
      <p id="para">I am paragraph</p> 
      <div id="box">I am box</div>
      <h1 id="head-1">I am heading 1</h1> 
  </body>
</html>

<script>
      console.log(document.getElementById("para").innerText)
      console.log(document.getElementById("box").innerText)
      console.log(document.getElementById("head-1").innerText)

</script>
```

**Output**:

![Screenshot 2022-05-11 at 6.58.46 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_6.58.46_PM.png)

## innerText vs innerHTML

Example: 

`<i>` tag is italic tag

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>innerText vs innerHTML</title>
  </head>
  <body>
    <div id="box">Welcome to <i> Masai School </i></div>
  </body>
</html>

<script>
      console.log(document.getElementById("box").innerText)

      console.log(document.getElementById("box").innerHTML)

</script>
```

**Output**:

![Screenshot 2022-05-12 at 10.22.15 AM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-12_at_10.22.15_AM.png)

- From the above example you can clearly see that
    - `innerText` is retreiving only text inside tags
    - `innerHTML` is retreiving with HTML elements (<i> tag)
    

## Changing innerText of an element

- Javascript provides us with the `innerText` property that we can use to change the text inside an element.

Syntax: 

```jsx
 element.textContent = "new_value" or
 element.innerText = "new_value" 
```

Example:

```jsx
<html>
<body>
  <h1 id="head">Amitabh bachan</h1>
	<button onClick="changeHeading()">Change heading</button>
</body>
<script>
	function changeHeading(){
	  document.getElementById("head").innerText = "Rajnikanth";
	}
</script>
</html>
```

Example 2 : [Codepen](https://codepen.io/vchandu111/pen/PoQGqeV)

## Value:

We have seen how to create an input tag, right? Now, after creating the input tag, we can use it to fill forms such as this. But what is the purpose of forms?

Forms are used to collect data and store that data. So, now we will see how to collect this data from an input tag.

- While interacting with users, its important to take few inputs from users, for eg:form inputs

### Getting values from Input tags

- In HTML introduction we have seen so many input tags.
- We have also seen masai form

![input.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/input.png)

- To interact with user, we need to get the value of
    - Full name
    - Email
    - Password
- How to get those values?
    - For getting those values we have an `attribute` in input tag known as `value` which is by default empty.

```jsx
<input type="text" value=""/>
```

- Try to type in some value and check the output

```jsx
<input type="text" value="Masai School"/>
```

Output:

![Screenshot 2022-05-12 at 10.54.21 AM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-12_at_10.54.21_AM.png)

- So, whatever we type in that input box, we can capture that in `value` attribute.

Example:

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
    <input id="name" type="text" value="" />
    <button onClick="catchValue()">Submit</button>
  </body>
</html>

<script>
  function catchValue() {
    var studentName = document.getElementById("name").value;
    console.log(studentName);
  }
</script>
```

Output:

![Screenshot 2022-05-12 at 11.13.42 AM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-12_at_11.13.42_AM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/oNEzjNM)

Example 2 : [Codepen](https://codepen.io/nrupuld/pen/zVBJaa)

## Displaying data on Browser

- Untill now we just got the value and displayed in console, but in real-world apps, we need to show data to users also
- Let’s take above example of taking input value of name from the user, instead of consoling the name , let’s try to print name on browser.
- For that let’s create <h1> tag in the body and we will try to fill in innerText

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
    <input id="name" type="text" value="" />
    <button onClick="catchValue()">Submit</button>
    <!-- Show output here -->
    <h1 id="output"></h1>
  </body>
</html>

<script>
  function catchValue() {
    var studentName = document.getElementById("name").value;
    document.getElementById("output").innerText = studentName;
  }
</script>
```

Output:

![Screenshot 2022-05-12 at 11.21.27 AM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-12_at_11.21.27_AM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/WNMGQrr)

### Getting values from Select tags

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
    <select id="gender">
      <option value="">Select gender</option>
      <option value="MALE">Male</option>
      <option value="FEMALE">Female</option>
    </select>
    <button onClick="getGender()">Submit</button>
  </body>
</html>

<script>
  function getGender() {
    var gen = document.getElementById("gender").value;
    console.log(gen);
  }
</script>
```

Live code : [Codepen](https://codepen.io/vchandu111/pen/dydpYax)

# **Styling DOM Elements in JavaScript**

- You can also apply style on HTML elements to change the visual presentation of HTML documents dynamically using JavaScript.
- You can set almost all the styles for the elements like, fonts, colors, margins, borders, background images, text alignment, width and height, position, and so on.

### **Setting Inline Styles on Elements**

- Inline styles are applied directly to the specific HTML element using the style attribute. In JavaScript the `style` property is used to get or set the inline style of an element.
- The following example will set the color and font properties of an element with `id="intro"`.

```jsx
<html lang="en">
<head>
    <title>JS Set Inline Styles Demo</title>
</head>
<body>
    <p id="intro">This is a paragraph.</p>
    <p>This is another paragraph.</p>
</body>
</html>
<script>
    // Selecting element
    var elem = document.getElementById("intro");

    // Appling styles on element
    elem.style.color = "blue";
    elem.style.fontSize = "18px";
    elem.style.fontWeight = "bold";
</script>

```

**Output:**

![Screenshot 2022-05-27 at 12.37.01 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_12.37.01_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/PoQEJmd)

> ***Similar to getElementById, we have getElementsByTagName and getElementsByClassName, but there is a drawback in this. Can anyone tell me what the drawback is?***
> 

- The drawback of above methods is, we are using different syntax for different methods, right.
- So now we will see a method where we can access/catch element by its
    - tagName
    - className
    - id
- These methods are known as `querySelector` and `querySelectorAll`

# **querySelector():**

### Syntax

```jsx
document.querySelector(CSS selector)
```

> ***Selector can be anything ⇒ class, id, tag, combinators. So we can use any of these as selector in the querySelector.***
> 
- Here selectors can be any selector (id,class,tag,universal)

**Example**

```jsx
<html>
  <body>
    <p>This is a first p element.</p>
    <p>This is a second p element.</p>
    <p>This is a third p element.</p>
  </body>
</html>
<script>
  document.querySelector("p").style.backgroundColor = "red";
</script>
```

Output:

![Screenshot 2022-05-27 at 12.41.29 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_12.41.29_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/zYRpEzB)

- In the above example, `querySelector` is making background color red to only first element that matches
- Let’s take one more example

```jsx
<html>
  <body>
    <p class="example">I am first paragraph.</p>
    <p class="example">I am second paragraph.</p>
  </body>
</html>
<script>
  document.querySelector(".example").style.backgroundColor = "teal";
</script>
```

**Output**

![Screenshot 2022-05-27 at 12.44.56 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_12.44.56_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/vYdpeZd)

- In the above example, `querySelector` is making background color teal to only first element that matches query class example
- We can also use combinators here, but even with combinators it will only return first element

Example:

```jsx
<html>
  <body>
    <h2>Masai School Students</h2>
    <p>Manish</p>
    <p>Vikash</p>
    <p>Charan</p>
    <p>Mounika</p>
  </body>
</html>
<script>
  document.querySelector("h2~p").style.backgroundColor = "teal";
</script>
```

- Basically `h2~p` should return all p’s, but `querySelector` will return only first p, in this case Manish

**Output**:

![Screenshot 2022-05-27 at 12.53.04 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_12.53.04_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/QWQaqqX)

- The `querySelector()` method returns the **`first`** element that matches a CSS selector.

- To return **all** matches (not only the first), use the `querySelectorAll()` instead.

# **querySelectorAll():**

- The `querySelectorAll()` method returns all elements that matches a CSS selector(s).
- The `querySelectorAll()` method returns a NodeList.

### Syntax

```jsx
document.querySelectorAll(CSS selectors)
```

- Here selectors can be any selector (id,class,tag,universal)
- Let’s take the same examples as querySelector

```jsx
<html>
  <body>
    <p>This is a first p element.</p>
    <p>This is a second p element.</p>
    <p>This is a third p element.</p>
  </body>
</html>
<script>
  // This won't work because querySelectorAll() method returns a NodeList.
  // document.querySelectorAll("p").style.backgroundColor = "red";
  // So we need to use for loop to select all elements

  var list = document.querySelectorAll("p");
  for (var i = 0; i < list.length; i++) {
    list[i].style.backgroundColor = "red";
  }
</script>
```

**Output**

![Screenshot 2022-05-27 at 1.18.45 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_1.18.45_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/JjpMrzO)

**Example 2**

```jsx
<html>
  <body>
    <p class="example">I am first paragraph.</p>
    <p class="example">I am second paragraph.</p>
  </body>
</html>
<script>
  var list = document.querySelectorAll(".example");
  for (var i = 0; i < list.length; i++) {
    list[i].style.backgroundColor = "teal";
  }
</script>
```

Output:

![Screenshot 2022-05-27 at 1.21.13 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_1.21.13_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/NWyXaVW)

**Example 3:**

```jsx
<html>
  <body>
    <h2>Masai School Students</h2>
    <p>Manish</p>
    <p>Vikash</p>
    <p>Charan</p>
    <p>Mounika</p>
  </body>
</html>
<script>
    var list = document.querySelectorAll("h2~p");
    for (var i = 0; i < list.length; i++) {
    list[i].style.backgroundColor = "teal";
  }

</script>
```

Output:

![Screenshot 2022-05-27 at 1.24.05 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_1.24.05_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/JjpMrQM)

## Questions to solve

`25245 - DOM SELECTORS`

**Solution**:

```jsx
function changeH1() {
        // the colour of first <h1> should turn to red
        document.querySelector("h1").style.color = "red";
      }

      function changeH3() {
        // the colour of all <h3> should turn to green
            var h3s= document.querySelectorAll('h3')
            for(var i=0;i<h3s.length;i++) {
                  h3s[i].style.color = "green"
            }
      }

      function changeH5() {
        // the colour of all <h5> should turn to blue
            var h5s= document.querySelectorAll('h5')
            for(var i=0;i<h5s.length;i++) {
                  h5s[i].style.color = "blue"
            }
      }

      function changeGreen() {
        // all the elements with the class green should change to green
        var cGreen= document.querySelectorAll('.green')
            for(var i=0;i<cGreen.length;i++) {
                  cGreen[i].style.color = "green"
            }
      }

      function changeRed() {
        // all the elements with the class red should change to red
        var cRed= document.querySelectorAll('.red')
            for(var i=0;i<cRed.length;i++) {
                  cRed[i].style.color = "red"
            }
      }

      function changeBlue() {
        // all the elements with the class blue should change to blue
        var cBlue= document.querySelectorAll('.blue')
            for(var i=0;i<cBlue.length;i++) {
                  cBlue[i].style.color = "blue"
            }
      }
```

`25237 - DOM-I CONTENT MANIPULATION`

**Solution:**

```jsx
function setFirstName() {
        // Change the content of h1 to your first name
        document.getElementById("firstname").innerText = "Chaila";

        //querySelector
      //   document.querySelector("#firstname").innerText = "Chaila";

      }

      function setLastName() {
        // Change the content of div to your last name
        document.getElementById("lastname").innerText = "Chaila1628";

      }

      function setFullName() {
        // Change the content of p to your full name (firstname - lastname)
        document.getElementById("fullname").innerText = "Chaila - 1628";

      }

      function resetDefaults() {
        // reset the firstname, lastname, and fullname to empty values
        document.querySelector("h1").innerText=""
        document.querySelector("div").innerText=""
        document.querySelector("p").innerText=""

      }
```

## **addEventListener()**

- Untill now, we are using onClick event listener, but we are using it inline to HTML element.
    
    ```jsx
    <button onClick="likeMe()">Like👍</button>
    ```
    
- But this method of adding event is not recommended. Why?
    
     Because we are writing JS inside HTML tags. 
    
    Why did we write our CSS in style tag inside head tag? Because the code is not clean and it is not recommended to write the styles inside our tags using style attribute, right? 
    
    Similarly, we can have the same behaviour of writing a function on click of the button without writing onClick as an attribute for the button tag.
    
- The method we have is called as **`addEventListener()`**
- The `addEventListener()` method attaches an event handler to a document, same functionality as onClick,it’s  just a syntax change.

# Syntax

```jsx
document.addEventListener(*event*, *function*)
```

### Parameters

- So, let’s try to rewrite DOM-1 example using `addEventListener`

```jsx
<html>
<head>
      <title>OnClick</title>
</head>
<body>
      <button>Like👍</button>
</body>
</html>
```

- To add `addEventListener` we need to catch the element to which we want to add and then add an event to that element

```jsx
<script>
			document.querySelector("button").addEventListener("click",likeMe)

      function likeMe() {
            console.log("Someone liked me")
      }
</script>
```

- Here is a list of some common HTML events:
- For more events - [Click here](https://www.w3schools.com/jsref/dom_obj_event.asp)

# CP Intro

CP slides - [https://docs.google.com/presentation/d/1GpFjAVOPlszZiJb3LZ1Rlm9yvuvTGtJlDw2O7nb4KK8/edit?usp=sharing](https://docs.google.com/presentation/d/1GpFjAVOPlszZiJb3LZ1Rlm9yvuvTGtJlDw2O7nb4KK8/edit?usp=sharing)

Open CP link - [https://cp.masaischool.com/problems](https://cp.masaischool.com/problems)

Go to this link - [https://cp.masaischool.com/assignments/736/view](https://cp.masaischool.com/assignments/736/view)

Solve BMI calculator -

- Download boiler plate
- and copy to masai-repo,
- code it and push
- Till now, we’ve built static web pages. That means our webpage did not interact with the user, right? Let’s see an alalogy of what a DOM is.

## **What is DOM?**

- Imagine this🤔 you are watching TV and you don't like the show that's being streamed, and you want to change it and you also want to increase its volume. To do that, there has to be a way for you to interact with your television. So how do you control your tv now?
- By using `remote`

![Screenshot 2022-05-11 at 3.51.28 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_3.51.28_PM.png)

- The remote serves as the **bridge** which allows you interact with your television.
- In the same way, JavaScript helps you to interact with the HTML page via **DOM.**
- For example, say that you want a button to change colours when it gets clicked or you want text to be changed. First, you need to reference those elements from your JavaScript.
- The DOM is a tree-like representation of the web page that gets loaded into the browser.
- Whenever html document is loaded on browser, corresponding to that document another representation of document is created which is known as DOM.
- Let’s suppose you have this code

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Text</title>
  </head>
  <body>
    <h1>My Header</h1>
    <p>My Paragraph</p>
  </body>
</html>
```

The Document Object Model (DOM) is an interface for web documents. It represents the page so that programs can change the document structure, style, and content. The DOM represents the document as nodes and objects; that way, programming languages can interact with the page.

A web page is a document that can be either displayed in the browser window or as the HTML source in our vs code, right?. In both cases, it is the same document but the DOM representation of this document allows it to be manipulated as an object-oriented representation.  Now that it is an object-orinted representation, it can be modified with a scripting language such as JavaScript.

- If you open this in browser, the web browser creates a DOM of the webpage when the page is loaded. The DOM model is created as a tree of objects like this

![javascript8_1.webp](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/javascript8_1.webp)

## HTML meets 🤝 JS

![Screenshot 2022-05-11 at 3.33.08 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_3.33.08_PM.png)

## How to add JS inside HTML

```html
<html>
<head>
  <title>Connecting JS</title>
</head>
<body>
</body>
</html>

<script>
	function doSomething(){
		 // Your Code Goes Here
	}
</script>
```

- Inside script tag you can write your js code

## Console.log():

- console.log() in javascript is your best friend life long

![Screenshot 2022-05-11 at 4.53.33 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_4.53.33_PM.png)

### Where to find your best friend ?

- As you already know, you should use console inside your js code, so I am writing console.log() in script tag

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Text</title>
  </head>
  <body>
    <h1>My Header</h1>
    <p>My Paragraph</p>
  </body>
</html>
<script>
	console.log("Oh my Friend")
</script>
```

- Now, where can I find my best friend

> Till now, if it is a .js extension, we can run it in our vs code only using `node filename` .But, this is a .html extension and we know we can open html extension in our browser, then where can we see this console from browser.
> 
- Step-1: Run HTML file on browser.
- Step-2: Right click and click on inspect.
- Step-3: You can see console beside Elements
    
    ![Screenshot 2022-05-11 at 5.03.05 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_5.03.05_PM.png)
    

- Now with help of your friend let’s see what is hiding in our window and document.
    
    

![Screenshot 2022-05-25 at 11.14.53 AM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-25_at_11.14.53_AM.png)

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Text</title>
  </head>
  <body>
    <h1>My Header</h1>
    <p>My Paragraph</p>
  </body>
</html>
<script>
	console.log(window)
</script>
```

> ***Show window object and document object from here and show the difference of how DOM is creating the objects and nodes representation of the html file.***
> 

**Output**

![Screenshot 2022-05-11 at 5.07.37 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_5.07.37_PM.png)

Similar to how we access keys in our object, we can access keys of our document also. Then what will be the output of 

```jsx
// URL of a page
console.log(document.URL)
// title of a page
console.log(document.title)
// domain
console.log(document.domain)
// doctype
console.log(document.doctype)
// head
console.log(document.head)
// body
console.log(document.body)
// all elements
console.log(document.all)
// forms
console.log(document.forms)
// links
console.log(document.links)
// images
console.log(document.images)

```

Similar to how the channel can change using the remote of our TV, or the vol decreases or increases by using the remote. In the similar manner, let’s see how we can create some buttons and make them interactive.

Example:

```jsx
<html>
<head>
      <title>OnClick</title>
</head>
<body>
      <button onClick="likeMe()">Like👍</button>
</body>
</html>
```

Now what should we do with a button, we will click on the button, right?

So, what is this on click, it is some action that the user is doing right? The actions that a user can do or the actions that will interact with the user or the browser are called events. So, onClick is an event. 

Now that we have seen what an event is, how do we describe what should happen on clicking that button? We are writing a function, right?

We know how to access functions in JS and write some logic there. So, we have to define the function in JS, i.e, script tag. 

- Now we need to define this function in javascript to make it work

```jsx
<script>
      function likeMe() {
            console.log("Someone liked me")
      }
</script>
```

## [onClick Event:](https://www.w3schools.com/jsref/event_onclick.asp)

![poke-poking.gif](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/poke-poking.gif)

- The `onclick` event occurs when the user clicks on an element.
- The `onclick`event executes a certain functionality when a button/element is clicked.

[OEAO.mp4](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/OEAO.mp4)

**Basic `onclick` syntax:**

```jsx
<element onclick="functionToExecute()">Click</element>
```

- Now when we click on “Like” button, we will get `“Someone liked me”` in console

![Screenshot 2022-05-11 at 5.44.25 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_5.44.25_PM.png)

- Let’s dry run it

![Screenshot 2022-05-11 at 5.59.43 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_5.59.43_PM.png)

## [Alert():](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert)

- The **alert()** method in JavaScript is used to display a virtual alert box.
- It is mostly used to give a warning message to the users. It displays an alert dialog box that consists of some specified message (which is optional) and an OK button.
- When the dialog box pops up, we have to click "OK" to proceed.

![Show_an_alert_dialog_in_JavaScript_Example.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Show_an_alert_dialog_in_JavaScript_Example.png)

### Syntax

```jsx
alert(message)
```

- In the above example instead of console, we will try to keep alert

```jsx
<html>
<head>
      <title>OnClick</title>
</head>
<body>
      <button onClick="likeMe()">Like👍</button>
</body>
</html>

<script>
      function likeMe() {
            alert("Someone liked me")
      }
</script>
```

**Output**

![Screenshot 2022-05-11 at 6.06.02 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_6.06.02_PM.png)

***You might have seen some websites ask for location access when you are opening it using alert boxes, right?***

## **[Document.getElementById()](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById#syntax)**

We’ve seen how we can apply styles to our html elements in style tag by giving ids, classes and selectors, combinators, right?

We can do the same without style tag and using Javascript as well. But first let us see how we can access these html elements in javascript.

**Example:**

```jsx
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
      <p id="para">I am paragraph</p> 
      <div id="box">I am box</div>
      <h1 id="head-1">I am heading 1</h1> 
  </body>
</html>

<script>
      console.log(document.getElementById("para"))
      console.log(document.getElementById("box"))
      console.log(document.getElementById("head-1"))

</script>
```

**Output**:

![Screenshot 2022-05-11 at 6.19.04 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_6.19.04_PM.png)

## Syntax

```jsx
document.getElementById(id_Name)
```

### Parameters

- `id`The ID of the element to locate. The ID is case-sensitive string which is unique within the document; only one element may have any given ID.

### Return value

- An `[Element](https://developer.mozilla.org/en-US/docs/Web/API/Element)` object describing the DOM element object matching the specified ID, or `null` if no matching element was found in the document.
- The `[Document](https://developer.mozilla.org/en-US/docs/Web/API/Document)` method **`getElementById()`** returns an `[Element](https://developer.mozilla.org/en-US/docs/Web/API/Element)` object representing the element whose `[id](https://developer.mozilla.org/en-US/docs/Web/API/Element/id)` property matches the specified string.

## innerText (or) textContent:

- Do you remember in our first class we have discussed about `HTML elements`

![a.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/a.png)

- The content inside opening and closing tag is called as `innerText` also called as `textContent`
- The `innerText` property sets or returns the text content of an element.

## Syntax

```jsx
*element*.innerText
```

**Example:**

Let’s take previous example and try to get innerText of tags

```jsx
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
      <p id="para">I am paragraph</p> 
      <div id="box">I am box</div>
      <h1 id="head-1">I am heading 1</h1> 
  </body>
</html>

<script>
      console.log(document.getElementById("para").innerText)
      console.log(document.getElementById("box").innerText)
      console.log(document.getElementById("head-1").innerText)

</script>
```

**Output**:

![Screenshot 2022-05-11 at 6.58.46 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_6.58.46_PM.png)

## innerText vs innerHTML

Example: 

`<i>` tag is italic tag

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>innerText vs innerHTML</title>
  </head>
  <body>
    <div id="box">Welcome to <i> Masai School </i></div>
  </body>
</html>

<script>
      console.log(document.getElementById("box").innerText)

      console.log(document.getElementById("box").innerHTML)

</script>
```

**Output**:

![Screenshot 2022-05-12 at 10.22.15 AM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-12_at_10.22.15_AM.png)

- From the above example you can clearly see that
    - `innerText` is retreiving only text inside tags
    - `innerHTML` is retreiving with HTML elements (<i> tag)
    

## Changing innerText of an element

- Javascript provides us with the `innerText` property that we can use to change the text inside an element.

Syntax: 

```jsx
 element.textContent = "new_value" or
 element.innerText = "new_value" 
```

Example:

```jsx
<html>
<body>
  <h1 id="head">Amitabh bachan</h1>
	<button onClick="changeHeading()">Change heading</button>
</body>
<script>
	function changeHeading(){
	  document.getElementById("head").innerText = "Rajnikanth";
	}
</script>
</html>
```

Example 2 : [Codepen](https://codepen.io/vchandu111/pen/PoQGqeV)

## Value:

We have seen how to create an input tag, right? Now, after creating the input tag, we can use it to fill forms such as this. But what is the purpose of forms?

Forms are used to collect data and store that data. So, now we will see how to collect this data from an input tag.

- While interacting with users, its important to take few inputs from users, for eg:form inputs

### Getting values from Input tags

- In HTML introduction we have seen so many input tags.
- We have also seen masai form

![input.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/input.png)

- To interact with user, we need to get the value of
    - Full name
    - Email
    - Password
- How to get those values?
    - For getting those values we have an `attribute` in input tag known as `value` which is by default empty.

```jsx
<input type="text" value=""/>
```

- Try to type in some value and check the output

```jsx
<input type="text" value="Masai School"/>
```

Output:

![Screenshot 2022-05-12 at 10.54.21 AM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-12_at_10.54.21_AM.png)

- So, whatever we type in that input box, we can capture that in `value` attribute.

Example:

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
    <input id="name" type="text" value="" />
    <button onClick="catchValue()">Submit</button>
  </body>
</html>

<script>
  function catchValue() {
    var studentName = document.getElementById("name").value;
    console.log(studentName);
  }
</script>
```

Output:

![Screenshot 2022-05-12 at 11.13.42 AM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-12_at_11.13.42_AM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/oNEzjNM)

Example 2 : [Codepen](https://codepen.io/nrupuld/pen/zVBJaa)

## Displaying data on Browser

- Untill now we just got the value and displayed in console, but in real-world apps, we need to show data to users also
- Let’s take above example of taking input value of name from the user, instead of consoling the name , let’s try to print name on browser.
- For that let’s create <h1> tag in the body and we will try to fill in innerText

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
    <input id="name" type="text" value="" />
    <button onClick="catchValue()">Submit</button>
    <!-- Show output here -->
    <h1 id="output"></h1>
  </body>
</html>

<script>
  function catchValue() {
    var studentName = document.getElementById("name").value;
    document.getElementById("output").innerText = studentName;
  }
</script>
```

Output:

![Screenshot 2022-05-12 at 11.21.27 AM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-12_at_11.21.27_AM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/WNMGQrr)

### Getting values from Select tags

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
    <select id="gender">
      <option value="">Select gender</option>
      <option value="MALE">Male</option>
      <option value="FEMALE">Female</option>
    </select>
    <button onClick="getGender()">Submit</button>
  </body>
</html>

<script>
  function getGender() {
    var gen = document.getElementById("gender").value;
    console.log(gen);
  }
</script>
```

Live code : [Codepen](https://codepen.io/vchandu111/pen/dydpYax)

# **Styling DOM Elements in JavaScript**

- You can also apply style on HTML elements to change the visual presentation of HTML documents dynamically using JavaScript.
- You can set almost all the styles for the elements like, fonts, colors, margins, borders, background images, text alignment, width and height, position, and so on.

### **Setting Inline Styles on Elements**

- Inline styles are applied directly to the specific HTML element using the style attribute. In JavaScript the `style` property is used to get or set the inline style of an element.
- The following example will set the color and font properties of an element with `id="intro"`.

```jsx
<html lang="en">
<head>
    <title>JS Set Inline Styles Demo</title>
</head>
<body>
    <p id="intro">This is a paragraph.</p>
    <p>This is another paragraph.</p>
</body>
</html>
<script>
    // Selecting element
    var elem = document.getElementById("intro");

    // Appling styles on element
    elem.style.color = "blue";
    elem.style.fontSize = "18px";
    elem.style.fontWeight = "bold";
</script>

```

**Output:**

![Screenshot 2022-05-27 at 12.37.01 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_12.37.01_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/PoQEJmd)

> ***Similar to getElementById, we have getElementsByTagName and getElementsByClassName, but there is a drawback in this. Can anyone tell me what the drawback is?***
> 

- The drawback of above methods is, we are using different syntax for different methods, right.
- So now we will see a method where we can access/catch element by its
    - tagName
    - className
    - id
- These methods are known as `querySelector` and `querySelectorAll`

# **querySelector():**

### Syntax

```jsx
document.querySelector(CSS selector)
```

> ***Selector can be anything ⇒ class, id, tag, combinators. So we can use any of these as selector in the querySelector.***
> 
- Here selectors can be any selector (id,class,tag,universal)

**Example**

```jsx
<html>
  <body>
    <p>This is a first p element.</p>
    <p>This is a second p element.</p>
    <p>This is a third p element.</p>
  </body>
</html>
<script>
  document.querySelector("p").style.backgroundColor = "red";
</script>
```

Output:

![Screenshot 2022-05-27 at 12.41.29 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_12.41.29_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/zYRpEzB)

- In the above example, `querySelector` is making background color red to only first element that matches
- Let’s take one more example

```jsx
<html>
  <body>
    <p class="example">I am first paragraph.</p>
    <p class="example">I am second paragraph.</p>
  </body>
</html>
<script>
  document.querySelector(".example").style.backgroundColor = "teal";
</script>
```

**Output**

![Screenshot 2022-05-27 at 12.44.56 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_12.44.56_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/vYdpeZd)

- In the above example, `querySelector` is making background color teal to only first element that matches query class example
- We can also use combinators here, but even with combinators it will only return first element

Example:

```jsx
<html>
  <body>
    <h2>Masai School Students</h2>
    <p>Manish</p>
    <p>Vikash</p>
    <p>Charan</p>
    <p>Mounika</p>
  </body>
</html>
<script>
  document.querySelector("h2~p").style.backgroundColor = "teal";
</script>
```

- Basically `h2~p` should return all p’s, but `querySelector` will return only first p, in this case Manish

**Output**:

![Screenshot 2022-05-27 at 12.53.04 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_12.53.04_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/QWQaqqX)

- The `querySelector()` method returns the **`first`** element that matches a CSS selector.

- To return **all** matches (not only the first), use the `querySelectorAll()` instead.

# **querySelectorAll():**

- The `querySelectorAll()` method returns all elements that matches a CSS selector(s).
- The `querySelectorAll()` method returns a NodeList.

### Syntax

```jsx
document.querySelectorAll(CSS selectors)
```

- Here selectors can be any selector (id,class,tag,universal)
- Let’s take the same examples as querySelector

```jsx
<html>
  <body>
    <p>This is a first p element.</p>
    <p>This is a second p element.</p>
    <p>This is a third p element.</p>
  </body>
</html>
<script>
  // This won't work because querySelectorAll() method returns a NodeList.
  // document.querySelectorAll("p").style.backgroundColor = "red";
  // So we need to use for loop to select all elements

  var list = document.querySelectorAll("p");
  for (var i = 0; i < list.length; i++) {
    list[i].style.backgroundColor = "red";
  }
</script>
```

**Output**

![Screenshot 2022-05-27 at 1.18.45 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_1.18.45_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/JjpMrzO)

**Example 2**

```jsx
<html>
  <body>
    <p class="example">I am first paragraph.</p>
    <p class="example">I am second paragraph.</p>
  </body>
</html>
<script>
  var list = document.querySelectorAll(".example");
  for (var i = 0; i < list.length; i++) {
    list[i].style.backgroundColor = "teal";
  }
</script>
```

Output:

![Screenshot 2022-05-27 at 1.21.13 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_1.21.13_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/NWyXaVW)

**Example 3:**

```jsx
<html>
  <body>
    <h2>Masai School Students</h2>
    <p>Manish</p>
    <p>Vikash</p>
    <p>Charan</p>
    <p>Mounika</p>
  </body>
</html>
<script>
    var list = document.querySelectorAll("h2~p");
    for (var i = 0; i < list.length; i++) {
    list[i].style.backgroundColor = "teal";
  }

</script>
```

Output:

![Screenshot 2022-05-27 at 1.24.05 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_1.24.05_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/JjpMrQM)

## Questions to solve

`25245 - DOM SELECTORS`

**Solution**:

```jsx
function changeH1() {
        // the colour of first <h1> should turn to red
        document.querySelector("h1").style.color = "red";
      }

      function changeH3() {
        // the colour of all <h3> should turn to green
            var h3s= document.querySelectorAll('h3')
            for(var i=0;i<h3s.length;i++) {
                  h3s[i].style.color = "green"
            }
      }

      function changeH5() {
        // the colour of all <h5> should turn to blue
            var h5s= document.querySelectorAll('h5')
            for(var i=0;i<h5s.length;i++) {
                  h5s[i].style.color = "blue"
            }
      }

      function changeGreen() {
        // all the elements with the class green should change to green
        var cGreen= document.querySelectorAll('.green')
            for(var i=0;i<cGreen.length;i++) {
                  cGreen[i].style.color = "green"
            }
      }

      function changeRed() {
        // all the elements with the class red should change to red
        var cRed= document.querySelectorAll('.red')
            for(var i=0;i<cRed.length;i++) {
                  cRed[i].style.color = "red"
            }
      }

      function changeBlue() {
        // all the elements with the class blue should change to blue
        var cBlue= document.querySelectorAll('.blue')
            for(var i=0;i<cBlue.length;i++) {
                  cBlue[i].style.color = "blue"
            }
      }
```

`25237 - DOM-I CONTENT MANIPULATION`

**Solution:**

```jsx
function setFirstName() {
        // Change the content of h1 to your first name
        document.getElementById("firstname").innerText = "Chaila";

        //querySelector
      //   document.querySelector("#firstname").innerText = "Chaila";

      }

      function setLastName() {
        // Change the content of div to your last name
        document.getElementById("lastname").innerText = "Chaila1628";

      }

      function setFullName() {
        // Change the content of p to your full name (firstname - lastname)
        document.getElementById("fullname").innerText = "Chaila - 1628";

      }

      function resetDefaults() {
        // reset the firstname, lastname, and fullname to empty values
        document.querySelector("h1").innerText=""
        document.querySelector("div").innerText=""
        document.querySelector("p").innerText=""

      }
```

## **addEventListener()**

- Untill now, we are using onClick event listener, but we are using it inline to HTML element.
    
    ```jsx
    <button onClick="likeMe()">Like👍</button>
    ```
    
- But this method of adding event is not recommended. Why?
    
     Because we are writing JS inside HTML tags. 
    
    Why did we write our CSS in style tag inside head tag? Because the code is not clean and it is not recommended to write the styles inside our tags using style attribute, right? 
    
    Similarly, we can have the same behaviour of writing a function on click of the button without writing onClick as an attribute for the button tag.
    
- The method we have is called as **`addEventListener()`**
- The `addEventListener()` method attaches an event handler to a document, same functionality as onClick,it’s  just a syntax change.

# Syntax

```jsx
document.addEventListener(*event*, *function*)
```

### Parameters

- So, let’s try to rewrite DOM-1 example using `addEventListener`

```jsx
<html>
<head>
      <title>OnClick</title>
</head>
<body>
      <button>Like👍</button>
</body>
</html>
```

- To add `addEventListener` we need to catch the element to which we want to add and then add an event to that element

```jsx
<script>
			document.querySelector("button").addEventListener("click",likeMe)

      function likeMe() {
            console.log("Someone liked me")
      }
</script>
```

- Here is a list of some common HTML events:
- For more events - [Click here](https://www.w3schools.com/jsref/dom_obj_event.asp)

# CP Intro

CP slides - [https://docs.google.com/presentation/d/1GpFjAVOPlszZiJb3LZ1Rlm9yvuvTGtJlDw2O7nb4KK8/edit?usp=sharing](https://docs.google.com/presentation/d/1GpFjAVOPlszZiJb3LZ1Rlm9yvuvTGtJlDw2O7nb4KK8/edit?usp=sharing)

Open CP link - [https://cp.masaischool.com/problems](https://cp.masaischool.com/problems)

Go to this link - [https://cp.masaischool.com/assignments/736/view](https://cp.masaischool.com/assignments/736/view)

Solve BMI calculator -

- Download boiler plate
- and copy to masai-repo,
- code it and push
- repo link - Till now, we’ve built static web pages. That means our webpage did not interact with the user, right? Let’s see an alalogy of what a DOM is.

## **What is DOM?**

- Imagine this🤔 you are watching TV and you don't like the show that's being streamed, and you want to change it and you also want to increase its volume. To do that, there has to be a way for you to interact with your television. So how do you control your tv now?
- By using `remote`

![Screenshot 2022-05-11 at 3.51.28 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_3.51.28_PM.png)

- The remote serves as the **bridge** which allows you interact with your television.
- In the same way, JavaScript helps you to interact with the HTML page via **DOM.**
- For example, say that you want a button to change colours when it gets clicked or you want text to be changed. First, you need to reference those elements from your JavaScript.
- The DOM is a tree-like representation of the web page that gets loaded into the browser.
- Whenever html document is loaded on browser, corresponding to that document another representation of document is created which is known as DOM.
- Let’s suppose you have this code

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Text</title>
  </head>
  <body>
    <h1>My Header</h1>
    <p>My Paragraph</p>
  </body>
</html>
```

The Document Object Model (DOM) is an interface for web documents. It represents the page so that programs can change the document structure, style, and content. The DOM represents the document as nodes and objects; that way, programming languages can interact with the page.

A web page is a document that can be either displayed in the browser window or as the HTML source in our vs code, right?. In both cases, it is the same document but the DOM representation of this document allows it to be manipulated as an object-oriented representation.  Now that it is an object-orinted representation, it can be modified with a scripting language such as JavaScript.

- If you open this in browser, the web browser creates a DOM of the webpage when the page is loaded. The DOM model is created as a tree of objects like this

![javascript8_1.webp](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/javascript8_1.webp)

## HTML meets 🤝 JS

![Screenshot 2022-05-11 at 3.33.08 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_3.33.08_PM.png)

## How to add JS inside HTML

```html
<html>
<head>
  <title>Connecting JS</title>
</head>
<body>
</body>
</html>

<script>
	function doSomething(){
		 // Your Code Goes Here
	}
</script>
```

- Inside script tag you can write your js code

## Console.log():

- console.log() in javascript is your best friend life long

![Screenshot 2022-05-11 at 4.53.33 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_4.53.33_PM.png)

### Where to find your best friend ?

- As you already know, you should use console inside your js code, so I am writing console.log() in script tag

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Text</title>
  </head>
  <body>
    <h1>My Header</h1>
    <p>My Paragraph</p>
  </body>
</html>
<script>
	console.log("Oh my Friend")
</script>
```

- Now, where can I find my best friend

> Till now, if it is a .js extension, we can run it in our vs code only using `node filename` .But, this is a .html extension and we know we can open html extension in our browser, then where can we see this console from browser.
> 
- Step-1: Run HTML file on browser.
- Step-2: Right click and click on inspect.
- Step-3: You can see console beside Elements
    
    ![Screenshot 2022-05-11 at 5.03.05 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_5.03.05_PM.png)
    

- Now with help of your friend let’s see what is hiding in our window and document.
    
    

![Screenshot 2022-05-25 at 11.14.53 AM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-25_at_11.14.53_AM.png)

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Text</title>
  </head>
  <body>
    <h1>My Header</h1>
    <p>My Paragraph</p>
  </body>
</html>
<script>
	console.log(window)
</script>
```

> ***Show window object and document object from here and show the difference of how DOM is creating the objects and nodes representation of the html file.***
> 

**Output**

![Screenshot 2022-05-11 at 5.07.37 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_5.07.37_PM.png)

Similar to how we access keys in our object, we can access keys of our document also. Then what will be the output of 

```jsx
// URL of a page
console.log(document.URL)
// title of a page
console.log(document.title)
// domain
console.log(document.domain)
// doctype
console.log(document.doctype)
// head
console.log(document.head)
// body
console.log(document.body)
// all elements
console.log(document.all)
// forms
console.log(document.forms)
// links
console.log(document.links)
// images
console.log(document.images)

```

Similar to how the channel can change using the remote of our TV, or the vol decreases or increases by using the remote. In the similar manner, let’s see how we can create some buttons and make them interactive.

Example:

```jsx
<html>
<head>
      <title>OnClick</title>
</head>
<body>
      <button onClick="likeMe()">Like👍</button>
</body>
</html>
```

Now what should we do with a button, we will click on the button, right?

So, what is this on click, it is some action that the user is doing right? The actions that a user can do or the actions that will interact with the user or the browser are called events. So, onClick is an event. 

Now that we have seen what an event is, how do we describe what should happen on clicking that button? We are writing a function, right?

We know how to access functions in JS and write some logic there. So, we have to define the function in JS, i.e, script tag. 

- Now we need to define this function in javascript to make it work

```jsx
<script>
      function likeMe() {
            console.log("Someone liked me")
      }
</script>
```

## [onClick Event:](https://www.w3schools.com/jsref/event_onclick.asp)

![poke-poking.gif](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/poke-poking.gif)

- The `onclick` event occurs when the user clicks on an element.
- The `onclick`event executes a certain functionality when a button/element is clicked.

[OEAO.mp4](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/OEAO.mp4)

**Basic `onclick` syntax:**

```jsx
<element onclick="functionToExecute()">Click</element>
```

- Now when we click on “Like” button, we will get `“Someone liked me”` in console

![Screenshot 2022-05-11 at 5.44.25 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_5.44.25_PM.png)

- Let’s dry run it

![Screenshot 2022-05-11 at 5.59.43 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_5.59.43_PM.png)

## [Alert():](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert)

- The **alert()** method in JavaScript is used to display a virtual alert box.
- It is mostly used to give a warning message to the users. It displays an alert dialog box that consists of some specified message (which is optional) and an OK button.
- When the dialog box pops up, we have to click "OK" to proceed.

![Show_an_alert_dialog_in_JavaScript_Example.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Show_an_alert_dialog_in_JavaScript_Example.png)

### Syntax

```jsx
alert(message)
```

- In the above example instead of console, we will try to keep alert

```jsx
<html>
<head>
      <title>OnClick</title>
</head>
<body>
      <button onClick="likeMe()">Like👍</button>
</body>
</html>

<script>
      function likeMe() {
            alert("Someone liked me")
      }
</script>
```

**Output**

![Screenshot 2022-05-11 at 6.06.02 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_6.06.02_PM.png)

***You might have seen some websites ask for location access when you are opening it using alert boxes, right?***

## **[Document.getElementById()](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById#syntax)**

We’ve seen how we can apply styles to our html elements in style tag by giving ids, classes and selectors, combinators, right?

We can do the same without style tag and using Javascript as well. But first let us see how we can access these html elements in javascript.

**Example:**

```jsx
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
      <p id="para">I am paragraph</p> 
      <div id="box">I am box</div>
      <h1 id="head-1">I am heading 1</h1> 
  </body>
</html>

<script>
      console.log(document.getElementById("para"))
      console.log(document.getElementById("box"))
      console.log(document.getElementById("head-1"))

</script>
```

**Output**:

![Screenshot 2022-05-11 at 6.19.04 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_6.19.04_PM.png)

## Syntax

```jsx
document.getElementById(id_Name)
```

### Parameters

- `id`The ID of the element to locate. The ID is case-sensitive string which is unique within the document; only one element may have any given ID.

### Return value

- An `[Element](https://developer.mozilla.org/en-US/docs/Web/API/Element)` object describing the DOM element object matching the specified ID, or `null` if no matching element was found in the document.
- The `[Document](https://developer.mozilla.org/en-US/docs/Web/API/Document)` method **`getElementById()`** returns an `[Element](https://developer.mozilla.org/en-US/docs/Web/API/Element)` object representing the element whose `[id](https://developer.mozilla.org/en-US/docs/Web/API/Element/id)` property matches the specified string.

## innerText (or) textContent:

- Do you remember in our first class we have discussed about `HTML elements`

![a.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/a.png)

- The content inside opening and closing tag is called as `innerText` also called as `textContent`
- The `innerText` property sets or returns the text content of an element.

## Syntax

```jsx
*element*.innerText
```

**Example:**

Let’s take previous example and try to get innerText of tags

```jsx
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
      <p id="para">I am paragraph</p> 
      <div id="box">I am box</div>
      <h1 id="head-1">I am heading 1</h1> 
  </body>
</html>

<script>
      console.log(document.getElementById("para").innerText)
      console.log(document.getElementById("box").innerText)
      console.log(document.getElementById("head-1").innerText)

</script>
```

**Output**:

![Screenshot 2022-05-11 at 6.58.46 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-11_at_6.58.46_PM.png)

## innerText vs innerHTML

Example: 

`<i>` tag is italic tag

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>innerText vs innerHTML</title>
  </head>
  <body>
    <div id="box">Welcome to <i> Masai School </i></div>
  </body>
</html>

<script>
      console.log(document.getElementById("box").innerText)

      console.log(document.getElementById("box").innerHTML)

</script>
```

**Output**:

![Screenshot 2022-05-12 at 10.22.15 AM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-12_at_10.22.15_AM.png)

- From the above example you can clearly see that
    - `innerText` is retreiving only text inside tags
    - `innerHTML` is retreiving with HTML elements (<i> tag)
    

## Changing innerText of an element

- Javascript provides us with the `innerText` property that we can use to change the text inside an element.

Syntax: 

```jsx
 element.textContent = "new_value" or
 element.innerText = "new_value" 
```

Example:

```jsx
<html>
<body>
  <h1 id="head">Amitabh bachan</h1>
	<button onClick="changeHeading()">Change heading</button>
</body>
<script>
	function changeHeading(){
	  document.getElementById("head").innerText = "Rajnikanth";
	}
</script>
</html>
```

Example 2 : [Codepen](https://codepen.io/vchandu111/pen/PoQGqeV)

## Value:

We have seen how to create an input tag, right? Now, after creating the input tag, we can use it to fill forms such as this. But what is the purpose of forms?

Forms are used to collect data and store that data. So, now we will see how to collect this data from an input tag.

- While interacting with users, its important to take few inputs from users, for eg:form inputs

### Getting values from Input tags

- In HTML introduction we have seen so many input tags.
- We have also seen masai form

![input.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/input.png)

- To interact with user, we need to get the value of
    - Full name
    - Email
    - Password
- How to get those values?
    - For getting those values we have an `attribute` in input tag known as `value` which is by default empty.

```jsx
<input type="text" value=""/>
```

- Try to type in some value and check the output

```jsx
<input type="text" value="Masai School"/>
```

Output:

![Screenshot 2022-05-12 at 10.54.21 AM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-12_at_10.54.21_AM.png)

- So, whatever we type in that input box, we can capture that in `value` attribute.

Example:

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
    <input id="name" type="text" value="" />
    <button onClick="catchValue()">Submit</button>
  </body>
</html>

<script>
  function catchValue() {
    var studentName = document.getElementById("name").value;
    console.log(studentName);
  }
</script>
```

Output:

![Screenshot 2022-05-12 at 11.13.42 AM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-12_at_11.13.42_AM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/oNEzjNM)

Example 2 : [Codepen](https://codepen.io/nrupuld/pen/zVBJaa)

## Displaying data on Browser

- Untill now we just got the value and displayed in console, but in real-world apps, we need to show data to users also
- Let’s take above example of taking input value of name from the user, instead of consoling the name , let’s try to print name on browser.
- For that let’s create <h1> tag in the body and we will try to fill in innerText

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
    <input id="name" type="text" value="" />
    <button onClick="catchValue()">Submit</button>
    <!-- Show output here -->
    <h1 id="output"></h1>
  </body>
</html>

<script>
  function catchValue() {
    var studentName = document.getElementById("name").value;
    document.getElementById("output").innerText = studentName;
  }
</script>
```

Output:

![Screenshot 2022-05-12 at 11.21.27 AM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-12_at_11.21.27_AM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/WNMGQrr)

### Getting values from Select tags

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
    <select id="gender">
      <option value="">Select gender</option>
      <option value="MALE">Male</option>
      <option value="FEMALE">Female</option>
    </select>
    <button onClick="getGender()">Submit</button>
  </body>
</html>

<script>
  function getGender() {
    var gen = document.getElementById("gender").value;
    console.log(gen);
  }
</script>
```

Live code : [Codepen](https://codepen.io/vchandu111/pen/dydpYax)

# **Styling DOM Elements in JavaScript**

- You can also apply style on HTML elements to change the visual presentation of HTML documents dynamically using JavaScript.
- You can set almost all the styles for the elements like, fonts, colors, margins, borders, background images, text alignment, width and height, position, and so on.

### **Setting Inline Styles on Elements**

- Inline styles are applied directly to the specific HTML element using the style attribute. In JavaScript the `style` property is used to get or set the inline style of an element.
- The following example will set the color and font properties of an element with `id="intro"`.

```jsx
<html lang="en">
<head>
    <title>JS Set Inline Styles Demo</title>
</head>
<body>
    <p id="intro">This is a paragraph.</p>
    <p>This is another paragraph.</p>
</body>
</html>
<script>
    // Selecting element
    var elem = document.getElementById("intro");

    // Appling styles on element
    elem.style.color = "blue";
    elem.style.fontSize = "18px";
    elem.style.fontWeight = "bold";
</script>

```

**Output:**

![Screenshot 2022-05-27 at 12.37.01 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_12.37.01_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/PoQEJmd)

> ***Similar to getElementById, we have getElementsByTagName and getElementsByClassName, but there is a drawback in this. Can anyone tell me what the drawback is?***
> 

- The drawback of above methods is, we are using different syntax for different methods, right.
- So now we will see a method where we can access/catch element by its
    - tagName
    - className
    - id
- These methods are known as `querySelector` and `querySelectorAll`

# **querySelector():**

### Syntax

```jsx
document.querySelector(CSS selector)
```

> ***Selector can be anything ⇒ class, id, tag, combinators. So we can use any of these as selector in the querySelector.***
> 
- Here selectors can be any selector (id,class,tag,universal)

**Example**

```jsx
<html>
  <body>
    <p>This is a first p element.</p>
    <p>This is a second p element.</p>
    <p>This is a third p element.</p>
  </body>
</html>
<script>
  document.querySelector("p").style.backgroundColor = "red";
</script>
```

Output:

![Screenshot 2022-05-27 at 12.41.29 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_12.41.29_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/zYRpEzB)

- In the above example, `querySelector` is making background color red to only first element that matches
- Let’s take one more example

```jsx
<html>
  <body>
    <p class="example">I am first paragraph.</p>
    <p class="example">I am second paragraph.</p>
  </body>
</html>
<script>
  document.querySelector(".example").style.backgroundColor = "teal";
</script>
```

**Output**

![Screenshot 2022-05-27 at 12.44.56 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_12.44.56_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/vYdpeZd)

- In the above example, `querySelector` is making background color teal to only first element that matches query class example
- We can also use combinators here, but even with combinators it will only return first element

Example:

```jsx
<html>
  <body>
    <h2>Masai School Students</h2>
    <p>Manish</p>
    <p>Vikash</p>
    <p>Charan</p>
    <p>Mounika</p>
  </body>
</html>
<script>
  document.querySelector("h2~p").style.backgroundColor = "teal";
</script>
```

- Basically `h2~p` should return all p’s, but `querySelector` will return only first p, in this case Manish

**Output**:

![Screenshot 2022-05-27 at 12.53.04 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_12.53.04_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/QWQaqqX)

- The `querySelector()` method returns the **`first`** element that matches a CSS selector.

- To return **all** matches (not only the first), use the `querySelectorAll()` instead.

# **querySelectorAll():**

- The `querySelectorAll()` method returns all elements that matches a CSS selector(s).
- The `querySelectorAll()` method returns a NodeList.

### Syntax

```jsx
document.querySelectorAll(CSS selectors)
```

- Here selectors can be any selector (id,class,tag,universal)
- Let’s take the same examples as querySelector

```jsx
<html>
  <body>
    <p>This is a first p element.</p>
    <p>This is a second p element.</p>
    <p>This is a third p element.</p>
  </body>
</html>
<script>
  // This won't work because querySelectorAll() method returns a NodeList.
  // document.querySelectorAll("p").style.backgroundColor = "red";
  // So we need to use for loop to select all elements

  var list = document.querySelectorAll("p");
  for (var i = 0; i < list.length; i++) {
    list[i].style.backgroundColor = "red";
  }
</script>
```

**Output**

![Screenshot 2022-05-27 at 1.18.45 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_1.18.45_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/JjpMrzO)

**Example 2**

```jsx
<html>
  <body>
    <p class="example">I am first paragraph.</p>
    <p class="example">I am second paragraph.</p>
  </body>
</html>
<script>
  var list = document.querySelectorAll(".example");
  for (var i = 0; i < list.length; i++) {
    list[i].style.backgroundColor = "teal";
  }
</script>
```

Output:

![Screenshot 2022-05-27 at 1.21.13 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_1.21.13_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/NWyXaVW)

**Example 3:**

```jsx
<html>
  <body>
    <h2>Masai School Students</h2>
    <p>Manish</p>
    <p>Vikash</p>
    <p>Charan</p>
    <p>Mounika</p>
  </body>
</html>
<script>
    var list = document.querySelectorAll("h2~p");
    for (var i = 0; i < list.length; i++) {
    list[i].style.backgroundColor = "teal";
  }

</script>
```

Output:

![Screenshot 2022-05-27 at 1.24.05 PM.png](DOM-1%20(1)%20fd7d04b4c9f845ffa71650bfe053a7a3/Screenshot_2022-05-27_at_1.24.05_PM.png)

Live code : [Codepen](https://codepen.io/vchandu111/pen/JjpMrQM)

## Questions to solve

`25245 - DOM SELECTORS`

**Solution**:

```jsx
function changeH1() {
        // the colour of first <h1> should turn to red
        document.querySelector("h1").style.color = "red";
      }

      function changeH3() {
        // the colour of all <h3> should turn to green
            var h3s= document.querySelectorAll('h3')
            for(var i=0;i<h3s.length;i++) {
                  h3s[i].style.color = "green"
            }
      }

      function changeH5() {
        // the colour of all <h5> should turn to blue
            var h5s= document.querySelectorAll('h5')
            for(var i=0;i<h5s.length;i++) {
                  h5s[i].style.color = "blue"
            }
      }

      function changeGreen() {
        // all the elements with the class green should change to green
        var cGreen= document.querySelectorAll('.green')
            for(var i=0;i<cGreen.length;i++) {
                  cGreen[i].style.color = "green"
            }
      }

      function changeRed() {
        // all the elements with the class red should change to red
        var cRed= document.querySelectorAll('.red')
            for(var i=0;i<cRed.length;i++) {
                  cRed[i].style.color = "red"
            }
      }

      function changeBlue() {
        // all the elements with the class blue should change to blue
        var cBlue= document.querySelectorAll('.blue')
            for(var i=0;i<cBlue.length;i++) {
                  cBlue[i].style.color = "blue"
            }
      }
```

`25237 - DOM-I CONTENT MANIPULATION`

**Solution:**

```jsx
function setFirstName() {
        // Change the content of h1 to your first name
        document.getElementById("firstname").innerText = "Chaila";

        //querySelector
      //   document.querySelector("#firstname").innerText = "Chaila";

      }

      function setLastName() {
        // Change the content of div to your last name
        document.getElementById("lastname").innerText = "Chaila1628";

      }

      function setFullName() {
        // Change the content of p to your full name (firstname - lastname)
        document.getElementById("fullname").innerText = "Chaila - 1628";

      }

      function resetDefaults() {
        // reset the firstname, lastname, and fullname to empty values
        document.querySelector("h1").innerText=""
        document.querySelector("div").innerText=""
        document.querySelector("p").innerText=""

      }
```

## **addEventListener()**

- Untill now, we are using onClick event listener, but we are using it inline to HTML element.
    
    ```jsx
    <button onClick="likeMe()">Like👍</button>
    ```
    
- But this method of adding event is not recommended. Why?
    
     Because we are writing JS inside HTML tags. 
    
    Why did we write our CSS in style tag inside head tag? Because the code is not clean and it is not recommended to write the styles inside our tags using style attribute, right? 
    
    Similarly, we can have the same behaviour of writing a function on click of the button without writing onClick as an attribute for the button tag.
    
- The method we have is called as **`addEventListener()`**
- The `addEventListener()` method attaches an event handler to a document, same functionality as onClick,it’s  just a syntax change.

# Syntax

```jsx
document.addEventListener(*event*, *function*)
```

### Parameters

- So, let’s try to rewrite DOM-1 example using `addEventListener`

```jsx
<html>
<head>
      <title>OnClick</title>
</head>
<body>
      <button>Like👍</button>
</body>
</html>
```

- To add `addEventListener` we need to catch the element to which we want to add and then add an event to that element

```jsx
<script>
			document.querySelector("button").addEventListener("click",likeMe)

      function likeMe() {
            console.log("Someone liked me")
      }
</script>
```

- Here is a list of some common HTML events:
- For more events - [Click here](https://www.w3schools.com/jsref/dom_obj_event.asp)

# CP Intro

CP slides - [https://docs.google.com/presentation/d/1GpFjAVOPlszZiJb3LZ1Rlm9yvuvTGtJlDw2O7nb4KK8/edit?usp=sharing](https://docs.google.com/presentation/d/1GpFjAVOPlszZiJb3LZ1Rlm9yvuvTGtJlDw2O7nb4KK8/edit?usp=sharing)

Open CP link - [https://cp.masaischool.com/problems](https://cp.masaischool.com/problems)

Go to this link - [https://cp.masaischool.com/assignments/736/view](https://cp.masaischool.com/assignments/736/view)

Solve BMI calculator -

- Download boiler plate
- and copy to masai-repo,
- code it and push
- repo link -

[https://github.com/masai-course/cp-test-pt](https://github.com/masai-course/cp-test-pt)

```jsx
<!DOCTYPE html>
<html>
  <head>
    <title>Calculator</title>
  </head>
  <body>
    <h1>BMI Calculator</h1>
    <input placeholder="Height" type="number" id="height" />
    <input placeholder="Weight" type="number" id="weight" />
    <button id="calculate">Calculate</button>
    <h1>
      Your BMI is:- <span id="bmi"></span>, that means you are
      <span id="status"></span>
    </h1>
  </body>
  <script>
    document.getElementById("calculate").addEventListener("click", BMIcal);
    function BMIcal() {
      let height = document.getElementById("height").value;
      let weight = document.getElementById("weight").value;
      let bmivalue = (weight / (height * height)).toFixed(1);
      document.getElementById("bmi").textContent = bmivalue;
      if (bmivalue < 18.5) {
        document.getElementById("status").textContent = "UnderWeight";
      } else if (bmivalue >= 18.5 && bmivalue <= 24.9) {
        document.getElementById("status").textContent = "Normal Weight";
      } else if (bmivalue >= 25 && bmivalue <= 29.9) {
        document.getElementById("status").textContent = "Overweight";
      } else if (bmivalue >= 30) {
        document.getElementById("status").textContent = "Obese";
      }
    }
  </script>
</html>
```