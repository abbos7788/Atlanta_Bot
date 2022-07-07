import telebot
import config
from telebot import types
from string import Template

bot = telebot.TeleBot(config.TOKEN)

user_dict = {}

class User:
    def __init__(self, city):
        self.city = city

        keys = ['jins','fio','joy', 't_sana', 
                't_raqam', 'uz_daraja', 'ru_daraja', 
                'oxirgi_ish_joyi', 'staj', 'rasm']
        
        for key in keys:
            self.key = None

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup_start = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text="🏢 |Kompaniya Haqida")
    btn2 = types.KeyboardButton(text="💼 |Bo'sh ish o'rinlari")
    btn3 = types.KeyboardButton(text="✉️ |Xabar yuborish")
    btn4 = types.KeyboardButton(text="📞 |Kontakt/Manzil")
    
    markup_start.add(btn1, btn2, btn3, btn4)
    images_path = 'images\phota01.jpg'
    text = "<b>Menyulardan birini tanlang!</b>"
    caption_text = "\n<b>Bot-sayt Atlanta do'konlar tarmog'iga nomzodlarni ishga joylashtirish uchun mo'ljallangan.</b>"
    bot.send_photo(message.chat.id, photo=open(images_path, 'rb'), caption=caption_text, parse_mode="HTML", reply_markup=markup_start) 
    bot.send_message(message.chat.id, text, parse_mode="HTML", reply_markup=markup_start)

@bot.message_handler(content_types=['text'])
def menu(message):
    get_message_bot = message.text.strip()
    if get_message_bot == "🏢 |Kompaniya Haqida":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn7 = types.KeyboardButton(text="📍 |Bizning manzilimiz!")
        markup.add(btn7)
        caption_text = """\n<b>ATLANTA</b>

Erkaklar va bolalar kiyimlari do'koni!

Atlanta 2019-yil, 7-martda ochildi.

Afzalliklari:

☑️Qulay joylashuv,

☑️Yuqori sifat,

☑️So'ngi urf,

☑️Keng assortiment,

☑️Hamyonbop narx,

☑️Bonuslar,

☑️Peredelka xizmati bepul."""
        images_path = 'images\phota02.jpg'
        bot.send_photo(message.chat.id, photo=open(images_path, 'rb'), caption=caption_text, parse_mode="HTML", reply_markup=markup)
        bot.register_next_step_handler(message, manzil)

    elif get_message_bot == "💼 |Bo'sh ish o'rinlari":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn8 = types.KeyboardButton(text="👨🏻‍💼 |Marketing bo'limi raxbari")
        btn9 = types.KeyboardButton(text="🧑🏻‍💻 |SMM mutaxasisi")
        btn10 = types.KeyboardButton(text="🦹🏻 |Bloger")
        btn11 = types.KeyboardButton(text="🧑🏻‍🎨 |Fotograf")     
        markup.add(btn8, btn9, btn10, btn11)
        text = """Ushbu bot bo'limi "Atlanta" kompaniyasida so'rovnomani to'ldirish✍️  va ishga joylashish uchun mo'ljallangan!

Bu yerda siz anketani to'ldirishingiz📄 va kompaniyamizdagi mavjud vakansiyalarni ko'rishingiz mumkin!"""
        bot.send_message(message.chat.id, text, parse_mode="HTML", reply_markup=markup)
        bot.register_next_step_handler(message, jobs_menyu)

    elif get_message_bot == "✉️ |Xabar yuborish":
        caption_text = """<b>✉️Savol va takliflaringizni yozib qoldiring,  
Biz albatta siz bilan bog'lanamiz</b>"""
        images_path = 'images\phota05.png'
        # удалить старую клавиатуру
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_photo(message.chat.id, photo=open(images_path, 'rb'), caption=caption_text, parse_mode="HTML", reply_markup=markup)
        bot.register_next_step_handler(message, xabar_yozish)

    elif get_message_bot == "📞 |Kontakt/Manzil":
        caption_text = """
<b>😊 Bizga qo'ng'iroq qiling

☎️Murojaat uchun:</b>

+998(33)434-50-15
+998(94)545-50-15

<a href="https://maps.app.goo.gl/hKB3sm7N2v1JCsGh9">➜ Joylashuv</a>

<a href="https://instagram.com/atlanta_uz?igshid=YmMyMTA2M2Y=">➜ Instagram</a>

<i>Ish vaqti : 9.00-22.00 dushanba-yakshanba</i>"""
        images_path = 'images\manzil_tel.jpg'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn99 = types.KeyboardButton(text="🏠 |Asosiy")
        markup.add(btn99)
        bot.send_photo(message.chat.id, photo=open(images_path, 'rb'), caption=caption_text, parse_mode="HTML", reply_markup=markup)
        bot.send_location(message.from_user.id, 41.3092418,69.265108)
        bot.register_next_step_handler(message, send_welcome)
    
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn87 = types.KeyboardButton(text="🏠 |Asosiy")
        markup.add(btn87)
        bot.send_message(message.chat.id, "<b>Noto'g'ri buruq berdingiz!\nIltimos qaytadan urinib ko'ring!</b>", parse_mode="HTML", reply_markup=markup)
        bot.register_next_step_handler(message, send_welcome)


