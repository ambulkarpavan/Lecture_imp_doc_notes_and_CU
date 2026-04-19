# Typescript React + Context API

You can also use TypeScript with more complex React features like context or reducers. Here's a brief example of how you might type a context:

```jsx
import React, { createContext, useContext } from 'react';

type Theme = 'light' | 'dark';
type ThemeContextType = {
  theme: Theme;
  toggleTheme: () => void;
};

const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

export const useTheme = () => {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within a ThemeProvider');
  }
  return context;
};

// ... ThemeProvider component definition
```