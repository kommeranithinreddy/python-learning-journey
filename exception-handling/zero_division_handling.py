#Write a program that asks for two numbers and performs division.
#Handle ZeroDivisionError.

def divide(num1, num2):
    return num1/num2

try:
    num1 = int(input('Enter your first number: '))
    num2 = int(input('Enter your second number: '))

    result = divide(num1, num2)
    print(result)
except ZeroDivisionError:
    print('Number cannot divide by Zero')