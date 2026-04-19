# Conditional Rendering and Conditional Styling

Serial: 8
Made for: Beginner
Requirement: Must Have
Time in minutes: 10
Learning Objectives: Conditional Rendering, Styling in React
doc-id: react-8

# Conditional Rendering :

Conditional rendering in React is a concept that allows you to display content based on certain conditions.

Let’s take a simple example : 

Imagine your `App` component has two `LightBulb` component. You pass a prop `“on”` which is a boolean value to this `LightBulb` component. The `LightBulb` will render `Bulb is on` or `Bulb is off` based on this prop

That means we are conditionally rendering `Bulb is on` or `Bulb is off` depending on prop `“on”` 

Approach 1 : 

```jsx
function LightBulb(props) {
  if (props.on) {
    return <div>Bulb is on</div>;
  } else {
    return <div>Bulb is off</div>;
  }
}

function App() {
  return (
    <>
      <LightBulb on={true} />
      <LightBulb on={false} />
    </>
  );
}
const reactRoot = ReactDOM.createRoot(document.getElementById("root"));

reactRoot.render(<App />);
```

Approach 2 : 

```jsx
function LightBulb(props) {
  return <div>Bulb is {props.on ? "on" : "off"}</div>;
}

function App() {
  return (
    <>
      <LightBulb on={true} />
      <LightBulb on={false} />
    </>
  );
}
const reactRoot = ReactDOM.createRoot(document.getElementById("root"));

reactRoot.render(<App />);
```

# Conditional Styling :

Based on certain condition; The styling is updated. 

```jsx
function LightBulb(props) {
  const styleObject = {
    backgroundColor: props.on ? "black" : "white",
    color: props.on ? "white" : "black",
    padding: "20px",
    border: `1px solid black`,
  };

  return <div style={styleObject}>Bulb is {props.on ? "on" : "off"}</div>;
}

function App() {
  return (
    <>
      <LightBulb on={true} />
      <LightBulb on={false} />
    </>
  );
}
const reactRoot = ReactDOM.createRoot(document.getElementById("root"));

reactRoot.render(<App />);
```

---

### Another example :

```jsx
const SuperheroDetails = ({
  name,
  hobbies,
  hasSuperPowers,
  isMarried,
  address,
  age,
}) => {
  return (
    <div className="card">
      <p>Name : {name}</p>
      {hobbies.length > 0 ? (
        <p>Hobbies : {hobbies.join(", ")}</p>
      ) : (
        <p>No hobbies</p>
      )}
      {/*
              <p>Has Super Powers : {hasSuperPowers ? "Yes" : "No"}</p>
            */}
      <p>
        Has Super Powers :{" "}
        <span style={{ color: hasSuperPowers ? "green" : "red" }}>
          {hasSuperPowers ? "Yes" : "No"}
        </span>
      </p>
      <div>
        <p>Street : {address.street}</p>
        <p>City : {address.city}</p>
        <p>Country : {address.country}</p>
      </div>
      <p>Age : {age}</p>
    </div>
  );
};

const App = () => {
  return (
    <div className="container">
      <SuperheroDetails
        name="Batman"
        hobbies={["Driving fancy cars", "Fighting crime"]}
        hasSuperPowers={false}
        address={{ street: "3rd Main", city: "Gotham", country: "USA" }}
        age={25}
      />
      <SuperheroDetails
        name="Superman"
        hobbies={["Flying", "Collecting coins"]}
        hasSuperPowers={true}
        address={{
          street: "4th Cross",
          city: "Central city",
          country: "USA",
        }}
        age={30}
      />
    </div>
  );
};

const reactRoot = ReactDOM.createRoot(document.getElementById("root"));

reactRoot.render(<App />);
```

Ever wondered how to show or hide something based on a condition? Here, we'll look at how you can conditionally render elements in React.

Let's say you want to display hobbies only if the superhero has some. Look at this part:

```jsx
{hobbies.length > 0 ? (
  <p>Hobbies : {hobbies.join(", ")}</p>
) : (
  <p>No hobbies</p>
)}
```

This is called a ternary operator. It checks if `hobbies.length > 0`. If it's true, it renders the superhero's hobbies; if false, it shows "No hobbies".

### 🔵 **Conditional Styling of Elements**

Now let's add a bit of style. You might want to visually highlight if a superhero has superpowers. Check out this code snippet:

```jsx
<p>Has Super Powers: {hasSuperPowers ? "Yes" : "No"}</p>
```

Want to make it colorful? You can conditionally add inline styles like this:

```jsx
<p>
  Has Super Powers:
  <span style={{ color: hasSuperPowers ? 'green' : 'red' }}>
    {hasSuperPowers ? "Yes" : "No"}
  </span>
</p>
```

In this snippet, the text will be green if `hasSuperPowers` is true; otherwise, it will be red.