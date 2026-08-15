#Find all characters that are either a, e, i, o, or u.
#text = "Beautiful Python Language"
#Don't use re.I for this one.

import re

text = "Beautiful Python Language"

result = re.findall(r"[aeiou]", text)
print(result)