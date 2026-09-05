from pathlib import Path

processed = Path("my_projects") / "datasets" / "processed"
print(processed.is_dir())
processed.mkdir(parents = True, exist_ok = True)
print(processed.is_dir())

