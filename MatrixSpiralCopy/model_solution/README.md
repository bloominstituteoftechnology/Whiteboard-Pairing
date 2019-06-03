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

## Coming Up with a Strategy

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
# simply reverse the start and end indices in the `range` function
for i in range(bottom_row, top_row + 1):
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
for i in range(right_column, left_column + 1):
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
    for i in range(right_column, left_column + 1):
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
    for i in range(right_column, left_column + 1):
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
    for i in range(right_column, left_column + 1):
        # append all the elements along the bottom row
        result.append(matrix[bottom_row][i])

    return result
```


