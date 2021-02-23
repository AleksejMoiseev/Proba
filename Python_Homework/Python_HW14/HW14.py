import csv
"""
1.Переписать задание No6.4 про великих баскетболистов используюпринципы OOP
(В решении как минимум должны быть классы BasketballPlayer и BasketballTeam )
2.Написать минимум 5 юнит тестов для методов из каждого классаиспользуя:
a.Unit test framework->test_basketball_ut.py
b.Pytest -> test_basketball_pt.py
"""


class BasketballPlayer:
    def __init__(self, name, last_name, birth_year, height):
        self._name = name
        self._last_name = last_name
        self.birth_year = int(birth_year)
        self.height = int(height)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @classmethod
    def make_basketball_player(cls, val):
        return cls(**val)

    def __str__(self):
        return f"{self.name},{self.last_name},{self.birth_year},{self.height}"

    def __repr__(self):
        obj = f" basketballplayer : \n name = {self.name} \n last_name = {self.last_name}\n"
        return obj

    def __eq__(self, other):
        if self.name == other.name and self.last_name == other.last_name:
            return True


class BasketballTeam:

    def __init__(self):
        self.main_list_basketball_team = []

    def load(self):
        with open("players_file.csv", "rt") as file:
            text_csv = csv.reader(file)
            list_all_basketball_player = [line for line in text_csv]
            for line in list_all_basketball_player:
                for row in line:
                    tuple_player = tuple(row.split(","))
                    dict_player = dict(name=tuple_player[0], last_name=tuple_player[1],
                                       birth_year=int(tuple_player[2]), height=int(tuple_player[3]))
                    self.main_list_basketball_team.append(BasketballPlayer.make_basketball_player(dict_player))

    def load_players(self, path):
        self.main_list_basketball_team.clear()
        with open(path, "rt") as file:
            file_text = file.read()
        list_all_basketball_player = file_text.split("\n")

        for player in list_all_basketball_player:
            tuple_player = tuple(player.split(","))
            dict_player = dict(name=tuple_player[0], last_name=tuple_player[1],
                               birth_year=tuple_player[2], height=tuple_player[3])
            self.main_list_basketball_team.append(BasketballPlayer.make_basketball_player(dict_player))

    def show_player(self, player):
        print(player)

    def show_players(self):
        for player in self.main_list_basketball_team:
            print(player)

    def add_player(self, player):
        self.main_list_basketball_team.append(player)

    def search_player(self, basketballplayer):
        for person in self.main_list_basketball_team:
            if person == basketballplayer:
                return person
        print("basketballplayer not team")
        return 0

    def sort_height_player(self):  # Функция сортировки по ' По росту'
        counter = 0
        print("Список трех самых высоких баскетболиста : ")
        list_dict = []
        for person in self.main_list_basketball_team:
            list_dict.append(person.__dict__)
        sort_list = sorted(list_dict, key=lambda k: int(k['height']), reverse=True)
        for person in sort_list:
            dic_of_player = {"name": person["_name"], "last_name": person["_last_name"],
                             "birth_year": int(person["birth_year"]), "height": int(person["height"])}
            print(BasketballPlayer.make_basketball_player(dic_of_player))
            counter += 1
            if counter >= 3:
                return 0

    def remove_player(self, basketballplayer):
        person = self.search_player(basketballplayer=basketballplayer)
        if person:
            index = self.main_list_basketball_team.index(person)
            return self.main_list_basketball_team.pop(index)
        return 0

    def save_players(self):
        with open("players_file.csv", "rt+") as file:
            text_csv = csv.writer(file)
            text_csv.writerow(self.main_list_basketball_team)


if __name__ == '__main__':
    dp = {"name": "fedor1", "last_name": "tolmatch", "birth_year": 1979, "height": 185}
    # bp = BasketballPlayer(name="fedor", last_name="tolmatch", birth_year=1979, height=185)
    bp1 = BasketballPlayer.make_basketball_player(dp)
    # print(bp1 == bp1)
    # print(bp1)
    team1 = BasketballTeam()
    team1.load()
    team1.add_player(player=bp1)
    # team1.add_player(player=bp1)
    # team1.load_players(path="basketballmen.txt")
    # team1.load_players(path="players_file.csv")
    # team1.add_player(player=bp1)
    # print(team1.search_player(basketballplayer=bp1))
    # team1.remove_player(basketballplayer=bp1)
    # team1.search_player(basketballplayer=bp1)
    # team1.sort_height_player()
    team1.show_players()
    # team1.save_players()
    # print(bp1.__dict__)
















