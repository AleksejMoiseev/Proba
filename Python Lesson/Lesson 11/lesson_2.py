"""
Дан текстовый файл. необходимо  создать  новый файл убрав из него
все слова содержащеся в другом файле
"""


def get_unwandet_word_list():
    words = []
    with open("/home/alameda/Proba_python/Proba/Python Lesson/Lesson 11/exclude.txt") as file:
        return [word.strip() for word in file.readlines()]


def get_text():
    with open("text.txt") as file:
        return file.read()


def replace_unwandet_words(text, unwandet_words):
    text_word = text.split()
    update_text =[]




if __name__ == '__main__':
    unwandet_words = get_unwandet_word_list()
    text = get_text()
    # new_next = replace_unwandet_words(text, unwandet_words)
    # write_newfile(new_next)