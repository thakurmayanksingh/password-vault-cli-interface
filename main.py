from scripts import initialize_db

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
    try:
        while True:
            access = authentication()
            if access == 'success':
                print("Welcome back to your Vault!")
            elif access == 'failed':
                print("Try Again or type quit/exit for exitting.")
            elif access == 'quit':
                break
    except Exception as e:
        print(f"Error: {e}")