import os

#Check whether data exists.
print(os.path.exists("python_practice/data"))
#Check whether students.csv is a file.
print(os.path.isfile("python_practice/data/student.csv"))
#Build the path to marks.txt using os.path.join().
path = os.path.join("python_practice", "data", "marks.txt")
#Get the filename from the path using basename().
print(os.path.basename(path))
#Get the extension of notes.pdf using splitext().
name, extension = os.path.splitext("python_practice/data/notes.pdf")
print(extension)