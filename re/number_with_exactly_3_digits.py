#text = "123 4567 89 10000"
#Find numbers containing exactly 3 digits.

import re

text = "123 4567 89 10000"

print(re.findall(r"\b\d{3}\b", text))
