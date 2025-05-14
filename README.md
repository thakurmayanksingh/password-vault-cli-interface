
# Password Vault CLI

A simple and secure command-line password vault built with Python and SQLite3. This tool allows users to store, search, delete, and export website credentials locally via an interactive interface.

## Features

- Add and store passwords for websites securely in a local database.
- View all stored passwords.
- Search for saved credentials using a keyword (name or address).
- Delete password entries using a keyword.
- Export saved passwords to a CSV file.

## Directory Structure

```
project/
│
├── database/
│   └── passDB.db
├── scripts/
│   └── initialize_db.py
│   └── vault_operations.py
│
├── main.py      
└── README.md       
```

## Tech Stack

- Python 3.7+
- `sqlite3` (built-in with Python)
- `csv` (built-in)

## How to Use

### 1. Clone the repository

```bash
git clone https://github.com/your-username/password-vault-cli.git
cd password-vault-cli
```

### 2. Run the main program

```bash
python main.py
```

### 3. Login

When prompted:
- Use the password to log in.
- You can type `quit` or `exit` to close the program.

## Available Options in CLI

```
1. Add new password
2. View all saved passwords
3. Search passwords by website name or address
4. Delete a password entry
5. Export to CSV
6. Exit
```

## Export Format

When exporting to CSV, you will be prompted for a file name (e.g., `vault_passwords.csv`). The exported file will contain:

```
id, website_name, website_address, website_pass
```

## Authors

- **Mayank Singh** — [LinkedIn](https://www.linkedin.com/in/mayank-singh-367572246/) • [GitHub](https://github.com/thakurmayanksingh)
- **Ishita Modi** — [LinkedIn](https://www.linkedin.com/in/ishita-modi-155676341/) • [GitHub](https://github.com/ishita230105)

```

*Thanks for checking it out! Contributions and suggestions are always welcome.*

