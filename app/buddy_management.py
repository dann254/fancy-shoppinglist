class BuddyManager(object):
    #friend creations

    def __init__(self):
        # initialize list to contain friends
        self.buddies = []
    #hanle creaton
    def add_new_buddy(self, parent, name):
        buddy_holder = {}
        if name:
            buddy_holder[parent] = name
            buddy_holder[name] = parent
            self.buddies.append(buddy_holder)
            return "success"
        else:
            return "blank_entry"


    #handle return of the friends
    def return_buddies(self):
        return self.buddies

    def delete_buddy(self, parent, name):
        counter=0
        default=""
        for i in self.buddies:
            if i.get(parent, default)==name:
                self.buddies.pop(counter)
                return "success"
            counter=counter+1
        return "error"
