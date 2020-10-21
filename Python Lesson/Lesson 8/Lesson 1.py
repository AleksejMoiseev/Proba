# генератор функция range()
# generator comreheition
list_o =["w", "i"]
result = (name for name in list_o if name.startswith("w"))
# function map  map(function, list) на каждый элемент  листа запускается функция function

names = ['bentsi', 'fedor']


def rev_n(name1):
    tmp = list(name1)
    tmp.reverse()
    i = ''.join(tmp)
    return i


print(list(map(rev_n, names)))




