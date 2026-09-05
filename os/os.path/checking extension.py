import os

paths = [
    "data/students.csv",
    "data/marks.txt",
    "data/employees.csv",
    "data/notes.pdf",
    "data/sales.xlsx"
]

for path in paths:
    _, extension = os.path.splitext(path)
    if extension == ".csv":
        print(os.path.basename(path))
