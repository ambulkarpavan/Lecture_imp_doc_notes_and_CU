# CSS Grid (Basic) (60-70mins)

## Introduction: Flex Vs Grid

![Flexbox-vs-CSS-Grid.webp](CSS%20Grid%20(Basic)%20(60-70mins)%20cac801f2aded4b979da33d78d7b57539/Flexbox-vs-CSS-Grid.webp)

> ***The basic difference between flex and grid is flex is a one dimensional layout whereas grid is a two dimensional layout.***
> 

## **Basic Grid :**

```html
<style>
      #container {
        display: grid;
      }
			#container > div {
        padding:20px;
				font-size:20px;
				color:white;
      }
			#container > div:nth-child(1) {
        background-color: cornsunflowerblue;
      }
			#container > div:nth-child(2) {
        background-color: crimson;
      }
			#container > div:nth-child(3) {
        background-color: olivegreen;
      }
			#container > div:nth-child(4) {
        background-color: teal;
      }
			
			
    </style>
  </head>
  <body>
    <div id="container">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>    
		</div>
  </body>
```

**Output**:

![Screenshot 2022-05-09 at 10.56.42 PM.png](CSS%20Grid%20(Basic)%20(60-70mins)%20cac801f2aded4b979da33d78d7b57539/Screenshot_2022-05-09_at_10.56.42_PM.png)

> ***The default behaviour of grid is like block only. But we told grid is a 2-D layout, right. So, 2-D layout contains rows and columns.***
> 

## **grid-template-columns**

- Defines the columns and rows of the grid with a space-separated list of values.

```html
<style>
      #container {
        display: grid;
        grid-template-columns: 100px 100px; // 100px represents column size
      }
    </style>
  </head>
  <body>
    <div id="container">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
      <div>6</div>
    </div>
  </body>
```

![Screenshot 2022-05-09 at 10.57.14 PM.png](CSS%20Grid%20(Basic)%20(60-70mins)%20cac801f2aded4b979da33d78d7b57539/Screenshot_2022-05-09_at_10.57.14_PM.png)

## **grid-template-rows**

- We can also specify height of each row by using `grid-template-rows` property

```html
<style>
      #container {
        display: grid;
        grid-template-columns: 100px 100px; // 100px represents column size
        grid-template-rows: 50px 50px ; // 100px represents row height 
      }
    </style>
  </head>
  <body>
    <div id="container">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
      <div>6</div>
    </div>
  </body>

Note: some styles are hidden like background color etc
```

![Screenshot 2022-05-09 at 10.59.39 PM.png](CSS%20Grid%20(Basic)%20(60-70mins)%20cac801f2aded4b979da33d78d7b57539/Screenshot_2022-05-09_at_10.59.39_PM.png)

- To get gap between each item, we can use `grid-row-gap`

```html
<style>
      #container {
        display: grid;
        grid-template-columns: 100px 100px;
        grid-template-rows: 50px 50px;
        grid-row-gap:20px
      }
    </style>
  </head>
  <body>
    <div id="container">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
      <div>6</div>
    </div>
  </body>
```

![Screenshot 2022-05-09 at 11.00.47 PM.png](CSS%20Grid%20(Basic)%20(60-70mins)%20cac801f2aded4b979da33d78d7b57539/Screenshot_2022-05-09_at_11.00.47_PM.png)

- **`grid-column-gap`**

```html
<style>
      #container {
        display: grid;
        grid-template-columns: 100px 100px;
        grid-template-rows: 50px 50px;
        grid-row-gap:20px;
        grid-column-gap:20px
      }
    </style>
  </head>
  <body>
    <div id="container">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
      <div>6</div>
    </div>
  </body>
```

![Screenshot 2022-05-09 at 11.02.52 PM.png](CSS%20Grid%20(Basic)%20(60-70mins)%20cac801f2aded4b979da33d78d7b57539/Screenshot_2022-05-09_at_11.02.52_PM.png)

- Shorthand notation for grid-gap

```html
<style>
      #container {
        display: grid;
        grid-template-columns: 100px 100px;
        grid-template-rows: 50px 50px;
        /* grid-row-gap:20px;
        grid-column-gap: 20px; */
				***/* gap : row-gap col-gap */***
        gap:20px 20px 
      }
    </style>
  </head>
  <body>
    <div id="container">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
    </div>
  </body>
```

> ***If there are 100 columns, then how will we write the size of column. Is it a good practice to write grid-template-columns: 100 100 and so on for 100 times. So, there is a CSS function called repeat for this.***
> 

## repeat():

- The **`repeat()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) [function](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Functions) represents a repeated fragment of the track list, allowing a large number of columns or rows that exhibit a recurring pattern to be written in a more compact form.
- Syntax : `repeat(no_of_times,size)`
- for eg:
    - grid-template-columns: 100px 100px can be written as `repeat(2,100px)`
- Now the above code can be changed as

```html
<style>
      #container {
        display: grid;
        grid-template-columns: repeat(2,100px);
        grid-template-rows: repeat(2,50px);
        gap:20px 20px 
      }
