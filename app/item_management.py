class ItemManager(object):
    #items creations

    def __init__(self):
        # initialize list to contain items
        self.items = []
    #hanle creation
    def create_new_item(self, name,price, quantity, list_id):
        item_holder = {}
        if name:
            if len(self.items)==0:
                item_id=1
            else:
                item_id=int(self.items[-1]['id'])+1
            item_holder['name'] = name.lower()
            item_holder['price'] = price
            item_holder['quantity'] = quantity
            item_holder['list_id'] = list_id
            item_holder['id'] = item_id
            self.items.append(item_holder)
            return "success"
        else:
            return "blank_entry"

    #handle updates on items
    def update_items(self, item_id, uname,uprice,uquantity):
        counter=0
        for i in self.items:
            if int(i['id'])==int(item_id):
                self.items[counter]['name']=uname
                self.items[counter]['price']=uprice
                self.items[counter]['quantity']=uquantity
                return "success"
            counter=counter+1

        return "error"

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
