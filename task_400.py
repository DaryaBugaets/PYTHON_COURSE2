# Задача №49(40). Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# from os.path import exists
# from csv import DictReader, DictWriter

# def get_info():
#     first_name = 'Иван'
#     last_name = 'Иванов'
#     phone_number = '8890567786543'
#     return [first_name, last_name, phone_number]
# # with это менеджер контекста, используя его нам не надо вызывать close
# def create_file(file_name):
#     with open(file_name, 'w', encoding = 'utf-8') as data: 
#         f_writer = DictWriter(data, fieldnames = ['Имя', 'Фамилия', 'Телефон'])
#         f_writer.writeheader()
# def read_file(file_name):
#     with open(file_name, 'r', encoding = 'utf-8') as data:
#         f_reader = DictReader(data)
#         return list(f_reader)
# def write_file(file_name, lst):
#     res = read_file(file_name)
#     obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
#     res.append(obj)
#     with open(file_name, 'w', encoding = 'utf-8', newline = '') as data: 
#         f_writer = DictWriter(data, fieldnames = ['Имя', 'Фамилия', 'Телефон'])
#         f_writer.writeheader()
#         f_writer.writerows(res)
# file_name = 'phone.csv'
# def main():
#     while True:
#         command = input('Введите комманду: ')
#         if command == 'q':
#             break
#         elif command == 'w':
#             if not exists(file_name):
#                 create_file(file_name)
#             write_file(file_name, get_info())
#         elif command == 'r':
#             if not exists(file_name):
#                 print('Файл отсутствует. Создайте его')
#                 continue
#             print(*read_file(file_name))
# main()


# усложнили
from os.path import exists
from csv import DictReader, DictWriter

class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt        

def get_info():
    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input('Введите имя: ')
            if len(first_name) < 2:
                raise NameError('Не валидное имя')
            else:
                is_valid_first_name = True
        except NameError as err:
            print(err)
            continue

    last_name = 'Иванов'
    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input('Введите номер: '))
            if len(str(phone_number)) != 11:
                raise LenNumberError('Неверная длина номера')
            else:
                is_valid_phone = True
        except ValueError:
            print('Не валидный номер!')
            continue
        except LenNumberError as err:
            print(err)
            continue


    return [first_name, last_name, phone_number]
# with это менеджер контекста, используя его нам не надо вызывать close
def create_file(file_name):
    with open(file_name, 'w', encoding = 'utf-8') as data: 
        f_writer = DictWriter(data, fieldnames = ['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding = 'utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)

def write_file(file_name, lst):
    res = read_file(file_name)
    for el in res:
        if el['Телефон'] == str(lst[2]):
           print('Такой телефон уже существует') 
           return
    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    res.append(obj)
    with open(file_name, 'w', encoding = 'utf-8', newline = '') as data: 
        f_writer = DictWriter(data, fieldnames = ['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

file_name = 'phone.csv'

def main():
    while True:
        command = input('Введите комманду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует. Создайте его')
                continue
            print(*read_file(file_name))

main()




    


