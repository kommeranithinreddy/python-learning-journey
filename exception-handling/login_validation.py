#Ask the user for a PIN.

#Convert it to an integer.
#If conversion succeeds, print "PIN accepted" in else.
#Always print "Session closed" in finally.
#Handle invalid input using ValueError.

def check_pin(dig):
    if dig == 1834:
        return True
    return False

try:
    entered_pin = int(input('Enter pin to continue: '))
    is_valid = check_pin(entered_pin)

except ValueError:
    print('Pin must be integer')
else:
    if is_valid:
        print('PIN Accepted')
    else:
        print('Incorrect pin')
finally:
    print('Session Closed')