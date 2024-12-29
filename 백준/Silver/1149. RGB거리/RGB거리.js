const fs = require('fs');
const [[N], ...costs] = fs
  .readFileSync(0)
  .toString()
  .trim()
  .split('\n')
  .map((line) => line.split(' ').map(Number));

let dp = [costs[0][0], costs[0][1], costs[0][2]];

for (let i = 1; i < N; i++) {
  const newDp = [
    costs[i][0] + Math.min(dp[1], dp[2]),
    costs[i][1] + Math.min(dp[0], dp[2]),
    costs[i][2] + Math.min(dp[0], dp[1]),
  ];
  dp = newDp;
}

console.log(Math.min(...dp));
