#---------------------------------------------------------#
#   filename: login_tests.py
#   Author: Wes Forman
#   Description: This is unit test for login method
#   which compares the input and output to the test case.
#   I use mock.patch to patch the input and getpass methods
#---------------------------------------------------------

import sys
import unittest
from unittest import mock
from main import *
from users import *

class loginTest(unittest.TestCase):

    def setUp(self):
        # Create a modList to pass to login()
        self.mod = [Mods("root", "root@host.com", "root", "root")]

    def test_login_correct(self):
        correct_mod = self.mod[0]

        with mock.patch('main.input', return_value='root'), mock.patch('getpass.getpass', return_value="root"):
            self.assertEqual(login(self.mod), correct_mod)
    
    def test_login_failed(self):
        correct_mod = None

        with mock.patch('main.input', return_value='root'), mock.patch('getpass.getpass', return_value="r"):
            self.assertEqual(login(self.mod), correct_mod)