# E-commerce - I (1)

Yesterday, I’ve given a hint for updating the todo arr on delete functionality. Could you do it ?

There are a few changes we’ve to do in order to obtain this delete functionality. So, `event.target.parentNode.remove()` will work but when we refresh it, it is coming again, right? So, what should we do? We’ve to update the todoArr on delete. How do you update it? 

We can use splice inbuilt function in order to delete a certain element placed at a certain index. We’ve learnt this, right?

Let’s revisit it again.

```jsx
var arr = [1,2,3,4,5,6,7]

// splice(startingIndex, no of items to be spliced)
Now, if I want to delete 5 from the above array, I can use splice method.
But the splice method requires an index also in order to delete 5

If I write something like this 

arr.splice(4,1)

What will this do, it'll delete the number 5
Now if I console.log(arr), we achieve the desired result.
```

So, now if I want to delete the second element, what can I do? Firstly, I have send the index of the second element. Now, how do I send this index. In map, we’ve 3 parameters ⇒ element, index and the array itself. So, can I just write index as seconds argument and then get index. Agree?

Now, we got the index. Then what should we do? We need to send this index to the delete function, right? 

```jsx
td3.addEventListener("click",deleteRow(index));
```

Will this be fine ?

No, because we can give any name, but by default it’ll show us event object, right? So, apart from the event object, how do we send arguments ?

```jsx
td3.addEventListener("click", function () {
      deleteRow(index);
    });
```

Now, all we’ve to do is filter the `todoArr` based on id and set it to local storage again.

```jsx
var updatedTodoArr = todoArr.splice(index,1)
  localStorage.setItem("todoList", JSON.stringify(updatedTodoArr));
  displayTodos(updatedTodoArr);
```

Now, it’ll work.

## Set Attribute

- The `setAttribute()` method sets a new value to an attribute.
- Here attributes can be any of the following
    - id
    - class
    - href
    - src, etc

# Syntax

```jsx
*element*.setAttribute(attributeN*ame*, attributeV*alue*)
```

**Example:**

```jsx
<html>
  <body>
    <div id="new">
      <p>Masai School</p>
    </div>
  </body>
</html>
<script>
      var newPara = document.createElement("p");
      newPara.innerText = "The Coding School that cares about you";
			// Setting class of "para" to p tag
			newPara.setAttribute("class","para")
			// Setting id of "container" to p tag
			newPara.setAttribute("id","container")
      document.getElementById("new").append(newPara);
</script>
```

- Now whatever styles we write for that class “para” or id “container” will be applied to that <p> tag

```jsx
<html>
<style>
.para {
	font-size:40px
}
</style>
  <body>
    <div id="new">
      <p>Masai School</p>
    </div>
  </body>
</html>
<script>
      var newPara = document.createElement("p");
      newPara.innerText = "The Coding School that cares about you";

			// Setting class of "para" to p tag
			newPara.setAttribute("class","para")

			// Setting id of "container" to p tag
			newPara.setAttribute("id","container")

      document.getElementById("new").append(newPara);
</script>
```

- Add a href attribute to an <a> element:

```jsx
myAnchor.setAttribute("href", "https://www.google.com");
```

## E- commerce app

Show the deployed layout and say we’re going to build that layout using HTML and CSS. Then we’ll build it using HTML, CSS and JS.

