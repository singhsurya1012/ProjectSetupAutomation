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
    




print("Github Token "  + gitToken)
print("Creating repo: " + projectName)