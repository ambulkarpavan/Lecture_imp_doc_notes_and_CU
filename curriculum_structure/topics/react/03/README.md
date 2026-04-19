# JSX and Babel

Serial: 3
Made for: Beginner
Requirement: Must Have
Time in minutes: 30
Learning Objectives: Babel, JSX
doc-id: react-3

What we have learned in the previous section is how React works internally. Like creating an element using `React.createElement` method. But generally speaking you’d write code in this way in react ( Remember this code in previous Section ?? )

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Create UI With React API</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
  <script
    crossorigin
    src="https://unpkg.com/react@18/umd/react.development.js"
  ></script>
  <script
    crossorigin
    src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"
  ></script>
  <script src="https://unpkg.com/@babel/standalone@7.8.3/babel.js"></script>
  <script type="text/babel">
    const root = ReactDOM.createRoot(document.getElementById("root"));
    root.render(<p className="quote">Carpe Diem</p>);
  </script>
</html>
```

A first question that comes to your mind when you see the above code 🤨 ?

How can one write HTML code within Javascript 🤔 ? It’s a good feature to have but How does this work ?

Well the react team came up with something called `JSX` for this.  It is tiresome to use `React.createElement` for even the simplest of things and hence came this JSX. 

# JSX :

**`JSX`** stands for JavaScript XML. It's a syntax extension for JavaScript, which allows you to write HTML-like code in your JavaScript files. However, it's not exactly HTML, nor is it strictly JavaScript. It's a blend of both. This might sound confusing at first, but it's actually one of the features that makes React so powerful and popular.

Let’s see how it works :

```jsx
const element = <p>Carpe Diem</p>;
```

Step 1: So you add some JSX code here instead of `React.createElement` . But nothing works, you don’t see anything on screen except for this error

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Test</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="<https://unpkg.com/react@18.2.0/umd/react.production.min.js>"></script>
    <script src="<https://unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js>"></script>
    <script>
      const element = <p>Carpe Diem</p>; // React Element created using JSX
      const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
      reactRoot.render(element);
    </script>
  </body>
</html>
```

![Screenshot 2023-12-21 at 11.14.19 AM.png](JSX%20and%20Babel%2070332e3fc8444ac786c6b1e91e6de31a/Screenshot_2023-12-21_at_11.14.19_AM.png)

The reason behind this is your browser does not understand JSX. Browsers look at JSX like it's an alien language. So we need something to translate it into plain old JavaScript. And there’s a tool called Babel for That. 

# Babel :

Babel is the translator. It takes in JSX and spits out something ( Plain Old Javascript ) browsers understand.

- **See for Yourself**: You can play around on Babel's [Try It Out Page](https://babeljs.io/repl).

### Setting up babel in our project :

Step 1 : Babel, the compiler, can be added as CDN link. 

Step 2:  Set your script type to `text/babel`

Step 3: Write code in JSX

Step 4: See for yourself, your browser displays the same react element that you just created using JSX on DOM

Ref : [https://github.com/abduljabbarpeer/fe-react/tree/main/react-5/example-1](https://github.com/abduljabbarpeer/fe-react/tree/main/react-5/example-1)

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>react-5 | example-1</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="https://unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
    <script src="https://unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
    <!-- Step 1: Add Babel package -->
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <!-- Step 2 : Add the script type as text/babel -->
    <script type="text/babel">
			// Step 3 : Create a react element; but this time using JSX and not React.createElement() method
      const element = <div>Carpe Diem</div>; 
      // Step 4: Using Render method; display the same element created to DOM
      const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
      reactRoot.render(element);
    </script>
  </body>
</html>
```

Step 5 :  Open your browser’s devtools and check this one out on how JSX Code is converted back to Non JSX ( Plain javascript ) Code by babel. 

![Screenshot 2023-09-29 at 12.07.44 PM.png](JSX%20and%20Babel%2070332e3fc8444ac786c6b1e91e6de31a/Screenshot_2023-09-29_at_12.07.44_PM.png)

Some Caveats about using babel as CDN Links :  Don't use this in production; it's not built for that.While Babel standalone is great for quick iterations and demos, it's not suitable for production use due to its performance implications and size.The browser will warn you when using the in-browser Babel transformer.

**Quick Recap**

- **JSX makes life easier**: It makes your code cleaner and your life simpler.
- **Babel is crucial**: It's what makes JSX usable by translating it into browser-friendly JavaScript.
- **Real-world Apps**: In a production setting, you'd use build tools like Webpack to handle Babel and other tasks.

Task : Create a p element which has following text "Seize the day"; But use JSX for the same; Display the same element onto DOM;

ref : [https://github.com/abduljabbarpeer/fe-react/blob/main/react-5/example-2/index.html](https://github.com/abduljabbarpeer/fe-react/blob/main/react-5/example-2/index.html)

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>react-5 | example-2</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="https://unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
    <script src="https://unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script type="text/babel">
      // Create a p element which has following text "Seize the day"; But use JSX for the same; Display the same element onto DOM;
    </script>
  </body>
</html>
```