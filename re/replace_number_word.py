#text = "I have 2 apples, 15 oranges and 100 bananas."
#Replace every number with NUMBER.

import re

text = "I have 2 apples, 15 oranges and 100 bananas."

print(re.sub(r"\d+", "NUMBER", text))