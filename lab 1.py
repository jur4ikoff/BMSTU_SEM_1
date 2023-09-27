# Попов Юрий Александрович ИУ7-12Б
# вариант - 11, найти объем, площадь поверхности и площадь боковой поверхности шарового слоя
import math

r, h1, h2 = map(int, input('Введите через пробел радиус основания и высоты шарового слоя: ').split())

'''Нормализуем данные'''
if h1 < 0:
    h1 = 0
elif h1 > r * 2:
    h1 = r * 2

if h2 < 0:
    h2 = 0
elif h2 > r * 2:
    h2 = r * 2

'''по формулам найдем значения велечин: v - объем шарового слоя; surface - площадь боковой поверхности; s_full -
площадь всей поверхности'''
h = abs(h2 - h1)  # высота шарового слоя
surface = round(2 * math.pi * r * abs(h2 - h1), 5)  # по формуле считаем площадь боковой поверхности

'''Геометрически найдем радиусы окружностей-ограничителей'''
r1 = (r ** 2 - (r - h1) ** 2) ** 0.5
r2 = (r ** 2 - (r - h2) ** 2) ** 0.5

'''По формулам считаем оставшиеся велечины'''
s_full = round(surface + math.pi * r1 ** 2 + math.pi * r2 ** 2, 5)
v = round(1 / 6 * math.pi * h ** 3 + 1 / 2 * math.pi * h * (r1 ** 2 + r2 ** 2), 5)
print(f'Объем шарового слоя: {v} \n Площадь боковой поверхности: {surface} \n Площадь полной поверхности: {s_full}')
