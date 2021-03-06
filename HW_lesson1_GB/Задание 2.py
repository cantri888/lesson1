# Задание № 2: Пользователь вводит время в секундах.
#              Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
#              Используйте форматирование строк.

count_seconds = int(input('Введите количество секунд: '))

h = (count_seconds // 3600)  # исходя из введенных секунд узнаем сколько в них часов
m = (count_seconds // 60) % 60  # сколько в них минут
s = count_seconds % 60  # сколько в них секунд (остаток в виде секунд)

# для правильного отображения в требуемом формате чч:мм:сс проверяем значение часов, минут и секунд
# если значения меньше 10, то преобразуем значения в строку,
# а перед этим добавляем строку '0' и соединяем их (конкатенация строки)
if h < 10:
    h = '0' + str(h)
else:
    h = str(h)

if m < 10:
    m = '0' + str(m)
# если больше 10, то просто преобразуем значения в строку
else:
    m = str(m)

if s < 10:
    s = '0' + str(s)
else:
    s = str(s)

# форматирование строки через f-строку:
# перед стракой указывается метка f; в самой строке, для вывода переменных используются круглые скобки {}
print(f'{h}:{m}:{s}')
