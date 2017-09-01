# this file contains all the required functions to run the app


class UserManager(object):
    #user registration and logging in

    def __init__(self):
        # initialize list to containusers
        self.user_list = []
    #hanle verification and registration
    def register_new_user(self, username, email, password, cpassword):
        user_holder = {}
        existance = False
        if password == cpassword:
            for user in self.user_list:
                if username == user['username'] or  email == user['email']:
                        existance = True
                        break
            if existance == False:
                user_holder['username'] = username
                user_holder['email'] = email
                user_holder['password'] = password
                self.user_list.append(user_holder)
                return "success"
            else:
                return "u_email_error"
        else:
            return "password_error"


    #hanle login verification and MaManagerlogin
    def login(self, username,password):
        #handle login session
        for user in self.user_list:
            if username == user['username'] and password == user['password']:
                return "success"
        else:
                return "details_error"

class FormSubmission(object):
    def after_add_list(self,listname):
        if AddList().check_for_blanks(listname)==True:
            if AddList().check_for_duplicate(listname)==True:
                return "success"
            else:
                return "duped_entry"

        else:
            return "blank_entry"


class AddList(object):
    def check_for_blanks(self,listname):
        if listname=="":
            return False
        else:
            return True
    #this check should happen based in the current user
    #def check_for_duplicate(self,listname):
    #    if listname == ShopList.list_name:
    #        return False
    #    else:
    #        return True
