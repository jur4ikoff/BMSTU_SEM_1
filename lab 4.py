#  Попов Юрий Александрович ИУ7-12Б
# Таблица значений и построение графика в осях z y
import math

'''Блок ввода'''
start_z, end_z, step = map(float, input('Введите через пробел начало отсчета, конец отсчета (по z) и шаг: ').split())

#  Функции
p1 = lambda z: (z ** 4) - (3 * z ** 3) + (8 * z ** 2) - 5
p2 = lambda z: (10.125 * z ** 0.5) - 20.15 * math.cos((math.pi / 2) * z)

draw_p_axis = False


#  Делаем таблицу
def make_table() -> list:
    global draw_p_axis
    '''Функция строит таблицу значений для функции и возвращает массив, состоящий из кортежа типа (z, p1)'''
    table = []
    print(f'\n{"Таблица значений для 2 функций":^106}')
    print('—' * 105)
    print(f'|{"Номер":^25}|{"z":^25}|{"p1":^25}|{"p2":^25}|')
    print('—' * 105)

    for i in range(math.ceil((end_z - start_z) / step) + 1):  # ищем порядковые номера
        cur_z = start_z + step * i
        cur_z1 = p1(cur_z)  # Получаем значение функции p1 and p2
        cur_z2 = p2(cur_z)

        if cur_z1 < 0:
            draw_p_axis = True
        if round(cur_z, 2) <= end_z:
            print(f'|{i + 1:^25.6g}|{cur_z:^25.6g}|{cur_z1:^25.6g}|{cur_z2:^25.6g}|')
            table.append((cur_z, cur_z1))

    print('—' * 105)
    return table


table = make_table()
size = 120  # размер графика
serifs = int(input('Введите количество засечек на оси Y (По умолчанию 8): ') or 8)

if not (4 <= serifs <= 8): # проверка на колво засечек
    pass
