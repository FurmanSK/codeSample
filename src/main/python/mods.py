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

    def __init__(self, name, email, nickname):
        self.Name = name
        self.email = email
        self.Nickname = nickname
        self.adminAccess = True

    def deleteUser(self, userList, index):
        """ Deletes a User Object from the userList.

        Returns list"""

        if(adminAccess):
            ret = userList.pop(index)
            print("User has been deleted")
        
        return userList