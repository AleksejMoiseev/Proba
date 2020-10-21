"""

"""
from collections import defaultdict # умеет создавать defolt значение
d = {"name":["bentsi", "anton"]}
d["name"].append("aleksey")
countries = {"Russia", "Israel", "Poland"}
def main():

    countries.add("New Zeland")
    countries.discard("Poland") # Удаление элемента


def find_country(countries, to_find):
    found_country = []
    for country in countries:
        if to_find.lower() in country.lower():
            found_country.append(country)
    return found_country





if __name__ == '__main__':
    main()
    print(find_country(countries=countries, to_find="ru"))