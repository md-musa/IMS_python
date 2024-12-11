def sales_associate_menu(sa, store):
    while True:
        print("\nSales Associate Menu:")
        print("1. View Inventory")
        print("2. Search Item")
        print("3. Create Sale")
        print("4. View Low Stock Items")
        print("5. Add item")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                sa.view_inventory(store)
            elif choice == 2:
                sa.search_item(store)
            elif choice == 3:
                sa.create_sale(store)
            elif choice == 4:
                sa.get_low_stock_items(store)
            elif choice == 5:
                sa.add_item(store)
            elif choice == 6:
                print("Exiting the application. Goodbye!")
                return True
            else:
                print("⚠ Invalid choice!")
        except ValueError as e:
            print("⚠ Invalid input! Please enter a number.")
        except Exception as e:
            print(f"⚠ An error occurred: {e}")





def manager_menu(manager, store):
    while True:
        print("\nManager Menu:")
        print("1. Add a User")
        print("2. Delete a User")
        print("3. View Users")
        print("4. Analyze Sales")
        print("5. View Transactions")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                manager.add_user(store)
            elif choice == 2:
                manager.delete_user(store)
            elif choice == 3:
                manager.view_users(store)
            elif choice == 4:
                manager.analyze_sales(store)
            elif choice == 5:
                manager.view_transactions(store)
            elif choice == 6:
                print("Exiting the application. Goodbye!")
                return True
            else:
                print("⚠ Invalid choice!")
        except ValueError:
            print("⚠ Invalid input! Please enter a number.")
        except Exception as e:
            print(f"⚠ sAn error occurred: {e}")


