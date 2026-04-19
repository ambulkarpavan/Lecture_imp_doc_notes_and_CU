# Media Queries (Basic) (20-25mins)

# Introduction:

- Media queries are what make modern responsive design possible. With them you can set different styling based on things like a users screen size, device capabilities or user preferences.

## **What are media queries?**

- What is a media query? A media query is a specific feature of CSS that lets you conditionally apply styling based on a media type, a media feature or both.
- You use them primarily to check the screen dimensions and apply CSS based on that, but media queries can do many other powerful things.

![EOA_MediaQueries2019_Blog.jpeg](Media%20Queries%20(Basic)%20(20-25mins)%209ec04e8d801c41a69ca939872d77a0f3/EOA_MediaQueries2019_Blog.jpeg)

- A media query is an expression that evaluates to either True or False.
- A media query consists of a test, followed by as many CSS rules as we want, with the rule block enclosed in a set of braces. If the test condition is false, the browser simply ignores the rule block and moves on.

## Syntax of  **Media Query**

![media-query-anatomy.webp](Media%20Queries%20(Basic)%20(20-25mins)%209ec04e8d801c41a69ca939872d77a0f3/media-query-anatomy.webp)

- `@media` specifies media queries declaration.
- `Media type` specifies what type of media are we trying to target, In many  cases, you’ll see a `screen`value used here, which makes sense since many of the media types we’re trying to match are devices with screens attached to them. It also includes
    - `all`: Matches all devices
    - `print`: Matches documents that are viewed in a print preview or any media that breaks the content up into pages intended to print.
    - `screen`: Matches devices with a screen
- `Media Feature` defines what features we are trying to match it to.
    - Desktop: (`min-width:1024px`)
    - Tablet: `(min-width:768px)` and `(max-width:1023px)`
    - Smartphone :`(min-width:340px)` and `(max-width:767px)`

![Screenshot 2022-05-11 at 11.42.27 AM.png](Media%20Queries%20(Basic)%20(20-25mins)%209ec04e8d801c41a69ca939872d77a0f3/Screenshot_2022-05-11_at_11.42.27_AM.png)

![code.png](Media%20Queries%20(Basic)%20(20-25mins)%209ec04e8d801c41a69ca939872d77a0f3/code.png)

- Let’s see how media query works by taking small example.
- In this example, we are just giving background color property to body, by default whatever we write is for large screens.

```html
<html>
  <head>
    <title>Document</title>
    <style>
      body {
        background-color: teal;
      }
    </style>
  </head>
  <body></body>
</html>
```

- **`Medium Screens`**

```html
<html>
  <head>
    <title>Document</title>
    <style>
      body {
        background-color: teal;
      }
@media all and (min-width: 768px) and (max-width: 1024px) {
        body {
          background-color: pink;
        }
      }
    </style>
  </head>
  <body></body>
</html>
```

- **`Large Screens:`**

```jsx
<html>
  <head>
    <title>Document</title>
    <style>
      body {
        background-color: teal;
      }
			/* meidum screens */
			@media all and (min-width: 651px) and (max-width: 1024px) {
        body {
          background-color: pink;
        }
      }

			/* small screens */
      @media all and (min-width: 320px) and (max-width: 650px) {
        body {
          background-color: crimson;
        }
      }

    </style>
  </head>
  <body></body>
</html>
```