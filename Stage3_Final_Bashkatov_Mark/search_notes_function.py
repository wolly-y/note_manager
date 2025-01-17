def search_notes(notes, keyword=None, status=None):
    if not notes:
        print("Список заметок пуст.")
        return
    filtered_notes = []

    for note in notes:
        # Поиск по ключевому слову
        if keyword and not (keyword.lower() in note['title'].lower() or
                            keyword.lower() in note['content'].lower() or
                            keyword.lower() in note['username'].lower()):
            continue  # Пропускаем заметку, если ключевое слово не найдено

        # Поиск по статусу
        if status and note['status'].lower() != status.lower():
            continue  # Пропускаем заметку, если статус не совпадает

        # Если прошли оба фильтра, добавляем заметку в результат
        filtered_notes.append(note)

    # Выводим результаты поиска
    if filtered_notes:
        print("Найдены заметки:\n")
        for index, note in enumerate(filtered_notes, start=1):
            print(f"Заметка №{index}:")
            print(f"Имя пользователя: {note['username']}")
            print(f"Заголовок: {note['title']}")
            print(f"Описание: {note['content']}")
            print(f"Статус: {note['status']}")
            print("------------------------------")
    else:
        print("Заметки, соответствующие запросу, не найдены.")

notes = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
    'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
    'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
    'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
    ]

search_notes(notes, keyword = 'покупок')
search_notes(notes, status = 'в процессе')
search_notes(notes, keyword = 'работы', status='выполнено')
search_notes(notes, status = 'python')
