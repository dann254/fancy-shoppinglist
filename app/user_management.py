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
