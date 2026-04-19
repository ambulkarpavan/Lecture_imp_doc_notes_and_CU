# CSS Combinators (Basic) (40-45mins)

## **CSS Combinators:**

- The CSS combinators represent the relationship between two selectors.
- The CSS selectors are the patterns that can be used for styling the particular HTML element. Sometimes, it is possible that there is more than one simple selector, and to combine the multiple simple selectors, we use the combinators.

## **Why use CSS Combinator❓**

- Learning about combinators makes you **better at writing CSS** and **helps you to avoid excess CSS code.**
- Combinators can also help you **pinpoint the section** or **part of HTML** you want to style with high accuracy because they are based on the **relationship between the selectors.**

> ***Open yesterday’s investors code and say, if suppose there are 100 boxes inside our parent, then we have to copy paste the class box 100 times,right? Is it possible to do it without any mistake? Is it feasible? So, in cases like these, we can use combinators to manage the styles of tags from the parent id. Then, we are just using one id and applying all the styles.***
> 

## How many of you know Amitabh Bachchan? So, you all know Big B, right? We will see the types of Combinators with Bachchan Family analogy.

## **Types of Combinators in CSS**

The combinators are of 4 types, which are given below:

1. `Descendant selector ( ) (space)`
2. `Child selector (>)`
3. `General sibling selector (~)`
4. `Adjacent sibling selector (+)`

## **Descendant Selector in CSS**

- **Descendant Meaning:** A person who is related to you and who lives after you, such as your child or grandchild

### Practical example:

![amb.jpeg](CSS%20Combinators%20(Basic)%20(40-45mins)%2040ab578b46704f178c77161f73a566ea/amb.jpeg)

- Look at Amitabh's family tree
    - Number of Descendants for Harivansh Rai Bachan - 15
    - Number of Descendants for Amitabh Bachan - 7
    - Number of Descendants for Abhishek Bachan - 1 (Aaradhya)
    - Number of Descendants for Sweta Nanda - 2
    
    Now, we will see this in code.
    
    - `Syntax`
    
    ```html
    selector1 selector2 selector3... {
    	// style properties
    }
    ```
    
    - Min 2 , can be greater than 2

![Screenshot 2022-05-09 at 11.12.55 AM.png](CSS%20Combinators%20(Basic)%20(40-45mins)%2040ab578b46704f178c77161f73a566ea/Screenshot_2022-05-09_at_11.12.55_AM.png)

```jsx
<!DOCTYPE html>
<html>
<head>
<style>
div p {
    /* It will select all p's which are descendants of div */
    background-color: teal;
}
</style>
</head>
<body>
<div>
  <p>Paragraph 1 in the div.</p>
  <p>Paragraph 2 in the div.</p>
  <span><p>Paragraph 3 in the div.</p></span>
</div>
<p>Paragraph 4. Not in a div, not a descendant</p>
<p>Paragraph 5. Not in a div, not a descendant</p>

</body>
</html>
```

![1.png](CSS%20Combinators%20(Basic)%20(40-45mins)%2040ab578b46704f178c77161f73a566ea/1.png)

- In the above figure div, p will select all p’s which are descendants of div

## **Child Selector**

- The child selector uses the greater than sign `(>)` to separate the elements. The child selector is used when we want to apply the styling properties to the immediate child/children of the particular HTML element.
- This combinator is quite strict than the descendant selector and the styling properties are acquired only when the second selector is the direct child of the first one.

![amb.jpeg](CSS%20Combinators%20(Basic)%20(40-45mins)%2040ab578b46704f178c77161f73a566ea/amb%201.jpeg)

- Look at Amitabh's family tree
    - Number of Childs for Harivansh Rai Bachan - 2
    - Number of Childs for Amitabh Bachan - 2
    - Number of Childs for Abhishek Bachan - 1 (Aaradhya)
    - Number of Childs for Sweta Nanda - 2
    

![Screenshot 2022-05-09 at 11.23.34 AM.png](CSS%20Combinators%20(Basic)%20(40-45mins)%2040ab578b46704f178c77161f73a566ea/Screenshot_2022-05-09_at_11.23.34_AM.png)

```jsx
<!DOCTYPE html>
<html>
<head>
<style>
div > p {
      /* Selects all p's which are child of div */
    background-color: teal;
}
</style>
</head>
<body>

<div>
  <p>Paragraph 1 in the div.</p>
  <p>Paragraph 2 in the div.</p>
  <span><p>Paragraph 3 in the div, but it is not child of div, it is child of span</p></span> 
</div>

<p>Paragraph 4. Not in a div, not child of div</p>
<p>Paragraph 5. Not in a div, not child of div</p>

</body>
</html>
```

