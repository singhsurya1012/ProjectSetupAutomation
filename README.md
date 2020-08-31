#### This is a utility script which gives you a simple command which you can run to automate your initial project creating steps. 

<br>


#### Type **np projectName** in cmd to create New Project ####

<br>

1) It will create a folder with the specified project name 
2) Create a git repo with the same name 
3) Create README.md
4) Create .gitignore file using the sample provided <br>
    **Optional** : updated this with your own .gitignore file
3) Link this folder to your git repo
4) Opens the project in Intellij

<br>


##### Steps (One time setup):

###### For Windows:

1) Clone this project in your local machine <br>
	git clone https://github.com/singhsurya1012/ProjectSetupAutomation.git
2) Install Python
3) Install PyGithub. Run command **pip install PyGithub**
4) Edit **setenv.bat** with your values and run (Note: This edits env variables. Can be done manually)

<br><br>



###### For Linux:

If you are using Linux as your personal OS you are smart enough to do this fun project on your own.

<br>

1) Clone this project in your local machine <br>
	git clone https://github.com/singhsurya1012/ProjectSetupAutomation.git
2) Install Python
3) Install Pip. Run Command **sudo apt install python3-pip**
4) Install PyGithub. Run command **pip3 install PyGithub**
5) Install python-dotenv. Run command **pip3 install python-dotenv**
6) Edit .env file with your git_token and default project directory
7) Edit **setenv** with proper ProjectSetupAutomation/Linux folder location and run
8) Restart terminal
9) You maybe required to make np file executable.
Run command **chmod +x np**


<br><br>

   	Command name can be changed by just renaming the np.bat or np file in Linux folder.

<br><br>

###### Future: 

1) Could be extended to create sample structure for spring boot app or a react js app etc using some template

<br><br>

###### References:

1) https://stackoverflow.com/questions/60250553/how-to-make-a-batch-script-to-execute-from-anywhere
2) https://stackoverflow.com/questions/5034076/what-does-dp0-mean-and-how-does-it-work\
3) https://stackoverflow.com/questions/28574800/add-batch-file-to-path
4) https://stackoverflow.com/questions/9546324/adding-a-directory-to-the-path-environment-variable-in-windows
5) https://pygithub.readthedocs.io/en/latest/introduction.html
6) https://medium.com/devnetwork/how-to-create-your-own-custom-terminal-commands-c5008782a78e
7) https://askubuntu.com/questions/503127/should-i-save-my-scripts-with-the-sh-extension#:~:text=No%2C%20it%20is%20not%20a,packages%20doesn't%20have%20a%20.&text=You%20can%20create%20directory%20~%2F,as%20any%20other%20shell%20command.
