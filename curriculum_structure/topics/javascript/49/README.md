# Infinite scrolling [60 min] (1)

Difference between `offsetHeight`, `clientHeight` and `scrollHeight`

**scrollHeight**: The `scrollHeight` value is equal to the minimum height the element would require in order to fit all the content in the viewport without using a vertical scrollbar.

`ENTIRE content & padding (visible or not)`

![https://miro.medium.com/v2/resize:fit:399/1*IjO5mKXNyTO5moRHlj4m1A.png](https://miro.medium.com/v2/resize:fit:399/1*IjO5mKXNyTO5moRHlj4m1A.png)

**clientHeight**: it includes the element’s padding, but not its border, margin or horizontal scrollbar (if present). It can also include the height of pseudo-elements such as `[::before](https://developer.mozilla.org/en-US/docs/Web/CSS/::before)` or `[::after](https://developer.mozilla.org/en-US/docs/Web/CSS/::after)`. If the element's content can fit without a need for vertical scrollbar, its `scrollHeight` is equal to`[clientHeight](https://developer.mozilla.org/en-US/docs/Web/API/Element/clientHeight). VISIBLE content & padding`

![https://miro.medium.com/v2/resize:fit:503/1*L-QquYrgfWfNNB8YP3K2eA.png](https://miro.medium.com/v2/resize:fit:503/1*L-QquYrgfWfNNB8YP3K2eA.png)

**offsetHeight**: is a measurement in pixels of the element’s CSS height, including border, padding and the element’s horizontal scrollbar (if present, if rendered). It does not include the height of pseudo-elements such as `[::before](https://developer.mozilla.org/en-US/docs/Web/CSS/::before)` or `[::after](https://developer.mozilla.org/en-US/docs/Web/CSS/::after)`.

The following equivalence returns `true` if an element is at the end of its scroll, `false` if it isn't.

```
**element.scrollHeight - element.scrollTop === element.clientHeight**
```

### **scrollHeight**: `ENTIRE  content & padding (visible or not)`

Height of all content + paddings, despite of height of the element.

### **clientHeight**: `VISIBLE content & padding`

Only visible height: content portion limited by explicitly defined height of the element.

### **offsetHeight**: `VISIBLE content & padding` `+ border + scrollbar`

Height occupied by the element on document.

Class Code : [A Pen by Adarsha khatua (codepen.io)](https://codepen.io/Adarsha-khatua/pen/ExOQjKe?editors=0010);

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            height: 500px;
        }
        #container{
            display: flex;
            flex-wrap: wrap;
        }
        .card {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 200px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin: 10px;
}

.card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 8px;
}

.card h2 {
  margin-top: 10px;
  font-size: 16px;
  font-weight: bold;
  text-align: center;
}

    </style>
</head>
<body>
    <div id="container">

    </div>
</body>
</html>
<script src="index.js"></script>
```

```jsx
//offsetHeight  
//clientHeight
//scrollHeight
//scrollTop

let container = document.getElementById("container");
// console.log(container.offsetHeight);
// console.log("clientHeight",container.clientHeight);
// console.log("scrollHeight",container.scrollHeight);
// let clientHeight = document.documentElement.clientHeight;
// let scrollHeight = document.documentElement.scrollHeight;
//let scrollTop = document.documentElement.scrollTop;

console.log(clientHeight,scrollHeight);

let page = 1;
fetchData()

window.addEventListener("scroll",()=>{
    
    let clientHeight = document.documentElement.clientHeight;
    let scrollHeight = document.documentElement.scrollHeight;
    let scrollTop = document.documentElement.scrollTop;

    //console.log(clientHeight,scrollHeight,scrollTop);
    if((scrollHeight - clientHeight)<=Math.ceil(scrollTop)){
        console.log("we are at the bottom");
        page++;
        fetchData(page);
    }
})

//to create the card
function createCard(item) {
    // Create card container element
    const card = document.createElement('div');
    card.classList.add('card');
  
    // Create image element
    const image = document.createElement('img');
    image.src = item.url;
    image.alt = item.title;
    card.appendChild(image);
  
    // Create title element
    const title = document.createElement('h2');
    title.textContent = item.title;
    card.appendChild(title);
  
    return card;
  }

  //to fetch the data
  async function fetchData(page=1){
    try{
        let res = await fetch(`https://jsonplaceholder.typicode.com/photos?_page=${page}&_limit=12`);
        let data = await res.json();
        console.log(data);
        appendData(data)
    }
    catch(err){
        console.log(err);
    }
  }

  //to append the data

  function appendData(data){
    data.forEach(item => container.append(createCard(item)));
  }
```