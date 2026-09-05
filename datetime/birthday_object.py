from datetime import date

birthday = date(2003, 7, 10)
print(birthday)
print(birthday.year)
print(birthday.month)
print(birthday.day)

future_date = date(2030, 1, 1)
print(birthday < future_date)