import random

sp = list(map(int, input('Введите список: ').split())) or [int(random.randint(0, 1000)) for _ in range(10)]
print(sp)

ind = int(input('Введите индекс элемента: '))
elem = int(input('Введите значение элемента: '))
new_sp = []
for i in range(len(sp)):
    if i == ind:
        new_sp.append(elem)
    else:
        new_sp.append(sp[i])

for i, val in enumerate(sp):
    print(f"lst[{i}] = {val}")
