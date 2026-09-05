from collections import Counter

transactions = [
    "food",
    "travel",
    "food",
    "shopping",
    "food",
    "travel",
    "bills",
    "shopping",
    "food",
    "bills",
    "travel",
    "food"
]

trans_count = Counter(transactions)
print(trans_count)
print(f'food count = {trans_count["food"]}')
print(trans_count.most_common(2))
for category, count in trans_count.most_common():
    print(category, ':', count)
