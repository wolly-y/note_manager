note = [
    input('Введите ваше имя: '),
    [
        input('Введите заголовок заметки №1: '),
        input('Введите заголовок заметки №2: '),
        input('Введите заголовок заметки №3: '),
    ],
    input('Введите описание заметки: '),
    input('Введите статус заметки: '),
    input('Введите дату создания заметки в формате дд.мм.гггг: '),
    input('Введите дату истечения заметки в формате дд.мм.гггг: ')
]

print('Имя пользователя: ', note[0])
print('Заголовки заметок: ', note[1])
print('Описание заметки: ', note[2])
print('Статус заметки: ', note[3])
print('Дата создания заметки: ', note[4])
print('Дата истечения заметки: ', note[5])