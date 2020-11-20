#!/usr/bin/env python3
"""
Реализуйте класс «Book». Необходимо хранить в полях класса: название
книги, год выпуска, жанр, автора (instance of Writer), ​ ISBN​ . Реализуйте
методы класса для ввода данных, вывода данных, реализуйте доступ к
отдельным полям через методы класса.
"""
import datetime


class Book:
    def __init__(self, name_book, year_of_issue, genre, isbn):
        self.__name_book = name_book
        self.__year_of_issue = year_of_issue
        self.__genre = genre
        self.__isbn = isbn

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
        print(self.library)

    def delete_book(self, book_obj):
        if book_obj in self.library:
            index = self.library.index(book_obj)
            del self.library[index]
            return print(f"Object deleted - {book_obj}")
        return print("Function don`t know this object")

    def find_book_by_name(self, name):
        for book in self.library:
            if name in book.name_book:
                return book
            return "Книга не найдена"

    def get_all_books_by_author(self, author):
        pass

    def new_books(self):
        list_new_books = []
        for book in self.library:
            if book == Library.year_now():
                list_new_books.append(book)
        return list_new_books

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


book1 = Book("first", 1934, "fant1934", 1123456)
book2 = Book("second", 1935, "fant1935", 2123456)
book3 = Book("third", 1936, "fant1936", 3123456)
book4 = Book("fourth", 1937, "fant1937", 4123456)
l = Library()
l.add_book(book1, book2, book3, book4)
print(l.find_book_by_name("fir"))
print(f"year today {Library.year_now()}")
