#Replace sequences of one or more spaces with a single space.
#text = "Python    is   very     useful"

import re

text = "Python    is   very     useful"

result = re.sub(r"\s+", ' ', text)

print(result)