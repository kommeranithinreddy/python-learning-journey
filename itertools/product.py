from itertools import product

models = ["Linear Regression", "Decision Tree"]
datasets = ["Training", "Testing"]


pairs = product(models, datasets)

for pair in pairs:
    print(pair)
