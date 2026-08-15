#Find numbers that occur at the end of each string.

sample = [
    "Age 25",
    "Python123",
    "123 Python",
    "Data 2026"
]
import re

texts = [
    "Age 25",
    "Python123",
    "123 Python",
    "Data 2026"
]

results = []
for text in texts:
    result = re.search(r"[0-9]+$", text)
    if result is not None:
        results.append(result.group())

print(results)
