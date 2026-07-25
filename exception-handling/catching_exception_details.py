#Catch any unexpected exception using:
#except Exception as e:
#The exception message
#The exception type


try:
    num = int(input('Enter any number: '))
    print(num)
except Exception as e:
    print("Exception message:", e)
    print("Exception type:", type(e).__name__)