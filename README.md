# Code Sample

Python Code Sample to showcase programming knowledge for job a interview.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

Python Version
```
python 3.6.8
```

I have a requirements.txt to install dependencies needed.
Run as sudo or add --user to install depending on how you want to install them
```
pip install pybuilder
```

### Installing and running tests

After cloning repository run pybuilder to install dependencies
```
pyb install_dependencies
```
Then run pybuilder to install. This will build and install in target/
```
pyb
```

To clean up you can run this
```
pyb clean
```
Which will delete the target directory and build files

### Run it

To run main.py, after you run pyb to build head to the dist dicrectory and run it.
```
cd target/dist/codeSample-1.0.dev0

python main.py
```

The code loads in a mod.txt and savedUsers.txt files and then prompts you to login as a mod.
To login, enter root and the password for this mod is test123.

Then you are shown a list of commands to run that look like this...
```
Login successful

------------------------------
What would you like to do?

C - Create new user
D - Delete user
S - Save users
Q - Quit program
------------------------------
Choice:
```

Choices are:
* Create New User - This will prompt you for input to create a new user
* Delete user - This will display all users and ask which one you want to delete based on an ID number
* Save users - This saves the current users to a text file by updating/overwriting it.
* Quit program - Quits the program.


## Built With

* [Python 3.6.8](https://python.org/) - Python 3 Core
* [Pybuilder](http://pybuilder.github.io/) - Pybuilder python project build and test


## Authors

* **Wes Forman** - *Author* 


## License

This project is licensed under the MIT License
