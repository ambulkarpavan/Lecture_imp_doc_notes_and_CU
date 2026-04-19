# Flexbox (Basic) (60-70mins)

- Grid-based layout
- Images that resize
- Media queries

Historically, the primary way to make a website adaptive and responsive were HTML tables and CSS floats. It was not a very pleasant experience. But now, flexbox makes it super easy. Flexbox stands for flexible boxes, and they are literally super flexible.

flex container ⇒ parent

flex item ⇒ children

![Untitled](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Untitled.png)

If the `flex-direction` is `row` the horizontal axis becomes the main axis

![Untitled](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Untitled%201.png)

If the `flex-direction` is  `column` the vertical axis becomes the main axis.

All you need to remember is that the **main axis** goes in the direction of the layout. For column, it goes in the vertical direction and for the row, it goes in the horizontal direction.

### Parent (Flex Container)

```
display: flex | inline-flex;

flex-direction: row | row-reverse | column | column-reverse;

flex-wrap: wrap | nowrap | wrap-reverse;

flex-flow (shorthand for flex-direction and flex-wrap) (flex-flow: row wrap;)
```

```
justify-content (main axis): flex-start | flex-end | center | space-between | space-around | space-evenly;

align-items (cross axis): flex-start | flex-end | center | baseline | stretch;

```

```
align-content: flex-start | flex-end | center | stretch | space-between | space-around | space-evenly; [wrapping scenario]
```

```
gap: <length>
```

## **flex-direction**

- Next is `flex-direction`, which defines the direction in which the flex items are placed in the container.
- `flex-direction` can accept one of four values:
    - `row`
    - `row-reverse`
    - `column`
    - `column-reverse`
    

## **flex-direction: `row`**

- The first value is a row that is the `default` value of `flex-direction`. It doesn’t make any changes by default. It’s placed on the main axis from left to the right.

```html
<style>
.box {
    display: flex;
    flex-direction: row;
}
</style>
<div class="box">
    <div>1</div>
    <div>2</div>
    <div>3</div>
</div>
```

**Output:**

![Screenshot 2022-05-10 at 5.04.26 PM.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Screenshot_2022-05-10_at_5.04.26_PM.png)

