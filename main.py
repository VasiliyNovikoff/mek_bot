import telebot
import yaml
from mek_dict import mek_dict
from random import randint
from mek_photo_dict import m_f_d

'''
Requested a bot token from BotFather and placed it in the 'token.yml' file 
in the form of "token: 'our bot token'".
Added 'token.yml' in the '.gitignore'
'''
with open("token.yml") as f:
    f = yaml.load(f, Loader=yaml.FullLoader)
    token = f['token']

bot = telebot.TeleBot(f'{token}')
print("Mek starting!")


@bot.message_handler(content_types=['text'])
def mess(message):
    m_b = message.text.strip().lower()
    rnd = randint(0, 10)
    m1 = 'mek'
    m2 = 'мек'
    m3 = "кош"
    m4 = "кот "
    # If there is "mek", "мек", "кош", "кот" in the message, the bot will respond
    if (m1 in m_b) or (m2 in m_b) or (m3 in m_b) or (m4 in m_b):
        if rnd > 5:
            # send one of the nicknames
            final_message = f'{mek_dict[randint(1, len(mek_dict))]}'
            bot.send_message(message.chat.id, final_message)
        else:
            # send one of a funny photo
            bot.send_photo(message.chat.id, f'{m_f_d[randint(1, len(m_f_d))]}')


bot.polling(none_stop=True)
