/*
  Naive recursive solution that recurses along
  each possible jump and branches out from there
*/
// function minJumps(arr, start=0, end=arr.length-1) {
//   // base case: when start and end are at the same spot
//   if (start === end) {
//     return 0;
//   }
//   // when nothing is reachable, return infinity
//   if (arr[start] === 0) {
//     return Infinity;
//   }
//   // traverse through all the spots reachable by
//   // arr[start], recursively getting the min number
//   // of jumps needed to reach arr[end]
//   let min = Infinity;
//   for (let i = start + 1; i <= end && i <= start + arr[start]; i++) {
//     const jumps = minJumps(arr, start, end);
//     if (jumps !== Infinity && jumps + 1 < min) {
//       min = jumps + 1;
//     }
//   }

//   return min;
// }

/*
  Solution that utilizes dynamic programming in order to
  build up a `jumps` array from left to right such that 
  `jumps[i]` indicates the minimum number of jumps needed
  to reach that spot from `arr[0]`. At the end, return 
  `jumps[n-1]`.
*/
function minJumps(arr, n=arr.length) {
  const jumps = new Array(n);

  if (n === 0 || arr[0] === 0) {
    return Infinity;
  }

  jumps[0] = 0;

  for (let i = 1; i < n; i++) {
    jumps[i] = Infinity;
    for (let j = 0; j < i; j++) {
      if (i <= j + arr[j] && jumps[j] !== Infinity) {
        jumps[i] = Math.min(jumps[i], jumps[j] + 1);
        break;
      }
    }
  }

  return jumps[n-1];
}

console.log(minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]));  // should print 3
console.log(minJumps([1, 3, 6, 1, 0, 9]));  // should print 3
console.log(minJumps([2, 0, 0, 5, 8, 1, 7, 4, 9, 12, 1]));  // should print Infinity
console.log(minJumps([1, 3, 6, 3, 2, 3, 6, 8, 9, 5]));  // should print 4