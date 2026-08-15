#Find strings that start with Python.

sample = [
    "Python is easy",
    "I love Python",
    "Python programming",
    "Java is different"
]

import re

texts = [
    "Python is easy",
    "I love Python",
    "Python programming",
    "Java is different"
]

results = []
for i in texts:
    result = re.match(r"Python.+", i)
    if result is not None:
        results.append(result.group())

print(results)