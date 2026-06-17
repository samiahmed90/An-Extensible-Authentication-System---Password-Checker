from Registration.registration import register_user
from Login.login import login_user


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