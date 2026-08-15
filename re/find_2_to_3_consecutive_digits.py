#Find strings containing exactly 2 to 3 consecutive digits.
#text = "A12 B123 C1234 D1 E99 F567"

import re

text = "A12 B123 C1234 D1 E99 F567"

result = re.findall(r"[A-Z]+\d{2,3}\b", text)
print(result)