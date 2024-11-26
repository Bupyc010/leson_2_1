def send_email(message, recipient, sender = "university.help@gmail.com"):
    if (sender[sender.find('@')] == '@' and (sender.endswith('.com') == True or sender.endswith('.ru') == True or sender.endswith('.net') == True)) and (recipient[recipient.find('@')] == '@' and (recipient.endswith('.com') == True or recipient.endswith('.ru') == True or recipient.endswith('.net') == True)):
        if sender == "university.help@gmail.com":
            print(f'Письмо успешно отправлено с адреса {sender} на {recipient}')
        elif recipient == sender:
            print(f'Нельзя отправить письмо самому себе!')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на {recipient}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')