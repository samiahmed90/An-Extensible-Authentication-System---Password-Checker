def main():
    print("Welcome to the User Registration System")
    while True:

        
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Please choose an option from 1-3:")

        if choice == "1":
            print("Registration Selected")
    
        elif choice == "2":
            print("Login Selected")

        elif choice == "3":
            print("Exiting the system...")
            break
        
        else:
            print("Invalid choice. Please try again.")  


main()