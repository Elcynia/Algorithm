const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const getBest = (y, x, N, matrix) => {
  let best = 0;

  // 행
  let bef = '-';
  let value = 0;
  for (let j = 0; j < N; j++) {
    if (bef === matrix[y][j]) {
      value += 1;
    } else {
      value = 1;
    }
    bef = matrix[y][j];
    best = Math.max(best, value);
  }

  // 열
  bef = '-';
  value = 0;
  for (let i = 0; i < N; i++) {
    if (bef === matrix[i][x]) {
      value += 1;
    } else {
      value = 1;
    }
    bef = matrix[i][x];
    best = Math.max(best, value);
  }

  return best;
};

const N = parseInt(input[0]);
const matrix = input.slice(1).map((line) => line.split(''));

const dy = [-1, 0, 1, 0];
const dx = [0, 1, 0, -1];

let ans = 0;

for (let y = 0; y < N; y++) {
  for (let x = 0; x < N; x++) {
    ans = Math.max(ans, getBest(y, x, N, matrix));
    for (let i = 0; i < 4; i++) {
      const ny = y + dy[i];
      const nx = x + dx[i];
      if (ny >= 0 && ny < N && nx >= 0 && nx < N) {
        if (matrix[y][x] !== matrix[ny][nx]) {
          [matrix[y][x], matrix[ny][nx]] = [matrix[ny][nx], matrix[y][x]];
          ans = Math.max(ans, getBest(y, x, N, matrix));
          // Swap back
          [matrix[y][x], matrix[ny][nx]] = [matrix[ny][nx], matrix[y][x]];
        }
      }
    }
  }
}

console.log(ans);
