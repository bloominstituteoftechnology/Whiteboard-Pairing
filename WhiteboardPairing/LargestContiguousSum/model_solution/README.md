# Largest Contiguous Sum Walkthrough

## Understanding the Problem

The problem statement for this question is pretty terse. Let's break it down.
It's asking us to find the maximum sum of some contiguous subarray of the input
array. The input array can contain both positive and negative integers. 

Let's start simple. The problem statement says the array can contain both
positive and negative values. Let's initially loosen the constraints and just
assume that our arrays can only contain positive integers. In that case, the
largest contiguous sum of any array is just going to be the sum of all the elements
in the array, since they're all positive!

Ok, what about if our array only contains negative values? What's the largest
contiguous sum in that case? Say we have something like this:

```
[-9, -18, -3, -99, -70, -1, -15]
```

The largest contiguous sum is going to be one largest negative value, since
every number is negative and we're looking for the largest sum. So with this
example, we would need to return just -1, which is the single largest value in
the entire array. 

Ok, with that in mind, let's look at an example array that contains both
positive and negative values:

```
[3, -10, 4]
```

When we had an array of just positive integers, we summed every value in the
array. When we had an array of just negative integers, we picked the largest
negative value. Let's try both of those strategies with this array that contains
both positive and negative values. 

The total sum of the entire array is 3 + (-10) + 4 which is -3. The single
largest value of this array is 4. So in this case, our answer would be 4. But
why? What was it about the elements in this example array that prompted us to
end up picking the single largest value over the sum of the entire array? Well,
that was because we saw that the overall sum of the entire array yielded a
negative value. 

That's a bit of handy insight, but it doesn't seem like we have enough
information yet to come up with an algorithm to solve the problem. So let's
continue evaluating some more examples. Let's take one of the example input
arrays: `[2, 3, -8, -1, 2, 4, -2, 3]`. Summing the entire array gives us a total 
sum of 3. Picking the largest single value from the array gives us 4. But we're 
told that the expected answer for this input array is 7, which is a result of
summing up the elements in the subarray `[2, 4, -2, 3]`, the last 4 elements in
the array. How are we supposed to know to sum up that particular subarray?

Let's try this: let's see what the sum at every step of the array is as we sum
up each element in the array one-by-one. If we do that we'll get the following:

```
[2, 3, -8, -1,  2, 4, -2, 3]
 2  5  -3  -4  -2  2   0  3 
```

That doesn't seem to help us much. There sure seem to be a lot of negative sums.
Do we want to take those into account? Are they important? After all, we're
looking for the largest sum, and negative sums don't contribute to that. 

What if we traversed the array, summing up every value as we walk the array, but
then if we see a negative sum, just throw it and start summing again from
scratch? Remember, we're only looking for sums of _contiguous_ subarrays after
all, so we don't need to go jumping around the array to try to find the largest
sum; all the values that we're summing have to be adjacent to one another. 

If we apply this idea to the same array, we have the following:

```
[2, 3, -8, -1,  2, 4, -2, 3]
 2  5   0   0   2  6   4  7
        ^   ^
        |   |
        |   |

these sums are 0 since they'll yield negative sums
```

Hey! We got the expected output of 7 when we applied this idea to the given
array. Let's check to make sure that this works with other arrays that have
positive and negative values.

```
[3, -10, 4]
 3   0   4
```

So far so good. Let's try a larger array:

```
[3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
 3  8   0  1  4  2   5  9 16 18   9 15 18 19  14 18
```

The expected output for this array is 19, which we do get when we apply our idea
to this array. Ok, so from all these sums, how do we pick the largest? To do
that, we can use a variable that will keep track of the largest sum we've seen
so far and update it if we see a larger sum. 

## Coming up with a Strategy

So the idea for our algorithm now is to walk along the input array, updating a
`current_sum` variable. If `current_sum` exceeds the `max_sum` variable, then
we'll update the `max_sum` variable with the value of `current_sum`. If we ever
see that our `current_sum` value is negative, then we'll set `current_sum` to 0
and continue traversing the array:

```python
def largest_contiguous_sum(arr):
    # variable to keep track of the largest sum
    max_sum = -Infinity 
    # variable to keep track of the current sum
    current_sum = 0
    # traverse our array
    for x in arr:
        # add the current element to our current sum
        current_sum += x
        # check to see if our current_sum is larger 
        # than the max_sum
        max_sum = max(max_sum, current_sum)
        # if our current_sum is a negative value
        # reset it to 0
        if current_sum < 0:
            current_sum = 0
    # return the max_sum
    return max_sum
```

## Evaluating our Implementation

The beautiful thing about this algorithm that we just derived (it has a name by
the way, it's called Kadane's Algorithm), is that it only requires a single pass
through the input array and doesn't require allocating any extra memory. So the
rumtime is O(n) and the space complexity is O(1). 

Is this the best we can do? Well, if we think about it, there's no way we can
solve this problem without inspecting every element at least once, since we're
looking to find the maximum contigous sum. We can only be sure that we've found
the maximum sum after we've inspected every value at least once. So, it would
seem our solution is optimal!
