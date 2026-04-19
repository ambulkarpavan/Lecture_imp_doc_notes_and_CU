# HTML special tags (Advanced) (20-25mins)

```html
<!-- HTML DOCUMENT -->

<!DOCTYPE html> <!-- they don't do much, just tells the web browser that this document is written in HTML5 -->
<html lang="en"> <!-- root element and also specifies that the document is written in English ("en") -->
<head> <!---the stuff you want to include on the HTML page that isn't the content you are showing to your page's viewers.
    contains meta-information about the document, such as character encoding and the document's title -->
    <meta charset="UTF-8"> <!-- character encoding which includes most characters from the vast majority of written languages -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- This meta tag is often used for responsive web design. It sets 
        the viewport's width to the device's width and sets the initial zoom level to 1.0. Ensures the page renders at the width of viewport, preventing mobile 
        browsers from rendering pages wider than the viewport and then shrinking them down. -->
    <title>My App</title> <!-- title of the web page, which is displayed in the browser's title bar or tab. -->
    </head>
<body>
    <!-- It contains the actual content of the web page, such as text, images, links, and other elements. 
    Anything inside the <body> element is what users see when they visit your web page. -->
</body>
</html>
```

# Meta tags

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="John Doe">
    <meta name="description" content="This is a sample web page about HTML meta tags.">
    <meta name="keywords" content="HTML, meta tags, web development">
    <meta name="viewport" content="width=100">
    <!-- <meta http-equiv="refresh" content="5;url=http://127.0.0.1:5500/2index.html"> -->
    <title>Document</title>
</head>
<body>
    <!-- <h1>asdgfjhgkvucijtdcfvfuubgyuvruycruykryilvyitryvicrtukghdghdffgkgjfk</h1> -->
</body>
</html>
```

# Semantic Tags

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Semantic tags</title>
    <!---Semantic tags in HTML are elements that convey meaning about the structure and content of a web page to both the browser and the developer.-->
</head>
<body>
    <header> <!--- Represents the header of a section or the entire page. It typically contains site branding, navigation menus, and other introductory content. --->
        <h1>Welcome to My Web Page</h1>
        <nav> <!---Defines a navigation menu, such as a site menu or a table of contents for a page-->
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Services</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main> <!---Represents the main content of the document. There should be only one <main> element per page-->
        <section> <!---Represents a thematic grouping of content within a page. It helps to organize content into meaningful sections.-->
            <h2>About Us</h2>
            <p>Welcome to our website! We are a team of passionate individuals dedicated to providing you with valuable information.</p>
        </section>

        <section>
            <h2>Services</h2>
            <ul>
                <li><strong>Web Design:</strong> We create beautiful and functional websites.</li>
                <li><strong>Graphic Design:</strong> Our designs will <mark>make your brand stand out.</mark></li>
                <li><strong>SEO:</strong> We optimize your website for search engines.</li>
            <!---<strong> is used to emphasize text.-->
            <!--  Represents text that has been highlighted or marked for reference, often with a yellow background. -->
            </ul>
        </section>

        <section>
            <h2>Contact Us</h2>
            <address> <!---<address> is used to define contact information.-->
                <p>Email: <a href="mailto:contact@example.com">contact@example.com</a></p>
                <p>Phone: <a href="tel:+123456789">+1 (234) 567-89</a></p>
            </address>
        </section>
    </main>

    <footer> <!---It typically contains copyright information, contact details, and other closing content.-->
        <p>&copy; 2023 My Web Page</p>
    </footer>
</body>
</html>

<!-- article:  It can be used for blog posts, news articles, forum posts, and other similar content. -->
```

