from mvc_movie.conector import Conector
from mvc_movie.model import Model


class View:

    def __init__(self):
        self.conector = Conector()
        self.model = Model()

    def show_all(self):
        movies = self.model.get_all_movie()
        for movie in movies:
            print(movie)

    def add_movie(self, movie_obj):
        self.conector.add_movie(movie_obj)