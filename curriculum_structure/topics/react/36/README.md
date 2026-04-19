# useRef - II ( Intermediate )

Serial: 36
Made for: Beginner
Requirement: Good to Have
Time in minutes: 30
Dependant on: useRef - I ( Basics ) (useRef%20-%20I%20(%20Basics%20)%20d68e93113d644115a5b8f733e250b4a4.md)
Learning Objectives: ref and useRef
doc-id: react-36

## `useRef` to access DOM elements - Some Additional Examples :

### Example 1 :

1. `useRef` hook allows you to keep a mutable value in it’s `.current` property
2. Create an application wherein you add video element. You do know that can access DOM nodes with `useRef` hook. So here in the application as well, please access video DOM notes using this hook `useRef`like this
    
    ```markdown
    const videoRef = useRef(null)
    <video ref={videoRef}></video>
    ```
    
    this will set the `.current`property of `videoRef`to video DOM node
    
3. Now you’ll create two buttons `PLAY` and `PAUSE` . clicking on `PLAY` button will call `onPlay` event handler. Similarly clicking on `PAUSE` button will call `onPause` event handler.  This event handler `onPlay` and `onPause` will play and pause the video ( This you will do by accessing the video node and then [HTMLMediaElement: play() method](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/play)   and [HTMLMediaElement: pause() method](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/pause) method )

Code :

![Snap (2).png](useRef%20-%20II%20(%20Intermediate%20)%20e862c25b7d024f419c6dc46e4cee3dd7/Snap_(2).png)

---

### Example 2 :

**useRef with callback refs :**

This is also a valid syntax wherein we use callback syntax inside useRef ( These are useful where you want to have bunch of element ; like bunch of input boxes used for Pin Component )

Syntax : 

```jsx
const ref = useRef(null)
```

```jsx
<input ref={ currentElement => ref.current = currentElement }/>
```

PinComponent.jsx

```jsx
import { useRef } from "react";

function PinComponent() {
  let inputRef = useRef([]);

  console.log(inputRef);
  // { current : [ input#1, input#2, input#3, input#4] }
  return (
    <div>
      <input
        style={{ width: "20px" }}
        id="1"
        ref={(elem) => {
          // elem --> input
          inputRef.current[0] = elem;
        }}
      />
      <input
        style={{ width: "20px" }}
        id="2"
        ref={(elem) => {
          // elem --> input
          inputRef.current[1] = elem;
        }}
      />
      <input
        style={{ width: "20px" }}
        id="3"
        ref={(elem) => {
          // elem --> input
          inputRef.current[2] = elem;
        }}
      />
      <input
        style={{ width: "20px" }}
        id="4"
        ref={(elem) => {
          // elem --> input
          inputRef.current[3] = elem;
        }}
      />
    </div>
  );
}

export default PinComponent;
```

---

## useRef for **Storing Instance Variables :**

The same Timer component that was done in the previous section can be made better by these little modifications

```jsx
import { useEffect, useState, useRef } from "react";

function fixtimeString(num) {
  return num <= 9 ? `0${num}` : `${num}`;
}

const formatTime = (timeInSecs) => {
  const seconds = timeInSecs % 60;
  const minutes = Math.floor(timeInSecs / 60) % 60;
  const hours = Math.floor(timeInSecs / 3600);
  return `${fixtimeString(hours)}:${fixtimeString(minutes)}:${fixtimeString(
    seconds
  )}`;
};

function Timer() {
  const [count, setCount] = useState(240);
  const intervalRef = useRef(null);

  useEffect(() => {
    const cleanup = () => {
      stopTimer();
    };
    return cleanup;
  }, []);
 
  const startTimer = () => {
    if (intervalRef.current !== null) {
      console.log(`timer is already running`);
      return;
    }
    intervalRef.current = setInterval(() => {
      console.log(`timer running`, Date.now());
      setCount((prevCount) => {
        if (prevCount <= 1) {
          clearInterval(intervalRef.current);
        }
        return prevCount - 1;
      });
    }, 1000);
  };

  const stopTimer = () => {
    console.log(`timer stopped`);
    clearInterval(intervalRef.current);
    intervalRef.current = null;
  };

  const resetTimer = () => {
    stopTimer();
    setCount(240);
  };

  return (
    <div>
      <h6>{formatTime(count)} </h6>
      <button onClick={startTimer}>START</button>
      <button onClick={stopTimer}>STOP</button>
      <button onClick={resetTimer}>RESET</button>
    </div>
  );
}

export default Timer;
```