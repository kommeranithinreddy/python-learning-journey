from itertools import combinations


subjects = ["Python", "NumPy", "Pandas", "SQL"]

pairs = combinations(subjects, 2)

for pair in pairs:
    print(pair)
