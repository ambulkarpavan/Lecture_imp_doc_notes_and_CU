# Data sharing between components

Serial: 19
Made for: Beginner
Requirement: Must Have
Time in minutes: 30
Learning Objectives: State Management, useState
doc-id: react-19

Let us try and understand how data can be shared between components in React Application. 

Data / Info can be passed from

1. Parent to Child
2. Child to Parent
3. Sibling to Sibling

# **Parent to Child : Sending some information from parent to child**

Here's a code example to visualize this:

```jsx
// The Child component
function Child(props) {
  return <h1>{props.count}</h1>; // The Child reads the note
}

// The Parent component
function Parent() {
  const [count, setCount] = React.useState(0); // The Parent has a number

  // This function changes the number when you click a button
  const increment => setCount(count + 1);;

  return (
    <div>
      <Child count={count} /> {/* The Parent passes the number to the Child */}
      <button onClick={increment}>Click Me</button>
    </div>
  );
}

// Rendering the Parent component
const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
reactRoot.render(<Parent />);
```

**Concept** : 

- Imagine you have a "Parent" component and a "Child" component. The Parent is like a generous giver, and the Child is the receiver.
- The Parent holds some information, like a number, in its personal box called 'state'. Whenever the Parent wants to share this information with the Child, it sends it over as a 'prop' (short for property). The Child can use this prop to display the information, but it can't change what's inside the prop. It's like receiving a letter that you can read but not edit.

**Example** : 

You have a Parent that keeps track of a number ( `count` ). The Parent saves this `count` and also passes it to the Child. The Child then displays this number.

![parent-child.png](Data%20sharing%20between%20components%203bc994c916c54c1f981a5f5cf0efe7a7/parent-child.png)

# Child to Parent : **Sending some information from child to parent**

```jsx
function Child(props) {
  return (
    <>
      <h1>{props.count}</h1>
      <button onClick={() => props.incrementByValue(1)}>INC BY 1</button>
      <button onClick={() => props.incrementByValue(5)}>INC BY 5</button>
      <button onClick={() => props.incrementByValue(8)}>INC BY 8</button>
      <button onClick={() => props.incrementByValue(10)}>INC BY 10</button>
    </>
  );
}

function Parent() {
  const [count, setCount] = React.useState(0);

  const incrementByValue = (val) => {
    setCount(count + val);
  };

  return (
    <div>
      <Child count={count} incrementByValue={incrementByValue} />
    </div>
  );
}

const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
reactRoot.render(<Parent />);
```

**Concept :** 

Sometimes, the Child needs to tell the Parent to change the information. Since the Child can't change the props directly, it uses a special method provided by the Parent. This method is like a phone call to the Parent, saying, "Hey, please change the information like this."

**Example :** 

The Child has buttons to increase the count by different amounts. When you click these buttons, they tell the Parent to increase the count by 1, 5, 8, or 10.

![child-parent.png](Data%20sharing%20between%20components%203bc994c916c54c1f981a5f5cf0efe7a7/child-parent.png)

# Sibling to Sibling : **Sharing some information between sibling components**

```jsx
function Child1(props) {
  return <h1>count : {props.count}</h1>;
}

function Child2(props) {
  return <button onClick={props.increment}>INCREMENT</button>;
}

function Child3(props) {
  function isEvenOrOdd(num) {
    return num % 2 === 0 ? "even" : "odd";
  }

  return <h1>count is {isEvenOrOdd(props.count)} number</h1>;
}

function Parent() {
  const [count, setCount] = React.useState(0);

  const increment = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <Child1 count={count} />
      <Child2 increment={increment} />
      <Child3 count={count} />
    </div>
  );
}

const reactRoot = ReactDOM.createRoot(document.getElementById("root"));
reactRoot.render(<Parent />);
```

**Concept :** 

Now, imagine the Parent has more than one Child – they are siblings. If these siblings need to share information, they can't do it directly. Instead, they ask the Parent to be the messenger. The Parent holds the information and passes it to each Child as needed.

**Example :** 

 There are three siblings: 

- Child1 shows the `count`
- Child2 has a button to increase the `count`
- Child3 tells if the `count` is an odd or even number.

The Parent keeps the `count` and shares it with all three children.

![sibling-to-sibling.png](Data%20sharing%20between%20components%203bc994c916c54c1f981a5f5cf0efe7a7/sibling-to-sibling.png)