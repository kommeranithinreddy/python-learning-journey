#Create InsufficientBalanceError.
#Create a simple program that can raise at least two different custom exceptions depending on the input.

class InsufficientBalanceError(Exception):
    pass

class NegativeAmountError(Exception):
    pass

balance = 5000
def withdraw(amount):
    global balance
    if amount < 0:
        raise NegativeAmountError('Amount should be positive')
    elif amount > balance:
        raise InsufficientBalanceError('Withdrawal amount exceeds the account balance')
    else:
        balance -= amount
        print('Transaction completed')

user_amt = int(input('Enter amount to withdraw: '))
withdraw(user_amt)