#Write a program using multiple except blocks for:
#ValueError
#IndexError
#ZeroDivisionError
num_dict = {0:0, 1:1, 2:2, 3:3, 4:4}
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def divide(num1, num2):
    return num1/num2

try:
    print('There are a list of number. please enter index values to divide')
    n1 = int(input('Enter first index number: '))
    n2 = int(input('Enter second index number: '))

    value = divide(num_dict[numbers[n1]], num_dict[numbers[n2]])
    print(value)
except ValueError:
    print('Only integers are accepted')
except IndexError:
    print('Index must be between 0 and 9')
except KeyError:
    print('Key must be between 0 and 4')
except ZeroDivisionError:
    print('Cannot divide by Zero')