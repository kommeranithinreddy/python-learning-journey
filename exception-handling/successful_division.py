#Accepts two numbers.
#Performs division inside try.
#Prints the result in else.
#Prints "Program finished" in finally.

try:
    n1 = int(input('Enter first number: '))
    n2 = int(input('Enter second number: '))

    result = n1/n2
except (ValueError, ZeroDivisionError) as t:
    print(t)
    print(type(t).__name__)
else:
    print(f'{n1}/{n2}={result}')
finally:
    print('Program finished')
