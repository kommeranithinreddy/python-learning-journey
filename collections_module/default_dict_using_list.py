from collections import defaultdict

employees = [
    ("Engineering", "Alice"),
    ("Sales", "Bob"),
    ("Engineering", "Charlie"),
    ("HR", "David"),
    ("Sales", "Emma"),
    ("Engineering", "Frank"),
    ("HR", "Grace")
]


grp_by_role = defaultdict(list)

for role, name in employees:
    grp_by_role[role].append(name)


for role, names in grp_by_role.items():
    print(f"{role} : {','.join(names)}")
