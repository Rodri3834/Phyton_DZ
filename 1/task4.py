# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти координатной плоскости (от 1 до 4): '))
if 0 < quarter < 5:
    print(f'\nДиапазон возможных координат точек в {quarter} четверти')
    if quarter == 1:
        print('по оси OX: от 0 до +∞')
        print('по оси OY: от 0 до +∞')
    elif quarter == 2:
        print('по оси OX: от -∞ до 0')
        print('по оси OY: от 0 до +∞')
    elif quarter == 3:
        print('по оси OX: от -∞ до 0')
        print('по оси OY: от -∞ до 0')
    else:
        print('по оси OX: от 0 до +∞')
        print('по оси OY: от -∞ до 0')
else:
    print('\n!!! Введен неверный номер четверти')