function searchInSortedMatrix(matrix, target) {
    let row = 0;
    let col = matrix[0].length - 1;

    while (row < matrix.length && col >= 0) {
        if (matrix[col][row] > target) {
            col--;
        } else if (matrix[col][row] < target) {
            row++;
        } else {
            return [row, col];
        }
    }

    return [-1, -1];
}

// Tests
const matrix = [ 
    [1, 4, 7, 12, 15, 999], 
    [2, 5, 19, 32, 35, 1001], 
    [4, 8, 24, 34, 36, 1002], 
    [40, 41, 42, 44, 45, 1003], 
    [98, 99, 101, 104, 190, 1009], 
];


