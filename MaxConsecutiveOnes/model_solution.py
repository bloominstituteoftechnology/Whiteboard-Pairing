"""
  Time Complexity: O(n)
  Space Complexity: O(1)
  
  Algorithm: We loop through our list of numbers and count how many consecutive 1s we see. When we come across a 0,
             we check and see if our current # of consecutive 1s is the longest one we've encountered before updating
             our final answer.
             
             
"""


def findMaxConsecutiveOnes(nums):
    max = 0
    count = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    return max if max > count else count


"""
Time Complexity: O(n)
Space Complexity: O(n)

Algorithm: Since the only valid inputs are 0s and 1s we know that the only thing that can separate a string of 1s is a 0.
           Therefore we can split on every occurrence of a "0" and store our 1s in a list
           The longest string in the resulting list will contain the most consecutive 1s and will therefore be our answer.

           Steps: convert to string
                  split by 'zero'
                  calculate substring length
                  get the max length
"""


def findMaxConsecutiveOnes2(nums):
    lst = ''.join([str(x) for x in nums]).split('0')  # not very efficient
    return max([len(x) for x in lst])


print(findMaxConsecutiveOnes([1, 1, 1, 0, 0, 1, 1]))  # should return 3
print(findMaxConsecutiveOnes2([1, 0, 0, 1, 1]))  # should return 2
