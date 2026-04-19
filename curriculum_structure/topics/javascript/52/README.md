# Flattening an Array [30 min] (1)

- Solution 1 (recursion + reduce)
    
    ```jsx
    /*
    Flatten a deeply nested array
    [ 1, [2,3], 5, [[6,[7]]], [9] ]
    */
    
    var array = [1, [2, 3], 5, [[6, [7]]], [9]];
    
    const flatten = (arr)=>{
        let newArray = arr.reduce((acc,item)=>{
          // if item is an array
          // or the item is an number
          if (Array.isArray(item)) {
              acc = acc.concat(flatten(item))
          }
          else {
              // acc.push(item);
              acc = [...acc, item];
          }
            return acc;
        }
        , [])
        
        return newArray;
    }
    
    console.log(flatten(array));
    ```
    
- Solution 2 (recursion + forEach)
    
    ```jsx
    /*
    Flatten a deeply nested array
    [ 1, [2,3], 5, [[6,[7]]], [9] ]
    */
    
    var array = [1, [2, 3], 5, [[6, [7, [8,9]]]], [10]];
    
    const flatten = (arr)=>{
        let newArray = [];
    
        arr.forEach(element => {
            if (Array.isArray(element)) {
                // manager receives a flattened array from its line manager. the work of the senior manager is just to concat the result it gets form its line manger.
                newArray = newArray.concat(flatten(element))
            } else {
                newArray.push(element)
            }
        })
    
        // every iteration is expected to return a flattened array to its manager.
        return newArray;
    }
    
    console.log(flatten(array));
    ```
    
- Solution 3 (Javascript’s flat() method)
    
    ```jsx
    /*
    Flatten a deeply nested array
    [ 1, [2,3], 5, [[6,[7]]], [9] ]
    */
    
    var array = [1, [2, 3], 5, [[6, [7, [8,9]]]], [10]];
    
    const flatten = (arr)=>{
        let newArray = arr.flat(4);
        return newArray;
    }
    
    console.log(flatten(array));
    ```