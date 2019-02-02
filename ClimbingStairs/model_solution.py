# Naive Recursive Solution
#
# Simple and intuitive, but has a runtime
# of O(3^n) due to the three recursive calls
# Successive calls also repeat a lot of work

def naive_climb_stairs(n):
    # base case 1
    if n < 0:
        return 0

    # base case 2
    elif n == 0:
        return 1

    # move towards our base case
    else:
        return naive_climb_stairs(n-1) + naive_climb_stairs(n-2) + naive_climb_stairs(n-3)

# Recursive solution that utilizes memoization
#
# This solution should run much faster than the naive
# solution, since it isn't repeating work, giving it 
# a runtime of O(n).
#
# Also takes O(n) additional space over the naive 
# solution due to the added usage of the cache array

def memoized_climb_stairs(n, cache):
    if n < 0: return 0
    elif n == 0: return 1
    elif cache[n] > 1: return cache[n]
    else:
        cache[n] = memoized_climb_stairs(n-1, cache) + \
                   memoized_climb_stairs(n-2, cache) + \
                   memoized_climb_stairs(n-3, cache)

        return cache[n]

# Some tests
print(naive_climb_stairs(10))  # should print 274
print(naive_climb_stairs(30))  # should print 53798080 after about 30 seconds

# print(memoized_climb_stairs(30, [0] * 31))  # should also print 53798080, though must quicker than the naive implementation
# print(memoized_climb_stairs(50, [0] * 51))  # should print 10562230626642
