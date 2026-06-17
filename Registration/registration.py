# rgistration function
def register_user():

    username = input ("Please enter a Username:")
    password = input ("Please enter a Password:")

    with open("users.txt", "a") as user_file:
        user_file.write(f"{username}:{password}\n")
    
    print("User Registration was Successful")
