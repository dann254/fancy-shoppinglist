# this file contains all the required functions to run the app

#import test data
from app.mock_data import User, ShopList

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
    def after_login_submit(self, username,password):
        if UserLogin().check_for_blanks(username,password)==True:
            if UserLogin().verify_login_details(username,password)==True:
                return "success"
            else:
                return "details_error"
        else:
            return "blank_entry"
    def after_add_list(self,listname):
        if AddList().check_for_blanks(listname)==True:
            if AddList().check_for_duplicate(listname)==True:
                return "success"
            else:
                return "duped_entry"

        else:
            return "blank_entry"

class UserRegister(object):
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

class UserLogin(object):
    def check_for_blanks(self, username, password):
        if username==""or password=="":
            return False
        else:
            return True
    def verify_login_details(self, username,password):
        if username == User.user_name and password== User.user_password:
            return True
        else:
            return False

class AddList(object):
    def check_for_blanks(self,listname):
        if listname=="":
            return False
        else:
            return True
    #this check should happen based in the current user
    def check_for_duplicate(self,listname):
        if listname == ShopList.list_name:
            return False
        else:
            return True
