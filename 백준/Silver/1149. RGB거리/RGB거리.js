const fs = require('fs');
const [[N], ...costs] = fs
  .readFileSync(0)
  .toString()
  .trim()
  .split('\n')
  .map((line) => line.split(' ').map(Number));

const dp = Array.from({ length: N }, () => new Array(N).fill(0));

dp[0][0] = costs[0][0];
dp[0][1] = costs[0][1];
dp[0][2] = costs[0][2];

for (let i = 1; i < N; i++) {
  dp[i][0] = costs[i][0] + Math.min(dp[i - 1][1], dp[i - 1][2]);
  dp[i][1] = costs[i][1] + Math.min(dp[i - 1][0], dp[i - 1][2]);
  dp[i][2] = costs[i][2] + Math.min(dp[i - 1][0], dp[i - 1][1]);
}

console.log(Math.min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]));
