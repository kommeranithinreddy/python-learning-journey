import csv

with open('students.csv', 'w', newline='') as fobj:
    writer = csv.DictWriter(fobj, fieldnames = ['roll', 'name', 'course'])
    writer.writeheader()

    writer.writerow({'roll': 1, 'name': 'Sunny', 'course': 'Data Science'})
    writer.writerow({'roll': 2, 'name': 'Rahul', 'course': 'CSE'})
    writer.writerow({'roll': 3, 'name': 'Ram', 'course': 'AI'})