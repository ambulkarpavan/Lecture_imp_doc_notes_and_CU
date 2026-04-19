# Context API - I : Basics

Serial: 38
Made for: Beginner
Requirement: Must Have
Time in minutes: 30
Dependant on: Props Drilling (Props%20Drilling%20774295057c2f4ebeb0bf7261a4d47c10.md)
Learning Objectives: Context API, Props Drilling
Related back to React: Context API - II : Intermediate (Context%20API%20-%20II%20Intermediate%2032cea13e9c534bf2acb938dc57c9b2d4.md)
doc-id: react-38

@Abdul Jabbar Peer - Add the github code snippets here

# Context API :

Context API basically provides a way to pass data through the component tree without having to pass props down manually at every level.

Let’s learn how to setup and use Context API by building a simple application which manages login state.  We'll create a context to manage the `isLoggedIn` state and use it across various components without props drilling.

Setup is pretty simple and straight forward and you can remember by ***CPC ( Create - Provide - Consume ) .***

### Step 1: Create Context

- **Purpose**: Create a React Context to hold global data.
- **Implementation**:
    
    ```jsx
    export const AuthContext = React.createContext();
    ```
    

### Step 2: Provide

- **Purpose**: Make the context available to components.
- **Implementation**:
    
    ```jsx
    export function AuthContextProvider({ children }) {
      const [isLoggedIn, setIsLoggedIn] = React.useState(false);
      // 2.A
    	return (
        <AuthContext.Provider value={{ isLoggedIn }}>
          {children}
        </AuthContext.Provider>
      );
    }
    
    ```
    
    main.jsx
    
    ```jsx
    import ReactDOM from "react-dom/client";
    import App from "./App.jsx";
    import { AuthContextProvider } from "./context/AuthContextProvider.jsx";
    
    ReactDOM.createRoot(document.getElementById("root")).render(
      //// 2.B. Provide Context
      <AuthContextProvider>
        <App />
      </AuthContextProvider>
    );
    ```
    

### Step 3: Consume

- **Purpose**: Utilize the context data in components.
- **Implementation**:
    
    ```jsx
    function BottomMainLeft() {
      const { isLoggedIn } = React.useContext(AuthContext);
      // Component code
    }
    ```
    

Do check out your React DevTools. You'll see the `Provider` components wrapping around your app components, and you'll see the context values there as well. Super handy for debugging!

And that's it! The Context API is a killer feature to keep your codebase clean and simple. 

Now that we got an idea let’s build an application using context API.

A visual to understand How data flows when you use context API

![Screenshot 2023-12-29 at 5.37.45 PM.png](Context%20API%20-%20I%20Basics%2078868d787f104162b79d8c0daa093e37/Screenshot_2023-12-29_at_5.37.45_PM.png)

### Real world examples :

When do we generally use Context API in everyday development

- A common scenario is managing user authentication state (like `isLoggedIn`) across multiple components.
- Or it could be to store and manage the current theme of your application using Context API
- Some libraries uses context API to manage routing in react ( e.g., react-router-dom )

### Benefits :

1. **Simplified Data Flow**: Eliminates the need for passing props through every level.
2. **Enhanced Reusability**: Components become more generic and reusable.
3. **Improved Code Maintenance**: Easier to track and debug data flow in the application.