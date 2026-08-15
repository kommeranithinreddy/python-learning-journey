#Extract sequences containing 2 to 4 digits.
#text = "1 12 123 1234 12345 123456"

import re

text = "1 12 123 1234 12345 123456"

result = re.findall(r"\b\d{2,4}\b", text)
print(result)

#Extract numbers containing at least 3 digits.
#text = "12 123 4567 89 12345"

text1 = "12 123 4567 89 12345"
result1 = re.findall(r"\b\d{3,}", text1)
print(result1)