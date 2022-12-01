# 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n=4 [2, 2.25, 2.37, 2.44]
# Сумма 9.06

number = int(input('Введите число: '))
list = [round((1+1/number)**number, 2) for number in range(1, number+1)]
print(f'Последовательность: {list}')
print(f'Сумма: {round(sum(list), 2)}')