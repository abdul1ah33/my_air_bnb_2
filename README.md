
## HBnB

AirBnB clone
------------

## Inroduction

The HBnB clone project which is a copy of the AirBnB website, is a full web application that intergrates the back-end console, database for data storage, front-end which is a  visual interface for users  and API that provides a the front-end and back-end to communicate.
The focus of this project however, is to build a back-end console.

## What is a console?
A console is a text-based interface or a command line interpreter that allows users to nteract with a computer program.

##Classes
The following classes are used for AirBnB:
	- A BaseModel class which is the parent class

	- User that inherits from BaseModel class
	
	-City class

	-State class

	-Place class
## Commands Used
	
	-create CLASS - Create a new class instance
	-destroy CLASS ID - Destroy a specified instance based on a given id
	-show CLASS ID - Outputs a string representation of a class instance
	-all [CLASS] - Outputs string representation of all instances of a given class
	-help - Assists in getting information about a command.
	-update CLASS ID ATTRIBUTE VALUE - Edit attributes of an instance.
	-quit - Close an interactive session. Also quit with ^-D or EOF.
## AirBnB console
The hBnB console can be run both interactively and non-interactively.

To start an interactive session run:

console.py

./console.py

If the execution is  successful it will display the prompt
hbnb

You can then proceed to type any of the commands named above.

To quit the interactve mode just type
quit

It may also be used in a non_interactive mode by piping a command to it.

##Storage Engine of AirBnB project
The project uses the File storage for storage of data, which which is the abstracted engine of the project

