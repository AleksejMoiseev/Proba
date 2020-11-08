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


def print_one_player(dic):  # Функция печати одного игрока
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


def search_player(name):  # функция поиска игрока по имени
    for person in main_list_basketball_player:
        if (name.lower() in person["first_name"].lower()) or \
                (name.lower() in person["last_name"].lower()):
            print_one_player(dic=person)
            return person
    return 1


def save_players():
    pass


def remove_player(name=""):
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
    return rm_player

#print_one_player(main_list_basketball_player[0])
#print_all_players(main_list_basketball_player)
#search_player("Расселл")
#new_player_add()
# print_all_players()
# remove_player()
# print_all_players()
