# 14 лаба
# Попов Ю.А
#  Binary DB
from utils import input_number, output_list
import os
import struct

# BD STRUCTURE
# ID NAME AGE
# 0 YURI 18
# h 225s h

FORMAT = "<h255sh"

# Скачать bin ed

class UnexpectedException(Exception):
    """Неожиданная ошибка"""


def ask_menu():
    print()
    print('Выберите действие')
    print('1 - Выбрать файл для работы (Переопределить изначально-выбранную)')
    # print('2 - Инициализировать базу данных') Реализовано
    print('2 - Вывести содержимое базы данных')
    print('3 - Добавить запись в произвольное место базы данных')
    print('4 - Удалить произвольную запись из базы данных')
    print('5 - Поиск по одному полю')
    print('6 - Поиск по двум полям')
    print('7 - Выход')
    command = input_number('Введите параметр от 1 до 7', int)
    while command not in range(1, 8):
        command = input_number('Введите параметр от 1 до 7', int)
    print()

    return command


def create_db(file: str):
    open(file, "wb").close()


def find_database():
    files = os.listdir()
    db_count = 0
    db_names = []
    for file in files:
        if os.path.isfile(file) and file.endswith(".db"):
            db_count += 1
            db_names.append(file)
    choice_mode = input('Создать новую базу данных(Y/N): ')
    if choice_mode.lower() == 'y':
            name = input("Введите название новой базы данных: ") + ".db"
            create_db(name)
            return name
    if db_count == 1:
        return db_names[0]
    if db_count > 1:
        print(output_list(db_names, message="Вывод возможных баз данных", n=db_count, lst_name='db_name'))
        db_number = input_number(f'Введите номер базы данных от 0 до {db_count - 1}', int)
        while db_number not in range(0, db_count):
            db_number = input_number(f'Введите номер базы данных от 0 до {db_count - 1}', int)
        return db_names[db_number]
    if db_count == 0:
        name = input("Введите название новой базы данных: ") + ".db"
        create_db(name)
        return name


def print_db(database):
    pass


def main():
    db_name = find_database()
    print(f"Инициализирована: {db_name}")
    while True:
        command = ask_menu()
        if command == 1:
            db_name = find_database()
            print(f"Используемая база: {db_name}")


print(struct.pack(FORMAT, 0, b'sdfdsf', 23))
if __name__ == '__main__':
    pass
    main()
