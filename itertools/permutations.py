from itertools import permutations

languages = ["Python", "SQL", "R"]

pairs = permutations(languages, 2)

for pair in pairs:
    print(pair)
