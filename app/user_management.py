
class UserRegister(object):
    def verify_password_similarity(self, password,confirm_pass):
        if password == confirm_pass:
            return True
        else:
            return False
