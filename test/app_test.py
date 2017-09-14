#this is the test form.
#some data like login and register are verified from mock_data.py
import unittest
# import all the required classes for testing
from app.user_management import UserManager
from app.list_management import ListManager
from app.buddy_management import BuddyManager
from app.zone_management import ZoneManager
from app.item_management import ItemManager

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
    #test 9
    #this is a test for list deletion
    def shoppinglist_deletion_test(self):
        self.list_manager.create_new_shoppinglist("kitchenware", "user")
        result = self.list_manager.delete_list("1")
        self.assertTrue("success"==result)
    #test 10
    #this is a test for list Share status change
    def share_test(self):
        self.list_manager.create_new_shoppinglist("kitchenware", "user")
        result = self.list_manager.share_shoppinglist("1")
        result2 = self.list_manager.share_shoppinglist("1")
        self.assertTrue("success"==result)
        self.assertTrue("success"==result2)

    #test 11
    #this is a test for list update
    def shoppinglist_update_test(self):
        self.list_manager.create_new_shoppinglist("kitchenware", "user")
        result = self.list_manager.update_shoppinglist("1", "cutlery")
        self.assertTrue("success"==result)

    #test 12
    #this is a test for zoning a shoppinglist
    def shoppinglist_zoning_test(self):
        self.list_manager.create_new_shoppinglist("kitchenware", "user")
        result = self.list_manager.update_zone("1", "adlife")
        self.assertTrue("success"==result)

# this is a test for buddies
class BuddyTest(unittest.TestCase):
    def setUp(self):
        self.user_manager=UserManager()
        self.buddy_manager=BuddyManager()
    #test 13
    #this is a test for friend addition and unfriending
    def add_and_unfriend_test(self):
        self.user_manager.register_new_user("user","user@mail","monkey", "monkey")
        self.user_manager.register_new_user("user2","user2@mail","monkey", "monkey")
        result = self.buddy_manager.add_new_buddy("user","user2")
        result2 = self.buddy_manager.add_new_buddy("user","user2")
        self.assertTrue("success"==result)
        self.assertTrue("success"==result2)

# this is a test for Zones
class ZoneTest(unittest.TestCase):
    def setUp(self):
        self.zone_manager=ZoneManager()
    #test 14
    #this is a test for zone addition and deletion
    def add_and_delete_zone_test(self):
        result = self.zone_manager.create_new_zone("user","adlife")
        result2 = self.zone_manager.delete_zone("user","adlife")
        self.assertTrue("success"==result)
        self.assertTrue("success"==result2)

# this are tests for items
class ItemTest(unittest.TestCase):
    def setUp(self):
        self.item_manager=ItemManager()
    #test 15
    #this is a test for item addition and deletion
    def add_and_delete_item_test(self):
        result = self.item_manager.create_new_item("item1","20","1","1")
        result2 = self.item_manager.delete_item("1")
        self.assertTrue("success"==result)
        self.assertTrue("success"==result2)

    #test 16
    #this is a test for item update
    def update_item_test(self):
        self.item_manager.create_new_item("item1","20","1","1")
        result = self.item_manager.update_item("1", "item_updated","65","3")
        self.assertTrue("success"==result)

if __name__ == '__main__':
    unittest.main()
