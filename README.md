# Python Task CLI

Gerenciador de tarefas via terminal escrito em Python.

## Funcionalidades

- **add** — Adicionar tarefa
- **list** — Listar tarefas
- **done** — Marcar como concluída
- **rm** — Remover tarefa
- **search** — Buscar por termo no título

### Prioridades

| Flag       | Visual |
|------------|--------|
| `--priority high`   | [!] |
| `--priority medium` | [ ] |
| `--priority low`    | [_] |

### Categorias

`add --cat estudos "Estudar Python"`  
`list --cat estudos`

## Uso

```bash
python main.py add "Estudar Python" --priority high --cat estudos
python main.py list
python main.py list --cat estudos
python main.py done 1
python main.py search "Python"
python main.py rm 1
```

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Testes

```bash
pytest -v
```
