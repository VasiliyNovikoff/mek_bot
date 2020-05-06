import telebot
from mek_dict import mek_dict
from random import randint
from mek_photo_dict import m_f_d

bot = telebot.TeleBot('1088368052:AAErWQO3QqQrzFzoJbVpyVlZ9Urye250VA8')


@bot.message_handler(content_types=['text'])
def mess(message):
    m_b = message.text.strip().lower()
    rnd = randint(0, 10)
    m1 = 'mek'
    m2 = 'мек'
    m3 = "кош"
    m4 = "кот "
    if (m1 in m_b) or (m2 in m_b) or (m3 in m_b) or (m4 in m_b):
        if rnd > 3:
            final_message = f'{mek_dict[randint(1, len(mek_dict))]}'
            bot.send_message(message.chat.id, final_message)
        else:
            bot.send_photo(message.chat.id, f'{m_f_d[randint(1, len(m_f_d))]}')


bot.polling(none_stop=True)
