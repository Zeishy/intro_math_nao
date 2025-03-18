def my_full_of_1_arr(lines, columns):
    array = [[1 for _ in range(columns)] for _ in range(lines)]
    for row in array:
        print(row)
    print("Nombre de lignes:", len(array))
    print("Nombre de colonnes:", len(array[0]) if array else 0)

my_full_of_1_arr(4, 4)