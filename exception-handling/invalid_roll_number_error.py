class InvalidRollNumberError(Exception):
    pass

students = dict()
class Student:
    def __init__(self, name, rollno, age):
        self.name = name
        self.setrollno(rollno)
        self.setage(age)
        students[self.rollnumber] = (self.name, self.age)

    def setrollno(self, rollno):
        if not(1000 <= rollno <= 9999):
            raise InvalidRollNumberError('Rollnumber must be in between 1000 and 9999')
        elif rollno in students:
            raise InvalidRollNumberError('Rollnumber already in use')
        else:
            self.rollnumber = rollno
    def setage(self, age):
        if 5 <= age < 60:
            self.age = age
        else:
            raise ValueError('Age must be in between 5 and 60')

print('Creating student. Please enter the below details.....')
while True:
    try:
        name = input('Enter student name: ')
        rollno = int(input('Enter student roll number: '))
        age = int(input('Enter student age: '))

        std1 = Student(name, rollno, age)
        print('Student Created')
        break
    except ValueError as v:
        print(v)
    except InvalidRollNumberError as e:
        print(e)