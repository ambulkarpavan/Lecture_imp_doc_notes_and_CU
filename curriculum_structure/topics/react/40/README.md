# Props Drilling

Serial: 37
Made for: Beginner
Requirement: Must Have
Time in minutes: 25
Learning Objectives: Context API, Props Drilling
Related back to React: Context API - I : Basics (Context%20API%20-%20I%20Basics%2078868d787f104162b79d8c0daa093e37.md)
doc-id: react-37

@Abdul Jabbar Peer - Add the github code snippets here

# Props Drilling :

Let's say you have an app where you're tracking whether a user is logged in or not. You might store that data in the state of your top-level `<App />` component like so : 

Imagine your component tree look something like this.  If the component say `BottomMainRight` requires this `isLoggedIn`, it has to pass through components. There are chances that some of these component in between doesn’t even require this value `isLoggedIn` but you are still passing so that it can be further passed down to `BottomMainRight`

![Screenshot 2023-12-29 at 4.39.55 PM.png](Props%20Drilling%20774295057c2f4ebeb0bf7261a4d47c10/Screenshot_2023-12-29_at_4.39.55_PM.png)

This passing down of information is called props drilling.

See what's happening here? Every time a deeply nested component needs access to some "global" data, you have to pass it down, level by level. This gets messy, fast. Imagine if you had like 10 nested components! Not cool, right?
The problem with props drilling

1. Reusability takes a toll. Can’t reuse some of the components as it’s not generic anymore.
2. Possibility of missing to pass props. That can lead to issues

Is there a better way ? 

Context API

**In a nutshell :**

### 1. Props Drilling

- **Concept**: Props drilling is the practice of passing data from a parent component through various levels of nested child components.
- **Problem**: This method becomes cumbersome and inefficient as the component tree grows deeper, leading to reduced reusability and the risk of missing props.

### 2. Context API

- **Solution**: The Context API is React's answer to the props drilling problem.