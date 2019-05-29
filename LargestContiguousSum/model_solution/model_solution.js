/*
  We'll use a greedy algorithm to check to see if we have a 
  new max sum as we iterate along the along. If at any time
  our sum becomes negative, we reset the sum. 
*/

function largestContiguousSum(arr) {
  let maxSum = 0;
  let sum = 0;

  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];

    if (maxSum < sum) {
      maxSum = sum;
    } else if (sum < 0) {
      sum = 0;
    }
  }

  return maxSum;
}

/* Some console.log tests */
console.log(largestContiguousSum([5, -9, 6, -2, 3]));           // should print 7
console.log(largestContiguousSum([1, 23, 90, 0, -9]));          // should print 114
console.log(largestContiguousSum([2, 3, -8, -1, 2, 4, -2, 3])); // should print 7