</style>
  </head>
  <body>
    <div id="container">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
    </div>
  </body>
```

- Now lets try to build a layout which has 2 rows and 3 columns with different backgrounds

```html
#container {
        display: grid;
        grid-template-columns: 100px 100px 100px;
        grid-template-rows: 100px 100px;
        gap:20px 20px
      }
    </style>
  </head>
  <body>
    <div id="container">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
      <div>6</div>
    </div>
  </body>
```

Output:

![Screenshot 2022-05-10 at 10.13.49 AM.png](CSS%20Grid%20(Basic)%20(60-70mins)%20cac801f2aded4b979da33d78d7b57539/Screenshot_2022-05-10_at_10.13.49_AM.png)

Live code: [Codepen](https://codepen.io/vchandu111/pen/eYyQvyr)

> ***This repeat will work only if the size of all the columns is same or size of all rows is same. What does that mean? That means grid-template-columns: 100px 100px 100px, then only it’ll work. If the  grid-template-columns: 200px 100px 50px is not there, then repeat won’t work.***
> 

## **Units of grid-template-columns:**

```html
**Pixels**
  grid-template-columns: 100px 100px or repeat(2,100px)

**Percentages**
  grid-template-columns: 50% 50% or repeat(2,50%)
  // each column will take 50% width in reference to its parent

**Fractions
	*If I want to divide 100% to 3 percentages => 33.33%, 33.33% , 33.33%
	The same output can be achieved by saying => 100 => 1fr, 1fr, 1fr 
	where fr is	fraction.***
	grid-template-columns:repeat(3,33.33%) or 1fr 1fr 1fr or repeat(3,1fr)
  // each column will take 1 fraction width in reference to its parent

```

```html
<style>
      #container {
        display: grid;
        grid-template-columns: repeat(3,1fr);
        grid-template-rows: 100px 100px;
        gap:20px 20px
      }
    </style>
  </head>
  <body>
    <div id="container">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
      <div>6</div>
    </div>
  </body>
```

**Output: Dividing each block into 3 fractions**

![Screenshot 2022-05-10 at 12.24.45 PM.png](CSS%20Grid%20(Basic)%20(60-70mins)%20cac801f2aded4b979da33d78d7b57539/Screenshot_2022-05-10_at_12.24.45_PM.png)

---

```html
<style>
      #container {
        display: grid;
        grid-template-columns: repeat(4,1fr);
        grid-template-rows: 100px 100px;
        gap:20px 20px
      }
    </style>
  </head>
  <body>
    <div id="container">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
      <div>6</div>
    </div>
  </body>
```

**Output: Dividing each block into 4 fractions**

![a.png](CSS%20Grid%20(Basic)%20(60-70mins)%20cac801f2aded4b979da33d78d7b57539/a.png)

Grid generator - [https://cssgrid-generator.netlify.app/](https://cssgrid-generator.netlify.app/)

## Exercise:

Show masai investor layout and build outer layout - only boxes not content

```css
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      #container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-template-rows: repeat(5, 400px);
        gap: 20px;
        width:80%;
        margin: 0 auto;
      }

      #container > div {
        border: 3px solid red;
      }
    </style>
  </head>
  <body>
    <div id="container">
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>
  </body>
</html>
```

> Write the below code and tell the similarity between flex and grid.
> 

```html
		<style>
      #parent {
        background-color: salmon;
        display: grid;
        justify-content: center;
        align-items: center;
        padding: 100px;
        width: 200px;
        margin: auto;
      }
      #parent > div {
        height: 200px;
        width: 200px;
        background-color: mediumaquamarine;
      }
    </style>
  </head>
  <body>
    <div id="parent">
      <div></div>
    </div>
  </body>
```

> ***What is the conclusion? The layouts which can be built using flex , can be built using grid also. And the layouts which can be built using grid can be built using grid also. But what to use to build layouts will depend on us as developers. For example, if we want to build investors layout, using grid is more advantageous than flex because we don’t even need to specify the percentage of width.***
> 

![Untitled](CSS%20Grid%20(Basic)%20(60-70mins)%20cac801f2aded4b979da33d78d7b57539/Untitled.png)

![Untitled](CSS%20Grid%20(Basic)%20(60-70mins)%20cac801f2aded4b979da33d78d7b57539/Untitled%201.png)

![Untitled](CSS%20Grid%20(Basic)%20(60-70mins)%20cac801f2aded4b979da33d78d7b57539/Untitled%202.png)

Student Activity

![Untitled](CSS%20Grid%20(Basic)%20(60-70mins)%20cac801f2aded4b979da33d78d7b57539/Untitled%203.png)

![Untitled](CSS%20Grid%20(Basic)%20(60-70mins)%20cac801f2aded4b979da33d78d7b57539/Untitled%204.png)

![Untitled](CSS%20Grid%20(Basic)%20(60-70mins)%20cac801f2aded4b979da33d78d7b57539/Untitled%205.png)

![Untitled](CSS%20Grid%20(Basic)%20(60-70mins)%20cac801f2aded4b979da33d78d7b57539/Untitled%206.png)