#!/usr/bin/python3

#---------------------------------------------------------#
#  App Title: Code Samples
#  File: main.py
#  Author: Wes Forman
#  Date: 8/20/2019
#  Description: This is a code sample that I have written
#  for job interviews. It will go over various logic, loops
#  if/else, functions or methods, classes and OOP, system 
#  calls writing and reading files and running commands and
#  more.
#---------------------------------------------------------#

import re
import json
import Mods
#--------------------------Classes------------------------#

# Class User
class User():
    
    Name = "John Doe"                # Default name is John Doe starting out
    email = "name@something.com"     # email address of user
    Nickname = "Slick"               # Nickname of user


    # constructor of the Character object.
    def __init__(self, name, email, nickname):
        self.Name = name
        self.email = email
        self.Nickname = nickname

    # Getter Methods
    def getName(self):
        return self.Name
    
    def getEmail(self):
        return self.email

    def getNickname(self):
        return self.Nickname

    # Setter Methods

    def setName(self, name):
        if( input("Do you really want to change your name Y/n?") == "Y"):
            self.Name = name
        else:
            print("Ok we won't change your name then")
    
    # Converts object to be stored as JSON format in text
    def toJson(self):
        return "{{Name:{0}, email:{1}, Nickname:{2} }}".format(self.Name, self.email, self.Nickname)

def checkEmail(email):
    """Checks if the user input a valid email address.

    Takes in a string and uses regex to make sure it is a valid email.
    
    Returns boolean True/False"""

    isValid = re.search('^\w+@\w+.\w+$', email)
    if isValid:
        return True
    else:
        return False

def displayUsers(userList):
    """Displays a list of the users created.

    Takes in a list of User Objects and outputs them in pretty format.
    
    Returns nothing"""

    print("---------------------------------")
    for u in userList:
        print("Name = ", u.getName())
        print("email = ", u.getEmail())
        print("Nickname = ", u.getNickname())
        print("---------------------------------")

def saveToDisk(userList):
    """Saves User List to flat file

    Takes in User List and saves to file in JSON format
    
    Returns nothing"""

    with open("savedUsers.txt", 'a') as fp:
        for u in userList:
            fp.writelines(u.toJson()+"\n")
    print("Saved so you can import this User List next time!\n")

def importUsers():
    """Imports User List from disk

    Looks for savedUsers.txt file and creates a list of Class objects

    Returns a list of User class objects"""
    with open("savedUsers.txt", "r") as fp:
        Users = []
        for line in fp:
            #expload string on comma
            lineArray = line.split(",")
            #Split each var up
            name = lineArray[0].split(":")[1]
            email = lineArray[1].split(":")[1]
            nickname = lineArray[2].split(":")[1].strip(" }")
            # clean up end of nickname string
            nickname = nickname.strip(" }\n")
            Users.append(User(name, email, nickname))
    return Users

# Main funciton for code sample
def main():
    print("Welcome to Code Sample by Wes Forman\n")

    print("Lets try some user input and logic first\n\n")

    # Try to import User List first before creating a new one
    Usr = importUsers()

    if(not Usr):

        # While loop asking for user input and using try except to make sure we only have ints
        ans = None
        while(ans is None):
            try:
                ans = int(input("Give me a number between 1 and 10\n"))
            except ValueError:
                print("Please only enter a number\n\n")
            if(ans < 1 or ans > 10):
                ans = None
            else:
                break

        print("Great, you answered with", ans)
        print("Now I am going to need some more input from you\n")
        print("Since you chose", ans,", please give me that many names")
        
        # Loop through and create a Name list based on the number they gave
        Name  = []
        for i in range(0,ans):
            Name.append(input("Enter a name\n"))
        
        print("Alright, lets now get ", ans, " emails, of course fake ones for this exercise\n")
        
        # Get email in the correct format from input and store in list
        Emails = []
        for i in range(0,ans):
            # Loop until they enter a valid email then store and go onto the next index
            while(True):
                address = input("Enter a valid email. something@yeah.com\n")
                if(not checkEmail(address)):
                    print("You didn't enter a correct type of email")
                    continue
                else:
                    break
            Emails.append(address)

        # Now we will read in one more value from the user as Nickname and store in list in a loop
        nickname = []
        print("Now the last thing, lets pick a nick name")
        
        for i in range(0,ans):
            nickname.append(input("Enter a nickname, nothing crazy now..."))

        # Now create user classes based on all that input
        Usr = []
        for i in range(0, ans):
            Usr.append(User(Name[i], Emails[i], nickname[i]))

        print("Now we have ", ans, "Users in a list\n")

        # Method called to display users in a nice format
        displayUsers(Usr)

        if(input("Would you like to save these users to a file Y/n?\n") == "Y"):
            saveToDisk(Usr)
    
    else:
        print("We loaded users list")

        # Method called to display users in a nice format
        displayUsers(Usr)
    
    while(True):
        response = input("Would you like to make an Mod User? Enter Y/n")
        if(response == "Y"):
            

if __name__ == "__main__":
    main()