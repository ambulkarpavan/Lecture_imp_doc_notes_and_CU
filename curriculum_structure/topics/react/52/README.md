# Environment Variables

Serial: 50

# Introduction

In this lesson, we will explore the concept of environment variables, focusing on their use in React projects created with Vite. Environment variables are a fundamental aspect of web development, offering a secure and flexible way to handle configuration settings.

# Detailed Explanation

**What are Environment Variables?**

Environment variables are dynamic-named values that can affect the way running processes in a computer behave. They are particularly useful in application development for:

1. **Storing Sensitive Data:** Keeping API keys, database passwords, and other sensitive information out of your source code.
2. **Configuration Settings:** Allowing different settings for development, testing, and production environments.
3. **Platform Agnostic Settings:** Facilitating a seamless transition between different platforms and deployment environments.

# Use-case & Benefits in a Vite-React Project

**Vite and React**

Vite is a modern front-end build tool that significantly improves the developer experience. It's designed for modern web projects, especially those using frameworks like React.

- **Fast Development:** Vite optimizes the handling of environment variables during development and production builds, ensuring quick iterations.
- **Secure Application:** By storing sensitive information in environment variables, Vite-React projects can keep such details out of the source code, enhancing security.
- **Flexible Configuration:** Easy switching of configurations between different stages of the development lifecycle (local development, staging, production).

# Real World Examples

1. **API URLs:** Setting different API endpoints for development and production.
2. **Feature Flags:** Toggling features in your React app based on the current environment.

# Setup and Usage in a Vite-React Project

## **Setup**

1. **Create a `.env` File:** In your Vite-React project, create a `.env` file in the root directory.
2. **Add Variables:** Prefix your variables with `VITE_` (e.g., `VITE_API_URL=https://api.example.com`).
3. **Git Ignore:** Ensure your `.env` file is listed in `.gitignore` to avoid pushing it to version control.

## **Usage**

1. **Accessing Variables:** In your React components, access the variables using `import.meta.env` (e.g., `const apiUrl = import.meta.env.VITE_API_URL;`).

# Instructor Activity

Let's demonstrate how to implement environment variables in a sample Vite-React project:

1. Create a new Vite-React app.
2. Set up a `.env` file with a sample variable.
3. Use this variable in a React component and display its value.

# Learners Activity

1. **Setup Task:** Create your own `.env` file in a Vite-React project and add a custom environment variable.
2. **Implementation Task:** Develop a small feature in your React app that uses the environment variable (e.g., fetching data from an API whose URL is stored in the environment variable).

Remember, the key to mastering environment variables in Vite-React projects is practice and understanding their importance in maintaining a secure and flexible development environment. Happy coding!