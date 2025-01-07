const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const board = Array.from({ length: 9 }, (_, i) => input[i].split(' ').map(Number));

function isPossible(y, x, n) {
  // 행
  for (let c = 0; c < 9; c++) {
    if (board[y][c] === n) return false;
  }
  // 열
  for (let r = 0; r < 9; r++) {
    if (board[r][x] === n) return false;
  }
  // 사각형
  const sRow = Math.floor(y / 3) * 3;
  const sCol = Math.floor(x / 3) * 3;
  for (let r = 0; r < 3; r++) {
    for (let c = 0; c < 3; c++) {
      if (board[sRow + r][sCol + c] === n) return false;
    }
  }
  return true;
}

function search(lev) {
  if (lev === position.length) {
    board.forEach((row) => console.log(row.join(' ')));
    process.exit(0);
  }

  const [y, x] = position[lev];
  // 1 ~ 9 탐색
  for (let n = 1; n <= 9; n++) {
    if (isPossible(y, x, n)) {
      board[y][x] = n;
      search(lev + 1);
      board[y][x] = 0;
    }
  }
}

// 비어있는 위치(position) 탐색
const position = [];
for (let i = 0; i < 9; i++) {
  for (let j = 0; j < 9; j++) {
    if (board[i][j] === 0) {
      position.push([i, j]);
    }
  }
}

search(0);

/* 브루트포스는 시간 초과가 나므로 백트래킹을 이용하여 풀어야한다.
 * (브루트포스 사용 시, 9^81)
 * 백트래킹 사용 시, 9^N (0의 개수)
 */
