import os
import json

path = "/home/john/Documents/tutoring/julien/root/home"
pwd = "/home"

def create_folder():
    """
    Creates a new folder on a given path
    """
    dir_name = input("Folder name: ")
    os.mkdir(f"{path}/{dir_name}")
    with open(f"{path}{pwd}.json", "r") as dir_r:
        data = json.load(dir_r)
        data[dir_name] = "folder"

        with open(f"{path}{pwd}.json", "w") as dir_w:
            dir_w.write(json.dumps(data))

        with open(f"{path}/{dir_name}/{dir_name}.json", "w") as new_dir:
            new_dir.write(json.dumps(dict()))

def list_files():
    with open(f"{path}{pwd}.json", "r") as dir_r:
        contents = json.load(dir_r)
        keys = list(contents.keys())
        for file in keys:
            print(f"{file}: {contents[file]}")    

create_folder()
list_files()