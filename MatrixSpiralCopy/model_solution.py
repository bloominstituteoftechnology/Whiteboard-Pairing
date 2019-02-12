

def spiralCopy(inputMatrix):
    numRows = len(inputMatrix)
    numCols = len(inputMatrix[0])

    # keep track of where we are along each
    # of the four sides of the matrix
    topRow = 0
    bottomRow = numRows - 1
    leftCol = 0
    rightCol = numCols - 1

    result = []
    # iterate throughout the entire matrix
    while topRow <= bottomRow and leftCol <= rightCol:
        # iterate along the top row from left to right
        for i in range(leftCol, rightCol + 1):
            result.append(inputMatrix[topRow][i])
        topRow += 1

        # iterate along the right column from top to bottom
        for i in range(topRow, bottomRow + 1):
            result.append(inputMatrix[i][rightCol])
        rightCol -= 1

        if topRow <= bottomRow:
            # iterate along the bottom row from right to left
            for i in reversed(range(leftCol, rightCol + 1)):
                result.append(inputMatrix[bottomRow][i])
            bottomRow -= 1

        if leftCol <= rightCol:
            # iterate along the left column from bottom to top
            for i in reversed(range(topRow, bottomRow + 1)):
                result.append(inputMatrix[i][leftCol])
            leftCol += 1

    return result


print(spiralCopy(
  [[1]]
  ))  # should print [1]


print(spiralCopy(
  [[1], [2]]
  ))  # should print [1, 2]


print(spiralCopy(
  [[1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20]]
  ))  # should print [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]



