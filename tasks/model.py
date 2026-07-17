from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
  id: int
  title: str
  done: bool = False
  created_at: str = ""
  priority: str = "medium"
  category: str = ""

  def __post_init__(self):
    if not self.created_at:
      self.created_at = datetime.now().isoformat()

  def to_dict(self) -> dict:
    return {
      "id": self.id,
      "title": self.title,
      "done": self.done,
      "created_at": self.created_at,
      "priority": self.priority,
      "category": self.category
    }

  @classmethod
  def from_dict(cls, data: dict) -> "Task":
    return cls(**data)