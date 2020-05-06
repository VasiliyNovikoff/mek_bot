import telebot
from mek_dict import mek_dict
from random import randint
from mek_photo_dict import m_f_d

bot = telebot.TeleBot('1088368052:AAErWQO3QqQrzFzoJbVpyVlZ9Urye250VA8')


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()
    rnd = randint(0, 10)
    m1 = 'mek'
    m2 = 'мек'
    print(rnd)
    if (m1 in get_message_bot) or (m2 in get_message_bot):
        if rnd > 3:
            final_message = f'{mek_dict[randint(1, len(mek_dict))]}'
            bot.send_message(message.chat.id, final_message)
        else:
            bot.send_photo(message.chat.id, f'{m_f_d[randint(1, len(m_f_d))]}')


bot.polling(none_stop=True)
