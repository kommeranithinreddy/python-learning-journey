from pathlib import Path
#dataset = Path("Documents") / "sales.csv"

dataset = Path("data") / "sales.csv"

if not dataset.exists():
    print("File does not exists")
else:
    print("File exists")