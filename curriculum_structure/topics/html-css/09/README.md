# HTML Tags, Attributes (Basic) (40mins)

## HTML Elements / Tags

The three main parts of the HTML elements are:

- Opening Tag : It marks the start of the element.
- Content : The content that is visible on the browser
- Closing Tag : It marks the end of the element. Usually it starts with a backward slash '/'

**Syntax :**

```html
<opening tag> Content </closing tag>
```

**Example :**

```html
<h1> Hello World! </h1>
```

![Screenshot 2022-04-04 at 1.05.48 PM.png](HTML%20Element%20and%20document%20structure%20(Basic)%20(15min%206c43462610404b62a071c7075657d29d/Screenshot_2022-04-04_at_1.05.48_PM.png)

## Let’s create a boilerplate for HTML and see what is present and why?

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  
</body>
</html>
```

In the first line, we have !DOCTYPE html. The DOCTYPE declaration is an instruction to the web browser about the version of HTML the page is written in. This ensures that the web page is parsed the same way by different web browsers, i.e, in whichever web browser you open the html page, it must look same.

There are other doctypes as well, but this is the latest HTML version. 

For eg, there is ,

**Strict doctype (HTML 4.01):** 
The HTML 4.01 strict doctype validates the written code against the HTML 4.01 spec.

The ***lang***
 attribute specifies the ***language***
 of the element's content. Common examples are "en" for English, "es" for Spanish, "fr" for French and so on.

<meta charset="*character_set*"> ⇒ Specifies the character encoding for the HTML document. The HTML5 specification encourages web developers to use the UTF-8 character set which includes all characters and almost all the symbols.

The `width=device-width`
 part sets the width of the page to follow the screen-width of the device (which will vary depending on the device).

The `initial-scale=1.0`
 part sets the initial zoom level when the page is first loaded by the browser.

Now, there are some other features that a meta tag provides which we will look into later.

## HTML Page Structure

You are one step away from building your first website in HTML. You need to add <html>, <head>, <title> and <body> tags to successfully build your website. Let's see what each tag means:

- The `<!DOCTYPE html>` declaration defines the version of HTML document, in this case it is 5
- The `<html>` element is the root element of an HTML page
- The `<head>` element contains meta information about the HTML page
- The `<title>` element specifies a title for the HTML page.
- The `<body>` element defines the document's body, and is a container for all the visible contents, such as headings, paragraphs, images, hyperlinks, tables, lists, etc.
- The `<h1>`, `<h2>` element defines a  headings.

```html
<html>
    <head>
        <title> HTML Introduction </title>
    </head>
    <body>
        <h1>Masai School</h1>
    </body>
</html>
```

**Explanation:**

- The <html> elements contains all the contents of the webpage.
- The <head> element contains additional information about the HTML page like the page title.

> ***Open masai school website and show the title name displayed and then show github also.***
> 
- The <title>element specifies a title for the webpage which is shown in the browser's window. **HTML Introduction** title will be shown on the browser's title bar.
- The <body> element contains all the contents of the webpage like the heading and the paragraph.
- The <h1> element specifies a heading

And finally your website looks like this!

![Screenshot 2022-05-02 at 2.16.52 PM.png](HTML%20Element%20and%20document%20structure%20(Basic)%20(15min%206c43462610404b62a071c7075657d29d/Screenshot_2022-05-02_at_2.16.52_PM.png)

## HTML Headings

- HTML headings are defined with the `<h1>` to `<h6>` tags.
- `<h1>` defines the most important heading. `<h6>` defines the least important heading:

# Example Code

```html
<h1>This is heading 1</h1>
<h2>This is heading 2</h2>
<h3>This is heading 3</h3>
<h4>This is heading 4</h4>
<h5>This is heading 5</h5>
<h6>This is heading 6</h6>
```

**Read more**:[https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements)

# HTML Paragraphs

HTML paragraphs are defined with the `<p>` tag:

# Example Code

```flow
<p> Welcome to Masai School.</p>
```

> ***Show the p tag in masai school website.***
> 

**Read more**:[https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p)

# Empty HTML Elements

HTML elements with no content are called empty elements.

The `<br>` tag defines a line break, and is an empty element without a closing tag:

# Example Code

```html
<p>This is a <br> paragraph with a line break.</p>
```

For instance, the horizontal ruling tag <hr> is an Empty HTML tag.

### Syntax

```html
    <hr>
```

### Attributes

- It is basically additional features, take an example of mobile and ask attributes of mobile for eg: battery, camera, ram, rom etc.
- Each and every tag in HTML will have some attributes(additional features)

![Screenshot 2022-04-05 at 2.08.03 PM.png](HTML%20Tags,%20Attributes%20(Basic)%20(40mins)%2087337868e4ee4b0d9ab44b1242294455/Screenshot_2022-04-05_at_2.08.03_PM.png)

### Anchor Tag

![Screenshot 2022-03-29 at 3.42.43 PM.png](HTML%20Tags,%20Attributes%20(Basic)%20(40mins)%2087337868e4ee4b0d9ab44b1242294455/Screenshot_2022-03-29_at_3.42.43_PM.png)

- The above example is the anchor which connects the ship to the shore
- Similarly, an anchor tag connects one website to other websites using an anchor tag - [codepen](https://codepen.io/vchandu111/pen/ZEabbop).

> ***Open masai school website and click on sign up or login button.***
> 
- The <a> tag is used to add external or internal links as content in your HTML document.
- You could also include external links to other websites in your HTML document. Here's an example that demonstrates this:

```html
    <a href="www.google.com">Visit Google</a>
```

- Above code will redirect you to [google.com](http://google.com) in same page, if you want to redirect to new blank page you should add an attribute known as target.
- target=”_blank” will open your page in new tab

```html
    <a target="_blank" href="www.google.com">Visit Google</a> 
```

## HTML Input

- So far we have found a great way of formatting whatever we want to share. This worked great for the scientific community to share their documents. But as HTML grew in popularity, it started getting used for a lot of other applications like filling online applications, online voting, etc.... . Now these applications needed user input! How do we do that?
- Take example of form which they generally fill online before joining masai.

> ***Open the below form and show them input, also show them input type password and date and submit. Later show them placeholder in below form and do the same.***
> 

![Screenshot 2022-03-29 at 8.38.15 AM.png](HTML%20Tags,%20Attributes%20(Basic)%20(40mins)%2087337868e4ee4b0d9ab44b1242294455/Screenshot_2022-03-29_at_8.38.15_AM.png)

- Different input tags

### Example Code

> ***Open input tag html mdn and show tell them to try diff input types later.***
> 

```jsx
<input type="text"/> (default value)
<input type="button"/>
<input type="checkbox"/>
<input type="color"/>
<input type="date"/>
<input type="datetime-local"/>
<input type="email"/>
<input type="file"/>
<input type="hidden"/>
<input type="image"/>
<input type="month"/>
<input type="number"/>
<input type="password"/>
<input type="radio"/>
<input type="range"/>
<input type="reset"/>
<input type="search"/>
<input type="submit"/>
<input type="tel"/>
<input type="time"/>
<input type="url"/>
<input type="week"/>
```

## HTML List Tags

> ***Open docs in google and show them bullet list and numbers list.***
> 

Lists are used quite often in websites to display a set of data or items in an ordered or unordered fashion.

HTML provides us with three types of list tags:

- Unordered List
- Ordered List

Let's learn a bit about each of these.

### Example Code

### Unordered List

```html
<ul>
<li>Hollywood</li>
<li>Bollywood</li>
<li>Tollywood</li>
</ul>
```

Output:

![Screenshot 2022-05-02 at 2.42.59 PM.png](HTML%20Tags,%20Attributes%20(Basic)%20(40mins)%2087337868e4ee4b0d9ab44b1242294455/Screenshot_2022-05-02_at_2.42.59_PM.png)

### Ordered List

```html
<ol>
<li>Hollywood</li>
<li>Bollywood</li>
<li>Tollywood</li>
</ol>
```

Output:

![Screenshot 2022-05-02 at 2.43.43 PM.png](HTML%20Tags,%20Attributes%20(Basic)%20(40mins)%2087337868e4ee4b0d9ab44b1242294455/Screenshot_2022-05-02_at_2.43.43_PM.png)

> ***Also, type for ol tag can be a or A or i or I. Show these . For ul tag, type can be disc which is default and then, square, circle and so on. Look into the documentation for more details and play around using the code.***
> 

### Example Code (nested lists)

- For `nested list` refer to this [codepen](https://codepen.io/vchandu111/pen/podjjKg)

```jsx
<ul type="none">
         <li>Hollywood
             <ul>
                 <li>Ironman</li>
                 <li>Spiderman</li>
             </ul>
         </li>
         <li>Bollywood
             <ol>
                 <li>DDLJ</li>
                 <li>Shole</li>
             </ol>
         </li>
         <li>Tollywood
             <ol>
                 <li>Pushpa</li>
                 <li>Bahubali</li>
             </ol>
         </li>
     </ul>
```

- To know more about type attribute read this [https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)

### HTML Image tag

- Have you ever wondered how to images in websites. Open masai school website and show them where images are used.

![Screenshot 2022-04-04 at 1.53.53 PM.png](HTML%20Tags,%20Attributes%20(Basic)%20(40mins)%2087337868e4ee4b0d9ab44b1242294455/Screenshot_2022-04-04_at_1.53.53_PM.png)

![html-image-tag.png](HTML%20Tags,%20Attributes%20(Basic)%20(40mins)%2087337868e4ee4b0d9ab44b1242294455/html-image-tag.png)

- The <img> tag in HTML is used to output or render images on the webpage. It specifies the source of the image using the src attribute as shown below:

```html
<img src="https://masai-website-images.s3.ap-south-1.amazonaws.com/Nrupul_d3fe3b289a.jpg" />
```

The above would render the image specified inside the src attribute:

![Screenshot 2022-05-02 at 2.48.04 PM.png](HTML%20Tags,%20Attributes%20(Basic)%20(40mins)%2087337868e4ee4b0d9ab44b1242294455/Screenshot_2022-05-02_at_2.48.04_PM.png)

> ***If the src address is wrong while copying or pasting, i.e, the img address is wrong, then the image will not come. Now, if there are 100 images and 2 or 3 images are broken, how will you know which image is broken. In order to make it easier for us, there is another attribute img tag known as alt which will get displayed if the image cannot be displayed due to any reason.***
>