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

    def test_authMod_correct(self):
        correct_mod = self.mod[0]

        self.assertEqual(authMod("root", "root", self.mod), correct_mod)
    
    def test_authMod_failed(self):
        correct_mod = None

        self.assertEqual(authMod("root", "r", self.mod), correct_mod)