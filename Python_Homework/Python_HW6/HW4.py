#!/usr/bin/env python3
"""Программа хранящая данные о великих баскетболистах
"""
main_list_basketball_player = []

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


def print_all_players(list_players):  # Функция печати всех игроков
    counter = 1
    for player_dic in list_players:
        print(f"№ {counter}")
        print_one_player(player_dic)
        counter = counter + 1


def search_player(name):  # функция печати всех игроков
    for person in main_list_basketball_player:
        if (name in person["first_name"]) or (name in person["last_name"]):
            print_one_player(dic=person)
            return person


def save_players():
    pass


def remove_player(name):
    name_players = search_player(name=name)
    print(main_list_basketball_player.index(name_players))  # нашли индекс в главном maine для удаления


#print_one_player(main_list_basketball_player[0])
#print_all_players(main_list_basketball_player)
#search_player("Расселл")
remove_player("Ларри")