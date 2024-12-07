

def sales_associate_menu(sales_associate, store):
    while True:
        print("\nSales Associate Menu:")
        print("1. View Inventory")
        print("2. Search Item")
        print("3. Create Sale")
        print("4. View Low Stock Items")
        print("5. Logout")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                sales_associate.view_inventory(store)
            elif choice == 2:
                sales_associate.search_item(store)
            elif choice == 3:
                sales_associate.create_sale(store)
            elif choice == 4:
                sales_associate.get_low_stock_items(store)
            elif choice == 5:
                return
            elif choice == 6:
                print("Exiting the application. Goodbye!")
                exit()
            else:
                print("⚠ Invalid choice!")
        except ValueError:
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
        print("6. Logout")
        print("7. Exit")

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
                return
            elif choice == 7:
                print("Exiting the application. Goodbye!")
                exit()
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input! Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")


