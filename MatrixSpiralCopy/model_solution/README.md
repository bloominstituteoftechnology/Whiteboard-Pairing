# Matrix Spiral Copy Walkthrough

## Understanding the Problem

This problem is asking us to traverse a matrix in spiral order, adding each of
these elements into a one-dimensional array in that order. 

Before we consider the spiral order constraint, let's start by considering how
we would traverse the matrix in left-to-right, top-to-bottom fashion. We'd start
off at coordinate [0, 0] in the upper left-hand corner. We'd traverse left until
we reached the end of the row, then we'd move on to the next row, repeating the
process of iterating along each column element until we reached the end of the
row. The code for this idea might look something like the following:

```python
def matrix_in_order_copy(matrix):
    # initialize a result array to hold the copied elements
    result = []
    # outer loop iterates along each row in the matrix
    for row in matrix:
        # inner loop iterates along each element in the row
        for elem in row:
            # add the element to the result array
            result.append(elem)
    return result
```

Ok, so we can traverse the matrix, but resulting order of the above
implementation doesn't achieve the traversal order the problem is looking for.
We need to figure out how to tailor this idea to print the elements in spiral
order, which is to say, in clockwise order starting at the top left corner and
moving from the outer layers inward towards the center. 

## Coming Up with a Strategy For a Simple Case

Let's start off with a simple matrix example and think through how we'd traverse
it in spiral order. Given the following matrix

```
[
    [1, 2],
    [3, 4]
]
```

the desired ordering we're looking for is `[1, 2, 4, 3]`. One thing to notice is
that the order in which we're iterating along the elements of the top row is the
same order with the in-order traversal example. We go from left to right. Once
we hit the end of that row, we need to start traversing down the column. How do
we traverse down a column? We do so by keeping the column index (the second
index when indexing into the matrix) constant and iterating along the rows.
Something like this:

```python
# iterate along a column from top to bottom
# we need to iterate from the index of the top row to the index of the 
# bottom row + 1 since the range function is exclusive on the end 
for i in range(top_row, bottom_row + 1):
    # only the first index varies as we iterate
    # the column index doesn't change 
    result.append(matrix[i][column_index])
```

The above pseudocode will iterate along a matrix column from top to bottom.
We'll also need to be able to traverse along columns from bottom to top. We can
achieve that with a simple change to the above pseudocode:

```python
# reverse the result of the `range` iterator function to traverse backwards
for i in reversed(range(top_row, bottom_row + 1)):
    result.append(matrix[i][column_index])
```

