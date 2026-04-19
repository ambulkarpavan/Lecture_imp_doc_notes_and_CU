# Box & Box Model (Basic) (50mins)

# Creating boxes

We use div to create boxes. We specify length, width and border for the same.

## Styling a table

**Example: 1**

![Untitled](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/Untitled.png)

```html
<table>
        <caption>The first table</caption>
        <thead>
            <tr>
                <th>Lime</th>
                <th>Knocky</th>
                <th>Flor</th>
                <th>Ella</th>
                <th>Juan</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Breed</td>
                <td>Jack Russell</td>
                <td>Poodle</td>
                <td>Streetdog</td>
                <td>Cocker Spaniel</td>
            </tr>
            <tr>
                <td>Age</td>
                <td>16</td>
                <td>9</td>
                <td>10</td>
                <td>5</td>
            </tr>
            <tr>
                <td>Owner</td>
                <td>Mother-in-law</td>
                <td>Me</td>
                <td>Me</td>
                <td>Sister-in-law</td>
            </tr>
            <tr>
                <td>Eating Habits</td>
                <td>Eats everyone</td>
                <td>Nibbles at food</td>
                <td>Hearty eater</td>
                <td>Will eat tills</td>
            </tr>
        </tbody>
        <tfoot>
            <tr>
                <td colspan="4">Total</td>
                <td >40</td> <!-- Sum of ages -->
            </tr>
        </tfoot>
    </table>
```

```html
table {
          border-collapse: collapse;
          width: 100%;
          margin-top: 20px;
      }

      th, td {
          border: 1px solid #ddd;
          padding: 8px;
          text-align: left;
      }

      th {
          background-color: #f2f2f2;
      }

      colgroup col:last-child, th:last-child, td:last-child {
          width: 200px;
          text-align: center;
					background-color: yellow;
      }
```

You can also apply styles to the last column as below. The empty tag <col /> is needed.

```html
<table>
<col />
<col />
<col />
<col />
<col style="background-color: #f2f2f2; width: 200px; text-align: center;"/>
```

**Example: 2**

- Basic Excel sheet and show them heading of the table and body of the table in google sheets.

![Screenshot 2021-09-24 at 8.51.09 PM.png](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/Screenshot_2021-09-24_at_8.51.09_PM.png)

Here, in the above table, we’ve in theads, 1 row and 3 columns and in tbody ⇒ 2 rows and 3 cols. Now, the row in tbody is represented by tr and col is represented by td(table division). 

Now code the same in vs code.

The `<table>` tag defines an HTML table.