def xabar_yozish(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn88 = types.KeyboardButton(text="🏠 |Asosiy")
    markup.add(btn88)
    bot.send_message(config.chat_id2, text=f"<b>Savol, Taklif ushbu profiledan: @{message.from_user.username} </b>\n\n" + message.text, parse_mode="HTML", reply_markup=markup)
    bot.send_message(message.chat.id, "<b>Savol, Taklifingiz qabul qilindi tez kunda xodimlarimiz siz bilan bog'lanishadi!</b>\n\n<i>E'tiboringiz uchun raxmat!</i>", parse_mode="HTML", reply_markup=markup)
    bot.register_next_step_handler(message, send_welcome)

def jobs_menyu(message):
    global a
    a = message.text
    if message.text == "👨🏻‍💼 |Marketing bo'limi raxbari":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn21 = types.KeyboardButton(text="👨 |Erkak")
        btn22 = types.KeyboardButton(text="👩 Ayol")
        markup.add(btn21, btn22)
        text = """Marketing bòlim rahbari uchun talablar:

🔹 Tajribasi kamida 1-3 yil bòlishi ;
🔹Erishgan natijalarining portfolisini taqdim etishi ;
🔹 Òzbek, rus tillarini bilishi;
🔹 Òz yo'nalishida biriktirilgan xodimlarni vazifalarini berib boshqara olishi ( SMM, SRM,Fotograf Operator...) kabilar;
🔹Liderlik qobilyatiga ega bo'lishi ; 
🔹Servisga asoslangan holda savdo hajmini ijtimoiy tarmoqlar orqali oshirishi 
🔹Yangi mijozlar oqimini jalb qilishi ;
🔹Bor mijozlarni ushlab qolishi ;
🔹Qaytgan mijozlarni jalb qilishi.
🔹Xisob kitob va hisobotlar bilan ishlay olishi talab etiladi 

💰Oylik ish haqi
5 000 000 so'mdan 8 000 000 so'mgacha"""
        bot.send_message(message.chat.id, text, parse_mode="HTML", reply_markup=markup)
        bot.send_message(message.chat.id, "Jinsni tanlang!", parse_mode="HTML", reply_markup=markup)
        bot.register_next_step_handler(message, jobs)

    elif message.text == "🧑🏻‍💻 |SMM mutaxasisi":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn21 = types.KeyboardButton(text="👨 |Erkak")
        btn22 = types.KeyboardButton(text="👩 Ayol")
        markup.add(btn21, btn22)
        text = """SMM mutaxassisidan talab qilinadiganlar:

🔹 Portfolioga ega boʻlishi;
🔹 Kontent plan tuza olishi;
🔹 Instagram, Telegram, You Tube, Tik Tok kabi ijtimoiy tarmoqlarni professional bilishi;
🔹 Trendlarni kuzatish va ulardan foydalanishi;
🔹Ingliz yoki rus tilini bilishi.

💰Oylik maosh:
3.000.000 so'm dan 5.000.000 so'm gacha"""
        bot.send_message(message.chat.id, text, parse_mode="HTML", reply_markup=markup)
        bot.send_message(message.chat.id, "Jinsni tanlang!", parse_mode="HTML", reply_markup=markup)
        bot.register_next_step_handler(message, jobs)

    elif message.text == "🦹🏻 |Bloger":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn21 = types.KeyboardButton(text="👨 |Erkak")
        btn22 = types.KeyboardButton(text="👩 Ayol")
        markup.add(btn21, btn22)
        text = """Blogerga qo'yiladigan talablar: 

🔹 Òz ustida muntazam ish olib borishi, sòngi trendlardan xabardor bòlishi; 
🔹 Ijtimoiy tarmoqlardan bemalol foydalana olishi;
🔹 Kiyim sohasidagi malumotlarni yorib bera olishi;
🔹 Yoshi 18 yoshdan 25 yoshgacha bòlishi;
🔹 O'zbek rus tillarida erkin gaplasha olishi; 
🔹 Tashqi ko'rinish muhim;
🔹Nutqi ravon bòlishi;
🔹 Òziga ishongan bòlishi; 
🔹 Xarezmaga ega bòlishi;
🔹Komputer, capcut, piskart, va boshqa programmalarda ishlay olishi.

💰Oylik ish haqi
4.000.000 usz dan 8.000.000 usz gacha"""
        bot.send_message(message.chat.id, text, parse_mode="HTML", reply_markup=markup)
        bot.send_message(message.chat.id, "Jinsni tanlang!", parse_mode="HTML", reply_markup=markup)
        bot.register_next_step_handler(message, jobs)

    elif message.text == "🧑🏻‍🎨 |Fotograf":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn21 = types.KeyboardButton(text="👨 |Erkak")
        btn22 = types.KeyboardButton(text="👩 Ayol")
        markup.add(btn21, btn22)
        text = """Fotograf uchun talablar:

🔹 Tajribasi kamida 3 yil bòlishi ;
🔹 Kompyuterda microsoft, fotoshop, capkut, piskart va boshqa dasturlarda ishlab bilishi;
🔹 Mahsulotlarning jozibasini rasmda aks ettira olishi kerak;
🔹 So'ngi trendlardan to'gri foydalana olishi ;
🔹 Har bir rasmga kreativ yondasha olishi.

Ish vaqti : 
Kelishiladi

💰Oylik ish haqi
Kelishiladi"""
        bot.send_message(message.chat.id, text, parse_mode="HTML", reply_markup=markup)
        bot.send_message(message.chat.id, "Jinsni tanlang!", parse_mode="HTML", reply_markup=markup)
        bot.register_next_step_handler(message, jobs)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn89 = types.KeyboardButton(text="🏠 |Asosiy")
        markup.add(btn89)
        bot.send_message(message.chat.id, "<b>Noto'g'ri buruq berdingiz!\nIltimos qaytadan urinib ko'ring!</b>", parse_mode="HTML", reply_markup=markup)
        bot.register_next_step_handler(message, send_welcome)

def jobs(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)
        user = user_dict[chat_id]
        user.jins = message.text
        

        # удалить старую клавиатуру
        markup = types.ReplyKeyboardRemove(selective=False)
        text = """<b>👤 Ism sharifingizni kiriting:
(Nazarov Abbos Olim o'g'li)</b>"""
        msg = bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=markup)
        bot.register_next_step_handler(msg, process_fullname_step)

    except Exception as e:
        text = """📌Eslatma
Yuqorida ko'rsatilgan namuna bo'yicha kiriting"""
        msg = bot.reply_to(message, text)
        bot.register_next_step_handler(msg, jobs)

