# initializing the db
import sqlite3 as sql

directory = "database/passDB.db"

def main():
    try:
        conn = sql.connect(directory)
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    website_name VARCHAR(100) NOT NULL,
                    website_address VARCHAR(200) NOT NULL,
                    website_pass VARCHAR(50) NOT NULL
                    );
        ''')
        print("Successfully Created!")
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error creating and setting up database!.\nError: {e}")