#find all occurrences of python
from re import findall
text = "Python Java Python C++ Java Python"


res = findall(r"Python", text)
print(res)