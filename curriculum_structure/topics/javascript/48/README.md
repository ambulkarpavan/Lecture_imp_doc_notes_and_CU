# Events handlers [60 min] (1)

Event handlers allow you to react when certain things (an event) happen to the page on an element on the page.

There are many different types of events that can occur. For example:

- The user selects a certain element or hovers the cursor over a certain element.
- The user chooses a key on the keyboard.
- The user resizes or closes the browser window.
- A web page finishes loading.
- A form is submitted.
- A video is played, paused, or finished.
- An error occurs.

A comprehensive list of events can be found here:  [https://developer.mozilla.org/en-US/docs/Web/Events](https://developer.mozilla.org/en-US/docs/Web/Events)

```html
<div class="box grandparent">
  grandparent
  <div class="box parent">
    parent
    <div class="box child">
      child
    </div>
  </div>
</div>
```

```css
.box {
  padding: 20px;
}

.grandparent {
  background-color: dodgerblue;
}

.parent {
  background-color: gold;
}

.child {
  background-color: aliceblue;
}
```

```css
let grandparent = document.querySelector(".grandparent");
let parent = document.querySelector(".parent");
let child = document.querySelector(".child");

grandparent.addEventListener('click', function (e) {
  console.log('Grandparent clicked 1');
  // console.log(e.target); 
  // the element on which the event actually happend
})

parent.addEventListener('click', function (e) {
  console.log('Parent clicked 1');
  // console.log(e.target); 
})

child.addEventListener('click', function (e) {
  console.log('child clicked 1');
  // console.log(e.target);
})
```

![Untitled](Events%20handlers%20%5B60%20min%5D%20(1)%20ba995d3ea14c4874b103fb3eb1ba3b3e/Untitled.png)

![Untitled](Events%20handlers%20%5B60%20min%5D%20(1)%20ba995d3ea14c4874b103fb3eb1ba3b3e/Untitled%201.png)

![Untitled](Events%20handlers%20%5B60%20min%5D%20(1)%20ba995d3ea14c4874b103fb3eb1ba3b3e/Untitled%202.png)

## Event Capturing vs Bubbling

![003_javascript_shorts.png](Events%20handlers%20%5B60%20min%5D%20(1)%20ba995d3ea14c4874b103fb3eb1ba3b3e/003_javascript_shorts.png)

When we clicked on the child, technically we also clicked on the parent and grandparent as the child is inside them. This process of event handling, going from the child out to its ancestors is called event **bubbling**.

When an event occurs on an element, it can propagate through the DOM tree in two phases: the capturing phase and the bubbling phase.

- **Capturing Phase:** During this phase, the event is captured from the root of the DOM tree down to the target element.
- **Bubbling Phase:** After the capturing phase, the event bubbles up from the target element back up to the root of the DOM tree.

By default, event listeners are set to listen in the bubbling phase, meaning that the innermost element's event listener is executed first, and then the event bubbles up to the outer elements, triggering their event listeners in order.

However, when you specify **`{capture: true}`** in an event listener, it changes the phase in which the event listener is triggered to the capturing phase.

We can prevent further bubbling or capturing of events using `e.stopPropagation()`

We can prevent further bubbling or capturing of events if there is more than one event present using `e.stopImmediatePropagation()`

As a third argument of the event listener, we can pass `{once: true}`, to immediately remove the listener after the first event.

`.removeEventListener()` can be used to remove a listener from an event.

```css
someFunction(){}

el.addEventListner('click', someFunction);
el.removeEventListener('click', someFunction);
```

### Event delegation using a global listener

```css
document.addEventListener("click", function (e) {
  if (e.target.matches(".box")) {
    console.log(e.target, 'I am clicked');
  }
})
```

difference between `e.stopPropagation()` and `e.preventDefault()`

### Listening to documents on load event

```jsx
window.onload = function() {
  console.log('Im loaded');
};
```