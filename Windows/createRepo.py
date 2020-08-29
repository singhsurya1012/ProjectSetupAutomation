import sys
import os

#Getting projectName from commandLine Argument passed from script
projectName = str(sys.argv[1])

#Geting project dir and github token from env variables\
projectDir = os.environ['proj_dir']
gitToken = os.environ['git_token']

projectDir = projectDir +'/' + projectName

if not os.path.exists(projectDir):
    os.mkdir(projectDir)
    print("Directory " , projectDir ,  " Created ")
else:    
    print("Directory " , projectDir ,  " already exists")
    

#change directory to  created folder
os.chdir(projectDir)

#Run git init commandLine
os.system('git init')

#create README.md file
os.system('echo New Project - ' + projectName + ' >> README.md')


print("Github Token "  + gitToken)
