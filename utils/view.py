from tabulate import tabulate

def print_table(obj_list):
    if not obj_list:
        print("No data available to display.")
        return
    
    # Convert list of objects to list of dictionaries
    data = [obj.__dict__ for obj in obj_list]
    
    # Extract headers dynamically from the first object's attributes
    headers = data[0].keys()
    print(tabulate(data, headers=headers, tablefmt="grid"))
