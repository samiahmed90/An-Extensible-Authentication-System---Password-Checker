# login function

def login_user():
    username = input ("Please enter a username:")
    password = input ("Please enter a password:")

    with open ("users.txt", "r") as user_file:
        users = user_file.readlines()
        
    for user in users:
        stored_username, stored_password = user.strip().split(":")
        if username == stored_username and password == stored_password:
            print("Login Successful")
            return
    print("Invalid Username or Password")
    
