def display_notes(notes):
    # Если список заметок пустой, выводим сообщение
    if not notes:
        print("У вас нет сохранённых заметок.")
        return

    # Перебираем список заметок и выводим каждую
    for index, note in enumerate(notes, start=1):
        print(f"Заметка №{index}:")
        print(f"Имя пользователя: {note.get('username', 'Не указано')}")
        print(f"Заголовок: {note.get('title', 'Не указан')}")
        print(f"Описание: {note.get('content', 'Не указано')}")
        print(f"Статус: {note.get('status', 'Не указан')}")
        print(f"Дата создания: {note.get('create_date', 'Не указана')}")
        print(f"Дедлайн: {note.get('issue_date', 'Не указан')}")
        print("------------------------------")

notes = [
    {
        'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'create_date': '27.11.2024',
        'issue_date': '30.11.2025'
    },
    {
        'user_name': 'Марина',
        'title': 'Важная встреча',
        'content': 'Подготовить материалы для встречи',
        'status': 'в процессе',
        'create_date': '01.12.2024',
        'issue_date': '05.01.202'
    }
]

display_notes(notes)
