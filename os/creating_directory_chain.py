'''
project/
├── output/
├── logs/
└── data/
'''

import os

for folder in ["output", "logs", "data"]:
    os.makedirs(f"project/{folder}", exist_ok = True)

print(os.path.exists("project/output"))