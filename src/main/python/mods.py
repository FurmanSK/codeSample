#!/usr/bin/python3

#---------------------------------------------------------#
#  App Title: Code Samples
#  File: mods.py
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
from main import User

class Mods(User):

    adminAccess = False
    passwd = ""

    def __init__(self, name, email, nickname, passwd):
        self.Name = name
        self.email = email
        self.Nickname = nickname
        self.adminAccess = True
        self.passwd = passwd

    def deleteUser(self, userList, index):
        """ Deletes a User Object from the userList.

        Returns list"""

        if(self.adminAccess):
            ret = userList.pop(index)
            print("User has been deleted")
        
        return userList
    
    def createNewUser(self, userList, UserObj):
        """ Creates new User Class Object and returns User Class Object
        
        Inputs: name(str), email(str), nickname(str)

        returns User Class Object
        """
        if(self.adminAccess):
            userList.append(UserObj)
        
        return userList

#--------------------Mods Lib Methods--------------------#
def importMods():
    """Imports mods List from disk

    Looks for mods.txt file and creates a list of Class objects

    Returns a list of Mods class objects if mods.txt exists else returns None"""
    try:
        with open("mods.txt", "r") as fp:
            ModsList = []
            for line in fp:
                #expload string on comma
                lineArray = line.split(",")
                #Split each var up
                name = lineArray[0].split(":")[1]
                email = lineArray[1].split(":")[1]
                nickname = lineArray[2].split(":")[1]
                passwd = lineArray[3].split(":")[1]
                # clean up end of nickname string
                passwd = passwd.strip(" }\n")
                ModsList.append(Mods(name, email, nickname, passwd))
    except IOError:
        ModsList = None
    return ModsList