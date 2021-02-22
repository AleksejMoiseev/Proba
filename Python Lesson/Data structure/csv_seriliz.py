import csv

"""
Помогает сохранять и читать в csv формате 
"""

with open("file.csv", "rt") as file:
    text = csv.reader(file)
    for line in text:
        print((line))