matrix_deck = [
    [], [], [], [],
    [], [], [], []
]
matrix_colums = 8
for line in range(len(matrix_deck)):
    for element in range(matrix_colums):
        matrix_deck[line].append(0)

matrix_copy = list(matrix_deck)

for index in range(len(matrix_copy)):
    line = matrix_copy[index]
    if index % 2 == 0:
        for num in range(len(line)):
            if num % 2 == 0:
                line[num] = 1
    else:
        for num in range(len(line)):
            if num % 2 != 0:
                line[num] = 1
for line in matrix_copy:
    print(line)


