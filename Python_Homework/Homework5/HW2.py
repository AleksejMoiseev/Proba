#!/usr/bin/env python3
"""
Написать программу которая принимает список имен и возвращает новый
список в котором к каждому имени будет добавлен суффикс рандомного
валютного символа [“$”, “€”, “”, “₪”]. Количество валютных символов
должно быть равно количеству букв в имени. Имя может содержать только
большие и маленькие буквы английского алфавита. Максимальная длина
имени 40 символов. В решении использовать генератор map. Выбросить
exceptions для некорректного ввода.
Написать как минимум 2 позитивных и 2 негативных теста в отдельном
файле.
"""
import random


def name_verification(word):
    flag = True
    for i in word:
        flag = flag * (((i >= "a") and (i <= "z")) or
                       ((i >= "A") and (i <= "Z")))
    if flag:
        return True
    return False


def input_names_list():
    arr_names = []
    flag = True
    print("Имя может содержать только большие и маленькие буквы английского алфавита."
          " Максимальная длина имени 40 символов.")
    while flag:
        new_name = input("Enter name > ")
        assert len(new_name) <= 40, "Длина слова не должны быть больше 40 символов"
        assert name_verification(new_name) == True, "В имени может содержать только буквы латинского алфавита"
        arr_names.append(new_name)
        stop_input = input("Хотите закончить ввод имен ? если да нажмите 'Y', если нет то любую букву > ")
        if stop_input == "Y" or stop_input == "y":
            flag = False
    return arr_names


def currency_suffix(word):
    character = random.choice(["$", "€", "@", "₪"])
    new_word = word + character * len(word)
    return new_word


# print(list(map(currency_suffix, names)))
# print(name_verification("фaaaAaAAA"))
#print(input_names_list())
if __name__ == "__main__":
    print(list(map(currency_suffix, input_names_list())))

