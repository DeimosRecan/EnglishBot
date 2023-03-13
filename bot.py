import telebot
import logging
import aiogram
import time
from telebot import types

bot = telebot.TeleBot('5499217323:AAEPhYHn2LK_LjVYBKic5T43jJ4kFO7VMqU')

@bot.message_handler(commands=['start'])
def start_handler(message:types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('Задания', callback_data='tasks')
    item2 = types.InlineKeyboardButton('Теория', callback_data='theory')
    item3 = types.InlineKeyboardButton('Справка', callback_data='reference')
    markup.add(item, item2, item3)

    bot.send_message(message.chat.id,
                           'Привет, этот бот содержит упражнения по основным темам грамматики английского языка. Перед выполнением заданий рекомендуется ознакомиться с теорией.',
                           reply_markup=markup)

    for i in range(10):
        time.sleep(86400)
        bot.send_message(message.chat.id, 'Изучал ли ты сегодня английский?')

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    MarkupTask = types.InlineKeyboardMarkup(row_width=2)
    itemTask = types.InlineKeyboardButton('Артикли', callback_data='articlesTasks')
    itemTask1 = types.InlineKeyboardButton('Местоимения', callback_data='pronounsTasks')
    itemTaskBack = types.InlineKeyboardButton('Назад', callback_data='MainMenuBack')
    MarkupTask.add(itemTask, itemTask1, itemTaskBack)

    MarkupTaskArticles = types.InlineKeyboardMarkup(row_width=3)
    itemTask1 = types.InlineKeyboardButton('Задание 1', callback_data='articlesTask1')
    itemTask2 = types.InlineKeyboardButton('Задание 2', callback_data='articlesTask2')
    itemTask3 = types.InlineKeyboardButton('Задание 3', callback_data='articlesTask3')
    itemTaskArticlesBack = types.InlineKeyboardButton('Назад', callback_data='TasksBack')
    MarkupTaskArticles.add(itemTask1, itemTask2, itemTask3, itemTaskArticlesBack)

    MarkupTheory = types.InlineKeyboardMarkup(row_width=2)
    itemTheory = types.InlineKeyboardButton('Артикли', callback_data='articlesTh')
    itemTheory1 = types.InlineKeyboardButton('Местоимения', callback_data='pronounsTh')
    itemTheoryArticlesBack = types.InlineKeyboardButton('Назад', callback_data='MainMenuBack')
    MarkupTheory.add(itemTheory, itemTheory1,itemTheoryArticlesBack)

    MarkupReference = types.InlineKeyboardMarkup(row_width=2)
    itemReferenceBack = types.InlineKeyboardButton('Назад', callback_data='MainMenuBack')
    MarkupReference.add(itemReferenceBack)

    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('Задания', callback_data='tasks')
    item2 = types.InlineKeyboardButton('Теория', callback_data='theory')
    item3 = types.InlineKeyboardButton('Справка', callback_data='reference')
    markup.add(item, item2, item3)

    if call.message:
        if call.data == 'tasks':
            bot.send_message(call.message.chat.id, 'Выберите тип заданий:', reply_markup=MarkupTask)
        if call.data == 'theory':
            bot.send_message(call.message.chat.id, 'Выберите раздел теории:', reply_markup=MarkupTheory)
        if call.data == 'reference':
            bot.send_message(call.message.chat.id, 'Этот бот был сделан с помощью учебника \nГолицынский Ю. Б Грамматика: Сборник упражнений.— 5-е изд. —СПб.: КАРО, 2006.— 544 с.'
                                                   '\n https://pgtk-perm.ru/Docs/%D0%A1%D1%82%D1%83%D0%B4%D0%B5%D0%BD%D1%82%D1%83/%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F%20%D0%BD%D0%B0%20%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4%20%D1%8D%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F/13.04.20-19.04.20/%D0%93%D0%BE%D0%BB%D0%B8%D1%86%D1%8B%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%B1%D0%BE%D1%80%D0%BD%D0%B8%D0%BA%20%D1%83%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D0%B9.pdf',
                             reply_markup=MarkupReference)

        if call.data == 'MainMenuBack':
            bot.send_message(call.message.chat.id,
                             'Этот бот содержит упражнения по основным темам грамматики английского языка. Перед выполнением заданий рекомендуется ознакомиться с теорией.',
                             reply_markup=markup)

        if call.data == 'articlesTh':
            bot.send_message(call.message.chat.id,
                             'Перед каждым нарицательным существительным должен стоять артикль. Если вы не употребляете артикль перед существительным, вы должны уметь объяснить, почему.'
                             ' \n\nАртикль не употребляется, если перед существительным стоит притяжательное или указательное местоимение, другое существительное в притяжательном падеже, количественное числительное или отрицание (no).'
                             '\n\n Упоминая предмет впервые, мы употребляем перед ним неопределенный артикль а(an). Упоминая этот же предмет вторично, мы ставим перед ним определенный артикль the.'
                             '\n• E.g. This is a book. The book is interesting.'
                             '\n\nНеопределенный артикль a (an) может употребляться только с исчисляемыми существительными, стоящими в единственном числе.'
                             ' Перед неисчисляемыми существительными или существительными во множественном числе неопределенный артикль опускается.'
                             ' Определенный артикль the употребляется как с исчисляемыми, так и с неисчисляемыми существительными, как с единственным, так и с множественным числом.'
                             '\n• E.g. This is a book. The book is interesting.\nисчисляемое в единственном числе'
                             '\nThis is s meat. The meat is fresh.\nнеисчисляемое'
                             '\nThese are s books. The books are good.\nмножественное число'
                             '\n\nЧасто, даже упоминая предмет впервые, мы тем не менее употребляем перед ним определенный артикль:'
                             '\nа) если упоминаемый предмет является единственным в мире:'
                             '\n• E.g. The sun is shining brightly.'
                             '\nб) если этот предмет является определенным по ситуации:'
                             '\n• E.g. Put the book on the table',
                             reply_markup=MarkupTheory)
        if call.data == 'articlesTasks':
            bot.send_message(call.message.chat.id, 'Выберите задание на артикли:', reply_markup=MarkupTaskArticles)
        if call.data == 'TasksBack':
            bot.send_message(call.message.chat.id, 'Выберите тип заданий:', reply_markup=MarkupTask)

        if call.data == 'articlesTask1':
            bot.send_message(call.message.chat.id,
                             'Напишите вставленные артикли через пробел,если артикль не нужен поставьте -.\n\nThis is ... book. It is my ... book. I have ... sister. My ... sister is ... engineer. Give me ... chair, please. They have ... dog and two ... cats.'
                             'My ... family live in ... house. ... house is comfortable.')
            answer_needed1 = True
            answer_correct = 'a - a - an a a - - a the'
            @bot.message_handler()
            def callback_art1(message):
                nonlocal answer_needed1
                answer_needed1 = True
                if answer_needed1:
                    if message.text == answer_correct:
                        answer_needed1 = False
                        bot.send_message(call.message.chat.id,
                                         'Вы успешно справились с заданием! Выберите другое задание.',
                                         reply_markup=MarkupTaskArticles)
                    else:
                        bot.send_message(call.message.chat.id,
                                         'Ошибка, попробуйте еще раз! Пример ввода ответа: a the - an the - an')

        if call.data == 'articlesTask2':
            bot.send_message(call.message.chat.id,
                             'Напишите вставленные артикли через пробел,если артикль не нужен поставьте -.\n\nThis is ... pen. ... pen is red.  In the morning I eat ... sandwich and drink ... tea.'
                             ' She gave me ... coffee and ... cake. ... coffee was hot. ... cake was tasty. He never eats ... meat. He is ... vegetarian.')
            answer_needed2 = True
            answer_correct = 'a the a - - a the the - a'
            @bot.message_handler()
            def callback_art2(message):
                nonlocal answer_needed2, answer_correct
                answer_needed2 = True
                if answer_needed2:
                    if message.text == answer_correct:
                        answer_needed2 = False
                        bot.send_message(call.message.chat.id,
                                         'Вы успешно справились с заданием! Выберите другое задание.',
                                         reply_markup=MarkupTaskArticles)
                        return
                    else:
                        bot.send_message(call.message.chat.id,
                                         'Ошибка, попробуйте еще раз! Пример ввода ответа: a the - an the - an')

        if call.data == 'articlesTask3':
            bot.send_message(call.message.chat.id,
                             'Напишите вставленные артикли через пробел,если артикль не нужен поставьте -.'
                             "\n\n What's ... weather like today? — ... weather is fine. We had ... English lesson yesterday."
                             " ... teacher asked me many ... questions. ... questions were difficult. Our ... cat is sitting on ... sofa."
                             "Nick went into ... bathroom, turned on ... water and washed his ... hands.")
            answer_needed3 = True
            answer_correct = 'the the an the - the - the the the -'
            @bot.message_handler()
            def callback_art3(message):
                nonlocal answer_needed3, answer_correct
                answer_needed3 = True
                if answer_needed3:
                    if message.text == answer_correct:
                        answer_needed3 = False
                        bot.send_message(call.message.chat.id,
                                         'Вы успешно справились с заданием! Выберите другое задание.',
                                         reply_markup=MarkupTaskArticles)
                        return
                    else:
                        bot.send_message(call.message.chat.id,
                                         'Ошибка, попробуйте еще раз! Пример ввода ответа: a the - an the - an')


bot.polling(none_stop=True)
