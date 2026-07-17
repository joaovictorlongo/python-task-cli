import json
from pathlib import Path
from tasks.model import Task

def test_save_and_load(tmp_path):
  file = tmp_path / "tasks_test.json"
  tasks = [Task(id=1, title="Teste")]
  with open(file, "w") as f:
    json.dump([t.to_dict() for t in tasks], f)
  with open(file) as f:
    data = json.load(f)
  assert len(data) == 1
  assert data[0]["title"] == "Teste"
