## Onboarding Process

## Process

1. The new member must reach out to the Track Lead to be added to their respective track repository.
2. They will first be added to the curriculum under the respective team on GitHub.
3. Additionally, they will be included in all the projects of that course by the Team Lead.
4. We conducted a session with the team to explain the entire curriculum structure. Here is the recording of this session: [Link](https://us06web.zoom.us/rec/share/Mic5SaazpWifs3miSDje7EKhsnW9ru8M9mByzuhEqsXQSF3PT60sswT-Vw_QLtfz.rKXu64q_aUSjm88Z). Please watch this recording and contact the Team Lead if you have any questions.
5. To raise any issue, you must submit the issue under GitHub projects. The Team Lead will guide you on how to do this.

Below is the process on how to raise an issue/ticket on GitHub:

# How to Push Changes to GitHub

This guide will walk you through the process of pushing your changes to GitHub.

Note : The newly created branch name should follow the convention "<issue_no>-<issue_name>"

## Step 1: Clone the Repository

First, clone the repository you want to work on:

```bash
git clone <repository_url>
```

Replace `<repository_url>` with the actual URL of the repository.

## Step 2: Create a New Branch

Before making changes, switch to a new branch named after the issue you're working on:

```bash
git checkout -b <issue_no>-<issue_name>
```

Replace `<issue_no>` with the issue number and `<issue_name>` with a brief description of the issue.

## Step 3: Make Your Changes

Make the necessary changes in the code or documentation as required.

## Step 4: Stage Your Changes

After making changes, stage them for commit:

```bash
git add .
```

Or, to stage specific files:

```bash
git add <file1> <file2>
```

## Step 5: Commit Your Changes

Commit your changes with a meaningful message:

```bash
git commit -m "Your detailed commit message"
```

## Step 6: Push Your Branch to GitHub

Finally, push your branch, along with the commits, to GitHub:

```bash
git push origin <issue_no>-<issue_name>
```

## Step 7: Create a Pull Request

- Navigate to the repository on GitHub.
- Click on the "Pull request" button.
- Select your branch and provide a title and detailed description for your pull request.
- Submit the pull request for review.

```
Remember to keep your branch up-to-date with the base branch to reduce merge conflicts. Always check the project's contributing guidelines before starting your work.
```
