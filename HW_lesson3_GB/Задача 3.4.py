# Задача № 4: Программа принимает действительное положительное число x и целое отрицательное число y.
#             Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
#             При решении задания нужно обойтись без встроенной функции возведения числа в степень.
#             Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора.
#                        Второй — более сложная реализация без оператора, предусматривающая использование цикла.
# Решение:

def degree_2(a, b):
    # из математики: число с отрицательным показателем степени равно дроби, числителем которой является единица,
    #                а знаменателем данное число
    # т.е. 2 в степени -3 = 1 / 2
    num = 1 / x
    # счетчик степеней (указано 1 т.к. само число это уже число в степени 1)
    count = 1

    # функция abs возвращает модуль числа т.е. abs(-7) --> 7
    # пока счетчик степеней меньше, чем модуль степени, то выполняем:
    while (count < abs(b)):
        # т.е. дробь умножается на саму себя (это и есть возведение в степень)
        # и это умножение происходи столько раз, сколько указано в степени (если степень -2, то итераций цикла будет 1)
        # еще раз: САМО ЧИСЛО это уже возведение в степень 1 т.е. поэтому итераций цикла одна, а степень -2
        num = num * (1 / a)

        # каждую итерацию цикла увеличиваем счетчик степеней на +1
        count += 1

    return num


def degree_1(a, b):
    return a ** b


x = 2
y = -4

# вызов функции для первого способа
d_1 = degree_1(x, y)
# вызов функции для второго способа
d_2 = degree_2(x, y)

print(f'Первый способ: ')
print(f'Основание степени {x} в показатели степени {y} = {d_1}')
print()
print(f'Второй способ: ')
print(f'Основание степени {x} в показатели степени {y} = {d_2}')
