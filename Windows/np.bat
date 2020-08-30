@echo off

::The %~dp0 (that’s a zero) variable when referenced within a Windows batch file will expand to the drive letter and path of that batch file.
::Example: Let’s say you have a directory on C: called bat_files, and in that directory is a file called example.bat. 
::In this case, %~dp0 (combining the d and p modifiers) will expand to C:\bat_files
::This is done so that the batch file can locate the python script
cd /d %~dp0

:: %1 is first parameter - ProjectName
If "%1" == "" (

	echo Error: Please pass the project name as parameter
	echo eg: np ^<projectName^>	
	
	
)else (

	echo Initiating Project Setup - %1
	python createRepo.py %1
	
)

