from telebot import *
import requests

bot = telebot.TeleBot("5289724578:AAGQWmsNaLFu35tG0Q5Wgsos5mArcpuMVg0")


def main():

    def for_developer(messang):
        # namespace = messang.from_user.__dict__
        # for k, v in namespace.items():
        #     print(f"{k} : {v}\n")
        # print(f'text : {messang.text}')
        # print('-----------------------------------\n')
        print(messang)


    @bot.message_handler(commands=['start'])
    def start(messang):
        with open("StartText.html", 'rb') as StartFile:
            user_first_name = messang.from_user.first_name.encode()
            bot.send_message(messang.chat.id, user_first_name + StartFile.read(), parse_mode="html")

    @bot.message_handler(commands=['help'])
    def help(messang):
        with open("HelpText.html", "rb") as HelpFile:
            bot.send_message(messang.chat.id, HelpFile.read(), parse_mode='html')

    @bot.message_handler(commands='userinfo')
    def userinfo(messang):
        user_name = messang.from_user.first_name
        user_last_name = messang.from_user.last_name
        user_id = messang.from_user.id
        user_username = messang.from_user.username
        bot.send_message(messang.chat.id, f"=============\n"
                                          f"\tВаши данные\n"
                                          f"=============\n\n"
                                          f"Имя: {str(user_name)}\n"
                                          f"Фамилия: {str(user_last_name)}\n"
                                          f"Ник: @{str(user_username)}\n"
                                          f"ID: {str(user_id)}")

    @bot.message_handler(commands="photo")
    def random_phroto(messang):
        import os
        from random import choice

        image_list = list()
        for filename in os.listdir('image'):
            image_list.append(filename)
        rand_img = choice(image_list)
        name_rand_img = rand_img[:rand_img.rfind('.')]
        bot.send_photo(messang.chat.id, open(r'D:\\Программирование\\TelegramBots\\image\\' + rand_img, "rb"), caption=name_rand_img)

    @bot.message_handler(content_types=["text"])
    def get_user_text(messang):
        if ("привет".upper() or "hello".upper()) in messang.text.upper():
            bot.send_message(messang.chat.id, "И тебе привет!")
        else:
            with open('NotUnderstandText.html', "rb") as file:
                user_first_name = messang.from_user.first_name.encode()
                bot.send_message(messang.chat.id,
                                 user_first_name +
                                 file.read(),
                                 parse_mode="html")
        for_developer(messang)

    bot.infinity_polling()


try:
    main()
except Exception as e:
    print(e)
    main()