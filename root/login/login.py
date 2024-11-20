import ceaser

CEASER = 6536

def get_username():
    username = input("Username: ")
    return username

def get_password():
    password = input("Password: ")
    return password

def create_user():
    username = get_username()
    password = get_password()
    password_encrypted = ceaser.encrypt(password, CEASER)

    with open("/home/john/Documents/tutoring/julien/root/login/login_credentials.csv", "a") as file:
        file.write("\n" + username + "," + password_encrypted)

def check_credentials(username, password):
    with open("/home/john/Documents/tutoring/julien/root/login/login_credentials.csv", "r") as file:
        
        lines = file.readlines()
        for line in lines:
            split_info = line.split(",")
            check_username = split_info[0]
            check_password = split_info[1].strip()

            if username == check_username:
                if password == check_password:
                    print("Welcome to Phil")
                    break
    
def log_in():
    username = get_username()
    password = get_password()
    encrypted_password = ceaser.encrypt(password, CEASER)
    check_credentials(username, password)

select = input("l to log in, c to create user: ")

if select == "l":
    log_in()

elif select == "c":
    create_user()