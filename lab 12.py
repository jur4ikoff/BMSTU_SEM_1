# 12 лаба
#  текстовый процессор
from utils import input_number

data = ['Дорожные размышления мои были не очень приятны.',
        'Проигрыш мой, по тогдашним ценам, был немаловажен. Я не мог не признаться в душе,что поведение мое в',
        'симбирском трактире было глупо, и чувствовал себя виноватым перед Савельичем. Все это меня мучило.',
        'Старик угрюмо сидел на облучке, отворотясь от меня, и молчал, изредка только покрякивая. Я непременно хотел с',
        'ним помириться и не знал с чего начать. Наконец я сказал ему: «Ну, ну, Савельич! полно, помиримся, виноват;',
        'вижу сам, что виноват. Я вчера напроказил, а тебя напрасно обидел. Обещаюсь вперед вести себя умнее и',
        'слушаться тебя. Ну, не сердись; помиримся».',
        'Эх, батюшка Петр Андреич! — отвечал он с глубоким вздохом. — Сержусь-то я на самого себя;',
        'сам я кругом виноват. Как мне было оставлять тебя одного в трактире! Что делать?',
        'Грех попутал: вздумал забрести к дьячихе, повидаться с кумою.']


def align_print(lst, align=None):
    size = len(max(lst, key=len))
    n = len(lst)
    string = ''
    for i in range(n):
        if align == None:
            if i != n - 1:
                string += f'{lst[i]}\n'
            else:
                string += f'{lst[i]}'
            continue
        elif align == 'l':
            string_len = len(lst[i])
            string += f'{(str(lst[i]) + (" " * (size - string_len)))}\n'
            continue
        elif align == 'r':
            string_len = len(lst[i])
            string += f'{(" " * (size - string_len) + str(lst[i]))}\n'
            continue
        elif align == 'c':
            string_len = len(lst[i])
            string += f'{" " * ((size - string_len) // 2) + str(lst[i]) + " " * ((size - string_len) // 2)}\n'
            continue

    return string


def ask_menu():
    print('Выберите действие')
    print()
    print('1 - Выравнивание по левому краю')
    print('2 - Выравнивание по правому краю')
    print('3 - Выравнивание по центру')
    print('4 - Удаление всех вхождений заданного слова')
    print('5 - Замена слова на другое')
    print('6 - Вычисление арифметических операций в тексте') # Сложение и вычитание
    print('7 - Найти и удалить предложение с максимальным количеством слов на заданную букву ')
    print('8 - Выход')
    command = input_number('Введите параметр от 1 до 8', int)
    while command not in range(1, 9):
        command = input_number("\033[31mОшибка! Введите параметр от 1 до 8", int)
    print("\033[0m", end=' ', sep='')


def main():
    while True:
        command = ask_menu()
        if command == 1:
            print(align_print(data, 'r'))
        elif command == 2:
            print(align_print(data, 'l'))
        elif command == 3:
            print(align_print(data, 'c'))


if __name__ == '__main__':
    main()
