# Создается список для хранения заголовков
heading = []
heading_print = ''
heading.append(input('Введите заголовок (Стоп или оставьте пустым для завершения): '))

# Цикл продолжается, пока не введено "Стоп" или пустая строка
while heading[-1] != '' and heading[-1].lower() != 'стоп':
    heading.append(input('Введите заголовок (Стоп или оставьте пустым для завершения): '))
    # если название заголовков повторяется, то удаляем его
    if heading[-2] == heading[-1]:
        heading.pop()
        print('Заголовок повторяется')

# Удаляем последний элемент, если это пустая строка или "Стоп"
if heading[-1].lower() == 'стоп' or heading[-1] == '':
    heading.pop()

print('Ваши заметки: ')
# Выводим список заголовков без скобок
for item in heading:
    print(f'- {item}')
