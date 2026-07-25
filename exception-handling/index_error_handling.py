#Create a list of five elements.
#Ask the user for an index and safely print the value.
#Handle IndexError.

items = ['Laptop', 'mouse', 'printer', 'keyboard', 'headset']

def item_finder(index):
    return items[index]

try:
    num = int(input('Enter index number to find the element: '))

    item = item_finder(num)
    print(item)
except IndexError:
    print('Please enter in range of 0 to 4')