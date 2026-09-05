file_obj = open('profile.txt', 'w')

name = input('Enter Your name: ')
age = int(input('Enter your age: '))
city = input('Enter your City name: ')
print(f'Name : {name}\nAge: {age}\nCity :{city}', file = file_obj)
file_obj.close()
