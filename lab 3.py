#  Попов Юрий Александрович ИУ7-12Б
'''Написать программу, которая по введенным целочисленным координатам трех точек на плоскости вычисляет длины сторон
образованного треугольника и длину высоты, проведенной из наименьшего угла. Определить, является ли
треугольник остроугольным. Далее вводятся координаты точки. Определить, находится ли точка внутри треугольника.
Если да, то найти расстояние от точки до наиболее удаленной стороны треугольника или ее продолжения.'''
import math


def get_triangle_area(a, b, c) -> float:
    '''Вычисление площади треугольника'''
    return 1 / 2 * abs((a[0] - c[0]) * (b[1] - c[1]) + (b[0] - c[0]) * (c[1] - a[1]))


'''Ввод. x1, y1 - координаты первой точки, x2, y2 - координаты второй точки, x3, y3 - координаты третий точки'''
x1, y1 = map(int, input('Введите целочисленные координаты первой вершины треугольника через пробел: ').split())
x2, y2 = map(int, input('Введите целочисленные координаты второй вершины треугольника через пробел: ').split())
x3, y3 = map(int, input('Введите целочисленные координаты третий вершины треугольника через пробел: ').split())

'''Вычисления'''
# Вычисления длин сторон по теореме Пифагора
l1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
l2 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
l3 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
min_l = min(l1, l2, l3)
print(f'В искомом треугольнике первая сторона: {l1:.6g}, вторая сторона: {l2:.6g}, третья сторона: {l3:.6g}')
# Поиск косинусов углов по теореме косинусов
cos1 = (l1 ** 2 + l3 ** 2 - l2 ** 2) / (2 * l1 * l3)
cos2 = (l1 ** 2 + l2 ** 2 - l3 ** 2) / (2 * l1 * l2)
cos3 = (l2 ** 2 + l3 ** 2 - l1 ** 2) / (2 * l2 * l3)
# Значение углов
a1 = round(math.degrees(math.acos(cos1)))
a2 = round(math.degrees(math.acos(cos2)))
a3 = round(math.degrees(math.acos(cos3)))
# поиск мин угла и поиск вершины с мин углом
min_angle = min(a1, a2, a3)  # минимальный угол
if a1 == min_angle:
    min_top = 1  # вершина с мин углом
elif a2 == min_angle:
    min_top = 2
else:
    min_top = 3

# напротив наименьшего угла лежит наименьшая сторона --> h_max = s_triangle / min(l1, l2, l3)
# макс косинус равен минимальному углу

s_triangle = get_triangle_area((x1, y1), (x2, y2), (x3, y3))
h_max = 2 * s_triangle / min(l1, l2, l3)  # высота из мин угла
print(f'Высота, проведенная из вершины с миниальным углом -  {h_max:.6g}')
if a1 < 90 and a2 < 90 and a3 < 90:  # проверка на остроугольность
    print(f"Треугольник остроугольный")
else:
    print(f'Треугольник неостроугольный')
x, y = map(int, input('Введите целочисленные координаты точки через пробел: ').split())


def is_point_in_triangle(a, b, c, p):
    '''Определяет принадлежит ли точка треугольнику'''
    tr_area = get_triangle_area(a, b, c)  # Площадь основного треугольника
    tr_area2 = get_triangle_area(a, b, p)  # Площади треугольника, образованного из 2 точек основного
    tr_area3 = get_triangle_area(a, p, c)  # и точки, которая проверяется на принадлежность
    tr_area4 = get_triangle_area(b, p, c)  # к треугольнику
    return (tr_area == tr_area2 + tr_area3 + tr_area4), tr_area2, tr_area3, tr_area4


flag, s2, s3, s4 = is_point_in_triangle((x1, y1), (x2, y2), (x3, y3), (x, y))
max_distanse = int
max_s = max(s2, s3, s4)
if s2 == max_s:  # a, b, p
    max_distanse = 2 * s2 / l1
elif s3 == max_s:  # a, c, p
    max_distanse = 2 * s3 / l3
elif s4 == max_s:  # b, c, p
    max_distanse = 2 * s3 / l2
if flag:
    print(f'Введеная точка находится внутри треугольника. наибольшее растояние до стороны: {max_distanse}')
else:
    print(f'Введеная точка находится снаружи треугольника. наибольшее растояние до стороны: {max_distanse}')
