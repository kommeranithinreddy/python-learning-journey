#Create a custom exception named InvalidAgeError.
#Raise it if the user's age is not between 18 and 60.

class InvalidAgeError(Exception):
    pass


def is_eligible(age):
    if 18 <= age < 60:
        print('Eligible')
    else:
        raise InvalidAgeError("user's age is not between 18 and 60")


input_age = int(input('Enter your age to continue: '))

is_eligible(input_age)