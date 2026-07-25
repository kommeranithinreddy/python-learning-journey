#Ask the user to enter their age.
#If the age is less than 18, raise a ValueError with a meaningful message.
#Otherwise, print "Eligible".

def is_eligible(age):
    if age>=18:
        print('Eligible')
    else:
        raise ValueError('Age must be equal or greater than 18')


is_eligible(int(input('Enter age to continue: ')))