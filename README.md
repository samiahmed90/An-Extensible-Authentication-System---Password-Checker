# An Extensible Authentication System & Password Checker

A Python-based authentication system built as a cybersecurity project. The system allows users to register and login securely, enforces strong password policies, hashes passwords before storage, and maintains a full audit log of all system events.

---

## Features

- **User Registration** — Register with a username and password. Duplicate usernames are blocked.
- **Password Strength Checker** — Passwords are validated for length, uppercase letters, numbers, and special characters before registration.
- **Password Hashing** — Passwords are hashed using SHA-256 before being stored. Plain text passwords are never saved.
- **User Login** — Authenticates users by comparing hashed passwords.
- **Audit Logging** — Every event (registration, login, failed login, logout) is recorded in `audit_log.txt` with a timestamp.
- **Post-Login Menu** — After logging in, users can view their personal logs or logout.

---

## Project Structure

```
An Extensible Authentication System & Password Checker/
│
├── main.py                  ← Entry point, run this to start the program
│
├── UI/
│   └── user_interface.py    ← Main menu and navigation
│
├── Registration/
│   └── registration.py      ← User registration logic
│
├── Login/
│   └── login.py             ← User login logic
│
├── Password_checker/
│   └── pwd_check.py         ← Password strength validation
│
├── Hashed_password/
│   └── hash.py              ← SHA-256 password hashing
│
├── Logs/
│   └── logs.py              ← View logs and post-login menu
│
├── Audit/
│   └── audit.py             ← Audit log event recorder
│
├── users.txt                ← Stores registered users (hashed passwords)
├── audit_log.txt            ← Stores all system events
└── README.md
```

---

## How to Run

Make sure you have Python 3 installed, then run:

```bash
python main.py
```

---

## How to Use

1. **Register** — Choose option 1, enter a username and a strong password
2. **Login** — Choose option 2, enter your credentials
3. **View Logs** — After login, choose option 1 to view your audit logs
4. **Logout** — After login, choose option 2 to logout
5. **Exit** — From the main menu, choose option 3 to exit

---

## Password Requirements

Passwords must meet all of the following:

- At least 8 characters long
- At least one uppercase letter
- At least one number
- At least one special character (e.g. `!@#$%^&*`)

---

## Security Features

- Passwords are never stored in plain text
- SHA-256 hashing is applied before saving to `users.txt`
- All login attempts (successful and failed) are recorded
- Duplicate usernames are not allowed

---

## Author

**samiahmed90**  
GitHub: [https://github.com/samiahmed90](https://github.com/samiahmed90)