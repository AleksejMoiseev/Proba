# Bubble sort
list_sort = [4, 6, 9, 2, 9, 0, 3]
# Определение индексов
for i in enumerate(list_sort):
    print(i)
for i in range(len(list_sort)):
    for j in range(len(list_sort)):
        if list_sort[i] < list_sort[j]:
            swap = list_sort[j]
            list_sort[j] = list_sort[i]
            list_sort[i] = swap

print(list_sort)