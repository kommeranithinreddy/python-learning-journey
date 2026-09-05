from itertools import count, islice

numbers = count(10, 5)
selected = islice(numbers, 4, 9)
for number in selected:
    print(number)
