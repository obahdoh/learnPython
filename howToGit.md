# How to use git

## Git status

In git files can be in one of three states

Committed - they're saved to your repo
Staged - they're ready to be added to your repo
unntracked - they have changes that aren't ready to be saved to your repo

You can run  `git status` to see the state of your files

## Git add

You use `git add` to prepare your files to be saved. When you run it you need to specify the names of the files you want to save. You can also specify a directory and it will stage (whcih means prepare to save) all the unsaved files in it

```bash
@obahdoh ➜ /workspaces/learnPython (main) $ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        howToGit.md

nothing added to commit but untracked files present (use "git add" to track)
@obahdoh ➜ /workspaces/learnPython (main) $ git add .
@obahdoh ➜ /workspaces/learnPython (main) $ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   howToGit.md
```

In the above example we run git status and see that this file is `untracked` we then run git add on the directory `.` (which is a shortcut for the current directory) and when we run `git status` you see it is now tracked.

## Git Commit

Once you've prepared some files to be saved you can actually save them with `git commit`, you should specify a message describing what the changes are

```bash
@obahdoh ➜ /workspaces/learnPython (main) $ git commit -m "Start writing basic guide on using git"
[main 2c4226b] Start writing basic guide on using git
 1 file changed, 15 insertions(+)
 create mode 100644 howToGit.md
```

The `-m` after commit is used to indicate that the next thing is the message for the commit. The message itself must be surround in quote marks.