#Find exactly 3-letter words.
#text = "cat dog python car bat apple sun"

import re

text = "cat dog python car bat apple sun"

result = re.findall(r"\b\w{3}\b", text)

print(result)