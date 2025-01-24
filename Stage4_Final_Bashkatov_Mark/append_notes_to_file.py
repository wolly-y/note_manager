from datetime import datetime

def append_notes_to_file(notes, filename):
    print('===== Создание заметки в файл filename.txt: =====')
    while True:
        username = input('Введите имя заметки: ').strip()
        while not username:
            username = input('Введите имя заметки: ').strip()

        title = input('Введите заголовок заметки: ').strip()
        while not title:
            title = input('Введите заголовок заметки: ').strip()

        content = input('Введите описание заметки: ').strip()
        while not content:
            content = input('Введите описание заметки: ').strip()

        status = input('Введите статус заметки, например "новая", "в процессе": ').strip()
        while not status:
            status = input('Введите статус заметки, например "новая", "в процессе": ').strip()

        issue_date = input('Введите дедлайн заметки в формате дд.мм.гггг: ').strip()
        while True:
            try:
                datetime.strptime(issue_date, '%d.%m.%Y')
                break
            except ValueError:
                print('Дата введена некорректно')
                issue_date = input('Введите дату дедлайна (в формате дд.мм.гггг): ').strip()

        notes.append({
            'Имя пользователя': username,
            'Заголовок заметки': title,
            'Описание заметки': content,
            'Статус заметки': status,
            'Дата создания': datetime.now().strftime("%d.%m.%Y"),
            'Дата дедлайна': issue_date,
        })
        choice_ = input('Хочешь создать еще заметку (да\нет): ').strip()
        while choice_.lower() != 'да' and choice_.lower() != 'нет':
            choice_ = input('Хочешь создать еще заметку (да\нет): ').strip()
        if choice_.lower() == 'нет':
            break
        if choice_.lower() == 'да':
            continue

    for index, note in enumerate(notes, start=1):
        for key, value in note.items():
            filename.write(f'{key}: {value}\n')
        filename.write('_____________________\n')

    filename.close()
    return notes

if __name__ == '__main__':
    notes = []
    try:
        filename = open('filename.txt', 'a', encoding='utf-8')
    except FileNotFoundError:
        filename = open('filename.txt', 'x', encoding='utf-8')
        filename = open('filename.txt', 'a', encoding='utf-8')
    except IOError:
        print('Ошибка при чтении файла filename, проверьте его содержимое')
    except UnicodeDecodeError:
        print('Не удалось декодировать файл')
    except PermissionError:
        print('Ошибка доступа, это системный файл')
    except Exception as e:
        print(f'Произошла ошибка: {e}')
    append_notes_to_file(notes, filename)