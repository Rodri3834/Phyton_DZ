# 3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# 
# *Пример:*
# 
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# 

data = '1.1 1.2 3.1 5 10.01'.split()
data = list(map(float, data))
fractional_values = [round((data[i] - int(data[i])), 5) for i in range(0, len(data))]
min = fractional_values[0]
max = fractional_values[0]
for i in range(1, len(fractional_values)):
    if max < fractional_values[i]:
        max = fractional_values[i]
    if min > fractional_values[i] and fractional_values[i] != 0.0:
        min = fractional_values[i]
print('Для списка - ', data, '\nРазница между максимальным и минимальным значением дробной части элементов - ', max - min)