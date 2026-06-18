# rgistration function
from Password_checker.pwd_check import is_strong_password
from Hashed_password.hash import hash_password
from Audit.audit import log_event
def register_user():

    username = input ("Please enter a Username:")
    # check if username already exists
    with open("users.txt", "a+") as user_file:
        user_file.seek(0)
        users = user_file.readlines()
    
    for user in users:
        stored_username = user.strip().split(":")[0]
        if username == stored_username:
            print("Username already exists! Please choose another.")
            return
    password = input ("Please enter a Password:")

    is_valid, feedback = is_strong_password(password)
    if not is_valid:
        print("Password is not strong enough")
        print(feedback)
        log_event(f"Registration failed for user {username}")
        return
    # hash the password
    hashed_password = hash_password(password)

    with open("users.txt", "a") as user_file:
        user_file.write(f"{username}:{hashed_password}\n")
    
    print("User Registration was Successful")
    log_event(f"{username} successfully registered")
