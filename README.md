# trading-intelligence

Личный репо для работы с Claude API и экосистемой Anthropic.

- **`learning/`** — конспекты и упражнения по курсам Anthropic Skilljar. Каждая концепция сначала проживается в виде минимального скрипта.
- **`playground/`** — FastAPI-приложение, в которое портируются концепты из учебных скриптов после того, как они поняты. Тут swagger, multi-turn `/chat`, RAG, агенты, и прочее в виде живых эндпоинтов.

Зачем разделение: учебный скрипт изолирует **одну** концепцию (multi-turn, tool-use, streaming) — без HTTP-плумбинга, схем и сессий. Когда концепция понята — портирую в `playground/` уже как роут, и решаю отдельную задачу "как это ляжет в HTTP". Не размазываю внимание между Claude API и FastAPI одновременно.

## Setup

```bash
cp .env.example .env          # вставь ANTHROPIC_API_KEY
python3.12 -m venv .venv
source .venv/bin/activate
pip install anthropic python-dotenv
```

Зависимости пока минимальные. FastAPI/uvicorn добавятся когда `playground/` начнёт наполняться.

## Текущий статус

- `learning/building-with-claude-api/` — в процессе, модуль *Accessing Claude with the API*, урок *Multi-Turn conversations*.
- `playground/` — пусто. Заведу первый эндпоинт после модуля 5 (Tool use), когда наберётся достаточно концептов для осмысленных роутов.
