# import telebot
# from telebot import types

# bot = telebot.TeleBot('')
# to_chat_id = ''

# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     btn1 = types.KeyboardButton('Заказать доставку')
#     btn2 = types.KeyboardButton('О нас')
#     markup.add(btn1,btn2)
#     start_handler = f"<b>Привет {message.from_user.first_name}, что именно тебя интересует?</b>"
#     bot.send_message(message.chat.id, start_handler, parse_mode='html', reply_markup=markup)

# @bot.message_handler(content_types=['text'])
# def menu(message):
#     get_message_bot = message.text.strip().lower()
#     if get_message_bot == "о нас":
#         markup = types.InlineKeyboardMarkup()
#         markup.add(types.InlineKeyboardButton("Посетить Instagram",url="sadasdasd"))
#         bot.send_message(message.chat.id, "Отличный выбор, нажми на кнопку ниже", parse_mode='html', reply_markup=markup)
#     if get_message_bot == "заказать доставку":
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3) #one_time_keyboard=True сразу убирает клаву, после нажатия
#         btn1 = types.KeyboardButton('Ташкент')
#         btn2 = types.KeyboardButton('Фергана')
#         btn3 = types.KeyboardButton('Навои')
#         btn4 = types.KeyboardButton('Самарканд')
#         btn5 = types.KeyboardButton('Бухара')
#         btn6 = types.KeyboardButton('Хива')
#         btn7 = types.KeyboardButton('Коканд')
#         btn8 = types.KeyboardButton('Ургенч')
#         btn9 = types.KeyboardButton('Нукус')
#         markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9)
#         send_mess = f"<b>{message.from_user.first_name}, в каком городе вы проживаете?</b>"
#         bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
#         bot.register_next_step_handler(message, askname)

# def askname(message):
#     markup = types.ReplyKeyboardRemove(selective=False)
#     bot.send_message(message.chat.id, "Напиши свою Ф.И.О.\n\nПример: Иванов Иван Иванович", reply_markup=markup)
#     bot.register_next_step_handler(message, askgeo)
#     markup = types.ReplyKeyboardRemove(selective=False)

# def askgeo(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
#     keyboard.add(button_geo)
#     bot.send_message(message.chat.id, "Отправь мне свою геопозицию", reply_markup=keyboard)
#     markup = types.ReplyKeyboardRemove(selective=False)
#     bot.register_next_step_handler(message, askphone)

# def askphone(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
#     keyboard.add(button_phone)
#     bot.send_message(message.chat.id, "Отправь мне свой номер телефона", reply_markup=keyboard)
#     markup = types.ReplyKeyboardRemove(selective=False)
#     bot.register_next_step_handler(message, askproduct)

# def askproduct(message):
#     markup = types.ReplyKeyboardRemove(selective=False)
#     bot.send_message(message.chat.id, "Пришлите фото или название модели товара\n\nНапример: Смарт часы HW16 / Лампа 52см", reply_markup = markup)
#     markup = types.ReplyKeyboardRemove(selective=False)
#     bot.register_next_step_handler(message, backtostart)

# def backtostart(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     btnn1 = types.KeyboardButton('Заказать доставку')
#     btnn2 = types.KeyboardButton('О нас')
#     markup.add(btnn1,btnn2)
#     start_handler = f"<b>{message.from_user.first_name}, я принял твой заказ :) Что нибудь ещё? </b>"
#     bot.send_message(message.chat.id, start_handler, parse_mode='html', reply_markup=markup)

# if __name__ == '__main__':
#     bot.polling(none_stop=True)

# bot.polling(none_stop=True)