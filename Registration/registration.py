# rgistration function
from Password_checker.pwd_check import is_strong_password
def register_user():

    username = input ("Please enter a Username:")
    password = input ("Please enter a Password:")

    is_valid, feedback = is_strong_password(password)
    if not is_valid:
        print("Password is not strong enough")
        print(feedback)
        return

    with open("users.txt", "a") as user_file:
        user_file.write(f"{username}:{password}\n")
    
    print("User Registration was Successful")
