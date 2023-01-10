import os
from dotenv import load_dotenv
import telebot
from PIL import Image, ImageDraw, ImageFont
from textwrap import fill
from random import choice
import redis

load_dotenv()

database = redis.Redis(host='localhost', port=6379, db=0)
bot = telebot.TeleBot(os.getenv('API_KEY'))


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    bot.send_message(message.from_user.id, 'Ауф! Цитатка дня для риал пацана: ')

    img = ['static/wolf_2.jpg', 'static/wolf_6.jpg', 'static/wolf_8.jpg', 'static/wolf_9.jpeg', 'static/wolf_10.jpg']
    img_open = Image.open(choice(img))
    idraw = ImageDraw.Draw(img_open)
    quote = ['Кем бы ты ни был, кем бы ты не стал, помни, где ты был и кем ты стал.',
             'Лучше быть последним – первым, чем первым – последним.',
             'Работа не волк, работа это ворк, а волк это ходить.',
             'Лев, может, и король джунглей, но волк в цирке не выступает.',
             'У волков нет правил поведения. Они им не нужны. Волкам, чтобы быть волками, не нужны никакие правила.',
             'Неважно, кто напротив. Важно, кто рядом.',
             'Волк не дергается, когда псы лают.',
             'Понять волка легко, если только не пытаться его объяснить.',
             'Волк слишком энергичен чтобы работать.',
             'На случай, если буду нужен, то я там же, где и был, когда был не нужен.',
             'Мы с тобой живучие волки. А сердце, наверное, болит от крепкого кофе…',
             'Если не будешь с волками в стае, то станешь их кормом.',
             'Ты словно волк — всегда осторожный и в меру голодный.',
             'Он не поставит в жизни точки. Ничто не может быть сильней, Чем сердце волка-одиночки.',
             'Я тебе доверяю, но ты иногда что-то скрываешь. ~Серега']
    text_wolf = fill(choice(quote), width=25)
    font = ImageFont.truetype("arial.ttf", size=55)
    idraw.text((10, 10), text_wolf, font=font, fill='#c6f2ea')
    img_open.save('img_open_watermarked.png')
    bot.send_photo(message.chat.id, img_open)


bot.polling(none_stop=True, interval=0)
