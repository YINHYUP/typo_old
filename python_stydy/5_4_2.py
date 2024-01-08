"""
c_users=["A","B","C","D","E","ADMIN"]
n_users=["f","g","A","c","Z"]
c_users_lower=[name.lower() for name in c_users]
n_users_lower=[name.lower() for name in n_users]



if c_users_lower:
    for user in n_users_lower:
        if user in c_users_lower:
            print(f"{user} is already used name. Please use other name.")
        else:
            print(f"user name {user} is possible to use.")
else:
    print("We need user.")

"""

numbers=list(range(1,10))
numbers_2=[]
print(numbers)

"""
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    else:
        print(f"{number}th")
"""
for number in numbers:
    if number == 1:
        numbers_2.append ( f"{number}st" )
        print(numbers)
        print(numbers_2)
    elif number == 2:
        numbers_2.append ( f"{number}nd" )
        print(numbers)
        print(numbers_2)
    else:
        numbers_2.append ( f"{number}st" )
        print(numbers)
        print(numbers_2)


