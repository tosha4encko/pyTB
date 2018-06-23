import telebot

bot = telebot.TeleBot('576157976:AAEU2KatpbAISu1BV34qUQCPKP0pwN0pteg')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)