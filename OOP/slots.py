class Value:

    __slots__ = ('first_value', 'second_value')  # Позволяет добавлять свойства указанные в неизменяемом списке

    def __init__(self, first_value, second_value):
        self.first_value = first_value
        self.second_value = second_value


if __name__ == '__main__':
    v = Value(first_value=1, second_value=2)
    v.val = 3
    """
    Traceback (most recent call last):
    File "/home/alex/Documents/Projects/Proba/OOP/slots.py", line 12, in <module>
    v.val = 3
    AttributeError: 'Value' object has no attribute 'val'
    """