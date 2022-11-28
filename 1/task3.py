# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

num_x = float(input('Введите координату точки по оси OX: '))
num_y = float(input('Введите координату точки по оси OY: '))
if num_x == 0 or num_y == 0:
    print(f'\nТочка с координатами ({num_x};{num_y})', end=' ')
    if num_x == 0 and num_y != 0:
        print('находится на оси OY')
    elif num_y == 0 and num_x != 0:
        print('находится на оси OX')
    else:
        print('является началом координат')
else:
    if num_x > 0 and num_y > 0:
        quarter = 1
    elif num_x < 0 and num_y > 0:
        quarter = 2
    elif num_x < 0 and num_y < 0:
        quarter = 3
    else:
        quarter = 4
    print(f'\nТочка с координатами ({num_x};{num_y}) находится в {quarter} четверти')