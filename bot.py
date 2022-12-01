from telebot import types
from creat_bot import *
import test1 as t1
import constructor as con
import logging
bot = creat()


logging.basicConfig(filename="server.log", level=logging.INFO)
logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>'

    bot.send_message(message.chat.id, mess,
                     parse_mode='html', reply_markup=keyboard)


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'photo i ts cool')


# keyboard
def read_file():
    with open('info.txt', 'r') as txt_file: text1 = str(txt_file.read())
    return text1

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

item1 = types.KeyboardButton('Во что поиграть???')
item2 = types.KeyboardButton('создание персонажа')
item3 = types.KeyboardButton('что посмотреть?')
item4 = types.KeyboardButton('информация о боте')

keyboard.row(item1, item2)
keyboard.row(item3, item4)

# keyboard.add(item1)
# keyboard.add(item2)
# keyboard.add(item3)
# keyboard.add(item4)

bot.send_message


@bot.message_handler(content_types=['text'])
def get_user_info(message):
    # if message.chat.type == 'private':
    if message.text == 'Во что поиграть???':
        photo = open('photo.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    if message.text == 'Во что поиграть???':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton(
            'Игры на ПК', callback_data='PC Game')
        item2 = types.InlineKeyboardButton(
            'Настольные игры', callback_data='Board Game')
        markup.add(item1, item2)

        bot.send_message(message.chat.id, 'Выберите платформу',
                         parse_mode='html', reply_markup=markup)
    elif message.text.lower() == 'информация о боте':
        photo = open('Аватар функции 2.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, read_file())
       
        #  begin что посмотреть 
    elif message.text.lower() == 'что посмотреть?':
        photo = open('cinema.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        inMurkup = types.InlineKeyboardMarkup(row_width=2)
        # check = requests.head(url='https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D1%80%D0%BC%D0%B8%D0%BD%D0%B0%D1%82%D0%BE%D1%80_2:_%D0%A1%D1%83%D0%B4%D0%BD%D1%8B%D0%B9_%D0%B4%D0%B5%D0%BD%D1%8C')
        # print(check.status_code)
        but1 = types.InlineKeyboardButton("Терминатор 2", url='https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D1%80%D0%BC%D0%B8%D0%BD%D0%B0%D1%82%D0%BE%D1%80_2:_%D0%A1%D1%83%D0%B4%D0%BD%D1%8B%D0%B9_%D0%B4%D0%B5%D0%BD%D1%8C')
        but2 = types.InlineKeyboardButton("Искуственный интелект", url='https://ru.wikipedia.org/wiki/%D0%98%D1%81%D0%BA%D1%83%D1%81%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9_%D0%B8%D0%BD%D1%82%D0%B5%D0%BB%D0%BB%D0%B5%D0%BA%D1%82_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)')
        but3 = types.InlineKeyboardButton("Господин никто", url='https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%81%D0%BF%D0%BE%D0%B4%D0%B8%D0%BD_%D0%9D%D0%B8%D0%BA%D1%82%D0%BE_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC,_2009)')
        but4 = types.InlineKeyboardButton("Сайлент хилл", url='https://ru.wikipedia.org/wiki/%D0%A1%D0%B0%D0%B9%D0%BB%D0%B5%D0%BD%D1%82_%D0%A5%D0%B8%D0%BB%D0%BB_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)')
        but5 = types.InlineKeyboardButton("Пятый элемент", url='https://ru.wikipedia.org/wiki/%D0%9F%D1%8F%D1%82%D1%8B%D0%B9_%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)')
        but6 = types.InlineKeyboardButton("Матрица", url='https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)')
        but7 = types.InlineKeyboardButton("ОНО", url='https://ru.wikipedia.org/wiki/%D0%9E%D0%BD%D0%BE_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC,_2017)')
        but8 = types.InlineKeyboardButton("Звездные войны", url='https://ru.wikipedia.org/wiki/%D0%97%D0%B2%D1%91%D0%B7%D0%B4%D0%BD%D1%8B%D0%B5_%D0%B2%D0%BE%D0%B9%D0%BD%D1%8B')
        but9 = types.InlineKeyboardButton("Властелин колец. \nБратство кольца", url='https://hd.kinopoisk.ru/film/4b1c140be7efc668a518bb8718ba159f')
        but10 = types.InlineKeyboardButton("Властелин колец. \nДве крепости", url='https://hd.kinopoisk.ru/film/4edfc8baf73a662bbcff2aee028c3e5f?from_block=kp-button-online')
        but11 = types.InlineKeyboardButton("Властелин колец. \nВозвращение короля", url='https://hd.kinopoisk.ru/film/469dd100cdfca80d94219646f6731e78')
        
        # inMurkup = types.InlineKeyboardMarkup(row_width=3)
        but12 = types.InlineKeyboardButton("Спасибо, выберу сам!", url='https://www.kinopoisk.ru/')
        inMurkup.add(but1, but2, but3, but4,but5, but6, but7, but8, but9, but10, but11, but12)
        bot.send_message(message.chat.id, "Фильмы на любой вкус", reply_markup=inMurkup)
        
        # end что посмотреть

    elif message.text == 'создание персонажа':
        photo = open('Аватар функции 1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton(
            'Текстовый документ', callback_data='Text_Doc')
        item2 = types.InlineKeyboardButton(
            'Excel-файл с одним персонажем', callback_data='Excel_one_character')
        item3 = types.InlineKeyboardButton(
            'Excel-таблицу с множеством персонажей', callback_data='Excel_only_character')
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id, text="В каком виде вы хотите получить карточку персонажа?", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю',
                         parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'PC Game':
                bot.send_message(call.message.chat.id,
                                 '1. Divinity original sin')
                bot.send_message(
                    call.message.chat.id, 'https://store.steampowered.com/app/373420/Divinity_Original_Sin__Enhanced_Edition/')
                bot.send_message(call.message.chat.id,
                                 '2. Pillars of Eternity')
                bot.send_message(
                    call.message.chat.id, 'https://store.steampowered.com/app/291650/Pillars_of_Eternity/')
                bot.send_message(call.message.chat.id,
                                 '3. Pathfinder: Wrath of the Righteous ')
                bot.send_message(
                    call.message.chat.id, 'https://store.steampowered.com/app/1694800/Pathfinder_Wrath_of_the_Righteous__Commander_Pack/')
                bot.send_message(call.message.chat.id,
                                 "4. Baldur's Gate: Enhanced Edition")
                bot.send_message(
                    call.message.chat.id, 'https://store.steampowered.com/app/228280/Baldurs_Gate_Enhanced_Edition/')
                bot.send_message(call.message.chat.id,
                                 '5. SpellForce 3 Reforced')
                bot.send_message(
                    call.message.chat.id, 'https://store.steampowered.com/app/311290/SpellForce_3_Reforced/')
            elif call.data == 'Board Game':
                bot.send_message(call.message.chat.id,
                                 '1. Dungeons & Dragons. Врата Балдура: Нисхождение в Авернус')
                bot.send_message(call.message.chat.id,
                                 'https://hobbygames.ru/dungeons-and-dragons-vrata-baldura-nishozhdenie-v-avernus')
                bot.send_message(
                    call.message.chat.id, '2. The Lord of the Rings: Travels in Middle-earth')
                bot.send_message(
                    call.message.chat.id, 'https://hobbygames.ru/vlastelin-kolec-stranstvija-v-sredizeme')
                bot.send_message(
                    call.message.chat.id, '3. Pathfinder. НРИ. Вторая редакция. Серия приключений "Зловещие катакомбы"')
                bot.send_message(
                    call.message.chat.id, 'https://hobbygames.ru/pathfinder-nri-vtoraja-redakcija-serija-prikljuchenij-zloveshhie-katakombi')
                bot.send_message(
                    call.message.chat.id, '4. Warhammer Underworlds: Gnarlwood')
                bot.send_message(
                    call.message.chat.id, 'https://hobbygames.ru/warhammer-underworlds-gnarlwood')
                bot.send_message(
                    call.message.chat.id, '5. Войны Чёрной Розы')
                bot.send_message(
                    call.message.chat.id, 'https://hobbygames.ru/vojni-chjornoj-rozi')
            elif call.data == 'Text_Doc':
                photo = open('Аватар функции 4.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo)
                t1.text_file2()
                doc = open("Команда персонажей.txt", 'rb')
                bot.send_document(call.message.chat.id, doc)
                #bot.send_document(call.message.chat.id, "Общий список с переносами.txt")
            elif call.data == 'Excel_one_character':
                photo = open('Аватар функции 5.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo)
                con.character_creater()
                doc = open("Persona.xls", 'rb')
                bot.send_document(call.message.chat.id, doc)
            elif call.data == 'Excel_only_character':
                photo = open('Аватар функции 3.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo)
                t1.Excel_All()
                doc = open("Общая таблица персонажей.xlsx", 'rb')
                bot.send_document(call.message.chat.id, doc)
                #bot.send_message(call.message.chat.id, 'и это, кстати, пока не умею')
            # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
            #     reply_markup=None)

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
