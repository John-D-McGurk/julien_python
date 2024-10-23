def check_credentials(username, password):
    with open("login_credentials.csv", "r" ) as file:
        lines = file.readlines()
        for line in lines:
            credentials = line.split(",")
            if username == credentials[0] and password == credentials[1].strip():
                print("Login successful!")
                return
        print("Login unsuccessful")

def create_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    password_check = input("Repeat password: ")
    
    if password != password_check:
        print("Passwords don't match!")
        return
    else:
        with open ("login_credentials.csv", "a") as file:
            file.write(username + "," + password + "\n")

def get_login_info():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password

if __name__ == "__main__":
    choose_operation = input("Type c to create user or l to login: ")
    if choose_operation == "c":
        create_user()
    elif choose_operation == "l":
        username, password = get_login_info()
        check_credentials(username, password)