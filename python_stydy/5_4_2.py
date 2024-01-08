c_users=["a","b","c","d","e","admin"]
n_users=["f","g","a","c","z"]


if c_users:
    for user in n_users:
        if user in c_users:
            print(f"{user} is already used name. Please use other name.")
        else:
            print(f"user name {user} is possible to use.")
else:
    print("We need user.")




