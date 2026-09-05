from pathlib import Path

file = Path("my_projects/datasets/processed") / "notes.txt"

file.write_text("Python\nNumpy\nPandas\nMachine Learning")
print(file.exists())
content = file.read_text()
print(content)