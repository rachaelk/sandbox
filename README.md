# Let's make a repo!

## Getting started
A nice git set-up tutorial are written nicely by one of my profs, Dr. Kooima, [here](http://csc.lsu.edu/~kooima/courses/csc4356/git.html). Below are some simple basics.
 * Get a local version of the repo. You can do one of two things: 
    1. Easiest: Clone this repository on your desktop or wherever you want to place it. (Check right-hand side of the repo or just "git clone https://github.com/rachaelk/sandbox").
    2. Go to your terminal (Powershell), cd into whichever base directory you want to use, and make a new directory ("mkdir sandbox"). Then write "git init" and set the upstream to this repo.
  
 * Git basic operations (in order)
    1. git add .
    2. git commit -a "Write modifications to code here."
    3. git push origin master

* Other useful commands
    - ``` git pull ``` pulls any changes made to the master repo
    - ``` git remote show origin ``` shows the info of the master branch you are working from
    - ``` git branch --set-upstream master= origin/master``` explicitly setting origin master