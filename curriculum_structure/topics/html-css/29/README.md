# Git Collaboration (Basic) (15mins)

Which PAN India movie do you like ?

Who is the director of the movie?

Whenever Rajamouli thinks of making a movie, firstly, a rough script has to be developed right? Then, the rough script will be improved. Now, after developing the rough script, in order to improve the rough script, he’ll hire some ADs right? AD means Asst Director. Let’s say he hires 4 ADs. Let’s consider them as AD1, AD2, AD3, AD4.

So, he’ll distribute the script to all the ADs. That means let’s say AD1 has to develop the HERO Introduction Scene, AD2 has to develop comedy scenes, AD3 has to develop fight sequences and AD4 has to develop the climax scene.

So, after the work alloted is finished, they’ll have to show it to the Director, right? Then, what will the Director do ? The Director will review Introduction Scene given by AD1 and will tell if any changes are required. If there are no changes, then it will be fixed and then the whole story will be given to the Hero, right? 

So, how will Rajamouli give the story to the Hero? Will he give 4 different pieces of script to the HERO or will he give the combined overall script ?

So, he’ll combine all the pieces of scripts given by ADs, i.e., he will merge all the scripts and give it to the HERO, right?

So, this is similar to our GIT Collab. Can anyone tell me how?

Who is RAJAMOULI in our case? MASTER / MAIN Branch

Then what are the ADs? AD1, AD2, AD3, AD4 are subsets of the master branch, right? That means, ADs are also branches but they are created from MASTER.

Now, let’s get back to the HERO Introduction Scene. 

After AD1 has completed working on the Hero Intro Scene, AD1 has to give it to Rajamouli, right?

How will he give it to Rajamouli ?

He has to first do

***add, commit and push to ad1 branch first.*** 

Then he’ll tell Rajamouli that I have finished my part, please take a look and tell me if any changes have to be made. If Rajamouli tells AD1 to make changes, then AD1 will again work on the changes and then

***add, commit and push to ad1 branch .***

Now, if there are no errors, then Rajamouli will merge the branch to master. ******

Same is the case with all the other ADs. 

After the whole script is ready, everything will be merged into the MASTER branch by Rajamouli and the script will be ready to be told to the HERO, right?

That means, the project is ready? Means, we can deploy? So, the deployed project or the script will be given to the HERO. Who is the HERO in the analogy? ***USER***, right.

That means, whatever is present in the master branch should be error free and should not be changed frequently. If there are any changes or errors, will the script be approved by the Director? No, right? He will tell to re-write or improve the script. So, if there are no bugs and there are no errors, then only it should be merged to master.

> ***So, let’s create a new Repository in our Github acc.***
> 

Keep it as Public. Now, the Rajamouli branch will either be main or master. If you add a reaadme file while creating a repo, the Rajamouli branch is `main`, else, the Rajamouli branch is `master`.

Both `master` and `main` are same. Create a repo and then clone it to our local system. Open VS Code and clone it on desktop itself.

How to clone now ?

```jsx
git clone <link copied from github>
```

Now, go to the folder and add some files for our project.

Let’s say that I want the Landing Page or Home Page.

```jsx
<h1>Home Page</h1>
```

Now, let’s add these changes to the project.

So, the steps we’ve to follow are:

***Add, push, and Commit.***

How will we know in which branch we are in ? 

We can see at the left bottom of the vs code screen.

> ***Open GitHub and show where branch name can be seen and the total count of branches.***
> 

Let’s say I want to create a branch from this master to work on Login Page. So, let’s create a branch called loginPage.  Now, lets create a new branch.

```jsx
git branch <branchName>
```

So, let’s write git branch loginPage so that we can work on the loginPage.

One command to see all the branches present in the project is

```jsx
git branch --list
```

Let’s see the branches we’ve. Now see the way the branches appear. There is a difference, right?

So, the current branch will be highlighted as shown. Now I have created the branch loginPage, but how do we go to the loginPage branch?

```jsx
git checkout <branchName>
```

Now check whether you’ve moved to the branch at the bottom left of vs code.

Also, check it by typing `git branch --list`

Now, for doing a project, you’ll be divided into teams, right? You won’t work alone in projects. So, how will you create a team in your repository? How can all of the team members work on the same project. So, they have to be added as collaborators. Let’s see how this can be done.

> ***Open github and go to `settings`, click on `Collaborators` and add people.***
> 

In order to add people, I should know the Github usernames of the people.

So, let’s type in Chandra’s username and click on Add button. 

You can add more than 1 person as collaborators by repeating the same steps.

Now, the emails will be sent to the people you’ve added as collaborators. Let’s see if Chandra has got an email and let’s see what he has to do after getting the email. 

> ***Tell Chandra to share his screen and show the students the next process***
> 

Now, he has added something and he’ll show the reviewers also. 

Then, you’ve to see for any changes for errors in the code. If everything is good, then you can `create a pull request` as follows.

When you create a `Pull request`, it’ll show from which branch to which branch it is pulling.

You can edit the details if the branches are wrong.

Now `confirm merge`

Now, can you tell whether the branch has been merged or not ?

In order to do that, we’ve to go to the repo and click on master/main branch. Can you see the data from loginPage is present in our master/main branch.

Now, we’ll see if I have the updated code in my system or not. Chandra has pushed some code to the branch, let’s see if I can access it from my system. No, right? Chandra has pushed to Github but I didn’t update it. So, how to update this on my local system.