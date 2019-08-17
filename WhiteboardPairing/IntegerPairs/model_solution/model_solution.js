/* 
  A runtime-efficient implemention that
  trades time efficiency for space efficiency

  O(n) runtime with O(n) space
*/
function integerPairs(arr, k) {
  // Use a hash to store key-value pairs of numbers
  const hash = {};
  // Loop through the arr
  arr.forEach((x, i) => {
    // check to see if the complement for the
    // current element exists in the hash
    if (hash[k - x]) {
      console.log(x, k - x);
    } else {
      // if it doesn't, then we hash this number
      // +1 so get around 0-indexing
      hash[x] = i + 1;
    }
  });
}

/*
  An alternative implementation that favors
  memory efficiency over time efficiency

  O(n log n) runtime due to the sorting
  with O(1) space
*/
function integerPairs(arr, k) {
  // sort the input array in-place
  arr.sort((x, y) => x - y);
  // initialize indices to track both ends of the array
  let first = 0;
  let last = arr.length - 1;

  while (first < last) {
    const sum = arr[first] + arr[last];
    // check to see if the two elements sum up to k
    if (sum == k) {
      console.log(arr[first], arr[last]);
      first++;
      last--;
    } else {
      // if they don't then we decide whether we increment
      // the first index or decrement the last index
      if (sum < k) first++;
      else last--;
    }
  }
}

/* Some console.log tests */
integerPairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11);  // should print '6 5', '7 4', '8 3', '9 2', '10 1'
console.log();
integerPairs([5, 5, 4], 12);                        // should not print anything
console.log();
integerPairs([99, 45, 38, 1, 68, 78], 100);         // should print '1 99'