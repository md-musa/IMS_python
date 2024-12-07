def authenticate_user(store):
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in store.users:
        if user.username == username and user.password == password:
            print(f"\nWelcome, {user.username}! You are logged in as {user.role}.")
            return user
    print("Invalid username or password! Please try again.")
    return None