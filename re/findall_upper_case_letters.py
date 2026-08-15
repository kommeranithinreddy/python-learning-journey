#Find all uppercase letters:
#text = "Python Is Very POWERFUL"

import re

text = "Python Is Very POWERFUL"

result = re.findall(r"[A-Z]", text)
print(result)