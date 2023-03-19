print("Hello from Mika!")

print("Hello from person 2")


# on local machine
git init  --> initialize git repo
create few files, add code, content

# on remote side (github)
create repo

# on local machine
attach github repo to local repo (git remote add origin "write github repo URL")

# create braches
git checkout -b "Task1"

# do some work
# add them to VCS
git add .   # to add all files
git add *.py  # to add files with pattern
git add my_file.py # to add only one file

# check status
git status

# if everything is okay, commit with message
git commit -m "write appropriate message to describe your current work"

# push your current changes to remote repo (i.e. to github / gitlab)
git push  # if you are doing this first time, you have to set upstream branch name  i.e. git push --set-upstream origin Task1

# once you have pushed everything, merge your current branch into main branch
# go to main branch
git checkout

# merge Task1 into main
git merge Task1








