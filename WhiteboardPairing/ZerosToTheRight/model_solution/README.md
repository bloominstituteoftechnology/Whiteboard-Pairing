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
elements in the array, which is an O(1) operation. So if the question
becomes "which elements are we looking to swap as we're iterating along
the array?", the answer to that would be that we want to swap 0s on the
left side of the array with non-0 values that are on the right side of
the array. 

Given that, we can keep track of two indices, one that starts at the
left end of the array, the other that starts at the right end. These
will be incremented until they meet in middle. While this is happening,
if the left index value is a 0 at the same time that the right index is
a non-0, then we'll swap those two values. Sketching this idea out, it
might look something like this:

```python
def zeros_to_the_right(arr):
    left = 0
    right = len(arr) - 1
    # keep iterating until the two indices meet in the middle
    while left <= right:
        # if the left index is a 0 and the right index is a non-0
        if arr[left] == 0 and arr[right] != 0:
            # swap them
            arr[left], arr[right] = arr[right], arr[left]
            # move the left and right indices towards the middle
            # of the array so that we make progress 
            left += 1
            right -= 1
```

Ok, so what about when the left index is a non-0 and/or the right index
is a 0? What do we do in those cases? As it stands, this code will very
likely not terminate because it will just hang forever on the while
loop. 

Well, in a vacuum, when do we want the left index to be incremented?
Again, we're looking to swap 0s on the left with non-0s on the right. So
we _don't_ want the left index to be incremented when it's on a 0. That
means that we _do_ want it to be incremented when it's a non-0.
Likewise, with the right index, we want it to _not_ decrement when it's
on a non-0 value, so we want it to be decremented when it's a 0. Let's
add this to our implementation:

```python
def zeros_to_the_right(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        # we're already handling incrementing the left and right
        # indices when we're swapping, so we need to stick the 
        # new iteration logic in an else statement
        else:
            if arr[left] != 0:
                left += 1
            if arr[right] == 0:
                right -= 1
```

With that logic added, we've ensured that the while loop will terminate
and that the input array will be mutated to the desired state with 0s on
the right and non-0 values on the left. But we aren't done yet, since
our function needs to return the number of non-0 values in the array. 

At this point, we could perform another walk through the array and count
the number of non-0 values we see along the way, but we're trying to
limit the number of walks we do through the array. Can we perform some
extra work the first time we walk through the array that would tell us
how many non-0 values exist in the array?

Sure, we can simply increment a counter of non-0 values we encounter as
we're performing our initial traversal through the array. We don't need
to perform a whole other traversal in this case. 

```python
def zeros_to_the_right(arr):
    left = 0
    right = len(arr) - 1

    # counter to keep track of number of non-0 values we see
    n_non_zeros = 0

    while left <= right:
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

            # we encounter a non-0 value in this case
            # increment our counter
            n_non_zeros += 1

        else:
            if arr[left] != 0:
                left += 1

                # we encounter a non-0 value in this case
                # increment our counter
                n_non_zeros += 1

            if arr[right] == 0:
                right -= 1

    return n_non_zeros
```

Lo and behold, we've implemented a working solution that only performs
_one_ traversal through the array that also only allocates a constant
amount of extra space! 
