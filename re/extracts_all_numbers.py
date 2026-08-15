#Extract all numbers.

import re
text = "My numbers are 123, 4567 and 89."

print(re.findall(r"\d+", text))