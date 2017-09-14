class ListManager(object):
    #shoppinglist creations

    def __init__(self):
        # initialize list to contain shoppinglists
        self.shoppinglists = []
    #hanle creaton
    def create_new_shoppinglist(self, name, owner_name):
        shoppinglist_holder = {}
        if name:
            if len(self.shoppinglists)==0:
                list_id=1
            else:
                list_id=int(self.shoppinglists[-1]['id'])+1
            shoppinglist_holder['name'] = name
            shoppinglist_holder['id'] = list_id
            shoppinglist_holder['ownername'] = owner_name
            shoppinglist_holder['shared'] = False
            shoppinglist_holder['zone'] = ""
            self.shoppinglists.append(shoppinglist_holder)
            return "success"
        else:
            return "blank_entry"


    #handle return of the shoppinglist user
    def return_shopping_list(self):
        return self.shoppinglists
    #handle shopping list sharing and unsharing
    def share_shoppinglist(self, list_id):
        counter=0
        for i in self.shoppinglists:
            if int(i['id'])==int(list_id):
                if i['shared']==False:
                    self.shoppinglists[counter]['shared']=True
                    return "success"
                else:
                    self.shoppinglists[counter]['shared']=False
                    return "success"
            counter=counter+1

        return "error"
    #handle updates on shoppinglist name
    def update_shoppinglist(self, list_id, new_name):
        counter=0
        for i in self.shoppinglists:
            if int(i['id'])==int(list_id):
                self.shoppinglists[counter]['name']=new_name
                return "success"
            counter=counter+1

        return "error"

    #handle updates on shoppingzone
    def update_zone(self, list_id, szone):
        counter=0
        for i in self.shoppinglists:
            if int(i['id'])==int(list_id):
                self.shoppinglists[counter]['zone']=szone
                return "success"
            counter=counter+1

        return "error"

    def delete_list(self, list_id):
        counter=0
        for i in self.shoppinglists:
            if int(i['id'])==int(list_id):
                self.shoppinglists.pop(counter)
                return "success"
            counter=counter+1
        return "error"
