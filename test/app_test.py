#this is the test form.
#some data like login and register are verified from mock_data.py
import unittest
# import all the required classes for testing
from app.user_management import UserManager
from app.list_management import ListManager

# these are the tests for user registrations
class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.user_manager=UserManager()
    #test 1
    #this is a test for successful registration of a user. the test should receive success.
    def successful_registration_test(self):
        result = self.user_manager.register_new_user("user","user@mail","monkey", "monkey")
        self.assertTrue("success"==result)
    #test 2
    #this is a test for unsuccessful registration of a user. the test should fail if it receives success.
    def failed_registration_test(self):
        result = self.user_manager.register_new_user("raider","user@mail","monker", "monkey")
        self.assertFalse("success"==result)
    #test 3
    #this is a test for the two passwords given by user at registration. the test should receive password_error if the passwords dont match.
    def confirm_password_test(self):
        result = self.user_manager.register_new_user("raider","user@mail","monker", "monkey")
        self.assertEqual("password_error", result)
    #test 4
    #this is a test fto see if user alredy exists. the test should receive u_email_error if the user exists.
    def existing_user_test(self):
        self.user_manager.register_new_user("raider","user@mail","monkey", "monkey")
        result = self.user_manager.register_new_user("raider","user@mail","monkey", "monkey")
        self.assertEqual("u_email_error", result)

# these are the tests for user login
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.user_manager=UserManager()
    #test 5
    #this is a test for successful login. the test should receive success.
    def successful_login_test(self):
        self.user_manager.register_new_user("user","user@mail","monkey", "monkey")
        result = self.user_manager.login("user","monkey")
        self.assertTrue("success"==result)
    #test 6
    #this is a test for unsuccessful login. the test should fail if it receives success.
    def failed_login_test(self):
        result = self.user_manager.login("raider", "monkey")
        self.assertFalse("success"==result)

# these are the tests for shoppinglists
class ShoppinglistTest(unittest.TestCase):
    def setUp(self):
        self.list_manager=ListManager()
    #test 7
    #this is a test for successful creation of a shoppinglist.
    def successful_list_creation_test(self):
        result = self.list_manager.create_new_shoppinglist("kitchenware", "user")
        self.assertTrue("success"==result)
    #test 8
    #this is a test for unsuccessful list creation
    def failed_list_creation_test(self):
        result = self.list_manager.create_new_shoppinglist("", "")
        self.assertFalse("success"==result)

if __name__ == '__main__':
    unittest.main()
