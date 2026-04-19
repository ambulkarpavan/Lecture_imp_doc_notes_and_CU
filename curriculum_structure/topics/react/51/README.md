# Chakra UI

Serial: 53

# Introduction to Chakra UI

Chakra UI is a modern, React-based library that offers a range of accessible, reusable, and composable UI components. It's designed to be simple and modular, allowing developers, especially beginners, to build beautiful, responsive websites with ease. Chakra UI stands out for its simplicity and focus on productivity, making it an excellent choice for those new to web development.

Some important basics to be cover

1. Setting up Chakra UI in a react project
2. Topics
    1. Components in Chakra UI
    2. Style Props and Responsiveness
    3. Hooks in Chakra UI
    4. How to customise theme in Chakra UI

## Setup in a React Project Created with VITE

1. **Creating a New VITE Project**:
If you haven't already, start by creating a new React project using VITE:
    
    ```bash
    npm create vite@latest my-chakra-app -- --template react
    cd my-chakra-app
    ```
    
2. **Installing Chakra UI**:
Inside your project directory, install Chakra UI and its peer dependencies:
    
    ```bash
    npm i @chakra-ui/react @emotion/react @emotion/styled framer-motion
    ```
    
3. **Setting Up Chakra UI**:
In your `main.jsx` or `index.js`, wrap your application in the `ChakraProvider` component to provide context:
    
    ```jsx
    import { ChakraProvider } from "@chakra-ui/react"
    import ReactDOM from 'react-dom'
    import App from './App'
    
    ReactDOM.render(
      <ChakraProvider>
        <App />
      </ChakraProvider>,
      document.getElementById('root')
    )
    ```
    

