# Sort Top Scores Walkthrough

## Understanding the Problem

This problems asks us, given that we receive the highest possible score as a
parameter to our function, can we use that fact to sort an unsorted array of
integers in faster than O(n log n) time in the worst case?

We assume any general sorting algorithm achieves an O(n log n) time in the worst
case. However, sorting algorithms have to be able to handle a wide variety of
cases, including those where there is no upper bound on the data they're
sorting. So this question is asking if we can make use of the knowledge of the
highest possible score to achieve a faster sorting runtime. 

To that end, we're looking to achieve an O(n) runtime (since there's no way to
sort data without at least looking at every element at least once). How can we
do that? How does knowing the highest possible score help us?  

## Coming up with a Strategy 

So we have an upper bound on all of the integer values that we're looking to
sort. Every element then is less than or equal to the upper bound value. Here's
an idea: since we know the upper bound, could we simply count the number of 
times every integer shows up in the unsorted array? 

For example, given the following array: `[10, 3, 9, 4, 7, 6, 8, 8, 8, 9, 3, 0, 
10, 9, 9, 0, 4, 2, 7, 1]`, where 10 is the upper bound of the array, we can 
count the number of times each element shows up in an array where each index
element in the `counts` array holds the number of times that index number shows
up in the array of unsorted data. That would look like the following:

```
[2, 1, 0, 2, 2, 0, 1, 2, 3, 4, 2]
``` 

where there are two 0s, no 2s, four 10s, etc. in the unsorted array. Then, to
yield the final array of sorted data, we would walk along the array of counts
and populate the final sorted array. 

The pseudocode for this idea looks like the following:

```
initialize a `counts` array of the range [0, highestPossibleScore]
iterate along the inputs array
for each element in the input array
    counts[element] += 1
at this point, the counts array has the counts
iterate along the counts array
for each count in counts
    append `count` number of the current index to the result array
return the result array
```

The entire crux of this strategy relies on the fact that we know the upper bound
of the data. Without this knowledge, we wouldn't be able to construct the counts
array because we wouldn't know the range of counts we'd have to allocate for it. 

## Implementing the Strategy

Turning the above pseudocode into code, it will look something like the
following:

```python
def sort_top_scores(arr, highest):
    result = []
    counts = [0 for _ range(highest)]
    for score in scores:
        counts[score] += 1
    for score in range(highest):
        count = counts[score]
        for i in range(count):
            result.append(score)
    return result
```

## Evaluating the Implementation


