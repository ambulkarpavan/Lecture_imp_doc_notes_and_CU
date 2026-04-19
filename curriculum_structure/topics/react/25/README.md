# Children Props

Serial: 7
Made for: Beginner
Requirement: Must Have
Time in minutes: 25
Learning Objectives: Components, Props
doc-id: react-7

# Children props in React Component :

"Children props in React Component" refers to a special prop in React, called `children`, which allows you to pass components as data to other components. This prop is a key concept in React's compositional model, where smaller components are composed together to build more complex UIs.

In React, any JSX elements you place between the opening and closing tags of a component are passed to it as `children` props. This allows components to define their structure with placeholders for any children elements to be defined later.

When you nest content inside a JSX tag, the parent component will receive that content in a prop called `children`. For example, the `Card` component below will receive a `children` prop set to `<Avatar />` and render it in a wrapper div:

```jsx
import "./styles.css";

function Card(props) {
  console.log(props);
  return (
    <div style={{ padding: "10px", border: `5px solid ${props.borderColor}` }}>
      {props.children}
    </div>
  );
}

function Avatar() {
  return (
    <div>
      <img
        src="https://i.pinimg.com/564x/f0/14/b4/f014b482978c37f0e12ea9db8f37a264.jpg"
        alt="batman"
        width={200}
      />
      <p>Batman</p>
    </div>
  );
}

export default function App() {
  return (
    <div className="App">
      <Card borderColor="black">
        <Avatar />
      </Card>
    </div>
  );
}
```

Try replacing the `<Avatar>` inside `<Card>` with some text to see how the `Card` component can wrap any nested content. It doesn’t need to “know” what’s being rendered inside of it. You will see this flexible pattern in many places.

You can think of a component with a `children` prop as having a “hole” that can be “filled in” by its parent components with arbitrary JSX. You will often use the `children` prop for visual wrappers: panels, grids, etc.

## Use-case & Benefits

The children prop is useful for creating reusable and dynamic components. For instance, a `Modal` component can be designed to accept any content as children, making it versatile for various scenarios.

Consider a `List` component. Without children props, you'd need to create a specific List for every type of item. With children props, you can create one List component and pass different items as children.

## Real world Examples

In real-world programming, a `Container` component could be used to apply consistent padding and margin around its children. Whether it's a form, a paragraph, or an image, the `Container` ensures consistent spacing.

## Usage

- `children`: This is a prop that contains any elements included between the opening and closing tags of a component. It can be used to dynamically render content inside a component.

Example:

```jsx
function Container({ children }) {
  return <div className="container">{children}</div>;
}

<Container>
  <p>This is a child paragraph</p>
</Container>

```

## Instructor Activity

Problem: Create a `PageLayout` component that takes a header, content, and footer as children and renders them in a structured layout.

Solution:

1. Define `PageLayout` with a `children` prop.
2. Use the `children` prop to render the passed elements.
3. Use the component by passing different elements as children.

```jsx
function PageLayout({ children }) {
  return <div className="page-layout">{children}</div>;
}

<PageLayout>
  <Header />
  <MainContent />
  <Footer />
</PageLayout>

```

## Learners Activity

Problem: Create a `Gallery` component that can display any number of `Image` components passed as children.

Step-by-Step:

1. Define `Gallery` with a `children` prop.
2. Render `children` within a grid layout.
3. Use `Gallery` by passing multiple `Image` components.

Solution:

```jsx
function Gallery({ children }) {
  return <div className="gallery-grid">{children}</div>;
}

<Gallery>
  <Image src="image1.jpg" />
  <Image src="image2.jpg" />
  // Add as many images as needed
</Gallery>

```

This approach demonstrates the power of composition in React, where `children` props allow for flexible and reusable components.