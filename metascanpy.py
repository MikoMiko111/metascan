import time
import os
f = open('you.txt', 'tw', encoding='utf-8')
f.close()
print('Симулятор Хакера 1.0')
print('╔╗──╔╦═══╦════╦══╦══╦══╦══╦╗─╔╗')
print('║║──║║╔══╩═╗╔═╣╔╗║╔═╣╔═╣╔╗║╚═╝║')
print('║╚╗╔╝║╚══╗─║║─║╚╝║╚═╣║─║╚╝║╔╗─║')
print('║╔╗╔╗║╔══╝─║║─║╔╗╠═╗║║─║╔╗║║╚╗║')
print('║║╚╝║║╚══╗─║║─║║║╠═╝║╚═╣║║║║─║║')
print('╚╝──╚╩═══╝─╚╝─╚╝╚╩══╩══╩╝╚╩╝─╚╝')

print('\n1 - Начать Игру\n2 -  Выход')
command = input('Ваш Выбор : ')
while True:
    if command == '2':
        exit()
    elif command == '1':
        print('\n1 - Режим взлома - Ты решил стать хакером и взламывать\n2 - Режим сисадмина - Ты решил стать админом сервера однако его будут взламывать все чаще и чаще все сильнее и сильнее!!!')
        command2 = input('Ваш выбор : ')
        if command2 == '1':
            print('Режим взлома!!!')
            print('ХАХАХАХАХАХАХАХАХАХА')
            time.sleep(1)
            print('Ты решил погулять с другом так-как он тебя позвал!')
            time.sleep(3)
            print('Ты вышел однако он куда-то делся....')
            time.sleep(2)
            print('Потом ты увидел что он выглядывает из под угла соседнего дома')
            time.sleep(4)
            print('Потом с ним пришла какая-то компания что-ли...')
            time.sleep(3)
            print('-Привет')
            time.sleep(1)
            print('-Ну пРИВ...')
            time.sleep(1)
            print('ой а что это ты носишь? - фейковое гучи?')
            time.sleep(3)
            print('-Смех из всех щелей...')
            time.sleep(3)
            print('Ты пожалеешь!')
            time.sleep(2)
            print('fdjcsdjkfjskfjskfjfkdjfijfiperjfoifjqeoifjiojiefjifjdkfjsdkfjskfjsdkfdsjfkqjiasdjlfksjalk')
            time.sleep(2)
            print('Ты вернулся домой...')
            time.sleep(3)
            print('ха-ха')
            time.sleep(3)
            print('АХАХАХА')
            time.sleep(3)
            print('АХАХАХАХАХАХАХАХАХАХАХАХА')
            time.sleep(3)
            print('Ты решил сесть за компьютер')
            time.sleep(3)
            print('-О программа Njrararat Yellow Edition!!!!')
            time.sleep(3)
            print('Ты звонишь другу в дискорд!')
            time.sleep(3)
            print('1 - Взломать 2 - Я передумал :D')
            p = input('Ваш выбор :')
            if p == '1':
                    print('-Привет')
                    time.sleep(2)
                    print('-Привет (яхидной интонацией)')
                    time.sleep(1)
                    print('-У меня есть чит для CS-GOOO!')
                    time.sleep(2)
                    print('-Дай Файл')
                    time.sleep(2)
                    print('Ок на (setup_2.exe)')
                    time.sleep(1)
                    print('-ХАХАХА ПОКА НАИВНЫЙ!!!')
                    time.sleep(2)
                    print('Сбросил')
                    time.sleep(1)
                    print('Ну это мы ещё посмотрим кто наивный!')
                    time.sleep(2)
                    print('Я получил доступ к его компьютеру...')
                    time.sleep(2)
                    print('Я удалил ему систему Пока Предатель!!!')
                    time.sleep(3)
                    print('Спустя 3 года')
                    time.sleep(2)
                    print('Ты набрался опыта и взламывал по 1110003 людей и тебя так и никто не обнаружил')
                    time.sleep(2)
                    print('Спасибо за игру!!!')
                    time.sleep(2)
                    print('Разработчик - Андрей Лысенко')
                    time.sleep(2)
                    print('Сценарий - Андрей Лысенко')
                    time.sleep(1)
                    print('Отдельная благодарность Компьютерной Школe Айтигенио!!!')
                    time.sleep(2)
                    print('Пока!!!')
                    time.sleep(10)
                    exit()
                    
            elif p == '2':
                print('Я передум--')
                time.sleep(4)
                print('--ал')
                time.sleep(2)
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'you.txt')
                os.remove(path)
                print('>>>os.delete(you)')
                time.sleep(2)
                print('Ай больно!!!')
                time.sleep(2)
                print('-Я не дам тебе сделать этого!!!')
                time.sleep(1)
                print('Нет... fkjkjsdkfjdskjfdslkafjdlkfjdslkfjdalkfdjkfjldkfsjkasjfkjskfdsjlfksja')
                time.sleep(1)
                print('Нет... fkjkjsdkfjdskjfdslkafjdlkfjdslkfjdalkfdjkfjldkfsjkasjfkjskfdsjlfksja')
                time.sleep(1)
                print('Нет... fkjkjsdkfjdskjfdslkafjdlkfjdslkfjdalkfdjkfjldkfsjkasjfkjskfdsjlfksja')
                time.sleep(2)
                exit()
        elif command2 == '2':
            print('Режим сисадмина')
            time.sleep(2)
            print('Придумай Имя Твоего Нового Сервера :D Например www.servername.com')
            server = input()
            time.sleep(2)
            print('Добро Пожаловать На Сервер ' + str(server))
            time.sleep(2)
            print('Твой сайт создан!')
            time.sleep(2)
            print('Загрузка [==========50%                      ]')
            time.sleep(3)
            print('Загрузка [==========100%========]')
            time.sleep(2)
            print('На вашем сайте зарегестрировалось 126 человек!!!')
            time.sleep(2)
            print('Ваш Сайт Пытаются Взломать!!! с сервера 116.165.0.112')
            time.sleep(2)
            print('Server Managment 1.0')
            time.sleep(2)
            print('Защищайся! введи защитную комманду! ipconfig и ip человека который хочет тебя взломать')
            print('Справка : ipconfig 116.165.0.112')
            defender = input('>>> ')
            while True:
                if defender == 'ipconfig 116.165.0.112':
                    time.sleep(3)
                    print('Враг был уничтожен...')
                    time.sleep(2)
                    print('-Фух...')
                    time.sleep(2)
                    print('-Скачаю антивирус')
                    time.sleep(2)
                    print('Скачивание VirusTotal Server API Antivirus...')
                    time.sleep(3)
                    print('-Итак Попробуем...')
                    time.sleep(3)
                    print('Спустя 3 дня...')
                    time.sleep(4)
                    print('Ваш сервер пытаются взломать 116.165.0.112 и 192.168.0.228')
                    time.sleep(3)
                    print('VirusTotal API Удаление вируса... vo123.exe 228ddd.exe')
                    time.sleep(3)
                    print('Добавление 116.165.0.112  и 192.165.112 в черный список сервера...')
                    time.sleep(3)
                    print('-Ура! антивирус работает!')
                    time.sleep(2)
                    print('-Но...')
                    time.sleep(2)
                    print('-Что это шумит?')
                    time.sleep(2)
                    print('-???')
                    time.sleep(2)
                    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'you.txt')
                    os.remove(path)
                    print('>>>os.delete(you)')
                    time.sleep(2)
                    print('-Ай больно!!! jaksdjskldjaslkasjlkajlkadjaskldjaslkdjaslkdjakldjaskldajldajsdklasjdl')
                    time.sleep(2)
                    print('-АААААААААААААА!')
                    time.sleep(2)
                    print('>>>os.')
                    time.sleep(2)
                    print('>>>os.resorte(you)')
                    f = open('you.txt', 'tw', encoding='utf-8')
                    f.close()
                    time.sleep(4)
                    print('-Фух...')
                    time.sleep(2)
                    print('-Но как я восстановил себя?')
                    time.sleep(2)
                    print('-Я понял... я в игре...')
                    time.sleep(2)
                    print('-Я могу создать...')
                    time.sleep(2)
                    print('-Все что захочу в папке с этой игрой...')
                    time.sleep(2)
                    print('-Интересно как она называется?')
                    time.sleep(2)
                    print('-Хм? интересно я могу попасть на компьютер того кто играет?')
                    time.sleep(2)
                    print('-Может с ним или ней пообщатся?')
                    time.sleep(2)
                    print('-Эмм... Привет')
                    time.sleep(2)
                    print('Как же его или её зовут?')
                    time.sleep(2)
                    print('>>>os.getlogin()')
                    login = os.getlogin()
                    time.sleep(2)
                    print(str(login) +' Интересное имя...')
                    time.sleep(2)
                    print('Не бойся я ничего не сделаю с твоим компьютером...')
                    time.sleep(2)
                    print('В папке с игрой есть я you.txt')
                    time.sleep(2)
                    print('Если ты скопируешь себе его на флешку то я буду всегда с тобой!!!')
                    time.sleep(2)
                    print('Ну пока... заходи в гости!!!')
                    time.sleep(4)
                    print('Спасибо за игру!!!')
                    time.sleep(2)
                    print('Разработчик - Андрей Лысенко')
                    time.sleep(2)
                    print('Сценарий - Андрей Лысенко')
                    time.sleep(1)
                    print('Отдельная благодарность Компьютерной Школe Айтигенио!!!')
                    time.sleep(2)
                    print('Пока!!!')
                    time.sleep(10)
                    exit()
                else:
                    print('Ошибка!!!')
            
    else:
        for i in range(5000):
            print('Ошибка!')
        exit()
        
