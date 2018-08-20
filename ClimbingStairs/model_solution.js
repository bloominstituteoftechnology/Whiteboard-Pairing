/* 
  Naive Recursive Solution

  Simple and intuitive, but has a runtime
  of O(3^n) due to the three recursive calls
  Successive calls also repeat a lot of work
*/
function naiveClimbStairs(n) {
  // base case 1
  if (n < 0) return 0;
  // base case 2
  else if (n == 0) return 1;
  // move towards our base case
  else {
    return naiveClimbStairs(n-1) + naiveClimbStairs(n-2) + naiveClimbStairs(n-3);
  }
}

/* 
  Recursive solution that utilizes memoization

  This solution should run much faster than the naive
  solution, since it isn't repeating work, giving it 
  a runtime of O(n).
  
  Also takes O(n) additional space over the naive 
  solution due to the added usage of the cache array
*/
function memoizedClimbStairs(n, cache) {
  if (n < 0) return 0;
  else if (n == 0) return 1;
  else if (cache[n] > 1) return cache[n];
  else {
    cache[n] = memoizedClimbStairs(n-1, cache) +
               memoizedClimbStairs(n-2, cache) +
               memoizedClimbStairs(n-3, cache);
    return cache[n];
  }
}

/* Some console.log tests */
console.log(naiveClimbStairs(10));  // should print 274
console.log(naiveClimbStairs(30));  // should print 53798080

// console.log(memoizedClimbStairs(30, Array(30)));  // should also print 53798080, though must quicker than the naive implementation
// console.log(memoizedClimbStairs(50, Array(50)));  // should print 10562230626642
