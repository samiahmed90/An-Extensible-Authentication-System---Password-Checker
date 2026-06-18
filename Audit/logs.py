from datetime import datetime #import for date and time

# Function to log user activities

def log_event(event):
    timestamp = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
    with open ("audit_log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {event}\n")