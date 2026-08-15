import re
text = "I am learning Python"

result = re.search(r"Python", text)

print(result.group())
print(result.start())
print(result.end())
print(result.span())