![2.png](CSS%20Combinators%20(Basic)%20(40-45mins)%2040ab578b46704f178c77161f73a566ea/2.png)

- In the above figure `div>p` will select all p’s which are `childs` of div

## **General Sibling Selector:**

- **Sibling meaning:** A brother or sister from the same parent
- The general sibling selector is used when the user wants to set the CSS properties for the elements that are the siblings of each other even if they are not the immediate ones.
- This selector is used when we have to set the styling properties of the elements that have the same parent element. This selector can be separated by adding the (~) sign between them.

![amb.jpeg](CSS%20Combinators%20(Basic)%20(40-45mins)%2040ab578b46704f178c77161f73a566ea/amb%202.jpeg)

- Look at Amitabh's family tree
    - Number of general siblings for Amitabh Bachan - 1 (Ajitabh Bachan)
    - Number of general siblings for Abhishek Bachan - 1 (Sweta Nanda)
    - Number of general siblings for Bhim Bachan - 1
    - Number of general siblings for Aaradhy - 0
    
    Remember that siblings will be of the same generation
    

![Screenshot 2022-05-09 at 11.39.42 AM.png](CSS%20Combinators%20(Basic)%20(40-45mins)%2040ab578b46704f178c77161f73a566ea/Screenshot_2022-05-09_at_11.39.42_AM.png)

```jsx
<!DOCTYPE html>
<html>
  <head>
    <style>
      h3 ~ p {
            /* selects all p's which are general siblings of h3 */
          background-color: yellow;
      }
    </style>
  </head>
  <body>
    <h3>I am heading 3</h3>
    <p>Paragraph 3, general sibling of h3</p>
    <p>Paragraph 4, general sibling of h3</p>
    <p>Paragraph 5, general sibling of h3</p>
    <p>Paragraph 6, general sibling of h3</p>
    <p>Paragraph 7, general sibling of h3</p>
  </body>
</html>
```

![3.png](CSS%20Combinators%20(Basic)%20(40-45mins)%2040ab578b46704f178c77161f73a566ea/3.png)

- In the above figure `h1 ~ p` will select all p’s which are siblings of h1

## **Adjacent / Immediate sibling Selector in CSS**

- The adjacent sibling selector is used when we want to apply the CSS property or styling to the adjacent sibling of any element.
- The siblings should have the same parent element and also the second element must be the immediate follower of the first element.
- The selectors are separated by adding the (+) sign between the separators.

![amb.jpeg](CSS%20Combinators%20(Basic)%20(40-45mins)%2040ab578b46704f178c77161f73a566ea/amb%203.jpeg)

