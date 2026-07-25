#Create InsufficientBalanceError.
#Raise it when a withdrawal amount exceeds the account balance.

class InsufficientBalanceError(Exception):
    pass


balance = 5000
def withdraw(amount):
    if amount > balance:
        raise InsufficientBalanceError('Withdrawal amount exceeds the account balance')
    else:
        print('Transaction completed')

user_amt = int(input('Enter amount to withdraw: '))
withdraw(user_amt)