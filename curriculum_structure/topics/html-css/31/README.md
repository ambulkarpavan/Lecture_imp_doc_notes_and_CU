# Bootstrap (Advanced) (40mins)

[https://www.canva.com/design/DAFw7nFG6-U/_eV4jl8b9XZ04RXp69exAA/edit?utm_content=DAFw7nFG6-U&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton](https://www.canva.com/design/DAFw7nFG6-U/_eV4jl8b9XZ04RXp69exAA/edit?utm_content=DAFw7nFG6-U&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

### How to Add Bootstrap to your HTML project

1. Inside <head> tag add ⇒ “<**`link href="[https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css](https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css)" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">`**”
2. Refer the image for better understanding . 

![bootstrapInstall.png](Bootstrap%20(Advanced)%20(40mins)%206bf905a1bd964f8a94fb2689f803f973/bootstrapInstall.png)

### **Aligning elements to the right on the navbar**

In some cases you might want to align elements in a navbar to the right (for example a login or sign-up button.). To do this you'll need to use the `navbar-right` class.

```html
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Site Name</a>
    </div>
    <ul class="nav navbar-nav">
      <li class="active"><a href="#">Home</a></li>
      <li><a href="#">Page 1</a></li>
      <li><a href="#">Page 2</a></li>
      <li><a href="#">Page 3</a></li>
    </ul>
    <ul class="nav navbar-nav navbar-right">
      <li><a href="#">Action Link #1</a></li>
      <li><a href="#">Action Link #2</a></li>
    </ul>
  </div>
</nav>
```

### **Displaying the navbar independent of scrolling**

In some cases you might want to keep the navbar at the top or bottom of the screen regardless of scrolling. You will need to add either the `navbar-fixed-top` or `navbar-fixed-bottom` class to the `<nav>`element.

### **Collapsing the navbar**

On a small screen (such as a phone or tablet) the navbar is going to take up too much space. Luckily the option to collase the navbar exists. You can accomplish this using the following example.

```html
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Site Name</a>
    </div>
    <ul class="nav navbar-nav">
      <li class="active"><a href="#">Home</a></li>
      <li><a href="#">Page 1</a></li>
      <li><a href="#">Page 2</a></li>
      <li><a href="#">Page 3</a></li>
    </ul>
  </div>
</nav>
```

### **Changing the Background Color of the Navbar**

You can easily change the background color of the navbar by applying a class like **`navbar-primary`**, **`navbar-success`**, or **`navbar-danger`**. Here's an example of how to do this:

```html
<nav class="navbar navbar-dark bg-primary"> 
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href="#">Site Name</a>
        </div>
        <ul class="nav navbar-nav">
          <li class="nav-item"><a class="nav-link" href="#">Home</a></li>
          <li class="nav-item"><a class="nav-link" href="#">Page 1</a></li>
          <li class="nav-item"><a class="nav-link" href="#">Page 2</a></li>
          <li class="nav-item"><a class="nav-link" href="#">Page 3</a></li>
        </ul>
      </div>
    </nav>

```

### **Adding a Search Bar to the Navbar**

You can include a search bar in your navbar. Here's an example with an input field:

```html

<nav class="navbar navbar-expand-lg navbar-light bg-light">
          <div class="container-fluid">
            <a class="navbar-brand" href="#">Site Name</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
              <form class="d-flex">
                <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success" type="submit">Search</button>
              </form>
            </div>
          </div>
        </nav>

```

## Learning Objectives

- Aligning elements to the right on the navbar
- Displaying the navbar independent of scrolling
- Collapsing the navbar
- Changing the Background Color of the Navbar
- Adding a Search Bar to the Navbar