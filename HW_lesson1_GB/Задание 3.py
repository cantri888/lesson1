# Задание № 3: Узнайте у пользователя число n.
#              Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
#              Считаем 3 + 33 + 333 = 369.

n = []  # список в котором будут храниться числа
summa = 0  # сумма чисел

# запрос ввести данные, которые будут типа str (строка) даже если мы ввели число
user_number = input('Введите, пожалуйста, целое число: ')

# согласно формуле n * nn * nnn, всего будет 3 итерации (количество выполнений) цикла for
# в каждой итерации добавляем с помощью метода append строку умноженную на текущий i
# т.е. ввели '5': '5' * 1 = '5'; '5' * 2 = '55'; '5' * 3 = '555'
# тогда конечные данные в переменной n будут содержать ['5', '55', '555']
for i in range(1, 4):  # i примет значение указанных, в скобках функции range, границ (2-ое значение не включительно)
    n.append(user_number * i)

# с помощью цикла for идем, по-очереди, внутри списка n
# и складываем каждое значение (изменяя тип со строки на целое число) с переменной summa
for i in n:
    summa = summa + int(i)

# вывод на экран результата используя форматирование строк f
print(f'{user_number} + {user_number * 2} + {user_number * 3} = {summa}')