def process_fullname_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.fio = message.text

        text = """"<b>📅 Tug'ilgan kuningizni kiriting(yyyy-mm-dd)</b>"""
        msg = bot.send_message(chat_id, text, parse_mode="HTML")
        bot.register_next_step_handler(msg, process_b_date_step)

    except Exception as e:
        text = """<b>📌Eslatma
Yuqorida ko'rsatilgan namuna bo'yicha kiriting</b>"""
        msg = bot.reply_to(message, text)
        bot.register_next_step_handler(msg, process_fullname_step)

def process_b_date_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.t_sana = message.text

        text = """"<b>🏠Yashash manzili (Tuman, ko'cha/kvartal, uy, xonadon):</b>"""
        msg = bot.send_message(chat_id, text, parse_mode="HTML")
        bot.register_next_step_handler(msg, process_joy_step)

    except Exception as e:
        text = """<b>📌Eslatma
Yuqorida ko'rsatilgan namuna bo'yicha kiriting</b>"""
        msg = bot.reply_to(message, text)
        bot.register_next_step_handler(msg, process_b_date_step)

def process_joy_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.joy = message.text

        text = """"<b>📱 O'z telefon raqamingizni yuboring (masalan: +998931234567):</b>"""
        msg = bot.send_message(chat_id, text, parse_mode="HTML")
        bot.register_next_step_handler(msg, process_raqam_step)

    except Exception as e:
        text = """📌Eslatma
Yuqorida ko'rsatilgan namuna bo'yicha kiriting"""
        msg = bot.reply_to(message, text)
        bot.register_next_step_handler(msg, process_joy_step)