- **Code with HTML and CSS**
    
    ```jsx
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <style>
          #mensData {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
          }
    
          #mensData > div > div {
            display: flex;
            justify-content: space-around;
          }
    
          #mensData > div > div > p:last-child {
            text-decoration: line-through;
          }
        </style>
      </head>
      <body>
        <div id="mensData">
          <div>
            <img
              src="https://content.shop4reebok.com/static/Product-EX4296/reebok_EX4296_1.jpg.plp"
              alt=""
            />
            <h5>MEN'S REEBOK RUNNING ROADMAP SHOES</h5>
            <div>
              <p>1170</p>
              <p>2599</p>
            </div>
          </div>
          <div>
            <img
              src="https://content.shop4reebok.com/static/Product-EX4296/reebok_EX4296_1.jpg.plp"
              alt=""
            />
            <h5>MEN'S REEBOK RUNNING ROADMAP SHOES</h5>
            <div>
              <p>1170</p>
              <p>2599</p>
            </div>
          </div>
          <div>
            <img
              src="https://content.shop4reebok.com/static/Product-EX4296/reebok_EX4296_1.jpg.plp"
              alt=""
            />
            <h5>MEN'S REEBOK RUNNING ROADMAP SHOES</h5>
            <div>
              <p>1170</p>
              <p>2599</p>
            </div>
          </div>
          <div>
            <img
              src="https://content.shop4reebok.com/static/Product-EX4296/reebok_EX4296_1.jpg.plp"
              alt=""
            />
            <h5>MEN'S REEBOK RUNNING ROADMAP SHOES</h5>
            <div>
              <p>1170</p>
              <p>2599</p>
            </div>
          </div>
          <div>
            <img
              src="https://content.shop4reebok.com/static/Product-EX4296/reebok_EX4296_1.jpg.plp"
              alt=""
            />
            <h5>MEN'S REEBOK RUNNING ROADMAP SHOES</h5>
            <div>
              <p>1170</p>
              <p>2599</p>
            </div>
          </div>
          <div>
            <img
              src="https://content.shop4reebok.com/static/Product-EX4296/reebok_EX4296_1.jpg.plp"
              alt=""
            />
            <h5>MEN'S REEBOK RUNNING ROADMAP SHOES</h5>
            <div>
              <p>1170</p>
              <p>2599</p>
            </div>
          </div>
          <div>
            <img
              src="https://content.shop4reebok.com/static/Product-EX4296/reebok_EX4296_1.jpg.plp"
              alt=""
            />
            <h5>MEN'S REEBOK RUNNING ROADMAP SHOES</h5>
            <div>
              <p>1170</p>
              <p>2599</p>
            </div>
          </div>
          <div>
            <img
              src="https://content.shop4reebok.com/static/Product-EX4296/reebok_EX4296_1.jpg.plp"
              alt=""
            />
            <h5>MEN'S REEBOK RUNNING ROADMAP SHOES</h5>
            <div>
              <p>1170</p>
              <p>2599</p>
            </div>
          </div>
        </div>
      </body>
    </html>
    ```
    
- If you see the above code there is so much repetition in our HTML, we are writing same div 8 times, so did you ever wonder whether we can use for loop for that?
- Yes we can use for loop, but for that we need to build same layout using JS dynamically by keeping all variables in array of objects.

```jsx
for(var i=0;i<9;i++){
 <div>
        <img
          src="https://content.shop4reebok.com/static/Product-EX4296/reebok_EX4296_1.jpg.plp"
          alt=""
        />
        <h5>MEN'S REEBOK RUNNING ROADMAP SHOES</h5>
        <div>
          <p>1170</p>
          <p>2599</p>
        </div>
      </div>

}
```

- We need to first create array of objects data, and then map that data.

