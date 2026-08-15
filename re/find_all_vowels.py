#Find all vowels:
#text = "Python programming is interesting"

import re

text = "Python programming is interesting"

res = re.findall(r"[AEIOU]", text, re.I)

print(res)