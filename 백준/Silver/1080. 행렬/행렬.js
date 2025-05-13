const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, M] = input.shift().split(' ').map(Number);
const A = input.slice(0, N).map((line) => line.split('').map(Number));
const B = input.slice(N).map((line) => line.split('').map(Number));

function flip(x, y) {
  for (let i = x; i < x + 3; i++) {
    for (let j = y; j < y + 3; j++) {
      A[i][j] = A[i][j] === 0 ? 1 : 0;
    }
  }
}

function isEqual() {
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (A[i][j] !== B[i][j]) return false;
    }
  }
  return true;
}

function flipCount() {
  let count = 0;
  for (let i = 0; i <= N - 3; i++) {
    for (let j = 0; j <= M - 3; j++) {
      if (A[i][j] !== B[i][j]) {
        flip(i, j);
        count++;
      }
    }
  }
  return isEqual() ? count : -1;
}
const result = flipCount();
console.log(result);
