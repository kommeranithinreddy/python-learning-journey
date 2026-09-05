from pathlib import Path

processed = Path("my_projects") / "datasets" / "processed"

csv_files = processed.glob("*.csv")

for file in csv_files:
    print(file)
    print(file.name)