#Find numbers with:
#exactly 3 digits before the decimal
#optional decimal part
#exactly 2 digits after the decimal if decimal exists
#text = "100 100.50 999.99 12 123.4 123.456 1000.00"

import re
text = "100 100.50 999.99 12 123.4 123.456 1000.00"

result = re.findall(r"\b\d{3}(?:\.\d{2})?\b", text)

print(result)