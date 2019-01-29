
#  An alternative implementation that favors
# memory efficiency over time efficiency
# O(n log n) runtime due to the sorting
# with O(1) space

def integerPairs(arr, k):
  found_pair = False
  # sort the input array in-place
  arr.sort()
  # initialize indices to track both ends of the array
  first = 0
  last = len(arr) - 1

  while first < last:
    sum = arr[first] + arr[last]
    # check to see if the two elements sum up to k
    if sum == k:
      print(str(arr[first]) + ', ' + str(arr[last]))
      first += 1
      last -= 1
      found_pair = True
    else:
      # if they don't then we decide whether we increment
      # the first index or decrement the last index
      if sum < k:
        first += 1
      else :
        last -= 1
  if not found_pair:
      print('No pairs found')

#  A runtime-efficient implemention that
# trades time efficiency for space efficiency
# O(n) runtime with O(n) space

def integerPairs(arr, k):
  found_pair = False
  # Use a hash to store key-value pairs of numbers
  hash = {}
  # Loop through the arr
  for i in range(0, len(arr)):
    # check to see if the complement for the
    # current element exists in the hash
    if k - arr[i] in hash.values():
      print(arr[i], k - arr[i])
      found_pair = True
    else:
      # if it doesn't, then we hash this number
      # +1 so get around 0-indexing
      hash[i+1] = arr[i]
  if not found_pair:
    print('No pairs found')
        
        
# Some basic tests 
integerPairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)   # should print '1, 10', '2, 9', '3, 8', '4, 7', '5, 6'
print('---------------')
integerPairs([5, 5, 4], 12)                         # should print 'No pairs found'
print('---------------')
integerPairs([99, 45, 38, 1, 68, 78], 100)          # should print '1, 99'
