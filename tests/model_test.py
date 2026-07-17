from tasks.model import Task

def test_create_task():
  t = Task(id=1, title="Estudar Python")
  assert t.id == 1
  assert t.title == "Estudar Python"
  assert t.done == False
  assert t.created_at != ""
  assert t.priority == "medium"

def test_to_dict():
  t = Task(id=1, title="Teste")
  d = t.to_dict()
  assert d["title"] == "Teste"

def test_from_dict():
  d = {"id": 2, "title": "Ler", "done": True, "created_at": "2024-01-01", "priority": "high"}
  t = Task.from_dict(d)
  assert t.id == 2
  assert t.done == True
  assert t.priority == "high"
