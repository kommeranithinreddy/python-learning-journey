import os

paths = [
    "python_practice/data/students.csv",
    "python_practice/data/marks.txt",
    "python_practice/data/notes.pdf",
    "python_practice/data/images"
]

for path in paths:
    if os.path.exists(path):
        if os.path.isfile(path):
            print(os.path.basename(path))
            print("Exists : True")
            print("Type : File")
            name, extension = os.path.splitext(path)
            print(f"Extension : {extension}")
            print()
        elif os.path.isdir(path):
            print("Exists : True")
            print("Type : Directory")
    else:
        print("Path doesn't exists")