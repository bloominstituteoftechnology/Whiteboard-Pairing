# We'll use a greedy algorithm to check to see if we have a 
# new max sum as we iterate along the array. If at any time
# our sum becomes negative, we reset the sum. 

def largest_contiguous_sum(arr):
    max_sum = 0
    current_sum = 0
    
    for x in arr:
        current_sum += x
        max_sum = max(currentSum, max_sum)

        if current_sum < 0:
            current_sum = 0

    return max_sum

# Tests
print(largest_contiguous_sum([5, -9, 6, -2, 3]))           # should print 7
print(largest_contiguous_sum([1, 23, 90, 0, -9]))          # should print 114
print(largest_contiguous_sum([2, 3, -8, -1, 2, 4, -2, 3])) # should print 7
