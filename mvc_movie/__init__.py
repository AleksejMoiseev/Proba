class Actor:

    def __init__(self, name, last_name, role):
        self._name = name
        self._last_name = last_name
        self._role = role

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, val):
        self._last_name = val

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    def __str__(self):
        return f" Actor: name {self.name}, last_name {self.last_name} in role {self.role}"



class Movie:

    def __init__(self, title, date_realized, actor):
        self.title = title
        self.date_realized = date_realized
        self.actor = actor

    def __str__(self):
        movie_str = f" Film_title {self.title}" + "\n " + f"realized {self.date_realized}\n Actors: \n"
        for actor in self.actor:
            movie_str = movie_str + str(actor) + "/n"
        return movie_str


if __name__ == '__main__':
    peter = [Actor(name="Peter", last_name="First", role="King")]
    movie1 = Movie(title="First Peter", date_realized=2020, actor=peter)
    print(movie1)