#text = "Python PYTHON python PyThOn"
#Find all occurrences of python, ignoring case.

import re

text = "Python PYTHON python PyThOn"

print(re.findall(r"python", text, re.IGNORECASE))