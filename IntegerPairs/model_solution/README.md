# Integer Pairs Walkthrough

## Understanding the Problem

The problem states that we want to find and print all of the pairs of values in
a given array that sum up to some input value. So for example, given an array
`[1, 4]` and input value 5, our function should print out `1 4` since those two
array values sum up to the input value. 

If we instead got an array `[9, 7]` and input value 3, our function shouldn't
print anything, since 9 and 7 don't sum up to 3. We'll also want to make sure
our function can handle an input array of just one element. 

## Coming up with a Strategy

The naive solution would be to perform a nested for loop that iterates over
every array element and performs another loop over the entire array to check if 
any of the other elements sum up to the input value. Something like this:

```python
def integer_pairs(arr, k):
    for x in arr:
        for y in arr:
            # check if x + y sums up to k
            if x + y == k:
                print(x, y)
```

Because of the nested loops that each iterate over the entire array, this
strategy exhibits an O(n^2) runtime. 

We can do better if we opt to sort the array first. That would allow us to then
perform the checking of whether two elements sum up to `k` in a single linear
pass. The pseudocode for such a strategy might look like the following:

```
def integer_pairs(arr, k):
    sort the input arr
    we'll keep two indices, one on the left side, the other on the right
    left = 0, right = len(arr) - 1
    loop so long as left and right indices haven't met 
        sum = arr[left] + arr[right]
        check if sum == k
        if it does 
            print out the two values 
            increment the left index
            decrement the right index
        if it doesn't
            figure out whether to move left or right indices
            if sum < k
                we'll want to increment the left index
            otherwise
                we'll want to decrement the right index
    if we haven't found any pairs at this point
        print("No pairs found")
```

The above implementation will yield an O(n log n) implementation due to the
sorting. The rest of the code only performs a single pass of the data, so
there's a total of two linear passes through the array. The above strategy also
only allocates a constant number of variables, so the resulting space complexity
if O(1). 

## Evaluating our Strategy (And Coming Up with a Better One)

Can we do better than this in the runtime department? Could we achieve an O(n)
runtime, perhaps at the expense of space complexity? It turns out we can.
Problems that ask us to find _complements_, i.e., two elements that somehow
combine to form some value, usually benefit from using a hash table (an Object) 
to store values we haven't seen yet while we're traversing a collection. 

In the case of this problem, we can iterate along the elements in the input
array and, if we see that `k - current_element` exists in the hash table, then
we've found the complement of `current_element` that sums up to `k`. Otherwise,
we'll want to insert the current element into the hash table because it might be
the complement of another element in the array that we just haven't reached yet
while iterating. 

Sketching the above out in code looks like this:

```python
def integer_pairs(arr, k):
    # dict where we'll store values as we're iterating
    hash = {}
    
    for elem in arr:
        # check to see if the complement of elem exists in the hash
        if k - elem in hash:
            # we've found two elements that sum up to k
            print(elem, k - elem)
        else:
            # elem doesn't have a complement in the hash
            # add it to the hash
            hash[elem] = True 
```

Nice! This strategy will yield an O(n) runtime with an O(n) space complexity,
which is generally more preferred than a solution that exhibits a slower runtime
but better space complexity. Memory is relatively plentiful and people are
impatient, after all. 

There are a few more things we need to account for, though. What if we don't
find any pairs? We want our implementation to return a "No pairs found" message
in that case. We can tack that on pretty easily by adding a flag that we'll
initialize to False and then toggle to True as soon as we've found at least a
single pair:

```python
def integer_pairs(arr, k):
    hash = {}
    found = False
    
    for elem in arr:
        if k - elem in hash:
            found = True
            print(elem, k - elem)
        else:
            hash[elem] = True 

    if not found:
        print("No pairs found")        
```

This solution will also adequately handle the case where we're handed a
single-element array as input. In that case, we should just always print "No
pairs found", which is what will happen with this implementation. 
