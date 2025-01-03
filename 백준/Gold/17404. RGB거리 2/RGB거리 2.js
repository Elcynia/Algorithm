const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input[0];
const costs = input.slice(1).map((v) => v.split(' ').map(Number));
let result = Number.MAX_SAFE_INTEGER;

// 첫 집의 색을 고정 (R, G, B)
for (let color = 0; color < 3; color++) {
  const dp = Array.from({ length: N }, () => new Array(N).fill(0));

  // 첫 집 색상 고정
  dp[0][color] = costs[0][color];
  dp[0][(color + 1) % 3] = Number.MAX_SAFE_INTEGER;
  dp[0][(color + 2) % 3] = Number.MAX_SAFE_INTEGER;

  for (let i = 1; i < N; i++) {
    dp[i][0] = costs[i][0] + Math.min(dp[i - 1][1], dp[i - 1][2]);
    dp[i][1] = costs[i][1] + Math.min(dp[i - 1][0], dp[i - 1][2]);
    dp[i][2] = costs[i][2] + Math.min(dp[i - 1][0], dp[i - 1][1]);
  }

  result = Math.min(result, dp[N - 1][(color + 1) % 3], dp[N - 1][(color + 2) % 3]);
}

console.log(result);
