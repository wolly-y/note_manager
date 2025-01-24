if __name__ == '__main__':
    try:
        with open('filename.txt', 'r', encoding ='utf-8') as filename:
            print(filename.read())
    except IOError:
        print('Ошибка при чтении файла filename, проверьте его содержимое')
    except FileNotFoundError:
        print('Файл filename не найден.')
        with open('filename.txt', 'w', encoding ='utf-8') as filename:
            print('Создан новый файл.')
    except UnicodeDecodeError:
        print('Не удалось декодировать файл')
    except PermissionError:
        print('Ошибка доступа, это системный файл')
    finally:
        print('Все ошибки обработаны, программа продолжает работу')