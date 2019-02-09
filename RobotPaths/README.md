# Robot Paths

Let's say a robot is located at the top-left corner of an n x n grid. The robot can move either up, down, left, or right, one space at a time. It also cannot visit the same spot twice. The robot is trying to reach the bottom-right corner of the grid. 

Write a function to count the number of ways that the robot can reach the bottom-right corner of the grid. Your function should receive `n` (the size of the grid) as a parameter. 

A board can be generated using this function:
```js
function makeBoard(n) {
  let board = [];
  for (let i = 0; i < n; i++) {
    board.push([]);
    for (let j = 0; j < n; j++) {
      board[i].push(false);
    }
  }
  board.toggle = (i, j) => {
    board[i][j] = !board[i][j];
  };
  board.hasBeenVisited = (i, j) => {
    return board[i][j];
  };
  return board;
}
```

## Example

`robotPaths(3)` should create a 3 X 3 board, count the following paths, and return `12`

| S |   |   |
|---|---|---|
| 1 |   |   |
| 2 | 3 | E |

| S |   |   |
|---|---|---|
| 1 | 4 | 5 |
| 2 | 3 | E |

| S | 5 | 6 |
|---|---|---|
| 1 | 4 | 7 |
| 2 | 3 | E |

| S |   |   |
|---|---|---|
| 1 | 2 | 3 |
|   |   | E |

| S | 3 | 4 |
|---|---|---|
| 1 | 2 | 5 |
|   |   | E |

| S |   |   |
|---|---|---|
| 1 | 2 |   |
|   | 3 | E |

| S | 1 | 2 |
|---|---|---|
|   |   | 3 |
|   |   | E |

| S | 1 | 2 |
|---|---|---|
|   | 4 | 3 |
|   | 5 | E |

| S | 1 | 2 |
|---|---|---|
| 5 | 4 | 3 |
| 6 | 7 | E |

| S | 1 |   |
|---|---|---|
|   | 2 |  |
|   | 3 | E |

| S | 1 |   |
|---|---|---|
| 3 | 2 |   |
| 4 | 5 | E |

| S | 1 |   |
|---|---|---|
|   | 2 | 3 |
|   |   | E |
