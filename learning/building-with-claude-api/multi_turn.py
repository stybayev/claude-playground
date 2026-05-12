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

from dotenv import load_dotenv
from anthropic import Anthropic

sys.stdin.reconfigure(encoding="utf-8", errors="replace")

load_dotenv()

client = Anthropic()
model = "claude-sonnet-4-6"


def add_user_message(messages, text):
    messages.append({'role': 'user', 'content': text})


def add_assistant_message(messages, text):
    messages.append({'role': 'assistant', 'content': text})


def chat(messages: list, system: str | None = None):
    params = {
        'model': model,
        'max_tokens': 1000,
        'messages': messages,
    }

    if system:
        params['system'] = system

    message = client.messages.create(
        **params
    )
    return message.content[0].text


if __name__ == "__main__":
    messages = []

    add_user_message(
        messages,
        "Напиши функцию на Python, которая проверяет строку на дубликаты символов.",
    )
    answer = chat(
        messages,
        system="Ты Python-инженер, который пишет очень лаконичный код.",
    )
    print(answer)
