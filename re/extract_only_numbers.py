#text = "Python123 Java456 C789"
#Extract only numbers

import re
text = "Python123 Java456 C789"

print(re.findall(r"\d+", text))