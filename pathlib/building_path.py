from pathlib import Path

'''project/
    datasets/
        raw/
            sales.csv'''

project = Path("project")
datasets = project / "datasets"
raw = datasets / "raw"
file_path = raw / "sales.csv"

print(file_path)