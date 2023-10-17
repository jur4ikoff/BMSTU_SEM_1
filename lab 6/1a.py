import random

sp = list(map(int, input('Введите список: ').split())) or [int(random.randint(0, 1000)) for _ in range(10)]
print(sp)


'''1 задание'''
ind = int(input('Введите индекс элемента: '))
elem = int(input('Введите значение элемента: '))
sp.insert(ind, elem)
print(sp)