#Find all words containing letters, digits, or _.
#text = "hello test_123 Python data science_1 456"

import re

text = "hello test_123 Python data science_1 456"

print(re.findall(r"[\w_]+", text))