# bigInt & Symbols [15 min] (1)

- bigInt
    
    [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
    
    In JavaScript, the “number” type cannot safely represent integer values larger than `(2^53-1)`  (that’s `9007199254740991`), or less than `-(2^53-1)`for negatives. 
    
    `BigInt` type was recently added to the language to represent integers of arbitrary length. A `BigInt` value is created by appending `n` to the end of an integer:
    
    ```jsx
    // the "n" at the end means it's a BigInt
    const aVeryBigNumber = 1234567890123456789012345678901234567890n;
    console.log(typeof aVeryBigNumber)
    ```
    
- symbol
    
    [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
    
    The `symbol` type is used to create unique identifiers for objects.  Javascript object has keys of type `String` . Modern Javascript provides a second type that you can use for object keys - the `Symbol` type. Symbols are a new primitive type in ES6. 
    
    We can create a symbol in any of the following ways:
    
    ```jsx
    let symbol1 = Symbol('hello'); // Guarenteed unique value
    let symbol2 = Symbol.for('world');
    ```
    
    Symbols can also be created with a label, by passing a string as the first argument. The **label** doesn’t affect the value of the symbol, but is useful for debugging, and is shown if the symbol’s toString() method is called.
    
    if you try to use a new Symbol using `Symbol('hello')` it will be a new symbol and won't interface with the existing one even if the **descriptor** is the same. On the other hand,  if you try to create a new Symbol using `Symbol.for('world')` , since the descriptor string is same, we will end up overwriting the existing symbol.
    
    Understanding the problem that `Symbol`s are designed to solve:
    
    ![Untitled](bigInt%20&%20Symbols%20%5B15%20min%5D%20(1)%20b7b2222c52bf4f828b6ecaa428018ac3/Untitled.png)
    
    Symbols are unique and this is the principal advantage of symbols. If we needed to have a string key that is guaranteed to be unique, we may add a counter or a timestamp or a random number, but Symbols looks to be a much cleaner and scalable solution.
    
    Since symbols are not strings, we cannot use a dot notation for symbol keys. Instead, we use a bracket operator:
    
    ```jsx
    let obj = {
      [symbol1]: 'world'
    }
    
    obj[symbol1] = 'Something else'
    ```
    
    Symbols being guaranteed unique is especially useful when multiple middlewares are updating the same object. It ensures that a new plugin or module will not accidentally overwrite another important property of the object. 
    
    Just for the sake of a simple example and some practice Let's say we have a really simple form in our application that takes just two inputs from every anonymous user. 
    
    It collects in their first name & the way they are feeling today `['bad', 'okay' or 'great']`.
    
    At the end of every day, we need a summary of the data. We have one big object and all the data must be stored in that object in a key-value pair.
    
    Here's a possible solution:
    
    ```jsx
    let feelingData = {
      addData: function (name, feeling) {
        this[name] = feeling;
      }
    }
    
    feelingData.addData('John', 'bad');
    feelingData.addData('Michael', 'good');
    feelingData.addData('John', 'bad');
    feelingData.addData('John', 'great');
    
    console.log(feelingData);
    
    // John: "great"
    // Michael: "good"
    ```
    
     
    
    As we can see we are getting a really perverted view of our users mood. This is a really good use case of Javascripts Symbols.
    
    ```jsx
    let feelingData = {
      addData: function (name, feeling) {
        this[Symbol(name)] = feeling;
      }
    }
    
    feelingData.addData('John', 'bad');
    feelingData.addData('Michael', 'good');
    feelingData.addData('John', 'bad');
    feelingData.addData('John', 'great');
    
    console.log(feelingData);
    
    // Symbol(John): "bad"
    // Symbol(John): "bad"
    // Symbol(John): "great"
    // Symbol(Michael): "good"
    ```
    
    This looks much more accurate. We only changed line 3 where instead of using the string name of a user as a key to store their response, use used a Symbol with the String descriptor to store their mood.
    
    Another use-case of Symbols is to partially hide a property in an object.  Take the following example object:
    
    ```jsx
    let passcodeSym = Symbol('passcode');
    let roleSym = Symbol.for('role');
    
    let obj = {
      name: 'John doe',
      age: 36,
      [passcodeSym]: 'world',
      [roleSym]: 'trainee'
    }
    
    obj[Symbol('passcode')] = 'Hello'; // will not overwrite but create a new property with the same descriptor
    obj[Symbol.for('role')] = 'developer'; // will overwrite the existing one with the same descriptor
    ```
    
    The properties with a Symbol as their key is partially hidden in a way that they can not be directly accessed in these obvious ways: 
    
    ```jsx
    console.log(obj.passcodeSym); // undefined
    console.log(Object.getOwnPropertyNames(obj)); // (2) ['name', 'age']
    
    for (const key in obj) {
      console.log(key);
    }
    // name
    // age
    
    console.log(Object.keys(obj))
    console.log(JSON.stringify(obj))
    ```
    
    However, they are not actually truly hidden because there are ways to see them:
    
    ```jsx
    console.log(Object.getOwnPropertySymbols(obj));
    // (3) [Symbol(passcode), Symbol(role), Symbol(passcode)]
    
    console.log(Reflect.ownKeys(obj));
    //(5) ['name', 'age', Symbol(passcode), Symbol(role), Symbol(passcode)]
    ```
    
    The Global registry: 
    
    `Symbol.for(key)` retrieves the symbol for a given key from the registry. If a symbol doesn’t exist for the key, a new one is returned. As you might expect, subsequent calls for the same key will return the same symbol.
    
    `Symbol.keyFor(symbol)` allows you to retrieve the key for a given symbol. Calling the method with a symbol that doesn’t exist in the registry returns undefined
    
    Video class for Symbols: [https://zoom-lecture-recordings.s3.ap-south-1.amazonaws.com/86817100867/js201_1668591674000](https://zoom-lecture-recordings.s3.ap-south-1.amazonaws.com/86817100867/js201_1668591674000) [starts from 1hr 41 mins]