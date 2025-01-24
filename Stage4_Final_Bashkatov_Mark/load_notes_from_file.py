def load_notes_from_file(filename):
    notes = []
    note = {}
    filename = filename.split('\n')
    for lines in filename:
        if 'Имя пользователя' in lines:
            line = lines.split(':',1)
            note['username'] = ''.join(line[1:]).strip()
        if 'Заголовок заметки' in lines:
            line = lines.split(':',1)
            note['title'] = ''.join(line[1:]).strip()
        if 'Описание заметки' in lines:
            line = lines.split(':',1)
            note['content'] = ''.join(line[1:]).strip()
        if 'Статус заметки' in lines:
            line = lines.split(':',1)
            note['status'] = ''.join(line[1:]).strip()
        if 'Дата создания' in lines:
            line = lines.split(':',1)
            note['created_date'] = ''.join(line[1:]).strip()
        if 'Дата дедлайна' in lines:
            line = lines.split(':',1)
            note['issue_date'] = ''.join(line[1:]).strip()
            notes.append(note)
            note = {}

    print(notes)
    return notes

if __name__ == '__main__':
    try:
        filename = open('filename.txt', encoding='utf-8')
        content = filename.read()
        if not content :
            print('Файл пуст.')
            filename.close()
            exit()
    except FileNotFoundError:
        print('Нет файла.')
        exit()
    except IOError:
        print('Ошибка при чтении файла filename, проверьте его содержимое')
    except UnicodeDecodeError:
        print('Не удалось декодировать файл')
    except PermissionError:
        print('Ошибка доступа, это системный файл')
    except Exception as e:
        print(f'Произошла ошибка: {e}')
    filename = content
    load_notes_from_file(filename)