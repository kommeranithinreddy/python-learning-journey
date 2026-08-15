#text = "cat bat rat car"
#Find all three-letter words that end with at.

import re
text = "cat bat rat car waat"

print(re.findall(r"\b\wat\b", text))