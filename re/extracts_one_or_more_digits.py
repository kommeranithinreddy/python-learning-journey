#Extract numbers containing one or more digits.
#text = "A 1 B 22 C 333 D"

import re

text = "A 1 B 22 C 333 D"

result = re.findall(r"\d+", text)
print(result)