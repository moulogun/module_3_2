def send_email(message, recipient, sender = "university.help@gmail.com"):
    total = 0
    while total < 1:
        # Проверка на идентичность отправителя и получателя
        if sender == recipient:
            (print('Нельзя отправить письмо самому себе!'))
            total = total + 1
        # Проверка получателя на соответствие
        else:
            for i in range(len(sender)):
                if sender[i] == '@':
                    dot = True
                    break
                else:
                    dot = False
                    continue
            if sender[-4:] == '.com' or sender[-3:] == '.ru' or sender[-4:] == '.net':
                result = True
            else:
                result = False
            if dot == False or result == False:
                print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
                total = total + 1
                break
            # Проверка отправителя на соответсиве
            for i in range(len(recipient)):
                if recipient[i] == '@':
                    dot_recipient = True
                    break
                else:
                    dot_recipient = False
                    continue
            if recipient[-4:] == '.com' or recipient[-3:] == '.ru' or recipient[-4:] == '.net':
                result_recipient = True
            else:
                result_recipient = False
            if dot_recipient == False or result_recipient == False:
                print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
                total = total + 1
                break
            # Проверка на стандартность отправителя
            if sender == 'university.help@gmail.com':
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
                break
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
                break



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')