# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


predicate_1 = [0, 0, 0, 0, 1, 1, 1, 1]
predicate_2 = [0, 0, 1, 1, 0, 0, 1, 1]
predicate_3 = [0, 1, 0, 1, 0, 1, 0, 1]

correct = 0
for i in range(8):
    part_left = not (predicate_1[i] or predicate_2[i] or predicate_3[i])
    print(f'¬({predicate_1[i]} ⋁ {predicate_2[i]} ⋁ {predicate_3[i]}) = {part_left}')
    part_right = not predicate_1[i] and not predicate_2[i] and not predicate_3[i]
    print(f'¬{predicate_1[i]} ⋀ ¬{predicate_2[i]} ⋀ ¬{predicate_3[i]} = {part_right}')
    print()
    if part_left == part_right:
        correct += 1
if correct == 8:
    print('Утверждение истинно при любых значениях предикат')
else:
    print('Что-то пошло не так(')