import unittest
from Python_Homework.Python_HW14.HW14 import BasketballTeam, BasketballPlayer


class TestBasketballPlayer(unittest.TestCase):

    def test_search_player(self):
        team = BasketballTeam()
        dp = {"name": "fedor2", "last_name": "tolmatchev", "birth_year": 1979, "height": 185}
        player = BasketballPlayer.make_basketball_player(dp)
        team.add_player(player=player)
        person = team.search_player(basketballplayer=player)
        self.assertEqual(player, person)

    def test_remove_player(self):
        team = BasketballTeam()
        dp = {"name": "fedor2", "last_name": "tolmatchev", "birth_year": 1979, "height": 185}
        player = BasketballPlayer.make_basketball_player(dp)
        team.add_player(player=player)
        person = team.remove_player(basketballplayer=player)
        self.assertEqual(player, person)


if __name__ == '__main__':
    unittest.main()
    # team = BasketballTeam()
    # dp = {"name": "fedor2", "last_name": "tolmatchev", "birth_year": 1979, "height": 185}
    # player = BasketballPlayer.make_basketball_player(dp)
    # team.add_player(player=player)
    # team.show_players()
