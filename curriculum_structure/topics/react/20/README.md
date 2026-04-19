# Forms in React

Serial: 21
Made for: Beginner
Requirement: Must Have
Time in minutes: 25
Learning Objectives: Forms in React, State Management, useState
doc-id: react-21

# Objectives :

1. Learn to create and handle forms in React.
2. Understand how to update objects in React's state.
3. Implement form submission and prevent default browser submission behavior.
4. Work with different types of input elements and their event handlers.

**Setting Up the Form Component and Integrating it to `App`**

- In your `src` directory, create a new folder called `components` and a  file named `FormComponent.jsx`. This component will contain our form.
- Export this FormComponent and import it to App component.

App.jsx

```jsx
import "./App.css";
import FormComponent from "./components/FormComponent";

function App() {
  return (
    <>
      <FormComponent />
    </>
  );
}

export default App;
```

FormComponent.jsx

```jsx
import { useState } from "react";

const FormComponent = () => {
  const [formState, setFormState] = useState({
    name: "",
    age: "",
    country: "United States",
    isMarried: false,
  });

  const handleInputChange = (e) => {
    const { name, value, type, checked } = e.target;

    const formInputValue =
      type === "checkbox" ? checked : type === "number" ? Number(value) : value;

    const newState = {
      ...formState,
      [name]: formInputValue,
    };

    setFormState(newState);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formState);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "20px",
          margin: "30px",
          padding: "20px",
          border: "1px solid black",
        }}
      >
        <input
          type="text"
          name="name"
          value={formState.name}
          onChange={handleInputChange}
          placeholder="Name"
        />
        <input
          type="number"
          name="age"
          value={formState.age}
          onChange={handleInputChange}
          placeholder="Age"
        />
        <select
          name="country"
          value={formState.country}
          onChange={handleInputChange}
        >
          <option value="">Select a country</option>
          <option value="India">India</option>
          <option value="China">China</option>
          <option value="Nepal">Nepal</option>
          <option value="USA">USA</option>
          <option value="UAE">UAE</option>
          <option value="UK">UK</option>
        </select>
        <label>
          Married:
          <input
            type="checkbox"
            name="isMarried"
            checked={formState.isMarried}
            onChange={handleInputChange}
          />
        </label>
        <button type="submit">Submit</button>
      </div>
    </form>
  );
};

export default FormComponent;
```

**Explanation of Key Concepts**

1. **Forms and Handle Submit** :
    - The `handleSubmit` function is triggered when the form is submitted.
    - `e.preventDefault()` is used to prevent the default form submission behavior, which refreshes the page.
2. **Updating Objects in React State** :
    - We maintain the form data in a single state object, `formState`. React's state can hold various types of data, including objects. However, when dealing with objects in state, it's crucial to understand the correct way to update them.
    - The `handleInputChange` function updates `formState` based on the input's `name` and `value`.
    - In the above example, You can observe that we did not mutate the state object directly ? Why ?
    
    **Why Not Mutate State Directly ?**
    
    In React, the state should be treated as immutable. This means you shouldn't directly modify (or mutate) the state object. For instance, doing something like `formState.name="bruce"` is a bad practice. Here’s why:
    
    1. **React's Re-rendering Mechanism**: React's re-rendering is triggered by a change in state or props. If you mutate the state directly, React won't be able to detect that there's been a change, leading to potential bugs and UI inconsistencies.
    2. **Maintaining Predictability**: Treating state as immutable leads to more predictable and easy-to-understand code, which is crucial in React's declarative nature.
    
    ### Correct Way to Update Object State
    
    When you want to update an object in the state, the best practice is to create a new object with the updated values. In the context of our form above, let’s see how this applies:
    
    ```jsx
      const handleInputChange = (e) => {
        const { name, value, type, checked } = e.target;
    
        const formInputValue =
          type === "checkbox" ? checked : type === "number" ? Number(value) : value;
    
    		// create a new object with the updated values
        const newState = {
          ...formState,
          [name]: formInputValue,
        };
    
        setFormState(newState); // set that newly created object as our latest state using setFormState function
      };
    ```
    
    **Key Takeaways**
    
    - **Creating a New Object**: The spread operator (`...`) is used to create a new object with the properties of the current state. This ensures we're not mutating the state directly.
    - **Updating the New Object**: After creating the new object, we update the relevant key with the new value.
    - **Setting the State**: Finally, we use the `setFormState` function to update the state with our new object.
    
    By following this approach, you ensure that React can accurately track state changes and update the UI accordingly. This practice leads to more robust and maintainable React applications.
    
3. **Prevent Default** :
    - `e.preventDefault()` in `handleSubmit` stops the browser's default form submission, allowing us to handle it within React.
4. **Different Input Elements and Their Event Handlers**:
    - **Text and Number Inputs**: These update the corresponding state properties directly. Based on the type we are updating string or number as value by applying our logic
    - **Select Box**: Reacts to changes and updates the `country` in the state.
    - **Checkbox**: Manages a boolean value; uses `checked` instead of `value`.

### Conclusion

This covers various input types and demonstrates how to handle form data in React. You've learned how to update state objects, prevent default form submission, and use different event handlers for various input types. Experiment with this setup to deepen your understanding of forms in React.