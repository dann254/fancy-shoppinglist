import unittest
from app.user_management import UserRegister, FormSubmission

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
    #test 9
    def faild_register_test(self):
        result = FormSubmission().after_user_submit_register("", "user1@mail", "password", "password")
        self.assertFalse("success"==result)

if __name__ == '__main__':
    unittest.main()
