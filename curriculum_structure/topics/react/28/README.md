# Side Effects or Effects

Serial: 27
Made for: Beginner
Requirement: Must Have
Time in minutes: 20
Learning Objectives: effects and useEffect
Related back to React: Effects and useEffect I - Mount phase (Effects%20and%20useEffect%20I%20-%20Mount%20phase%20a7c8ad7722e34cc4a163c1b374ca1b45.md)
doc-id: react-27

- Side effects or effects
    - Introduction
    - Some examples

# Effects or Side effects :

Side effects are operations outside the component's scope, such as API calls, timers, or manipulating the DOM directly.

To understand this. let’s take a simple example

### Example 1 : Counter/Todo and Working with Document API of browser

Build a simple counter that gets incremented on click of a button

```jsx
import { useState } from "react"
import "./App.css"

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <h1>Count : {count}</h1>
      <button onClick={() => setCount(count + 1)}>INCREASE COUNT</button>
    </div>
  )
}

export default App
```

**Problem statement 1** : I want to change the title of the page from the default title to `“Counter Application"` from my `App` component as soon as the component is mounted onto UI. ( mount event )

For this, from my react functional component `App` ; I have to interact with `document` API which is a browser API. 

- This means I have to go outside the scope of my component and interact with document API.
- This means I have to perform a side effect.

**What is side effect ?**

In React, a "side effect" or “effect” is any operation that interacts with the outside of a component's scope. To put it in simple words - “side effect” is when you have to go outside the scope of your react component and interact with “outside world”

This can include things like:

**Some Real World Examples :** 

1. Making API calls to get or send data ( Fetch or Axios )
2. Setting up subscriptions or event listeners ( Interacting with some external API )
3. Interacting with document API which is a browser API 
4. Using timers ( using `setTimeout` , `setInterval` etc which are browser API )
5. Using local storage which is again a browser API

Coming back to the problem statement. I now have to use document API ( perform “sideeffect”  ) in my App component as soon as the component is mounted. 

Initially you might feel like doing something like this

```jsx
import { useState } from "react"
import "./App.css"

function App() {
  const [count, setCount] = useState(0)

  document.title = "Counter Application" /** THIS IS NOT THE RIGHT WAY **/

  return (
    <div>
      <h1>Count : {count}</h1>
      <button onClick={() => setCount(count + 1)}>INCREASE COUNT</button>
    </div>
  )
}

export default App
```

**The problem with the above approach :**

Side effects are operations that can't be done during the rendering process and need to be handled separately. So in the above example, you can’t block the rendering process and interact with document API. 

**Reason** : These side effect operations wherein you go and interact with outside APIs are unpredictable. You don’t know how long is it gonna take for that operation to complete. Are we going to block the component render till that time ??

No

So how do we handle these side effects ?

By using `useEffect` hook from react