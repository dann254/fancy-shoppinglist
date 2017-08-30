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
    def blank_check_success(self):
        result = UserRegister().check_for_blanks("name", "mail@mail","passord","cpassword")
        self.assertEqual(True, result)

    #test 4
    def blank_check_fail(self):
        result = UserRegister().check_for_blanks("name", "mail@mail","cpassword")
        self.assertEqual(False, result)

if __name__ == '__main__':
    unittest.main()
