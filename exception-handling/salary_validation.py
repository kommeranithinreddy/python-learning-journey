class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.set_age(age)
        self.set_salary(salary)
    def set_age(self, age):
        if 18 <= age < 60:
            self.age = age
        else:
            raise ValueError('Age must be between 18 and 60')
    def set_salary(self, salary):
        if salary > 0:
            self.salary = salary
        else:
            raise ValueError('Salary must be positive')

e_name = input('Enter employee name: ')
e_age = int(input('Enter age: '))
e_salary = int(input('Enter employee salary: '))

emp1 = Employee(e_name, e_age, e_salary)
print(f'Employee : {emp1.name} created successfully')