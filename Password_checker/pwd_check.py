import re #import for regular expressions

# Password checker function

def is_strong_password(password):
    if len(password)<8:
        return False, "Password must be at least 8 characters long."
    
    if not re.search(r'[A-Z]', password):
        return False, "Password must include atleast one uppercase letter."
    
    if not re.search(r'[0-9]', password):
        return False, "Password must include atleast one number"
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must include atleast one special symbol."

    return True, "Password is strong"
    