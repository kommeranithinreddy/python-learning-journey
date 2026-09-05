from pathlib import Path
#Creates a Path for processed.

processed = Path(r"my_projects\datasets\processed")

#Finds all .csv files using glob().

csv_files = processed.glob("*.csv")
for file in csv_files:
    print(file.name)
    print(file.suffix)
    print(file.parent)

backup = processed / "backup"
backup.mkdir(parents = True, exist_ok = True)
print(backup.exists())