import pytest
from HW_pt_basketballplayer.HW14 import BasketballPlayer, BasketballTeam


@pytest.fixture
def make_player():
    dp = {"name": "fedor", "last_name": "tolmatchev", "birth_year": 1979, "height": 185}
    player = BasketballPlayer.make_basketball_player(dp)
    return player


@pytest.mark.parametrize("name, last_name, birth_year, height", [("fedor", "tolmatchev", 1979, 185)])
def test_basic(make_player, name, last_name, birth_year, height):
    assert make_player.name == name
    assert make_player.last_name == last_name


def test_add_player(make_player):
    team = BasketballTeam()
    team.add_player(player=make_player)
    assert team.search_player(basketballplayer=make_player) == make_player