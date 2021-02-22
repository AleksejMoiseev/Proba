from mvc_movie import Movie, Actor
from mvc_movie.view import View


def main():
    view = View()
    view.show_all()
    peter = [Actor(name="Peter", last_name="First")]
    movie_obj = Movie(title="First Peter", date_realized=2020, actor=peter)
    view.add_movie(movie_obj)
    view.show_all()


if __name__ == '__main__':
    main()