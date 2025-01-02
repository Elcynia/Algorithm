const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [R, C] = input[0].split(' ').map(Number);
const dy = [-1, 1, 0, 0];
const dx = [0, 0, -1, 1];
const board = [];
const visited = new Set();
let cnt = 1;

for (let i = 1; i <= R; i++) {
  board.push(input[i].split(''));
}

function DFS(y, x, count) {
  cnt = Math.max(cnt, count);

  for (let i = 0; i < 4; i++) {
    const ny = dy[i] + y;
    const nx = dx[i] + x;
    if (ny < 0 || ny >= R || nx < 0 || nx >= C) continue;
    const next = board[ny][nx];
    if (!visited.has(next)) {
      visited.add(next);
      DFS(ny, nx, count + 1);
      visited.delete(next);
    }
  }
}

visited.add(board[0][0]);
DFS(0, 0, 1);
console.log(cnt);
