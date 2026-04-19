# Introduction to CSS (Basic) (15mins)

### History of CSS

- Before CSS we used to have black and white layouts, just like emails

![Screenshot 2022-04-06 at 10.37.13 AM.png](Introduction%20to%20CSS%20(Basic)%20(15mins)%20605ebc57063a49ad89dbb57040b8e1ed/Screenshot_2022-04-06_at_10.37.13_AM.png)

- There are various properties in CSS to set and change the color of the elements.

> ***For all tags, there is a common attribute called style.***
> 

### How to add CSS to HTML?

![Combinators.jpg](Introduction%20to%20CSS%20(Basic)%20(15mins)%20605ebc57063a49ad89dbb57040b8e1ed/Combinators.jpg)

Units to mention the size of elements are pixels (px), %, vh, vw, em, rem.

3 ways of adding colors to your text

```html
<h1 style="color: blue;">Title</h1> 
<h1 style="color: #fcde9f;">Title</h1>
<h1 style="color: rgb(252,222,159)">Title</h1>
```

In HTML we have tags such as 

```html
<i>Italic</i>
<u>Underline</u>
<b>Bold</b>
<strong>Bold</strong>
```

In CSS to decorate your text

```jsx
font-size: 30px;
font-weight: bold;
font-style: italic;
text-align: center;
text-decoration:line-through;
text-shadow: #fcde9f;
```

# Types of CSS color values

- There are various color values in CSS through which you can specify the color to your HTML elements. These values are in different formats, which are explained below.

## CSS  Color Keywords

- Using a keyword (such as `blue` or `transparent`).
- Color keywords are case-insensitive identifiers that represent a specific color, such as `red`, `blue`, `black`, or `lightseagreen`. Although the names more or less describe their respective colors, they are essentially artificial, without a strict rationale behind the names used.
- The complete list of such keywords is available [here](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/color_keywords).

**Example:**

```html
<p style="color:blue">I am paragraph</p>
```

Now, there are 2 more ways to represent colors.

## CSS RGB Colors

- RGB value is the combination of Red, Green, and Blue colors.
- An RGB color value is specified with : rgb(red, green, blue). The range of these three colors is defined from 0 to 255 and it defines the intensity of the color. The colors can be changed by changing these values.

**Example:**

```html
<p style="color:rgb(0, 0, 255)">I am paragraph</p>
```

### CSS HEX Colors

- The colors in CSS can be specified in Hexadecimal values also.
- A hexadecimal color is a 6 digit representation of the color.
- The notation of the HEX value starts with the "#" symbol followed by the six characters within the range of 0 to F.

**Example:**

```html
<p style="color:#bfff00">I am paragraph</p>
```

- Overview of all types of colors

![CSS-Color-Codes.jpg.jpeg](Introduction%20to%20CSS%20(Basic)%20(15mins)%20605ebc57063a49ad89dbb57040b8e1ed/CSS-Color-Codes.jpg.jpeg)

> ***Also, tell about background color property: Syntax ==⇒ background-color:pink***
> 

# **CSS Font-size**

- In CSS the font-size property is used to set or tweak the size of the font.
- It can have several values that can be absolute (eg.- xx-small, medium, xx-large.) or relative (larger, smaller, %) or length (numbered- 12px, 1em, etc.)

![Screenshot 2022-05-04 at 10.45.02 AM.png](Introduction%20to%20CSS%20(Basic)%20(15mins)%20605ebc57063a49ad89dbb57040b8e1ed/Screenshot_2022-05-04_at_10.45.02_AM.png)

# Text-align:

> ***Open google docs and show them text alignment.***
> 
- We use the CSS `text-align`property to align content inside a block-level element.
- This alignment affects the horizontal axis only.

# **Basic Syntax**

- The `text-align` property accepts `left`, `center`, `right`, `justify` as values.
- The `left` Value: The `left` value of the `text-align` property is the default. So, every content inside a block-level element is aligned to the left by default.
- The `center` Value: With the center value, spaces are created on the left and right, so, everything gets pushed to the center.
- The `right` Value:Assigning a value of `right` to the `text-align` property pushes the content inside a block-level element to the right.

![Screenshot 2022-05-04 at 10.52.09 AM.png](Introduction%20to%20CSS%20(Basic)%20(15mins)%20605ebc57063a49ad89dbb57040b8e1ed/Screenshot_2022-05-04_at_10.52.09_AM.png)

- The `justify` Value:The `justify` value of the `text-align` property lines up the content on the left and right edges of the block-level element (the box). If the last line isn't a full line, then it leaves it alone. It's easier to see how this works in the image below: Justify is normally seen in newspapers.

![Screenshot 2022-05-04 at 10.54.41 AM.png](Introduction%20to%20CSS%20(Basic)%20(15mins)%20605ebc57063a49ad89dbb57040b8e1ed/Screenshot_2022-05-04_at_10.54.41_AM.png)

**student task:**

Problem: [Link](https://codepen.io/Pavan-Ambulkar/pen/MWLBxKY)

Solution: [Link](https://codepen.io/Pavan-Ambulkar/pen/qBgyvOm)