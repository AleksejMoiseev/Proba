#!/usr/bin/env python3
"""
1. Программа удаляет все гласные буквы в слове
2. Программа принимает строку и возращает список слов
   содержащий слово и его длину
"""


def remove_vowels(sentence, arr):
    new_sentence = ""
    for i in sentence:
        if i not in arr:
            new_sentence = new_sentence + i
    return new_sentence


def split_sentence(sentence):
    sentence_list = sentence.split()
    list_sentence = [[i, len(i)] for i in sentence_list]
    return list_sentence

if __name__ == "__main__":
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    sentence = input("Enter sentence > ")
    print(remove_vowels(sentence=sentence, arr=vowels))
    print(split_sentence(sentence=sentence))
