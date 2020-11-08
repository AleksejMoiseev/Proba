#!/usr/bin/env python3
"""Программа хранящая данные о великих баскетболистах
"""
main_list_basketball_player = []


def make_list():  # Функция считывает  и сохраняет текст в главный Лист
    main_list_basketball_player.clear()
    with open("basketballmen.txt", "r") as file:
        file_text = file.read()
    list_all_basketball_player = file_text.split("\n")

    for player in list_all_basketball_player:
        tuple_player = tuple(player.split(","))
        dict_player = dict(first_name=tuple_player[0], last_name=tuple_player[1],
                           birth_year=tuple_player[2], height=tuple_player[3])
        main_list_basketball_player.append(dict_player)


def print_one_player(dic={}):  # Функция печати одного игрока
    if len(dic.values()) == 0:
        dic = search_player()
    else:
        print(f"---- Имя ---- Фамилия ---- День рождения ---- Рост")
        print(f"--- {dic['first_name']} --- {dic['last_name']} --- "
              f"--- {dic['birth_year']} -------- {dic['height']}")
        print()


def print_all_players():  # Функция печати всех игроков
    counter = 1
    for player_dic in main_list_basketball_player:
        print(f"№ {counter}")
        print_one_player(player_dic)
        counter = counter + 1
    print()


def new_player_add():  # функция добавления нового игрока
    print("Добавление нового игрока в команду: ")
    first_name = input("Введите имя нового игрока > ")
    last_name = input("Введите фамилию нового игрока > ")
    birth_year = input("Введите год рождения нового игрока > ")
    height = input("Введите рост нового игрока > ")
    main_list_basketball_player.append({
        "first_name": first_name,
        "last_name": last_name,
        "birth_year": birth_year,
        "height": height,
    })
    print("Игрок добавлен")


def search_player(name=""):  # функция поиска игрока по имени
    if name == "":
        name = input("Введите имя или фамилию для поиска игрока в словаре > ")
    for person in main_list_basketball_player:
        if (name.lower() in person["first_name"].lower()) or \
                (name.lower() in person["last_name"].lower()):
            print_one_player(dic=person)
            return person
    print("Внимание игрок в словаре отсутсвует")
    return 1


def save_players():  # Функция сохранения изменений в текстовый файл
    with open("new_players_file.txt", "w+") as file:
        for dic in main_list_basketball_player:
           player = ",".join(dic.values())
           file.write(player + "\n")
    print("Изменения сохранены")


def sort_height_player():  # Функция сортировки по ' По росту'
    counter = 0
    print("Список трех самых высоких баскетболиста : ")
    sort_list = sorted(main_list_basketball_player, key=lambda k: k['height'], reverse=True)
    for person in sort_list:
        print_one_player(dic=person)
        counter += 1
        if counter >= 3:
            return 0


def remove_player(name=""):  # Удаление игрока
    if not name:
        name = input("Введите имя или фамилию для удаления игрока > ")
        name_players = search_player(name=name)
    else:
        name_players = search_player(name=name)
    if name_players == 1:
        print("Указаного игрока в списке нет")
        return name_players
    index_player = main_list_basketball_player.index(name_players)  # нашли индекс в главном maine для удаления
    rm_player = main_list_basketball_player.pop(index_player)
    print("Удален")
    return rm_player


def choice():  # Функция выбора
    flag = True
    while flag:
        choice_value = int(input("Введите Ваш выбор > "))
        if choice_value == -1:
            return -1
        try:
            if (choice_value >= 1) and (choice_value <= 8):
                raise Exception("Разрешенный диапазон данных от 1 до 8, -1 для выхода")
        except Exception:
            flag = False
    return choice_value


def main():  # Главная функция
    make_list()
    print("*" * 10, "Добро пожаловать в супер словарь", "*" * 10)
    print("Программа предлагает выбрать следующие возможности :")
    print("1. - Считать из файла всех баскетболистов")
    print("2. - Вывести на экран красиво данные одного баскетболиста")
    print("3. - Вывести данные всех баскетболистов")
    print("4. - Сохранить изменения в файл")
    print("5. - Поиск баскетболиста по имени или фамилии")
    print("6. - Вывод на экран тройки самых высоких игрока")
    print("7. - Удалить из списка баскетболиста")
    print("8. - Добавить баскетболиста в список великих")
    print("Выход. - выбрать '-1'")

    while True:
        choice_result = choice()
        if choice_result == -1:
            return -1
        if choice_result == 1:
            make_list()
        elif choice_result == 2:
            print_one_player()
        elif choice_result == 3:
            print_all_players()
        elif choice_result == 4:
            save_players()
        elif choice_result == 5:
            search_player()
        elif choice_result == 6:
            sort_height_player()
        elif choice_result == 7:
            remove_player()
        elif choice_result == 8:
            new_player_add()


if __name__ == '__main__':
    main()