# Image and Figcaption

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=\, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <img
      src="https://images.unsplash.com/photo-1612441804231-77a36b284856?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8bW91bnRhaW4lMjBsYW5kc2NhcGV8ZW58MHx8MHx8fDA%3D&w=1000&q=80"
      alt="A beautiful landscape"
      title="Landscape"
    />

    <!-- Use the <img> tag when you have a standalone image that doesn't require additional context or explanation -->
    <br /><br /><br />
    <hr />
    <br /><br />
    <figure>
      <img
        src="https://i0.wp.com/techqualitypedia.com/wp-content/uploads/2022/03/PFC-detailed.png?resize=1024%2C747&ssl=1"
        alt="A diagram illustrating the process"
      />
      <figcaption>Figure 1: Process Flow Diagram</figcaption>
    </figure>
    <!-- useful when the image needs context or when you want to provide additional information about the image. -->
    <br /><br /><br />
    <hr />
    <br /><br />
    <p>
      The <abbr title="World Health Organization">WHO</abbr> is an important
      organization in the field of global health.
    </p>
  </body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <details>
        <summary>Click to expand/collapse</summary>
        <p>This is the hidden content that can be toggled.</p>
        <p>This is the hidden content that can be toggled.</p>
        <p>This is the hidden content that can be toggled.</p>
        <p>This is the hidden content that can be toggled.</p>
        <p>This is the hidden content that can be toggled.</p>
    </details>  
    
    <p>This is some regular text in a paragraph.</p>

    <blockquote>
        <p>This is a blockquote. It represents a quotation from another source. Blockquotes are often styled differently from regular text to make them stand out.</p>
        <footer>- John Doe</footer>
    </blockquote>

    <p>Back to regular text after the blockquote.</p>

    <p>Here is a short inline quotation: <q>This is a quote within the text.</q></p>

    <p>You can also use <code>&lt;code&gt;</code> to display HTML tags in your text.</p>

    <pre>
        <code>
            function greet(name) {
                console.log('Hello, ' + name + '!');
            }
            greet('Alice');
        </code>
    </pre>

    <p>The formula for calculating the area of a circle is <var>A = πr<sup>2</sup></var>, where <var>r</var> is the radius.</p>

    <p>Here is the output of a computer program enclosed in the <samp> element: <samp>Hello, world!</samp></p>

    <pre>
        <samp>
            $ echo "This is a sample command."
            This is a sample command.
        </samp>
    </pre>

    <p>This text is in <small>smaller font size</small> using the &lt;small&gt; element.</p>

    <p>On April 1st, 2022, we <del>increased</del> <ins>reduced</ins> our prices.</p>

    <pre>
        This is preformatted text.
        It preserves spaces and line                        breaks exactly as they are typed.
        You can use it for displaying code or other text that needs precise formatting.
    </pre>
</body>
</html>
```

# Video, maps and pdf

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            display: flex;
            flex-direction: column;
        }
    </style>
</head>
<body>
    <video width="640" height="360" controls>
        <source src="q1q2.mp4" type="video/mp4">
        <!-- <source src="sample.webm" type="video/webm">
        Your browser does not support the video tag. -->
    </video>

    <!-- The <embed> element is used to embed multimedia content like audio or video directly into a webpage. -->
    <embed src="q1q2.mp4" width="300" height="400" autostart="false" />

    <embed src="Radical.pdf" width="500" height="800"/>

    <!-- The <iframe> element is used to embed external web content, such as web pages or videos, within a webpage. -->
    <iframe width="560" height="315" src="https://www.youtube.com/embed/305YfKMyqVw?si=rSuCDOR3am6_D3fm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d62217.09202527259!2d77.5909926235628!3d12.93544771824801!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae144ed898fc2d%3A0x1681f38e8c00ae56!2sKoramangala%2C%20Bengaluru%2C%20Karnataka!5e0!3m2!1sen!2sin!4v1694689530423!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>    
</body>
</html>
```

# Responsiveness using HTML

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <picture>
        <source media="(max-width: 799px)" srcset="3-b-image.png" />
        <source media="(min-width: 800px)" srcset="3-a-image.png" />
        <img src="3-a-image.png" alt="Chris standing up holding his daughter Elva" />
      </picture>
      
  </body>
</html>
```

# All the input tags

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<input type="text"/> (default value)
<input type="button" name="button" placeholder="button"/>
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
</body>
</html>
```

# Lists

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h2>Unordered List (Numbered)</h2>
    <ul>
        <li>Apple</li>
        <li>Orange</li>
        <li>Banana</li>
        <li>Mango</li>
    </ul>

    <h2>Ordered List (Numbered)</h2>

    <ol>
      <li>First, wash the fruits.</li>
      <li>Peel the skin if necessary.</li>
      <li>Slice the fruits into bite-sized pieces.</li>
      <li>Enjoy your healthy snack!</li>
    </ol>

    <ol type="a">
      <li>Item A</li>
      <li>Item B</li>
      <li>Item C</li>
    </ol>

    <ol type="A">
      <li>Item A</li>
      <li>Item B</li>
      <li>Item C</li>
    </ol>
    <ol type="i">
      <li>Item i</li>
      <li>Item ii</li>
      <li>Item iii</li>
    </ol>
    <ol type="I">
      <li>Item I</li>
      <li>Item II</li>
      <li>Item III</li>
    </ol>
    <ol start="10">
      <li>Item 10</li>
      <li>Item 11</li>
      <li>Item 12</li>
    </ol>
  </body>
</html>
```