def matrix_spiral_copy(matrix):
    result = []
    left_column = 0
    right_column = len(matrix[0]) - 1
    top_row = 0
    bottom_row = len(matrix) - 1
    
    while top_row <= bottom_row and left_column <= right_column:
        for i in range(left_column, right_column + 1):
            result.append(matrix[top_row][i])
        top_row += 1
        for i in range(top_row, bottom_row + 1):
            result.append(matrix[i][right_column])
        right_column -= 1
        # check if there's still a top row we need to traverse
        if top_row <= bottom_row:
            for i in reversed(range(left_column, right_column + 1)):
                result.append(matrix[bottom_row][i])
            bottom_row -= 1
        # check if there's still a left column we need to traverse
        if left_column <= right_column:
            for i in reversed(range(top_row, bottom_row + 1)):
                result.append(matrix[i][left_column])
            left_column += 1
    return result