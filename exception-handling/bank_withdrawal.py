#Create a variable balance = 5000.
#Ask the user for a withdrawal amount.
#If the amount is greater than the balance, raise an exception with an appropriate message.
#Otherwise, deduct the amount and display the remaining balance.
balance = 5000
def withdrawal(amount):
    if amount > balance:
        raise ValueError(f'Withdrawal amount : {amount} is greater than current balance')
    else:
        print(f'Transaction completed. Current balance : {balance-amount}')

input_amount = int(input('Enter amount to withdraw: '))

withdrawal(input_amount)