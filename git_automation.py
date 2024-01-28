# import os
import subprocess

# Get the current directory 
# curdir = os.getcwd()

# Navigate back to the Git root folder
# os.chdir(os.path.join(curdir, "../"))

# Run git status
subprocess.run(["git", "status"])

# Run git add . 
subprocess.run(["git", "add", "."])

# Get user input for the commit message
commit_message = input("Enter your commit message: ")

# Run git commit with the custom message
subprocess.run(["git", "commit", "-m", commit_message])

# Run git push
subprocess.run(["git", "push"])
