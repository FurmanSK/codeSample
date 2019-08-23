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

# Imports
import re
import json
import getpass
from users import *
from mods import *

#--------------------------Methods------------------------#

def displayUsers(userList):
    """Displays a list of the users created.

    Takes in a list of User Objects and outputs them in pretty format.
    
    Returns nothing"""

    print("---------------------------------")
    for id, u in enumerate(userList):
        print("User ID = ", id)
        print("Name = ", u.getName())
        print("email = ", u.getEmail())
        print("Nickname = ", u.getNickname())
        print("---------------------------------")

def saveToDisk(userList):
    """Saves User List to flat file

    Takes in User List and saves to file in JSON format
    
    Returns nothing"""

    with open("savedUsers.txt", 'w') as fp:
        fp.truncate()
        for u in userList:
            fp.writelines(u.toJson()+"\n")
    print("Saved so you can import this User List next time!\n")

def login(mList):
    """Prompts user for Mod login
    
    Takes in Mods list to verify against

    Returns a Mods object of current Mod if valid, None if they didn't login correctly
    """
    print("Logging in system\n")
    username = input("Enter your Mod user name:")
    passwd = getpass.getpass()

    for m in mList:
        if(m.Name == username and m.passwd == passwd):
            mod = m
        else: 
            mod = None
    
    return mod


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
    
    # Create or Read in mods list
    print("\n-----------------------------\nLoading a mods list\n")

    ModsList = importMods()
    curMod = login(ModsList)
    if(curMod):
        print("Login successful\n")
        while(True):
            print("------------------------------")
            print("What would you like to do?\n")
            print("C - Create new user")
            print("D - Delete user")
            print("S - Save users")
            print("SC - Start MySQL Container")
            print("Q - Quit program")
            print("------------------------------")
            choice = input("Choice: ")

            if(choice == "C"):
                Usr.append(createUser())
            if(choice == "D"):
                displayUsers(Usr)
                id = int(input("Pick the ID to delete:"))
                Usr = curMod.deleteUser(Usr, id)
            if(choice == "S"):
                print("Saving to disk...")
                saveToDisk(Usr)

    else:
        print("Login failed. Try again. Staying in user mode")
        print("Would you like to add a post?")


if __name__ == "__main__":
    main()