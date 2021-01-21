""""
Approach #1:  use slicing to reverse k numbers in the array
Time Complexity: O(n)
Space Complexity: O(1)

"""


def rotate(nums, k):
    # % k to make sure it's less than total length of nums array
    k %= len(nums)

    nums[k:], nums[:k] = nums[:-k], nums[-k:]


"""
Time complexity : O(n) n elements are reversed a total of three times.
Space complexity : O(1)

reverse all the elements of the array. Then, reversing the first
k elements followed by reversing the rest n-kn−k elements gives us the required result.

Original List                   : 1 2 3 4 5 6 7
After reversing all numbers     : 7 6 5 4 3 2 1
After reversing first k numbers : 5 6 7 4 3 2 1
After revering last n-k numbers : 5 6 7 1 2 3 4 --> Output
"""

nums = [1, 2, 3, 4, 5, 6, 7]
nums2 = [99, -1, -100, 3]


def rotate2(nums, k):
    # % k to make sure it's less than total length of nums array
    k %= len(nums)

    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums)-1)


print(nums)  # [1, 2, 3, 4, 5, 6, 7]
print(rotate(nums, 3))
print(nums, 'after')  # [5, 6, 7, 1, 2, 3, 4]

print(nums2)  # [99, -1, -100, 3]
print(rotate2(nums2, 2))
print(nums2, 'after')  # [-100, 3, 99, -1]
