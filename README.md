
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
│   └── passDB.db         # SQLite3 database file
├── scripts/
│   └── initialize_db.py
│   └── vault_operations.py  # Core database operations
│
├── main.py              # Main CLI interface
└── README.md            # Project documentation
```

## Requirements

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

Note: The `id` values are auto-incremented and are not reset after deletion.

## Known Limitations

- Passwords are stored in plain text (consider encrypting them for production use).
- Deletion and indexing do not reset the primary key ID values.
- Authentication is basic (`admin` as password). Improve this for production use.
