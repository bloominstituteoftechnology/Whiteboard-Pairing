"""
Approach #1
Time Complexity: O(n)
Space Complexity: O(n)

Algorithm: We can use a set to store each number and remove duplicates. If we come across a number that is already in our set, we know
           that it must not be our `Single Number` therefore we can remove it from the set. In the end the only number in the set will
           be the number that was unpaired and therefore not removed.
"""


def singleNumber(nums):
    s = set()
    for num in nums:
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    return s.pop()

  """
  Approach #2
  Time Complexity: O(n)
  Space Complexity: O(1)
  
  Algorithm: We can use bit manipulation to find the unique element using the bitwise XOR operator.
  any number XORed with itself is 0, so each duplicate number will "cancel out" itself, except for the number that only exists once in the list

  Let's say we have an array - [2,1,3,5,2,3,1].
  What we are doing is essentially this-

  => 0 ^ 2 ^ 1 ^ 3 ^ 5 ^ 2 ^ 3 ^ 1

  => 0^ 2^2 ^ 1^1 ^ 3^3 ^5 (Rearranging, taking same numbers together)

  => 0 ^ 0 ^ 0 ^ 0 ^ 5

  => 0 ^ 5

  => 5
  """

  
  
def singleNumber(nums):

    for i in range(1, len(nums)):
        nums[0] ^= nums[i]
    return nums[0]
