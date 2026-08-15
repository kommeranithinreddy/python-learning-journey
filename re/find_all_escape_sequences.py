#Find every whitespace character in:
#text = "Python is\tvery\npowerful"
#Then count how many whitespace characters exist.

import re

text = "Python is\tvery\npowerful"

res = re.findall(r"\s", text)
print(res)
