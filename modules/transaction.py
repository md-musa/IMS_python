from datetime import datetime
from tabulate import tabulate




class Transaction():
    def __init__(self, item_id, quantity, total_price):
        self.trans_id = f"TRANS-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.item_id = item_id
        self.quantity = quantity
        self.total_price = total_price
        self.timestamp = datetime.now()

    def generate_invoice(self):
        invoice_data = [
            ["Transaction ID", self.trans_id],
            ["Item ID", self.item_id],
            ["Quantity", self.quantity],
            ["Total Price", f"${self.total_price:.2f}"],
            ["Timestamp", self.timestamp.strftime('%Y-%m-%d %H:%M:%S')]
        ]
        
        print("\nInvoice Details:")
        print(tabulate(invoice_data, headers=["Field", "Value"], tablefmt="grid"))
   
    def to_dict(self):
         """Convert object to dictionary, converting datetime to string."""
         data = self.__dict__.copy()
         data["timestamp"] = self.timestamp.isoformat()  # Convert datetime to ISO string
         return data
   
     
    
    