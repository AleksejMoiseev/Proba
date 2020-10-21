#!/usr/bin/env python3
"""
Программа проверки являются ли два слова гематрически равными
"""


def gematria(word, arr):
    value_gematria = 0
    word = word.lower()
    for i in word:
        value_gematria = value_gematria + arr.index(i)
    return value_gematria


def compare_words(word1, word2):
    value_gematria_word1 = gematria(word=word1, arr=dictionary_list)
    value_gematria_word2 = gematria(word=word2, arr=dictionary_list)
    if value_gematria_word1 == value_gematria_word2:
        print(f'Слова "{word1}" и "{word2}" гематрически равны')
    else:
        print(f'Слова "{word1}" и "{word2}" гематрически не равны')


if __name__ == "__main__":
    dictionary_list = [chr(a) for a in range(96, 123, 1)]
    compare_words(word1="Bentsi", word2="Darwin")
