from datetime import datetime

notes = []

def create_note(notes):
    print('Создание заметки: ')
    note = {'username': input('Введите ваше имя: ').strip(),
                  'title': input('Введите заголовок заметки: ').strip(),
                  'content': input('Введите описание заметки: ').strip(),
                  'status': input('Введите статус заметки (например "новая", "в процессе", "выполнена"): ').strip(),
                  'created_date': datetime.now().strftime('%d.%m.%Y').strip(),
                  'issue_date': input('Введите дедлайн заметки в формате дд.мм.гггг: ').strip(),
    }

    while note['username'] == '':
        print('Имя пользователя не может быть пустым')
        note['username'] = input('Введите имя пользователя: ').strip()

    while note['title'] == '':
        print('Заголовок не может быть пустым')
        note['title'] = input('Введите заголовок заметки: ').strip()

    while note['status'] == '':
        print('Статус не может быть пустым')
        note['status'] = input('Введите статус заметки: ').strip()

    while note['content'] == '':
        print('Описание не может быть пустым')
        note['status'] = input('Введите описание заметки: ').strip()

    while True:
        try:
            datetime.strptime(note['issue_date'], '%d.%m.%Y')
            break
        except ValueError:
            print('Дата введена некорректно')
            note['issue_date'] = input('Введите дату дедлайна (в формате дд.мм.гггг): ').strip()

    notes.append(note)
    print('Заметка создана: ', note)
    print('----------------')
    return notes

def display_notes():
    print(' ')
    if not notes:
        print('Заметок нет.')
        return
    print('Ваши заметки:')
    for index, note in enumerate(notes, start=1):
        print(f"Заметка №{index}:")
        print(f"Имя пользователя: {note.get('username', 'не указано')}")
        print(f"Заголовок: {note.get('title')}")
        print(f"Описание: {note.get('content')}")
        print(f"Статус: {note.get('status')}")
        print(f"Дата создания: {note.get('created_date')}")
        print(f"Дедлайн: {note.get('issue_date')}")
        print("------------------------------")

def update_note(notes):
    if notes == []:
        print('Заметок нет')
        return notes

    print('Изменение заметки:')
    up_note = int(input('Введите номер заметки ').strip()) - 1
    print(notes[up_note])
    print('''
    Параметры заметки:
    1. Имя пользователя
    2. Заголовок заметки
    3. Описание заметки
    4. Статус заметки
    5. Дата дедлайна
    ''')
    changes_note = int(input('Введите параметр который хотите изменить (от 1 до 5): ').strip())
    if 1 > changes_note or changes_note > 5:
        changes_note = int(input('Введите параметр от 1 до 5: ').strip())
    if changes_note == 1:
        new_value = input('Введите новое имя пользователя: ').strip()
        while new_value == '':
            new_value = input('Имя пользователя не может быть пустым: ').strip()
        notes[up_note]['username'] = new_value
    if changes_note == 2:
        new_value = input('Введите новый заголовок заметки: ').strip()
        while new_value == '':
            new_value = input('Заголовок не может быть пустым: ').strip()
        notes[up_note]['title'] = new_value
    if changes_note == 3:
        new_value = input('Введите новое описание заметки: ').strip()
        while new_value == '':
            new_value = input('Описание не может быть пустым: ').strip()
        notes[up_note]['content'] = new_value
    if changes_note == 4:
        new_value = input('Введите новый статус заметки: ').strip()
        while new_value == '':
            new_value = input('Статус не может быть пустым: ').strip()
        notes[up_note]['status'] = new_value
    if changes_note == 5:
        new_value = input('Введите новую дату дедлайна в формате дд.мм.гггг: ').strip()
        while True:
            try:
                datetime.strptime(note['issue_date'], '%d.%m.%Y')
                break
            except ValueError:
                print('Дата введена некорректно')
                new_value = input('Введите дату дедлайна (в формате дд.мм.гггг): ').strip()
        notes[up_note]['issue_date'] = new_value

def delete_note(notes):
    if notes == []:
        print('Заметок нет')
        return
    print('Удаление заметок: ')

    print('''
    Удаление заметки по:
    1.Номеру заметки
    2.Имени
    3.Заголовку заметки
    ''')
    parametr = input('Введите параметр для удаление заметки: ').strip()
    if parametr != '1' and parametr != '2' and parametr != '3':
        parametr = input('Введите цифру от 1 до 3: ').strip()

    if parametr == '1':
        try:
            number_note = int(input('Введите номер заметки: ').strip()) - 1
            if number_note < 0 or number_note >= len(notes):
                print('Нет такой заметки.')
            else:
                notes.pop(number_note)
                print('Заметка удалена.')

        except ValueError:
            print('Введите корректный номер заметки.')

    if parametr == '2':
        name_note = input('Введите имя заметки: ').strip()
        if name_note == '':
            print('\nИмя заметки не может быть пустым!')
            name_note = input('\nВведите имя заметки: ').strip()

        note = []
        for x in range(len(notes) -1, -1, -1):
            n = notes[x]
            if name_note.lower() == n['username'].lower():
                a = notes.pop(x)
                note.append(a)
                print('Заметка удалена.')
        if note == []:
            print('Заметок не найдено.')

    if parametr == '3':
        title_note = input('Введите загловок заметки: ').strip()
        if title_note == '':
            print('\nЗаголовок заметки не может быть пустым!')
            title_note = input('\nВведите заголовок заметки: ').strip()

        note = []
        for x in range(len(notes) - 1, -1, -1):
            n = notes[x]
            if title_note.lower() == n['title'].lower():
                a = notes.pop(x)
                note.append(a)
                print('Заметка удалена.')
        if note == []:
            print('Заметок не найдено.')

    return notes

