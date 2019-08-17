function searchInSortedMatrix(matrix, target) {
    let row = 0;
    let col = matrix[0].length - 1;

    while (row < matrix.length && col >= 0) {
        if (matrix[row][col] > target) {
            col--;
        } else if (matrix[row][col] < target) {
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

console.log(searchInSortedMatrix(matrix, 1));    // should print [0, 0]
console.log(searchInSortedMatrix(matrix, 7));    // should print [0, 2]
console.log(searchInSortedMatrix(matrix, 999));  // should print [0, 5]
console.log(searchInSortedMatrix(matrix, 1001)); // should print [1, 5]
console.log(searchInSortedMatrix(matrix, 104));  // should print [4, 3]
console.log(searchInSortedMatrix(matrix, 1010)); // should print [-1, -1]
