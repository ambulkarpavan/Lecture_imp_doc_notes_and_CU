# CSS Selectors (Basic) (30mins)

[https://www.canva.com/design/DAFpqAYUCuI/THgqnPk6B5uwSxjBS5cysA/edit?utm_content=DAFpqAYUCuI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton](https://www.canva.com/design/DAFpqAYUCuI/THgqnPk6B5uwSxjBS5cysA/edit?utm_content=DAFpqAYUCuI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

# CSS Selectors

1. Id (100)
2. Class & pseudo-classes(10)
3. Tag & pseudo elements (1)
4. Universal (0)

`Combinators, such as [+](https://developer.mozilla.org/en-US/docs/Web/CSS/Next-sibling_combinator), [>](https://developer.mozilla.org/en-US/docs/Web/CSS/Child_combinator), [~](https://developer.mozilla.org/en-US/docs/Web/CSS/Subsequent-sibling_combinator), [" "](https://developer.mozilla.org/en-US/docs/Web/CSS/Descendant_combinator), and [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Column_combinator), may make a selector more specific in what is selected but they don't add any value to the specificity weight.`

Try to clone:
[Masai School - Become an Industry Mentor](https://www.masaischool.com/become-coach)

Student task

1. Create a button that on hovering changes color from red to blue.

2. Create this 

![Untitled](CSS%20Selectors%20(Basic)%20(30mins)%207202204b211e4c6392469dbc5ee98af3/Untitled.png)

# **What Are Selectors?**

- ***A selector in CSS is a part of the CSS ruleset, that is basically used to select the element you want to style. CSS selectors select HTML elements according to their id, class, type, attribute, etc.***

## Why do we need Selectors?

> ***We’ve learnt style attribute right. Then, why do we need Selectors? Because we can write less code using selectors by avoiding repeating style attributes. For example, if we want to style all the h1 tags to a color green, using style attribute we’ve to write for each and every h1 tag but it is not the same in selectors. We’ll see how we can achieve it using selectors in a moment.***
> 

# **Types of Selectors**

There are various types of selectors in CSS. They are:

1. **CSS Element / tag Selector**
2. **CSS Id Selector**
3. **CSS Class Selector**
4. **CSS Universal Selector**

## **CSS Element or tag Selector**

- The element selectors select the HTML elements by its tag name.

![Screenshot 2022-05-04 at 9.19.32 PM.png](CSS%20Selectors%20(Basic)%20(30mins)%207202204b211e4c6392469dbc5ee98af3/Screenshot_2022-05-04_at_9.19.32_PM.png)

- All the <p> elements will be center-aligned and all h1’s will get teal color
- **Live code - [click here](https://codepen.io/vchandu111/pen/yLvNPzd)**

## CSS ID Selector

### Instructor Task:

- **Explaining the analogy of an IPL team.**
- In a team, there are so many players
- When you want to point out or select one player.
- In this case, you will call out his jersey number/ name to pick up.
- This is similar to an id selector where we pick up a tag based on a particular id name
- [Codepen](https://codepen.io/vchandu111/pen/WNdOxwG)
- In the above example, we want to select dhoni, we have to use the ID selector

![dhoni.png](CSS%20Selectors%20(Basic)%20(30mins)%207202204b211e4c6392469dbc5ee98af3/dhoni.png)

- An ID selector is declared using a hash, or pound symbol (`#`) preceding a string of characters.
- This selector matches any HTML element that has an ID attribute with the same value as that of the selector.
- Here’s an example:

![id.png](CSS%20Selectors%20(Basic)%20(30mins)%207202204b211e4c6392469dbc5ee98af3/id.png)

- **Live code : [Click here](https://codepen.io/vchandu111/pen/WNdOxwG)**

## CSS Class selector:

- Now you want to select a group of players based on their team name eg,(CSK,MI,RCB)
- In this case we can will call out by using class selector, so all players with particular class  will be selected
- [Codepen](https://codepen.io/vchandu111/pen/gOvpqMa)

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <style>
      .csk{
        background-color:yellow
      }

      .rcb{
        background-color:rgb(182, 65, 65)
      }
    </style>

  </head>
  <body>
    <p class="csk" id="dhoni">I am Dhoni from Chennai</p>
    <p class="mi">I am Sachin from Mumbai</p>
    <p class="rcb">I am Kohli from Banglore</p>
    <p class="mi">I am Rohit from Mumbai</p>
    <p class="rcb" id="abd">I am ABD from Banglore</p>
    <p class="csk">I am Raina from Chennai</p>
  </body>
</html>
```

- In the above example we are selecting rcb team members

![RCBSquadWeb.jpeg](CSS%20Selectors%20(Basic)%20(30mins)%207202204b211e4c6392469dbc5ee98af3/RCBSquadWeb.jpeg)

## Universal selectors:

- Now you wants to select all teams at once, in this case we will use universal selector
- [Codepen](https://codepen.io/vchandu111/pen/ZEvyOLv)

![Screenshot 2022-05-05 at 12.00.50 PM.png](CSS%20Selectors%20(Basic)%20(30mins)%207202204b211e4c6392469dbc5ee98af3/Screenshot_2022-05-05_at_12.00.50_PM.png)

## Now, let’s look at an example, let’s create a single p tag with different properties.

```jsx
<html lang="en">
  <head>
    <style>
      * {
        font-size: 60px;
        color: teal;
        font-style: italic;
        font-weight: bold;
        text-align: center;
      }

      p {
        color: red;
      }

      .online {
        font-size: 100px;
        color: rgb(146, 146, 39);
      }

      #school {
        font-style: normal;
        font-size: 150px;
        color: green;
      }
    </style>
  </head>
  <body>
    <p id="school" class="online" style="color: pink">Masai School</p>
  </body>
</html>
```

## Priority of Selectors

![Screenshot 2022-05-05 at 12.49.11 PM.png](CSS%20Selectors%20(Basic)%20(30mins)%207202204b211e4c6392469dbc5ee98af3/Screenshot_2022-05-05_at_12.49.11_PM.png)

![Screenshot 2022-05-05 at 1.45.01 PM.png](CSS%20Selectors%20(Basic)%20(30mins)%207202204b211e4c6392469dbc5ee98af3/Screenshot_2022-05-05_at_1.45.01_PM.png)

- Follow this order **SICTU**
    - S - inline style
    - I  - Id selector
    - C - Class selector
    - T - Type/Tag selector
    - U - Universal selector
- [Codepen](https://codepen.io/vchandu111/pen/abEwZVQ)

## Same Selectors Multiple Definitions:

- **Different Properties** - All the different properties are applied to the elements
    
    ![same.png](CSS%20Selectors%20(Basic)%20(30mins)%207202204b211e4c6392469dbc5ee98af3/same.png)
    

- **Live code: [codepen](https://codepen.io/vchandu111/pen/XWZmJPa)**
- **Same Properties** - Properties Values Defined at the bottom are applied to the elements

![sameDiff.png](CSS%20Selectors%20(Basic)%20(30mins)%207202204b211e4c6392469dbc5ee98af3/sameDiff.png)

- **Live Code: [codepen](https://codepen.io/vchandu111/pen/RwQWNed)**

## Multiple Classes, Definitions & Ordering:

- Different Properties - All the different properties are applied to the elements
- Same Properties - Properties Values Defined at the bottom are applied to the elements
- [Codepen](https://codepen.io/vchandu111/pen/qBpjNpv)

## div tag

Let us learn about div tag now.

The `<div>` tag defines a division or a section in an HTML document.

The `<div>` tag is used as a container for HTML elements - which is then styled with CSS or manipulated with JavaScript.

Any sort of content can be put inside the `<div`tag!

The **`<div`HTML** element is the generic container for flow content. It has no effect on the content or layout until styled in some way using CSS (e.g. styling is directly applied to it)