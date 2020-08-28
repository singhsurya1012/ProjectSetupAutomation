@echo off

:: Get the project name from parameter
set projectName = %1


If "%1" == "" (

	echo Please pass the project name as parameter
	echo eg: setup projectName	
	
	
)else (

	echo Initiating Project Setup - %1
	python createRepo.py 
	
)

