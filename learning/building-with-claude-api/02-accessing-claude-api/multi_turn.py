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


# TODO: реализовать helper-функции
# def add_user_message(messages, text): ...
# def add_assistant_message(messages, text): ...
# def chat(messages) -> str: ...


if __name__ == "__main__":
    # TODO: построить диалог из двух раундов
    pass
