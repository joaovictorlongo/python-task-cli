import json
from pathlib import Path
from .model import Task

FILE = Path("tasks.json")

def load() -> list[Task]:
  if not FILE.exists():
    return []
  with open(FILE) as f:
    data = json.load(f)
  return [Task.from_dict(item) for item in data]

def save(tasks: list[Task]):
  with open (FILE, "w") as f:
    json.dump([t.to_dict() for t in tasks], f, indent=2)
