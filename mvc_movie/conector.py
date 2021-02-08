from mvc_movie.model import Model


class Conector:
    def __init__(self):
        self.model = Model()

    def add_movie(self, movie_obj):
        self.model.add_movie(movie_obj)
