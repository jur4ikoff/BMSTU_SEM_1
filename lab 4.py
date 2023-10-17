#  Попов Юрий Александрович ИУ7-12Б
# Таблица значений и построение графика в осях z y
import math

'''Блок ввода'''
start_b, end_b, step = map(float, input('Введите через пробел начало отсчета, конец отсчета (по b) и шаг: ').split())

#  Функции
d1 = lambda b: (b + 1) ** 0.5 - (1 / (b + 1)) - 0.5
d2 = lambda b: b ** 3 + (9.3 * b ** 2) + 7.4 * b - 16.3

draw_b_axis = False
change_sign = 0
eps = 10 ** -4


#  Делаем таблицу
def make_table() -> list:
    global draw_b_axis, change_sign, eps
    '''Функция строит таблицу значений для функции и возвращает массив, состоящий из кортежа типа (b, d1)'''
    table = []
    print(f'\n{"Таблица значений для 2 функций":^106}')
    print('—' * 105)
    print(f'|{"Номер":^25}|{"b":^25}|{"d1":^25}|{"d2":^25}|')
    print('—' * 105)

    compl = False  # проверка на комплексной число
    last = cur_z2 = d2(start_b)
    for i in range(math.ceil((end_b - start_b) / step) + 1):  # ищем порядковые номера
        cur_b = start_b + step * i  # значение b
        cur_b1 = '-'  # Получаем значение функции d1 and d2
        cur_b2 = '-'
        try:
            cur_b1 = d1(cur_b)  # Получаем значение функции d1 and d2
            cur_b2 = d2(cur_b)
        except ZeroDivisionError:
            compl = True

        if type(cur_b1) == complex:
            cur_b1 = '-'
            compl = True
        if type(cur_b2) == complex:
            cur_b2 = '-'
            compl = True
        if cur_b == -1:
            cur_b1 = '-'
            compl = True

        if not compl and (
                type(last) == int or type(last) == float):  # если не комплекс и предыдущее число принадлежит R
            if (last >= 0 and cur_b2 < 0) or (last < 0 and cur_b2 >= 0):  # Проверка на смену знака
                change_sign += 1

        if (type(cur_b1) == int or type(
                cur_b1) == float) and cur_b1 < 0:  # Если значение функции меньше 0, то рисуем ось x
            draw_b_axis = True

        if cur_b <= end_b + eps:  # Если текущий z меньше чем верхняя граница интервала
            if not (compl):  # Если на интервале нет комплексных чисел
                print(f'|{i + 1:^25.6g}|{cur_b:^25.6g}|{cur_b1:^25.6g}|{cur_b2:^25.6g}|')
            else:
                print(f'|{i + 1:^25.6g}|{cur_b:^25.6g}|{cur_b1:^25}|{cur_b2:^25}|')
            table.append((cur_b, cur_b1))
        last = cur_b2

    print('—' * 105)
    return table


table = make_table()
print(f'Функция d2 меняет знак на заданном промежутке {change_sign:.6g} раз(а) \n')

size = 120  # размер графика
serifs = int(input('Введите количество засечек на оси Y (По умолчанию 8): ') or 8)

if not (4 <= serifs <= 8):  # проверка на колво засечек
    raise Exception('count of serifs must be in interval [4, 8]')

# минимальный и максимальный элемент значения функции
maxx = max(table, key=lambda x: x[1])[1]
minn = min(table, key=lambda x: x[1])[1]
max_len_b = -1  # максимальная длина b
for i in table:
    symb = format(i[0], '.6g')
    max_len_b = max(len(str(symb)), max_len_b)


# Рисуем график
step_point = (maxx - minn) / (serifs - 1)  # дельта между засечками
scale = size / (maxx - minn)  # числовой шаг между засечками

y_edge = 0  # граница y
up_line = '  ' * (max_len_b - 1)  # верхняя строка
for i in range(serifs):
    y_value = minn + step_point * i # находим значение y
    y_pos = round((y_value - minn) * scale) # ищем местонахождение значения на прямой
    y_value = format(y_value, '.6g') # форматируем
    up_line += ' ' * (y_pos - y_edge) + f'|{y_value}' # добавляем пробелы до нового значение и значение
    y_edge = y_pos + len(y_value) + 1

print(up_line)
print("—" * (size + max_len_b + 4) + "> y")  # ось ординат

pos_b_axis = -2
if draw_b_axis:
    pos_b_axis = round(size * (1 - maxx / (maxx - minn)))

for b, y in table: # иттерируемся по таблице b, y
    b = format(b, ".6g")
    print(f"{b:>{max_len_b}}| ", end="")
    if not draw_b_axis: # если нет отрицательных y
        y_pos = round(size * ((y - minn) / (maxx - minn))) # позиция по y
        print(" " * (y_pos - 1) + "*")
    else:
        if y < 0:
            y_pos = math.floor(pos_b_axis - pos_b_axis * (y / minn))
            print(" " * y_pos + "*" + " " * (pos_b_axis - y_pos - 1) + "|")
        elif y > 0:
            y_pos = round((size - pos_b_axis) * (y / maxx))
            print(" " * pos_b_axis + "|" + " " * y_pos + "*")
        else:
            print(" " * pos_b_axis + "|")

print(" " * (max_len_b + pos_b_axis + 2) + "|")
print(" " * (max_len_b + pos_b_axis + 2) + "˅ b")
