
# Telegram Bot для отправки Email

Этот проект представляет собой Telegram-бота, который позволяет пользователям отправлять сообщения на указанный email с использованием SMTP-сервера.

## Требования

- Python 3.8 или выше
- Установленные зависимости (указаны в файле `requirements.txt`)

## Установка и запуск

1. **Склонируйте репозиторий или скачайте скрипт:**
   ```bash
   git clone <URL репозитория>
   cd <папка с проектом>
   ```

2. **Установите необходимые зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Запустите скрипт:**
   Перед запуском укажите параметры запуска:
   - `--token` — токен вашего Telegram-бота
   - `--email` — email-адрес, с которого будет отправлено сообщение
   - `--password` — пароль от email

   Пример запуска:
   ```bash
   python bot.py --token <TELEGRAM_TOKEN> --email <SMTP_EMAIL> --password <SMTP_PASSWORD>
   ```

## Использование

1. В Telegram начните диалог с ботом и отправьте команду `/start`.
2. Введите ваш email-адрес, на который будет отправлено сообщение.
3. Введите текст сообщения.
4. Бот отправит сообщение на указанный email.

## SMTP-сервер

По умолчанию используется сервер `smtp.yandex.ru` и порт `465`. Если вы хотите использовать другой SMTP-сервер, отредактируйте соответствующие переменные в коде.

## Зависимости

- `pyTelegramBotAPI` для работы с Telegram API
- `smtplib` для отправки писем
- `email` для формирования структуры письма
- `argparse` для обработки аргументов командной строки

## Лицензия

Этот проект предоставляется "как есть" без каких-либо гарантий.
