# rgistration function
def register_user():

    username = input ("Please enter a Username:")
    password = input ("Please enter a Password:")

    with open("users.txt", "a") as user_file:
        user_file.write(f"{username}:{password}\n")
    
    print("User Registration was Successful")


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
    




def main():
    print("Welcome to the User Registration System")
    while True:

        
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Please choose an option from 1-3:")

        if choice == "1":
            register_user()
    
        elif choice == "2":
            login_user()

        elif choice == "3":
            print("Exiting the system...")
            break
        
        else:
            print("Invalid choice. Please try again.")  


main()