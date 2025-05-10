from scripts import initialize_db, vault_operations

def authentication():
    try:
        inp = str(input("""
LOGIN
Enter Password: """))
        if inp == 'admin':
            print("Login Successful!")
            return 'success'
        elif inp.lower() == 'quit' or inp.lower() == 'exit':
            print("Exiting on request!")
            return 'quit'
        else:
            print("Wrong Password!")
            return 'failed'
    
    except Exception as e:
        print(f"Error Authenticating...\nError: {e}")

if __name__ == '__main__':
    print("\nHello and Welcome to the Password Vault!")
    outer_loop = True
    try:
        while outer_loop:
            access = authentication()
            if access == 'success':
                outer_loop = False
                while True:
                    print("Welcome back to your Vault!")
                    print("1. Add new password\n2. View all saved password\n" \
                    "3. Search passwords by website name\n4. Delete a password entry\n" \
                    "5. Export to CSV\n6. Exit")
                    
                    inp_menu = int(input("-> "))
                    if inp_menu == 1:
                        inp_website_name = str(input("Enter website name: "))
                        inp_website_address = str(input("Enter website address: "))
                        inp_website_pass = str(input("Enter website password: "))
                        if inp_website_name and inp_website_address and inp_website_pass:
                            vault_operations.add_password(inp_website_name, inp_website_address,
                                                        inp_website_pass)
                        else:
                            print("Error! All fields are required to be filled...")
                    
                    elif inp_menu == 2:
                        passwords_list = vault_operations.view_all_password()
                        for item in passwords_list:
                            print(item)
                    
                    elif inp_menu == 6:
                        print("Thank you for using the vault.")
                        break

            elif access == 'failed':
                print("Try Again or type quit/exit for exitting.")
                
            elif access == 'quit':
                break

    except Exception as e:
        print(f"Error: {e}")