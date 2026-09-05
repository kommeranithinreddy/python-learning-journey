from collections import defaultdict

sales = [
    ("Alice", 100),
    ("Bob", 200),
    ("Alice", 150),
    ("Charlie", 300),
    ("Bob", 100),
    ("Alice", 50)
]

total_sales = defaultdict(int)

for name, amount in sales:
    total_sales[name] += amount

for name, amount in total_sales.items():
    print(f"{name}: {amount}")