def process_raqam_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.t_raqam = message.text

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        btn40 = types.KeyboardButton("Boshlang'ich")
        btn41 = types.KeyboardButton("A'lo")
        btn42 = types.KeyboardButton("O'rtacha")
        btn43 = types.KeyboardButton("Erkin")
        markup.add(btn40, btn41, btn42, btn43)
        
        text = """"<b>O'zbek tilini bilish darajangiz qanday? 🇺🇿</b>"""
        msg = bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=markup)
        bot.register_next_step_handler(msg, process_uz_daraja_step)

    except Exception as e:
        text = """<b>📌Eslatma
Yuqorida ko'rsatilgan namuna bo'yicha kiriting</b>"""
        msg = bot.reply_to(message, text)
        bot.register_next_step_handler(msg, process_raqam_step)

def process_uz_daraja_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.uz_daraja = message.text

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        btn50 = types.KeyboardButton("Boshlang'ich")
        btn51 = types.KeyboardButton("A'lo")
        btn52 = types.KeyboardButton("O'rtacha")
        btn53 = types.KeyboardButton("Erkin")
        markup.add(btn50, btn51, btn52, btn53)

        text = """"Rus tilini bilish darajangiz qanday? 🇷🇺"""
        msg = bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=markup)
        bot.register_next_step_handler(msg, process_ru_daraja_step)

    except Exception as e:
        text = """📌Eslatma
Yuqorida ko'rsatilgan namuna bo'yicha kiriting"""
        msg = bot.reply_to(message, text)
        bot.register_next_step_handler(msg, process_uz_daraja_step)

def process_ru_daraja_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.ru_daraja = message.text
        
        # # удалить старую клавиатуру
        # markup = types.ReplyKeyboardRemove(selective=False)
        text = """"<b>Oxirgi ish joyingiz nomi:
Davr, tashkilot, lavozim</b>"""
        msg = bot.send_message(chat_id, text, parse_mode="HTML")
        bot.register_next_step_handler(msg, process_oxirgi_ish_joyi_step)

    except Exception as e:
        text = """<b>📌Eslatma
Yuqorida ko'rsatilgan namuna bo'yicha kiriting</b>"""
        msg = bot.reply_to(message, text)
        bot.register_next_step_handler(msg, process_ru_daraja_step)

def process_oxirgi_ish_joyi_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.oxirgi_ish_joyi = message.text

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        btn30 = types.KeyboardButton("hali ish tajribam yo'q")
        btn31 = types.KeyboardButton('1 dan 3 yilgacha')
        btn32 = types.KeyboardButton('3 yildan 5 yilgacha')
        btn33 = types.KeyboardButton("6 yildan ko'p")
        markup.add(btn30, btn31, btn32, btn33)

        text = """"<b>Ish tajribangiz qanday ?</b>"""
        msg = bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=markup)
        bot.register_next_step_handler(msg, process_staj_step)

    except Exception as e:
        text = """<b>📌Eslatma
Yuqorida ko'rsatilgan namuna bo'yicha kiriting</b>"""
        msg = bot.reply_to(message, text)
        bot.register_next_step_handler(msg, process_oxirgi_ish_joyi_step)

