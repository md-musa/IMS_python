
class Item():
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_item(self, quantity):
        try:
            if quantity <= 0: 
                raise ValueError("Quantity must be greater than 0")
            self.quantity += quantity
        except ValueError as e:
            print(f"Error in updating item quantity: {e}")

    def is_stock_out(self):
        return self.quantity < 5
       
