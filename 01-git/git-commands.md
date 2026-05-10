# Git Documentation

## Goal

The goal of this task was to understand the git workflow and practice some commands

## Commands I Used

### 1. Clone Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

I used this command to clone the github repository.

### 2. Check Status

```bash
git status
```

I used this command a lot to check the status of the files that were updated or added.

### 3. Add Files

```bash
git add .
```

I used this command to stage all changed files before committing.

### 4. Commit Changes

```bash
git commit -m "added ToDo app"
```

I used commits to save files to the repository, for example, I created a commit after adding the first version of the ToDo app.

### 5. Push to Github

```bash
git push
```

I used this command to upload my local commits to the repository.

### 6. View Commit History

```bash
git log --oneline
```

I used this command to view my commit history.

## Branching Experiment

I have never used branching before, so I decided to try it out with an experiment.

I first created a new branch:

```bash
git checkout -b improve-readme
```

On this branch, I changed the README file. After that, I committed the change:

```bash
git add .
git commit -m "Improve project README"
```

Then I switched back to the main branch:

```bash
git checkout main
```

Finally, I merged the branch into main:

```bash
git merge improve-readme
```

During this experiment, I encountered two issues:

First, I modified the README file before creating the new branch and because of this, the change was not clearly connected to the branch. I fixed this by creating a new branch anyway and making sure that the README change was committed on that branch. This helped me understand that uncommitted changes can move with me when I switch branches.

Second, I switched back to `main` before committing the change on the branch. When I tried to merge the branch, Git showed that everything was already up to date because the branch did not contain a new commit yet. I fixed this by switching back to the feature branch, staging the modified README file with `git add`, and committing it there. After that, I switched back to `main`, merged the branch, and pushed the result to GitHub.

## Time Travel Experiment