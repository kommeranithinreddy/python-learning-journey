#Find all words containing only letters.
#text = "Python123 Java hello DATA 456 test_1"

import re

text = "Python123 Java hello DATA 456 test_1"

res = re.findall(r"\b[a-zA-Z]+\b", text)
print(res)