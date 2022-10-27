import telebot
from config import keys, TOKEN
from extensions import ConversionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message):
    text = 'Чтобы начать работать введите команду боту в следующем формате (через пробел):\n <имя валюты, цену которой вы хотите узнать> \
<имя валюты, в которой надо узнать цену первой валюты> \
<количество первой валюты>\nУвидеть список всех доступных валют: /values'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text',])
def convert(message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConversionException('Слишком много/мало параметров.')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except ConversionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Стоимость {amount} {quote} в {base} равна {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)



