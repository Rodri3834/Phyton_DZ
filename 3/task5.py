# 5'. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)
# 
# *Пример:*
# 
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
# 
n = int(input())
f1 = 0
f2 = 1
nlist = [0, 1]
list = [0, 1]
for i in range(2, n + 1):
    f1, f2 = f2, f1 + f2
    list.append(f2)
for i in range(2, n + 1):
    nlist.append(((-1) ** (i + 1)) * list[i])
nlist.reverse()
for i in range(1, n + 1):
    nlist.append(list[i])
print(nlist)