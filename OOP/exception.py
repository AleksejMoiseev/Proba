"""
Пример создания собственных Exception
"""


class MyExption(Exception):

    def __init__(self, *args):
        self.msg = args[0] if args else None
        super().__init__(*args)

    def __str__(self):
        return f"Всё пипец {self.msg}"


if __name__ == '__main__':
    try:
        raise MyExption('uuuuuuuuuuuuuuuuuu')
    except MyExption:
        print("wwwwwwww")
