import random

sp = list(map(int, input('Введите список: ').split())) or [int(random.randint(0, 1000)) for _ in range(10)]
print(sp)

ind = int(input('Введите индекс элемента: '))

del_elem = None
new_sp = []
for i in range(len(sp)):
    if i == ind:
        del_elem = sp[i]
    else:
        new_sp.append(sp[i])

print(f'Список {new_sp}, удаленный элемент - {del_elem}')