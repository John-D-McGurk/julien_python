import datetime

def read_entries():
    with open("journal/journal.txt", "r") as file_read:
        content = file_read.read()
        content = content.split("\n\n")   
        number_entries = len(content)     
        print("You have " + str(number_entries) + "entries.")
        entry_picker = int(input("Choose which entry or type a to print all: "))
        print(content[entry_picker - 1])

def write_entries():
    with open("journal/journal.txt", "a") as file_append: 
        time = datetime.datetime.now().strftime("%d/%m/%Y")
        new_entry = "### "  + input("Enter a heading: ") + " ###\n"
        new_entry += time
        new_entry += "\n" + input("Write a new entry: ")
        file_append.write("\n\n" + new_entry)

read_or_write = input("Type r to read or w to write: ")

if read_or_write == "r":
    read_entries()
elif read_or_write == "w":
    write_entries()