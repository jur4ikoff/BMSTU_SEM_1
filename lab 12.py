# 12 лаба
#  текстовый процессор
# 6 - сложение и вычитание
# 7 - Найти (вывести на экран) и затем удалить слово или предложение по вариант  Предложение с максимальным количеством слов, начинающихся на заданную
# букву.
from utils import input_number

data = ['Дорожные размышления мои были не очень приятны.',
        'Проигрыш мой, по тогдашним ценам, был немаловажен. Я не мог не признаться в душе,что поведение мое в',
        'симбирском трактире было глупо, и чувствовал трактире себя виноватым перед Савельичем. Все это меня мучило.',
        'Старик угрюмо сидел на облучке, отворотясь от меня, и молчал, изредка только покрякивая. Я непременно хотел с',
        'ним помириться и не знал с чего начать. Наконец я сказал ему: «Ну, ну, Савельич! полно, помиримся, виноват;',
        'вижу сам, что виноват. Я вчера напроказил, а тебя напрасно обидел. Обещаюсь вперед вести себя умнее и',
        'слушаться тебя. Ну, не сердись; помиримся».',
        'Эх, батюшка Петр Андреич! — отвечал он с глубоким вздохом. — Сержусь-то я на самого себя;',
        'сам я кругом виноват. Как мне было оставлять тебя одного в трактире! Что делать?',
        'Грех попутал: вздумал забрести к дьячихе, 5 + 5 повидаться с кумою.']


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


def replace_word(lst, align, command):
    if command == 4:
        word = input('Введите слово для удаления: ')
        to_change = ''
    elif command == 5:
        word = input('Введите слово для замены: ')
        to_change = input('Введите слово на которое заменить: ')
    for i in range(len(lst)):
        sp = lst[i].split(' ')
        for j in range(len(sp)):
            if word in sp[j]:
                sp[j] = to_change
        new_str = ''
        for el in sp:
            if el != '':
                new_str += f'{el} '
        lst[i] = new_str
    print(align_print(lst, align))


def calculate(lst, align):
    for i in range(len(lst)):
        sp = lst[i].split(' ')
        if '+' in sp or '-' in sp:
            for j in range(len(sp)):
                if j > 0 and j < (len(sp) - 1) and sp[j] == '+' and (sp[j - 1].isdecimal() and sp[j + 1].isdecimal()):
                    sp[j] = str(int(sp[j - 1]) + int(sp[j + 1]))
                    sp[j - 1] = ''
                    sp[j + 1] = ''
                if j > 0 and j < (len(sp) - 1) and sp[j] == '-' and (sp[j - 1].isdecimal() and sp[j + 1].isdecimal()):
                    sp[j] = str(int(sp[j - 1]) - int(sp[j + 1]))
                    sp[j - 1] = ''
                    sp[j + 1] = ''

        new_str = ''
        for el in sp:
            if el != '':
                new_str += f'{el} '
        lst[i] = new_str
    print(align_print(lst, align))


def delete_proposal(lst, align):
    full_data = ' '.join(lst).replace('!', '.').replace(';', '.').replace('?', '.').split('.')
    max_count = 0
    index = -1
    letter = input('Введите букву: ')
    for i in range(len(full_data)):
        count = 0
        sp = full_data[i].split()
        for j in range(len(sp)):
            if sp[j][0].lower() == letter.lower():
                count += 1
        if count > max_count:
            max_count = count
            index = i

    if index == -1:
        return 'Нет слов на данную букву'
    proposal = full_data.pop(index)
    print(f"Предложение с наибольшим количеством буквы {letter} - {proposal}")
    print(align_print(full_data, align))


def ask_menu():
    print()
    print('Выберите действие')
    print('1 - Выравнивание по левому краю')
    print('2 - Выравнивание по правому краю')
    print('3 - Выравнивание по центру')
    print('4 - Удаление всех вхождений заданного слова')
    print('5 - Замена слова на другое')
    print('6 - Вычисление арифметических операций в тексте')  # Сложение и вычитание
    print('7 - Найти и удалить предложение с максимальным количеством слов на заданную букву ')
    print('8 - Выход')
    command = input_number('Введите параметр от 1 до 8', int)
    while command not in range(1, 9):
        command = input_number("\033[31mОшибка! Введите параметр от 1 до 8", int)
    print("\033[0m", end=' ', sep='')

    return command


def main():
    align = 'l'
    while True:
        command = ask_menu()
        if command == 1:
            print(align_print(data, 'l'))
            align = 'l'
        elif command == 2:
            print(align_print(data, 'r'))
            align = 'r'
        elif command == 3:
            print(align_print(data, 'c'))
            align = 'c'
        elif command == 4:
            replace_word(data, align, command)
        elif command == 5:
            replace_word(data, align, command)
        elif command == 6:
            calculate(data, align)
        elif command == 7:
            delete_proposal(data, align)
        elif command == 8:
            print('Программа завершилась успешно')
            exit(1)


if __name__ == '__main__':
    main()
