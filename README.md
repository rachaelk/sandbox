# Let's make a repo!

## Getting started
A nice git set-up tutorial are written nicely by one of my profs, Dr. Kooima, [here](http://csc.lsu.edu/~kooima/courses/csc4356/git.html). Below are some simple basics.
 * Get a local version of the repo. You can do one of two things: 
    1. Easiest: Clone this repository on your desktop or wherever you want to place it. (Check right-hand side of the repo or just "git clone https://github.com/rachaelk/sandbox").
    2. Go to your terminal (Powershell), cd into whichever base directory you want to use, and make a new directory ("mkdir sandbox"). Then write "git init" and set the upstream to this repo.
 
## Fundamentals
 * Git basic operations (in order)
    1. ```git add .```
    2. ```git commit -m "Write modifications to code here."```
    3. ```git push origin master```
        * 'origin master' is needed only really the first time..you can set it yourself.

* Other useful commands
    - ``` git status ``` outputs status of files (changes made, modifications pushed or not pushed, etc.)
    - ``` git pull ``` pulls any changes made to the master repo
    - ``` git remote show origin ``` shows the info of the master branch you are working from
    - ``` git branch --set-upstream master= origin/master``` explicitly setting origin master


* Useful and related stackoverflow/blog pages.
    - [pull/merge branch](http://stackoverflow.com/questions/10298291/cannot-push-to-github-keeps-saying-need-merge)
    - [fetch and merge, don't pull [branches] ](http://longair.net/blog/2009/04/16/git-fetch-and-merge/)

