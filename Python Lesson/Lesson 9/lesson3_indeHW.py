"""
САМОСТОЯТЕЛЬНАЯ РАБОТА ПО ИЗУЧЕНИЮ СПИСКОВ, СРЕЗОВ, СЛОВАРЕЙ. ФАЙЛОВ
"""

# Ниже два списка преобрзовать его в словарь


keys = ['ten', 'fifty', 'therty']
value = [10, 20, 30]
keys_value = dict(zip(keys, value))
print(keys_value)


# Обьединить следующие два словаря python в один


dict1 = {'ten': 10, 'twenty': 20, 'therty': 30}
dict2 = {'therty': 30, 'forthy': 40, 'fifty': 50,}
set_dict1_values = set(dict1.values())
set_dict2_values = set(dict2.values())
set_result = set_dict1_values.union(set_dict2_values)
set_dict1_key = set(dict1.keys())
set_dict2_key = set(dict2.keys())
set_result_key = set_dict1_key.union(set_dict2_key)
print(set_result_key)
print(set_result)
dict_result = dict(zip(dict1, dict2))
print(dict_result)
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)



