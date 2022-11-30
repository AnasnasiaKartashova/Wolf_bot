from api import API_KEY
import telebot
from random import choice
import redis

database = redis.Redis(host='localhost', port=6379, db=0)
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    img = ['wolf.jfif', 'wolf_2.jpg', 'wolf_3.jfif', 'wolf_4.jfif', 'wolf_5.jfif',
           'wolf_6.jpg', 'wolf_7.jpg', 'wolf_8.jpg', 'wolf_9.jpeg', 'wolf_10.jpg']
    img_open = open(choice(img), 'rb')
    bot.send_photo(message.chat.id, img_open)
    bot.send_message(message.from_user.id, 'Ауф! Цитатка дня для риал пацана: ')
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
    bot.send_message(message.from_user.id, f'{choice(quote)}')


bot.polling(none_stop=True, interval=0)
