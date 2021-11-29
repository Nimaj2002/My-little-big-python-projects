def show_Matris_from_list(Matris_List, row, column):
    result = []
    for _ in range(row):
        new_M = []
        for _ in range(column):
            new_M.append(0)
        result.append(new_M)

    for i in range(row):
        j = 0
        while j < column:
            result[i][j] = Matris_List.pop(0)
            j += 1

    for R in result:
        print(*R)


show_Matris_from_list([0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1], 3, 4)
