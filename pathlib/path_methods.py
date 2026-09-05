from pathlib import Path
#("project") / "datasets" / "raw" / "sales.csv"
file_path = Path("project") / "datasets" / "raw" / "sales.csv"

print(file_path.name)
print(file_path.suffix)
print(file_path.stem)
print(file_path.parent)
print(file_path.exists())