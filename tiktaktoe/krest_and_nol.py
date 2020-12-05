"""
Практическое задание
создание игры крестики нолики
сущности - доска 3*3 клетки
два игрока которые по очереди ставят либо крестик либо нолик в отдельную ячейку доски

"""
from tiktaktoe.board import Board


class Game:
    def __init__(self, players):
        self._board = Board()
        self._players = players

    @property
    def players(self):
        return self._players

    def run(self):
        pass




if __name__ == '__main__':
    b = Board()
    b.board = X(2, 2)
    print(b)
