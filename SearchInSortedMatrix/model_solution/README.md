# Search In Sorted Matrix Walkthrough

## Understanding the Problem

The first thing that should be jumping at when reading the prompt for the
problem is the fact that the rows and columns of the matrix are already sorted.
Of course, we could iterate through every element in the matrix one by one,
going from left to right and then top to bottom, checking every element to see
if we've found the matching element. In the worst case, this would yield us a
runtime of O(n * m) where n is the number of rows and m is the number of
columns. If we had a square matrix where the number of rows and columns is the
same, this would be the same as O(n^2). That solution would look something like
this:

```python
def search_in_sorted_matrix(matrix, target):
    # iterate along each row
    for row in range(len(matrix)):
        # iterate along each column
        for col in range(len(matrix[0])):
            if matrix[row][col] == target:
                return [row, col]
    # we iterated through the whole matrix and didn't find the target
    return (-1, -1)
```

If our matrix was unsorted, this would most likely be the best we could do,
since we don't know anything about the order of the elements in an unsorted
matrix. However, in this case, since the matrix is sorted, we can take advantage
of this fact to achieve a more performant algorithm. 

## Coming up with a Strategy

When we're handed a problem where the data is already sorted, one of the first
questions we should be asking is if we can utilize binary search in some way for
this problem. The binary search algorithm is typically used on already-sorted or
almost-sorted one-dimensional arrays. Can we utilize the same idea to search
through a sorted matrix? 

To reiterate on the binary search algorithm, we start off by calculating the
midpoint of the array we're searching through, then we check to see if the
midpoint element of the array is less than, equal to, or greater than our target
element. If the midpoint element is equal to the target element, then great,
we're done! If the midpoint element is less than the target element, then we
know, by virtue of the fact that the data is already sorted, that it must exist
in the right half of the sorted array (if it exists in the array in the
first place). Similarly, if the midpoint element is greater than the target 
element, then we know that the target element must exist in the left half of the 
sorted array (again, if it exists in the array in the first place).

So how can we apply this idea to a sorted matrix? Let's consider an example.
Let's say we have the following sorted matrix:

```
[
    [1,  4,  7,   12,  15,  997,  999],
    [2,  5,  19,  32,  35,  1001, 1007],
    [4,  8,  24,  34,  36,  1008, 1015],
    [40, 41, 42,  44,  45,  1018, 1020],
    [98, 99, 101, 104, 190, 1021, 1025],
]
```

How would we go about trying to find 41 in this sorted matrix? The binary search
algorithm prescribes first finding the midpoint, so let's try that with our
matrix. In this example, the midpoint is the element in the middle column and
middle row, which in this case is the element located at row 2 column 3, or 34.
41 is greater than 34. What does that tell us? Well, it tells us that if 41
exists in the matrix, it's either in a column to the right of column 3, or it's
in a row lower than row 2. But how do we know in which dimension to continue
searching from this point, rows or columns? 

With the information we currently have, it's not really clear. In this case,
perhaps starting at the midpoint of the matrix doesn't work out so well as
starting at the midpoint in a one-dimensional array. So if we're not going to
start in the midpoint, where should we start instead? 

What if we tried starting in one of the corners? Let's try the northwest corner.
The element there, 1, is less than 41. Ok, what does that tell us? Well, not
much, since 41 could still be to the right of 1 or underneath it, since it's
larger. So that was even less helpful than starting at the midpoint. 

Ok, let's try the northeast corner. The element there, 999, is larger than 41,
is located at coordinates [0, 6], row 0 and column 6. Now, we know that 41 must 
be in a column to the right of column 6, since every element directly underneath 
999 is greater than it. Ok, let's keep going. If we shift over one column to the 
left, we're now at coordinates [0, 5], which is where 997 is located. Again, 997 
is larger than 41, so we can continue shifting to the left since we know that 41
can't be located directly underneath 997; all of those elements are larger than
997. 

Shifting over to the left one more time, we end up at coordinates [0, 4], where
15 is located. At this point, 15 is less than 41, so it could certainly be
directly underneath 15 in column 4. But now we know that 41 cannot be in this
row, since it would have been between elements 15 and 997. Thus, we can move on
to the next row in the matrix. This takes us to coordinates [1, 4], where 35 is
located. 35 is less than 41, so 41 cannot exist in this row either. We keep
moving down to [2, 4]. Again, 36 is less than 41, so it can't exist in this row.
Moving down one more time to [3, 4], we land on 45. Since 45 is greater than 41,
it _can_ exist in this row. 

Since    45 is greater than 41, we move leftward to [3, 3]. 44 is greater than 41,
so we continue moving leftward, where we get to [3, 2] and see that we need to
move leftward again. Finally, at [3, 1], we find 41. 

So starting in the northeast corner worked because it gave us more information
as to which direction we could be moving as we searched through the matrix. This
same idea works just as well if we start in the southwest corner, but it would
not work if we started in the southeast corner for the same reasons it didn't
work when we tried starting in the northwest corner. We need to start at the
large end of one of the dimensions and the small end of the other. It doesn't
work when we start at the small end of both dimensions or the large end of both
dimensions. 

With that being said, does this strategy work when we try searching for an
element that isn't in the matrix? Let's see what happens when we try searching
for 1016 in the matrix. Starting at the northeast corner again, we'd see that
999 is less than 1016, so we'd move one row down to [1, 6]. From there, we'd
move down again to [2, 6], then down again to [3, 6]. We'd start moving leftward
from there until we hit [3, 4], where we'd noticed that we'd have skipped over
1016 if it existed in the matrix. Therefore, 1016 can't exist in the matrix and
we'd return [-1, -1]. 

## Evaluating this Strategy

Let's the evaluate the time complexity for this algorithm. In the worst case,
the element we're looking for would be located in the opposite corner as the one
we started at. In that case, how many elements would we need to check? In that
case, we'd have to traverse both the width and the height of the entire matrix
to get to the opposite corner. So the total number of elements we'd end up
inspecting in that situation is equal to the number of columns plus the number
of rows. Thus, the runtime of this algorithm will be O(n + m) where n is the
number of rows and m is the number of columns. This is certainly a much better
runtime than O(n * m). Can we do even better? Probably not, since doing any
better than this would entail not checking every row and column at least once in
the worst case, and we don't have enough information to be able to make that
assumption.

For the space complexity of this algorithm, we don't need to allocate memory for
any data structures or anything like that. All we need to keep track of is the
current coordinates of where we are in the matrix as we're traversing it, so the
space complexity of this algorithm will be O(1). 

## Implementing the Strategy

Now that we've sketched out the idea and determined that it's the best we can
do, let's put it down in code:

```python
def search_in_sorted_matrix(matrix, target):
    # initialize variables to keep track of where we are in the matrix
    # we want to start in the northeast (or southwest) corner
    # which has the coordinates [0, len(matrix[0])-1] 
    row = 0
    col = len(matrix[0]) - 1
    # we'll traverse so long as the row index < len(matrix) and the
    # column index >= 0
    while row < len(matrix) and col >= 0:
        # check if the value at these coordinates is > target
        if matrix[row][col] > target:
            # if it is, shift one column to the left
            col -= 1
        # check if the value at these coordinates is < target
        elif matrix[row][col] < target:
            # if it is, shift down one row
            row += 1
        # otherwise, the value at these coordinates is == target
        else:
            # we've found the element, return its coordinates
            return (row, col)
    # we've traversed the entire matrix and didn't find the matching element
    return (-1, -1)
```
