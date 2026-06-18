# login function
from Hashed_password.hash import hash_password
from Audit.audit import log_event


def login_user():
    username = input ("Please enter a username:")
    password = input ("Please enter a password:")

    with open ("users.txt", "r") as user_file:
        users = user_file.readlines()
        
    for user in users:
        stored_username, stored_password = user.strip().split(":")
        if username == stored_username and hash_password(password) == stored_password:
            print("Login Successful")
            log_event(f"{username} successfulyy logged in")
            return
        
    print("Invalid Username or Password")
    log_event(f"Failed login attempt for the user {username}")
