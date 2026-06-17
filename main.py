def register_user():

    username = input ("Please enter a Username:")
    password = input ("Please enter a Password:")

    with open("users.txt", "a") as user_file:
        user_file.write(f"{username}: {password}\n")
    
    print("User Registration was Successful")









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
            print("Login Selected")

        elif choice == "3":
            print("Exiting the system...")
            break
        
        else:
            print("Invalid choice. Please try again.")  


main()