- **Code with HTML, CSS and JS**
    
    ```jsx
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Cart</title>
        <style>
          #mensData {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
          }
          #mensData > div {
            box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px,
              rgba(0, 0, 0, 0.3) 0px 30px 60px -30px,
              rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
    				border-radius:20px;
          }
          img {
            width: 100%;
    				border-radius:20px;
          }
          .priceBox {
            display: flex;
            justify-content: space-around;
          }
         .priceBox > p:last-child {
            text-decoration: line-through;
            text-decoration-color: crimson;
            color: dodgerblue;
            text-decoration-thickness: 3px;
          }
        </style>
      </head>
      <body>
        <div id="mensData"></div>
      </body>
    </html>
    <script>
     
     var mensData =[] //array of objects we'll take 
    	See below for the array of objects
    
      displayProducts(mensData);
    
      function displayProducts(data) {
        data.map(function (elem) {
          var div = document.createElement("div");
          var image = document.createElement("img");
          image.setAttribute("src", elem.image_url);
          var productName = document.createElement("h5");
          productName.innerText = elem.name;
          var priceBox = document.createElement("div");
          var price = document.createElement("p");
          price.innerText = elem.price;
          var strikedPrice = document.createElement("p");
          strikedPrice.innerText = elem.strikedoffprice;
          priceBox.append(price, strikedPrice);
          //  priceBox.style.display = "flex" we won't use this now because this will create inline styles
          priceBox.setAttribute("class", "priceBox");
          div.append(image, productName, priceBox);
          document.querySelector("#mensData").append(div);
        });
      }
    </script>
    ```
    
    ```jsx
    var mensData = [
        {
          id: 1,
          image_url:
            "https://content.shop4reebok.com/static/Product-EX4296/reebok_EX4296_1.jpg.plp",
          name: "MEN'S REEBOK RUNNING ROADMAP SHOES",
          price: 1170,
          strikedoffprice: 2599,
        },
    
        {
          id: 2,
          image_url:
            "https://content.shop4reebok.com/static/Product-EX3921/reebok_EX3921_1.jpg.plp",
          name: "MEN'S REEBOK SWIM ARUBA FLIP SLIPPERS ",
          price: 699,
          strikedoffprice: 999,
        },
        {
          id: 3,
          image_url:
            "https://content.shop4reebok.com/static/Product-EX4160/reebok_EX4160_1.jpg.plp",
          name: " MEN'S REEBOK RUNNING AUSTIN SHOES",
          price: 945,
          strikedoffprice: 2099,
        },
        {
          id: 4,
          image_url:
            "https://content.shop4reebok.com/static/Product-EX3921/reebok_EX3921_1.jpg.plp",
          name: "MEN'S REEBOK SWIM ARUBA FLIP SLIPPERS ",
          price: 699,
          strikedoffprice: 999,
        },
        {
          id: 5,
          image_url:
            "https://content.shop4reebok.com/static/Product-EX4160/reebok_EX4160_1.jpg.plp",
          name: " MEN'S REEBOK RUNNING AUSTIN SHOES",
          price: 945,
          strikedoffprice: 2099,
        },
        {
          id: 6,
          image_url:
            "https://content.shop4reebok.com/static/Product-EX3921/reebok_EX3921_1.jpg.plp",
          name: "MEN'S REEBOK SWIM ARUBA FLIP SLIPPERS ",
          price: 699,
          strikedoffprice: 999,
        },
        {
          id: 7,
          image_url:
            "https://content.shop4reebok.com/static/Product-EX4160/reebok_EX4160_1.jpg.plp",
          name: " MEN'S REEBOK RUNNING AUSTIN SHOES",
          price: 945,
          strikedoffprice: 2099,
        },
        {
          id: 8,
          image_url:
            "https://content.shop4reebok.com/static/Product-EX3921/reebok_EX3921_1.jpg.plp",
          name: "MEN'S REEBOK SWIM ARUBA FLIP SLIPPERS ",
          price: 699,
          strikedoffprice: 999,
        },
        {
          id: 9,
          image_url:
            "https://content.shop4reebok.com/static/Product-EX4160/reebok_EX4160_1.jpg.plp",
          name: " MEN'S REEBOK RUNNING AUSTIN SHOES",
          price: 945,
          strikedoffprice: 2099,
        },
      ];
    ```
    
    Now let’s add a button `Add to Cart` . Add this code below priceBox
    
    ```jsx
    var cartBtn = document.createElement("button")
    cartBtn.innerText = "Add to Cart"
    cartBtn.setAttribute("class","cartBtn")
    div.append(add cartBtn at last)
    ```
    
    Now we can add a few styles to this cart button as follows
    
    ```jsx
          .cartBtn {
            width: 50%;
            border-radius: 5px;
            padding: 5px 0;
            display: block;
            background-color: teal;
            border: 0;
            margin: 15px auto;
            color: white;
          }
          p {
            margin: -3px 0;
          }
    ```
    
    Now let’s write the functionality of this cart button.
    
    ```jsx
    cartBtn.addEventListener("click",function(){
    	addToCart(index)
    })
    var productsInCart = JSON.parse(localStorage.getItem("cart")) || [];
    function addToCart(i) {
    	var product = mensData.filter(function(elem,index){
    		return index == i
    	})
    	productsInCart.push(product)
    	localStorage.setItem("cart",JSON.stringify(productsInCart))
    }
    ```
    
    Now let’s create a cart page where we can see all the products we’ve added to cart. 
    
    So let’s create one more file with name, cart.html. We’ve seen how we can link masai school website using anchor tag, right? So, we’ll now link this cart page also using anchor tag.
    
    ```jsx
    In html, before div,
    <body>
    		<button id="cartPage"><a href="cart.html">Go To Cart</a></button>
        <div id="mensData"></div>
      </body>
    ```
    
    Let us style it also 
    
    ```jsx
    #cartPage {
            background-color: crimson;
            border: 0;
            padding: 5px;
            border-radius: 5px;
            margin-bottom: 20px;
          }
          #cartPage > a {
            color: white;
            text-decoration: none;
          }
    ```
    
    Now, we’ve created a cart page. So, let us show what products are present inside the cart in this page.
    
    ```jsx
    <html lang="en">
      <head>
        <title>Cart Page</title>
        <style>
          .product {
            display: flex;
            justify-content: space-around;
            align-items: center;
          }
          #total {
            display: flex;
            justify-content: space-around;
          }
        </style>
      </head>
      <body>
        <h2>Cart Page</h2>
        <div id="cart"></div>
      </body>
    </html>
    
    <script>
      var products = JSON.parse(localStorage.getItem("cart")) || [];
      var cart = document.getElementById("cart");
      if (products.length == 0) {
        cart.innerText = "Cart is empty. Add products to cart.";
      } else {
        displayProducts();
        calculateTotal();
      }
    
      function displayProducts() {
        cart.innerText = "";
        products.map(function (elem) {
          var div = document.createElement("div");
          div.setAttribute("class", "product");
          var image = document.createElement("img");
          image.setAttribute("src", elem.image_url);
          var productName = document.createElement("h5");
          productName.innerText = elem.name;
          var price = document.createElement("p");
          price.innerText = elem.price;
          div.append(image, productName, price);
          cart.append(div);
        });
      }
      function calculateTotal() {
        var total = products.reduce(function (acc, curr) {
          return acc + curr.price;
        }, 0);
        var cartVal = document.createElement("h5");
        cartVal.innerText = "₹ " + total;
        var p = document.createElement("p");
        p.innerText = "Total";
        var div = document.createElement("div");
        div.append(p, cartVal);
        div.setAttribute("id", "total");
        document.querySelector("body").append(div);
      }
    </script>
    ```
    

