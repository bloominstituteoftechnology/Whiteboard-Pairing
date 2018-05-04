function spiralCopy(inputMatrix) {
  const numRows = inputMatrix.length;
  const numCols = inputMatrix[0].length;
  // keep track of where we are along each
  // of the four sides of the matrix
  let topRow = 0;
  let bottomRow = numRows - 1;
  let leftCol = 0;
  let rightCol = numCols - 1;

  const result = [];
  // iterate throughout the entire matrix
  while (topRow <= bottomRow && leftCol <= rightCol) {
    // iterate along the top row from left to right
    for (let i = leftCol; i <= rightCol; i++) {
      result.push(inputMatrix[topRow][i]);
    }
    topRow++;
    // iterate along the right column from top to bottom
    for (let i = topRow; i <= bottomRow; i++) {
      result.push(inputMatrix[i][rightCol]);
    }
    rightCol--;

    if (topRow <= bottomRow) {
      // iterate along the bottom row from right to left
      for (let i = rightCol; i >= leftCol; i--) {
        result.push(inputMatrix[bottomRow][i]);
      }
      bottomRow--;
    }

    if (leftCol <= rightCol) {
      // iterate along the left column from bottom to top
      for (let i = bottomRow; i >= topRow; i--) {
        result.push(inputMatrix[i][leftCol]);
      }
      leftCol++;
    }
  }

  return result;
}

/* Some simple console.log tests */
console.log(spiralCopy(
  [[1]]
));   // should print [1]

console.log(spiralCopy(
  [[1], [2]]
));   // should print [1, 2]

console.log(spiralCopy(
  [[1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20]]
));   // should print [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]