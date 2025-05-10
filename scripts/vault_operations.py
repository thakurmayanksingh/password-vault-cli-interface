import sqlite3 as sql
import csv

directory = "database/passDB.db"

def add_password(website_name, website_address, website_password):
    try:
        conn = sql.connect(directory)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO passwords (website_name, website_address, website_pass)
            VALUES (?, ? , ?);""", (website_name, website_address, website_password))
        conn.commit()
        conn.close()

    except Exception as e:
        print(f"Error while adding password: {e}")

def delete_password(keyword):
    pass

def search_password(keyword):
    pass

def view_all_password():
    try:
        conn = sql.connect(directory)
        cur = conn.cursor()
        cur.execute("" \
        "SELECT website_name, website_address, website_pass FROM passwords;")
        rows = cur.fetchall()
        conn.close()
        return rows
    
    except Exception as e:
        print(f"Error while viewing passwords: {e}")

def export_to_csv(filename="vault_passwords.csv"):
    pass