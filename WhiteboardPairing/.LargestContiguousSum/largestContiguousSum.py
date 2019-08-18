# Create function that pulls in the array:
def largest_contiguous_sum(array):
    #   if array is empty, return None:
    if len(array) == 0:
        return None
# Create a variable to keep track of largest contiguous sum
    largest_sum = float("-inf")
#   This variable will need to be negative -inf so that any value will replace it
# Create variable to keep track of the current contiguous sum being investigated
    current_sum = 0
#   This can be equal to the first value in the array
# Create a for loop for the length of the array
    for i in range(len(array)):
        #   Add the value of the current item to the current contiguous sum.
        current_sum += array[i]
#   If the value is larger than the largest contiguous sum,
        if current_sum > largest_sum:
            #       largest contiguous sum = current contiguous sum
            largest_sum = current_sum
#   If the value of current contiguous sum drops below 0,
        if current_sum < 0:
            #       current contiguous sum equals 0 and start the count over.
            current_sum = 0
# Return largest contiguous sum.
    return largest_sum


print(largest_contiguous_sum([5, -9, 6, -2, 3]))           # should print 7
print(largest_contiguous_sum([1, 23, 90, 0, -9]))          # should print 114
print(largest_contiguous_sum([2, 3, -8, -1, 2, 4, -2, 3]))  # should print 7
