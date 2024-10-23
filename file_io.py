with open("text.txt", "r") as file_read:
    print(file_read)

    lines = file_read.readlines()
    for line in lines:
        print(line)

with open("text.txt", "a") as file_write: 
    user_input = input("add to file: ")
    file_write.write(user_input + "\n")