def process_staj_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.staj = message.text

        # удалить старую клавиатуру
        # markup = types.ReplyKeyboardRemove(selective=False)
        text = """"<b>🤵 Rasmingizni yuboring (hujjat uchun rasm)</b>"""
        msg = bot.send_message(chat_id, text, parse_mode="HTML")
        bot.register_next_step_handler(msg, process_rasm_step)

    except Exception as e:
        text = """<b>📌Eslatma
Yuqorida ko'rsatilgan namuna bo'yicha kiriting</b>"""
        msg = bot.reply_to(message, text)
        bot.register_next_step_handler(msg, process_staj_step)

def process_rasm_step(message):
    try:
        if message.content_type == 'photo':
            global a
            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.rasm = message.text

            markup7 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn58 = types.KeyboardButton(text="🏠 |Asosiy")
            markup7.add(btn58)
            
            # ваша заявка "Имя пользователя"
            bot.send_photo(config.chat_id2, photo=message.photo[-1].file_id, caption=getRegData(user, '\n\n<b>Ariza egasining Profile Name: </b>', message.from_user.first_name + f"\n<b>Username: @{message.from_user.username} </b>\n" + f"\n<b>Ariza ushbu vakansiya uchun: \n</b>{a}\n"), parse_mode="HTML", reply_markup=markup7)

            bot.send_photo(chat_id, photo=message.photo[-1].file_id, caption=getRegData(user, '\nArizachi: ', message.from_user.first_name ), parse_mode="HTML", reply_markup=markup7)
            bot.send_message(chat_id, "<b>Arizangiz qabul qilindi. Tez kunda xodimlarimiz siz bilan bog'lanishadi!</b>\n\n<i>Bizning Kompaniyamizni tanlaganingiz uchun raxmat!</i>", parse_mode="HTML")
            
            bot.register_next_step_handler(message, send_welcome)

        else:
            # text = "<b>Noto'g'ri malumot jo'natdingiz, Qaytadan urinib ko'ring!</b>"
            bot.reply_to(chat_id, "Noto'g'ri malumot jo'natdingiz, Qaytadan urinib ko'ring!")
    except Exception as e:
        text = """<b>📌Eslatma
Yuqorida ko'rsatilgan namuna bo'yicha kiriting</b>"""
        msg = bot.reply_to(message, text)
        bot.register_next_step_handler(msg, process_staj_step)


        
def getRegData(user, title, name):

    t = Template('$title <b>$name</b> \n Jins: <b>$jins</b>\n F.I.O: <b>$fio</b> \n Yashash joyi: <b>$joy</b> \n Tug\'ulgan sana: <b>$t_sana</b>\n Telefon raqam: <b>$t_raqam</b> \n O\'zbekcha daraja: <b>$uz_daraja</b> \n Ruscha daraja: <b>$ru_daraja</b> \n Oxirgi ish joyi: <b>$oxirgi_ish_joyi</b> \n Staj: <b>$staj</b> ')

    return t.substitute({
        'title': title,
        'name': name,
        'fio': user.fio,
        'jins': user.jins,
        'joy': user.joy,
        't_sana': user.t_sana,
        't_raqam': user.t_raqam,
        'uz_daraja': user.uz_daraja,
        'ru_daraja': user.ru_daraja,
        'oxirgi_ish_joyi': user.oxirgi_ish_joyi,
        'staj': user.staj,
        'rasm': user.rasm,
    })

def manzil(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn14 = types.KeyboardButton(text="🏠 |Bosh Sahifa")
    btn15 = types.KeyboardButton(text="⬅️ |Orqaga qaytish")
    markup.add(btn14,btn15)
    caption_text = "\n<b>Bizning Manzilimiz:</b>\n\nМирабадский район, Ташкент, Узбекистан\n"
    images_path = 'images\phota04.jpg'
    bot.send_photo(message.chat.id, photo=open(images_path, 'rb'), caption=caption_text, parse_mode="HTML", reply_markup=markup)
    bot.send_location(message.from_user.id, 41.3092418,69.265108)
    bot.register_next_step_handler(message, send_welcome)
    

if __name__ == '__main__':
    bot.polling(none_stop=True)
