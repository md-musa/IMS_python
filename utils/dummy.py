from modules.user import Manager, SalesAssociate
from modules.item import Item
from modules.transaction import Transaction

def add_dummy_data(store, current_user):
    # Dummy Data for Users
    manager = Manager("1", "manager", "manager123", "Manager")
    sales_associate1 = SalesAssociate("2", "associate1", "pass1", "SalesAssociate")
    sales_associate2 = SalesAssociate("3", "associate2", "pass2", "SalesAssociate")
    
    current_user.add_user(manager)
    current_user.add_user(sales_associate1)
    current_user.add_user(sales_associate2)

    # Dummy Data for Items
    current_user.add_item(Item("101", "Laptop", 1000.0, 10))
    current_user.add_item(Item("102", "Mouse", 25.0, 50))
    current_user.add_item(Item("103", "Keyboard", 40.0, 30))
    current_user.add_item(Item("104", "Monitor", 150.0, 20))
    current_user.add_item(Item("105", "Printer", 300.0, 5))

    # Dummy Data for Transactions
    current_user.add_transaction(Transaction("101", 2, 2000.0))
    current_user.add_transaction(Transaction("102", 5, 125.0))
