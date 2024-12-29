const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [nm, ...arr] = input;
const [n, m] = nm.split(' ').map(Number);
const dp = Array.from({ length: n }, () => new Array(m).fill(0));
const map = arr.map((row) => row.split(' ').map(Number));

dp[0][0] = map[0][0];

// 첫 행 초기화
for (let j = 1; j < m; j++) {
  dp[0][j] = dp[0][j - 1] + map[0][j];
}

// 첫 열 초기화
for (let i = 1; i < n; i++) {
  dp[i][0] = dp[i - 1][0] + map[i][0];
}

// 나머지 칸 계산
for (let i = 1; i < n; i++) {
  for (let j = 1; j < m; j++) {
    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + map[i][j];
  }
}

console.log(dp[n - 1][m - 1]);
