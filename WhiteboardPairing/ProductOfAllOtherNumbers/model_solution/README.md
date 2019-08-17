# Product Of All Other Numbers 

## Understanding the Problem

This problems asks, given an array of integers as input, to produce another
array where each value in the resulting is the product of every element from the
input array _except_ the one at the current index. Let's break that down with
some more examples. 

If we're given the array `[6, 9, 1, 4, 8]`, then our function should produce an
array of the same length, where the value at index 0 should be the product of
every element _except_ the value at index 0. So index 0 of our result array
should be:

```
[9*1*4*8, ... ] <- No 6 since 6 is the value at index 0 in the input array
```

In other words, every index in our result array should be the product of every
array element _except_ the value at the same index in the input array. So then
the other values in the result array would be:

```
[288, 6*1*4*8, 6*9*4*8, 6*9*1*8, 6*9*1*4]

-> [288, 192, 1728, 432, 216]
```

Ok, what about edge cases? Well, what if we're handed an empty array? We should
probably just return an empty list then. What about a one element array? There
are no other values to multiply by in that case. Let's just return the input
array then. Once we have an array of at least length two, then we should be able
to handle that array adequately. Let's make sure with the following two-element
array: `[66, 4]`.

With such an input array, the array our function should return would be:

```
[4*1, 66*1] -> [4, 66]
```

In the case of a two-element array, since there are no other elements for each
array element to be multiplied by, we'll make do by multiplying each element by
the multiplicative identity 1. This has the same result as reversing the
two-element array.

## Coming Up With A Strategy

One straightforward idea that comes to mind could be to use nested loops, an
outer loop for looping through all the array elements to keep track of which
element to _not_ multiply by, with an inner loop that performs the
multiplication of each element. In pseudocode:

```
def product_of_all_others(arr):
    result = []
    outer loop that keeps track of which element we don't want to multiply
        inner loop performs the multiplication
            product = 1
            if inner loop index matches outer loop index
                don't multiply by this value
            otherwise, multiply this value to product 
            add product to our result array
    return result
```

This implementation exhibits O(n^2) runtime, since we're looping over every
element as many times as there are elements in the array. The best we can
probably do as far as runtime is concerned is linear, since there's no way
around touching every array element at least once, since we'll have to do that
to calculate the running products. 

Are there any clues in the problem that we could make use of? Since this problem
is asking us to not include a particular value, could we perhaps frame the
problem slightly differently? After all, in order to not include some element, 
we could just as well include it and then take it away. How do we reverse
multiplication? Division! Well, wouldn't the value that we would need at every 
index be the same as the _total_ product of every element in the array, but 
divided by element at that index? 

Here's an idea: what if we calculated the total product of the entire array, and
then looped through our array, dividing the total product by the current array
element to get the product of every array element _except_ the value at the
current index. In pseudocode, that might look like this:

```
def product_of_all_others(arr):
    calculate the total product of every array element 
    loop through our array
        divide the total product by the current array element
        add this product to a result array
    return the result array 
```

That seems promising. It would be a linear solution, though we'd have to perform
two passes over the data, the first time to calculate the total product, and the
second time to divide the total product by each array element. Nonetheless, that
is a linear solution! 

In python, that might look like the following:

```python
# functools is the module that includes the `reduce` function
import functools

def product_of_all_others(arr):
    # use reduce to calculate the total product
    total_product = reduce(lambda x, y: x * y, arr)
    # return a list of total_product divided by every arr element
    return [total_product // x for x in arr]
```

Short and sweet! 

As a follow up, think about how you would solve this problem if division was
disallowed. 
