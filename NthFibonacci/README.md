# Nth Fibonacci

We can implement a naive recursive algorithm to display the nth Fibonacci number with the following code:

```js
function naiveNthFib(n) {
  if (n === 0 || n === 1) {
    return n;
  }
  return nthFib(n-1) + nthFib(n-2);
}
```

This solution works fine for small inputs, but even for n = 50, this function takes a significant amount of time to run. 

Implement a more efficient 