#---------------------------------------------------------#
#   filename: displayUsers_text.py
#   Author: Wes Forman
#   Description: This is unit test for displayUsers method
#   which compares the output to the test case.
#---------------------------------------------------------

import sys
import unittest
import io
from contextlib import redirect_stdout
from main import *
from users import *

class displayUsersTest(unittest.TestCase):
    
    def setUp(self):
        self.usr = [User("Wes", "wes@test.com", "West"), User("Test2", "test@test.com", "tests")]

    def test_display_users(self):
        txt_out = io.StringIO()

        with redirect_stdout(txt_out):
            displayUsers(self.usr)

        # build a output string
        outTestStr = """---------------------------------\nUser ID = 0\nName = Wes\nemail = wes@test.com\nNickname = West\n---------------------------------\nUser ID = 1\nName = Test2\nemail = test@test.com\nNickname = tests\n---------------------------------\n"""

        # Call assertEqual to test that we get the correct output
        self.assertEqual(txt_out.getvalue(), outTestStr)
        