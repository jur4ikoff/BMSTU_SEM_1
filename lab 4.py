#  Попов Юрий Александрович ИУ7-12Б
'''Таблица значений и построение графика'''
import math

'''Блок ввода'''
start_z, end_z, step = map(float, input('Введите через пробел начало отсчета, конец отсчета (по z) и шаг: ').split())


#  Функции
p1 = lambda z: (z ** 4) - (3 * z ** 3) + (8 * z ** 2) - 5
p2 = lambda z: (10.125 * z ** 0.5) - 20.15 * math.cos((math.pi / 2) * z)

#  Делаем таблицу
table = []
print(f'\n{"Таблица значений для 2 функций":^106}')
print('—' * 105)
print(f'|{"Номер":^25}|{"z":^25}|{"p1":^25}|{"p2":^25}|')
print('—' * 105)


for i in range(math.ceil((end_z - start_z) / step) + 1): # ищем порядковые номера
    cur_z = start_z + step * i
    cur_z1 = p1(cur_z)
    cur_z2 = p2(cur_z)

    if cur_z <= end_z:
        print(f'|{i + 1:^25.6g}|{cur_z:^25.6g}|{cur_z1:^25.6g}|{cur_z2:^25.6g}|')

print('—' * 105)