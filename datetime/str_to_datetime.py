from datetime import datetime

text = "25/12/2026 18:45:30"

dt = datetime.strptime(text, "%d/%m/%Y %H:%M:%S")
print(dt)
print(type(dt))
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)