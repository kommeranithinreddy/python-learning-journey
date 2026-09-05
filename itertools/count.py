from itertools import count

number_generator = count(50, 10)

print(next(number_generator))
print(next(number_generator))
print(next(number_generator))
print(next(number_generator))
print(next(number_generator))


for num in number_generator:
    print(num)
    if num >= 150:
        break
