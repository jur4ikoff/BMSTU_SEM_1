# Файл с частоиспользуемыми функциями


def input_number(user_message, to_type: [int, float]) -> [int, float]:
    """Ввод числа"""
    while True:
        user_input = input(f"{user_message}: ")
        try:
            return to_type(user_input)
        except ValueError as e:
            print(f'Неверный ввод числа\nКод ошибки: {e}')
        # except ValueError as e:
        #    print


def input_lst(n=None, list_type=int):
    """Ввод списка"""
    if n == None:
        n = input_number('Введите количество элементов в списке:', int)

    list_of_numbers = []
    for i in range(n):
        el = input_number(f'Введите {i} элемент списка', list_type)
        list_of_numbers.append(el)

    return list_of_numbers
