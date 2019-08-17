function getIndicesOfItemWeights(arr, limit) {
  // use an object to store item weights
  // along with their 'complement'
  const o = {};
  
  for (let i = 0; i < arr.length; i++) {
    const weight = arr[i];
    // check the object to see we have the 
    // complement of the current weight
    const complementIndex = o[limit - weight];
    // if we do, then we're done!
    if (complementIndex !== undefined) {
      return [i, complementIndex];
    } else {
      // otherwise, store the weight with its index
      o[weight] = i;
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