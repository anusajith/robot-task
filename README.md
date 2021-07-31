# Take Robo Home !!

## Contents
- [Description](#Description)
- [Files](#files)
- [Execution](#execution)
- [Assumptions](#assumptions)
- [Additional Docs](#additional docs)
- [Extensibility](#extensibility)


## Description

This is a CLI Python application to receives a string of commands and will output 
the robot's distance from it's starting point.  This distance will be the minimum 
amount of units the robot will need to traverse in order to get back to it's starting point.  
The robot can only turn 90 degrees at a time, so it cannot go directly back home, it must 
go in north, south, east, west directions.

There are two ways of input methods to feed the robot.We can choose the input method from the 
option(1 or 2) and accordingly pass our commands to robot.
The commands can be in string format or list of commands in 'input.yml' file.
eg: `F1,R1,B2,L1,B3`

### Available commands:
* `F` - move forward 1 unit
* `B` - move backward 1 unit
* `R` - turn right 90 degrees
* `L` - turn left 90 degrees



## Files
- [input.yml](https://github.com/anusajith/robot-task/blob/master/input.yml "input.yml")- This is the input file where we 
can provide the list of commands to robot.

- [calculate_distance.py](https://github.com/anusajith/robot-task/blob/master/calculate_distance.py "calculate_distance.py")- This is the file where all 
the functions to determine the distance and directions are implemented. This will validate the input commands, and then output the units it has to take 
to reach back the starting position.

- [test.py](https://github.com/anusajith/robot-task/blob/master/test.py "test.py") - This file decides our input method and then executes 
the functions inside 'calculate_distance.py'.

- [requirements.txt](https://github.com/anusajith/robot-task/blob/master/requirements.txt "requirements.txt")- Contains all the python 
package required to execute this application.


## Execution
The application is developed in python3.9 and required packages are available in 'requirements.txt'.\
Steps to execute:\
	1) Run the 'test.py'\
	2) Select the input method. '1' for string input or '2' for input commands in yml file.\
	3) If option '1' is chosen, enter the string input command like 'F1,R1,B2,L1,B3'\
    4) If option '2' there should be command list inside 'input.yml' file.\
	5) Gives the total units to reach source will be the output.
	
	
## Assumptions
Following are the assumptions in building this application.\
	1) Robot can only turn 90 degrees at a time.\
	2) The commands possible are 'F,L,R,B' and units from [1-9].\
	3) Final direction doesn't matter for now.\
	4) If option '2' is chosen, there should be atleast one entry in the 'input.yml' file
	
	
## Additional Documents
Hereby adding some extra files in the repo:
- [Dockerfile](https://github.com/anusajith/robot-task/blob/master/Dockerfile "Dockerfile") - Dockerfile to containerize the application.
- [Jenkinsfile.txt](https://github.com/anusajith/robot-task/blob/master/Jenkinsfile.txt "Jenkinsfile.txt") - Jenkinsfile file to automate 
the container build and testing using 'input.yml' file.
	
## Extensibility
 This CLI application is designed and build	considering the extensibility. If we want to add more complex functionalities it will be easier to 
 add and track them. Even we can extend the input methods according to user's ease.
	




