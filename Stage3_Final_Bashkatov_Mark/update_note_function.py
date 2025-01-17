from datetime import datetime
current_date = datetime.now()

note = [{'username': 1,
        'title': 2,
        'content': 3,
        'status': 4,
        'created_date': current_date.strftime('%d.%m.%Y'),
        'issue_date': '05.01.2025'}]
print('Текущие данные заметки:\n', note)

def update_note():
    choice_ = input('Какие данные вы хотите обновить? (username, title, content, status,'\
    'issue_date, пустое для завершения): ')

    while choice_ != '':

        if choice_ == 'username':
            note[0]['username'] = input('Введите имя пользователя: ')

        if choice_ == 'title':
            note[0]['title'] = input('Введите заголовок заметки: ')

        if choice_ == 'content':
            note[0]['content'] = input('Введите описание заметки: ')

        if choice_ == 'status':
            note[0]['status'] = input('Введите статус заметки: ')

        if choice_ == 'issue_date':
            note[0]['issue_date'] = input('Введите дату дедлайна (в формате дд.мм.гггг): ')

            if note[0]['issue_date'] != '%d.%m.%Y':
                print('Дата введена некорректно')
                note[0]['issue_date'] = input('Введите дату дедлайна (в формате дд.мм.гггг): ')

        choice_ = input('Какие данные вы хотите обновить? (username, title, content, status,'\
            'issue_date, пустое для завершения): ')

    print('Заметка обновлена:\n', note)

update_note()
