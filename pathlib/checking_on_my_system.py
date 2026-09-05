from pathlib import Path

dataset = Path(r"C:\Users\NITHIN\OneDrive\Documents") / "Python_Practice" / "pathlib" / "building_path.py"

print(dataset.exists())
print(dataset.is_file())
print(dataset.parent)