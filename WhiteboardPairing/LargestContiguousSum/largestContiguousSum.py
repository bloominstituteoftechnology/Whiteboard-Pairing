# Create function that pulls in the array:
#   if array is empty, return None:
# Create a variable to keep track of largest contiguous sum
#   This variable will need to be negative -inf so that any value will replace it
# Create variable to keep track of the current contiguous sum being investigated
#   This can be equal to the first value in the array
# Create a for loop for the length of the array
#   Add the value of the current item to the current contiguous sum.
#   If the value is larger than the largest contiguous sum,
#       largest contiguous sum = current contiguous sum
#   If the vale of current contiguous sum drops below 0,
#       current contiguous sum equals 0 and start the count over.
# Return largest contiguous sum.
