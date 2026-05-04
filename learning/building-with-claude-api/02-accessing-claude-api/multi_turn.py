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

from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()
model = "claude-sonnet-4-6"


def add_user_message(messages, text):
    messages.append({'role': 'user', 'content': text})


def add_assistant_message(messages, text):
    messages.append({'role': 'assistant', 'content': text})


def chat(messages: list):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text


if __name__ == "__main__":
    messages = []

    add_user_message(messages, "что такое ислам? Ответь одним предложением.")
    answer_1 = chat(messages)
    add_assistant_message(messages, answer_1)
    print("Round 1:", answer_1)

    add_user_message(messages, "напиши ещё одно предложение")
    answer_2 = chat(messages)
    add_assistant_message(messages, answer_2)
    print("Round 2:", answer_2)
