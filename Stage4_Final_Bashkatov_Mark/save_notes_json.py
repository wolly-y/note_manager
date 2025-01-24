import json
from datetime import datetime

def save_notes_json(notes, filename):
    json.dump(notes, filename, indent=4, ensure_ascii=False)
    filename.close()

if __name__ == '__main__':
    try:
        with open('filename.json', 'w', encoding='utf-8') as filename:
            notes = {'username': 'Алексей',
                 'title': 'Список покупок',
                 'content': 'Купить продукты',
                 'status': 'новая',
                 'created_date': datetime.now().strftime('%d.%m.%Y'),
                 'issue_date': '20.01.2026'}
            save_notes_json(notes, filename)
    except Exception as error:
        print(f'Произошла ошибка: {error}')