def send_email (message, recipient, *, sender = "university.help@gmail.com"):
    if '@' not in recipient or '@' not in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return False

    for member_chat in [sender, recipient]:
        send = False
        for end_adress in [".com", ".ru", ".net"]:
            if end_adress in member_chat:
                send = True
                continue
        if send == False:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            return False

    if sender == recipient:
        print('Нельзя отправлять письмо самому себе!')
        return False

    if sender == "university.help@gmail.com":
        print(f'Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')