import numpy as np
from tabulate import tabulate
from modules.transaction import Transaction
from utils.customError import InsufficientStockError
from modules.item import Item

class User:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.__password = password
        self.role = role
    def getPassword(self):
        return self.__password


class SalesAssociate(User):
    def __init__(self, user_id, username, __password, role):
        super().__init__(user_id, username, __password, role)
    
    def view_inventory(self, store):
        if not store.items:
             print("The inventory is empty.")
             return

        print("\nStore Inventory:")
        data = [
          {"Item ID": item.item_id, "Name": item.name, "Price": item.price, "Quantity": item.quantity} for item in store.items]
        print(tabulate(data, headers="keys", tablefmt="grid"))

    def search_item(self, store):
        pd_name = input("Enter product name: ").lower()
        items = [item for item in store.items if pd_name in item.name.lower()]
        if items:
            print("\nFound Items:")
            item_data = [{"Item ID": item.item_id, "Name": item.name, "Price": item.price, "Quantity": item.quantity} for item in items]
            print(tabulate(item_data, headers="keys", tablefmt="grid"))
        else:
            print("No items found with that name.")
    
    def create_sale(self, store):
        try:
            item_id = input("Enter the item ID: ")
            quantity = int(input("Enter the quantity: "))
            item = store.find_item_by_id(item_id)

            if not item:
                print("Item not found.")
                return

            if quantity <= 0:
                raise ValueError("Invalid quantity")
            
            if quantity > item.quantity: 
                raise InsufficientStockError(item.name, item.quantity)

            transaction = Transaction(item_id, quantity, quantity * item.price)
            store.transactions.append(transaction)
            item.quantity -= quantity

            print("Transaction created successfully!")
            transaction.generate_invoice()

        except Exception as e:
            print(f"Failed to create sale: {e}")

    def get_low_stock_items(self, store):
        items = list(filter(lambda item: item.quantity < 5, store.items))
        if items:
            print("\nLow Stock Items:")
            low_stock_data = [{"Item ID": item.item_id, "Name": item.name, "Quantity": item.quantity} for item in items]
            print(tabulate(low_stock_data, headers="keys", tablefmt="grid"))
        else:
            print("No low stock items.")
    
    def add_item(self, store):
        name = input("Enter item name: ")
        try:
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
        except ValueError:
            print("Invalid input. Price must be a number and quantity must be an integer.")
            return

        id = int(store.items[-1].item_id) + 1 if len(store.items) > 0 else 100
        item = Item(id, name, price, quantity)
        store.add_item(item)
        print(f"Item '{name}' added successfully with ID {id}.")

        



class Manager(User):
    def __init__(self, user_id, username, __password, role):
        super().__init__(user_id, username, __password, role)

    def add_user(self, store):
        username = input("Enter new user's username: ")
        password = input("Enter new user's password: ")
        role = input("Enter new user's role (Manager/SalesAssociate): ")
        
        isUserExist = any(user.username == username for user in store.users)
        if isUserExist:
            print("User already exists!")
            return

        user_id = int(store.users[-1].user_id)+1 if len(store.users) > 0 else 100
        
        if role.lower() == "manager":
            new_user = Manager(user_id, username, password, "Manager")
        elif role.lower() == "salesassociate":
            new_user = SalesAssociate(user_id, username, password, "SalesAssociate")
        else:
            print("Invalid role! User creation failed.")
            return

        store.add_user(new_user)
        print(f"User with ID {user_id} added successfully.")

    def delete_user(self, store):
        user_id = input("Enter the user ID to delete: ")
        user_to_remove = next((user for user in store.users if user.user_id == user_id), None)
        
        if user_to_remove == None:
            raise ValueError("User does not exist with this Id")

        store.users.remove(user_to_remove)
        print(f"User with ID {user_id} deleted successfully.")
        

    def view_users(self, store):
        if not store.users:
            print("No users found.")
            return

        print("\nList of Users:")
        user_data = [{"ID": user.user_id, "Username": user.username, "Role": user.role} for user in store.users]
        print(tabulate(user_data, headers="keys", tablefmt="grid"))

    def view_transactions(self, store):
        if not store.transactions:
            print("No transactions found.")
            return

        print("\nList of Transactions:")
        transaction_data = [
            {
                "Transaction ID": transaction.trans_id,
                "Item ID": transaction.item_id,
                "Quantity": transaction.quantity,
                "Total Price": transaction.total_price,
                "Timestamp": transaction.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            }
            for transaction in store.transactions
        ]
        print(tabulate(transaction_data, headers="keys", tablefmt="grid"))
    
    def analyze_sales(self, store):
        tp = [t.total_price for t in store.transactions]
        if tp:
            avg_sales = np.mean(tp)
            total_sales = np.sum(tp)
            max_sale = np.max(tp)

            print(f"Average Sale: ${avg_sales:.2f}")
            print(f"Total Sales: ${total_sales:.2f}")
            print(f"Highest Sale: ${max_sale:.2f}")
        else:
             print("No transactions available for analysis.")


# 15da2