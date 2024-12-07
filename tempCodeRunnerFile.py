current_user = None
    while not current_user:
        current_user = authenticate_user(store)
