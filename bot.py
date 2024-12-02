import telebot
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import argparse

# Настройка парсера аргументов
parser = argparse.ArgumentParser(description='Запуск Telegram-бота для отправки сообщений через SMTP.')
parser.add_argument('--token', type=str, required=True, help='Токен Telegram-бота')
parser.add_argument('--email', type=str, required=True, help='Email для SMTP')
parser.add_argument('--password', type=str, required=True, help='Пароль для SMTP')

args = parser.parse_args()

# Конфигурация
API_TOKEN = args.token
SMTP_SERVER = 'smtp.yandex.ru'
SMTP_PORT = 465
SMTP_EMAIL = args.email
SMTP_PASSWORD = args.password

bot = telebot.TeleBot(API_TOKEN)

# Хранение состояний пользователей
user_data = {}

# Регулярное выражение для проверки email
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет! Пожалуйста, введите ваш email:")
    user_data[message.chat.id] = {'state': 'awaiting_email'}


# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def text_handler(message):
    user_state = user_data.get(message.chat.id, {})

    if user_state.get('state') == 'awaiting_email':
        email = message.text
        if re.match(EMAIL_REGEX, email):
            user_data[message.chat.id]['email'] = email
            user_data[message.chat.id]['state'] = 'awaiting_message'
            bot.send_message(message.chat.id, "Email принят! Теперь введите текст сообщения:")
        else:
            bot.send_message(message.chat.id, "Некорректный email. Попробуйте снова.")

    elif user_state.get('state') == 'awaiting_message':
        email = user_data[message.chat.id]['email']
        text_message = message.text

        try:
            send_email(email, text_message)
            bot.send_message(message.chat.id, "Сообщение отправлено на ваш email!")
        except Exception as e:
            bot.send_message(message.chat.id, f"Ошибка отправки сообщения: {e}")

        # Сброс состояния
        user_data.pop(message.chat.id, None)
    else:
        bot.send_message(message.chat.id, "Я не понимаю. Используйте команду /start для начала.")


# Функция отправки email
def send_email(to_email, message_text):
    msg = MIMEMultipart()
    msg['From'] = SMTP_EMAIL
    msg['To'] = to_email
    msg['Subject'] = "Сообщение из Telegram-бота"
    msg.attach(MIMEText(message_text, 'plain'))

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.send_message(msg)


# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)
