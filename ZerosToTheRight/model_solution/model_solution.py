def zeros_to_the_right(arr):
    non_zero_index = 0
   
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[non_zero_index] = arr[non_zero_index], arr[i]
            non_zero_index += 1
    
    print(arr)
    return non_zero_index

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

print("Number of non-zero integers: ", zeros_to_the_right([0, 0, 0, 0, 3, 2, 1]))
# should print:
# [1, 2, 3, 0, 0, 0, 0]
# Number of non-zero integers: 3
