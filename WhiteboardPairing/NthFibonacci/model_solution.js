/* 
  Solution that utilizes memoization to 
  cache prior results

  Exhibits a worst-case runtime of O(2^n)
  due to the unbounded recursion
*/
function nthFib(n) {
  let memo = Array(n);

  function nthFibMemo(n) {
    let v = memo[n];

    if (!v) {
      v = recurse(n);
      memo[n] = v;
    }
    return v;
  }

  function recurse(n) {
    if (n === 0 || n === 1) return n;
    return nthFibMemo(n-1) + nthFibMemo(n-2);
  }

  return nthFibMemo(n);
}

/*
  Linear time and linear space algorithm that 
  builds a memo from the ground up 
*/
function nthFibIterative(n) {
  let memo = Array(n);
  memo[0] = 0;
  memo[1] = 1;

  for (let i = 2; i <= n; i++) {
    memo[i] = memo[i-1] + memo[i-2];
  }

  return memo[n];
}

/* Some console.log tests */
console.log(nthFib(50));
console.log(nthFibIterative(50));
// Both of the above should print 12586269025
// within a quick span of time (less than 1 second)

console.log(nthFib(1000));
console.log(nthFibIterative(1000));
// Both of the above runs should print 4.346655768693743e+208
// within a quick span of time (less than 1 second)