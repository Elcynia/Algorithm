const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const n = +input[0];
const board = input.slice(1).map((line) => line.split(' ').map(Number));
const dy = [-1, 1, 0, 0];
const dx = [0, 0, -1, 1];
let ans = 0;

function DFS(y, x, h, visited) {
  visited[y][x] = true;
  for (let i = 0; i < 4; i++) {
    const ny = y + dy[i];
    const nx = x + dx[i];
    if (0 <= ny && ny < n && 0 <= nx && nx < n && !visited[ny][nx] && board[ny][nx] > h) {
      DFS(ny, nx, h, visited);
    }
  }
}

const maxHeight = Math.max(...board.flat());

for (let h = 0; h < maxHeight; h++) {
  const visited = Array.from({ length: n }, () => Array(n).fill(false));
  let cnt = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] > h && !visited[i][j]) {
        DFS(i, j, h, visited);
        cnt++;
      }
    }
  }
  ans = Math.max(ans, cnt);
}

console.log(ans);