**Live Code : [Codepen](https://codepen.io/vchandu111/pen/WNMwmXE)**

## **flex-direction: `row-reverse`**

- This sets the main access direction from right to left, which results in the flex items being placed from right to left. In the example below, you can see that the items are now placed in the reverse order. Item 1 is placed to the right:

```html
<style>
.box {
    display: flex;
    flex-direction: row-reverse;
}
</style>
<div class="box">
      <div>1</div>
      <div>2</div>
      <div>3</div>
</div>
```

**Output:**

![Screenshot 2022-05-10 at 5.09.18 PM.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Screenshot_2022-05-10_at_5.09.18_PM.png)

**Live Code : [Codepen](https://codepen.io/vchandu111/pen/QWQNoaq)**

## **flex-direction: `column`**

- When you set `flex-direction` to `column`, the main axis goes from top to bottom, so the items are now stacked on top of each other:

```html
<style>
.box {
    display: flex;
    flex-direction: column;
}
</style>
<div class="box">
      <div>1</div>
      <div>2</div>
      <div>3</div>
 </div>
```

**Output**:

![Screenshot 2022-05-10 at 5.11.18 PM.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Screenshot_2022-05-10_at_5.11.18_PM.png)

**Live Code : [Codepen](https://codepen.io/vchandu111/pen/NWyNJyg)**

## **flex-direction: `column-reverse`**

- We also have `column-reverse`, which stacks the items in the reverse order. Look at the example below. You can see Item 1 is at the bottom and Item 3 is at the top:

```html
<style>
.box {
    display: flex;
    flex-direction: column-reverse;
}
</style>
<div class="box">
      <div>1</div>
      <div>2</div>
      <div>3</div>
 </div>
```

**Output:**

![Screenshot 2022-05-10 at 5.12.30 PM.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Screenshot_2022-05-10_at_5.12.30_PM.png)

**Live Code : [Codepen](https://codepen.io/vchandu111/pen/VwQaRXY)**

![2.gif](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/2.gif)

# **flex-wrap**

- `flex-wrap` is used to control the wrapping of items within a container. If we reduce the browser width, we lose some items for the browser width.

- The behavior changes with the `flex-wrap` property. It can accept three possible values:
- `nowrap` (default value)
- `wrap`
- `wrap-reverse`

## **flex-wrap: `nowrap`**

- This is the `flex-wrap` property default value. If you set the property value to `nowrap`, there are no changes.(It’s a default property)

## **flex-wrap: `wrap`**

- When you set the `flex-wrap` property to `wrap`, you reduce the browser width that the items have wrapped in the container:

```html
<style>
.box {
    display: flex;
    flex-wrap: wrap;
}
</style>
<div class="box">
  <div>1</div>
  <div>2</div>
  <div>3</div>
  <div>4</div>
  <div>5</div>
  <div>6</div>
  <div>7</div>
  <div>8</div>
  <div>9</div>
</div>
```

**Output:**

![Screenshot 2022-05-10 at 5.17.07 PM.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Screenshot_2022-05-10_at_5.17.07_PM.png)

**Live Code : [Codepen](https://codepen.io/vchandu111/pen/JjpXzZQ)**

![w.gif](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/w.gif)

## **flex-wrap: `wrap-reverse`**

- Instead of items falling into the row below, they climb into the row above. Wrapping always occurs from the last item. `wrap-reverse` pushes the last item above instead of below:

```html
<style>
.box {
    display: flex;
    flex-wrap: wrap-reverse;
}
</style>
<div class="box">
  <div>1</div>
  <div>2</div>
  <div>3</div>
  <div>4</div>
  <div>5</div>
  <div>6</div>
  <div>7</div>
  <div>8</div>
  <div>9</div>
</div>
```

**Output:**

![Screenshot 2022-05-10 at 5.18.11 PM.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Screenshot_2022-05-10_at_5.18.11_PM.png)

**Live Code : [Codepen](https://codepen.io/vchandu111/pen/XWZdGBo)**

### Student Task : Design a horizontal navigation bar using a flex container. Set the **`flex-direction`** property to make the items lay out horizontally in reverse and apply a **`flex-wrap`** property to wrap items onto a new line when the container width is limited.

```jsx
.navbar {
  display: flex;
  flex-direction: row-reverse; /* Horizontal layout */
  flex-wrap: wrap; /* Wrap items when needed */
}
```

# **justified-content**

- `justified-content` defines the alignment of the items along the main axis. There are six possible values for the `justified-content` property:
    - `flex-start`
    - `flex-end`
    - `center`
    - `space-between`
    - `space-around`
    - `space-evenly`

## **justified-content: `flex-start`**

- Setting the value to `flex-start` places the flex items at the beginning of the main axis, which is also known as the main start. `flex-start` is the default value in this property.

```html
<style>
.box {
  display: flex;
  justify-content: flex-start;
}
</style>
<div class="box">
      <div>1</div>
      <div>2</div>
      <div>3</div>
</div>
```

**Output:**

![Screenshot 2022-05-10 at 5.20.27 PM.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Screenshot_2022-05-10_at_5.20.27_PM.png)

**Live Code : [Codepen](https://codepen.io/vchandu111/pen/poayYxV)**

## **justified-content: `flex-end`**

- This aligns the items to be placed at the end of the main axis:

```html
<style>
.box {
  display: flex;
  justify-content: flex-end;
}
</style>
<div class="box">
      <div>1</div>
      <div>2</div>
      <div>3</div>
 </div>
```

**Output:**

![Screenshot 2022-05-10 at 5.21.50 PM.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Screenshot_2022-05-10_at_5.21.50_PM.png)

**Live Code : [Codepen](https://codepen.io/vchandu111/pen/vYdGPQG)**

## **justified-content: `center`**

- The `center` value aligns all content at the center of the main axis:

```html
<style>
.box {
  display: flex;
  justify-content: center;
}
</style>
<div class="box">
      <div>1</div>
      <div>2</div>
      <div>3</div>
 </div>
```

**Output:**

![Screenshot 2022-05-10 at 5.22.45 PM.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Screenshot_2022-05-10_at_5.22.45_PM.png)

**Live Code : [Codepen](https://codepen.io/vchandu111/pen/MWQyxzq)**

## **justified-content: `space-between`**

- This value helps to evenly split extra space and add it in between the flex items:

```html
<style>
.box {
  display: flex;
  justify-content: space-between;
}
</style>
<div class="box">
      <div>1</div>
      <div>2</div>
      <div>3</div>
 </div>
```

**Output:**

![Screenshot 2022-05-10 at 5.23.33 PM.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Screenshot_2022-05-10_at_5.23.33_PM.png)

**Live Code : [Codepen](https://codepen.io/vchandu111/pen/BaYKbvZ)**

## **justified-content: `space-around`**

- This value splits the extra space at the beginning and the end. The space in question is equal to half of the space between the flex items:

```html
<style>
.box {
  display: flex;
  justify-content: space-around;
}
</style>
<div class="box">
      <div>1</div>
      <div>2</div>
      <div>3</div>
 </div>
```

**Output:**

![Screenshot 2022-05-10 at 5.24.40 PM.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Screenshot_2022-05-10_at_5.24.40_PM.png)

**Live Code : [Codepen](https://codepen.io/vchandu111/pen/NWyNJow)**

## **justified-content: `space-evenly`**

- This value distributes the extra space in the container:

```html
<style>
.box {
  display: flex;
  justify-content: space-evenly;
}
</style>
<div class="box">
      <div>1</div>
      <div>2</div>
      <div>3</div>
 </div>
```

**Output:**

![Screenshot 2022-05-10 at 5.26.19 PM.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Screenshot_2022-05-10_at_5.26.19_PM.png)

**Live Code : [Codepen](https://codepen.io/vchandu111/pen/NWyNJJX)**

## Justify-content Overview

![3.gif](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/3.gif)

> ***Open masai school website and open testimonials and annotate the box with image and logo, it is space-between. Then, click on courses and show  Next batch card and Upcoming Batches card also, space-between is used.***
> 

# **align-items**

The `align-items` property defines how the flex items are laid out along the cross axis, i.e., vertical alignment. Justify content is horizontal alignment.

- `align-items: stretch`
- `align-items: flex-start`
- `align-items: flex-end`
- `align-items: center`
- `align-items: baseline`

## **align-items: `stretch`**

- The items stretch the entire length of the cross axis and `stretch` is the `default` value:

```html
#box {
        display: flex;
        align-items: stretch;
        padding: 50px;
        height: 300px;
        background-color: #c3a7a7;
      }
      #box > div {
        width: 100px;
      }
      #box > div:first-child {
        background-color: cadetblue;
        padding: 100px 0;
      }
      #box > div:nth-child(2) {
        background-color: coral;
        padding: 50px 0;
      }
      #box > div:last-child {
        background-color: mediumslateblue;
        padding: 75px 0;
      }

<div id="box">
      <div>1</div>
      <div>2</div>
      <div>3</div>
    </div>
```

**Output:**

![Screenshot 2022-05-10 at 5.28.04 PM.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Screenshot_2022-05-10_at_5.28.04_PM.png)

**Live Code : [Codepen](https://codepen.io/vchandu111/pen/OJQNqYg)**

## **align-items: `flex-start`**

- This is the starting point of the cross axis. The cross axis flows from top to bottom. The item doesn’t stretch and is aligned with the cross start of the line:

```html
<style>
.box {
  height: 300px;
  display: flex;
  align-items: flex-start;
}
</style>
<div class="box">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>
```

**Output:**

![Screenshot 2022-05-10 at 5.30.22 PM.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Screenshot_2022-05-10_at_5.30.22_PM.png)

**Live Code : [Codepen](https://codepen.io/vchandu111/pen/eYVZXax)**

## **align-items: `flex-end`**

- This value pushes the items to the end of the cross axis:

```html
<style>
.box {
  height: 300px;
  display: flex;
  align-items: flex-end;
}
</style>
<div class="box">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>
```

**Output:**

![Screenshot 2022-05-10 at 5.32.01 PM.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Screenshot_2022-05-10_at_5.32.01_PM.png)

**Live Code : [Codepen](https://codepen.io/vchandu111/pen/OJQNqYg)**

## **align-items: `center`**

- This centers the content along the cross axis:

```html
<style>
.box {
  height: 300px;
  display: flex;
  align-items: center;
}
</style>
<div class="box">
    <div class="box-item">1</div>
    <div class="box-item">2</div>
    <div class="box-item">3</div>
    <div class="box-item">4</div>
</div>
```

**Output:**

![Screenshot 2022-05-10 at 5.32.29 PM.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Screenshot_2022-05-10_at_5.32.29_PM.png)

**Live Code : [Codepen](https://codepen.io/vchandu111/pen/OJQNqYg)**

## Align-items Overview

![q.gif](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/q.gif)

### Student Task : Build a flex container with multiple items and use the **`flex-direction`** property to stack items vertically. Implement both horizontal and vertical alignment using **`justify-content`** and **`align-items`** properties.

```jsx
.container {
  display: flex;
  flex-direction: column; /* Vertical stacking */
  justify-content: center; /* Horizontal alignment */
  align-items: center; /* Vertical alignment */
}
```

## Children (Flex Items)

```
order: <integer>;

align-self: overrides alignment set on parent

flex-grow: <number>; (Defaults to 0)

flex-shrink: <number>; (Defaults to 1)

flex-basis: <length> | auto; (Defaults to auto ) [starting width]

flex: shorthand for grow, shrink, and basis (default:  0 1 auto)
```

# Child **Properties**

- `order`
- `flex-grow`
- `flex-shrink`
- `flex-basis`

***But we’ll learn only order and flex-grow which are important and you can read about flex shrink and flex basis.***

## **`order`**

- The **order** property of CSS can be used for ordering flex items. It specifies the order of a flex item with respect to the other flex items. The element has to be a flexible item for the order property to work. The elements are displayed in ascending order of their order values. If two elements have the same order value then they are displayed on the basis of their occurrence in the source code.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <style>
      body {
        margin: 0;
      }
      .container {
        border: 6px solid black;
        display: flex;
      }
      .container > div {
        color: white;
        font-size: 25px;
        padding: 15px;
        text-align: center;
      }
      #item1 {
        background-color: cadetblue;
				order:0 ==> default
				***keep order : 1 and show the output***
      }
      #item2 {
        background-color: coral;
				***keep order : 2 and show the output***
      }
      #item3 {
        background-color: darkgoldenrod;
      }
      #item4 {
        background-color: darkcyan;
      }
      #item5 {
        background-color: darkmagenta;
      }
      #item6 {
        background-color: darkolivegreen;
      }
      #item7 {
        background-color: darksalmon;
      }
      #item8 {
        background-color: deepskyblue;
      }
      #item9 {
        background-color: darkslategrey;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div id="item1">Item 1</div>
      <div id="item2">Item 2</div>
      <div id="item3">Item 3</div>
      <div id="item4">Item 4</div>
      <div id="item5">Item 5</div>
      <div id="item6">Item 6</div>
      <div id="item7">Item 7</div>
      <div id="item8">Item 8</div>
      <div id="item9">Item 9</div>
    </div>
  </body>
</html>
```

**Output:**

![Screenshot 2022-05-10 at 6.20.11 PM.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Screenshot_2022-05-10_at_6.20.11_PM.png)

**Live Code : [Codepen](https://codepen.io/vchandu111/pen/abqNxZz)**

## **`flex-grow`**

> ***In order to understand flex-grow property clearly, we will keep only 3 divs.***
> 
- `flex-grow` allows a flex item to grow if necessary. This property specifies what amount of  remaining space inside the flex container the item should take up. All flex items have a `flex-grow` of zero by default.

```html
<style>
    .box {
        display: flex;
     }
   .box > div:first-child {
        flex-grow: 1;
     }
		.box > div:nth-child(2){
				flex-grow:1
		}
</style>
<div class="box">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>
```

> ***So, if there is a gap of 400px, and the flex grow property is 1 : 1, like ratio, it’ll take 200px and 200px each.***
> 

**Output:**

![Screenshot 2022-05-10 at 6.22.23 PM.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Screenshot_2022-05-10_at_6.22.23_PM.png)

**Live Code : [Codepen](https://codepen.io/vchandu111/pen/oNExRgo)**

## **`flex-shrink`**

- `flex-shrink` defines the capacity for a flex item to shrink if necessary. The default value of `flex-shrink` is one.

```html
<style>
    .box {
        display: flex;
     }
   .item-1 {
        flex-shrink: 4;
     }
</style>
<div class="box">
  <div>1</div>
  <div>2</div>
  <div>3</div>
  <div>4</div>
  <div>5</div>
  <div>6</div>
  <div>7</div>
  <div>8</div>
  <div>9</div>
</div>
```

**Output:**

![https://miro.medium.com/max/990/1*VRzYKwb5x8i7UNO6N_yUcw.png](https://miro.medium.com/max/990/1*VRzYKwb5x8i7UNO6N_yUcw.png)

## **`flex-basis`**

- `flex-basis` specifies the initial main size of a flex item before the extra space in the container is distributed:

```html
<style>
    .box {
        display: flex;
     }
   .item-1 {
        flex-basis: 400px;
     }
</style>
<div class="box">
    <div class="box-item">1</div>
    <div class="box-item">2</div>
    <div class="box-item">3</div>
    <div class="box-item">4</div>
    <div class="box-item">5</div>
    <div class="box-item">6</div>
    <div class="box-item">7</div>
    <div class="box-item">8</div>
    <div class="box-item">9</div>
</div>
```

**Output:**

![z.png](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/z.png)

## Examples

**Two possibilities:** 

- number of columns & their ratio is known - we use percentages & gap
- number of columns is known but we need their ratios to be dynamic - we use separate containers for each row and let flexbox calculate the width (space-in between)
- number of columns is not known - we use padding or margins for gap (space-in between)

## Exercise - fundamentals

![q4.jpg](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/q4.jpg)

![responsive-flexbox.gif](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/responsive-flexbox.gif)

- Calculation
    
    ![Untitled](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Untitled%202.png)
    

start: [https://codepen.io/drupalastic/pen/abwvddV?editors=1100](https://codepen.io/drupalastic/pen/abwvddV?editors=1100) 

end: [https://codepen.io/drupalastic/pen/QWgjNzB?editors=0100](https://codepen.io/drupalastic/pen/QWgjNzB?editors=0100) 

## Exercise - 4 Column grid system

Welcome to our simple grid system! This documentation will provide an overview of how to use the grid to create responsive layouts with ease.

### 1. Overview

Our grid system utilizes flexible `row` and `col` classes. Additionally, we use `span` classes to control the width of columns within rows.

### 2. Basic Structure

```html
<div class="row">
  <div class="col">Your Content</div>
</div>

```

### Rows

- Class `row`: The foundational block of our grid system. It ensures the contained columns flex and wrap correctly.

### Columns

- Class `col`: By default, columns are equally distributed within rows.

To define the width of columns, use `span-*` classes.

- `span-2`: Makes the column take up approximately 48% of the row width.
- `span-3`: Makes the column take up approximately 74% of the row width.
- `span-4`: Makes the column take up the entire row width.

### 3. Responsive Behavior

(Don’t worry about responsiveness in your first attempt)

By default, on screens smaller than 576px, columns will stack, each taking the full width of its container. On screens larger than this breakpoint, the columns will align side by side, adhering to the defined `span-*` classes or defaulting to equal distribution.

For responsive spans, you may need to create different versions of spans for large, small & medium screens, for example: `span-2-lg` `span-2-md` `span-2-lg` etc.

### 4. Custom Styling

### Rows

- Background Color: `gold`
- Border: Dashed 3px black
- Padding: `20px`
- Margin Bottom: `20px`

### Columns

- Border: Solid 3px #333
- Background Color: `#dfdfdf`
- Font Size: `20px`

### 5. Example

```html
<div class="row">
  <div class="col span-2">This is 48% width content.</div>
  <div class="col span-3">This is 74% width content.</div>
  <div class="col">This column will distribute equally with other standard columns.</div>
</div>

```

### 6. Final Notes

This grid system is meant to be lightweight and straightforward. For more advanced layouts or additional functionality, consider expanding upon this foundation or exploring other robust grid systems.

Thank you for choosing our simple grid system. Happy coding!

![Untitled](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Untitled%203.png)

![Untitled](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Untitled%204.png)

![Untitled](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Untitled%205.png)

Start: [https://codepen.io/drupalastic/pen/PojogPZ](https://codepen.io/drupalastic/pen/PojogPZ)

Simple Solution with breakpoints: [https://codepen.io/drupalastic/pen/WNObrGp](https://codepen.io/drupalastic/pen/WNObrGp)

Complete grid solution: [https://codepen.io/drupalastic/pen/WNLPvZP](https://codepen.io/drupalastic/pen/WNLPvZP) 

## 

## Game

[https://codepip.com/games/flexbox-froggy/](https://codepip.com/games/flexbox-froggy/)

`Solution - [https://gist.github.com/lukasrudnik/c72cafebd0db5bae4aa5563b24e73fd2](https://gist.github.com/lukasrudnik/c72cafebd0db5bae4aa5563b24e73fd2)`

## Exercise - Responsive card layout

![Untitled](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Untitled%206.png)

![Untitled](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Untitled%207.png)

![Untitled](Flexbox%20(Basic)%20(60-70mins)%2066ec31d5c2c44ff59c1e716bade6b89d/Untitled%208.png)

Start: [https://codepen.io/drupalastic/pen/jOwPabR](https://codepen.io/drupalastic/pen/jOwPabR)

End: [https://codepen.io/drupalastic/pen/NWgrJmy?editors=0100](https://codepen.io/drupalastic/pen/NWgrJmy?editors=0100)

End2: [https://codepen.io/drupalastic/pen/BaZLjXv?editors=0100](https://codepen.io/drupalastic/pen/BaZLjXv?editors=0100)