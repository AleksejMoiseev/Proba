country_capital = {
    "Russia": "Moscow",
    "Israel": "Jerusalem",
    "Japan": "Tokyo",
    "China": "Beijing",
}


def add_capital(country, city, dict):  # добавление элемента страны
    dict[country] = city


def delete_country(country, dict):
    return dict.pop(country)


def search_country_by_capital(city):
    for item in country_capital.items():
        if item[1] == city:
            return item[0]


print(delete_country("Japan", country_capital))
print(country_capital)