Just this simple change has us iterating along columns from bottom to top
(though we don't actually need this logic for the simple example). The last
direction we need to be iterate along is right to left along a row. Again, we
can do this similarly to how we iterated along columns. Instead of keeping the
column index constant, we'll instead keep the row index constant such that we're
iterating along column values. The following code achieves this:

```python
# iterate along the column indices from right to left
# we'll have to reverse this one too 
for i in reversed(range(left_column, right_column + 1)):
    # vary the column index while keeping the row index constant
    result.append(matrix[row_index][i])
```

With all that said and done, we're able to iterate along our simple example
matrix in every direction we need to (left-to-right, top-to-bottom, then
right-to-left). Let's try to come up with an implementation that solves achieves
the desired result for our simple four-element matrix.

## Implementing our Strategy

For our simple four-element matrix, we'll start off in the top left corner,
traverse right to the end of the row, then start traversing from the top of the
right column to the bottom, and then finally traverse from right to left along
the bottom row. Cobbling the code that we've come up with so far to achieve
this, we have:

```python
def matrix_spiral_copy(matrix):
    result = []
    # iterate from right to left
    for i in range(left_column, right_column + 1):
        result.append(matrix[row_index][i])
    # iterate from top to bottom
    for i in range(top_row, bottom_row + 1):
        result.append(matrix[i][column_index])
    # iterate from right to left
    for i in reversed(range(left_column, right_column + 1)):
        result.append(matrix[row_index][i])
    return result
```

As of now, this code doesn't work. We haven't defined `left_column`,
`right_column`, `top_row`, and `bottom_row`, as well as `row_index` and
`column_index`. Let's go ahead and add those variables to our implementation:

```python
def matrix_spiral_copy(matrix):
    result = []
    # left_column starts off at index 0
    left_column = 0
    # right_column is the last column of the matrix
    right_column = len(matrix[0]) - 1
    # top_row also starts off at index 0
    top_row = 0
    # bottom_row is the last row of the matrix
    bottom_row = len(matrix) - 1
    # column_index starts off as column 0
    column_index = 0
    # row_index starts off as the right-most row, since that's the
    # row where we're going to be iterating from top to bottom
    row_index = len(matrix[0]) - 1 

    for i in range(left_column, right_column + 1):
        result.append(matrix[row_index][i])
    for i in range(top_row, bottom_row + 1):
        result.append(matrix[i][column_index])
    for i in reversed(range(left_column, right_column + 1)):
        result.append(matrix[row_index][i])

    return result
```

It turns out we can consolidate the `column_index` and `row_index` variables
into the `top_row` and `right_column` variables respectively. Doing so will
yield us the following slightly cleaner implementation:

```python
def matrix_spiral_copy(matrix):
    result = []
    left_column = 0
    right_column = len(matrix[0]) - 1
    top_row = 0
    bottom_row = len(matrix) - 1

    for i in range(left_column, right_column + 1):
        # append all the elements along the top row
        result.append(matrix[top_row][i])
    for i in range(top_row, bottom_row + 1):
        # append all the elements along the right column
        result.append(matrix[i][right_column])
    for i in reversed(range(left_column, right_column + 1)):
        # append all the elements along the bottom row
        result.append(matrix[bottom_row][i])

    return result
```

However, if we go ahead and test this implementation out, we'll see that it
doesn't actually work for our simple example. This function returns `[1, 2, 2,
4]`, not the expected answer of `[1, 2, 4, 3]`. Why is this the case?

This is happening because our `top_row` variable stays at 0 such that we iterate
to the end of the top row and then start iterating along the left column while
the `top_row` variable is still 0, which means we end up printing the last
element of the top row, which is also the first element of the right column,
twice. We can fix this easily by incrementing the `top_row` variable. 

This in fact ends up being the desirable result when we generalize our
implementation to work with larger matrices. Once we've incremented along a row,
we don't need to touch it again, i.e. the new top row will be the next row down
in the matrix. We'll want to do the same thing with the bottom row and the left
and right columns too, i.e., shift them "inwards" towards the center of the
matrix after we're done traversing them. 

Updating our implementation one more time yields us the following:

```python
def matrix_spiral_copy(matrix):
    result = []
    left_column = 0
    right_column = len(matrix[0]) - 1
    top_row = 0
    bottom_row = len(matrix) - 1

    for i in range(left_column, right_column + 1):
        result.append(matrix[top_row][i])
    # move the top_row index towards the center of the matrix
    top_row += 1
    for i in range(top_row, bottom_row + 1):
        result.append(matrix[i][right_column])
    # move the right_column index towards the center of the matrix
    right_column -= 1

    for i in reversed(range(left_column, right_column + 1)):
        result.append(matrix[bottom_row][i])

    return result
```

The above implementation now works for our simple example!

## Generalizing our Strategy to Larger Matrices

Ok, now we need to figure out how to be able to handle any matrix. One thing
we'll certainly need is to be able to traverse from bottom to top along the
left-most column, along with having that column index move towards the center of
the matrix after we're done with it. Adding that logic to what we have is pretty
simple:

```python
def matrix_spiral_copy(matrix):
    result = []
    left_column = 0
    right_column = len(matrix[0]) - 1
    top_row = 0
    bottom_row = len(matrix) - 1

    for i in range(left_column, right_column + 1):
        result.append(matrix[top_row][i])
    top_row += 1
    for i in range(top_row, bottom_row + 1):
        result.append(matrix[i][right_column])
    right_column -= 1
    for i in reversed(range(left_column, right_column + 1)):
        result.append(matrix[bottom_row][i])
    # move the bottom_row index towards the center of the matrix
    bottom_row -= 1
    # iterate from bottom to top along the left column
    for i in reversed(range(top_row, bottom_row + 1)):
        result.append(matrix[i][left_column])
    left_column += 1

    return result
