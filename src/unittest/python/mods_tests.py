#---------------------------------------------------------#
#   filename: mods_tests.py
#   Author: Wes Forman
#   Description: This is unit test for mods Class methods.
#---------------------------------------------------------

import sys
import unittest
from unittest import mock
from main import *
from users import *

class modsTest(unittest.TestCase):

    def setUp(self):
        # Creat mod object
        self.mod = Mods('root', 'root@host.com', 'root', 'root')

        # Creat list of User class objects
        self.usrList = [User("Wes", "wes@test.com", "West"), User("Test2", "test@test.com", "tests")]
    
    def test_createNewUser(self):

        expectedUser = User('Jim', 'jim@host.com', 'jimbo')
        
        with mock.patch('users.input', return_value="Jim"), mock.patch('users.input', return_value='jim@host.com'), mock.patch('users.input', return_value='jimbo'):
            retUsrList = self.mod.createNewUser(self.usrList, createUser())
            self.assertEqual(len(retUsrList), 3)
            self.assertEqual(retUsrList[-1], expectedUser)
            self.usrList.pop() # remove before next text


    def test_deleteUser(self):
        with mock.patch('main.input', return_value=0):
            retUsrList = self.mod.deleteUser(self.usrList, 0)
            self.assertEqual(len(retUsrList), 1)
            self.assertNotEqual(retUsrList[0].getName(), "Wes")
