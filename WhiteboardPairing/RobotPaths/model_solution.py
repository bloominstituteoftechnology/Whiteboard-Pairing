def makeBoard(n):
  board = []
  for i in range(0, n):
    board.append([])
    for j in range(0, n):
      board[i].append(False)

  return board
  
  
def robotPaths(n):
  robotPaths.pathCounter = 0
  board = makeBoard(n)
  
  hasBeenVisited = lambda i, j: board[i][j]

  def traversePaths(i, j): 
    if i == n - 1 and j == n - 1:
      robotPaths.pathCounter  += 1
      return

    if i < 0 or i >= n or j < 0 or j >= n:
      return

    if hasBeenVisited(i,j):
      return
  
    else:
      board[i][j] = not board[i][j]
      traversePaths(i, j + 1)
      traversePaths(i + 1, j)
      traversePaths(i, j - 1)
      traversePaths(i - 1, j)
      board[i][j] = not board[i][j]
  
  traversePaths(0, 0)
  
  return robotPaths.pathCounter
  
  
# Some tests
print(robotPaths(2))   # Should print 2
print(robotPaths(3))   # Should print 12
print(robotPaths(4))   # Should print 184
