# Effects and useEffect - A quick revision

Serial: 34
Made for: Beginner
Requirement: Must Have
Time in minutes: 15
Learning Objectives: React Component Lifecycle, effects and useEffect
doc-id: react-34

These events are

1. **Mount** : This is when the component is created and attached( mounted ) to the UI. This stage includes creation of component and the rendering of its initial state and props
2. **Update** : This is when the component is updated based on the change in it’s state or prop. component re-renders in this stage with updated state/props values
3. **Unmount** : This is when the component is removed from the UI. This stage includes any cleanup that needs to happen before the component is removed. 

React provides some ways/methods.These are called lifecycle Methods and are special methods  that gets called at each of these component’s lifecycle. Now these methods allows us to control what happens during 

1. the mount phase/event.
2. the update phase/event.
3. the unmount phase/event.

Basically you use `useEffect` for this :   All side effects that needs to be performed during mount, update and unmount phase will be done using the useEffect with arguments passed

**useEffect Syntax :**

```jsx
useEffect( callbackFunction, dependancyArray )
useEffect(()=>{
	
},[])
```

This dependencyArray will decide whether the callback should be called

1. only once when the component gets mounted onto UI
2. all the time when the component renders and re-renders
3. only when certain thing changes
4. I want to perform some side effect during the initial render ( as soon as the component mount ) or also called mount phase/event.
    
    ```jsx
    // This will run the callback function inside useEffect 
    	// 1. During the mount phase ( initial render )
    useEffect(() => {
       // Called during the mount phase
      }, []) // You'd keep the dependancy array empty
    ```
    

1. I want to perform some side effect during the update phase
    
    
    ```jsx
    // This will run the callback function inside useEffect 
    	// 1. During the mount phase ( inital render )
    	// 2. During the update phase ( whenever the component re-renders due to change in any variable ). Not so ideal
    
    useEffect(() => {
        // called everytime
      }) // No dependancy array is passed here
    ```
    
    ```jsx
    // This will run the callback function inside useEffect 
    	// 1. During the mount phase ( inital render )
    	// 2. During the update phase. whenever the variable inside dependancy array is updated 
    useEffect(() => {
       // called during mount phase and when dependancyVariable changes
      },[dependancyVariable]) // dependancy array with dependancyVariable is passed here
    ```
    
2. I want to remove all the effects / Side effects that were performed during the mount and update phase. Cleanup functions help you with that. They are called when the component unmounts and prevents any memory leaks
    
    ```jsx
    useEffect(() => {
      const intervalId = setInterval(() => {
        console.log(`this code runs every 1 second`, Date.now())
      }, 1000)
    
      // Cleanup function
      return () => {
        clearInterval(intervalId);
      };
    }, [])
    
    ```
    
3. These cleanups are also called before the next update as well.