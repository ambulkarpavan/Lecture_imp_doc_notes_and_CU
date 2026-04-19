# Higher order component

# Introduction

Higher-Order Components (HOCs) are an advanced pattern in React for reusing component logic. They are not part of the React API, per se, but are a pattern that emerges from React's compositional nature. Essentially, a HOC is a function that takes a component and returns a new component.

# Detailed Explanation

A Higher-Order Component (HOC) in React is essentially a function that takes a component and returns a new component with additional props or behaviors. The pattern is derived from higher-order functions in JavaScript, which are functions that can take functions as arguments or return functions.

The typical signature of a HOC looks like this:

```jsx
const EnhancedComponent = higherOrderComponent(WrappedComponent);
```

Here, `WrappedComponent` is the component you want to wrap with additional functionalities, and `EnhancedComponent` is the new component returned by the HOC, enriched with new props or behaviors.

# Use-case & Benefits

1. **Code Reusability**: HOCs abstract shared logic between components, promoting code reusability and separation of concerns.
2. **Prop Manipulation**: HOCs can manipulate props before passing them to the wrapped component, which is useful for injecting new props or modifying existing ones.
3. **State Abstraction and Manipulation**: HOCs can also manage state and introduce new behavior, encapsulating interactions with a global state or APIs.
4. **Conditional Rendering**: HOCs can decide to render the wrapped component or something else (like a loading indicator) based on certain conditions.

# Real-World Examples

- **With Authentication**: A common use case for HOCs is to create a protected route component that checks if a user is authenticated before rendering the component.
- **With Loading**: You can create an HOC that displays a loading spinner while data is being fetched and then renders the component with the fetched data.

# Usage in Functional Components

With the introduction of React Hooks, you might wonder whether HOCs are still relevant. Hooks provide a way to use state and other React features without writing a class, thus simplifying the component logic and management. Here’s how the landscape looks:

1. **React Hooks**: They offer a more straightforward way to handle state and side effects in functional components. For many use cases where HOCs were used, like managing state or lifecycle methods, hooks provide a cleaner and more intuitive solution.
2. **Context API**: For sharing state across many components, the modern Context API is more favored. It reduces the need for prop drilling, which was another common use case for HOCs.

### Is HOC Still Required for Functional Components?

While HOCs are not as prevalent as before due to Hooks and Context API, they are not obsolete. They are still useful in scenarios where you want to abstract or modify component behavior across multiple components in your application.

1. **Composition vs. Custom Hooks**: Even though custom hooks can encapsulate logic, they don't wrap components. HOCs, on the other hand, can wrap components and modify props, behavior, and render output, providing a level of composition that hooks don't.
2. **Third-Party Libraries**: Many third-party libraries still use HOCs. Until these libraries migrate to hooks or other patterns, HOCs will remain in use.
3. **Legacy Codebases**: In legacy projects, refactoring all HOCs to use hooks might not be feasible or necessary, especially if the HOCs are stable and well-tested.

# Instructor Activity / Code Example

Approach 1 : Let's build a simple HOC that provides a loading spinner while data is being fetched:

```jsx
// withLoading.js
import React from 'react';

const withLoading = (WrappedComponent) => {
  return class extends React.Component {
    render() {
      if (this.props.isLoading) {
        return <div>Loading...</div>;
      }
      return <WrappedComponent {...this.props} />;
    }
  };
};

export default withLoading;
```

Usage:

```jsx
import withLoading from './withLoading';
import MyComponent from './MyComponent';

const MyComponentWithLoading = withLoading(MyComponent);

// Use MyComponentWithLoading and pass isLoading prop
<MyComponentWithLoading isLoading={dataFetchingStatus} />
```

Approach 2 : It's not mandatory to use class components when working with Higher-Order Components (HOCs). You can certainly implement HOCs using functional components, especially with the advent of React Hooks which provide a more functional approach to handling state and side effects. Let's refactor the **`withLoading`** HOC example to use a functional component instead:

```jsx
// withLoading.js
import React from 'react';

const withLoading = (WrappedComponent) => {
  const WithLoadingComponent = (props) => {
    if (props.isLoading) {
      return <div>Loading...</div>;
    }
    return <WrappedComponent {...props} />;
  };

  return WithLoadingComponent;
};

export default withLoading;
```

```jsx
import withLoading from './withLoading';
import MyComponent from './MyComponent';

const MyComponentWithLoading = withLoading(MyComponent);

// Use MyComponentWithLoading and pass isLoading prop
<MyComponentWithLoading isLoading={dataFetchingStatus} />
```

In this refactored example, **`withLoading`** is still a Higher-Order Component that takes a **`WrappedComponent`** and returns a new component. However, instead of returning a class, it returns a functional component **`WithLoadingComponent`**. This functional component checks the **`isLoading`** prop, and based on its value, it either renders a loading indicator or the **`WrappedComponent`** with the passed props.

# Learner Activity

1. **Create a HOC**: Write a HOC named `withUserData` that fetches user data from an API and passes it to the wrapped component as a prop named `userData`.
2. **Implement a Loading Indicator**: Enhance the `withUserData` HOC to show a loading indicator while the data is being fetched.

### Learner Activity Solution

```jsx
// withUserData.js
import React, { useState, useEffect } from 'react';

const withUserData = (WrappedComponent) => {
  return (props) => {
    const [userData, setUserData] = useState(null);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
      const fetchData = async () => {
        try {
          const response = await fetch('<https://api.example.com/user>');
          const data = await response.json();
          setUserData(data);
        } catch (error) {
          console.error(error);
        } finally {
          setIsLoading(false);
        }
      };

      fetchData();
    }, []);

    if (isLoading) {
      return <div>Loading user data...</div>;
    }

    return <WrappedComponent {...props} userData={userData} />;
  };
};

export default withUserData;

```

In this lesson, we explored the concept of Higher-Order Components in React, their relevance, and the alternatives provided by modern features like Hooks and the Context API. HOCs, while not as predominant as before, still have their place in specific scenarios, especially concerning component composition and behavior abstraction.