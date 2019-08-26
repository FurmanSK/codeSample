#---------------------------------------------------------#
#   filename: mods_tests.py
#   Author: Wes Forman
#   Description: This is unit test for mods Class methods.
#---------------------------------------------------------

import sys
import unittest
import builtins
from unittest import mock
from main import *
from users import *

class modsTest(unittest.TestCase):

    userinput = (user for user in ['Jim', 'jim@host.com', 'jimbo'])

    def setUp(self):
        # Creat mod object
        self.mod = Mods('root', 'root@host.com', 'root', 'root')

        # Creat list of User class objects
        self.usrList = [User("Wes", "wes@test.com", "West"), User("Test2", "test@test.com", "tests")]
    
    def mock_input(self, prompt):
        return next(self.userinput)

    def test_createNewUser(self):

        expectedUser = User('Jim', 'jim@host.com', 'jimbo')
        
        with mock.patch('builtins.input', self.mock_input):
            retUsrList = self.mod.createNewUser(self.usrList, createUser())
            self.assertEqual(len(retUsrList), 3)
            self.assertEqual(retUsrList[-1].Name, expectedUser.Name)
            self.assertEqual(retUsrList[-1].email, expectedUser.email)
            self.assertEqual(retUsrList[-1].Nickname, expectedUser.Nickname)
            self.usrList.pop() # remove before next text


    def test_deleteUser(self):
        with mock.patch('main.input', return_value=0):
            retUsrList = self.mod.deleteUser(self.usrList, 0)
            self.assertEqual(len(retUsrList), 1)
            self.assertNotEqual(retUsrList[0].getName(), "Wes")