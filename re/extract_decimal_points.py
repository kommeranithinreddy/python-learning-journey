#text = "Prices: 10.50, 25.75 and 100.00"
#Extract all decimal numbers:

import re
text = "Prices: 10.50, 25.75 and 100.00"

result = re.findall(r"\d+\.\d{2}", text)
print(result)