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

function robotPaths(n) {
  let pathCounter = 0;
  const board = makeBoard(n);

  const traversePaths = (i, j) => {
    if (i === n - 1 && j === n - 1) {
      pathCounter++;
      return;
    }
    if (i < 0 || i >= n || j < 0 || j >= n) {
      return;
    }
    if (board.hasBeenVisited(i,j)) {
      return;
    }
    else {
      board.toggle(i, j);
      traversePaths(i, j + 1);
      traversePaths(i + 1, j);
      traversePaths(i, j - 1);
      traversePaths(i - 1, j);
      board.toggle(i, j);
    }
  };
  
  traversePaths(0, 0);
  return pathCounter;
}