- Any track ( Frontend, Backend, DA, DSA ) encompasses a variety of languages, frameworks, and tools/technologies including HTML/CSS, JavaScript, React, Node.js, and more. You will find the content for each area broken down into manageable segments here.

- Each folder is assigned a unique identifier following a sequential naming convention (01, 02, 03, 04, 05, ...). Comprehensive details about the contents of each sub-topic folder are provided in the README.md file located in the root directory of the topic folder. For instance, the README.md for the html-css folder can be found at `<track>/topics/html-css/README.md`. Below is a sample of what you might find inside:

```markdown
| Serial No | Topic                         | Time |
| --------- | ----------------------------- | ---- |
| 1         | How the web works             | 15   |
| 2         | Introduction to HTML          | 15   |
| 3         | Installing VS Code            | 10   |
| 4         | Creating your first HTML file | 5    |
```

- Should you require assistance in generating content for a specific topic, the following GPT prompt may prove useful.

```
Write a very deep, detailed and interactive lesson on the {topic} in around 4000 characters. Use relevant CODE EXAMPLES with explanation. Your explanations should be driven by code examples. keep it hands on.

Keep the following lesson structure:

## Introduction to { topic }
If possible, define {topic} in technical terms.

## Detailed Explanation
Explain {topic} to an absolute beginner. Use easy to understand Analogies and examples. Use step by step teaching. Start with simplest examples and build on top of that. Your explanations should be driven by code examples. keep it hands on.

## Use-case & benefits
Tell about the problems {topic} is solving. Give example of problem that {topic} solves and how it solves the problem.

## Real world Examples
Give examples that are easy to relate and relevant to the real world programming

## Usage
If relevant to {topic}, give all important methods, properties with definitions and example in a nice tabular format.

## Instructor Activity
A relatively big problem statement related to {topic} that instructor solves in class. Provide step by step explanation and the solution as well.

## Learners Activity
A relatively big problem statement related to {topic} that student solves in class. Provide step by step explanation and the solution as well.

## Learning Check
In the learning check give 3 Multiple choice questions about the topic and add 2 live coding challenges.

## Live Coding
Give 2 Live Coding Challenge
```
