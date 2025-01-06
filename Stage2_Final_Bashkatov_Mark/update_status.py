status = {
    1: 'В процессе',
    2: 'Выполнено',
    3: 'Отложено'
}
#  Используем цикл для вывода без скобок
print('Выберите статус вашей заметки:')
for key, value in status.items():
    print(f"{key}: {value}")

status_now = input('Выберите новый статус заметки (0 для завершения): ')
# Проверяем выбрал ли пользователь статус не "0" и не буквами
if status_now.isnumeric() == True and status_now != '0':
    status_now = int(status_now)
else:
    status_now = int(input('Выберите цифру из предложенных вариантов: '))
# Делаем "0" командой для завершения
while status_now != 0:
    status_presently = status.get(status_now)
    # Проверяем выбрал ли пользователь статус из предложенного
    if status.get(status_now) != None:
        print('Статус заметки обновлен: ', status.get(status_now))
        status_now = int(input('Выберите новый статус заметки (0 для завершения):'))
    else:
        print('Такого значения статуса нет')

print('Текущий статус заметки: ', status_presently)
