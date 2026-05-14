"""
Упражнение: Structured data.

Задачи:
1. Попросить Claude сгенерировать три коротких примера AWS CLI команд.
2. Сначала вызвать без prefill — увидеть, что ответ обёрнут в текст
   и markdown-блоки. С такой строкой неудобно работать в программе.
3. Применить prefill ("```bash") + stop_sequences (["```"]),
   чтобы получить чистый блок команд без пояснений.
4. Подсказка из курса: prefill — это не только тройные кавычки.
   Можно "толкать" Claude любой фразой, например
   "Here are all three commands in a single block without any commentary:"

Важно: модели с extended thinking (claude-sonnet-4-6) не поддерживают
assistant-prefill — последнее сообщение обязано быть от user. Поэтому
здесь используем claude-haiku-4-5, которая prefill поддерживает.

Запуск: python learning/building-with-claude-api/structured_data_exercise.py
"""

import sys

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


def chat(messages: list,
         system: str | None = None,
         stop_sequences: list[str] | None = None, ):
    params = {
        'model': model,
        'max_tokens': 1000,
        'messages': messages,
    }

    if system:
        params['system'] = system

    if stop_sequences:
        params['stop_sequences'] = stop_sequences

    message = client.messages.create(**params)
    return message.content[0].text


PROMPT = """
Generate three different sample AWS CLI commands. Each should be very short.
"""


def run_without_prefill() -> str:
    """Базовый вариант: без prefill. Claude добавит пояснения и markdown."""
    messages = []
    add_user_message(messages, PROMPT)

    text = chat(messages)
    return text.strip()


def run_with_code_block_prefill() -> str:
    """Prefill через ```bash + stop на ```. Получаем чистые команды."""
    messages = []
    add_user_message(messages, PROMPT)
    add_assistant_message(messages, "```bash")

    text = chat(messages, stop_sequences=["```"])
    return text.strip()


def run_with_sentence_prefill() -> str:
    """Prefill через обычную фразу — это не только про тройные кавычки."""
    messages = []
    add_user_message(messages, PROMPT)
    add_assistant_message(
        messages,
        "Here are all three commands in a single block without any commentary:",
    )

    text = chat(messages, stop_sequences=["```"])
    return text.strip()


if __name__ == "__main__":
    print("=" * 60)
    print("1) БЕЗ prefill — Claude обернёт в текст и markdown")
    print("=" * 60)
    print(run_without_prefill())

    print("\n" + "=" * 60)
    print("2) PREFILL ```bash — получаем чистые команды")
    print("=" * 60)
    print(run_with_code_block_prefill())

    print("\n" + "=" * 60)
    print("3) PREFILL обычной фразой — тоже работает")
    print("=" * 60)
    print(run_with_sentence_prefill())
