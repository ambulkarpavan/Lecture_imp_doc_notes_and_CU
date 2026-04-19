# Animation (Advanced) (35-40mins)

Now before we jump into animations, we are going to discuss two important types of css properties that will help us understand how to use animations better

Those are:

- Transform
- Transition

### Transform

The transform CSS property lets you rotate, scale, skew, or translate an element. It modifies the coordinate space of the CSS visual formatting model.

```css
/* Keyword values */
transform: none;

/* Function values */
transform: rotate(0.5turn);
transform: rotateX(10deg);
transform: rotateY(10deg);
transform: translate(12px, 50%);
transform: translateX(2em);
transform: translateY(3in);
transform: scale(2, 0.5);
transform: scaleX(2);
transform: scaleY(0.5);

/* Multiple function values */
transform: translateX(10px) rotate(10deg) translateY(5px);

```

[Transform](https://developer.mozilla.org/en-US/docs/Web/CSS/transform)[Transform functions - MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function)

## **Timing Function:**

- The **`timing-function`** defines the pace of the transition.
- Common values are **`ease`**, **`linear`**, **`ease-in`**, **`ease-out`**, and **`ease-in-out`**.

```
.element {
  transition: opacity 0.5s ease-in-out;
}
```

### Transition

CSS transitions provide a way to control animation speed when changing CSS properties. Instead of having property changes take effect immediately, you can cause the changes in a property to take place over a period of time. For example, if you change the color of an element from white to black, usually the change is instantaneous. With CSS transitions enabled, changes occur at time intervals that follow an acceleration curve, all of which can be customized.

CSS transitions let you decide which properties to animate (by listing them explicitly), when the animation will start (by setting a delay), how long the transition will last (by setting a duration), and how the transition will run (by defining a timing function, e.g. linearly or quick at the beginning, slow at the end).

You can use the transition shorthand or provide individual properties as well

```css
div {
    transition: <property> <duration> <timing-function> <delay>;
}
/* another example  is */
.box {
    border-style: solid;
    border-width: 1px;
    display: block;
    width: 100px;
    height: 100px;
    background-color: #0000FF;
    transition: width 2s, height 2s, background-color 2s, transform 2s;
}

.box:hover {
    background-color: #FFCCCC;
    width: 200px;
    height: 200px;
    transform: rotate(180deg);
}

```

You can also provide the individual properties in the following manner

```css
.box{

    background-color: red;
    transition-property: transform, background;
    transition-timing-function: linear;
    transition-duration: 1s;
    transition-delay: 1s;
}

```

**Transition on Hover:**

- You can apply transitions on hover states, making it a great way to create smooth hover effects.

```
/* Example */
.element {
  transition: transform 0.3s ease-in-out;
}

.element:hover {
  transform: scale(1.2);
}
```

**Multiple Transitions:**

- You can apply transitions to multiple properties by separating them with commas.

```
/* Example */
.element {
  transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out;
}
```

Now if you wanted to create your own timing function for transition you can do that by using cubic bezier functions.

Cubic Bezier functions are a type of easing function commonly used in web development for creating smooth and natural animations. These functions are particularly popular in CSS (Cascading Style Sheets) transitions and animations.

A cubic Bezier function is defined by four control points, which determine the shape of the curve. The curve starts at the first point, goes to the second and ends at the fourth, using the third and fourth points as control handles to define the direction and curvature of the curve.

The function is usually denoted as **`cubic-bezier(P1x, P1y, P2x, P2y)`**, where:

- **`(P1x, P1y)`** are the coordinates of the first control point,
- **`(P2x, P2y)`** are the coordinates of the second control point.

The curve interpolates between the start and end points based on the position in time. In CSS animations, the time parameter typically ranges from 0 to 1, representing the start and end of the animation.

Here's a simple breakdown of how cubic Bezier functions work:

- **P0 (0, 0):** Starting point of the curve.
- **P1 (P1x, P1y):** First control point, influencing the direction of the curve at the beginning.
- **P2 (P2x, P2y):** Second control point, influencing the direction of the curve at the end.
- **P3 (1, 1):** Ending point of the curve.

The curve is calculated using the cubic Bezier formula:

Cubic Bezier functions are widely used because they offer a high degree of flexibility in defining the pacing of animations. The ease-in, ease-out, and ease-in-out timing functions commonly used in CSS are specific cases of cubic Bezier functions. They provide a way to create smooth transitions that simulate natural motion and are a powerful tool in the hands of web developers for creating engaging user interfaces.

```
.box{

    background-color: red;
    transition-property: transform, background;
    transition-timing-function: cubic-bezier(.07,.82,.78,.44);
    transition-duration: 1s;
    transition-delay: 1s;
}

```

[Cuber Bezier](https://cubic-bezier.com/)

Cubic bezier is nothing but a curve / spline that is generated between two points, P1, and P2 in the following graph

![https://developer.mozilla.org/en-US/docs/Web/CSS/easing-function/cubic-bezier-example.png](https://developer.mozilla.org/en-US/docs/Web/CSS/easing-function/cubic-bezier-example.png)

Where in `cubic-bezier(x1, y1, x2, y2)`

- x1, y1 are coordinates of the point P1
- x2, y2 are coordinates of the point P2

The spline is interpolated from this and the rate of change can be calculated. ( Who said maths was not used in UI engineering! 👀  )

[Transition](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions)

### Ok but wait. What about animation?

By now, we have understood:

- how we can transform elements
- how we can transition elements from one state to another

Well there is one more property called animation that we can use, which builds on top of the knowledge we just learnt.

### Animation

CSS animations make it possible to animate transitions from one CSS style configuration to another. Animations consist of two components, a style describing the CSS animation and a set of keyframes that indicate the start and end states of the animation’s style, as well as possible intermediate waypoints.

We saw two keywords, `animation` and `keyframes`

- animation is the property that we can use ( similar to transition, it is a shorthand )
- keyframes represent how the animation should behave, a bit similar to the cubic bezier or the timing functions we discussed earlier, but a bit more controlled
    - assuming an animation is divided into stages between 0 - 100%
    - we can define points at any time between the start and end as well, and define how the property should animate
    - if we just have two, that is the start and end, we can just use from and to

## [**animation](https://developer.mozilla.org/en-US/docs/Web/CSS/animation)[@keyframe](https://developer.mozilla.org/en-US/docs/Web/CSS/@keyframes)**

**`@keyframes` Rule:**

- Keyframes define the stages and styles of an animation.

```html
@keyframes slide {
  0% { transform: translateX(0); }
  100% { transform: translateX(100px); }
}
```

**`animation` Property:**

- The **`animation`** property is used to assign an animation to an element.
- It includes values for **`name`**, **`duration`**, **`timing-function`**, **`delay`**, **`iteration-count`**, **`direction`**, **`fill-mode`**, and **`play-state`**.
- **`animation-duration`**: Specifies the duration of the animation.
- **`animation-timing-function`**: Defines the pace of the animation.
- **`animation-delay`**: Delays the start of the animation.
- **`animation-iteration-count`**: Sets the number of times the animation should repeat.
- **`animation-direction`**: Defines whether the animation should play in reverse.
- **`animation-fill-mode`**: Specifies how the styles are applied before and after the animation.
- **`animation-play-state`**: Defines whether the animation is running or paused.

```html
@keyframes slide {
  0% { transform: translateX(0); }
  100% { transform: translateX(100px); }
}
```

**Animation Shorthand:**

- Like transitions, you can use the shorthand property **`animation`** to set all animation properties at once.

```html
.element {
  /* Transition */
  transition: opacity 0.5s ease-in-out;

  /* Animation */
  animation: slide 2s ease-in-out 1s infinite alternate;
}

@keyframes slide {
  0% { transform: translateX(0); }
  100% { transform: translateX(100px); }
}
```

There are three key advantages to CSS animations over traditional script-driven animation techniques:

- They’re easy to use for simple animations; you can create them without even having to know JavaScript.
- The animations run well, even under moderate system load. Simple animations can often perform poorly in JavaScript. - The rendering engine can use frame-skipping and other techniques to keep the performance as smooth as possible.
- Letting the browser control the animation sequence lets the browser optimise performance and efficiency by, for example, reducing the update frequency of animations running in tabs that aren't currently visible.

### How do i use it?

To create a CSS animation sequence, you style the element you want to animate with the `animation property` or its sub-properties. This lets you configure the timing, duration, and other details of how the animation sequence should progress. This does not configure the actual appearance of the animation, which is done using the `@keyframes` at-rule.

```css
p {
  animation-duration: 3s;
  animation-name: slidein;
}

@keyframes slidein {
  from {
    margin-left: 100%;
    width: 300%;
  }

  to {
    margin-left: 0%;
    width: 100%;
  }
}

```

In this example the style for the <p> element specifies that the animation should take 3 seconds to execute from start to finish, using the animation-duration property, and that the name of the @keyframes at-rule defining the keyframes for the animation sequence is named “slidein”.

```css

@keyframes identifier {
  0% { top: 0; left: 0; }
  30% { top: 50px; }
  60% { left: 50px; }
  100% { top: 100px; left: 100%; }
}

```

the keyframe selector can be either of these `from | to | %`

so similar to how you define a variable in js, we can define a @keyframe and the variables identifier is what we will use in the animation name:

[CSS Variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)

[example code gist](https://gist.github.com/albseb511/afb941bc063d7c47e46d18e356bcaa53)

### Keyframes examples

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @keyframes scaleAnimation {
            0% { transform: scale(1); }
            50% { transform: scale(1.5); }
            100% { transform: scale(1); }
        }

        .animated-element {
            margin-left: 400px;
            margin-top: 300px;
            width: 100px;
            height: 100px;
            background-color: blue; /* Set your desired background color */
            animation: scaleAnimation 3s infinite; /* Adjust the duration and other properties as needed */
        }
    </style>
</head>
<body>
    <div class="animated-element"></div>
</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    @keyframes colorChange {
      0% { background-color: red; }
      50% { background-color: blue; }
      100% { background-color: green; }
    }

    .color-changing-element {
      width: 100px;
      height: 100px;
      animation: colorChange 3s infinite; /* Adjust the duration as needed */
    }
  </style>
</head>
<body>

<div class="color-changing-element"></div>

</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <style>
      @keyframes combinedAnimation {
        0% {
          transform: scale(1);
          background-color: red;
        }
        50% {
          transform: scale(1.5);
          background-color: blue;
        }
        100% {
          transform: scale(1);
          background-color: green;
        }
      }

      .animated-element {
        margin-left: 400px;
        margin-top: 300px;
        width: 100px;
        height: 100px;
        animation: combinedAnimation 3s infinite; /* Adjust the duration and other properties as needed */
      }
    </style>
  </head>
  <body>
    <div class="animated-element"></div>
  </body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0"
    />
    <style>
      
      @keyframes combinedAnimation {
        0% {
            transform: scale(1) translateX(0) rotate(0deg);
          background-color: red;
        }
        50% {
          transform: scale(.5) translateX(475px) rotate(180deg);
          background-color: blue;
        }
        100% {
          transform: scale(1) translateX(600px) rotate(1080deg);
          background-color: green;
        }
      }

      .material-symbols-outlined {
        font-size: 200px; /* Adjust the font-size to increase or decrease the size of the heart */
        animation: combinedAnimation 3s infinite;
    }
    </style>
  </head>
  <body>
    <span class="material-symbols-outlined"> favorite </span>
  </body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    @keyframes fadeIn {
      0% { opacity: 0; }
      100% { opacity: 1; }
    }

    .fade-in-element {
      animation: fadeIn 2s ease-in-out; /* Adjust the duration and timing function as needed */
    }
  </style>
  <title>Fade In Animation</title>
</head>
<body>

  <div class="fade-in-element">
    <!-- Your content goes here -->
    <h1>Hello, this is a fade-in element!</h1>
    <p>This content will fade in using the defined keyframes animation.</p>
  </div>

</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    @keyframes bounce {
      0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
      40% { transform: translateY(-300px); }
      60% { transform: translateY(-150px); }
    }

    .animated-element {
      width: 100px;
      height: 100px;
      margin-top: 30%;
      background-color: #3498db;
      border-radius: 50%;
      animation: bounce 2s infinite; /* Adjust the duration and iteration count as needed */
    }
  </style>
</head>
<body>

<div class="animated-element"></div>

</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    @keyframes bounce {
      0% { transform: translateY(0) translateX(0);}
      20%, 50%, 80%, 100% { transform: translateY(0)}
      40% { transform: translateY(-300px) translateX(300px); }
      60% { transform: translateY(-150px) translateX(500px); }
    }

    .animated-element {
      width: 100px;
      height: 100px;
      margin-top: 30%;
      background-color: #3498db;
      border-radius: 50%;
      animation: bounce 2s infinite; /* Adjust the duration and iteration count as needed */
    }
  </style>
</head>
<body>

<div class="animated-element"></div>

</body>
</html>
```