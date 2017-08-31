#this is the test form.
#some data like login and register are verified from mock_data.py
import unittest
# import all the required classes for testing
from app.user_management import UserRegister, FormSubmission, UserLogin, AddList

class RegisterTest(unittest.TestCase):
    #test 1
    #this test verifies if, when password and confirm password are similar, the result is always TRUE.
    def test_simmilar_passwords_return_true(self):
        result = UserRegister().verify_password_similarity("monkey", "monkey")
        self.assertEqual(True, result)

    #test 2
    #This test is the inverse of test one and confirms if the result is false when the passwords dont match
    def test_different_passwords_return_false(self):
        result = UserRegister().verify_password_similarity("monkey", "baboon")
        self.assertEqual(False, result)
    #test 3
    #this test checks if a username exists and should receive True if the username doesnt exists
    def username_success_test(self):
        result = UserRegister().check_if_username_exists("user1")
        self.assertEqual(True, result)
    #test 4
    #this is the inverse of test 3 and reurns False if the username exists
    def username_fail_test(self):
        result = UserRegister().check_if_username_exists("user")
        self.assertEqual(False, result)
    #test 5
    #Test 5 and 6 work similar to test 3 and 4 above, but in this case, it verifies the email.
    def email_success_test(self):
        result = UserRegister().check_if_email_exists("user1@mail")
        self.assertEqual(True, result)
    #test 6
    def email_fail_test(self):
        result = UserRegister().check_if_email_exists("user@mail")
        self.assertEqual(False, result)
    #test 7
    #this test checks for blank entries and should receive True if no blanks are found
    def blanks_success_test(self):
        result = UserRegister().check_for_blanks("name", "user1@mail", "password", "cpassword")
        self.assertEqual(True, result)
    #test 8
    #is the inverse of test 7 and receives False if there are blanks.
    def blanks_fail_test(self):
        result = UserRegister().check_for_blanks("", "user1@mail", "", "cpassword")
        self.assertEqual(False, result)
    #test 9
    #test 9 and 10 summarize all the above tests and check for successful and unsuccessful user registrations.
    def sucessful_register_test(self):
        result = FormSubmission().after_user_submit_register("name", "user1@mail", "password", "password")
        self.assertEqual("success", result)
    #test 10
    def failed_register_test(self):
        result = FormSubmission().after_user_submit_register("", "user1@mail", "password", "")
        self.assertFalse("success"==result)

class LoginTest(unittest.TestCase):
    #test 11
    #test 11 and 12 check for blanks in user login
    def login_blanks_success_test(self):
        result = UserLogin().check_for_blanks("name", "password")
        self.assertEqual(True, result)
    #test 12
    def login_blanks_fail_test(self):
        result = UserLogin().check_for_blanks("", "password")
        self.assertEqual(False, result)
    #test 13
    #these tests check for successful and unsuccessful user login respectively.
    def sucessful_login_test(self):
        result = FormSubmission().after_login_submit("user", "password")
        self.assertEqual("success", result)
    #test 14
    def failed_login_test(self):
        result = FormSubmission().after_login_submit("user2","password")
        self.assertFalse("success"==result)

class ShoppinglistTest(unittest.TestCase):
    #test 15
    #these check if an added name is a blank and respond accordingly
    def addlist_blanks_success_test(self):
        result = AddList().check_for_blanks("name")
        self.assertEqual(True, result)
    #test 16
    def addlists_blanks_fail_test(self):
        result = AddList().check_for_blanks("")
        self.assertEqual(False, result)
    #test 17
    #test 17 and 18 these check if a list name already exists
    def non_existinglist_test(self):
        result = AddList().check_for_duplicate("clothes")
        self.assertEqual(True, result)
    #test 18
    def existinglist_test(self):
        result = AddList().check_for_duplicate("kitchenware")
        self.assertEqual(False, result)
    #test 19
    #test check how successful and unsuccessful list additions workout
    def successful_addlist_test(self):
        result = FormSubmission().after_add_list("list2")
        self.assertEqual("success",result)
    #test 20
    def failed_addlist_test(self):
        result = FormSubmission().after_add_list("kitchenware")
        self.assertFalse("success"==result)

if __name__ == '__main__':
    unittest.main()
