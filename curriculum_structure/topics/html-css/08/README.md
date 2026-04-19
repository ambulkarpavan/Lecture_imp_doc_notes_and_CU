# HTML Element and document structure (Basic) (15mins)

Why do we need HTML elements ?

> ***Even if we write normally without any tags or elements, it’ll appear on the website. Then why do we need elements? Because if we want to show an image or a button or an input form, all these features cannot be written in the html file without tags or elements. So, in order to create a structural website, we need html elements.***
> 

## HTML Elements

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

### Example Code

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

## HTML document structure

Imagine you're building a house. Like any house, there's a basic structure and blueprint you need to follow to ensure it stands firm and functions properly. In the world of the web, HTML (HyperText Markup Language) provides the blueprint for how a website should look and function.

Let's dive into this analogy:

### 1. **Doctype Declaration (`<!DOCTYPE html>`):**

- **Analogy:** Think of the Doctype as the building permit for your house. Before you start building, you need to declare what type of building it is.
- **Importance:** The Doctype tells the web browser which version of HTML the page is written in. This ensures that the browser renders the page correctly according to the rules of that HTML version.

### 2. **HTML (`<html>`):**

- **Analogy:** This is the plot of land where your house will stand. Everything you build will be within this plot.
- **Importance:** The `<html>` tag encapsulates all the content of an HTML document. It tells the browser that everything inside it is HTML content.

### 3. **Language (`lang` attribute):**

- **Analogy:** Think of the `lang` attribute as the region or country where your house is located. Just as different regions might have different building standards or styles, websites can have different languages.
- **Importance:** It's important for accessibility. Screen readers use this attribute to pronounce words correctly. It also helps search engines understand the primary language of the content.

### 4. **Head (`<head>`):**

- **Analogy:** This is like the foundation and utilities of your house: water, electricity, and gas lines. While they aren't visible or flashy, they are essential for the house to function.
- **Importance:** The `<head>` section contains meta information, links to stylesheets, scripts, and other resources that are essential for the proper presentation and behavior of the web page.

### 5. **Meta Tags (`<meta>`):**

- **Analogy:** These are the specifications and labels on your utility lines and foundation. They provide additional information about the house, like its energy efficiency or the capacity of the water heater.
- **Importance:** Meta tags provide essential information to browsers and search engines about the content and character of a page. Common meta tags include charset (character encoding), viewport (for responsive design), and description (which provides a brief overview of the site for search engines).

### 6. **Body (`<body>`):**

- **Analogy:** Now we're talking about the visible part of the house: walls, rooms, windows, and doors. This is where you live, decorate, and interact.
- **Importance:** The `<body>` tag contains everything that a user will see and interact with on the web page. This is where you put your content: text, images, videos, links, and more.

### Recap:

Building a website is like building a house. You need a permit (`<!DOCTYPE>`), a plot of land (`<html>`), a foundation (`<head>`), utilities (`<meta>` tags), and of course, the living space (`<body>`). Just as you wouldn't skip the foundation or utilities when building a house, you shouldn't skip these elements when building a website. They ensure your site is stable, functional, and accessible to everyone.

### Example Code

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <!-- your code goes here -->
</body>
</html>
```