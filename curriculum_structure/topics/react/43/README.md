# Routing - NotFound Page

Serial: 43
Made for: Beginner
Requirement: Must Have
Time in minutes: 5
Dependant on: Routing - Introduction, Installation & Setup,BrowserRouter, Routes, Route and Link (Routing%20-%20Introduction,%20Installation%20&%20Setup,Brows%202b38a28f30a34da596f1926ad5e7824f.md)
Learning Objectives: Routing Basics
doc-id: react-43

# Routing - NotFound Page :

Page to show when none of the route matches

```jsx
// src/pages/NotFound.jsx
function NotFound() {
  return (
    <>
      <h1>Page Not Found</h1>
    </>
  );
}

export default NotFound;
```

```jsx
// src/components/AllRoutes.jsx
import { Routes, Route } from "react-router-dom";
import NotFound from "../pages/NotFound";

function AllRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
	     ... All Other Routes...
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
}

export default AllRoutes;
```