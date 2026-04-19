# forwardRef

### This component will demonstrate how to enforce the types of props, utilize default props if required, and manage state across multiple input boxes, including handling focus shifts and paste events.

### Case 1: Basic Prop Type Checks

### App.jsx

```jsx
import InputBoxes from "./components/InputBoxes";
import "./styles.css";

export default function App() {
  return (
    <div className="App">
      <InputBoxes length={4} label="Input boxes" />
    </div>
  );
}

```

### InputBoxes.jsx

```jsx
import PropTypes from "prop-types";

function InputBoxes({ length, label }) {
  return <>{label}</>;
}

InputBoxes.propTypes = {
  length: PropTypes.number,
  label: PropTypes.string
};

export default InputBoxes;

```

In this setup, passing `length="some string"` would log a warning in the console, indicating that `length` is expected to be a number.

### Case 2: Making a Prop Mandatory and Setting Default Props

### App.jsx

```jsx
import InputBoxes from "./components/InputBoxes";
import "./styles.css";

export default function App() {
  return (
    <div className="App">
      <InputBoxes label="Input boxes" />
    </div>
  );
}

```

### InputBoxes.jsx

```jsx
import PropTypes from "prop-types";

function InputBoxes({ length, label }) {
  return <>{label}</>;
}

InputBoxes.propTypes = {
  length: PropTypes.number.isRequired,
  label: PropTypes.string
};

InputBoxes.defaultProps = {
  length: 2
};

export default InputBoxes;

```

Here, if the `length` prop is not passed, React will log an error in the console because it's marked as `isRequired`. However, the component will still work, and `length` will default to 2, as specified in `defaultProps`.

### Case 3 : useRef and forwardRef

Let's build upon the `InputBoxes` component to handle individual input boxes (`PinItem`), manage their values, handle focus shift, and process paste events.

### App.jsx

```jsx
import InputBoxes from "./components/InputBoxes";
import "./styles.css";

export default function App() {
  return (
    <div className="App">
      <InputBoxes length={4} label="Input boxes" perBox={1} />
    </div>
  );
}

```

### InputBoxes.jsx

```jsx
import PropTypes from "prop-types";
import { useState, useRef } from "react";
import PinItem from "./PinItem";

function InputBoxes({ length, label, perBox }) {
  const [values, setValues] = useState(new Array(length).fill(""));
  const ref = useRef(new Array(length).fill(0).map(() => React.createRef()));

  const handleChange = (value, index) => {
    const newValues = [...values];
    newValues[index] = value;
    setValues(newValues);

    if (value.length >= perBox && index < length - 1) {
      ref.current[index + 1].current.focus();
    }
  };

  return (
    <>
      <h1>{label}</h1>
      {values.map((item, index) => (
        <PinItem
          key={index}
          max={perBox}
          ref={ref.current[index]}
          value={values[index]}
          onChange={(e) => handleChange(e.target.value, index)}
        />
      ))}
    </>
  );
}

InputBoxes.propTypes = {
  length: PropTypes.number.isRequired,
  label: PropTypes.string,
  perBox: PropTypes.number
};

InputBoxes.defaultProps = {
  length: 2,
  perBox: 1
};

export default InputBoxes;

```

### PinItem.jsx

```jsx
import { forwardRef } from "react";
import PropTypes from "prop-types";

const PinItem = forwardRef(({ max, onChange, value }, ref) => {
  return (
    <input
      type="text"
      maxLength={max}
      onChange={onChange}
      value={value}
      ref={ref}
      style={{ width: "30px", padding: "10px", margin: "5px" }}
    />
  );
});

PinItem.propTypes = {
  max: PropTypes.number,
  onChange: PropTypes.func.isRequired,
  value: PropTypes.string
};

export default PinItem;
```

In this example, `InputBoxes` manages an array of values and passes individual values and change handlers to each `PinItem`. `PinItem` is a controlled component, receiving its current value and a change handler from its parent. This setup allows `InputBoxes` to control the focus and input values of each `PinItem`, making it a versatile and reusable component for handling multiple input boxes in a form.

This example demonstrates how to create generic components in React using prop types for validation and default props for fallback values. The `InputBoxes` component is modular and handles complex interactions like focus management and input handling, making it a powerful building block for React applications.