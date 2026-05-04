# trading-intelligence

Личный репо под три направления:

- **`trading/`** — доменный fintech-проект (FastAPI + MCP + Claude поверх рыночных данных).
- **`learning/`** — конспекты и упражнения по курсам Anthropic Skilljar.
- **`automation/`** — AI-наработки по автоматизации (боты, скрипты, утилиты).

## Setup

```bash
cp .env.example .env          # заполни ключи
python3.12 -m venv .venv
source .venv/bin/activate
pip install anthropic python-dotenv
```

Дальше работа идёт внутри соответствующей подпапки.

## Текущий статус

- `learning/building-with-claude-api/` — в процессе, модуль *Accessing Claude with the API*.
- `trading/` — пока пусто.
- `automation/` — пока пусто.
