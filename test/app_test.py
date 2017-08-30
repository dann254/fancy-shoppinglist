#this is the test form.
#some data like login and register are verified from mock_data.py
import unittest
from app.user_management import UserRegister, FormSubmission, UserLogin, AddList

class RegisterTest(unittest.TestCase):
    #test 1
    def test_simmilar_passwords_return_true(self):
        result = UserRegister().verify_password_similarity("monkey", "monkey")
        self.assertEqual(True, result)

    #test 2
    def test_different_passwords_return_false(self):
        result = UserRegister().verify_password_similarity("monkey", "baboon")
        self.assertEqual(False, result)
    #test 3
    def username_success_test(self):
        result = UserRegister().check_if_username_exists("user1")
        self.assertEqual(True, result)
    #test 4
    def username_fail_test(self):
        result = UserRegister().check_if_username_exists("user")
        self.assertEqual(False, result)
    #test 5
    def email_success_test(self):
        result = UserRegister().check_if_email_exists("user1@mail")
        self.assertEqual(True, result)
    #test 6
    def email_fail_test(self):
        result = UserRegister().check_if_email_exists("user@mail")
        self.assertEqual(False, result)
    #test 7
    def blanks_success_test(self):
        result = UserRegister().check_for_blanks("name", "user1@mail", "password", "cpassword")
        self.assertEqual(True, result)
    #test 8
    def blanks_fail_test(self):
        result = UserRegister().check_for_blanks("", "user1@mail", "", "cpassword")
        self.assertEqual(False, result)
    #test 9
    def sucessful_register_test(self):
        result = FormSubmission().after_user_submit_register("name", "user1@mail", "password", "password")
        self.assertEqual("success", result)
    #test 10
    def failed_register_test(self):
        result = FormSubmission().after_user_submit_register("", "user1@mail", "password", "")
        self.assertFalse("success"==result)

class LoginTest(unittest.TestCase):
    #test 11
    def login_blanks_success_test(self):
        result = UserLogin().check_for_blanks("name", "password")
        self.assertEqual(True, result)
    #test 12
    def login_blanks_fail_test(self):
        result = UserLogin().check_for_blanks("", "password")
        self.assertEqual(False, result)
    #test 13
    def sucessful_login_test(self):
        result = FormSubmission().after_login_submit("user", "password")
        self.assertEqual("success", result)
    #test 14
    def failed_login_test(self):
        result = FormSubmission().after_login_submit("user2","password")
        self.assertFalse("success"==result)

class ShoppinglistTest(unittest.TestCase):
    #test 15
    def addlist_blanks_success_test(self):
        result = AddList().check_for_blanks("name")
        self.assertEqual(True, result)
    #test 16
    def addlists_blanks_fail_test(self):
        result = AddList().check_for_blanks("")
        self.assertEqual(False, result)
    #test 17
    def non_existinglist_test(self):
        result = AddList().check_for_duplicate("clothes")
        self.assertEqual(True, result)
    #test 18
    def existinglist_test(self):
        result = AddList().check_for_duplicate("kitchenware")
        self.assertEqual(False, result)
    #test 19
    def successful_addlist_test(self):
        result = FormSubmission().after_add_list("list2")
        self.assertEqual("success",result)
    #test 20
    def failed_addlist_test(self):
        result = FormSubmission().after_add_list("kitchenware")
        self.assertFalse("success"==result)

if __name__ == '__main__':
    unittest.main()
