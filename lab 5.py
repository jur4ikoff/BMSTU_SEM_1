# Попов Юрий ИУ7-12Б
# Нахождение суммы мат ряда 𝑦 = 1 + 𝑥/1 + (x ** 2) /2 + (x ** n) / n


# Ввод
eps, step, n = map(float, input(
    'Введите точность (float), шаг печать (int) и количество итераций (int) через пробел: ').split())
x = float(input('Введите x (по умолчанию x = 1): ') or 1)


def check_data(eps, step, n) -> tuple:
    '''Фуункция принимает на вход введенные данные и валидирует их'''
    if step == int(step):
        step = int(step)
    else:
        raise Exception('Step must be integer')

    if n == int(n):
        n = int(n)
    else:
        raise Exception('number of iterations must be integer')

    return eps, step, n


eps, step, n = check_data(eps, step, n)

# вычисляем значение функции
summ = 1  # изначальна сумма равна единице, тк первый элемент = 1
index = n
if n > 0:
    table = [(1, 1)]
else:
    table = []
for i in range(1, n):  # первая иттерация - первый элемент равен 1 -> осталось 9 иттераций
    cur = (x ** i) / i
    summ += cur
    if cur < eps:
        index = i
        break
    table.append((cur, summ))

# перебираем таблицу и выводим
print('—' * 100)
print(f'┃{"№ итерации":^32}┃{"Текущий элемент":^32}┃{"Сумма ряда":^32}┃')
print('—' * 100)
for i in range(0, index, step):
    number = i
    cur = table[i][0]
    summ = table[i][1]
    print(f'┃{number + 1:^32.7g}┃{cur:^32.7g}┃{summ:^32.7g}┃')
print('—' * 100)
print(f'Сумма ряда равна - {table[index - 1][1]}. Посчитано за {index} итераций')


# cur = 4 * ((-1) ** i) / (2 * i + 1) формула pi нужно много иттераций