import random

sp = list(map(int, input('Введите список: ').split())) or [int(random.randint(0, 1000)) for _ in range(10)]
print(sp)

ind = int(input('Введите индекс элемента: '))
del_elem = sp.pop(ind)

print(f'Список {sp}, удаленный элемент - {del_elem}')