from datetime import datetime

dt = datetime(2003, 7, 10, 8, 30, 15)
print(dt.strftime("%d-%m-%Y"))
print(dt.strftime("%Y/%m/%d %H:%M:%S"))