- Look at Amitabh's family tree
    - Number of immediate siblings for Amitabh Bachan - 1 (Ajitabh Bachan)
    - Number of immediate siblings for Abhishek Bachan - 1 (Sweta Nanda)
    - Number of immediate siblings for Bhim Bachan - 1 (Namrata Bachan)
    - Number of immediate siblings for Navya Naveli - 1
    
    Remember that siblings will be of the same generation
    
    ![Screenshot 2022-05-09 at 5.09.39 PM.png](CSS%20Combinators%20(Basic)%20(40-45mins)%2040ab578b46704f178c77161f73a566ea/Screenshot_2022-05-09_at_5.09.39_PM.png)
    
    ## Exercises:
    
    - Copy these code snippets and ask students the output (no need to code just copy paste it)
    
    ```jsx
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Document</title>
        <style>
          div > p {
            background-color: red;
          }
        </style>
      </head>
      <body>
        <div>
          <p>p1</p>
          <p>p2</p>
          <p>p3</p>
          <span>
            <p>p3</p>
          </span>
        </div>
    
        <p>P4</p>
        <p>P5</p>
      </body>
    </html>
    
    --------------------------------------------------
    
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Document</title>
        <style>
          div  p {
            background-color: red;
          }
        </style>
      </head>
      <body>
        <div>
          <p>p1</p>
          <p>p2</p>
          <p>p3</p>
          <span>
            <p>p3</p>
          </span>
        </div>
    
        <p>P4</p>
        <p>P5</p>
      </body>
    </html>
    
    ```
    
    ```jsx
    <!DOCTYPE html>
    <html lang="en">
    <head>
      
      <title>Document</title>
      <style>
        div+p{
          background-color: red
        }
      </style>
    </head>
    <body>
      <div>
        <p>p1</p>
        <p>p2</p>
        <p>p3</p>
      </div>
    
      <p>P4</p>
      <p>P5</p>
    </body>
    </html>
    ```
    
    ```jsx
    <!DOCTYPE html>
    <html lang="en">
    <head>
      
      <title>Document</title>
      <style>
        div~p{
          background-color: red
        }
      </style>
    </head>
    <body>
      <div>
        <p>p1</p>
        <p>p2</p>
        <p>p3</p>
      </div>
    
      <p>P4</p>
      <p>P5</p>
    </body>
    </html>
    ```
    
    ```jsx
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Document</title>
        <style>
          #para ~ p{
            background-color: red
          }
        </style>
      </head>
      <body>
      <p id="para">p1</p>
      <p>p2</p>
      <p>p3</p>
      <p>p4</p>
      <p>p5</p>
      </body>
    </html>
    
    -----------------------------------
    
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Document</title>
        <style>
          #para + p{
            background-color: red
          }
        </style>
      </head>
      <body>
      <p id="para">p1</p>
      <p>p2</p>
      <p>p3</p>
      <p>p4</p>
      <p>p5</p>
      </body>
    </html>
    ```
    
    > ***Let’s rewrite the investors layout we created yesterday with combinators.***
    > 
    

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Box Model</title>
    <style>
      #parent > div {
        height: auto;
        width: 20%;
        margin: auto;
      }
      h1 {
        text-align: center;
      }
      #parent {
        display: flex;
        margin: auto;
      }
      h2 {
        text-align: center;
      }

      p {
        text-align: center;
      }
      #parent > div > img {
        width: 100%;
				border-radius: 15px 15px 0px 0px;
        /* top-left top-right  bottom-right bottom-left*/
      }
      #parent > div > p + img {
        width: 140px;
        margin: auto;
        display: block;
      }
    </style>
  </head>
  <body>
    <h1>Strategic Investors</h1>
    <div id="parent">
      <div>
        <img
          src="https://masai-website-images.s3.ap-south-1.amazonaws.com/Vijay_Shekhar_Sharma_Paytm_96f52579b8.jpg"
          alt="Vijay"
        />
        <h2>Vijay Shekhar Sharma</h2>
        <p>Founder & CEO</p>
        <img
          src="https://masai-website-images.s3.ap-south-1.amazonaws.com/paytm_rect_06df45a24f.svg"
          alt="logo"
        />
      </div>
      <div>
        <img
          src="https://masai-website-images.s3.ap-south-1.amazonaws.com/Vijay_Shekhar_Sharma_Paytm_96f52579b8.jpg"
          alt="Vijay"
        />
        <h2>Vijay Shekhar Sharma</h2>
        <p>Founder & CEO</p>
        <img
          src="https://masai-website-images.s3.ap-south-1.amazonaws.com/paytm_rect_06df45a24f.svg"
          alt="logo"
        />
      </div>
      <div>
        <img
          src="https://masai-website-images.s3.ap-south-1.amazonaws.com/Vijay_Shekhar_Sharma_Paytm_96f52579b8.jpg"
          alt="Vijay"
        />
        <h2>Vijay Shekhar Sharma</h2>
        <p>Founder & CEO</p>
        <img
          src="https://masai-website-images.s3.ap-south-1.amazonaws.com/paytm_rect_06df45a24f.svg"
          alt="logo"
        />
      </div>
      <div>
        <img
          src="https://masai-website-images.s3.ap-south-1.amazonaws.com/Vijay_Shekhar_Sharma_Paytm_96f52579b8.jpg"
          alt="Vijay"
        />
        <h2>Vijay Shekhar Sharma</h2>
        <p>Founder & CEO</p>
        <img
          src="https://masai-website-images.s3.ap-south-1.amazonaws.com/paytm_rect_06df45a24f.svg"
          alt="logo"
        />
      </div>
    </div>
  </body>
</html>

```

# Inheritance of Properties

```jsx
<html>
  <head>
    <title>Box model</title>
    <style>
**Write each property and ask if it is inheriting or not**
     div {
			font-size:80px;
			color:red;
			text-align:center;
			background-color:green;
			text-decoration:underline;
			border:2px solid crimson; ===> **applies only to the div whereas 
the above properties apply to all the elements inside div**		
			margin-top: 40px;		
		}
    </style>
  </head>
  <body>
    <div>
	      <h1>I am heading 1</h1>
				<p>I am para</p>
				<h2>I am heading 2</h2>
    </div>
  </body>
