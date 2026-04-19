# Context API - II : Intermediate

Serial: 39
Made for: Beginner
Requirement: Must Have
Time in minutes: 30
Dependant on: Context API - I : Basics (Context%20API%20-%20I%20Basics%2078868d787f104162b79d8c0daa093e37.md)
Learning Objectives: Context API, Props Drilling
doc-id: react-39

@Abdul Jabbar Peer - Include source code as well here

Our project includes two context providers: `AuthContextProvider` and `ThemeContextProvider`. We'll use these to illustrate how to work with multiple contexts.

The Context API in React allows for managing global application states without prop drilling. In our project, we have two contexts - Authentication (`AuthContext`) and Theme (`ThemeContext`), which are essential for many applications.

### Step 1: Creating Contexts

1. **AuthContext**: Manages user authentication status.
    - In `AuthContextProvider.jsx`, create a context using `React.createContext()`.
    - Define state to track user authentication status.
2. **ThemeContext**: Manages the application's theme.
    - Similar to `AuthContextProvider`, create a `ThemeContext` in `ThemeContextProvider.jsx`.
    - Include state for theme data (like dark or light mode).

### Step 2: Providing Contexts

- In `App.jsx`, wrap your component tree with both `AuthContextProvider` and `ThemeContextProvider`.
    
    ```jsx
    <AuthContextProvider>
      <ThemeContextProvider>
        {/* Rest of your app components */}
      </ThemeContextProvider>
    </AuthContextProvider>
    
    ```
    

### Step 3: Consuming Contexts in Components

- To use contexts in components like `Navbar`, `Main`, or `Footer`:
    - Import the contexts.
    - Use the `useContext` hook to access the context values.
    - For example, in `Navbar.jsx`, to access the theme, `const theme = useContext(ThemeContext)`.

### Step 4: Updating Context Values

- Context values can be updated using setters provided in the respective context providers.
- For instance, if you want to change the theme in `BottomMainRight.jsx`:
    - Access the setter function from `ThemeContext`.
    - Update the theme on a specific action like a button click.

### Step 5: Best Practices

- Keep context values as minimal as possible to avoid unnecessary re-renders.
- Use `useMemo` or `useCallback` for optimization if context values are computation-heavy.

Using multiple contexts in React helps in efficiently managing different global states like user authentication and application themes. This approach enhances scalability and maintainability of your React application.

Visual :

![Screenshot 2023-12-29 at 6.53.35 PM.png](Context%20API%20-%20II%20Intermediate%2032cea13e9c534bf2acb938dc57c9b2d4/Screenshot_2023-12-29_at_6.53.35_PM.png)