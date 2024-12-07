
class Store:
    def __init__(self):
        self.users = []
        self.items = []
        self.transactions = []
    
    def add_user(self, user):
        self.users.append(user)
    
    def add_item(self, item):
        self.items.append(item)
        
    def add_transaction(self, trs):
        self.transactions.append(trs)
    
    def find_item_by_id(self, item_id):
        item = next((item for item in self.items if item.item_id == item_id), None)        
        if item:
            return item
        else:
            print(f"Item with ID {item_id} not found.")
            return None

 

   
