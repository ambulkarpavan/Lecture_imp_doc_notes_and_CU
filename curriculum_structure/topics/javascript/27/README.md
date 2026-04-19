# Store by value VS Store by reference [15 min] (1)

## Things & the places where we store them

![Untitled](Store%20by%20value%20VS%20Store%20by%20reference%20%5B15%20min%5D%20(1)%20d5b2ef7fe4ef455da1a7d04f7e30fa0e/Untitled.png)

![Untitled](Store%20by%20value%20VS%20Store%20by%20reference%20%5B15%20min%5D%20(1)%20d5b2ef7fe4ef455da1a7d04f7e30fa0e/Untitled%201.png)

![Untitled](Store%20by%20value%20VS%20Store%20by%20reference%20%5B15%20min%5D%20(1)%20d5b2ef7fe4ef455da1a7d04f7e30fa0e/Untitled%202.png)

![Untitled](Store%20by%20value%20VS%20Store%20by%20reference%20%5B15%20min%5D%20(1)%20d5b2ef7fe4ef455da1a7d04f7e30fa0e/Untitled%203.png)

![Untitled](Store%20by%20value%20VS%20Store%20by%20reference%20%5B15%20min%5D%20(1)%20d5b2ef7fe4ef455da1a7d04f7e30fa0e/Untitled%204.png)

![Untitled](Store%20by%20value%20VS%20Store%20by%20reference%20%5B15%20min%5D%20(1)%20d5b2ef7fe4ef455da1a7d04f7e30fa0e/Untitled%205.png)

Just like different things are stored in a different way, Javascript stores primitives and non-primitives in a very different way.

**Primitives (value types)**

string, number, boolean, undefined, null, bigInt, symbol

[https://www.canva.com/design/DAFiovh2Pb4/QUrBlfL4HuGDwvBjRuxhKA/edit?utm_content=DAFiovh2Pb4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton](https://www.canva.com/design/DAFiovh2Pb4/QUrBlfL4HuGDwvBjRuxhKA/edit?utm_content=DAFiovh2Pb4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

[By reference.pdf](Store%20by%20value%20VS%20Store%20by%20reference%20%5B15%20min%5D%20(1)%20d5b2ef7fe4ef455da1a7d04f7e30fa0e/By_reference.pdf)

**Non Primitives (reference types)**

object, array, function

let’s see an example with a string & arrays

## Storing `strings` vs storing `arrays`

![Untitled](Store%20by%20value%20VS%20Store%20by%20reference%20%5B15%20min%5D%20(1)%20d5b2ef7fe4ef455da1a7d04f7e30fa0e/Untitled%206.png)

Variable created + value directly put on `vs` Variable created + value referenced 

Animation: [https://vivmagarwal.github.io/course-animations/animations/by-ref-by-val-2/index.html#0](https://vivmagarwal.github.io/course-animations/animations/by-ref-by-val-2/index.html#0) 

Python tutor: [link](https://pythontutor.com/render.html#code=let%20str%20%3D%20%22Vivek%22%3B%0Alet%20num%20%3D%20%22999%22%3B%0Alet%20bool%20%3D%20false%3B%0Alet%20nl%20%3D%20null%3B%0Alet%20ud%20%3D%20undefined%3B%0A%0Alet%20obj%20%20%3D%20%7Bname%3A%20'vivek'%7D%3B%0Alet%20arr%20%3D%20%5B1,2,3%5D%3B%0Alet%20fun%20%3D%20function%28a,b%29%7B%20return%20a%2Bb%3B%20%7D&cumulative=false&curInstr=8&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=js&rawInputLstJSON=%5B%5D&textReferences=false)

### Student Task

- Stored by Value
    
    ```jsx
    
    let a = 10;
    let b = a;
    
    b = 20;
    
    console.log(a);
    console.log(b);
    
    //Guess the Output for **a** and **b**: __________
    ```
    
- Stored by Reference - Array
    
    ```jsx
    
    let arr1 = [1, 2, 3];
    let arr2 = arr1;
    
    arr2.push(4);
    
    console.log(arr1);
    console.log(arr2);
    
    //Guess the Output for **`arr1`** and **`arr2`**: __________
    ```
    
- Stored by Reference - Object
    
    ```jsx
    
    let obj1 = { name: "Alice", age: 25 };
    let obj2 = obj1;
    
    obj2.age = 30;
    
    console.log(obj1.age);
    console.log(obj2.age);
    
    //Guess the Output for **obj1.age** and **obj2.age**: __________
    ```
    
- Stored by Value-Function Arguments
    
    ```jsx
    
    function modifyValue(value) {
      value = "Modified";
    }
    
    let originalValue = "Original";
    modifyValue(originalValue);
    
    console.log(originalValue);
    
    //Guess the Output for **originalValue**: __________
    ```
    
- Stored by Reference - Function Arguments
    
    ```jsx
    
    function modifyArray(arr) {
      arr.push(4);
    }
    
    let myArray = [1, 2, 3];
    modifyArray(myArray);
    
    console.log(myArray);
    
    //Guess the Output for myArray: __________
    ```