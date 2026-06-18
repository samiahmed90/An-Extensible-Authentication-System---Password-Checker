from Audit.audit import log_event

# Function to view logs
def view_logs(username):
    print(f"\nLogs for user '{username}'")
    with open ("audit_log.txt", "r") as log_file:
        logs =log_file.readlines()
    user_logs = [log.strip() for log in logs if username in log]
    if user_logs:
        for log in user_logs:
            print(log)
    else:
        print("No Logs were found in your account")

# Function to display Post Login Menu
def post_login_menu(username):
    while True:
        print("\nPost-Login Menu")
        print("1. View my Logs")
        print("2. Logout")

        choice = input("What would you like to do?")
        if choice == "1":
            view_logs(username)
        elif choice == "2":
            log_event(f"User '{username}' logged out")
            print("Logged out successfully")
            break
        else:
            print("Invalid choice. Please choose a valid option")

