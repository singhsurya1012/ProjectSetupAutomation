import os
import sys

from github import Github

# Getting projectName from commandLine Argument passed from script
projectName = str(sys.argv[1])

# Geting project dir and github token from env variables\
projectDir = os.environ['proj_dir']
gitToken = os.environ['git_token']

projectDir = projectDir + '/' + projectName

if not os.path.exists(projectDir):
    os.mkdir(projectDir)
    print("Directory " , projectDir ,  " Created ")
else:
    print("Directory ", projectDir, " already exists")
    exit()

# change directory to  created folder
os.chdir(projectDir)

# Run git init commandLine
os.system('git init')

# create README.md file
os.system('echo New Project - ' + projectName + ' >> README.md')

# Using PyGithub for access Githib Api's

# login into github using github token
g = Github(gitToken)

# Get user details
user = g.get_user()

# Create repo with given name
repo = user.create_repo(projectName)
cloneUrl = repo.clone_url

# link repo
os.system('git remote add origin ' + cloneUrl)
os.system('git add .')
os.system('git commit -m "Repo setup"')
os.system('git push -u origin master')

# open folder in Intellij
os.system('idea .')

print('Project setup complete.... Project will be opened in Intellij')
