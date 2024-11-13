import getpass
import ceaser_cipher_solution as cs

CEASER_CODE = 25

def check_credentials(username, password):
    with open("login_credentials.csv", "r" ) as file:
        lines = file.readlines()
        for line in lines:
            credentials = line.split(",")
            password_encrypted = cs.encrypt(password, CEASER_CODE)
            if username == credentials[0] and password_encrypted == credentials[1].strip():
                print("Login successful!")
                return True
        print("Login unsuccessful")
        return False

def create_user(username, password):
    password_check = input("Repeat password: ")
    
    if password != password_check:
        print("Passwords don't match!")
        return
    else:
        password_encrypted = cs.encrypt(password, CEASER_CODE)
        with open ("login_credentials.csv", "a") as file:
            file.write(username + "," + password_encrypted + "\n")

def get_login_info():
    username = input("Enter username: ")
    password = getpass.getpass()
    return username, password

if __name__ == "__main__":
    choose_operation = input("Type c to create user or l to login: ")
    if choose_operation == "c":
        username, password = get_login_info()
        create_user(username, password)
    elif choose_operation == "l":
        username, password = get_login_info()
        check_credentials(username, password)