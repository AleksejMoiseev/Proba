import yaml


class Model:

    def __init__(self):
        self._list_movie = []
        self._dump_filename = "./movies.dump"
        self.load()

    def add_movie(self, movie_obj):
        self._list_movie.append(movie_obj)

    def dump(self):
        with open(self._dump_filename, "at") as file:
            yaml.dump(self._list_movie, file)

    def load(self):
        """ load all movie"""
        try:
            with open(self._dump_filename, "rt") as file:
                data_movie = yaml.safe_load(file)
                self._list_movie = data_movie
        except FileNotFoundError:
            f = open(self._dump_filename, "wt")
            f.close()
        finally:
            return self._list_movie

    def get_all_movie(self):
        return self._list_movie


if __name__ == '__main__':
    mod = Model()
    # mod.add_movie(movie_obj=["petr", 1984, "Детектив"])
    # mod.dump()
    # print(mod.load())
