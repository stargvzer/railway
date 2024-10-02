import telebot
import kol

bot = telebot.TeleBot(kol.token)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, kol.startAnswer)

# Обработчик сообщений, содержащих команду /request или ключевое слово
@bot.message_handler(func=lambda message: message.text and ('/request' in message.text or 'шерсть' in message.text.lower()))
def handle_request(message):
    bot.send_message(message.chat.id, kol.random_message())

if __name__ == '__main__':
    bot.polling(none_stop=True)
