# this file contains all the required functions to run the app

from app.mock_data import User

class FormSubmission(object):
    def after_user_submit_register(self, username, email, password, confirm_pass):
        if UserRegister().check_for_blanks(username, email, password, confirm_pass)==True:
            if UserRegister().verify_password_similarity(password, confirm_pass) == True:
                if UserRegister().check_if_username_exists(username) == True:
                    if UserRegister().check_if_email_exists(email) == True:
                        return "success"
                    else:
                        return "email_error"

                else:
                    return "username_error"

            else:
                return "password_error"
        else:
            return "blank_entry"

class UserRegister():
    def check_for_blanks(self, username, email, password, confirm_pass):
        if username=="" or email=="" or password=="" or confirm_pass == "":
            return False
        else:
            return True
    def verify_password_similarity(self, password,confirm_pass):
        if password == confirm_pass:
            return True
        else:
            return False
    def check_if_username_exists(self, username):
        if User.user_name!=username:
            return True
        else:
            return False
    def check_if_email_exists(self, email):
        if User.user_email!=email:
            return True
        else:
            return False
