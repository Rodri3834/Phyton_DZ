# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

print('Введите ниже координаты точек A и B в координатной плоскости')

coord_x_a = float(input('\nВведите координату точки A по оси OX: '))
coord_y_a = float(input('Введите координату точки A по оси OY: '))
coord_x_b = float(input('Введите координату точки B по оси OX: '))
coord_y_b = float(input('Введите координату точки B по оси OY: '))

sum_squares = (coord_x_a - coord_x_b) ** 2 + (coord_y_a - coord_y_b) ** 2
result = sum_squares ** 0.5
print(f'\nРасстояние между точками A({coord_x_a};{coord_y_a}) '
      f'и B({coord_x_b};{coord_y_b}) = {round(result, 2)}')