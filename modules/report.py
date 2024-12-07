from tabulate import tabulate
from datetime import datetime
from modules.store import Store

class Report(Store):
    def __init__(self, report_id, report_type, data):
        self.report_id = report_id
        self.report_type = report_type
        self.data = data

    def generate_inventory_report(self, store):
        return [
            {"Item ID": item.item_id, "Name": item.name, "Quantity": item.quantity}
            for item in store.items
        ]

    def generate_low_stock_report(self, store):
        return [
            {"Item ID": item.item_id, "Name": item.name, "Quantity": item.quantity}
            for item in store.items if item.quantity < 5
        ]

    def generate_sales_report(self, store):
        return store.transactions  # Assuming store.transactions contains all transaction data

    def print_inventory_report(self, store):
        inventory_data = self.generate_inventory_report(store)
        low_stock_data = self.generate_low_stock_report(store)
        total_items = sum(item.quantity for item in store.items)
        total_sold = sum(t.quantity for t in store.transactions)

        print("\nLow Stock Products (Quantity < 5):")
        if low_stock_data:
            print(tabulate(low_stock_data, headers="keys", tablefmt="grid"))
        else:
            print("All items are sufficiently stocked.")

        print(f"\nTotal Items Available: {total_items}")
        print(f"Total Items Sold: {total_sold}")

    def print_sales_report(self, store):
        sales_data = self.generate_sales_report(store)
        if not sales_data:
            print("\nNo sales data available.")
            return

        today = datetime.now().date()
        current_month = datetime.now().month
        total_today = sum(
            t.total_price for t in sales_data if t.date.date() == today
        )
        total_this_month = sum(
            t.total_price for t in sales_data if t.date.month == current_month
        )
        total_all_time = sum(t.total_price for t in sales_data)

        product_sales = {}
        for t in sales_data:
            product_sales[t.item_id] = product_sales.get(t.item_id, 0) + t.quantity

        product_sales_table = [
            {"Item ID": item_id, "Total Sold": quantity}
            for item_id, quantity in product_sales.items()
        ]

        print("\nSales Report:")
        print(f"Today's Sales Amount: {total_today}")
        print(f"This Month's Sales Amount: {total_this_month}")
        print(f"All-Time Sales Amount: {total_all_time}")

        print("\nProduct-Wise Total Sold:")
        print(tabulate(product_sales_table, headers="keys", tablefmt="grid"))
