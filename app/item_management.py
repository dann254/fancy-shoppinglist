class ItemManager(object):
    #items creations

    def __init__(self):
        # initialize list to contain items
        self.items = []
    #hanle creation
    def create_new_item(self, name,price, quantity, list_id):
        item_holder = {}
        if name:
            item_holder['name'] = name
            item_holder['price'] = price
            item_holder['quantity'] = quantity
            item_holder['list_id'] = list_id
            item_holder['id'] = len(self.items)+1
            self.items.append(item_holder)
            return "success"
        else:
            return "blank_entry"


    #handle return all items
    def return_items(self):
        return self.items


    def delete_item(self, item_id):
        counter=0
        for i in self.items:
            if int(i['id'])==int(item_id):
                self.items.pop(counter)
                return "success"
            counter=counter+1
        return "error"
