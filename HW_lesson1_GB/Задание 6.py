# Задание № 6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
#              Это отношение прибыли к выручке.
#              Далее запросите численность сотрудников фирмы.
#              Определите прибыль фирмы в расчета на одного сотрудника.

profit = 0  # прибыль
profitability = 0  # рентабельность выручки
number_employees = 0  # кол-во сотрудников
profit_employee = 0  # прибыль на одного сотрудника

# выручка
revenue = input('Введите, пожалуйста, выручку компании: ')
revenue = int(revenue)

# издержки
costs = input('Введите, пожалуйста, издержки компании: ')
costs = int(costs)

# если выручка больше издержки
if (revenue > costs):
    # находим прибыль
    profit = revenue - costs
    print()
    print(f'Прибыль Вашей компании составляет: {profit}')

    # находим рентабельность выручки по формуле: прибыль / выручка * 100 = (значение в процентах)
    profitability = profit / revenue * 100
    # :.1f - указатель количество цифр после запятой т.е. в данном случаи 1 цифра
    print(f'Рентабельность выручки Вашей компании составляет: {profitability:.1f} %')

    print()

    number_employees = input('Введите количество сотрудников: ')
    number_employees = int(number_employees)

    # прибыль на одного сотрудника находится по формуле: прибыль / кол-во сотрудников
    profit_employee = profit / number_employees
    print(f'Прибыль на одного сотрудника составляет: {profit_employee:.1f}')

# если издержки больше выручки
else:
    print(f'Финансовый результат Вашей фирмы: убыток')
