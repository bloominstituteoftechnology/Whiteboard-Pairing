/*
  Iterative in-place solution using two loops
*/
function rotateImage(matrix) {
  const len = matrix.length;

  for (let i = 0; i < len / 2; i++) {
    for (let j = i; j < len - i - 1; j++) {

      let bucket = matrix[i][j];
      matrix[i][j] = matrix[j][len - i - 1];
      matrix[j][len - i - 1] = matrix[len - i - 1][len - j - 1];
      matrix[len - i - 1][len - j - 1] = matrix[len - j - 1][i];
      matrix[len - j - 1][i] = bucket;
    }
  }
  return matrix;
}

/*
  A slick functional solution using `Array.map`
  However, this is not an in-place solution since `map`
  returns copies of the mapped array
*/
function rotateImage(matrix) {
  return matrix.map(m => m.reverse())[0]
               .map((cv, i) => matrix.map((rv, j) => matrix[j][i]));
}

/* Some console.log tests */
console.log(rotateImage([
  [1, 2],
  [3, 4]
]));    // should print [ [2, 4], [1, 3] ]

console.log(rotateImage([
  [1, 1, 5, 9, 9],
  [2, 2, 6, 0, 0],
  [3, 3, 7, 1, 1],
  [4, 4, 8, 2, 2],
  [5, 5, 9, 3, 3]
]));    // should print [ [ 9, 0, 1, 2, 3 ],
        //                [ 9, 0, 1, 2, 3 ],
        //                [ 5, 6, 7, 8, 9 ],
        //                [ 1, 2, 3, 4, 5 ],
        //                [ 1, 2, 3, 4, 5 ] ]

