function solution(rows, columns, queries) {
  const res = [];
  const board = Array.from({ length: rows }, (_, i) => Array.from({ length: columns }, (_, j) => i * columns + j + 1));

  for (const query of queries) {
    const [x1, y1, x2, y2] = query.map((v) => v - 1);
    let min = Infinity;
    let prev = board[x1][y1];

    // 우측
    for (let j = y1 + 1; j <= y2; j++) {
      min = Math.min(min, prev);
      [prev, board[x1][j]] = [board[x1][j], prev];
    }

    // 아래
    for (let i = x1 + 1; i <= x2; i++) {
      min = Math.min(min, prev);
      [prev, board[i][y2]] = [board[i][y2], prev];
    }

    // 좌측
    for (let j = y2 - 1; j >= y1; j--) {
      min = Math.min(min, prev);
      [prev, board[x2][j]] = [board[x2][j], prev];
    }

    // 위
    for (let i = x2 - 1; i >= x1; i--) {
      min = Math.min(min, prev);
      [prev, board[i][y1]] = [board[i][y1], prev];
    }

    res.push(Math.min(min, prev));
  }

  return res;
}

console.log(
  solution(6, 6, [
    [2, 2, 5, 4],
    [3, 3, 6, 6],
    [5, 1, 6, 3],
  ])
);