</html>
```

# Why do we need to study inheritance?

> ***Now that we are visualising everything in our websites as a box model, we will try to create a boc using div and keep our tags like img, heading inside that div, right? So, if the properties are being inherited, then we can set properties for parent div and the elements inside div will also inherit those properties, so we don’t need to write extra css or classes or selectors right?***
> 

## Overview of all selectors:

![Screenshot 2022-05-09 at 4.09.34 PM.png](CSS%20Combinators%20(Basic)%20(40-45mins)%2040ab578b46704f178c77161f73a566ea/Screenshot_2022-05-09_at_4.09.34_PM.png)

## More Selectors:

**CSS *element, element* Selector**

Select and style all <h2> elements AND all <p> elements:

```html
<!DOCTYPE html>
<html>
<head>
<style>
h2, p {
  background-color: yellow;
}
</style>
</head>
<body>

<h1>Demo of the element, element selector</h1>

<h2>Welcome to My Homepage</h2>

<div>
  <p>My name is Donald.</p>
  <p>I live in Duckburg.</p>
</div>

<p>My best friend is Mickey.</p>

</body>
</html>
```

## **CSS Attribute Selectors**

- The `[attribute]` selector is used to select elements with a specified attribute.

![Screenshot 2022-05-09 at 11.58.42 AM.png](CSS%20Combinators%20(Basic)%20(40-45mins)%2040ab578b46704f178c77161f73a566ea/Screenshot_2022-05-09_at_11.58.42_AM.png)

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>

    <style>
      a[href="https://www.masaischool.com/"]
      {
        color: red;
      }

      a[target="_self"] {
        font-size: 40px;
      }
			input[type="text"] {
				background-color:crimson;
				color: white;
			}
    </style>
  </head>
  <body>
    <a href="https://www.masaischool.com/" target="_blank">Masai school</a>
    <a target="_self"
      href="https://sso.masaischool.com/signin/?returnTo=https://dashboard.masaischool.com/#/"
      >Onwards</a
    >
    <input type="text" placeholder="Enter name"/>
    <input type="number" placeholder="Enter mobile"/>
  </body>
</html>
```

## **Types of attribute selector**

![7196.1589957400.png](CSS%20Combinators%20(Basic)%20(40-45mins)%2040ab578b46704f178c77161f73a566ea/7196.1589957400.png)

**Read more : [Link](https://www.w3schools.com/css/css_attribute_selectors.asp)**

`Game - [https://flukeout.github.io/](https://flukeout.github.io/)`

`Solution - [https://andersjensen.org/solutions-to-css-diner/](https://andersjensen.org/solutions-to-css-diner/)`

## Assignment que to be solved:

Link : [https://course.masaischool.com/problems/26835](https://course.masaischool.com/problems/26835)

Solution

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>U2C1</title>
    <style>
      h1 {
        text-align: center;
        font-size: 60px;
        color: #c78b36;
      }
      .des {
        text-align: center;
        width: 40%;
        margin: auto;
        line-height: 25px;
        font-size: 18px;
        margin-top: -15px;
      }

			#container {
        width: 80%;
        margin: auto;
        margin-top: 50px;
				border: 1px solid red;
        display: flex;
        text-align: center;
      }

      #container > div {
				border: 1px solid red;
        width: 30%;
        margin: auto;
        /* height:400px initially */
      }

      #container > div > img {
        width: 100%;
      }
    </style>
  </head>
  <body>
    <!-- Heading section -->
    <h1>Rooms & Suits</h1>
    <!-- Don't change class and Id names -->
    <p class="des">
      Far far away, behind the word mountains, far from the countries Vokalia
      and Consonantia, there live the blind texts. Separated they live in
      Bookmarksgrove right at the coast of the Semantics, a large language
      ocean.
    </p>
    <!-- cards section -->
    <!-- Don't change class and Id names -->

    <div id="container">
      <div>
        <img
          src="https://preview.colorlib.com/theme/sogo/images/ximg_1.jpg.pagespeed.ic.sI14MfHd8f.webp"
          alt=""
        />
        <h2>Single Room</h2>
        <p>90$ / Per Night</p>
      </div>
      <div>
        <img
          src="https://preview.colorlib.com/theme/sogo/images/ximg_1.jpg.pagespeed.ic.sI14MfHd8f.webp"
          alt=""
        />
        <h2>Single Room</h2>
        <p>90$ / Per Night</p>
      </div>
      <div>
        <img
          src="https://preview.colorlib.com/theme/sogo/images/ximg_1.jpg.pagespeed.ic.sI14MfHd8f.webp"
          alt=""
        />
        <h2>Single Room</h2>
        <p>90$ / Per Night</p>
      </div>
    </div>
  </body>
</html>
```