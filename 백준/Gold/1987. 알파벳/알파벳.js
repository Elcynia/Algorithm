const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [R, C] = input[0].split(' ').map(Number);
const board = input.slice(1);

const dy = [-1, 0, 1, 0];
const dx = [0, 1, 0, -1];

let check = Array(26).fill(false);
let curLen = 0;
let ans = 0;

function search(y, x) {
  if (y < 0 || x < 0 || y >= R || x >= C) return;
  const charIndex = board[y][x].charCodeAt(0) - 'A'.charCodeAt(0);
  if (check[charIndex]) return;

  check[charIndex] = true;
  curLen++;

  ans = Math.max(ans, curLen);

  for (let i = 0; i < 4; i++) {
    const ny = y + dy[i];
    const nx = x + dx[i];
    search(ny, nx);
  }

  curLen--;
  check[charIndex] = false;
}

search(0, 0);
console.log(ans);
