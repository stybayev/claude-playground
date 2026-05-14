"""
Упражнение: Multi-turn conversations.

Задачи:
1. Загрузить ANTHROPIC_API_KEY из .env.
2. Написать helper-функции add_user_message, add_assistant_message, chat.
3. Сделать диалог из двух раундов: спросить про что-то, потом задать
   follow-up который требует контекста ("write another sentence").
4. Распечатать обе реплики и проверить что Claude помнит контекст.

Запуск: python -m learning.building-with-claude-api.02-accessing-claude-api.multi_turn
       (или просто из IDE)
"""

import sys
import json

from dotenv import load_dotenv
from anthropic import Anthropic

sys.stdin.reconfigure(encoding="utf-8", errors="replace")

load_dotenv()

client = Anthropic()
model = "claude-haiku-4-5-20251001"


def add_user_message(messages, text):
    messages.append({'role': 'user', 'content': text})


def add_assistant_message(messages, text):
    messages.append({'role': 'assistant', 'content': text})


def chat(
    messages: list,
    system: str | None = None,
    stop_sequences: list[str] | None = None,
):
    params = {
        'model': model,
        'max_tokens': 1000,
        'messages': messages,
    }

    if system:
        params['system'] = system

    if stop_sequences:
        params['stop_sequences'] = stop_sequences

    message = client.messages.create(
        **params
    )
    return message.content[0].text


if __name__ == "__main__":
    messages = []

    add_user_message(messages, "Generate a very short event bridge rule as json")
    add_assistant_message(messages, "```json")

    text = chat(messages, stop_sequences=["```"])
    print(text.strip())
    clean_json = json.loads(text.strip())

    print(json.dumps(clean_json, indent=2, ensure_ascii=False))
