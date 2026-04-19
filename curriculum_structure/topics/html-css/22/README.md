# Pseudo Elements, Pseudo Classes, and Specificity (Basic) (20-25mins)

### **Pseudo-Elements:**

Pseudo-elements are used to style a specific part of an element. They are denoted by a double colon (::) and are used to style things like the first line or the first letter of an element.

![Untitled](Pseudo%20Elements,%20Pseudo%20Classes,%20and%20Specificity%20(%20404e1a00428145a78b71f733afc8df48/Untitled.png)

![Untitled](Pseudo%20Elements,%20Pseudo%20Classes,%20and%20Specificity%20(%20404e1a00428145a78b71f733afc8df48/Untitled%201.png)

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Pseudo-Elements</title>
    <style>
      p::before {
        content: "Before ";
      }
      p::after {
        content: " After";
      }
      p::first-line {
        color: blue;
      }
    </style>
  </head>
  <body>
    <p>Rahul</p>

    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
      veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
      commodo consequat.
    </p>
    
  </body>
</html>
```

![Untitled](Pseudo%20Elements,%20Pseudo%20Classes,%20and%20Specificity%20(%20404e1a00428145a78b71f733afc8df48/Untitled%202.png)

### **Pseudo-Classes:**

Pseudo-classes are used to select and style an element based on its state or position. They are denoted by a single colon (:).

![Untitled](Pseudo%20Elements,%20Pseudo%20Classes,%20and%20Specificity%20(%20404e1a00428145a78b71f733afc8df48/Untitled%203.png)

![Untitled](Pseudo%20Elements,%20Pseudo%20Classes,%20and%20Specificity%20(%20404e1a00428145a78b71f733afc8df48/Untitled%204.png)

## **CSS Pseudo-classes**

A pseudo-class is used to define a special state of an element.

For example, it can be used to:

- Style an element when a user mouses over it
- Style visited and unvisited links differently
- Style an element when it gets focus

# Syntax

The syntax of pseudo-classes:

```html
selector:pseudo-class { 
	 property: value;
}
```

- Although there are various CSS pseudo-classes, here we are going to discuss some of the most commonly used pseudo-classes. The widely used CSS classes are tabulated as follows:

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      button {
        background-color: crimson;
        color: white;
        padding: 10px 20px 10px 20px;
        border: 0;
        border-radius: 10px;
      }
      /* Psuedo classes */
      button:hover {
        background-color: cornflowerblue;
        color: coral;
      }
      input:focus {
        background-color: darksalmon;
      }
      /* then, keep odd and even in place 5, then finally  */
      div > p:nth-child(5) {
        color:firebrick;
      }
    </style>
  </head>
  <body>
    <input type="text" placeholder="Enter name" /> ===> 2nd tag
    <button>Sign Up</button> ===> 1st this tag
    <div> ====> finally
      <!-- 10 p tags -->
      <p>p1</p>
      <p>p2</p>
      <p>p3</p>
      <p>p4</p>
      <p>p5</p>
      <p>p6</p>
      <p>p7</p>
      <p>p8</p>
      <p>p9</p>
      <p>p10</p>
    </div>
  </body>
</html>
```

# All CSS Pseudo Classes

> ***Open masai school website and show them the navbar by hovering the mouse, we see the changes, right? These are achieved by pseudo classes.***
> 

## **CSS Pseudo-elements**

A CSS pseudo-element is used to style specified parts of an element.

For example, it can be used to:

- Style the first letter, or line, of an element
- Insert content before, or after, the content of an element

## Syntax

The syntax of pseudo-elements:

```html
selector::pseudo-element {
  property: value;
}
```

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>

    <style>
      p::first-line {
        color: red;
        font-size: 40px;
      }

      p::before{
            content:"masai"
      }
    </style>
  </head>
  <body>
    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis
      impedit consequatur enim rerum exercitationem natus iusto, repellendus
      porro minus illo. Laborum, ducimus. Cum enim nisi assumenda voluptates
      recusandae. Ipsa, fugit. Vel repellendus quidem debitis repellat fugiat
      corporis blanditiis omnis perferendis harum, consequatur nemo commodi
      deserunt placeat iure delectus distinctio voluptatum? Aspernatur
      perspiciatis consequuntur alias magnam nihil dolores dolore hic illo.
      Illum itaque odit ipsam vitae officia saepe? Eveniet nobis quisquam porro
      officiis dolorum labore dolorem necessitatibus tempore incidunt
      repellendus ullam odio quis, molestias distinctio aliquid repudiandae
      officia voluptate recusandae accusamus!
    </p>
  </body>
</html>
```

# All CSS Pseudo Elements

Read more: [Link](https://www.w3schools.com/css/css_pseudo_elements.asp)

# Specificity

- In Selectors lecture we have seen scores of various selectors

![Screenshot 2022-05-05 at 12.49.11 PM.png](CSS%20Selectors%20(Basic)%20(30mins)%207202204b211e4c6392469dbc5ee98af3/Screenshot_2022-05-05_at_12.49.11_PM.png)

- We have also learned few more selectors like
    - Attribute Selector
    - Pseudo Class
        - :hover
        - :nth-child
        - :focus
    - Pseudo Element
        - ::first-line
        - ::after
        
- What about scores of above selectors?

![Screenshot 2022-05-13 at 4.29.45 PM.png](Pseudo%20Elements,%20Pseudo%20Classes,%20and%20Specificity%20(%20404e1a00428145a78b71f733afc8df48/Screenshot_2022-05-13_at_4.29.45_PM.png)

# What is Specificity?

- If there are two or more CSS rules that point to the same element, the selector with the highest specificity value will "win", and its style declaration will be applied to that HTML element.
- Think of specificity as a score/rank that determines which style declaration are ultimately applied to an element.
- Let’s take an example

## Specificity using all combinators and selectors

- Think of specificity as a score/rank that determines which style declaration are ultimately applied to an element.
- Let’s take an example

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
    <style>
      /* Specificity score - 100 points */
      #masai {
        background-color: teal;
      }
      /* specificity score - 1 point */
      h1 {
        background-color: red;
      }
		
    </style>
  </head>
  <body>
		<div>
	    <h1 id="masai">Masai school</h1>
		</div>
  </body>
</html>
```

- In the above example id has more specificity score compared to tag, so background of `teal` will be applied.
- Now, what if I use combinators to style `h1` tag

```html
<style>
      /* Specificity score - 100 points */
      #masai {
        background-color: teal;
      }
      
      /* specificity score - 1 point */
      h1 {
        background-color: red;
      }

      /* specificity score - 1+1 = 2 points */
      div > h1 {
        background-color: yellow;
      }

      /* specificity score - 1+100 = 101 points */
      div > #masai {
        background-color: pink;
      }
    </style>
```

- Now since `div>#masai` has highest specificiy score of 101, `pink` will be applied

## Exercise

```jsx
ul.class  -> 1+10 = 11

h1+p -> 1+1 =2

.heading > .main -> 10+10=20

.heading > #main+p -> 10+100+1 = 111

#heading p ul li .box li -> 100+1+1+1+10+1 = 114

#navbar > p + #demo -> 100+1+100=201

h1 ~ p::first-letter -> 1+1+10= 12

```