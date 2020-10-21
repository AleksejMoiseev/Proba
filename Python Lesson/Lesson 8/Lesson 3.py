names = ["€bentsi", "$Fedor", "€Ilya", "$Roman"]
euro_millioners = []
for name in names:
    if name.startswith("€"):
        euro_millioners.append(name)

# Через лист компрехейшен
euro_millioners = [name for name in names if name.startswith("€")]
print(euro_millioners)
# Generator comrehistion
generator = (name for name in names if name.startswith("€"))
print(generator)
# print(list(generator))# Проходит один раз и по всему и потом доступа к значению не будет
for i in generator:
    print(f"generatjr{i}")# не выведит ничего так весь генератор обнулился в предыдущем  List
# Создание генератора через yield и через Generator comrehistion
