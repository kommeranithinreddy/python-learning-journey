#Find words beginning with Py and followed by one or more word characters.
#text = "Python PyTorch Py123 Java P"

import re

text = "Python PyTorch Py123 Java P"

result = re.findall(r"\bPy\w+", text)
print(result)