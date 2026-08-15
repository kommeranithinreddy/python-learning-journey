#text = "Python Java Python Python C++"
#Replace every Python with Programming.

import re

text = "Python Java Python Python C++"

print(re.sub(r"Python", 'Programming', text))