import datetime

def read_entries():


def write_entries():
    time = datetime.datetime.now().strftime("%d/%m/%Y")
    with open("journal.txt", "a") as file_append: 
        new_entry = "### " + input("Enter a heading for your entry: ") + " ###\n"        
        new_entry += str(time) + "\n"
        new_entry += input("Write a your entry: ")

        file_append.write("\n\n" + new_entry)

if __name__ == "__main__":
    read_or_write = input("Type r to read or w to write: ")

    if read_or_write == "r":
        with open("journal.txt", "r") as file_read:
            content = file_read.read().split("\n\n")
            entry_to_open = input("You have " + str(len(content)) + " entries. Enter an index to open one entry, or type a to open all: ")
            if entry_to_open == "a":
                for entry in content:
                    print("\n" + entry, end="\n\n")
            elif int(entry_to_open) <= len(content):
                print(content[int(entry_to_open) - 1])
            else:
                print("Invalid index!")    elif read_or_write == "w":
            write_entries()