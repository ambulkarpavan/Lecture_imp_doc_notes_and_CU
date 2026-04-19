# Debouncing & Throttling [120 min] (1)

### Story of an Indian kid

![Untitled](Debouncing%20&%20Throttling%20%5B120%20min%5D%20(1)%202fc679c0da95467f86f0ee8e34c20b61/Untitled.png)

- bread
- and wheat
- and suji
- and potatoes
- and tomatoes

### Discuss different ways by which the action can be optimized

- Probable solutions
    - you run to shop only when your mom pauses for 5 seconds
    - you

### The client-server model

![Untitled](Debouncing%20&%20Throttling%20%5B120%20min%5D%20(1)%202fc679c0da95467f86f0ee8e34c20b61/Untitled%201.png)

Codepen examples: 

Normal: [https://codepen.io/drupalastic/pen/dyjRZzg?editors=1011](https://codepen.io/drupalastic/pen/dyjRZzg?editors=1011) 

With Debouncing: [https://codepen.io/drupalastic/pen/WNKOXbN?editors=1011](https://codepen.io/drupalastic/pen/WNKOXbN?editors=1011)

Live example: [https://www.hotstar.com/in](https://www.hotstar.com/in) 

### Simplified example - Normal

```html
<input id = "input"></input>
```

```jsx
let input = document.getElementById('input');

function greet(name) {
  console.log(`Greetings from ${name}`)
}

input.addEventListener('keyup', function(e) {
  console.log('changed', e.target.value)
})
```

Codepen: [https://codepen.io/drupalastic/pen/PoBjJqE?editors=1011](https://codepen.io/drupalastic/pen/PoBjJqE?editors=1011) 

OMDB API: [https://www.omdbapi.com](https://www.omdbapi.com/)

### Closure with example

```jsx
function outerFunction(){
    let x = 10;

    function innerFunction(){
        return x+=1;
    };

    return innerFunction;
}

let f1 = outerFunction();
let f2 = outerFunction();

// console.log(f1());11
// console.log(f1());12
// console.log(f1());13
// console.log(f2());11
// console.log(f2());12
```

### Simplified example - with debouncing

```jsx
function deBounce(fn,delay){

    let id;
    return function f(){
        clearInterval(id)
        id= setTimeout(function(){
            fn();
        },delay);
    }
}
```

### Simplified example - with throttling

```jsx
function throttle(fn,delay){
    let id1=false;

    return function (){
        if(id1){
            return;
        }
        fn();
        id1 = true;
        setTimeout(function(){  
            id1 = false;
        },delay)
    }

}
```

## Debouncing vs Throttling - Visualised

[https://redd.one/blog/debounce-vs-throttle](https://redd.one/blog/debounce-vs-throttle) 

(Student task: go to this site and try to make sense of the difference between them)

Debouncing

![Untitled](Debouncing%20&%20Throttling%20%5B120%20min%5D%20(1)%202fc679c0da95467f86f0ee8e34c20b61/Untitled%202.png)

Closure WhiteBoarding : 

[closure.pdf](Debouncing%20&%20Throttling%20%5B120%20min%5D%20(1)%202fc679c0da95467f86f0ee8e34c20b61/closure.pdf)

## closure example live class

```jsx

function outerFunction(){
    let x= 10;

    return function innerFunction(){
        return x += 1;
    }
}

let f1 = outerFunction(); //x =10
let f2 = outerFunction(); //x=10

console.log(f1()) //11
console.log(f1()) //12
console.log(f1()) //13
console.log(f1()) //14

console.log(f2())//11
console.log(f2())//12
console.log(f2())//13
```

## debounce example live class

```jsx
let inpt = document.getElementById("inpt");
let container = document.getElementById('container');

function appendcard(data){

    container.innerHTML ="";

    data.forEach(item =>{
        let card = createCard(item);
        container.append(card)
    })

 
}

function createCard(item){

    let card = document.createElement("div");
    let img = document.createElement("img");
    let p = document.createElement("p");
    let h3 = document.createElement("h3");

    card.className = "card";
    img.className = "poster";
    h3.className = "title";
    p.className = "type";

    img.src= item.Poster;
    h3.innerText = item.Title;
    p.innerText = item.Type;

    card.append(h3,p,img);
    return card;
}

inpt.addEventListener("input",()=>{deBounce1()})

//to fetch the data from api

async function fetchData(){
    try{
        let res = await fetch(`https://www.omdbapi.com/?apikey=a4ed1e08&s=${inpt.value}`);
        let data = await res.json();
        console.log(data);
        appendcard(data.Search);
    }
    catch(err){

    }
}

let timer;

function deBounce(fun,delay){
    if(timer){
        clearTimeout(timer);
    }

   timer = setTimeout(function(){
        // fetchData()
        fun()
    },delay)
}

//refactor debouncing

function deBounce(fun,delay){
    let timer;

    return function (){
        if(timer){
            clearTimeout(timer);
        }

    timer = setTimeout(function(){
            // fetchData()
            fun()
        },delay)
    }
}

let deBounce1 = deBounce(fetchData,1000);

```

## throttling example live class

```jsx
let inpt = document.getElementById("inpt");
let container = document.getElementById('container');

function appendcard(data){

    container.innerHTML ="";

    data.forEach(item =>{
        let card = createCard(item);
        container.append(card)
    })

 
}

function createCard(item){

    let card = document.createElement("div");
    let img = document.createElement("img");
    let p = document.createElement("p");
    let h3 = document.createElement("h3");

    card.className = "card";
    img.className = "poster";
    h3.className = "title";
    p.className = "type";

    img.src= item.Poster;
    h3.innerText = item.Title;
    p.innerText = item.Type;

    card.append(h3,p,img);
    return card;
}

inpt.addEventListener("input",()=>{deBounce1()})

//to fetch the data from api

async function fetchData(){
    try{
        let res = await fetch(`https://www.omdbapi.com/?apikey=a4ed1e08&s=${inpt.value}`);
        let data = await res.json();
        console.log(data);
        appendcard(data.Search);
    }
    catch(err){

    }
}

inpt.addEventListener("input",()=>{throttling1()})

let flag = false;//timer is not running

function throttling(fun,delay){
    if(flag==true){
        //if timer is running i will simply return or do nothing
        return;
    }
    fun()
    
    flag =true;//timer is starting
    setTimeout(function(){
        flag =false;
        //timer is end
    },delay)

}

//refactoring of throttling
function throttling(fun,delay){
    let flag = false;//timer is not running

    return function (){
        if(flag==true){
            //if timer is running i will simply return or do nothing
            return;
        }
        fun()
        
        flag =true;//timer is starting
        setTimeout(function(){
            flag =false;
            //timer is end
        },delay)

    }
}

let throttling1 = throttling(fetchData,1000);
```

**CP Assignment Link:**

| debouncing | JS-Startwars | https://cp.masaischool.com/problems/587/view#basicDetails |
| --- | --- | --- |
| Throttling | JS-Startwars | https://cp.masaischool.com/problems/547/view#basicDetails |
|  | js-debounce-throttle-API | https://cp.masaischool.com/problems/1994/view#basicDetails |

**CP Evaluation Link:**

| Contacts-book+Debounce-Throttling | https://cp.masaischool.com/problems/1988/view#basicDetails | https://github.com/masai-problems/Contacts-book-Debounce-Throttling |
| --- | --- | --- |