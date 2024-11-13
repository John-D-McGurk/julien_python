import ceaser_cipher_solution as cs
import datetime

start = datetime.datetime.now()

USERNAME = "hacker"

def crack_ceaser(file_password, known_password):
    for current_test in range(100):
        encrypted_pass = cs.encrypt(known_password, current_test)
        if file_password == encrypted_pass:
            return current_test

def list_passwords(known_username, known_password):
    with open('login_credentials.csv', 'r')as file:
        lines = file.readlines()
        for line in lines:
            row = line.split(',')
            file_username = row[0]
            file_password = row[1].strip()
            if file_username == known_username:
                ceaser_code = crack_ceaser(file_password, known_password)
        for line in lines:
            row = line.split(',')
            file_username = row[0]
            file_password = row[1].strip()
            unencrypted_pass = cs.encrypt(file_password, -1 * ceaser_code)

            print(f"User: {file_username}, Password: {unencrypted_pass}")



list_passwords(USERNAME, "cracked")

print(datetime.datetime.now() - start)