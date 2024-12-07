from modules.store import Store
from modules.user import Manager, SalesAssociate
from modules.item import Item
from modules.transaction import Transaction
from utils.auth import authenticate_user
from utils.tasks import manager_menu
from utils.tasks import sales_associate_menu

store = Store()
ROLES = ("Manager", "SalesAssociate")

def add_dummy_data(store):
    manager = Manager("1", "musa-m", "musa", "Manager")
    store.add_user(manager)

    sales_associate1 = SalesAssociate("2", "musa-s", "musa", "SalesAssociate")
    sales_associate2 = SalesAssociate("3", "associate2", "pass2", "SalesAssociate")
    store.add_user(sales_associate1)
    store.add_user(sales_associate2)

    store.add_item(Item("101", "Laptop", 1000.0, 10))
    store.add_item(Item("102", "Mouse", 25.0, 50))
    store.add_item(Item("103", "Keyboard", 40.0, 30))
    store.add_item(Item("104", "Monitor", 150.0, 20))
    store.add_item(Item("105", "Printer", 300.0, 5))

    store.add_transaction(Transaction("101", 2, 2000.0))
    store.add_transaction(Transaction("102", 5, 125.0))
    store.add_transaction(Transaction("105", 3, 125.0))
    store.add_transaction(Transaction("104", 1, 125.0))

def main():
    print("\n-----Inventory Management System-----")
    add_dummy_data(store)

    current_user = None
    while not current_user:
        current_user = authenticate_user(store)


    while True:
        if current_user.role == "Manager":
            manager_menu(current_user, store)
        elif current_user.role == "SalesAssociate":
            sales_associate_menu(current_user, store)


if __name__ == "__main__":
    main()
