from datetime import datetime

# Выводим текущую дату
current_date = datetime.now()
print(f"Текущая дата: {current_date.strftime('%d-%m-%Y')}")

# Запрашиваем у пользователя дату дедлайна
while True:
    try:
        issue_date_str = input("Введите дату дедлайна (в формате день-месяц-год): ")
        # Преобразуем строку в объект datetime
        issue_date = datetime.strptime(issue_date_str, '%d-%m-%Y')
        break  # Если дата введена правильно, выходим из цикла
    except ValueError:
        # Если дата введена в неправильном формате, выводим ошибку
        print("Ошибка: Неверный формат даты. Пожалуйста, используйте формат день-месяц-год (например, 20-01-2025).")

# Рассчитываем разницу в днях между текущей датой и дедлайном
days_left = (issue_date - current_date).days

# Выводим, прошел ли дедлайн
if days_left < 0:
    print(f"Внимание! Дедлайн истёк {-days_left} дня(ей) назад.")
elif days_left == 0:
    print("Дедлайн сегодня!")
else:
    print(f"До дедлайна осталось {days_left} дня(ей).")