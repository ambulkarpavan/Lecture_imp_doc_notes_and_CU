# **Problem Creation Guidelines**

## Frontend Coding Problem Guidelines

To ensure a productive learning experience and maintain course consistency, all problems provided to students must adhere to the following guidelines:

- **Problem Structure**

  Each problem should be structured as follows:

  - **Overview:** This section provides a high-level summary of the problem's objectives, outlining the problem to be solved and the expected outcomes. It should also specify the tools and technologies students are expected to use.

    **Example:**

    - Evaluate the developer's understanding of React's State management and the `useState` hook.
    - The problem involves creating a counter application in React using the `useState` hook, starting at 0.
    - Include a button to increment the count by 1 with each click.

  - **Detailed Explanation:** Offer a comprehensive explanation to help students grasp the problem fully. This section should cover:

    - **Topics:** List essential topics and concepts necessary for tackling the problem, formatted as bullet points. For example:

      - State management and the useState hook in React
      - JSX

    - **Setup Guidelines and Instructions:** Provide a detailed, step-by-step setup guide. For example:

      - **Creating a New Vite Project:**

        - Launch the terminal.
        - Execute `npm create vite@latest <app-name> -- --template react` to initiate a new project.
        - Change directory to your new project with `cd <app-name>`.

      - **Installing Dependencies:**

        - In the project directory, run `npm install` to add required dependencies.

      - **Launching the Development Server:**
        - Start the development server with `npm run dev`.
        - Visit `http://localhost:5173` to view the project.

    - **Problem Statement:** Define the problem clearly, outlining every task or feature the students are expected to implement. This should be comprehensive, eliminating any potential ambiguities. Include all critical details, such as API specifications, within this section. All the guidelines specific to problem goes here.

  - **Submission Guidelines:**
    - Clearly state all submission-related guidelines in this section.
    - Avoid creating multiple subsections like General Guidelines, Misc Guidelines, Notes, etc. All guidelines should be categorized under Setup, Problem Statement, or Submission sections as appropriate.
    - Ensure every detail regarding the submission process is mentioned, including steps like pushing the code to GitHub and submitting the repository link on CP. Do not make any assumptions and clearly define instructions. Each problem should contain all necessary submission details.

  **Suggested Structure:**

  ```
  # Problem Statement :

  ## Time to solve the problem

  ## Overview

  ## Detailed Explanation

  ### Topics

  ### Setup Guidelines and Instructions

  ### Problem Statement

  ## Submission Guidelines

  ---

  # Solution :
  ```
