import unittest
from app.user_management import UserRegister

class password_test(unittest.TestCase):
    def test_simmilar_passwords_return_true(self):
        result = UserRegister().verify_password_similarity("monkey", "monkey")
        self.assertEqual(True, result)

if __name__ == '__main__':
    unittest.main()
