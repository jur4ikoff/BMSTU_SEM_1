# Попов Юрий Александрович ИУ7-12Б

import random

sp = [int(random.randint(0, 1000)) for _ in range(10)]


def task1a(sp):
    '''1 задание'''
    ind = int(input('Введите индекс элемента: '))
    elem = int(input('Введите значение элемента: '))
    sp.insert(ind, elem)
    return sp


print(task1a(sp))


def task1b(sp):
    '''Добавить элем в заданое место списка алгоритмически'''
    ind = int(input('Введите индекс элемента: '))
    elem = int(input('Введите значение элемента: '))
    new_sp = []
    for i in range(len(sp)):
        if i == ind:
            new_sp.append(elem)
        else:
            new_sp.append(sp[i])

    return new_sp


print(task1b(sp))


def task2(sp):
    pass

print()