import numpy as np
from tabulate import tabulate
from modules.transaction import Transaction
from utils.customError import InsufficientStockError

class User:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role


class SalesAssociate(User):
    def __init__(self, user_id, username, password, role):
        super().__init__(user_id, username, password, role)
    
    def view_inventory(self, store):
        print(store.items[0].__dict__)
        if not store.items:
             print("The inventory is empty.")
             return

        print("\nStore Inventory:")
        data = [
          {"Item ID": item.item_id, "Name": item.name, "Price": item.price, "Quantity": item.quantity} for item in store.items]
        print(tabulate(data, headers="keys", tablefmt="grid"))

    def search_item(self, store):
        product_name = input("Enter product name: ").lower()
        found_items = [item for item in store.items if product_name in item.name.lower()]
        if found_items:
            print("\nFound Items:")
            item_data = [{"Item ID": item.item_id, "Name": item.name, "Price": item.price, "Quantity": item.quantity} for item in found_items]
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
            print(transaction.generate_invoice())

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
    
    def add_item(self):
        pass



class Manager(User):
    def __init__(self, user_id, username, password, role):
        super().__init__(user_id, username, password, role)

    def add_user(self, store):
        user_id = input("Enter new user's ID: ")
        username = input("Enter new user's username: ")
        password = input("Enter new user's password: ")
        role = input("Enter new user's role (Manager/SalesAssociate): ")

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

        if user_to_remove:
            store.users.remove(user_to_remove)
            print(f"User with ID {user_id} deleted successfully.")
        else:
            print(f"User with ID {user_id} not found.")

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
        trs_totals = [t.total_price for t in store.transactions]
        if trs_totals:
            avg_sales = np.mean(trs_totals)
            total_sales = np.sum(trs_totals)
            max_sale = np.max(trs_totals)

            print(f"Average Sale: ${avg_sales:.2f}")
            print(f"Total Sales: ${total_sales:.2f}")
            print(f"Highest Sale: ${max_sale:.2f}")
        else:
             print("No transactions available for analysis.")


