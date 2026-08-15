#Find numbers where the decimal part is optional.
#text = "10 10.5 25 25.75 100 3.14"

import re

text = "10 10.5 25 25.75 100 3.14"

result = re.findall(r"\b\d+\.?\d+", text)
print(result)