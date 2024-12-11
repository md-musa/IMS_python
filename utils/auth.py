def authenticate_user(store):
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in store.users:
        if user.username == username and user.getPassword() == password:
            print(f"+----------------------------------------------+")
            print(f"| UserName: {username}    Role: {user.role}    |")
            print(f"+----------------------------------------------+\n")
            return user
    print("Invalid username or password! Please try again.")
    return None