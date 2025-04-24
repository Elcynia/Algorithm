const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input.shift();
const arr = input.map((line) => line.split(' ').map(Number));

// dp[y][x][dir]
// 0=가로, 1=세로, 2=대각선
const dp = Array.from({ length: N }, () => Array.from({ length: N }, () => Array(3).fill(0)));
dp[0][1][0] = 1;

for (let y = 0; y < N; y++) {
  for (let x = 0; x < N; x++) {
    if (arr[y][x] === 1) continue;

    // 가로
    if (x - 1 >= 0) {
      dp[y][x][0] += dp[y][x - 1][0] + dp[y][x - 1][2];
    }

    // 세로
    if (y - 1 >= 0) {
      dp[y][x][1] += dp[y - 1][x][1] + dp[y - 1][x][2];
    }

    // 대각선
    if (y - 1 >= 0 && x - 1 >= 0) {
      if (arr[y][x - 1] === 0 && arr[y - 1][x] === 0 && arr[y - 1][x - 1] === 0) {
        dp[y][x][2] += dp[y - 1][x - 1][0] + dp[y - 1][x - 1][1] + dp[y - 1][x - 1][2];
      }
    }
  }
}

const result = dp[N - 1][N - 1][0] + dp[N - 1][N - 1][1] + dp[N - 1][N - 1][2];
console.log(result);
