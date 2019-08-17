# Solution that makes use of division
# import functools
# import operator
# 
# def product_of_all_others(arr):
#     if len(arr) < 2:
#         return None
#     total_product = reduce(operator.mul, arr)
#     return [total_product // x for x in arr]

# Solution that doesn't make use of division
def product_of_all_others(arr):
    if len(arr) < 2:
        return None

    products = [0 for _ in range(len(arr))]

    # For each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1

    for i in range(len(arr)):
        products[i] = product_so_far
        product_so_far *= arr[i]


    # For each integer, we find the product of all the integers
    # after it. Since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product_so_far = 1

    for i in range(len(arr) - 1, -1, -1):
        products[i] *= product_so_far
        product_so_far *= arr[i]

    return products


# Tests 
print(getProductsOfAllIntsExceptAtIndex( [1, 2, 3, 4, 5] ))   
# should print [120, 60, 40, 30, 24]

print(getProductsOfAllIntsExceptAtIndex( [9, 90] ))   
# should print [90, 9]

print(getProductsOfAllIntsExceptAtIndex( [50] ))   
# should print None

