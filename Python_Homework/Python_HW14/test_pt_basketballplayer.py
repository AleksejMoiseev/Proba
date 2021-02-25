import pytest
from Python_Homework.Python_HW14.HW14 import BasketballTeam,BasketballPlayer


@pytest.fixture
def make_player():
    dp = {"name": "fedor2", "last_name": "tolmatchev", "birth_year": 1979, "height": 185}
    player = BasketballPlayer.make_basketball_player(dp)
    return player


@pytest.mark.parametrize("name, last_name, birth_year, height", [("Fedor", "tolmatchev", 1979, 185)])
def test_basic(make_player, name, last_name, birth_year, height):
    assert make_player.name == name
    assert make_player.last_name == last_name



