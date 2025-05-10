import sqlite3 as sql
import csv

directory = "database/passDB.db"

def add_password(website_name, website_address, website_password):
    try:
        conn = sql.connect(directory)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO passwords (website_name, website_address, website_pass)
            VALUES (?, ?, ?);""", (website_name, website_address, website_password))
        conn.commit()
        conn.close()
        print("Password added successfully.")
    except Exception as e:
        print(f"Error while adding password: {e}")

def delete_password(keyword):
    try:
        conn = sql.connect(directory)
        cur = conn.cursor()
        print(f"Attempting to delete records with keyword: {keyword}")
        
        cur.execute('''
            DELETE FROM passwords 
            WHERE website_name LIKE ? OR website_address LIKE ?;
        ''', (f"%{keyword}%", f"%{keyword}%"))
        
        conn.commit()
        
        rows_deleted = cur.rowcount
        if rows_deleted > 0:
            print(f"{rows_deleted} password entry(ies) deleted successfully.")
        else:
            print("No entries found matching the keyword.")
    
    except sql.Error as e:
        print(f"An error occurred while deleting the password: {e}")
    
    finally:
        if conn:
            conn.close()

def search_password(keyword):
    try:
        conn = sql.connect(directory)
        cur = conn.cursor()
        cur.execute('''
    SELECT * FROM passwords 
    WHERE website_name LIKE ? OR website_address LIKE ?
    ORDER BY id ASC;
''', (f"%{keyword}%", f"%{keyword}%"))

        rows = cur.fetchall()
        conn.close()
        if rows:
            return rows
        else:
            return 'na'
    
    except Exception as e:
        print(f"Error while searching password!\nError: {e}")

def view_all_password():
    try:
        conn = sql.connect(directory)
        cur = conn.cursor()
        cur.execute("SELECT website_name, website_address, website_pass FROM passwords ORDER BY id ASC;")

        rows = cur.fetchall()
        conn.close()
        return rows
    
    except Exception as e:
        print(f"Error while viewing passwords: {e}")

def export_to_csv(filename="vault_passwords.csv"):
    try:
        connection = sql.connect(directory)
        cursor = connection.cursor()
        cursor.execute("SELECT website_name, website_address, website_pass FROM passwords ORDER BY id ASC")
        data = cursor.fetchall()

        if not data:
            print("No passwords to export. Your vault is empty.")
            return

        # Add custom index starting from 1
        with open(filename, "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["id", "website_name", "website_address", "website_pass"])
            for i, row in enumerate(data, start=1):
                writer.writerow([i] + list(row))

        print(f"Passwords exported successfully to '{filename}'.")

    except sql.Error as error:
        print("Database error occurred while exporting.")
        print(f"Error: {error}")

    except Exception as error:
        print("An unexpected error occurred during export.")
        print(f"Error: {error}")

    finally:
        if connection:
            connection.close()
