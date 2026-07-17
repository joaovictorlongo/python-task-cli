import argparse
from .model import Task
from .repository import load, save
from rich.console import Console
console = Console()

def run():
  parser = argparse.ArgumentParser(description="Gerenciador de Tarefas")
  sub = parser.add_subparsers(dest="command")

  p_add = sub.add_parser("add", help="Adiciona tarefa")
  p_add.add_argument("title")
  p_add.add_argument("--priority", choices=["high", "medium", "low"], default="medium")
  p_add.add_argument("--cat")

  p_list = sub.add_parser("list", help="Lista tarefas")
  p_list.add_argument("--cat")

  p_done = sub.add_parser("done", help="Conclui tarefa")
  p_done.add_argument("id", type=int)

  p_rm = sub.add_parser("rm", help="Remove tarefa")
  p_rm.add_argument("id", type=int)

  p_search = sub.add_parser("search", help="Procura tarefa")
  p_search.add_argument("term", type=str)

  args = parser.parse_args()
  tasks = load()

  if args.command == "add":
    new_id = max([t.id for t in tasks], default=0) + 1
    tasks.append(Task(id=new_id, title=args.title, priority=args.priority, category=args.cat))
    print(f"Tarefa {new_id} adicionada")

  elif args.command == "list":
    data = [t for t in tasks if args.cat.lower() in t.category.lower()] if args.cat else tasks
    for t in data:
      pending = f"[yellow][ ][/yellow] {t.id}: {t.title}"
      if t.priority == "high":
        pending = f"[red][!][/red] {t.id}: {t.title}"
      if t.priority == "low":
        pending = f"[blue][_][/blue] {t.id}: {t.title}"
      row = f"[green][x][/green] {t.id}: {t.title}" if t.done else pending
      console.print(row)

  elif args.command == "done":
    for t in tasks:
      if t.id == args.id:
        t.done = True
        print(f"Tarefa {args.id} concluída")
        break

  elif args.command == "rm":
    tasks[:] = [t for t in tasks if t.id != args.id]
    print(f"Tarefa {args.id} removida")

  elif args.command == "search":
    filtered = [t for t in tasks if args.term.lower() in t.title.lower()]
    for t in filtered:
      status = "[x]" if t.done else "[ ]"
      print(f"{status} {t.id}: {t.title}")

  save(tasks)