# We'll use a greedy algorithm to check to see if we have a 
# new max sum as we iterate along the along. If at any time
# our sum becomes negative, we reset the sum. 

def largestContiguousSum(arr):
    maxSum = 0
    currentSum = 0

    for i in range(len(arr)):
        currentSum += arr[i]

        if maxSum < currentSum:
            maxSum = currentSum
        elif currentSum < 0:
            currentSum = 0

    return maxSum





# Tests
print(largestContiguousSum([5, -9, 6, -2, 3]))           # should print 7
print(largestContiguousSum([1, 23, 90, 0, -9]))          # should print 114
print(largestContiguousSum([2, 3, -8, -1, 2, 4, -2, 3])) # should print 7