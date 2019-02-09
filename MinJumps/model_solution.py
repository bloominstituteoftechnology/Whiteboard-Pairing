
# Naive recursive solution that recurses along
# each possible jump and branches out from there

def naiveMinJumps(arr, start=0, end=None):
   if end is None:
     end=len(arr)-1
     
   # base case: when start and end are at the same spot
   if start >= end:
     return 0
   
   # when nothing is reachable, return infinity
   if arr[start] == 0:
     return float("inf")

   # traverse through all the spots reachable by
   # arr[start], recursively getting the min number
   # of jumps needed to reach arr[end]
   min = float("inf")
   for i in range(start + 1, start + arr[start]+1): 
     jumps = naiveMinJumps(arr, i, end);
     if jumps != float("inf") and jumps + 1 < min:
       min = jumps + 1

   return min



# Solution that utilizes dynamic programming in order to
# build up a `jumps` array from left to right such that 
# `jumps[i]` indicates the minimum number of jumps needed
# to reach that spot from `arr[0]`. At the end, return 
# `jumps[n-1]`.

def minJumps(arr, n=None):
  if n is None:
    n=len(arr)
    
  jumps = [None]*n

  if n == 0 or arr[0] == 0:
    return float("inf")
  
  jumps[0] = 0

  for i in range(1, n):
    jumps[i] = float("inf")
    for j in range(0, n):
      if i <= j + arr[j] and jumps[j] != float("inf"):
        if jumps[j] is not None:
          jumps[i] = min(jumps[i], int(jumps[j]) + 1)
          break

  return jumps[n-1]


# TESTS
print(naiveMinJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]));  # should print 3
print(naiveMinJumps([1, 3, 6, 1, 0, 9]));  # should print 3
print(naiveMinJumps([2, 0, 0, 5, 8, 1, 7, 4, 9, 12, 1]));  # should print Infinity
print(naiveMinJumps([1, 3, 6, 3, 2, 3, 6, 8, 9, 5]));  # should print 4

print("****")

print(minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]));  # should print 3
print(minJumps([1, 3, 6, 1, 0, 9]));  # should print 3
print(minJumps([2, 0, 0, 5, 8, 1, 7, 4, 9, 12, 1]));  # should print Infinity
print(minJumps([1, 3, 6, 3, 2, 3, 6, 8, 9, 5]));  # should print 4