[Installation](https://chakra-ui.com/getting-started)

---

## Components in Chakra UI

Chakra UI offers a variety of components. Here are some commonly used ones:

1. **Button**:
    - Usage: `<Button colorScheme='blue'>Button</Button>`
    - It's a basic interactive element for form submissions or user actions.
2. **Box**:
    - Usage: `<Box p={5} color='white' bg='blue.500'>Welcome</Box>`
    - Acts as a div tag but with Chakra UI styling props.
3. **Flex** and **Grid**:
    - Usage:
        - Flex: `<Flex align='center'>...</Flex>`
        - Grid: `<Grid templateColumns='repeat(5, 1fr)' gap={6}>...</Grid>`
    - These components are used for layout structure.
4. **Input**:
    - Usage: `<Input placeholder='Enter text' />`
    - For user input fields.
5. **Text**:
    - Usage: `<Text fontSize='xl'>Hello World</Text>`
    - To display text with various styling options.
6. **Stack**:
    - Usage: `<Stack direction='row' spacing={4}>...</Stack>`
    - Helps in managing layout and spacing of child components.

[Components](https://chakra-ui.com/docs/components)

---

## Style Props and Responsiveness

In Chakra UI, style props are a powerful feature that allows you to apply styles directly to components using props. This approach is inspired by the idea of "style as props", which makes styling more intuitive and efficient, especially for React developers. Let's delve into the details.

## Understanding Style Props in Chakra UI

### Basics of Style Props

- **Inline Styling Made Easy**: Chakra UI's style props let you style components directly in the JSX code, similar to inline styles in HTML but more powerful.
- **Responsive Design**: You can use array syntax or object syntax to apply different styles at various breakpoints, making it easier to build responsive designs.
- **Theming**: Style props are tied to Chakra UI's theme, ensuring consistency across your application.

### Common Style Props Categories

1. **Layout Props**: Like `width`, `height`, `display`, `overflow`, etc.
    
    ```jsx
    <Box width="100%" height="50px" overflow="hidden"></Box>
    
    ```
    
2. **Color and Background**: Such as `color`, `bg`, `backgroundColor`, etc.
    
    ```jsx
    <Text color="red.500" bg="yellow.100">Hello, Chakra!</Text>
    
    ```
    
3. **Typography**: Like `fontSize`, `fontWeight`, `lineHeight`, `textAlign`, etc.
    
    ```jsx
    <Text fontSize="lg" fontWeight="bold" lineHeight="short">Bold Text</Text>
    
    ```
    
4. **Spacing**: Including `margin`, `padding`, `space`, etc.
    
    ```jsx
    <Box m={4} p={5}></Box> {/* m for margin, p for padding */}
    
    ```
    
5. **Flexbox and Grid**: Props to control flex and grid layouts like `justifyContent`, `alignItems`, `gridGap`, etc.
    
    ```jsx
    <Flex justifyContent="center" alignItems="center"></Flex>
    ```
    
6. **Borders**: Such as `border`, `borderRadius`, `borderColor`, etc.
    
    ```jsx
    <Box border="1px solid" borderColor="gray.200" borderRadius="md"></Box>
    ```
    
    ### Responsive Styling with Array Syntax
    
    Chakra UI allows you to define responsive styles using an array syntax where each element corresponds to a breakpoint:
    
    ```jsx
    <Box width={['100%', '75%', '50%', '25%']} p={[1, 2, 4, 8]}>
      {/* Width and padding will change based on the screen size */}
    </Box>
    
    ```
    
    ### Using Object Syntax for Responsive Styles
    
    Alternatively, you can use object syntax to define styles for specific breakpoints:
    
    ```jsx
    <Text fontSize={{ base: '12px', md: '16px', lg: '20px' }}>
      Responsive font size
    </Text>
    ```
    
    ### Example: Building a Responsive Card
    
    ```jsx
    import { Box, Image, Text } from '@chakra-ui/react';
    
    function ResponsiveCard() {
      return (
        <Box maxW="sm" borderWidth="1px" borderRadius="lg" overflow="hidden" p={4} m={2}
             width={['100%', '48%', '32%', '23%']} boxShadow="md">
          <Image src="path/to/image" alt="Image" />
          <Text mt={2} fontSize="xl" fontWeight="semibold" lineHeight="short">
            Card Title
          </Text>
          <Text mt={2}>Card description goes here...</Text>
        </Box>
      );
    }
    
    ```
    
    In this example, the `ResponsiveCard` component uses various style props for layout, typography, and spacing, demonstrating how Chakra UI simplifies styling in React applications.
    
    ### Assignments for Practice
    
    1. **Styling a User Profile Card**:
        - Create a user profile card with an image, name, and a short bio.
        - Use style props to set the layout, background, typography, and spacing.
        - Make the card responsive for different screen sizes.
    2. **Designing a Responsive Header**:
        - Build a website header with a logo, navigation links, and a CTA button.
        - Apply responsive styles to adjust the layout and spacing on different devices.
    
    Using style props, you can efficiently apply and manage styles across your application, making your development process faster and your codebase cleaner.
    

[Style Props](https://chakra-ui.com/docs/styled-system/style-props)

[Responsive Styles](https://chakra-ui.com/docs/styled-system/responsive-styles)

---

## Hooks in Chakra UI :

Chakra UI provides a set of custom React hooks that make it easier to manage various UI states and behaviors. Let's discuss two popular hooks: `useDisclosure` and `useToast`.

### 1. `useDisclosure`

This hook is commonly used for handling open-close actions for modals, drawers, or any expandable components. It provides a convenient way to control the visibility of such components.

- **Methods and Properties**:
    - `isOpen`: A boolean indicating if the component is open.
    - `onOpen`: A function to open the component.
    - `onClose`: A function to close the component.
    - `onToggle`: A function to toggle the component's open state.

### Code Example: Using `useDisclosure` with a Modal

```jsx
import React from 'react';
import { Button, Modal, ModalOverlay, ModalContent, ModalHeader, ModalFooter, ModalBody, ModalCloseButton, useDisclosure } from '@chakra-ui/react';

function ExampleModal() {
  const { isOpen, onOpen, onClose } = useDisclosure();

  return (
    <>
      <Button onClick={onOpen}>Open Modal</Button>

      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>Modal Title</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            {/* Your modal content goes here */}
          </ModalBody>
          <ModalFooter>
            <Button colorScheme="blue" mr={3} onClick={onClose}>
              Close
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  );
}

export default ExampleModal;

```

### 2. `useToast`

`useToast` is another powerful hook that Chakra UI provides for showing toast notifications. It's a great way to give feedback or information to users after an action.

- **Usage**:
    - You can customize the appearance, duration, and position of the toast.

### Code Example: Displaying a Toast Notification

```jsx
import React from 'react';
import { Button, useToast } from '@chakra-ui/react';

function ToastExample() {
  const toast = useToast();

  return (
    <Button
      onClick={() =>
        toast({
          title: "Account created.",
          description: "We've created your account for you.",
          status: "success",
          duration: 9000,
          isClosable: true,
          position: "bottom-left"
        })
      }
    >
      Show Toast
    </Button>
  );
}

export default ToastExample;

```

In this example, clicking the button triggers a toast notification at the bottom left of the screen with a success message.

### Assignments to Practice with Hooks

1. **Modal Implementation Assignment**:
    - Create a component with a list of items.
    - Implement a button that, when clicked, opens a modal showing details about the selected item.
    - Use `useDisclosure` to control the modal's open and close actions.
2. **Toast Notification Assignment**:
    - Build a simple form that accepts user feedback.
    - On submitting the form, display a toast notification using `useToast` to confirm submission.
    - Experiment with different toast properties like position, status, and duration.

These hooks from Chakra UI simplify handling common UI patterns, making your code cleaner and more maintainable. They also enhance user experience by providing intuitive interactions.

---

## Custom Theme

Creating a custom theme in Chakra UI involves overriding the default theme:

1. **Import extendTheme**:
    
    ```jsx
    import { extendTheme } from '@chakra-ui/react'
    ```
    
2. **Define Your Custom Theme**:
    
    ```jsx
    const theme = extendTheme({
      colors: {
        brand: {
          900: '#1a365d',
          800: '#153e75',
          700: '#2a69ac',
        },
      },
    })
    ```
    
3. **Use Your Custom Theme**:
Provide your custom theme to `ChakraProvider`:
    
    ```jsx
    <ChakraProvider theme={theme}>
      <App />
    </ChakraProvider>
    ```
    

[Customize Theme](https://chakra-ui.com/docs/styled-system/customize-theme)

---

## More Examples :

### Example 1: Creating a Responsive Navbar

```jsx
import { Box, Flex, Text, Button, useColorMode } from '@chakra-ui/react';

function Navbar() {
  const { colorMode, toggleColorMode } = useColorMode();
  return (
    <Flex as="nav" align="center" justify="space-between" wrap="wrap" padding="1.5rem" bg="teal.500" color="white">
      <Text as="h1" fontSize="xl" letterSpacing={"-.1rem"}>
        Chakra UI Navbar
      </Text>
      <Box display={{ base: "block", md: "none" }} onClick={toggleColorMode}>
        {colorMode === "light" ? "Dark" : "Light"}
      </Box>
      <Box display={{ sm: "block", md: "none" }} onClick={toggleColorMode}>
        <Button bg="transparent" border="1px">
          Toggle {colorMode === "light" ? "Dark" : "Light"}
        </Button>
      </Box>
    </Flex>
  );
}

export default Navbar;

```

### Example 2: Building a Sign-up Form

```jsx
import { Box, FormControl, FormLabel, Input, Button } from '@chakra-ui/react';

function SignupForm() {
  return (
    <Box p={8} maxWidth="500px" borderWidth={1} borderRadius={8} boxShadow="lg">
      <form>
        <FormControl id="email">
          <FormLabel>Email address</FormLabel>
          <Input type="email" />
        </FormControl>
        <FormControl id="password" mt={4}>
          <FormLabel>Password</FormLabel>
          <Input type="password" />
        </FormControl>
        <Button width="full" mt={4} type="submit">
          Sign Up
        </Button>
      </form>
    </Box>
  );
}

export default SignupForm;

```

---

# Use-case & Benefits

- **Accessibility**: Built with accessibility in mind, ensuring your site is user-friendly for everyone.
- **Responsive Design**: Components are responsive, making your website look great on any device.
- **Customizability**: Easily customizable to fit your design needs.
- **Productivity**: Speeds up the development process with its out-of-the-box components.

## Real-World Examples

- **Portfolio Websites**: Using Chakra UI to create stunning, professional portfolio sites.
- **E-commerce Platforms**: Build interactive product listings and cart functionalities.
- **Blogs**: Design a clean, readable blog layout with ease.

## Assignments to Practice

1. **Responsive Portfolio Site**:
    - Create a single-page portfolio website using Chakra UI.
    - Include a header, about section, project showcase, and contact form.
    - Make sure the layout is responsive for mobile and desktop views.
2. **Themed Blog Page**:
    - Design a blog page with a list of articles.
    - Implement a custom theme that changes the color scheme of buttons and headings.
    - Add a toggle to switch between light and dark mode.
3. **E-commerce Product Grid**:
    - Build a grid layout to display products using the Grid component.
    - Each product card should include an image, title, price, and 'Add to Cart' button.
    - Implement a filter bar to sort products by category.
4. **Interactive To-Do List**:
    - Create a to-do list application.
    - Users should be able to add, delete, and mark tasks as completed.
    - Use Chakra UI components for the input field, buttons, and task list.

These examples and assignments offer a practical approach to learning Chakra UI by creating common web components and applications. They are designed to help you understand how to integrate Chakra UI into various types of projects, enhancing both your layout skills and your understanding of this library.