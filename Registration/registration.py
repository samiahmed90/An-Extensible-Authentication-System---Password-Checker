# rgistration function
from Password_checker.pwd_check import is_strong_password
from Hashed_password.hash import hash_password
from Audit.logs import log_event
def register_user():

    username = input ("Please enter a Username:")
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
