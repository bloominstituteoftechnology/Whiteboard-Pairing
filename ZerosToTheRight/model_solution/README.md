# Zeros to the Right Walkthrough

## Understanding the Problem

This problem is relatively straightforward to understand. Any 0s that
aren't on the right side of the input array need to get to the right
side of the array. Ok, we can do that pretty easily. 

One question we'd want to address first before we start sketching out a
strategy is whether we'd want to mutate the input array or whether we
should instead create a new array. Well, we'll definitely want to
iterate along the array, and if we opt to mutate the input array, that's
going to make iterating along the array a lot trickier since the array
is going to be changing with each iteration step. 

## A First Pass Strategy

So it will probably be a lot easier to simply opt to create and return a
new array. With that question answered, a strategy falls into place.
We can iterate along the input array, and we'll keep track of the number
of 0s we see as we're iterating. Every time we see a non-0 integer, we
can simply copy it to our output array. Once we've traversed the entire
input array, all of the non-0 integers will be in the output array and
we'll also know how many 0s we saw in the input array. From there, we
can simply push that many 0s onto the end of the output array. Note that
the problem asks us to return the number of non-0 integers in the array.
Since we've been counting the number of 0s we've been seeing as we've
been traversing through the array, to figure out the number of non-0
integers, we can simply subtract the length of the entire array by the
number of 0s we've seen. So our first pass implementation might look
something like this: 

```python
def zeros_to_the_right(arr):
    output = []
    n_zeros = 0

    for x in arr:
        if x == 0:
            n_zeros += 1
        else:
            output.append(x)

    for _ in range(n_zeros):
        output.append(0)
    
    return len(output) - n_zeros
```

## Evaluating our First Pass Implementation

This implementation works as expected. Hooray! Now it's time to figure
out the time and space complexity of this implementation. We have a
single traversal over our input array, and we only perform O(1)
operations inside this loop, so the for loop incurs an O(n) runtime
cost. 

The second for loop incurs a runtime cost proportional to the number 
of elements we are adding to the output array. In the worst case this
would never be more than the length of the entire input array (like in
the case that our function receives an input array of all 0s). So as far
as time complexity is concerned, our worst case runtime is O(2n).

As far as space complexity is concerned, we're creating a new array that
has the exact same number of elements as our input array, so the amount
of additional memory we're using is proportional to the number of input
elements. Thus our space complexity is O(n).

So the next question we should ask ourselves is, can we do better than
this? As far time complexity is concerned, we've _technically_ achieved a
linear runtime. It's not possible to achieve a runtime faster than
linear since we can't get away with not inspecting each array element at
least once to see whether an element is a 0 or a non-0 integer value. 

That being said, our first pass solution achieves an O(2n) runtime. Even
though this theoretically simplifies down to an O(n) runtime, in
practice, actually eliminating unnecessary linear passes does yield
significant performance improvements when the input size is very large.
So if we're able to get our implementation down to the point where it
only performs one loop through the data, then we should aim for that as
our next goal. 

Similarly, the extra memory usage is also not desirable unless we
_absolutely_ need it. Let's think about whether we can get away with not
incurring that extra memory cost. So we're going to see if we can
achieve an implementation that only performs _one_ pass through the
input data and doesn't require any extra memory. 

## Improving Upon our First Pass Implementation

If we're not looking to incur any extra memory, then we'll have to
directly mutate the input array. If we're looking to do that, then we'll
not want to remove elements from the input array since it makes iterating
through the array tricky, along with the fact that removing elements
from an array incurs an O(n) runtime in the worst case. 

As an alternative to removing from the array, we can instead swap two
elements in the array, which is an O(1) operation. 
