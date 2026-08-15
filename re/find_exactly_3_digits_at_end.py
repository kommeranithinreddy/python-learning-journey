#text = "ABC123 XYZ456 HELLO"
#Find strings containing exactly 3 digits at the end.

import re
text = "ABC123 XYZ456 HELLO"
print(re.findall(r"\b\w+\d{3}\b", text))
#\b at starting means the word is starting there and \b at ending is the words ends.