def search_notes():
    if notes == []:
        print('Заметок нет')
        return

    print('Поиск заметок: ')
    print('''
        Поиск заметок по:
        1.Имени
        2.Заголовку заметки
        3.Описанию
        ''')
    parametr = input('Введите параметр для поиска заметки: ').strip()
    if parametr != '1' and parametr != '2' and parametr != '3':
        parametr = input('Введите цифру от 1 до 3: ').strip()

    if parametr == '1':
        name_note = input('Введите имя заметки: ').strip()
        if name_note == '':
            print('\nИмя заметки не может быть пустым!')
            name_note = input('\nВведите имя заметки: ').strip()

        note = []
        for x in range(len(notes) - 1, -1, -1):
            n = notes[x]
            if name_note.lower() == n['username'].lower():
                note.append(n)
        if note == []:
            print('Заметок не найдено.')
        else:
            print('Найдены заметки:\n')
            for index, note_ in enumerate(note, start=1):
                print(f'Заметка №{index}:')
                print(f'Имя пользователя: {note_['username']}')
                print(f'Заголовок: {note_['title']}')
                print(f'Описание: {note_['content']}')
                print(f'Статус: {note_['status']}')
                print('------------------------------')

    if parametr == '2':
        title_note = input('Введите заголовок заметки: ').strip()
        if title_note == '':
            print('\nЗаголовок заметки не может быть пустым!')
            title_note = input('\nВведите заголовок заметки: ').strip()

        note = []
        for x in range(len(notes) - 1, -1, -1):
            n = notes[x]
            if title_note.lower() == n['title'].lower():
                note.append(n)
        if note == []:
            print('Заметок не найдено.')
        else:
            print('Найдены заметки:\n')
            for index, note_ in enumerate(note, start=1):
                print(f'Заметка №{index}:')
                print(f'Имя пользователя: {note_['username']}')
                print(f'Заголовок: {note_['title']}')
                print(f'Описание: {note_['content']}')
                print(f'Статус: {note_['status']}')
                print('------------------------------')

    if parametr == '3':
        content_note = input('Введите описание заметки: ').strip()
        if content_note == '':
            print('\nОписание заметки не может быть пустым!')
            content_note = input('\nВведите описание заметки: ').strip()

        note = []
        for x in range(len(notes) - 1, -1, -1):
            n = notes[x]
            if content_note.lower() == n['content'].lower():
                note.append(n)
        if note == []:
            print('Заметок не найдено.')
        else:
            print('Найдены заметки:\n')
            for index, note_ in enumerate(note, start=1):
                print(f'Заметка №{index}:')
                print(f'Имя пользователя: {note_['username']}')
                print(f'Заголовок: {note_['title']}')
                print(f'Описание: {note_['content']}')
                print(f'Статус: {note_['status']}')
                print('------------------------------')


print('''
        Меню действий:
        1. Создать новую заметку
        2. Показать все заметки
        3. Обновить заметку
        4. Удалить заметку
        5. Найти заметку
        6. Выйти из программы
''')
choice_ = input('Ваш выбор: ').strip()
print()
if choice_ != '1' and choice_ != '2' and choice_ != '3' and choice_ != '4' and choice_ != '5':
    choice_ = input('\nВведите значение от 1 до 5: ').strip()
while choice_ == '1' or choice_ == '2' or choice_ == '3' or choice_ == '4' or choice_ == '5' or choice_ == '6':
    if choice_ == '1':
        create_note(notes)
        print('''
        Меню действий:
        1. Создать новую заметку
        2. Показать все заметки
        3. Обновить заметку
        4. Удалить заметку
        5. Найти заметку
        6. Выйти из программы
        ''')
        choice_ = input('Ваш выбор: ').strip()
        continue

    if choice_ == '2':
        display_notes()
        print('''
        Меню действий:
        1. Создать новую заметку
        2. Показать все заметки
        3. Обновить заметку
        4. Удалить заметку
        5. Найти заметку
        6. Выйти из программы
        ''')
        choice_ = input('Ваш выбор: ').strip()
        continue

    if choice_ == '3':
        update_note(notes)
        print('''
        Меню действий:
        1. Создать новую заметку
        2. Показать все заметки
        3. Обновить заметку
        4. Удалить заметку
        5. Найти заметку
        6. Выйти из программы
        ''')
        choice_ = input('Ваш выбор: ').strip()
        continue

    if choice_ == '4':
        delete_note(notes)
        print('''
        Меню действий:
        1. Создать новую заметку
        2. Показать все заметки
        3. Обновить заметку
        4. Удалить заметку
        5. Найти заметку
        6. Выйти из программы
        ''')
        choice_ = input('Ваш выбор: ').strip()
        continue

    if choice_ == '5':
        search_notes()
        print('''
        Меню действий:
        1. Создать новую заметку
        2. Показать все заметки
        3. Обновить заметку
        4. Удалить заметку
        5. Найти заметку
        6. Выйти из программы
        ''')
        choice_ = input('Ваш выбор: ').strip()
        continue

    if choice_ == '6':
        break
print('Завершение программы.')