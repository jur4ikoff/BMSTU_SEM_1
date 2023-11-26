# Выполнил Попов Юрий ИУ7-12Б
# сортировки
# метод вставок с бинарным поиском
import math
import time
from utils import input_number, input_lst, generate_list


def input_data():
    """Ввод размерности"""
    n1 = input_number("Введите N1:", int)
    n2 = input_number("Введите N2:", int)
    n3 = input_number("Введите N3:", int)
    return (n1, n2, n3)


def make_table():
    pass


def binary_sort(lst: list, n=None) -> list:
    if n == None:
        n = len(lst)




def main():
    n1, n2, n3 = input_data()  # Ввод N
    user_list = input_lst()

    list1 = generate_list(n1, 0, 1000)
    list2 = generate_list(n2, 0, 1000)
    list3 = generate_list(n3, 0, 1000)


if __name__ == '__main__':
    main()
