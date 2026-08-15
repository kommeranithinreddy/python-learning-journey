#text = "My age is 25 and my friend's age is 30."
#Replace all ages with XX.

import re

text = "My age is 25 and my friend's age is 30."

print(re.sub(r"\d{2}", "XX", text))