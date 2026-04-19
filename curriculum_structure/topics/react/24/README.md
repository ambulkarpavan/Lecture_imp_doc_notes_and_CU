# Lifecycle of a React Component

Serial: 26
Made for: Beginner
Requirement: Must Have
Time in minutes: 10
Learning Objectives: React Component Lifecycle, effects and useEffect
doc-id: react-26

# Component Lifecycle in React :

React components follow a lifecycle, which is a series of events from the moment they are created and mounted on the UI to the moment they are removed from the UI. 

### Different phases/events of component’s lifecycle :

Similar to a person’s lifecycle; A component’s lifecycle also has 3 phases 

1. **Birth (Mount Phase)**: The component is created and rendered on the UI for the first time.
2. **Life (Update Phase)** :  Occurs when a component's state or props change, leading to re-rendering.
3. **Death (Unmount Phase)**: The component is removed from the UI.

So these are basically events. mount event, update event and unmount event. 

### Event and Event Handlers  ( A Quick Recap ) :

Events in React, like in JavaScript, trigger certain actions (event handlers). 

For instance, 

```jsx
window.addEventListener('load', function() {...}) //  This is an event that triggers when the window loads.
// Event --> load
// Event Handler --> the function
```

```jsx
let someButton = document.createElement('button')
someButton.addEventListener('click',() => {
	// what should happen when the button is clicked
})
// Event --> click
// Event Handler --> the function here
```