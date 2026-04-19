### Overview

### Top-Level Folders

- **`README.md`**: This file contains comprehensive details about the repository, including its purpose, structure, and how to navigate or contribute to it.

- **`guidelines`**: This folder holds documents related to various aspects of the curriculum, such as assignment expectations, evaluation criteria, folder structure conventions, instructor notes, learning checks, onboarding processes, and problem-solving strategies.

- **`learning-objectives`**: A placeholder for documents outlining the learning goals for different segments of the curriculum.

- **`programs`**: Divided into subfolders for different educational programs offered, such as Masai One (ms1), College Network (cn), offline college programs (college), Prepleaf Programs (pl), and Vector Program (vector). Each program folder contains course-specific folders like `aaa-111`, which are named according to the curriculum (e.g., WEB204, JS204, RCT104).

- **`topics`**: Contains a placeholder for future topics that might be added to the curriculum. The `.keep` file serves the same purpose as in the `learning-objectives` folder.

### Program Folder Structure

Each program folder, e.g., `ms1` for Masai One, includes course folders that follow a standard structure:

- **`blockwise-data`**: Contains folders for each block of the course (e.g., `b33`, `b34`), each with a `README.md` detailing the block's content.

- **`evaluation-guidelines`**: Offers specific guidelines for creating evaluation, rubrics for any particular course for evaluating students performance across different sprints (`sprint1.md`, `sprint2.md`, etc.).

- **`sessions`**: Organizes the curriculum into session-based folders (`01`, `02`, etc.), each divided into `class` and `pre-class` activities with respective assignments, instructor notes, student notes, and learning checks.

### Detailed Guidelines for Key Components

- **Assignments (`assignments`)**:

  - The `README.md` in each assignment folder should link to the master template for that session's assignments.
  - Each problem (e.g., `problem-1.md`, `problem-2.md`) should include a problem statement and a solution, formatted with headers for clarity.

- **Instructor Notes (`instructor-notes`)**:

  - Contains all necessary notes for instructors, following the format outlined in the `guidelines` folder.

- **Student Notes (`student-notes`)**:

  - Contains all necessary notes to be shared with students, following the format outlined in the `guidelines` folder.

- **Learning Checks (`learning-checks`)**:
  - Includes a `README.md` with a master template link for quiz questions.
  - Each question file (e.g., `quiz-question-1.md`) should list the quiz question, multiple-choice options, and the solution with an explanation.

```markup
└── 📁curriculum-frontend
    └── README.md
    └── 📁guidelines
        └── assignment.md
        └── evaluations.md
        └── folder-structure.md
        └── instructor-notes.md
        └── learning-check.md
        └── onboarding.md
        └── problem.md
    └── 📁learning-objectives
        └── .keep
    └── 📁programs
        └── ms1
            └── 📁web-204
                └── 📁blockwise-data
                    └── 📁b33
                        └── README.md
                    └── 📁b34
                        └── README.md
                └── 📁evaluation-guidelines
                    └── sprint1.md
                    └── sprint2.md
                    └── sprint3.md
                    └── sprint4.md
                └── 📁sessions
                    └── 📁01
                        └── 📁class
                            └── 📁assignment
                                └── README.md
                                └── problem-1.md
                                └── problem-2.md
                            └── 📁instructor-notes
                                └── README.md
                            └── 📁learning-checks
                                └── README.md
                                └── question-1.md
                                └── question-2.md
                            └── 📁student-notes
                                └── README.md
                        └── 📁pre-class
                            └── 📁assignment
                                └── README.md
                            └── 📁instructor-notes
                                └── README.md
                            └── 📁student-notes
                                └── README.md

    └── 📁topics
        └── .keep
```

- Different frontend courses that are currently running and their course-code

1. ms1/web-204 ( masai-one web 204 course )
2. ms1/js-204
3. ms1/rct-104
4. pl/web-2004
5. pl/js-2004
6. pl/rct-1004
