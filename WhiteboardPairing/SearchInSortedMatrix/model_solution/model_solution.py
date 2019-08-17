def search_sorted_matrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return (row, col)

    return (-1, -1)

# Tests
matrix = [ 
    [1, 4, 7, 12, 15, 999], 
    [2, 5, 19, 32, 35, 1001], 
    [4, 8, 24, 34, 36, 1002], 
    [40, 41, 42, 44, 45, 1003], 
    [98, 99, 101, 104, 190, 1009], 
]

print(search_sorted_matrix(matrix, 1))    # should print (0, 0)
print(search_sorted_matrix(matrix, 7))    # should print (0, 2)
print(search_sorted_matrix(matrix, 999))  # should print (0, 5)
print(search_sorted_matrix(matrix, 1001)) # should print (1, 5)
print(search_sorted_matrix(matrix, 104))  # should print (4, 3)
print(search_sorted_matrix(matrix, 1010)) # should print (-1, -1)

