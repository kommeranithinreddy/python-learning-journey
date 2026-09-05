from datetime import date

today = date.today()
deadline = date(2026, 12, 31)

remaining = deadline - today

print(f'Remaining days to deadline: {remaining}')