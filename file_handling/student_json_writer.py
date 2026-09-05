import json

with open('student.json', 'r') as fobj:
    student = json.load(fobj)
    print(student)