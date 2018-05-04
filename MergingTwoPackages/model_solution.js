function getIndicesOfItemWeights(arr, limit) {
  const o = {};
  
  for (let i = 0; i < arr.length; i++) {
    const w = arr[i];
    const complementIndex = o[limit - w];
    if (complementIndex !== undefined) {
      return [i, complementIndex];
    } else {
      o[w] = i;
    }
  }
  return [];
}

/* Some simple console.log tests */
console.log(getIndicesOfItemWeights(
  [4, 6, 10, 15, 16],
  21
));   // should print [3, 1]

console.log(getIndicesOfItemWeights(
  [4, 4],
  8
));   // should print [1, 0]

console.log(getIndicesOfItemWeights(
  [12, 6, 7, 14, 19, 3, 0, 25, 40],
  7
));   // should print [6, 2]

console.log(getIndicesOfItemWeights(
  [9],
  9
));   // should print []