#2026-08-16

from datetime import timedelta, date

yesterday = date(2026, 8, 16)
print(f'Yesterdays date : {yesterday}')
future = yesterday + timedelta(days=30)
print(f'30 days from yesterday : {future}')

past = yesterday - timedelta(days=10)
print(f'10 days past yesterday: {past}')

