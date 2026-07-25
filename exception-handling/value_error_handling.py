#Ask the user to enter an integer.
#Handle ValueError if they enter text.

def read_int(value):
    result = int(value)
    return f'{result} is an integer'


try:
    value = input('Enter any number: ')
    output = read_int(value)
    print(output)
except ValueError:
    print('Only integer values are allowed')
