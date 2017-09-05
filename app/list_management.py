class ListManager(object):
    #shoppinglist creations

    def __init__(self):
        # initialize list to contain shoppinglists
        self.shoppinglists = []
    #hanle creaton
    def create_new_shoppinglist(self, name):
        shoppinglist_holder = {}
        existance = False
        if name:
            shoppinglist_holder['name'] = name
            shoppinglist_holder['id'] = len(self.shoppinglists)+1
            self.shoppinglists.append(shoppinglist_holder)
            return "success"
        else:
            return "blan_entry"


    #handle return of the shoppinglist to other users
    def return_shopping_list(self):

        if self.shoppinglists != []:
            return self.shoppinglists
        else:
                return "none"
