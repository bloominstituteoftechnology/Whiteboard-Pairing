# Solution that utilizes memoization to 
# cache prior results
# Exhibits a worst-case runtime of O(2^n)
# due to the unbounded recursion

def nthFib(n):
  memo = [None]*(n+1)

  def nthFibMemo(n):
    v = memo[n]

    if v is None:
      v = recurse(n)
      memo[n] = v
    
    return v
  

  def recurse(n):
    if n == 0 or n == 1:
      return n
    return nthFibMemo(n-1) + nthFibMemo(n-2)
  

  return nthFibMemo(n)



# Linear time and linear space algorithm that 
# builds a memo from the ground up 

def nthFibIterative(n):
  memo = [None]*(n+1)
  memo[0] = 0;
  memo[1] = 1;

  for i in range(2, n+1):
    memo[i] = memo[i-1] + memo[i-2]
  

  return memo[n]


# Some console.log tests 
print(nthFib(50));
print(nthFibIterative(50));
# Both of the above should print 12586269025
# within a quick span of time (less than 1 second)

print(nthFib(498));
# Should print 325493296145942940693607070474249585412918826163
#6423939579059478176515507039697978099330699648074089624 
print(nthFibIterative(1000));
# Should print 4.346655768693743e+208
# within a quick span of time (less than 1 second)
