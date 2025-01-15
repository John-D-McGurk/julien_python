import os
import json

path = "home"

def create_folder():
    dir_name = input("Folder name: ")
    #os.mkdir(f"{path}/dir2")
    with open(f"/home/john/Documents/tutoring/julien/root/{path}.json", "r") as dir_r:
        data = json.load(dir_r)
        print(data)
        data[dir_name] = "folder"

        with open(f"/home/john/Documents/tutoring/julien/root/{path}.json", "w") as dir_w:
            dir_w.write(json.dumps(data))



create_folder()