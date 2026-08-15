#Find words that start with an uppercase letter.
#text = "Python is Easy and Powerful"

import re

text = "Python is Easy and Powerful"

result = re.findall(r"\b[A-Z][a-z]+", text)

print(result)
