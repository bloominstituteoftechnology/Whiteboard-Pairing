def zeros_to_the_right(arr):
    left = 0
    right = len(arr) - 1
    n_zeros = 0
    did_swap = False

    while left < right:
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            did_swap = True
        else:
            if arr[left] != 0:
                left += 1
            if arr[right] == 0:
                right -= 1
    print(arr)

    if did_swap:
        return len(arr) - right
    else:
        return len(arr) - left

print("Number of non-zero integers: ", zeros_to_the_right([0, 3, 1, 0, -2]))  
# should print:
# [-2, 3, 1, 0, 0]
# Number of non-zero integers: 3

print("Number of non-zero integers: ", zeros_to_the_right([1, 2, 3, 0, 4, 0, 0]))
# should print:
# [1, 2, 3, 4, 0, 0, 0]
# Number of non-zero integers: 4

print("Number of non-zero integers: ", zeros_to_the_right([4, 1, 2, 5]))
# should print:
# [4, 1, 2, 5]
# Number of non-zero integers: 4

print("Number of non-zero integers: ", zeros_to_the_right([0, 0, 0, 0, 0]))
# should print:
# [0, 0, 0, 0, 0]
# Number of non-zero integers: 0
