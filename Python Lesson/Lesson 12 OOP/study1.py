"""
Stack
"""


class Stack:
    """Этот класс описание Стэка"""
    def __init__(self):
        self._container = []  # "_ позволяет обозначить метод как приватный"

    def __str__(self):
        return str(self._container)

    def pop(self):
        value = self._container[1]
        del self._container[-1]
        return value

    def push(self, obj):
        self._container.append(obj)

    def is_empty(self):
        return len(self._container) == 0

    def top(self):
        return self._container[-1]


if __name__ == '__main__':
    s = Stack()
    # Даёт доступ к атрибутом класса __dict__ вывод:{'_container': []}
    print(s.__dict__)