An HTML table consists of one `<table>` element and one or more [<tr>](https://www.w3schools.com/tags/tag_tr.asp), [<th>](https://www.w3schools.com/tags/tag_th.asp), and [<td>](https://www.w3schools.com/tags/tag_td.asp) elements.

The <tr> element defines a table row, the <th> element defines a table header, and the <td> element defines a table cell.

Codepen Link : [https://codepen.io/vchandu111/pen/qBVbdQO](https://codepen.io/vchandu111/pen/qBVbdQO)

**Read more**:

- [Table](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)
- [Table Head](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/thead)
- [Table Body](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tbody)
- [TH](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th)
- [TR](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr)
- [TD](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td)

> ***Now, a table has border right, so attribute for table is border and value is 1 and for single line border → use, border-collapse as collapse in style tag.***
> 

# Box Model

The CSS box model is a container that contains multiple properties including
borders, margin, padding, and the content itself. It is used to create the design
and layout of web pages.

![Untitled](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/Untitled%201.png)

![Untitled](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/Untitled%202.png)

# Visualising box model

![div.jpg](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/div.jpg)

[Masai School - Meet our Investors](https://www.masaischool.com/our-investors)

# **Properties of the Box Model**

## **Content**

- The content area consists of content like image, text, or other forms of media content. The height and width properties help to modify the box dimensions.

## **Padding**

- The padding area is the space around the content area and within the border-box. It can be applied to all sides of the box or to the specific, selected side(s) - top, right, bottom, and/or left.

## **Border**

- The border area surrounds the padding and the content, and can be applied to all the sides of the box or to selected side(s) - top, right, bottom, and/or left.

## **Margin**

- The margin area consists of space between the border and the margin. The margin does not possess its own background color and is completely transparent. It shows the background color of the element, like the body element.

## What is Margin in CSS?

- Margin is a CSS property that defines the empty space around an HTML element. Margins ensure that the specified region around an element remains unoccupied by any neighboring element.

## Syntax

There are four margin properties, one for each side of the HTML element box.

- **margin-top:** adds margin space on top of the element.
- **margin-right:** adds margin space on the right of the element.
- **margin-bottom:** adds margin space on the bottom of the element.
- **margin-left:** adds margin space on the left of the element.

![Screenshot 2022-05-04 at 12.00.22 PM.png](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/Screenshot_2022-05-04_at_12.00.22_PM.png)

- In above example, we are setting a margin of 20px on the top and left sides and also a margin of 40px on the right and bottom side.

## **CSS Margin Shorthand Property**

- **Single Value (margin:20px )** :
    - The single value is set as margin on all four sides.
        
        ![Screenshot 2022-05-04 at 11.58.24 AM.png](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/Screenshot_2022-05-04_at_11.58.24_AM.png)
        

- **Two Values (margin:4px 5px ):**
    - The first value is set as vertical margin (top & bottom) while the second is set as horizontal margin (right & left).
    
    ![Screenshot 2022-05-04 at 12.03.05 PM.png](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/Screenshot_2022-05-04_at_12.03.05_PM.png)
    
- **Three Values (margin:4px 5px 2px ):**
    - The first value is set as top margin, second as horizontal margin (right & left) while the third is set as bottom margin.
    
    ![Screenshot 2022-05-04 at 12.03.49 PM.png](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/Screenshot_2022-05-04_at_12.03.49_PM.png)
    
- **Four values (margin:4px 5px 2px 1px ):**
    - The values are assigned to margins on sides starting from top and moving in a clockwise direction, i.e. the four values are set as top, right, bottom and left margin respectively.
    
    ![Screenshot 2022-05-04 at 12.05.18 PM.png](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/Screenshot_2022-05-04_at_12.05.18_PM.png)
    
    # Negative margin:
    
    - Positive margin values move the content towards the inner side of its position or page. But if we take negative margin values, it moves the content towards outside of its position or page. The margin property in html gives space around the outermost element’s content of the box-like structure
    
    ![Screenshot 2022-05-04 at 12.12.31 PM.png](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/Screenshot_2022-05-04_at_12.12.31_PM.png)
    
- A funny example of negative margin

![hotel-room-css-air-conditioner-between-rooms-negative-css-margin.jpeg](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/hotel-room-css-air-conditioner-between-rooms-negative-css-margin.jpeg)

## Example Code

## ***Now, let’s open an assignment and build the investors page layout.***

 ******

```jsx
<html>
  <head>
    <title>Box model</title>
    <style>
      h1 {
        text-align: center;
      }
      #parentBox {
        width: 80%;
        border: 1px solid red;
        margin: auto;
        display: flex;
        /* can give height as auto so that it takes
         the height of the content present inside it */
        height: auto;
      }
      .box {
        /* height: 92%; */
        width: 23%;
        border: 1px solid blue;
        margin: auto;
      }
      .avatar {
        width: 100%;
      }
      .tc {
        text-align: center;
      }
      .logo {
        width: 140px;
       //display:block;
        margin:auto
      }
    </style>
  </head>
  <body>
    <h1>Strategic Investors</h1>
    <div id="parentBox">
      <div class="box">
        <img class="avatar" src="" alt="" />
        <h2 class="tc">Name of investor</h2>
        <p class="tc">Founder & CEO</p>
        <img class="logo" src="" alt="" />
      </div>
      <div class="box"></div>
      <div class="box"></div>
      <div class="box"></div>
    </div>
  </body>
</html>
```

> ***Margin auto will be applicable for block level elements only since it has width right. So, margin auto won’t work for img tag. Then, how do we center the image. We make img element as block and then use margin auto.***
> 

## Block, Inline and Inline-block Elements

Inline elements do not start on a new line and only take up as much width as necessary. They typically flow within the content and do not create a new "block" of content.

- **`<span>`**
- **`<a>`** (anchor)
- **`<strong>`** and **`<em>`** (text emphasis)
- **`<img>`** (image)
- **`<br>`** (line break)
- **`<i>`** (italic)
- **`<b>`** (bold)
- **`<u>`** (underline)
- **`<small>`** (small text)
- **`<code>`** (code)

![block-and-inline-elements.jpeg](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/block-and-inline-elements.jpeg)

```html
<!-- Block-->
    <div style="background-color: yellow;">Hello</div>
    <p style="background-color: pink;">Hello</p>

    <div style="background-color: yellow; width: 100px; height: 100px;">Hello</div>
    <div style="background-color: pink; width: 100px; height: 100px;">Hello</div>
```

![Untitled](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/Untitled%203.png)

Block elements typically start on a new line and take up the full width available.

- **`<div>`**
- **`<p>`** (paragraph)
- **`<h1>`**, **`<h2>`**, ..., **`<h6>`** (headings)
- **`<ul>`**, **`<ol>`**, **`<li>`** (lists)
- **`<table>`**, **`<tr>`**, **`<th>`**, **`<td>`** (table elements)
- **`<form>`**, **`<input>`**, **`<button>`**, **`<textarea>`** (form elements)
- **`<blockquote>`** (block quotation)
- **`<hr>`** (horizontal rule)
- **`<header>`**, **`<footer>`**, **`<section>`**, **`<article>`**, **`<nav>`**, **`<aside>`** (HTML5 structural elements)

```html
<!-- Inline -->
    <span style="background-color: yellow;">Hello</span>
    <span style="background-color: pink;">Hello</span>

    <span style="background-color: yellow; width: 100px; height: 100px;">Hello</span>
    <span style="background-color: pink; width: 100px; height: 100px;">Hello</span>
```

![Untitled](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/Untitled%204.png)

Inline-block elements combine aspects of both inline and block elements. They flow like inline elements but can have block-level properties like setting width and height.

```html
<!-- Inline block -->
    <span style="display: inline-block; background-color: yellow; width: 100px; height: 100px;">Hello</span>
    <div style="display: inline-block; background-color: pink; width: 100px; height: 100px;">Hello</div>
```

![Untitled](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/Untitled%205.png)

# Tasks

1. [https://codepen.io/Rahul-Rajeevan-the-scripter/pen/PoXxmdv](https://codepen.io/Rahul-Rajeevan-the-scripter/pen/PoXxmdv)

![Untitled](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/Untitled%206.png)

1. Create the following layout.

![Untitled](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/Untitled%207.png)

# Box sizing

The **`box-sizing`** property in CSS is used to control how the sizing of an element is calculated. It determines whether an element's width and height should include padding and borders or not.

![Untitled](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/Untitled%208.png)

![Untitled](Box%20&%20Box%20Model%20(Basic)%20(50mins)%20402338cd28d344eab8cfd94e24650f5f/Untitled%209.png)