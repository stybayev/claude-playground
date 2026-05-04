# Multi-Turn conversations

## Главное

Anthropic API — **stateless**. Сервер не помнит ничего между запросами. Каждый запрос — независимый. Если хочешь чтобы Claude помнил предыдущие сообщения, ты сам поддерживаешь историю на своей стороне и шлёшь её целиком при каждом вызове.

## Почему stateless важно понимать

Если просто отправить:

1. "What is quantum computing?" → получаешь ответ
2. "Write another sentence" → Claude не знает к чему это относится, напишет про что попало

Чтобы это работало, нужно во втором запросе послать **всю историю**: вопрос 1, ответ 1, вопрос 2.

## Поток

1. Шлёшь user-сообщение.
2. Получаешь assistant-ответ.
3. Добавляешь оба в свой список `messages`.
4. Добавляешь следующий user-вопрос в список.
5. Шлёшь весь `messages` обратно — Claude видит полный контекст.

Список — это просто `list[dict]`, где каждый dict вида `{"role": "user" | "assistant", "content": str}`.

## Helper-функции из урока

```python
def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text
```

## Использование

```python
messages = []
add_user_message(messages, "Define quantum computing in one sentence")
answer = chat(messages)
add_assistant_message(messages, answer)

add_user_message(messages, "Write another sentence")
final_answer = chat(messages)   # видит всю историю → понимает контекст
```

## Что я для себя отметил

- История растёт линейно — каждый запрос отправляет все предыдущие токены. На длинных диалогах это бьёт по биллингу и по лимиту context window.
- Решения: усечение старых сообщений, суммаризация, prompt caching (будет дальше в курсе).
- `message.content[0].text` — берём первый блок. Когда появятся tool_use или другие блоки, такой код сломается.
- В FastAPI-приложении `messages` обычно живёт в БД (per conversation_id), а не в памяти процесса.
