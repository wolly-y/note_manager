notes = [
    {'1.Имя': 'Марк',
     'Заголовок': 'Курсы',
     'Описание': 'Git и Github'},
    {'1.Имя': 'Мария',
     'Заголовок': 'Уход',
     'Описание': 'В понедельник маникюр'},
    {'1.Имя': 'Саша',
     'Заголовок': 'Футбол',
     'Описание': 'Завтра хотели поиграть'}
]
# Выводим список
print("Список заметок:")
for dict_item in notes:
    for key, value in dict_item.items():
        print(f"{key}: {value}")
    print()

choice_ = input('Хотите удалить заметку? (да/нет): ')

while choice_.lower() == 'да':
    if choice_.lower() == 'да':
        # Запрашиваем у пользователя значение для удаления
        value_to_remove = input('Введите имя, заголовок или описание заметки, которую вы хотите удалить: ')
        value_to_remove = value_to_remove.capitalize()
        # Создаем новый список, в который добавляем только те заметки, которые не содержат введённое значение
        updated_notes = [note for note in notes if value_to_remove not in note.values()]
        # Проверяем, изменился ли список
        if len(updated_notes) == len(notes):
            print('Заметка с таким значением не найдена.')
        else:
            print('Заметка удалена.')
    choice_ = input('Хотите удалить ещё одну заметку? (да/нет): ')

# Обновляем список заметок
notes = updated_notes

print("Обновленный список заметок:")
for dict_item in notes:
    for key, value in dict_item.items():
        print(f"{key}: {value}")
    print()