```

At this point, we're almost there; there's just one more crucial piece that's
missing. As of now, this code only iterates along the outer layer of a matrix.
We need to be able to traverse through all the inner layers as. How should we go
ahead and implement that?

The easiest way would probably be to throw all of our traversal logic into a
while loop. We'll keep looping until the `top_row` index reaches the
`bottom_row` index and the `left_column` index reaches the `right_column` index:

```python
def matrix_spiral_copy(matrix):
    result = []
    left_column = 0
    right_column = len(matrix[0]) - 1
    top_row = 0
    bottom_row = len(matrix) - 1
    
    while top_row <= bottom_row and left_column <= right_column:
        for i in range(left_column, right_column + 1):
            result.append(matrix[top_row][i])
        top_row += 1
        for i in range(top_row, bottom_row + 1):
            result.append(matrix[i][right_column])
        right_column -= 1
        for i in reversed(range(left_column, right_column + 1)):
            result.append(matrix[bottom_row][i])
        bottom_row -= 1
        for i in reversed(range(top_row, bottom_row + 1)):
            result.append(matrix[i][left_column])
        left_column += 1

    return result
```

If we test this implementation on the following matrix

```
[</br>
    [1, 2, 3, 4, 5],</br>
    [6, 7, 8, 9, 10],</br>
    [11, 12, 13, 14, 15],</br>
    [16, 17, 18, 19, 20],</br>
]
```

we'll see that it returns the expected result!

## Improving our Implementation

Let's try a few more test cases to make sure we haven't missed anything we
needed to account for. A single element matrix like `[[1]]` works fine. What
about a matrix that only contains one row? Something like `[[1, 2]]`. If we try
running our implementation with this matrix, we get back `[1, 2, 1]`, which
definitely isn't right. What's the problem here?

Our while loop keeps running so long as `top_row <= bottom_row` and `left_column
<= right_column`, but these variables are being updated within the body of the
while loop. So it turns out some of the traversal loops within the while loop
are running when we actually don't want them to, but the while loop alone isn't
actually able to check this since the updates are happening in the middle of an
iteration. 

More specifically, we want to explicitly check that the `top_row` index isn't
out of bounds before we run the for loop that traverses from right to left along 
the bottom row. If we don't, then our code copies elements that it thinks are
still within bounds of the matrix when we've in fact already traversed out of
the bounds of the matrix. Similarly, we also need to check that the
`left_column` index isn't out of bounds before we run the for loop that
traverses from bottom to top along the left column for the same reason.

Adding those checks to our implementation, we get:

```python
def matrix_spiral_copy(matrix):
    result = []
    left_column = 0
    right_column = len(matrix[0]) - 1
    top_row = 0
    bottom_row = len(matrix) - 1
    
    while top_row <= bottom_row and left_column <= right_column:
        for i in range(left_column, right_column + 1):
            result.append(matrix[top_row][i])
        top_row += 1
        for i in range(top_row, bottom_row + 1):
            result.append(matrix[i][right_column])
        right_column -= 1
        # check if there's still a top row we need to traverse
        if top_row <= bottom_row:
            for i in reversed(range(left_column, right_column + 1)):
                result.append(matrix[bottom_row][i])
            bottom_row -= 1
        # check if there's still a left column we need to traverse
        if left_column <= right_column:
            for i in reversed(range(top_row, bottom_row + 1)):
                result.append(matrix[i][left_column])
            left_column += 1

    return result
```

This time, when we test this implementation against the input matrix `[[1, 2]]`
we get the desired output!

## Evaluating our Implementation

The problem asks us to copy all of the elements of the input matrix, so we can't
get away from touching every single element in the matrix. So our running time
is proportional to the total number of elements in the matrix, which is given by
the height of the matrix * the width. Hence the running time of our algorithm is
O(n * m). 

For the space complexity, we're copying every matrix element into another array,
such that the total amount of extra memory we're consuming is proportional to
the total number of matrix elements, so the space complexity is also O(n * m).
This is fine in this case since the problem is specifically asking us to copy
the matrix elements into another array. 