```jsx
var mensData = [
  {
    id: 1,
    image_url:
      "https://content.shop4reebok.com/static/Product-EX4296/reebok_EX4296_1.jpg.plp",
    name: "MEN'S REEBOK RUNNING ROADMAP SHOES",
    price: 1170,
    strikedoffprice: 2599,
  },
  {
    id: 2,
    image_url:
      "https://content.shop4reebok.com/static/Product-EX3921/reebok_EX3921_1.jpg.plp",
    name: "MEN'S REEBOK SWIM ARUBA FLIP SLIPPERS ",
    price: 699,
    strikedoffprice: 999,
  },
  {
    id: 3,
    image_url:
      "https://content.shop4reebok.com/static/Product-EX4160/reebok_EX4160_1.jpg.plp",
    name: " MEN'S REEBOK RUNNING AUSTIN SHOES",
    price: 945,
    strikedoffprice: 2099,
  },
  {
    id: 4,
    image_url:
      "https://content.shop4reebok.com/static/Product-EX3921/reebok_EX3921_1.jpg.plp",
    name: "MEN'S REEBOK SWIM ARUBA FLIP SLIPPERS ",
    price: 699,
    strikedoffprice: 999,
  },
  {
    id: 5,
    image_url:
      "https://content.shop4reebok.com/static/Product-EX4160/reebok_EX4160_1.jpg.plp",
    name: " MEN'S REEBOK RUNNING AUSTIN SHOES",
    price: 945,
    strikedoffprice: 2099,
  },
  {
    id: 6,
    image_url:
      "https://content.shop4reebok.com/static/Product-EX3921/reebok_EX3921_1.jpg.plp",
    name: "MEN'S REEBOK SWIM ARUBA FLIP SLIPPERS ",
    price: 699,
    strikedoffprice: 999,
  },
  {
    id: 7,
    image_url:
      "https://content.shop4reebok.com/static/Product-EX4160/reebok_EX4160_1.jpg.plp",
    name: " MEN'S REEBOK RUNNING AUSTIN SHOES",
    price: 945,
    strikedoffprice: 2099,
  },
  {
    id: 8,
    image_url:
      "https://content.shop4reebok.com/static/Product-EX3921/reebok_EX3921_1.jpg.plp",
    name: "MEN'S REEBOK SWIM ARUBA FLIP SLIPPERS ",
    price: 699,
    strikedoffprice: 999,
  },
  {
    id: 9,
    image_url:
      "https://content.shop4reebok.com/static/Product-EX4160/reebok_EX4160_1.jpg.plp",
    name: " MEN'S REEBOK RUNNING AUSTIN SHOES",
    price: 945,
    strikedoffprice: 2099,
  },
];
```