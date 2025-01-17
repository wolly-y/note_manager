from datetime import datetime
current_date = datetime.now()
note = []

def created_note():
    note.append({
        'username': input('Введите имя пользователя: '),
        'title': input('Введите заголовок заметки: '),
        'content': input('Введите описание заметки: '),
        'status': input('Введите статус заметки (например, "новая", "в процессе", "выполнена"): '),
        'created_date': current_date.strftime('%d.%m.%Y'),
        'issue_date': input('Введите дату дедлайна (в формате дд.мм.гггг): ')
    })

    if note[0]['username'] == '':
        print('Имя пользователя не может быть пустым')
        note[0]['username'] = input('Введите имя пользователя: ')

    if note[0]['title'] == '':
        print('Заголовок не может быть пустым')
        note[0]['title'] = input('Введите заголовок заметки: ')

    if note[0]['status'] == '':
        print('Статус не может быть пустым')
        note[0]['status'] = input('Введите статус заметки: ')

    if note[0]['issue_date'] != '%d.%m.%Y':
        print('Дата введена некорректно')
        note[0]['issue_date'] = input('Введите дату дедлайна (в формате дд.мм.гггг): ')

    print('Заметка создана: ', note)

created_note()
