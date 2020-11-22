#!/usr/bin/env python3
"""
Реализуйте класс «Book». Необходимо хранить в полях класса: название
книги, год выпуска, жанр, автора (instance of Writer), ​ ISBN​ . Реализуйте
методы класса для ввода данных, вывода данных, реализуйте доступ к
отдельным полям через методы класса.
"""
import datetime
from Python_Homework.Python_HW9.OOP3 import Writer


class Book(Writer):
    def __init__(self, name_book, year_of_issue, genre, isbn, writer):
        self.__name_book = name_book
        self.__year_of_issue = year_of_issue
        self.__genre = genre
        self.__isbn = isbn
        super().__init__(first_name=writer.first_name,
                         last_name=writer.last_name,
                         birth_year=writer.birth_year)

    @property
    def name_book(self):
        return self.__name_book

    @name_book.setter
    def name_book(self, value):
        self.__name_book = value

    @property
    def year_of_issue(self):
        return self.__year_of_issue

    @year_of_issue.setter
    def year_of_issue(self, value):
        self.__year_of_issue = value

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = value

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        self.__isbn = value

    def __str__(self):
        return f"Название книги: {self.__name_book}\n" \
               f"Год выпуска: --- {self.__year_of_issue}\n" \
               f"Жанр: ----------- {self.__genre}"


"""
Реализуйте класс Library. Класс будет содержать объекты класса «Book»
Имплементировать следующие методы:
○ add_book(book_obj)
○ delete_book(book_obj)
○ find_book_by_name(name)
○ get_all_books_by_author(author)
○ new_books() - книги выпущенные в этом году (текущий год должен
быть выбран актуальным, не hardcoded 2020)
○ __str__
"""


class Library:
    library = []

    def add_book(self, *book_obj):
        for book in book_obj:
            self.library.append(book)
        Library.print_obj_list(self.library)

    def delete_book(self, book_obj):
        if book_obj in self.library:
            index = self.library.index(book_obj)
            del self.library[index]
            return print(f"Object deleted - \n{book_obj}")
        return print("Function don`t know this object")

    def find_book_by_name(self, name):
        for book in self.library:
            if name in book.name_book:
                return book
            return "Книга не найдена"

    def get_all_books_by_author(self, author):
        list_author = []
        author = author.lower()
        for book in self.library:
            first_name = str(book.first_name)
            last_name = str(book.last_name)
            if (author in last_name.lower()) or (author in first_name.lower()):
                list_author.append(book)
        Library.print_obj_list(list_author)
        return list_author

    def new_books(self):
        list_new_books = []
        for book in self.library:
            if book.year_of_issue == Library.year_now():
                list_new_books.append(book)
        Library.print_obj_list(list_new_books)
        return list_new_books

    @staticmethod
    def print_obj_list(arr):
        if not len(arr):
            return print("Запрошенных книг нет в библиотеке")
        print("Запрошенные обьeкты: ")
        for element in arr:
            print(element, end="\n\n")

    @staticmethod
    def year_now():
        year_today = datetime.date.today().year
        return year_today

    def __str__(self):
        result_str = ""
        for book in self.library:
            result_str = result_str + book.name_book + ", " + f"{book.year_of_issue}" \
                         + ", " + book.genre + "\n"
        print()
        return result_str


pushkin = Writer("Пушкин", "Александр", "2005")
ivan_pupkin = Writer("Пупкин", "Иван", "2020")
book1 = Book(name_book="first", year_of_issue=2020, genre="fant1934", isbn=1123456, writer=pushkin)
book2 = Book(name_book="second", year_of_issue=1935, genre="fant1935", isbn=2123456, writer=ivan_pupkin)
book3 = Book("third", 1936, "fant1936", 3123456, pushkin)
book4 = Book("fourth", 1937, "fant1937", 4123456, pushkin)
l = Library()


def main():
    """
    Добавление в библиотеку 4 книги
    """
    print("Список добавленных обьектов: ")
    l.add_book(book1, book2, book3, book4)
    print()
    """
    Удаление книги
    """
    print("Удаление книги")
    l.delete_book(book4)
    print()
    """
    Поиск книги по названию
    """
    print("Поиск книги по названию:")
    print(l.find_book_by_name("fir"))
    print()
    """
    Поиск всех книг автора
    """
    print("вывод всех книг одного автора")
    l.get_all_books_by_author("Пушкин")
    print()
    """
    Книги выпущенные в текущем году
    """
    print("Книги текущего года")
    l.new_books()
    print()
    """
    Репрезентация библиотеки в str
    """
    print("Демонстрация репрезентации")
    print(l)


if __name__ == '__main__':
    main()