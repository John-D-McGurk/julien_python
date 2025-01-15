import datetime

def read_entries():
    with open("/home/john/Documents/tutoring/julien/root/journal/journal.txt", "r") as file_read:
        content = file_read.read()
        content = content.split("\n\n")   
        number_entries = len(content)     
        print("You have " + str(number_entries) + "entries.")
        entry_picker = input("Choose which entry or type a to print all: ")
        if entry_picker == "a":
            for entry in content:
                print(entry)
        if entry_picker.isnumeric():
            print(content[int(entry_picker) - 1])

def write_entries():
    with open("/home/john/Documents/tutoring/julien/root/journal/journal.txt", "a") as file_append: 
        time = datetime.datetime.now().strftime("%d/%m/%Y")
        new_entry = "### "  + input("Enter a heading: ") + " ###\n"
        new_entry += time
        new_entry += "\n" + input("Write a new entry: ")
        file_append.write("\n\n" + new_entry)

def start():
    read_or_write = input("Type r to read or w to write: ")
    if read_or_write == "r":
        read_entries()
    elif read_or_write == "w":
        write_entries()


if __name__ == "__main__":
    start()