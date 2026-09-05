import csv

with open('students.csv', 'r') as fobj:
    reader = csv.reader(fobj)

    for row in reader:
        print(row)